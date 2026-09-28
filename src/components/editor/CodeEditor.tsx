import React, { useState } from 'react';
import CodeMirror from '@uiw/react-codemirror';
import { python } from '@codemirror/lang-python';
import { javascript } from '@codemirror/lang-javascript';
import { oneDark } from '@codemirror/theme-one-dark';
import { indentUnit } from '@codemirror/language';
import { EditorState, Prec } from '@codemirror/state';
import { keymap } from '@codemirror/view';
import { indentMore, indentLess } from '@codemirror/commands';
import { useGameStore, getStarterCode, getSolutionCode } from '../../store/useGameStore';
import { executeSolution } from '../../engine/runner';
import { executePythonSolution } from '../../engine/pythonRunner';
import { Play, RotateCcw, Lightbulb, Code2, BookOpen, Swords } from 'lucide-react';

// Smart 4-space Tab command: indents selected lines or inserts spaces up to the next 4-space tab stop
const smartTab = ({ state, dispatch }: { state: any; dispatch: any }) => {
  if (state.selection.ranges.some((r: any) => !r.empty)) {
    return indentMore({ state, dispatch });
  }
  const range = state.selection.main;
  const line = state.doc.lineAt(range.head);
  const col = range.head - line.from;
  const spaces = 4 - (col % 4);
  dispatch(
    state.update(state.replaceSelection(' '.repeat(spaces)), {
      scrollIntoView: true,
      userEvent: 'input',
    })
  );
  return true;
};

const customTabKeymap = Prec.highest(
  keymap.of([
    { key: 'Tab', run: smartTab, shift: indentLess },
  ])
);

