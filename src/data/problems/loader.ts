import { Problem, TestCase } from '../../types/problem';
import { DungeonTopic, Difficulty } from '../../types/game';
import { VisualizerFrame } from '../../types/visualizer';
import { problemCatalog, CatalogEntry } from './catalog';

export type { CatalogEntry };
export { problemCatalog };

// In-memory runtime problem cache
const problemCache = new Map<string, Problem>();

// Fallback frame generator when loading problems dynamically from JSON
export function createDefaultFrames(p: Partial<Problem>, tc: TestCase): VisualizerFrame[] {
  const type = p.visualizerType || 'array';
  const inp = tc.input?.[0];

  if (type === 'bits') {
    const val = typeof inp === 'number' ? inp : 0;
    const binary = (val >>> 0).toString(2);
    return [
      {
        type: 'bits',
        binaryString: binary,
        decimalValue: val,
        message: `Bit state for ${tc.inputDisplay}`,
      },
    ];
  }

  if (type === 'stack') {
    return [
      {
        type: 'stack',
        stack: Array.isArray(inp) ? inp : [],
        message: `Stack state for ${tc.inputDisplay}`,
      },
    ];
  }

  if (type === 'tree') {
    return [
      {
        type: 'tree',
        nodes: [],
        rootId: '0',
        message: `Tree structure for ${tc.inputDisplay}`,
      },
    ];
  }

  if (type === 'graph') {
    return [
      {
        type: 'graph',
        nodes: [],
        edges: [],
        message: `Graph traversal for ${tc.inputDisplay}`,
      },
    ];
  }

  if (type === 'dp') {
    const rawGrid = Array.isArray(inp)
      ? (Array.isArray(inp[0]) ? inp : [inp])
      : [[inp]];
    return [
      {
        type: 'dp',
        dimensions: Array.isArray(inp) && Array.isArray(inp[0]) ? '2D' : '1D',
        grid: rawGrid,
        message: `DP computation table for ${tc.inputDisplay}`,
      },
    ];
  }

  if (p.id === 'maximum-parentheses' && tc.input && Array.isArray(tc.input[2])) {
    const chars = typeof tc.input[1] === 'string' ? tc.input[1].split('') : [];
    const vals = tc.input[2];
    return [
      {
        type: 'array',
        array: chars.length <= 15 ? chars : chars.slice(0, 15),
        secondaryArray: vals.length <= 15 ? vals : vals.slice(0, 15),
        message: `Evaluating parentheses case: ${tc.inputDisplay}`,
      },
    ];
  }

  // Default array visualizer frame
  return [
    {
      type: 'array',
      array: Array.isArray(inp) ? inp : [inp],
      secondaryArray: tc.input?.[1] && Array.isArray(tc.input[1]) ? tc.input[1] : undefined,
      message: `Evaluating case: ${tc.inputDisplay}`,
    },
  ];
}

