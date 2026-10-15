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
import { useAuthStore } from './useAuthStore';
import {
  apiRecordSubmission,
  apiSaveDungeonRun,
  apiGetActiveRuns,
  apiAbandonDungeonRun,
} from '../services/api';

export function getStarterCode(problem: Problem, lang: 'python' | 'javascript' = 'python'): string {
  if (lang === 'python' || !problem.starterCode) {
    return problem.python?.starterCode || `def ${problem.functionName}(*args):\n    pass\n`;
  }
  return problem.starterCode;
}

export function getSolutionCode(problem: Problem, lang: 'python' | 'javascript' = 'python'): string {
  if (lang === 'python' || !problem.solutionCode) {
    return problem.python?.solutionCode || `def ${problem.functionName}(*args):\n    pass\n`;
  }
  return problem.solutionCode;
}

export interface FloatingText {
  id: string;
  text: string;
  color: string;
}

export interface SavedWingRun {
  wingId: DungeonTopic;
  currentFloor: number;
  maxFloorReached: number;
  currentRunCatalog: CatalogEntry[];
  currentProblemId: string;
  code?: string;
  language?: 'python' | 'javascript';
  hp?: number;
  maxHp?: number;
  gold?: number;
  potions?: number;
  monsterHp?: number;
  maxMonsterHp?: number;
  status: 'in_progress' | 'completed' | 'abandoned';
  isSolutionUsedForProblem?: boolean;
  updatedAt?: number;
}

interface GameState {
  // Screens & Navigation
  screen: GameScreen;
  previousScreen: GameScreen;
  setScreen: (screen: GameScreen, pushHistory?: boolean) => void;
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
  isSolutionUsedForProblem: boolean;
  setIsSolutionUsedForProblem: (used: boolean) => void;

  // Active in-progress runs by wing
  activeWingRuns: Record<string, SavedWingRun>;
  startNewRun: (wing: DungeonTopic) => Promise<void>;
  continueRun: (wing: DungeonTopic) => Promise<void>;
  syncActiveRunsFromDatabase: () => Promise<void>;

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
  restoreSession: () => Promise<void>;
}

const initialRun = initialCatalogRun;
const initialProblem = defaultInitialProblem;

const defaultStats: PlayerStats = {
  maxHp: 100,
  hp: 100,
  shield: 0,
  shieldPassedCount: 0,
  gold: 50,
  level: 1,
  xp: 0,
  potions: 2,
  totalSolved: 0,
};

const defaultUnlockedFloors: Record<DungeonTopic, number> = {
  'data-structures': 1,
  'backtracking': 1,
  'graphs': 1,
  'binary-search-greedy': 1,
  'bit-manipulation': 1,
  'security-sectors-trial': 1,
  'maximum-parentheses-trial': 1,
};

const SESSION_STORAGE_KEY = 'algo_dungeon_game_session';
const ACTIVE_RUNS_STORAGE_KEY = 'algo_dungeon_active_wings';

interface PersistedGameSession {
  screen?: GameScreen;
  previousScreen?: GameScreen;
  currentWing?: DungeonTopic;
  currentFloor?: number;
  currentRunCatalog?: CatalogEntry[];
  currentProblemId?: string;
  code?: string;
  language?: 'python' | 'javascript';
  stats?: PlayerStats;
  unlockedFloors?: Record<DungeonTopic, number>;
  monsterHp?: number;
  maxMonsterHp?: number;
  activeWingRuns?: Record<string, SavedWingRun>;
  isSolutionUsedForProblem?: boolean;
}

function loadSavedActiveRuns(): Record<string, SavedWingRun> {
  if (typeof window === 'undefined') return {};
  try {
    const raw = localStorage.getItem(ACTIVE_RUNS_STORAGE_KEY);
    if (!raw) return {};
    return JSON.parse(raw);
  } catch (err) {
    console.warn('Failed to parse saved active runs:', err);
    return {};
  }
}

function saveActiveRuns(activeWingRuns: Record<string, SavedWingRun>) {
  if (typeof window === 'undefined') return;
  try {
    localStorage.setItem(ACTIVE_RUNS_STORAGE_KEY, JSON.stringify(activeWingRuns));
  } catch (err) {
    console.warn('Failed to save active runs:', err);
  }
}

