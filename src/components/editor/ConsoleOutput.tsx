import React, { useState } from 'react';
import { useGameStore } from '../../store/useGameStore';
import { CheckCircle2, XCircle, Terminal, Swords, AlertTriangle } from 'lucide-react';

export const ConsoleOutput: React.FC = () => {
  const {
    currentProblem,
    lastReport,
    activeTestCaseId,
    setActiveTestCaseId,
    combatLogs,
  } = useGameStore();

  const [activeTab, setActiveTab] = useState<'tests' | 'logs'>('tests');

  const currentResult = lastReport?.results.find((r) => r.testCaseId === activeTestCaseId);
  const currentTestCase = currentProblem.testCases.find((t) => t.id === activeTestCaseId) || currentProblem.testCases[0];

  return (
    <div className="w-full flex flex-col bg-dungeon-dark/95 border border-dungeon-border rounded-xl overflow-hidden shadow-xl min-h-[220px]">
      {/* Console Tabs */}
      <div className="flex items-center justify-between px-3 py-2 bg-dungeon-darker/90 border-b border-dungeon-border">
        <div className="flex items-center gap-2">
          <button
            onClick={() => setActiveTab('tests')}
            className={`px-3 py-1 rounded-lg text-xs font-pixel flex items-center gap-1.5 transition-colors ${
              activeTab === 'tests'
                ? 'bg-slate-800 text-emerald-400 border border-emerald-500/30'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            <Terminal className="w-3.5 h-3.5" />
            <span>TEST SUITE</span>
          </button>
          <button
            onClick={() => setActiveTab('logs')}
            className={`px-3 py-1 rounded-lg text-xs font-pixel flex items-center gap-1.5 transition-colors ${
              activeTab === 'logs'
                ? 'bg-slate-800 text-rose-400 border border-rose-500/30'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            <Swords className="w-3.5 h-3.5" />
            <span>BATTLE LOGS</span>
          </button>
        </div>

        {/* Status Summary */}
        {lastReport && (
          <div className="flex items-center gap-2 text-xs font-pixel">
            <span className="text-[9px] text-slate-400 bg-slate-800 px-2 py-0.5 rounded border border-slate-700 uppercase">
              {lastReport.mode === 'run' ? 'SAMPLE TEST' : 'ATTACK SUBMISSION'}
            </span>
            {lastReport.allPassed ? (
              <span className="text-emerald-400 flex items-center gap-1">
                <CheckCircle2 className="w-4 h-4" /> ALL PASSED ({lastReport.passCount}/{lastReport.totalCount})
              </span>
            ) : (
              <span className="text-rose-400 flex items-center gap-1">
                <XCircle className="w-4 h-4" /> FAILED ({lastReport.passCount}/{lastReport.totalCount})
              </span>
            )}
          </div>
        )}
      </div>

      {/* Tab 1: Test Cases */}
      {activeTab === 'tests' ? (
        <div className="p-3 flex flex-col gap-3">
          {/* Global Error Banner */}
          {lastReport?.globalError && (
            <div className="p-2.5 rounded-lg bg-rose-950/70 border border-rose-600/50 text-rose-300 text-xs font-mono flex items-start gap-2">
              <AlertTriangle className="w-4 h-4 text-rose-400 flex-shrink-0 mt-0.5" />
              <div>
                <span className="font-pixel text-[9px] text-rose-400 mr-2">EXECUTION ERROR:</span>
                {lastReport.globalError}
              </div>
            </div>
          )}

          {/* Test Case Buttons */}
          <div className="flex items-center gap-2 flex-wrap">
            {currentProblem.testCases.map((tc) => {
              const res = lastReport?.results.find((r) => r.testCaseId === tc.id);
              const isSelected = activeTestCaseId === tc.id;

              // Hide extra edge cases until Submit Attack has been triggered
              if (tc.isHidden && lastReport?.mode !== 'submit') {
                return null;
              }

              return (
                <button
                  key={tc.id}
                  onClick={() => setActiveTestCaseId(tc.id)}
                  className={`px-2.5 py-1.5 rounded-lg text-xs font-pixel flex items-center gap-1.5 transition-all ${
                    isSelected
                      ? 'bg-slate-700 text-white border-2 border-sky-400 shadow'
                      : 'bg-dungeon-darker hover:bg-slate-800 text-slate-400 border border-slate-700'
                  }`}
                >
                  <span>{tc.isHidden ? `Edge ${tc.id}` : `Case ${tc.id}`}</span>
                  {res && (
                    res.passed ? (
                      <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
                    ) : (
                      <XCircle className="w-3.5 h-3.5 text-rose-400" />
                    )
                  )}
                </button>
              );
            })}

            {lastReport?.mode !== 'submit' && (
              <span className="text-[10px] font-mono text-slate-500 italic ml-1">
                + 7 Hidden Edge Cases tested on Attack ⚔️
              </span>
            )}
          </div>

          {/* Active Test Case Details */}
          <div className="bg-dungeon-darker/90 rounded-lg p-3 border border-slate-700/60 font-mono text-xs space-y-2">
            <div>
              <span className="text-slate-400 font-bold block mb-1">Input:</span>
              <div className="bg-dungeon-card p-2 rounded text-slate-200 border border-slate-800">
                {currentTestCase.inputDisplay}
              </div>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
              <div>
                <span className="text-emerald-400 font-bold block mb-1">Expected Output:</span>
                <div className="bg-dungeon-card p-2 rounded text-emerald-300 border border-slate-800">
                  {currentTestCase.expectedDisplay}
                </div>
              </div>

              <div>
                <span className="text-sky-400 font-bold block mb-1">Your Output:</span>
                <div
                  className={`bg-dungeon-card p-2 rounded border border-slate-800 ${
                    currentResult
                      ? currentResult.passed
                        ? 'text-emerald-300'
                        : 'text-rose-400 font-semibold'
                      : 'text-slate-500 italic'
                  }`}
                >
                  {currentResult ? currentResult.actualDisplay : 'Run logic to see output'}
                </div>
              </div>
            </div>

            {/* Error or Console Prints */}
            {currentResult?.error && (
              <div className="p-2 rounded bg-rose-950/60 border border-rose-800 text-rose-300 text-xs">
                <span className="font-bold text-rose-400">Error: </span>
                {currentResult.error}
              </div>
            )}

            {currentResult?.logs && currentResult.logs.length > 0 && (
              <div>
                <span className="text-slate-500 font-bold block mb-0.5">Console Output:</span>
                <pre className="bg-black/50 p-2 rounded text-slate-300 text-[11px] overflow-x-auto max-h-24">
                  {currentResult.logs.join('\n')}
                </pre>
              </div>
            )}
          </div>
        </div>
      ) : (
        /* Tab 2: Battle Logs */
        <div className="p-3 max-h-56 overflow-y-auto space-y-1.5 font-mono text-xs">
          {combatLogs.map((log) => (
            <div
              key={log.id}
              className={`p-2 rounded border text-xs ${
                log.type === 'damage'
                  ? 'bg-rose-950/40 border-rose-800/50 text-rose-300'
                  : log.type === 'critical'
                  ? 'bg-sky-950/40 border-sky-800/50 text-sky-300 font-bold'
                  : log.type === 'victory'
                  ? 'bg-emerald-950/40 border-emerald-800/50 text-emerald-300'
                  : 'bg-dungeon-darker border-slate-800 text-slate-300'
              }`}
            >
              <span className="text-[10px] font-pixel text-slate-500 mr-2 uppercase">
                [{log.sender}]
              </span>
              <span>{log.message}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
