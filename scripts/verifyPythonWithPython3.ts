import { allProblems } from '../src/data/problems';
import { pythonCurriculum } from '../src/data/pythonCurriculum';
import { DungeonTopic } from '../src/types/game';
import { execSync } from 'child_process';
import * as fs from 'fs';
import * as path from 'path';

async function verifyAllPython() {
  console.log('🐍 VERIFYING ALL 83 PYTHON SOLUTIONS WITH PYTHON 3.13...');
  let totalProblems = 0;
  let passedProblems = 0;
  let totalTests = 0;
  let passedTests = 0;

  const topics = Object.keys(allProblems) as DungeonTopic[];
  const tmpScript = path.join(process.cwd(), 'scripts', '_temp_py_test.py');

  for (const topic of topics) {
    console.log(`\n=== Topic Wing: ${topic.toUpperCase()} ===`);
    const problems = allProblems[topic];

    for (const prob of problems) {
      totalProblems++;
      const pyEntry = pythonCurriculum[prob.id];
      if (!pyEntry) {
        console.error(`  ❌ Missing pythonCurriculum entry for ${prob.id}`);
        continue;
      }

      // Check clean starter code
      if (pyEntry.starterCode.includes('#') || pyEntry.starterCode.includes('"""') || pyEntry.starterCode.includes("'''")) {
        console.error(`  ⚠️ Starter code contains comments or hints for ${prob.id}!`);
      }

      const solCode = pyEntry.solutionCode;
      let probPassed = true;

      for (const tc of prob.testCases) {
        totalTests++;

        // Prepare test runner script
        const pyScript = `import json
import sys

${solCode}

inputs = json.loads('''${JSON.stringify(tc.input)}''')
expected = json.loads('''${JSON.stringify(tc.expected)}''')

actual = ${prob.functionName}(*inputs)

def normalize(v):
    if isinstance(v, (list, tuple)):
        return [normalize(x) for x in v]
    return v

norm_actual = normalize(actual)
norm_expected = normalize(expected)

if norm_actual == norm_expected:
    print("PASS")
    sys.exit(0)
else:
    print(f"FAIL: expected {norm_expected}, got {norm_actual}")
    sys.exit(1)
`;

        fs.writeFileSync(tmpScript, pyScript, 'utf-8');

        try {
          execSync(`python3 "${tmpScript}"`, { timeout: 3000, stdio: 'pipe' });
          passedTests++;
        } catch (err: any) {
          probPassed = false;
          const out = err.stdout ? err.stdout.toString() : err.message;
          const stderr = err.stderr ? err.stderr.toString() : '';
          console.error(`  ❌ [${prob.id}] Case ${tc.id} failed:`, out.trim(), stderr.trim());
        }
      }

      if (probPassed) {
        passedProblems++;
        console.log(`  ✅ ${prob.title} (${prob.difficulty}) - ${prob.testCases.length}/${prob.testCases.length} Python tests passed`);
      }
    }
  }

  if (fs.existsSync(tmpScript)) fs.unlinkSync(tmpScript);

  console.log('\n=======================================');
  console.log(`PYTHON SUMMARY: ${passedProblems}/${totalProblems} problems passed.`);
  console.log(`PYTHON TEST CASES: ${passedTests}/${totalTests} tests passed.`);
  console.log('=======================================');

  if (passedProblems !== totalProblems) {
    process.exit(1);
  }
}

verifyAllPython().catch((err) => {
  console.error('Fatal python verification error:', err);
  process.exit(1);
});