function loadSavedSession(): PersistedGameSession | null {
  if (typeof window === 'undefined') return null;
  try {
    const raw = localStorage.getItem(SESSION_STORAGE_KEY);
    if (!raw) return null;
    return JSON.parse(raw);
  } catch (err) {
    console.warn('Failed to parse saved game session:', err);
    return null;
  }
}

function saveSession(state: GameState) {
  if (typeof window === 'undefined') return;
  try {
    const session: PersistedGameSession = {
      screen: state.screen,
      previousScreen: state.previousScreen,
      currentWing: state.currentWing,
      currentFloor: state.currentFloor,
      currentRunCatalog: state.currentRunCatalog,
      currentProblemId: state.currentProblem?.id || defaultInitialProblem.id,
      code: state.code,
      language: state.language,
      stats: state.stats,
      unlockedFloors: state.unlockedFloors,
      monsterHp: state.monsterHp,
      maxMonsterHp: state.maxMonsterHp,
      activeWingRuns: state.activeWingRuns,
      isSolutionUsedForProblem: state.isSolutionUsedForProblem,
    };
    localStorage.setItem(SESSION_STORAGE_KEY, JSON.stringify(session));
    saveActiveRuns(state.activeWingRuns);
  } catch (err) {
    console.warn('Failed to save game session:', err);
  }
}

const saved = loadSavedSession();
const savedRuns = saved?.activeWingRuns && Object.keys(saved.activeWingRuns).length > 0
  ? saved.activeWingRuns
  : loadSavedActiveRuns();

