import { problemCatalog, loadProblem } from '../src/data/problems/loader';
import { execSync } from 'child_process';
import * as fs from 'fs';
import * as path from 'path';

async function verifyAllPython() {
  console.log(`🐍 VERIFYING ALL ${problemCatalog.length} PYTHON SOLUTIONS WITH PYTHON 3.13...`);
  let totalProblems = 0;
  let passedProblems = 0;
  let totalTests = 0;
  let passedTests = 0;

  const tmpScript = path.join(process.cwd(), 'scripts', '_temp_py_test.py');

  for (const entry of problemCatalog) {
    totalProblems++;
    const prob = await loadProblem(entry.id);
    const pyEntry = (prob as any).python;
    if (!pyEntry || !pyEntry.solutionCode) {
      console.error(`  ❌ Missing python solution for ${prob.id}`);
      continue;
    }

    const solCode = pyEntry.solutionCode;
    let probPassed = true;

    for (const tc of prob.testCases) {
      totalTests++;

      const pyScript = `import json
import sys

${solCode}

inputs = json.loads('''${JSON.stringify(tc.input)}''')
expected = json.loads('''${JSON.stringify(tc.expected)}''')

actual = ${prob.functionName}(*inputs)

def normalize(v):
    if isinstance(v, (list, tuple)):
        # Normalize list of lists where order doesn't strictly matter or compare sets
        return [normalize(x) for x in v]
    return v

norm_actual = normalize(actual)
norm_expected = normalize(expected)

# Handle possible order differences in set/array results for 3sum/word-break/subsets
if isinstance(norm_actual, list) and isinstance(norm_expected, list):
    try:
        if sorted([str(x) for x in norm_actual]) == sorted([str(x) for x in norm_expected]):
            sys.exit(0)
    except:
        pass

if norm_actual == norm_expected:
    sys.exit(0)
else:
    print(f"FAILED: expected {norm_expected}, got {norm_actual}", file=sys.stderr)
    sys.exit(1)
`;

      fs.writeFileSync(tmpScript, pyScript, 'utf-8');

      try {
        execSync(`python3 "${tmpScript}"`, { stdio: 'pipe' });
        passedTests++;
      } catch (err: any) {
        probPassed = false;
        console.error(`  ❌ [${prob.id}] Case ${tc.id} Failed: ${err.stderr?.toString() || err.message}`);
      }
    }

    if (probPassed) {
      passedProblems++;
      console.log(`  ✅ [${prob.id}] Python 3 passed (${prob.testCases.length}/${prob.testCases.length})`);
    } else {
      console.error(`  ❌ [${prob.id}] FAILED in Python 3`);
    }
  }

  if (fs.existsSync(tmpScript)) {
    fs.unlinkSync(tmpScript);
  }

  console.log('\n=======================================');
  console.log(`PYTHON SUMMARY: ${passedProblems}/${totalProblems} problems passed.`);
  console.log(`TEST CASES: ${passedTests}/${totalTests} tests passed.`);
  console.log('=======================================');

  if (passedProblems !== totalProblems) {
    process.exit(1);
  }
}

verifyAllPython().catch((err) => {
  console.error(err);
  process.exit(1);
});
