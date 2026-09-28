import { Problem, TestCase } from '../types/problem';
import { ExecutionReport, TestResult, deepEqual, stringifyResult } from './runner';

declare global {
  interface Window {
    loadPyodide?: (config: { indexURL: string }) => Promise<any>;
  }
}

let pyodideInstance: any = null;
let pyodideLoadingPromise: Promise<any> | null = null;
let pyodideStatus: 'uninitialized' | 'loading' | 'ready' | 'error' = 'uninitialized';

export function getPyodideStatus(): 'uninitialized' | 'loading' | 'ready' | 'error' {
  return pyodideStatus;
}

export async function initPyodide(): Promise<any> {
  if (pyodideInstance) return pyodideInstance;
  if (pyodideLoadingPromise) return pyodideLoadingPromise;

  pyodideStatus = 'loading';

  pyodideLoadingPromise = (async () => {
    try {
      // If script is not yet loaded, wait for it
      let tries = 0;
      while (!window.loadPyodide && tries < 20) {
        await new Promise((r) => setTimeout(r, 200));
        tries++;
      }

      if (!window.loadPyodide) {
        throw new Error('Pyodide script failed to load. Please check your internet connection.');
      }

      pyodideInstance = await window.loadPyodide({
        indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/',
      });

      pyodideStatus = 'ready';
      return pyodideInstance;
    } catch (err) {
      pyodideStatus = 'error';
      pyodideLoadingPromise = null;
      throw err;
    }
  })();

  return pyodideLoadingPromise;
}

export async function executePythonSolution(
  problem: Problem,
  userCode: string,
  mode: 'run' | 'submit' = 'submit'
): Promise<ExecutionReport> {
  const TIMEOUT_MS = 3000;
  const py = await initPyodide();

  const results: TestResult[] = [];
  const targetCases = mode === 'run'
    ? problem.testCases.filter((tc) => !tc.isHidden).slice(0, 3)
    : problem.testCases;

  try {
    // Reset Python stdout buffer
    await py.runPythonAsync(`
import sys
from io import StringIO
_custom_stdout = StringIO()
sys.stdout = _custom_stdout
    `);

    // Execute user code to define function
    await py.runPythonAsync(userCode);

    const fnName = problem.functionName;
    const pyFn = py.globals.get(fnName);

    if (!pyFn) {
      return {
        mode,
        allPassed: false,
        passCount: 0,
        totalCount: targetCases.length,
        results: [],
        globalError: `Function '${fnName}' not found in Python code. Make sure to define 'def ${fnName}(...)'.`,
      };
    }

    if (mode === 'submit') {
      // High-performance batched execution: runs all test cases in Python VM in a single pass (<10ms)
      const batchPayload = JSON.stringify(
        targetCases.map((tc) => ({ id: tc.id, input: tc.input }))
      );

      const batchScript = `
import json

_test_payload = json.loads('''${batchPayload.replace(/\\/g, '\\\\').replace(/'/g, "\\'")}''')
_batch_results = []

for _item in _test_payload:
    _custom_stdout.truncate(0)
    _custom_stdout.seek(0)
    try:
        _actual = ${fnName}(*_item['input'])
        _batch_results.append({
            'id': _item['id'],
            'actual': _actual,
            'logs': _custom_stdout.getvalue().strip().split('\\n') if _custom_stdout.getvalue().strip() else [],
            'error': None
        })
    except Exception as _e:
        _batch_results.append({
            'id': _item['id'],
            'actual': None,
            'logs': _custom_stdout.getvalue().strip().split('\\n') if _custom_stdout.getvalue().strip() else [],
            'error': str(_e)
        })

import json as _j
_batch_json = _j.dumps(_batch_results, default=str)
_batch_json
`;

      const rawBatchOut = await py.runPythonAsync(batchScript);
      const parsedBatch: any[] = JSON.parse(rawBatchOut);

      for (let i = 0; i < targetCases.length; i++) {
        const tc = targetCases[i];
        const res = parsedBatch[i];
        let actual = res.actual;
        try {
          if (typeof actual === 'string' && (actual.startsWith('[') || actual.startsWith('{'))) {
            actual = JSON.parse(actual);
          }
        } catch {}

        const passed = !res.error && deepEqual(actual, tc.expected);
        const shouldGenFrames = !passed || tc.id === targetCases[0].id;

        results.push({
          testCaseId: tc.id,
          passed,
          actual,
          expected: tc.expected,
          inputDisplay: tc.inputDisplay,
          expectedDisplay: tc.expectedDisplay,
          actualDisplay: res.error ? 'Python Error' : stringifyResult(actual),
          logs: res.logs || [],
          error: res.error,
          frames: shouldGenFrames ? problem.generateDefaultFrames(tc) : [],
        });
      }
    } else {
      // mode === 'run': runs sample cases with detailed per-case tracing and frames
      for (const tc of targetCases) {
        let isTimedOut = false;
        const timeoutPromise = new Promise<never>((_, reject) => {
          setTimeout(() => {
            isTimedOut = true;
            reject(new Error('Time Limit Exceeded (> 3s): Check your loops or recursion base cases!'));
          }, TIMEOUT_MS);
        });

        try {
          const executionPromise = (async () => {
            await py.runPythonAsync(`
_custom_stdout.truncate(0)
_custom_stdout.seek(0)
            `);

            const pyArgs = JSON.parse(JSON.stringify(tc.input));
            const rawResult = pyFn(...pyArgs);

            let actualJs = rawResult;
            if (rawResult && typeof rawResult.toJs === 'function') {
              actualJs = rawResult.toJs({ dict_converter: Object.fromEntries });
            }

            const pyLogsRaw = await py.runPythonAsync(`_custom_stdout.getvalue()`);
            const logs = pyLogsRaw ? pyLogsRaw.trim().split('\n').filter(Boolean) : [];

            return { actualJs, logs };
          })();

          const { actualJs, logs } = await Promise.race([executionPromise, timeoutPromise]);

          const passed = deepEqual(actualJs, tc.expected);
          const frames = problem.generateDefaultFrames(tc);

          results.push({
            testCaseId: tc.id,
            passed,
            actual: actualJs,
            expected: tc.expected,
            inputDisplay: tc.inputDisplay,
            expectedDisplay: tc.expectedDisplay,
            actualDisplay: stringifyResult(actualJs),
            logs,
            frames,
          });
        } catch (err: any) {
          results.push({
            testCaseId: tc.id,
            passed: false,
            actual: null,
            expected: tc.expected,
            inputDisplay: tc.inputDisplay,
            expectedDisplay: tc.expectedDisplay,
            actualDisplay: isTimedOut ? 'Time Limit Exceeded' : 'Python Exception',
            logs: [],
            error: err?.message || String(err),
            frames: problem.generateDefaultFrames(tc),
          });
        }
      }
    }

    const passCount = results.filter((r) => r.passed).length;
    const allPassed = passCount === results.length;

    return {
      mode,
      allPassed,
      passCount,
      totalCount: results.length,
      results,
    };
  } catch (err: any) {
    return {
      mode,
      allPassed: false,
      passCount: 0,
      totalCount: targetCases.length,
      results: [],
      globalError: err?.message || String(err),
    };
  }
}