// Utility to shuffle an array immutably
function shuffle<T>(array: T[]): T[] {
  const arr = [...array];
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

/**
 * Generates a randomized 10-floor roguelike dungeon run using the lightweight catalog.
 * Executes instantly without any network fetch.
 */
export function generateDungeonRunCatalog(
  topic: DungeonTopic,
  excludeProblemIds: Set<string> = new Set()
): CatalogEntry[] {
  if (topic === 'security-sectors-trial') {
    return [
      {
        id: 'koko-eating-bananas',
        wingId: 'security-sectors-trial',
        floor: 1,
        title: 'Trial 1: Koko Eating Bananas (Binary Search on Answer)',
        difficulty: 'medium',
        visualizerType: 'array',
        leetcodeId: 875,
        leetcodeTitle: 'Koko Eating Bananas',
        leetcodeUrl: 'https://leetcode.com/problems/koko-eating-bananas/',
        monster: {
          id: 'mon-trial-koko',
          name: 'King Kong the Hoarder',
          title: 'Guardian of Threshold Capacity',
          maxHp: 8,
          hp: 8,
          sprite: 'golem',
          color: '#06b6d4',
          attackName: 'Banana Barrage',
          attackPower: 1,
          defeatQuote: 'Optimal eating speed found! You mastered Binary Search on Answer.',
        },
      },
      {
        id: 'graph-m-cheapest-flights-k-stops',
        wingId: 'security-sectors-trial',
        floor: 2,
        title: 'Trial 2: Cheapest Flights Within K Stops (Budget Constraints)',
        difficulty: 'medium',
        visualizerType: 'graph',
        leetcodeId: 787,
        leetcodeTitle: 'Cheapest Flights Within K Stops',
        leetcodeUrl: 'https://leetcode.com/problems/cheapest-flights-within-k-stops/',
        monster: {
          id: 'mon-trial-flights',
          name: 'Aero Harpy',
          title: 'Navigator of Constrained Airspace',
          maxHp: 10,
          hp: 10,
          sprite: 'wraith',
          color: '#f59e0b',
          attackName: 'Sky Turbulence',
          attackPower: 2,
          defeatQuote: 'You learned how to prune and track budgeted hops (at most K steps)!',
        },
      },
      {
        id: 'graph-m-path-min-effort',
        wingId: 'security-sectors-trial',
        floor: 3,
        title: 'Trial 3: Path with Minimum Effort (Graph Thresholding)',
        difficulty: 'medium',
        visualizerType: 'grid',
        leetcodeId: 1631,
        leetcodeTitle: 'Path with Minimum Effort',
        leetcodeUrl: 'https://leetcode.com/problems/path-with-minimum-effort/',
        monster: {
          id: 'mon-trial-effort',
          name: 'Crag Wyrm',
          title: 'Sentinel of Maximum Edge Heights',
          maxHp: 12,
          hp: 12,
          sprite: 'dragon',
          color: '#8b5cf6',
          attackName: 'Altitude Shear',
          attackPower: 2,
          defeatQuote: 'You conquered graph thresholding! Minimizing the maximum edge weight.',
        },
      },
      {
        id: 'graph-h-shortest-path-all-keys',
        wingId: 'security-sectors-trial',
        floor: 4,
        title: 'Trial 4: Shortest Path to Get All Keys (Multi-State Bitmask BFS)',
        difficulty: 'hard',
        visualizerType: 'grid',
        leetcodeId: 864,
        leetcodeTitle: 'Shortest Path to Get All Keys',
        leetcodeUrl: 'https://leetcode.com/problems/shortest-path-to-get-all-keys/',
        monster: {
          id: 'mon-trial-keys',
          name: 'Keymaster Behemoth',
          title: 'Keeper of Sector Bitmasks',
          maxHp: 14,
          hp: 14,
          sprite: 'boss',
          color: '#ec4899',
          attackName: 'Cipher Wave',
          attackPower: 3,
          defeatQuote: 'You mastered state expansion (node, bitmask) in BFS!',
        },
      },
      {
        id: 'the-security-sectors-path-of-trials',
        wingId: 'security-sectors-trial',
        floor: 5,
        title: 'Final Boss: The Security Sectors & Path of Trials',
        difficulty: 'hard',
        visualizerType: 'graph',
        leetcodeId: null,
        leetcodeTitle: 'The Security Sectors & Path of Trials (HackerRank Contest)',
        leetcodeUrl: 'https://www.hackerrank.com/contests/spct2026batch-3-pretest-1/challenges/the-security-sectors-path-of-trials/problem',
        monster: {
          id: 'mon-security-overlord',
          name: 'Malcor the Citadel Core',
          title: 'Grand Sentinel of the High Firewall',
          maxHp: 18,
          hp: 18,
          sprite: 'lich',
          color: '#f43f5e',
          attackName: 'Firewall Purge Pulse',
          attackPower: 4,
          defeatQuote: 'All 10 security sectors breached... the core firewall is conquered!',
        },
      },
    ];
  }

  if (topic === 'maximum-parentheses-trial') {
    return [
      {
        id: 'valid-parentheses',
        wingId: 'maximum-parentheses-trial',
        floor: 1,
        title: 'Trial 1: Valid Parentheses (Prefix Balance & LIFO Stack)',
        difficulty: 'easy',
        visualizerType: 'stack',
        leetcodeId: 20,
        leetcodeTitle: 'Valid Parentheses',
        leetcodeUrl: 'https://leetcode.com/problems/valid-parentheses/',
        monster: {
          id: 'mon-trial-valid-paren',
          name: 'Gargoyle of the Outer Gate',
          title: 'Sentinel of Balanced Enclosures',
          maxHp: 8,
          hp: 8,
          sprite: 'golem',
          color: '#06b6d4',
          attackName: 'Brace Crush',
          attackPower: 1,
          defeatQuote: 'You understand the core law: brackets must open and close in exact parity!',
        },
      },
      {
        id: 'bsg-m-min-add-parentheses-valid',
        wingId: 'maximum-parentheses-trial',
        floor: 2,
        title: 'Trial 2: Minimum Add to Make Parentheses Valid (Greedy Balance)',
        difficulty: 'medium',
        visualizerType: 'array',
        leetcodeId: 921,
        leetcodeTitle: 'Minimum Add to Make Parentheses Valid',
        leetcodeUrl: 'https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/',
        monster: {
          id: 'mon-trial-min-add',
          name: 'Specter of Stray Brackets',
          title: 'Weaver of Deficit Counts',
          maxHp: 10,
          hp: 10,
          sprite: 'wraith',
          color: '#f59e0b',
          attackName: 'Unpaired Strike',
          attackPower: 2,
          defeatQuote: 'You mastered greedy balance tracking of unmatched open and close counts!',
        },
      },
      {
        id: 'ds-h-longest-valid-parentheses',
        wingId: 'maximum-parentheses-trial',
        floor: 3,
        title: 'Trial 3: Longest Valid Parentheses (Boundary Tracking)',
        difficulty: 'hard',
        visualizerType: 'stack',
        leetcodeId: 32,
        leetcodeTitle: 'Longest Valid Parentheses',
        leetcodeUrl: 'https://leetcode.com/problems/longest-valid-parentheses/',
        monster: {
          id: 'mon-trial-longest-paren',
          name: 'Hydra of Nested Spans',
          title: 'Guardian of Substring Continuity',
          maxHp: 12,
          hp: 12,
          sprite: 'dragon',
          color: '#8b5cf6',
          attackName: 'Cascading Parenthesis Surge',
          attackPower: 2,
          defeatQuote: 'Contiguous valid intervals mastered under dynamic stack boundaries!',
        },
      },
      {
        id: 'bsg-h-course-schedule-iii',
        wingId: 'maximum-parentheses-trial',
        floor: 4,
        title: 'Trial 4: Course Schedule III (Priority Queue Regret Greedy)',
        difficulty: 'hard',
        visualizerType: 'array',
        leetcodeId: 630,
        leetcodeTitle: 'Course Schedule III',
        leetcodeUrl: 'https://leetcode.com/problems/course-schedule-iii/',
        monster: {
          id: 'mon-trial-course-regret',
          name: 'Chronos the Regret Sentinel',
          title: 'Keeper of Optimal Replacements',
          maxHp: 14,
          hp: 14,
          sprite: 'boss',
          color: '#ec4899',
          attackName: 'Temporal Eviction',
          attackPower: 3,
          defeatQuote: 'You mastered the Regret Greedy pattern with Max-Heaps!',
        },
      },
      {
        id: 'maximum-parentheses',
        wingId: 'maximum-parentheses-trial',
        floor: 5,
        title: 'Final Boss: Maximum Parentheses',
        difficulty: 'hard',
        visualizerType: 'array',
        leetcodeId: null,
        leetcodeTitle: 'Maximum parentheses (HackerRank Contest)',
        leetcodeUrl: 'https://www.hackerrank.com/contests/spct2026batch-1-pretest-1/challenges/maximum-parentheses/problem',
        monster: {
          id: 'mon-maximum-parentheses-boss',
          name: 'Equilibria the Parity Overlord',
          title: 'Arch-Master of Slope-Trick Matching',
          maxHp: 18,
          hp: 18,
          sprite: 'lich',
          color: '#8b5cf6',
          attackName: 'Singularity Inversion Wave',
          attackPower: 4,
          defeatQuote: 'The balance is unbroken... You achieved optimal parentheses subsequence profit!',
        },
      },
    ];
  }

  const pool = problemCatalog.filter((p) => p.wingId === topic);
  const fallback = problemCatalog.filter((p) => p.wingId === 'data-structures');
  const basePool = pool.length >= 10 ? pool : fallback;

  // Filter out problems that the user has already passed
  const unpassed = basePool.filter((p) => !excludeProblemIds.has(p.id));

  // If there are enough unpassed problems in this wing, prioritize them!
  // If the user conquered nearly all, supplement with mastered problems so a full 10-floor run completes.
  let activePool: CatalogEntry[];
  if (unpassed.length >= 10) {
    activePool = unpassed;
  } else if (unpassed.length > 0) {
    const passed = basePool.filter((p) => excludeProblemIds.has(p.id));
    activePool = [...unpassed, ...shuffle(passed)].slice(0, Math.max(10, unpassed.length));
  } else {
    // All problems in this wing have been conquered!
    activePool = basePool;
  }

  const easyPool = activePool.filter((p) => p.difficulty === 'easy');
  const mediumPool = activePool.filter((p) => p.difficulty === 'medium');
  const hardPool = activePool.filter((p) => p.difficulty === 'hard');

  // Progression: Heavily weighted toward Medium and Hard (1-2 Easy, 5-6 Medium, 3-4 Hard)
  const hardCount = Math.min(hardPool.length, Math.random() < 0.5 ? 4 : 3);
  const easyCount = Math.min(easyPool.length, Math.random() < 0.5 ? 1 : 2);
  const mediumCount = Math.max(0, 10 - hardCount - easyCount);

  const selectedEasy = shuffle(easyPool).slice(0, easyCount);
  const selectedMedium = shuffle(mediumPool).slice(0, mediumCount);
  const selectedHard = shuffle(hardPool).slice(0, hardCount);

  // Progressive dungeon difficulty order: Easy -> Medium -> Hard
  let rawSelection = [...selectedEasy, ...selectedMedium, ...selectedHard];

  // If counts were short due to pool size, pad from activePool
  if (rawSelection.length < 10) {
    const existingIds = new Set(rawSelection.map((p) => p.id));
    const remainder = shuffle(activePool.filter((p) => !existingIds.has(p.id)));
    rawSelection = [...rawSelection, ...remainder].slice(0, 10);
  }

  return rawSelection.map((p, idx) => {
    const floorNum = idx + 1;
    const isBoss = floorNum === 10;
    return {
      ...p,
      floor: floorNum,
      monster: {
        ...p.monster,
        maxHp: isBoss ? Math.max(12, p.monster.maxHp) : p.monster.maxHp,
        hp: isBoss ? Math.max(12, p.monster.hp) : p.monster.hp,
      },
    };
  });
}

/**
 * Loads a full problem definition on-demand by ID.
 * Caches in memory for instant subsequent access.
 * Works across both browser (via fetch) and Node.js (via filesystem).
 */
export async function loadProblem(problemId: string): Promise<Problem> {
  const cached = problemCache.get(problemId);
  if (cached) return cached;

  let rawData: any;

  if (typeof window === 'undefined') {
    // Node.js environment (for tests/verification scripts)
    const fs = await import('fs');
    const path = await import('path');
    const filePath = path.join(process.cwd(), 'public', 'problems', 'data', `${problemId}.json`);
    const content = fs.readFileSync(filePath, 'utf-8');
    rawData = JSON.parse(content);
  } else {
    // Browser environment (runtime SPA)
    const base = (typeof import.meta !== 'undefined' && (import.meta as any).env?.BASE_URL) || '/';
    const cleanBase = base.endsWith('/') ? base.slice(0, -1) : base;
    const res = await fetch(`${cleanBase}/problems/data/${problemId}.json`);
    if (!res.ok) {
      throw new Error(`Failed to load problem "${problemId}": HTTP ${res.status}`);
    }
    rawData = await res.json();
  }

  const problem: Problem = {
    ...rawData,
    generateDefaultFrames: (tc: TestCase) => createDefaultFrames(rawData, tc),
  };

  problemCache.set(problemId, problem);
  return problem;
}

/**
 * Asynchronously prefetches a list of problems into the in-memory cache.
 */
export async function prefetchProblems(problemIds: string[]): Promise<void> {
  const missing = problemIds.filter((id) => !problemCache.has(id));
  if (missing.length === 0) return;

  await Promise.allSettled(missing.map((id) => loadProblem(id)));
}

/**
 * Synchronous cache lookup for an already loaded problem.
 */
export function getCachedProblem(problemId: string): Problem | undefined {
  return problemCache.get(problemId);
}

/**
 * Default initial problem definition for zero-latency, synchronous initial mount.
 */
export const defaultInitialProblem: Problem = {
  id: 'two-sum',
  wingId: 'data-structures',
  floor: 1,
  title: 'Two Sum',
  difficulty: 'easy',
  visualizerType: 'array',
  monster: {
    id: 'goblin-scout',
    name: 'Grom the Key Goblin',
    title: 'Scavenger of Key-Value Shards',
    maxHp: 10,
    hp: 10,
    sprite: 'goblin',
    color: '#eab308',
    attackName: 'Rusty Dagger Shank',
    attackPower: 1,
    defeatQuote: 'Grom could not find complement in time...',
  },
  description:
    'Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.\n\nYou may assume that each input would have exactly one solution, and you may not use the same element twice.',
  examples: [
    {
      input: 'nums = [2, 7, 11, 15], target = 9',
      output: '[0, 1]',
    },
    {
      input: 'nums = [3, 2, 4], target = 6',
      output: '[1, 2]',
    },
    {
      input: 'nums = [3, 3], target = 6',
      output: '[0, 1]',
    },
  ],
  constraints: [
    '2 <= nums.length <= 10^4',
    '-10^9 <= nums[i] <= 10^9',
    'Exactly one valid answer exists.',
  ],
  starterCode: 'def twoSum(nums: list[int], target: int) -> list[int]:\n    return []\n',
  solutionCode:
    'def twoSum(nums: list[int], target: int) -> list[int]:\n    seen = {}\n    for i, num in enumerate(nums):\n        comp = target - num\n        if comp in seen:\n            return [seen[comp], i]\n        seen[num] = i\n    return []\n',
  functionName: 'twoSum',
  testCases: [
    {
      id: 1,
      input: [[2, 7, 11, 15], 9],
      expected: [0, 1],
      inputDisplay: 'nums = [2, 7, 11, 15], target = 9',
      expectedDisplay: '[0, 1]',
    },
    {
      id: 2,
      input: [[3, 2, 4], 6],
      expected: [1, 2],
      inputDisplay: 'nums = [3, 2, 4], target = 6',
      expectedDisplay: '[1, 2]',
    },
    {
      id: 3,
      input: [[3, 3], 6],
      expected: [0, 1],
      inputDisplay: 'nums = [3, 3], target = 6',
      expectedDisplay: '[0, 1]',
    },
    {
      id: 4,
      input: [[-1, -2, -3, -4, -5], -8],
      expected: [2, 4],
      inputDisplay: '[-1,-2,-3,-4,-5], -8',
      expectedDisplay: '[2,4]',
      isHidden: true,
    },
    {
      id: 5,
      input: [[0, 4, 3, 0], 0],
      expected: [0, 3],
      inputDisplay: '[0,4,3,0], 0',
      expectedDisplay: '[0,3]',
      isHidden: true,
    },
    {
      id: 6,
      input: [[-3, 4, 3, 90], 0],
      expected: [0, 2],
      inputDisplay: '[-3,4,3,90], 0',
      expectedDisplay: '[0,2]',
      isHidden: true,
    },
    {
      id: 7,
      input: [[1, 5, 8, 12, 20, 35], 55],
      expected: [4, 5],
      inputDisplay: '[1, 5, 8, 12, ... (6 items)], 55',
      expectedDisplay: '[4,5]',
      isHidden: true,
    },
    {
      id: 8,
      input: [[100, 200, 300, 400], 700],
      expected: [2, 3],
      inputDisplay: '[100,200,300,400], 700',
      expectedDisplay: '[2,3]',
      isHidden: true,
    },
    {
      id: 9,
      input: [[5, 75, 25], 100],
      expected: [1, 2],
      inputDisplay: '[5,75,25], 100',
      expectedDisplay: '[1,2]',
      isHidden: true,
    },
    {
      id: 10,
      input: [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19],
      expected: [8, 9],
      inputDisplay: '[1, 2, 3, 4, ... (10 items)], 19',
      expectedDisplay: '[8,9]',
      isHidden: true,
    },
  ],
  hints: ['Store previously seen values in a Hash Map to look up complements in O(1) time.'],
  python: {
    starterCode: 'def twoSum(nums, target):\n    return []\n',
    solutionCode:
      'def twoSum(nums, target):\n    seen = {}\n    for i, num in enumerate(nums):\n        comp = target - num\n        if comp in seen:\n            return [seen[comp], i]\n        seen[num] = i\n    return []\n',
  },
  generateDefaultFrames: (tc) => createDefaultFrames({ visualizerType: 'array' }, tc),
  leetcodeId: 1,
  leetcodeTitle: 'Two Sum',
  leetcodeUrl: 'https://leetcode.com/problems/two-sum/',
};

// Seed problem cache with initial problem
problemCache.set('two-sum', defaultInitialProblem);

// Export randomized initial catalog run
export const initialCatalogRun: CatalogEntry[] = generateDungeonRunCatalog('data-structures');

// Start background prefetch if running in the browser
if (typeof window !== 'undefined') {
  setTimeout(() => {
    prefetchProblems(initialCatalogRun.map((entry) => entry.id));
  }, 100);
}

