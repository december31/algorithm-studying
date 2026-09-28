import { Difficulty, DungeonTopic, Monster } from './game';
import { VisualizerFrame, VisualizerType } from './visualizer';

export interface TestCase {
  id: number;
  input: any[];
  expected: any;
  inputDisplay: string;
  expectedDisplay: string;
  isHidden?: boolean;
}

export interface Problem {
  id: string;
  wingId: DungeonTopic;
  floor: number;
  title: string;
  difficulty: Difficulty;
  visualizerType: VisualizerType;
  monster: Monster;
  description: string;
  examples: {
    input: string;
    output: string;
    explanation?: string;
  }[];
  constraints: string[];
  starterCode: string;
  solutionCode: string;
  functionName: string;
  testCases: TestCase[];
  hints: string[];
  // Generates visual frames for step-by-step animation based on the problem test case
  generateDefaultFrames: (testCase: TestCase) => VisualizerFrame[];
}
