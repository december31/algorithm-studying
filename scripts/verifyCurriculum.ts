import { problemCatalog, loadProblem } from '../src/data/problems/loader';
import { executeSolution } from '../src/engine/runner';
import { DungeonTopic } from '../src/types/game';

async function verifyAll() {
  console.log(`⚔️  VERIFYING ALGODUNGEON CURRICULUM (ALL 5 TOPICS / ${problemCatalog.length} PROBLEMS FROM JSON DATABASE)...`);
  let totalProblems = 0;
  let passedProblems = 0;
  let totalTests = 0;
  let passedTests = 0;

  const topics: DungeonTopic[] = [
    'data-structures',
    'backtracking',
    'graphs',
    'binary-search-greedy',
    'bit-manipulation',
  ];

  for (const topic of topics) {
    const topicEntries = problemCatalog.filter((p) => p.wingId === topic);
    console.log(`\n=== Topic Wing: ${topic.toUpperCase()} (${topicEntries.length} Problems) ===`);

    for (const entry of topicEntries) {
      totalProblems++;
      const prob = await loadProblem(entry.id);
      totalTests += prob.testCases.length;

      // Test with starter/solution code
      const codeToTest = prob.solutionCode || prob.starterCode;
      const report = await executeSolution(prob, codeToTest);

      passedTests += report.passCount;

      if (report.allPassed) {
        passedProblems++;
        console.log(`  ✅ [${prob.difficulty.toUpperCase()}] ${prob.title} - ${report.passCount}/${prob.testCases.length} tests passed`);
      } else {
        console.error(`  ❌ [${prob.difficulty.toUpperCase()}] ${prob.title} FAILED:`, report.globalError || 'Test failure');
        for (const res of report.results) {
          if (!res.passed) {
            console.error(`     - Case ${res.testCaseId} Failed: expected ${res.expectedDisplay}, got ${res.actualDisplay}`);
            if (res.error) console.error(`       Error: ${res.error}`);
          }
        }
      }

      // Verify frame generation
      for (const tc of prob.testCases) {
        const frames = prob.generateDefaultFrames(tc);
        if (!frames || frames.length === 0) {
          console.warn(`     ⚠️ Warning: No default frames generated for Case ${tc.id}`);
        }
      }
    }
  }

  console.log('\n=======================================');
  console.log(`SUMMARY: ${passedProblems}/${totalProblems} problems passed.`);
  console.log(`TEST CASES: ${passedTests}/${totalTests} tests passed.`);
  console.log('=======================================');

  if (passedProblems !== totalProblems) {
    process.exit(1);
  }
}

verifyAll().catch((err) => {
  console.error(err);
  process.exit(1);
});
