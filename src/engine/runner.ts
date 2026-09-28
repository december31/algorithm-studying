import { Problem, TestCase } from '../types/problem';
import { VisualizerFrame } from '../types/visualizer';

export interface TestResult {
  testCaseId: number;
  passed: boolean;
  actual: any;
  expected: any;
  inputDisplay: string;
  expectedDisplay: string;
  actualDisplay: string;
  logs: string[];
  error?: string;
  frames: VisualizerFrame[];
}

export interface ExecutionReport {
  mode?: 'run' | 'submit';
  allPassed: boolean;
  passCount: number;
  totalCount: number;
  results: TestResult[];
  globalError?: string;
}

// Deep comparison for algorithm outputs (handles arrays, objects, primitives)
export function deepEqual(a: any, b: any): boolean {
  if (a === b) return true;
  if (a == null || b == null) return false;
  if (typeof a !== typeof b) return false;

  if (Array.isArray(a) && Array.isArray(b)) {
    if (a.length !== b.length) return false;
    for (let i = 0; i < a.length; i++) {
      if (!deepEqual(a[i], b[i])) return false;
    }
    return true;
  }

  if (typeof a === 'object') {
    const keysA = Object.keys(a);
    const keysB = Object.keys(b);
    if (keysA.length !== keysB.length) return false;
    for (const key of keysA) {
      if (!keysB.includes(key)) return false;
      if (!deepEqual(a[key], b[key])) return false;
    }
    return true;
  }

  return false;
}

export function stringifyResult(val: any): string {
  if (val === undefined) return 'undefined';
  try {
    return JSON.stringify(val);
  } catch {
    return String(val);
  }
}

// Run user code against test cases with safety timeout
export async function executeSolution(
  problem: Problem,
  userCode: string,
  mode: 'run' | 'submit' = 'submit'
): Promise<ExecutionReport> {
  const results: TestResult[] = [];
  const TIMEOUT_MS = 2500; // 2.5 second watchdog against infinite loops
  const targetCases = mode === 'run'
    ? problem.testCases.filter((tc) => !tc.isHidden).slice(0, 3)
    : problem.testCases;

  try {
    // Construct runner script
    // We bind console.log to capture prints
    const resultsPromises = targetCases.map((tc) => {
      return new Promise<TestResult>((resolve) => {
        const capturedLogs: string[] = [];
        const recordedFrames: VisualizerFrame[] = [];

        // Timeout timer
        let isTimedOut = false;
        const timer = setTimeout(() => {
          isTimedOut = true;
          resolve({
            testCaseId: tc.id,
            passed: false,
            actual: 'TIMEOUT (Execution exceeded 2.5s)',
            expected: tc.expected,
            inputDisplay: tc.inputDisplay,
            expectedDisplay: tc.expectedDisplay,
            actualDisplay: 'Time Limit Exceeded (Infinite loop detected)',
            logs: capturedLogs,
            error: 'Time Limit Exceeded: Check your loops and recursion base cases!',
            frames: [],
          });
        }, TIMEOUT_MS);

        try {
          // Tracer proxy for visualizer
          const tracer = {
            step: (frame: VisualizerFrame) => {
              if (recordedFrames.length < 100) {
                recordedFrames.push(frame);
              }
            }
          };

          const customConsole = {
            log: (...args: any[]) => {
              capturedLogs.push(args.map(stringifyResult).join(' '));
            },
            error: (...args: any[]) => {
              capturedLogs.push('ERROR: ' + args.map(stringifyResult).join(' '));
            },
            warn: (...args: any[]) => {
              capturedLogs.push('WARN: ' + args.map(stringifyResult).join(' '));
            }
          };

          // Wrap user code in a function constructor
          // Returns the target function
          const runnerWrapper = new Function(
            'console',
            'tracer',
            `
            ${userCode}
            if (typeof ${problem.functionName} !== 'function') {
              throw new Error("Function '${problem.functionName}' was not defined. Make sure not to change the function name.");
            }
            return ${problem.functionName};
            `
          );

          const userFn = runnerWrapper(customConsole, tracer);

          // Deep clone inputs to prevent mutation across tests
          const clonedInput = JSON.parse(JSON.stringify(tc.input));

          const startTime = performance.now();
          const actualOutput = userFn(...clonedInput);
          const duration = performance.now() - startTime;

          clearTimeout(timer);
          if (isTimedOut) return;

          const passed = deepEqual(actualOutput, tc.expected);

          // Generate frames for sample runs, failures, or first test case
          const shouldGenerateFrames = mode === 'run' || !passed || tc.id === targetCases[0].id;
          const frames = recordedFrames.length > 0
            ? recordedFrames
            : shouldGenerateFrames
            ? problem.generateDefaultFrames(tc)
            : [];

          resolve({
            testCaseId: tc.id,
            passed,
            actual: actualOutput,
            expected: tc.expected,
            inputDisplay: tc.inputDisplay,
            expectedDisplay: tc.expectedDisplay,
            actualDisplay: stringifyResult(actualOutput),
            logs: capturedLogs,
            frames,
          });
        } catch (err: any) {
          clearTimeout(timer);
          if (isTimedOut) return;

          resolve({
            testCaseId: tc.id,
            passed: false,
            actual: null,
            expected: tc.expected,
            inputDisplay: tc.inputDisplay,
            expectedDisplay: tc.expectedDisplay,
            actualDisplay: 'Runtime Error',
            logs: capturedLogs,
            error: err?.message || String(err),
            frames: problem.generateDefaultFrames(tc),
          });
        }
      });
    });

    const settledResults = await Promise.all(resultsPromises);
    const passCount = settledResults.filter((r) => r.passed).length;
    const allPassed = passCount === settledResults.length;

    return {
      mode,
      allPassed,
      passCount,
      totalCount: settledResults.length,
      results: settledResults,
    };
  } catch (globalErr: any) {
    return {
      mode,
      allPassed: false,
      passCount: 0,
      totalCount: targetCases.length,
      results: [],
      globalError: globalErr?.message || 'Syntax Error in solution',
    };
  }
}