export const CodeEditor: React.FC = () => {
  const {
    currentProblem,
    code,
    setCode,
    language,
    setLanguage,
    isRunning,
    setRunning,
    setExecutionReport,
    takeSacrificeHealth,
  } = useGameStore();

  const [activeTab, setActiveTab] = useState<'editor' | 'description'>('editor');
  const [showHintIndex, setShowHintIndex] = useState<number>(-1);

  const editorExtensions = React.useMemo(() => {
    const langExt = language === 'python' ? python() : javascript({ jsx: false, typescript: false });
    return [
      langExt,
      indentUnit.of('    '),
      EditorState.tabSize.of(4),
      customTabKeymap,
    ];
  }, [language]);

  // Run Code (Safe Test on 3 Sample Cases)
  const handleRunCode = async () => {
    if (isRunning) return;
    setRunning(true);
    try {
      const report = language === 'python'
        ? await executePythonSolution(currentProblem, code, 'run')
        : await executeSolution(currentProblem, code, 'run');
      setExecutionReport(report);
    } catch (err: any) {
      setExecutionReport({
        mode: 'run',
        allPassed: false,
        passCount: 0,
        totalCount: 3,
        results: [],
        globalError: err?.message || String(err),
      });
    } finally {
      setRunning(false);
    }
  };

  // Attack Monster (Submit Full Suite of 10 Cases)
  const handleSubmitAttack = async () => {
    if (isRunning) return;
    setRunning(true);
    try {
      const report = language === 'python'
        ? await executePythonSolution(currentProblem, code, 'submit')
        : await executeSolution(currentProblem, code, 'submit');
      setExecutionReport(report);
    } catch (err: any) {
      setExecutionReport({
        mode: 'submit',
        allPassed: false,
        passCount: 0,
        totalCount: currentProblem.testCases.length,
        results: [],
        globalError: err?.message || String(err),
      });
    } finally {
      setRunning(false);
    }
  };

  const handleReset = () => {
    if (window.confirm('Reset code to starter template?')) {
      setCode(getStarterCode(currentProblem, language));
    }
  };

  const handleLoadSolution = () => {
    if (
      window.confirm(
        `Load reference ${language === 'python' ? 'Python' : 'JavaScript'} solution? This forbidden knowledge will sacrifice 15 HP!`
      )
    ) {
      if (takeSacrificeHealth(15, 'Forbidden Solution')) {
        setCode(getSolutionCode(currentProblem, language));
      }
    }
  };

  const handleToggleHint = () => {
    if (showHintIndex < currentProblem.hints.length - 1) {
      if (takeSacrificeHealth(5, 'Hint Revelation')) {
        setShowHintIndex((prev) => prev + 1);
      }
    } else {
      setShowHintIndex(-1);
    }
  };

  return (
    <div className="w-full flex flex-col bg-dungeon-dark/95 border border-dungeon-border rounded-xl overflow-hidden shadow-xl">
      {/* Editor Header Navigation */}
      <div className="flex flex-wrap items-center justify-between gap-2 px-3 py-2 bg-dungeon-darker/90 border-b border-dungeon-border">
        {/* Left: Tab Toggle & Language Switcher */}
        <div className="flex items-center gap-2">
          {/* Code vs Description */}
          <div className="flex items-center gap-1">
            <button
              onClick={() => setActiveTab('editor')}
              className={`px-2.5 py-1.5 rounded-lg text-xs font-pixel flex items-center gap-1.5 transition-colors ${
                activeTab === 'editor'
                  ? 'bg-slate-800 text-sky-400 border border-sky-500/30'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
            >
              <Code2 className="w-3.5 h-3.5" />
              <span>CODE</span>
            </button>
            <button
              onClick={() => setActiveTab('description')}
              className={`px-2.5 py-1.5 rounded-lg text-xs font-pixel flex items-center gap-1.5 transition-colors ${
                activeTab === 'description'
                  ? 'bg-slate-800 text-amber-400 border border-amber-500/30'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
            >
              <BookOpen className="w-3.5 h-3.5" />
              <span>INFO</span>
            </button>
          </div>

          {/* Language Selector (Python by default) */}
          <div className="flex items-center bg-dungeon-darkest border border-slate-700/80 rounded-lg p-0.5 font-pixel text-[10px]">
            <button
              onClick={() => setLanguage('python')}
              className={`px-2 py-1 rounded transition-colors ${
                language === 'python'
                  ? 'bg-amber-500 text-slate-950 font-bold shadow'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
              title="Python 3.12 (via Pyodide WebAssembly)"
            >
              🐍 Python
            </button>
            <button
              onClick={() => setLanguage('javascript')}
              className={`px-2 py-1 rounded transition-colors ${
                language === 'javascript'
                  ? 'bg-sky-500 text-slate-950 font-bold shadow'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
              title="JavaScript ES6"
            >
              ⚡ JS
            </button>
          </div>
        </div>

        {/* Right: Actions: Solution, Hints, Reset, Run, Attack */}
        <div className="flex items-center gap-1.5 sm:gap-2">
          {/* Load Solution Button */}
          <button
            onClick={handleLoadSolution}
            className="px-2 sm:px-2.5 py-1.5 rounded-lg bg-purple-950/70 hover:bg-purple-900 border border-purple-600/40 text-purple-300 font-pixel text-[10px] flex items-center gap-1 transition-colors"
            title="Load reference solution (-15 HP)"
          >
            <span>💡</span>
            <span className="hidden sm:inline">SOLUTION (-15 HP)</span>
          </button>

          {/* Hints Toggle */}
          <button
            onClick={handleToggleHint}
            className="px-2 sm:px-2.5 py-1.5 rounded-lg bg-amber-950/60 hover:bg-amber-900/60 border border-amber-600/40 text-amber-300 font-pixel text-[10px] flex items-center gap-1 transition-colors"
            title="Reveal hint (-5 HP)"
          >
            <Lightbulb className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">HINT (-5 HP)</span>
          </button>

          {/* Reset Code */}
          <button
            onClick={handleReset}
            className="p-1.5 rounded-lg hover:bg-slate-800 text-slate-400 hover:text-slate-200 transition-colors"
            title="Reset code"
          >
            <RotateCcw className="w-3.5 h-3.5" />
          </button>

          {/* Run 3 Sample Cases (Safe Test) */}
          <button
            onClick={handleRunCode}
            disabled={isRunning}
            className="px-2.5 sm:px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-sky-400 border border-sky-500/40 disabled:opacity-50 font-pixel text-[10px] sm:text-[11px] font-bold flex items-center gap-1.5 transition-all active:scale-95 shadow"
            title="Run 3 sample test cases safely without combat damage"
          >
            <Play className="w-3 h-3 fill-current" />
            <span>{isRunning ? 'TESTING...' : 'RUN (3 SAMPLES)'}</span>
          </button>

          {/* Attack Monster (Submit Full Suite) */}
          <button
            onClick={handleSubmitAttack}
            disabled={isRunning}
            className="px-3 sm:px-3.5 py-1.5 rounded-lg bg-gradient-to-r from-emerald-500 via-teal-500 to-sky-500 hover:from-emerald-400 hover:to-sky-400 disabled:opacity-50 text-slate-950 font-pixel text-[10px] sm:text-[11px] font-bold flex items-center gap-1.5 shadow-lg shadow-emerald-950/40 transition-all active:scale-95"
            title="Attack monster with full 10-test suite submission!"
          >
            <Swords className="w-3.5 h-3.5" />
            <span>{isRunning ? 'ATTACKING...' : 'ATTACK (SUBMIT)'}</span>
          </button>
        </div>
      </div>

      {/* Hints Banner if active */}
      {showHintIndex >= 0 && (
        <div className="px-4 py-2 bg-amber-950/40 border-b border-amber-600/30 flex items-start gap-2">
          <Lightbulb className="w-4 h-4 text-amber-400 flex-shrink-0 mt-0.5" />
          <div className="text-xs font-mono text-amber-200">
            <span className="font-pixel text-[9px] text-amber-400 mr-2">HINT #{showHintIndex + 1}:</span>
            {currentProblem.hints[showHintIndex]}
          </div>
        </div>
      )}

      {/* Editor Body */}
      {activeTab === 'editor' ? (
        <div className="w-full text-sm font-mono overflow-auto max-h-[360px]">
          <CodeMirror
            value={code}
            height="340px"
            theme={oneDark}
            extensions={editorExtensions}
            indentWithTab={false}
            onChange={(val) => setCode(val)}
            basicSetup={{
              lineNumbers: true,
              foldGutter: true,
              highlightActiveLine: true,
              indentOnInput: true,
            }}
          />
        </div>
      ) : (
        /* Problem Description View */
        <div className="p-4 overflow-y-auto max-h-[340px] space-y-4 text-slate-300">
          <div>
            <h3 className="font-pixel text-xs text-sky-400 mb-2">DESCRIPTION</h3>
            <p className="font-sans text-sm leading-relaxed whitespace-pre-line text-slate-200">
              {currentProblem.description}
            </p>
          </div>

          <div>
            <h4 className="font-pixel text-[10px] text-amber-400 mb-2">EXAMPLES</h4>
            <div className="space-y-2">
              {currentProblem.examples.map((ex, i) => (
                <div key={i} className="bg-dungeon-darker p-2.5 rounded-lg border border-slate-700/60 font-mono text-xs">
                  <div className="text-slate-400">Input: <span className="text-slate-200">{ex.input}</span></div>
                  <div className="text-emerald-400">Output: <span className="text-slate-200">{ex.output}</span></div>
                  {ex.explanation && (
                    <div className="text-slate-500 text-[11px] mt-1">{ex.explanation}</div>
                  )}
                </div>
              ))}
            </div>
          </div>

          <div>
            <h4 className="font-pixel text-[10px] text-purple-400 mb-1">CONSTRAINTS</h4>
            <ul className="list-disc list-inside font-mono text-xs text-slate-400 space-y-0.5">
              {currentProblem.constraints.map((c, i) => (
                <li key={i}>{c}</li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </div>
  );
};
