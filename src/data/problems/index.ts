import { Problem } from '../../types/problem';
import { DungeonTopic } from '../../types/game';
import { dataStructureProblems } from './dataStructures';
import { backtrackingProblems } from './backtracking';
import { graphProblems } from './graphs';
import { binarySearchGreedyProblems } from './binarySearchGreedy';
import { bitManipulationProblems } from './bitManipulation';
import { getEnrichedTestCases } from '../edgeCases';

export const allTopics: DungeonTopic[] = [
  'data-structures',
  'backtracking',
  'graphs',
  'binary-search-greedy',
  'bit-manipulation',
];

export const allProblems: Record<DungeonTopic, Problem[]> = {
  'data-structures': dataStructureProblems,
  'backtracking': backtrackingProblems,
  'graphs': graphProblems,
  'binary-search-greedy': binarySearchGreedyProblems,
  'bit-manipulation': bitManipulationProblems,
};

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
 * Dynamically generates a randomized 10-floor roguelike dungeon run for a given topic.
 * Requirements:
 * - Exactly 10 problems chosen for the run.
 * - At most 3 Hard problems per run.
 * - Progressive difficulty curve: Floors 1-4/5 Easy -> Floors 5/6-8 Medium -> Floors 9-10 Hard (Boss at Floor 10).
 * - Fresh random selection on every call (re-rolls on permadeath!).
 * - Full suite of 10 test cases per problem (3 sample + 7 hidden edge cases).
 */
export function generateDungeonRun(topic: DungeonTopic): Problem[] {
  const pool = allProblems[topic] || dataStructureProblems;

  const easyPool = pool.filter((p) => p.difficulty === 'easy');
  const mediumPool = pool.filter((p) => p.difficulty === 'medium');
  const hardPool = pool.filter((p) => p.difficulty === 'hard');

  // Hard problems: exactly 2 or 3 (strictly <= 3)
  const hardCount = Math.min(hardPool.length, Math.random() < 0.5 ? 2 : 3);
  // Medium problems: 3 or 4
  const mediumCount = Math.min(mediumPool.length, 10 - hardCount >= 8 ? 4 : 3);
  // Easy problems: fill remaining slots to reach exactly 10
  const easyCount = 10 - hardCount - mediumCount;

  const selectedEasy = shuffle(easyPool).slice(0, easyCount);
  const selectedMedium = shuffle(mediumPool).slice(0, mediumCount);
  const selectedHard = shuffle(hardPool).slice(0, hardCount);

  const rawSelection = [...selectedEasy, ...selectedMedium, ...selectedHard];

  // Assign sequential floors 1 to 10 with enriched test cases
  const runProblems: Problem[] = rawSelection.map((p, idx) => {
    const floorNum = idx + 1;
    const isBoss = floorNum === 10;
    const enrichedTests = getEnrichedTestCases(p);

    return {
      ...p,
      floor: floorNum,
      title: isBoss ? `Floor 10: BOSS - ${p.title}` : `Floor ${floorNum}: ${p.title}`,
      testCases: enrichedTests,
      monster: {
        ...p.monster,
        maxHp: isBoss ? Math.max(12, enrichedTests.length) : enrichedTests.length,
        hp: isBoss ? Math.max(12, enrichedTests.length) : enrichedTests.length,
      },
    };
  });

  return runProblems;
}

export function getProblem(wingId: DungeonTopic, floor: number): Problem | undefined {
  const problems = allProblems[wingId] || dataStructureProblems;
  const p = problems.find((item) => item.floor === floor) || problems[0];
  if (!p) return undefined;
  const enrichedTests = getEnrichedTestCases(p);
  return {
    ...p,
    testCases: enrichedTests,
    monster: {
      ...p.monster,
      maxHp: enrichedTests.length,
      hp: enrichedTests.length,
    },
  };
}
