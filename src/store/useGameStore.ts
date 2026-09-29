import { create } from 'zustand';
import { DungeonTopic, GameScreen, PlayerStats, CombatLog } from '../types/game';
import { Problem } from '../types/problem';
import { VisualizerFrame } from '../types/visualizer';
import { ExecutionReport } from '../engine/runner';
import {
  loadProblem,
  prefetchProblems,
  generateDungeonRunCatalog,
  defaultInitialProblem,
  initialCatalogRun,
  CatalogEntry,
} from '../data/problems/loader';
import { sfx } from '../engine/sfx';

export function getStarterCode(problem: Problem, lang: 'python' | 'javascript'): string {
  if (lang === 'python') {
    return problem.python?.starterCode || `def ${problem.functionName}(*args):\n    pass\n`;
  }
  return problem.starterCode;
}

export function getSolutionCode(problem: Problem, lang: 'python' | 'javascript'): string {
  if (lang === 'python') {
    return problem.python?.solutionCode || `def ${problem.functionName}(*args):\n    pass\n`;
  }
  return problem.solutionCode;
}

export interface FloatingText {
  id: string;
  text: string;
  color: string;
}

interface GameState {
  // Screens & Navigation
  screen: GameScreen;
  previousScreen: GameScreen;
  setScreen: (screen: GameScreen) => void;
  closeShop: () => void;

  // Player Stats
  stats: PlayerStats;
  
  // Dungeon & Run State
  currentWing: DungeonTopic;
  currentFloor: number;
  currentRunCatalog: CatalogEntry[];
  currentRunProblems: (CatalogEntry | Problem)[];
  currentProblem: Problem;
  isLoadingProblem: boolean;
  monsterHp: number;
  maxMonsterHp: number;
  unlockedFloors: Record<DungeonTopic, number>;

  // Combat Animations & Logs
  heroAnim: 'idle' | 'attack' | 'cast' | 'hurt';
  monsterAnim: 'idle' | 'attack' | 'hurt' | 'defeated';
  screenShake: boolean;
  floatingTexts: FloatingText[];
  combatLogs: CombatLog[];

  // Code Editor & Runner
  language: 'python' | 'javascript';
  setLanguage: (lang: 'python' | 'javascript') => void;
  code: string;
  isRunning: boolean;
  lastReport: ExecutionReport | null;
  activeTestCaseId: number;

  // Visualizer Timeline Playback
  frames: VisualizerFrame[];
  currentFrameIndex: number;
  isPlayingTimeline: boolean;
  playbackSpeed: number;

  // Actions
  selectWing: (wing: DungeonTopic) => void;
  selectFloor: (floor: number) => void;
  setCode: (code: string) => void;
  setRunning: (isRunning: boolean) => void;
  setExecutionReport: (report: ExecutionReport) => void;
  setActiveTestCaseId: (tcId: number) => void;
  
  // Combat triggers
  takePlayerDamage: (damageHp?: number) => void;
  takeSacrificeHealth: (amount: number, reason: string) => boolean;
  healPlayer: (amount?: number) => void;
  usePotion: () => void;
  buyPotion: () => void;
  hitMonster: (damageCount?: number) => void;
  advanceFloor: () => void;
  restartRunOnPermadeath: () => void;
  addCombatLog: (sender: 'hero' | 'monster' | 'system', message: string, type: CombatLog['type']) => void;

  // Timeline
  setCurrentFrameIndex: (idx: number) => void;
  togglePlayTimeline: () => void;
  setPlaybackSpeed: (speed: number) => void;
  stepForward: () => void;
  stepBackward: () => void;
}

const initialRun = initialCatalogRun;
const initialProblem = defaultInitialProblem;