export const useGameStore = create<GameState>((set, get) => ({
  screen: saved?.screen || 'map',
  previousScreen: saved?.previousScreen || 'map',
  setScreen: (screen, pushHistory = true) => {
    const current = get().screen;
    if (current === screen) return;

    if (pushHistory && typeof window !== 'undefined') {
      const targetHash = screen === 'battle' ? '#battle' : screen === 'shop' ? '#shop' : '#map';
      if (window.location.hash !== targetHash) {
        window.history.pushState({ screen }, '', targetHash);
      }
    }

    set({
      previousScreen: current !== 'shop' && current !== 'victory' && current !== 'gameover' ? current : get().previousScreen,
      screen,
    });
  },
  closeShop: () => {
    const { previousScreen } = get();
    const target = previousScreen || 'map';
    if (typeof window !== 'undefined' && window.location.hash === '#shop') {
      window.history.back();
      return;
    }
    set({ screen: target });
  },

  stats: saved?.stats ? { ...defaultStats, ...saved.stats } : defaultStats,

  currentWing: saved?.currentWing || 'data-structures',
  currentFloor: saved?.currentFloor || 1,
  currentRunCatalog: saved?.currentRunCatalog && saved.currentRunCatalog.length > 0 ? saved.currentRunCatalog : initialRun,
  currentRunProblems: saved?.currentRunCatalog && saved.currentRunCatalog.length > 0 ? saved.currentRunCatalog : initialRun,
  currentProblem: initialProblem,
  isLoadingProblem: Boolean(saved?.currentProblemId && saved.currentProblemId !== initialProblem.id),
  monsterHp: saved?.monsterHp ?? initialProblem.testCases.length,
  maxMonsterHp: saved?.maxMonsterHp ?? initialProblem.testCases.length,
  unlockedFloors: saved?.unlockedFloors ? { ...defaultUnlockedFloors, ...saved.unlockedFloors } : defaultUnlockedFloors,
  activeWingRuns: savedRuns,
  isSolutionUsedForProblem: saved?.isSolutionUsedForProblem || false,
  setIsSolutionUsedForProblem: (used) => set({ isSolutionUsedForProblem: used }),

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

  language: saved?.language || 'python',
  setLanguage: (lang) => {
    const { currentProblem } = get();
    set({
      language: lang,
      code: getStarterCode(currentProblem, lang),
      lastReport: null,
    });
  },

  code: saved?.code !== undefined ? saved.code : getStarterCode(initialProblem, saved?.language || 'python'),
  isRunning: false,
  lastReport: null,
  activeTestCaseId: 1,

  frames: initialProblem.generateDefaultFrames(initialProblem.testCases[0]),
  currentFrameIndex: 0,
  isPlayingTimeline: false,
  playbackSpeed: 1,

  syncActiveRunsFromDatabase: async () => {
    const token = useAuthStore.getState().token;
    if (!token) return;

    try {
      const runs = await apiGetActiveRuns(token);
      if (Array.isArray(runs) && runs.length > 0) {
        const activeMap: Record<string, SavedWingRun> = { ...get().activeWingRuns };
        const unlocked = { ...get().unlockedFloors };

        for (const r of runs) {
          if (r.status === 'in_progress' && r.wing_id && Array.isArray(r.run_catalog) && r.run_catalog.length > 0) {
            activeMap[r.wing_id] = {
              wingId: r.wing_id as DungeonTopic,
              currentFloor: r.current_floor,
              maxFloorReached: r.max_floor_reached || r.current_floor,
              currentRunCatalog: r.run_catalog,
              currentProblemId: r.current_problem_id,
              code: r.code || '',
              language: (r.language as 'python' | 'javascript') || 'python',
              hp: r.hp ?? 100,
              maxHp: r.max_hp ?? 100,
              gold: r.gold ?? 50,
              potions: r.potions ?? 2,
              status: 'in_progress',
              updatedAt: r.updated_at ? new Date(r.updated_at).getTime() : Date.now(),
            };
            unlocked[r.wing_id as DungeonTopic] = Math.max(
              unlocked[r.wing_id as DungeonTopic] || 1,
              r.current_floor
            );
          }
        }

        set({
          activeWingRuns: activeMap,
          unlockedFloors: unlocked,
        });
        saveActiveRuns(activeMap);
      }
    } catch (err) {
      console.warn('Failed to sync active runs from DB:', err);
    }
  },

  restoreSession: async () => {
    const savedSession = loadSavedSession();
    if (!savedSession || !savedSession.currentProblemId) return;

    if (savedSession.currentProblemId === defaultInitialProblem.id && get().currentProblem.id === defaultInitialProblem.id) {
      set({ isLoadingProblem: false });
      return;
    }

    try {
      set({ isLoadingProblem: true });
      const problem = await loadProblem(savedSession.currentProblemId);
      const { language, code } = get();
      set({
        currentProblem: problem,
        isLoadingProblem: false,
        code: code || getStarterCode(problem, language),
        monsterHp: savedSession.monsterHp !== undefined ? savedSession.monsterHp : problem.testCases.length,
        maxMonsterHp: savedSession.maxMonsterHp !== undefined ? savedSession.maxMonsterHp : problem.testCases.length,
        activeTestCaseId: problem.testCases[0]?.id || 1,
        frames: problem.generateDefaultFrames(problem.testCases[0]),
        currentFrameIndex: 0,
        isPlayingTimeline: false,
        isSolutionUsedForProblem: savedSession.isSolutionUsedForProblem || false,
      });
    } catch (err) {
      console.error('Failed to restore problem on reload:', err);
      set({ isLoadingProblem: false });
    }
  },

  startNewRun: async (wing: DungeonTopic) => {
    const authState = useAuthStore.getState();
    const token = authState.token;

    // Abandon any previous active run on backend
    if (token) {
      apiAbandonDungeonRun(token, wing).catch(() => {});
    }

    const excludeIds = authState.hidePassedProblems && authState.hero
      ? new Set(authState.hero.passed_problems || [])
      : new Set<string>();
    const runCatalog = generateDungeonRunCatalog(wing, excludeIds);
    const floor = 1;
    const entry = runCatalog[0];
    const { language, stats } = get();

    if (typeof window !== 'undefined' && window.location.hash !== '#battle') {
      window.history.pushState({ screen: 'battle' }, '', '#battle');
    }

    const starterHp = stats.maxHp || 100;
    const newRun: SavedWingRun = {
      wingId: wing,
      currentFloor: 1,
      maxFloorReached: 1,
      currentRunCatalog: runCatalog,
      currentProblemId: entry.id,
      code: '',
      language,
      hp: starterHp,
      maxHp: stats.maxHp || 100,
      gold: stats.gold,
      potions: stats.potions,
      status: 'in_progress',
      isSolutionUsedForProblem: false,
      updatedAt: Date.now(),
    };

    const updatedRuns = {
      ...get().activeWingRuns,
      [wing]: newRun,
    };
    saveActiveRuns(updatedRuns);

    set((s) => ({
      activeWingRuns: updatedRuns,
      currentWing: wing,
      currentFloor: floor,
      currentRunCatalog: runCatalog,
      currentRunProblems: runCatalog,
      isLoadingProblem: true,
      isSolutionUsedForProblem: false,
      monsterHp: entry.monster.maxHp,
      maxMonsterHp: entry.monster.maxHp,
      lastReport: null,
      heroAnim: 'idle',
      monsterAnim: 'idle',
      previousScreen: 'map',
      screen: 'battle',
      stats: {
        ...s.stats,
        hp: starterHp,
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
      const starterCode = getStarterCode(problem, language);
      newRun.code = starterCode;
      const finalRuns = {
        ...get().activeWingRuns,
        [wing]: newRun,
      };
      saveActiveRuns(finalRuns);

      set({
        activeWingRuns: finalRuns,
        currentProblem: problem,
        isLoadingProblem: false,
        code: starterCode,
        monsterHp: problem.testCases.length,
        maxMonsterHp: problem.testCases.length,
        activeTestCaseId: problem.testCases[0].id,
        frames: problem.generateDefaultFrames(problem.testCases[0]),
        currentFrameIndex: 0,
        isPlayingTimeline: false,
      });

      // Save initial state of the new run to DB
      if (token) {
        apiSaveDungeonRun(token, {
          wing_id: wing,
          current_floor: 1,
          max_floor_reached: 1,
          status: 'in_progress',
          run_catalog: runCatalog,
          current_problem_id: entry.id,
          code: starterCode,
          language,
          hp: starterHp,
          max_hp: stats.maxHp || 100,
          gold: stats.gold,
          potions: stats.potions,
        });
      }

      // Prefetch remaining floors in the background
      prefetchProblems(runCatalog.slice(1).map((e) => e.id));
    } catch (err) {
      console.error('Failed to load problem:', err);
      set({ isLoadingProblem: false });
    }
  },

  continueRun: async (wing: DungeonTopic) => {
    const activeRun = get().activeWingRuns[wing];
    if (!activeRun || activeRun.status !== 'in_progress') {
      return get().startNewRun(wing);
    }

    const { currentFloor, currentRunCatalog, currentProblemId, code, language, hp, gold, potions, isSolutionUsedForProblem } = activeRun;
    const entry = currentRunCatalog[currentFloor - 1] || currentRunCatalog[0];
    const activeLanguage = language || get().language;

    if (typeof window !== 'undefined' && window.location.hash !== '#battle') {
      window.history.pushState({ screen: 'battle' }, '', '#battle');
    }

    set((s) => ({
      currentWing: wing,
      currentFloor,
      currentRunCatalog,
      currentRunProblems: currentRunCatalog,
      language: activeLanguage,
      isLoadingProblem: true,
      isSolutionUsedForProblem: isSolutionUsedForProblem || false,
      monsterHp: entry.monster.maxHp,
      maxMonsterHp: entry.monster.maxHp,
      lastReport: null,
      heroAnim: 'idle',
      monsterAnim: 'idle',
      previousScreen: 'map',
      screen: 'battle',
      stats: {
        ...s.stats,
        hp: hp !== undefined && hp > 0 ? hp : s.stats.hp,
        gold: gold !== undefined ? gold : s.stats.gold,
        potions: potions !== undefined ? potions : s.stats.potions,
        shield: 0,
        shieldPassedCount: 0,
      },
      combatLogs: [
        {
          id: `log-${Date.now()}`,
          sender: 'system',
          message: `Resumed expedition at Floor ${currentFloor} (${entry.title})! Strike down ${entry.monster.name}.`,
          type: 'info',
          timestamp: Date.now(),
        },
      ],
    }));

    try {
      const problem = await loadProblem(currentProblemId || entry.id);
      const activeCode = code || getStarterCode(problem, activeLanguage);

      set({
        currentProblem: problem,
        isLoadingProblem: false,
        code: activeCode,
        monsterHp: problem.testCases.length,
        maxMonsterHp: problem.testCases.length,
        activeTestCaseId: problem.testCases[0]?.id || 1,
        frames: problem.generateDefaultFrames(problem.testCases[0]),
        currentFrameIndex: 0,
        isPlayingTimeline: false,
      });

      // Prefetch remaining floors
      if (currentFloor < currentRunCatalog.length) {
        prefetchProblems(currentRunCatalog.slice(currentFloor).map((e) => e.id));
      }
    } catch (err) {
      console.error('Failed to load problem in continueRun:', err);
      set({ isLoadingProblem: false });
    }
  },

  selectWing: async (wing) => {
    const run = get().activeWingRuns[wing];
    if (run && run.status === 'in_progress' && run.currentFloor >= 1) {
      await get().continueRun(wing);
    } else {
      await get().startNewRun(wing);
    }
  },

  selectFloor: async (floor) => {
    const { currentRunCatalog, language } = get();
    const entry = currentRunCatalog[floor - 1];
    if (!entry) return;

    set({
      currentFloor: floor,
      isLoadingProblem: true,
      isSolutionUsedForProblem: false,
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

  setCode: (code) => {
    const { currentWing, activeWingRuns } = get();
    if (activeWingRuns[currentWing]) {
      const updated = {
        ...activeWingRuns,
        [currentWing]: {
          ...activeWingRuns[currentWing],
          code,
        },
      };
      saveActiveRuns(updated);
      set({ code, activeWingRuns: updated });
    } else {
      set({ code });
    }
  },
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
      const { isSolutionUsedForProblem } = get();

      if (isSolutionUsedForProblem) {
        // Solved by sacrificing health for solution:
        // DO NOT mark problem as conquered so it CAN be shown again in future dungeon runs!
        // Ensure it is un-marked in case it was previously conquered:
        useAuthStore.getState().unmarkProblemConquered(currentProblem.id);

        // Record submission noting solution was used
        apiRecordSubmission({
          problem_id: currentProblem.id,
          language: get().language,
          code: get().code,
          status: 'ACCEPTED_WITH_SOLUTION',
          tests_passed: report.passCount,
          total_tests: report.totalCount,
          execution_time_ms: 0,
        });

        addCombatLog(
          'system',
          '📜 Forbidden Solution used! The monster was banished, but because health was sacrificed for the solution, this challenge is NOT marked conquered and will be shown again in future runs.',
          'info'
        );
      } else {
        // Legitimate algorithmic solve! Mark problem as conquered in hero account
        useAuthStore.getState().markProblemConquered(currentProblem.id);

        // Record successful submission
        apiRecordSubmission({
          problem_id: currentProblem.id,
          language: get().language,
          code: get().code,
          status: 'ACCEPTED',
          tests_passed: report.passCount,
          total_tests: report.totalCount,
          execution_time_ms: 0,
        });

        addCombatLog('hero', `All ${report.passCount} test cases passed! Hero unleashed a fatal logic spell.`, 'critical');
      }

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
    const { stats, addCombatLog, currentWing, activeWingRuns } = get();
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
    const isForbiddenSolution = reason === 'Forbidden Solution';

    let updatedRuns = activeWingRuns;
    if (isForbiddenSolution && activeWingRuns[currentWing]) {
      updatedRuns = {
        ...activeWingRuns,
        [currentWing]: {
          ...activeWingRuns[currentWing],
          isSolutionUsedForProblem: true,
        },
      };
      saveActiveRuns(updatedRuns);
    }

    set((s) => ({
      stats: { ...s.stats, hp: newHp },
      heroAnim: 'hurt',
      isSolutionUsedForProblem: isForbiddenSolution ? true : s.isSolutionUsedForProblem,
      activeWingRuns: updatedRuns,
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
    const { currentWing, currentFloor, unlockedFloors, language, currentRunCatalog, stats, activeWingRuns } = get();
    const nextFloor = currentFloor + 1;
    const token = useAuthStore.getState().token;

    const totalFloors = currentRunCatalog?.length || 10;

    if (nextFloor <= totalFloors) {
      const nextEntry = currentRunCatalog[nextFloor - 1];
      if (nextEntry) {
        const updatedUnlocked = {
          ...unlockedFloors,
          [currentWing]: Math.max(unlockedFloors[currentWing] || 1, nextFloor),
        };

        set({
          currentFloor: nextFloor,
          isLoadingProblem: true,
          unlockedFloors: updatedUnlocked,
          monsterHp: nextEntry.monster.maxHp,
          maxMonsterHp: nextEntry.monster.maxHp,
          lastReport: null,
          heroAnim: 'idle',
          monsterAnim: 'idle',
          screen: 'battle',
        });

        try {
          const nextProblem = await loadProblem(nextEntry.id);
          const starterCode = getStarterCode(nextProblem, language);

          const updatedRun: SavedWingRun = {
            wingId: currentWing,
            currentFloor: nextFloor,
            maxFloorReached: Math.max(updatedUnlocked[currentWing] || 1, nextFloor),
            currentRunCatalog,
            currentProblemId: nextEntry.id,
            code: starterCode,
            language,
            hp: get().stats.hp,
            maxHp: get().stats.maxHp,
            gold: get().stats.gold,
            potions: get().stats.potions,
            status: 'in_progress',
            isSolutionUsedForProblem: false,
            updatedAt: Date.now(),
          };

          const updatedRuns = {
            ...get().activeWingRuns,
            [currentWing]: updatedRun,
          };
          saveActiveRuns(updatedRuns);

          set({
            activeWingRuns: updatedRuns,
            currentProblem: nextProblem,
            isLoadingProblem: false,
            code: starterCode,
            monsterHp: nextProblem.testCases.length,
            maxMonsterHp: nextProblem.testCases.length,
            activeTestCaseId: nextProblem.testCases[0].id,
            frames: nextProblem.generateDefaultFrames(nextProblem.testCases[0]),
            currentFrameIndex: 0,
            isSolutionUsedForProblem: false,
          });

          // Sync to database
          if (token) {
            apiSaveDungeonRun(token, {
              wing_id: currentWing,
              current_floor: nextFloor,
              max_floor_reached: updatedRun.maxFloorReached,
              status: 'in_progress',
              run_catalog: currentRunCatalog,
              current_problem_id: nextEntry.id,
              code: starterCode,
              language,
              hp: get().stats.hp,
              max_hp: get().stats.maxHp,
              gold: get().stats.gold,
              potions: get().stats.potions,
            });
          }
        } catch (err) {
          console.error('Failed to advance floor problem:', err);
          set({ isLoadingProblem: false });
        }
      }
    } else {
      // Completed all floors of this wing! Return to map
      const updatedRuns = { ...activeWingRuns };
      delete updatedRuns[currentWing];
      saveActiveRuns(updatedRuns);

      set({
        activeWingRuns: updatedRuns,
        screen: 'map',
      });

      if (token) {
        apiSaveDungeonRun(token, {
          wing_id: currentWing,
          current_floor: totalFloors,
          max_floor_reached: totalFloors,
          status: 'completed',
          run_catalog: currentRunCatalog,
          current_problem_id: currentRunCatalog[totalFloors - 1]?.id || '',
          hp: stats.hp,
          max_hp: stats.maxHp,
          gold: stats.gold,
          potions: stats.potions,
        });
      }
    }
  },

  restartRunOnPermadeath: async () => {
    // Permadeath reset: full health, re-roll fresh 10 problems for current wing starting at Floor 1!
    const { currentWing } = get();
    const token = useAuthStore.getState().token;
    if (token) {
      apiAbandonDungeonRun(token, currentWing).catch(() => {});
    }
    const updatedRuns = { ...get().activeWingRuns };
    delete updatedRuns[currentWing];
    saveActiveRuns(updatedRuns);
    set({ activeWingRuns: updatedRuns });

    await get().startNewRun(currentWing);
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

if (typeof window !== 'undefined') {
  useGameStore.subscribe((state) => {
    saveSession(state);
  });

  // Seed browser history stack so the browser Back button navigates to the map instead of exiting the website
  const currentHash = window.location.hash;
  if (saved?.screen === 'battle' || currentHash === '#battle') {
    window.history.replaceState({ screen: 'map' }, '', '#map');
    window.history.pushState({ screen: 'battle' }, '', '#battle');
    useGameStore.getState().restoreSession();
  } else if (saved?.screen === 'shop' || currentHash === '#shop') {
    window.history.replaceState({ screen: 'map' }, '', '#map');
    window.history.pushState({ screen: 'shop' }, '', '#shop');
  } else {
    window.history.replaceState({ screen: 'map' }, '', '#map');
  }

  // Handle browser Back / Forward buttons and mobile back gestures
  window.addEventListener('popstate', (e) => {
    const hash = window.location.hash;
    const stateScreen = e.state?.screen;

    if (hash === '#battle' || stateScreen === 'battle') {
      useGameStore.getState().setScreen('battle', false);
    } else if (hash === '#shop' || stateScreen === 'shop') {
      useGameStore.getState().setScreen('shop', false);
    } else {
      useGameStore.getState().setScreen('map', false);
    }
  });
}
