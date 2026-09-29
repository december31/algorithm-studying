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
export function generateDungeonRunCatalog(topic: DungeonTopic): CatalogEntry[] {
  const pool = problemCatalog.filter((p) => p.wingId === topic);
  const fallback = problemCatalog.filter((p) => p.wingId === 'data-structures');
  const activePool = pool.length >= 10 ? pool : fallback;

  const easyPool = activePool.filter((p) => p.difficulty === 'easy');
  const mediumPool = activePool.filter((p) => p.difficulty === 'medium');
  const hardPool = activePool.filter((p) => p.difficulty === 'hard');

  const hardCount = Math.min(hardPool.length, Math.random() < 0.5 ? 2 : 3);
  const mediumCount = Math.min(mediumPool.length, 10 - hardCount >= 8 ? 4 : 3);
  const easyCount = 10 - hardCount - mediumCount;

  const selectedEasy = shuffle(easyPool).slice(0, easyCount);
  const selectedMedium = shuffle(mediumPool).slice(0, mediumCount);
  const selectedHard = shuffle(hardPool).slice(0, hardCount);

  const rawSelection = [...selectedEasy, ...selectedMedium, ...selectedHard];

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
  starterCode: 'function twoSum(nums, target) {\n  return [];\n}',
  solutionCode:
    'function twoSum(nums, target) {\n  const map = new Map();\n  for (let i = 0; i < nums.length; i++) {\n    const complement = target - nums[i];\n    if (map.has(complement)) {\n      return [map.get(complement), i];\n    }\n    map.set(nums[i], i);\n  }\n  return [];\n}',
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