export const useGameStore = create<GameState>((set, get) => ({
  screen: 'map',
  previousScreen: 'map',
  setScreen: (screen) => {
    const current = get().screen;
    if (current === screen) return;
    set({
      previousScreen: current !== 'shop' && current !== 'victory' && current !== 'gameover' ? current : get().previousScreen,
      screen,
    });
  },
  closeShop: () => {
    const { previousScreen } = get();
    set({ screen: previousScreen || 'map' });
  },

  stats: {
    maxHp: 100,
    hp: 100,
    shield: 0,
    shieldPassedCount: 0,
    gold: 50,
    level: 1,
    xp: 0,
    potions: 2,
    totalSolved: 0,
  },

  currentWing: 'data-structures',
  currentFloor: 1,
  currentRunCatalog: initialRun,
  currentRunProblems: initialRun,
  currentProblem: initialProblem,
  isLoadingProblem: false,
  monsterHp: initialProblem.testCases.length,
  maxMonsterHp: initialProblem.testCases.length,
  unlockedFloors: {
    'data-structures': 1,
    'backtracking': 1,
    'graphs': 1,
    'binary-search-greedy': 1,
    'bit-manipulation': 1,
  },

  heroAnim: 'idle',
  monsterAnim: 'idle',
  screenShake: false,
  floatingTexts: [],
  combatLogs: [
    {
      id: 'log-0',
      sender: 'system',
      message: 'You entered the Vault of Data Structures! Solve the algorithm challenge to strike down the monster.',
      type: 'info',
      timestamp: Date.now(),
    },
  ],

  language: 'python',
  setLanguage: (lang) => {
    const { currentProblem } = get();
    set({
      language: lang,
      code: getStarterCode(currentProblem, lang),
      lastReport: null,
    });
  },

  code: getStarterCode(initialProblem, 'python'),
  isRunning: false,
  lastReport: null,
  activeTestCaseId: 1,

  frames: initialProblem.generateDefaultFrames(initialProblem.testCases[0]),
  currentFrameIndex: 0,
  isPlayingTimeline: false,
  playbackSpeed: 1,

  selectWing: async (wing) => {
    const runCatalog = generateDungeonRunCatalog(wing);
    const floor = 1;
    const entry = runCatalog[0];
    const { language } = get();

    set((s) => ({
      currentWing: wing,
      currentFloor: floor,
      currentRunCatalog: runCatalog,
      currentRunProblems: runCatalog,
      isLoadingProblem: true,
      monsterHp: entry.monster.maxHp,
      maxMonsterHp: entry.monster.maxHp,
      lastReport: null,
      heroAnim: 'idle',
      monsterAnim: 'idle',
      previousScreen: 'map',
      screen: 'battle',
      stats: {
        ...s.stats,
        hp: s.stats.maxHp, // Restores hero to 100 HP for the new journey!
        shield: 0,
        shieldPassedCount: 0,
      },
      combatLogs: [
        {
          id: `log-${Date.now()}`,
          sender: 'system',
          message: `Arrived at ${entry.title}. ${entry.monster.name} emerges! 10 floors await you in this wing.`,
          type: 'info',
          timestamp: Date.now(),
        },
      ],
    }));

    try {
      const problem = await loadProblem(entry.id);
      set({
        currentProblem: problem,
        isLoadingProblem: false,
        code: getStarterCode(problem, language),
        monsterHp: problem.testCases.length,
        maxMonsterHp: problem.testCases.length,
        activeTestCaseId: problem.testCases[0].id,
        frames: problem.generateDefaultFrames(problem.testCases[0]),
        currentFrameIndex: 0,
        isPlayingTimeline: false,
      });

      // Asynchronously prefetch remaining floors in the background
      prefetchProblems(runCatalog.slice(1).map((e) => e.id));
    } catch (err) {
      console.error('Failed to load problem:', err);
      set({ isLoadingProblem: false });
    }
  },

  selectFloor: async (floor) => {
    const { currentRunCatalog, language } = get();
    const entry = currentRunCatalog[floor - 1];
    if (!entry) return;

    set({
      currentFloor: floor,
      isLoadingProblem: true,
      monsterHp: entry.monster.maxHp,
      maxMonsterHp: entry.monster.maxHp,
      lastReport: null,
      heroAnim: 'idle',
      monsterAnim: 'idle',
      screen: 'battle',
    });

    try {
      const problem = await loadProblem(entry.id);
      set({
        currentProblem: problem,
        isLoadingProblem: false,
        code: getStarterCode(problem, language),
        monsterHp: problem.testCases.length,
        maxMonsterHp: problem.testCases.length,
        activeTestCaseId: problem.testCases[0].id,
        frames: problem.generateDefaultFrames(problem.testCases[0]),
        currentFrameIndex: 0,
        isPlayingTimeline: false,
      });
    } catch (err) {
      console.error('Failed to load floor problem:', err);
      set({ isLoadingProblem: false });
    }
  },

  setCode: (code) => set({ code }),
  setRunning: (isRunning) => set({ isRunning }),

  setExecutionReport: (report) => {
    const { currentProblem, stats, addCombatLog } = get();

    // Mode 'run': safe test run on sample cases without combat damage
    if (report.mode === 'run') {
      const activeTest = report.results.find((r) => !r.passed) || report.results[0];
      set({
        lastReport: report,
        activeTestCaseId: activeTest ? activeTest.testCaseId : 1,
        frames: activeTest ? activeTest.frames : [],
        currentFrameIndex: 0,
        isPlayingTimeline: true,
      });

      if (report.allPassed) {
        sfx.playStep();
        addCombatLog(
          'system',
          `[SAMPLE RUN] All ${report.passCount} sample test cases passed! Click ATTACK to strike the monster.`,
          'info'
        );
      } else {
        sfx.playHit();
        addCombatLog(
          'system',
          `[SAMPLE RUN] ${report.passCount}/${report.totalCount} sample test cases passed. Debug your code in the visualizer.`,
          'damage'
        );
      }
      return;
    }

    // Mode 'submit': full grading suite drives monster combat!
    if (report.allPassed) {
      // Hero attacks and defeats monster!
      sfx.playAttack();
      setTimeout(() => sfx.playMonsterHit(), 150);

      // Hero attack animation
      set((s) => ({
        heroAnim: 'cast',
        monsterAnim: 'hurt',
        monsterHp: 0,
        stats: {
          ...s.stats,
          gold: s.stats.gold + 30 * s.currentFloor,
          xp: s.stats.xp + 50 * s.currentFloor,
          totalSolved: s.stats.totalSolved + 1,
        },
        floatingTexts: [
          ...s.floatingTexts,
          { id: String(Date.now()), text: 'CRITICAL SPELL HIT!', color: '#38bdf8' },
        ],
      }));

      addCombatLog('hero', `All ${report.passCount} test cases passed! Hero unleashed a fatal logic spell.`, 'critical');

      setTimeout(() => {
        set({ heroAnim: 'idle', monsterAnim: 'defeated' });
        sfx.playVictory();
        set({ screen: 'victory' });
      }, 1200);

    } else {
      // Failed test case or error: Monster retaliates!
      sfx.playHit();
      const failCount = report.totalCount - report.passCount;
      const passCount = report.passCount;
      const monster = currentProblem.monster;

      // Base monster damage: 30 HP
      const baseDamage = 30;

      // Each passed test case generates shield reduction!
      // Shield reduction: up to 75% max (e.g. 1/3 = 25%, 2/3 = 50%, etc.)
      const maxReduction = 0.75;
      const shieldRatio = report.totalCount > 0 ? (passCount / report.totalCount) * maxReduction : 0;
      const rawDamage = Math.round(baseDamage * (1 - shieldRatio));

      // Requirement: "just reduce, not make the damage 0"
      const finalDamage = Math.max(6, rawDamage);
      const damageBlocked = Math.max(0, baseDamage - finalDamage);
      const shieldPercent = Math.round(shieldRatio * 100);

      set((s) => ({
        stats: {
          ...s.stats,
          shield: shieldPercent,
          shieldPassedCount: passCount,
        },
        monsterAnim: 'attack',
        heroAnim: 'hurt',
        screenShake: true,
        floatingTexts: [
          ...s.floatingTexts,
          {
            id: String(Date.now()),
            text: damageBlocked > 0
              ? `-${finalDamage} HP (🛡️ Blocked ${damageBlocked}!)`
              : `-${finalDamage} HP (${monster.attackName})`,
            color: damageBlocked > 0 ? '#38bdf8' : '#ef4444',
          },
        ],
      }));

      addCombatLog(
        'monster',
        damageBlocked > 0
          ? `${monster.name} attacks with ${monster.attackName} (30 DMG). Your ${passCount} passed test cases created a magical shield blocking ${damageBlocked} DMG! You take ${finalDamage} HP.`
          : `${monster.name} strikes with ${monster.attackName} dealing ${finalDamage} HP damage! (${failCount} tests failed)`,
        'damage'
      );

      setTimeout(() => {
        set({ heroAnim: 'idle', monsterAnim: 'idle', screenShake: false });
        get().takePlayerDamage(finalDamage);
      }, 500);
    }

    // Set frames from first failing test or test 1
    const activeTest = report.results.find((r) => !r.passed) || report.results[0];
    if (activeTest) {
      set({
        lastReport: report,
        activeTestCaseId: activeTest.testCaseId,
        frames: activeTest.frames,
        currentFrameIndex: 0,
        isPlayingTimeline: true,
      });
    }
  },

  setActiveTestCaseId: (tcId) => {
    const { lastReport, currentProblem } = get();
    if (lastReport) {
      const res = lastReport.results.find((r) => r.testCaseId === tcId);
      if (res) {
        set({
          activeTestCaseId: tcId,
          frames: res.frames,
          currentFrameIndex: 0,
        });
        return;
      }
    }
    const tc = currentProblem.testCases.find((t) => t.id === tcId);
    if (tc) {
      set({
        activeTestCaseId: tcId,
        frames: currentProblem.generateDefaultFrames(tc),
        currentFrameIndex: 0,
      });
    }
  },

  takePlayerDamage: (damageHp = 25) => {
    const { stats, addCombatLog } = get();
    const newHp = Math.max(0, stats.hp - damageHp);

    set({
      stats: { ...stats, hp: newHp },
    });

    if (newHp === 0) {
      // Roguelike Permadeath!
      sfx.playGameOver();
      addCombatLog('system', 'Hero fell in combat! The dungeon claims another soul. Permadeath triggered.', 'defeat');
      setTimeout(() => {
        set({ screen: 'gameover' });
      }, 700);
    }
  },

  takeSacrificeHealth: (amount: number, reason: string) => {
    const { stats, addCombatLog } = get();
    // Safety check: Cannot sacrifice HP if it would kill the player (must have at least 1 HP remaining)
    if (stats.hp <= amount) {
      addCombatLog(
        'system',
        `Cannot sacrifice HP for ${reason}! You have ${stats.hp} HP remaining (requires at least ${amount + 1} HP).`,
        'info'
      );
      return false;
    }

    const newHp = stats.hp - amount;
    const textId = String(Date.now() + Math.random());
    set((s) => ({
      stats: { ...s.stats, hp: newHp },
      heroAnim: 'hurt',
      floatingTexts: [
        ...s.floatingTexts,
        { id: textId, text: `-${amount} HP (${reason})`, color: '#f87171' },
      ],
    }));

    sfx.playHit();
    addCombatLog('hero', `Hero sacrificed ${amount} HP for ${reason}! (${newHp}/${stats.maxHp} HP)`, 'damage');

    setTimeout(() => {
      if (get().heroAnim === 'hurt') {
        set({ heroAnim: 'idle' });
      }
    }, 400);

    setTimeout(() => {
      set((s) => ({
        floatingTexts: s.floatingTexts.filter((t) => t.id !== textId),
      }));
    }, 1500);

    return true;
  },

  healPlayer: (amount = 35) => {
    const { stats } = get();
    const newHp = Math.min(stats.maxHp, stats.hp + amount);
    set({
      stats: { ...stats, hp: newHp },
    });
  },

  usePotion: () => {
    const { stats, addCombatLog } = get();
    if (stats.potions > 0 && stats.hp < stats.maxHp) {
      sfx.playCoin();
      const healAmount = 35;
      const newHp = Math.min(stats.maxHp, stats.hp + healAmount);
      const restored = newHp - stats.hp;
      set((s) => ({
        stats: {
          ...s.stats,
          potions: s.stats.potions - 1,
          hp: newHp,
        },
        floatingTexts: [
          ...s.floatingTexts,
          { id: String(Date.now()), text: `+${restored} HP! 🧪`, color: '#34d399' },
        ],
      }));
      addCombatLog('hero', `Hero drank a Health Potion, recovering ${restored} HP! (${newHp}/${stats.maxHp} HP)`, 'heal');
    }
  },

  buyPotion: () => {
    const { stats } = get();
    const cost = 40;
    if (stats.gold >= cost) {
      sfx.playCoin();
      set({
        stats: {
          ...stats,
          gold: stats.gold - cost,
          potions: stats.potions + 1,
        },
      });
    }
  },

  hitMonster: (damage = 1) => {
    set((s) => ({
      monsterHp: Math.max(0, s.monsterHp - damage),
    }));
  },

  advanceFloor: async () => {
    const { currentWing, currentFloor, unlockedFloors, language, currentRunCatalog } = get();
    const nextFloor = currentFloor + 1;
    if (nextFloor <= 10) {
      const nextEntry = currentRunCatalog[nextFloor - 1];
      if (nextEntry) {
        set({
          currentFloor: nextFloor,
          isLoadingProblem: true,
          unlockedFloors: {
            ...unlockedFloors,
            [currentWing]: Math.max(unlockedFloors[currentWing] || 1, nextFloor),
          },
          monsterHp: nextEntry.monster.maxHp,
          maxMonsterHp: nextEntry.monster.maxHp,
          lastReport: null,
          heroAnim: 'idle',
          monsterAnim: 'idle',
          screen: 'battle',
        });

        try {
          const nextProblem = await loadProblem(nextEntry.id);
          set({
            currentProblem: nextProblem,
            isLoadingProblem: false,
            code: getStarterCode(nextProblem, language),
            monsterHp: nextProblem.testCases.length,
            maxMonsterHp: nextProblem.testCases.length,
            activeTestCaseId: nextProblem.testCases[0].id,
            frames: nextProblem.generateDefaultFrames(nextProblem.testCases[0]),
            currentFrameIndex: 0,
          });
        } catch (err) {
          console.error('Failed to advance floor problem:', err);
          set({ isLoadingProblem: false });
        }
      }
    } else {
      // Completed all 10 floors of this wing! Return to map
      set({ screen: 'map' });
    }
  },

  restartRunOnPermadeath: async () => {
    // Permadeath reset: full health, re-roll fresh 10 problems for current wing starting at Floor 1!
    const { currentWing, language } = get();
    const freshRun = generateDungeonRunCatalog(currentWing);
    const floor1Entry = freshRun[0];

    set((s) => ({
      screen: 'battle',
      currentFloor: 1,
      currentRunCatalog: freshRun,
      currentRunProblems: freshRun,
      isLoadingProblem: true,
      lastReport: null,
      heroAnim: 'idle',
      monsterAnim: 'idle',
      stats: {
        ...s.stats,
        hp: s.stats.maxHp, // Restored 100 HP to try again
        shield: 0,
        shieldPassedCount: 0,
      },
      combatLogs: [
        {
          id: `log-${Date.now()}`,
          sender: 'system',
          message: 'Reborn at Floor 1! The dungeon re-aligns its challenges with a fresh randomized run. Rise again!',
          type: 'info',
          timestamp: Date.now(),
        },
      ],
    }));

    try {
      const floor1Problem = await loadProblem(floor1Entry.id);
      set({
        currentProblem: floor1Problem,
        isLoadingProblem: false,
        code: getStarterCode(floor1Problem, language),
        monsterHp: floor1Problem.testCases.length,
        maxMonsterHp: floor1Problem.testCases.length,
        activeTestCaseId: floor1Problem.testCases[0].id,
        frames: floor1Problem.generateDefaultFrames(floor1Problem.testCases[0]),
        currentFrameIndex: 0,
      });

      prefetchProblems(freshRun.slice(1).map((e) => e.id));
    } catch (err) {
      console.error('Failed to restart run problem:', err);
      set({ isLoadingProblem: false });
    }
  },

  addCombatLog: (sender, message, type) => {
    set((s) => ({
      combatLogs: [
        {
          id: `log-${Date.now()}-${Math.random()}`,
          sender,
          message,
          type,
          timestamp: Date.now(),
        },
        ...s.combatLogs.slice(0, 40),
      ],
    }));
  },

  setCurrentFrameIndex: (idx) => {
    sfx.playStep();
    set({ currentFrameIndex: idx });
  },

  togglePlayTimeline: () => set((s) => ({ isPlayingTimeline: !s.isPlayingTimeline })),

  setPlaybackSpeed: (speed) => set({ playbackSpeed: speed }),

  stepForward: () => {
    const { currentFrameIndex, frames } = get();
    if (currentFrameIndex < frames.length - 1) {
      sfx.playStep();
      set({ currentFrameIndex: currentFrameIndex + 1 });
    }
  },

  stepBackward: () => {
    const { currentFrameIndex } = get();
    if (currentFrameIndex > 0) {
      sfx.playStep();
      set({ currentFrameIndex: currentFrameIndex - 1 });
    }
  },
}));
