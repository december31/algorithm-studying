import React from 'react';
import { useGameStore } from './store/useGameStore';
import { BattleArena } from './components/arena/BattleArena';
import { VisualizerHost } from './components/visualizers/VisualizerHost';
import { CodeEditor } from './components/editor/CodeEditor';
import { ConsoleOutput } from './components/editor/ConsoleOutput';
import { DungeonMap } from './components/screens/DungeonMap';
import { GameOverModal } from './components/screens/GameOverModal';
import { VictoryModal } from './components/screens/VictoryModal';
import { ShopModal } from './components/screens/ShopModal';
import { Map, ShoppingBag, Volume2, VolumeX, BookOpen, ExternalLink } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import { sfx } from './engine/sfx';

export const App: React.FC = () => {
  const { screen, previousScreen, setScreen, stats, currentFloor, currentProblem, isLoadingProblem } = useGameStore();
  const [muted, setMuted] = React.useState(sfx.isMuted());

  const toggleSound = () => {
    const isNowMuted = sfx.toggleMute();
    setMuted(isNowMuted);
  };

  // When an overlay modal like 'shop' is active, preserve the underlying base screen (map vs battle)
  const activeBaseScreen = screen === 'shop' || screen === 'victory' || screen === 'gameover' ? previousScreen : screen;

  return (
    <div className="min-h-screen bg-dungeon-darkest text-slate-100 flex flex-col font-sans selection:bg-rose-500 selection:text-white">
      {/* Streamlined Top Navigation Header */}
      <header className="sticky top-0 z-40 bg-dungeon-darker/95 backdrop-blur border-b border-dungeon-border px-3 sm:px-5 py-2.5 flex items-center justify-between shadow-md">
        {/* Game Title & Stage Badge */}
        <div className="flex items-center gap-3">
          <div
            className="flex items-center gap-2 cursor-pointer hover:opacity-90 transition-opacity"
            onClick={() => setScreen('map')}
          >
            <div className="w-8 h-8 rounded-lg bg-rose-950 border border-rose-600 flex items-center justify-center text-base shadow">
              ⚔️
            </div>
            <div>
              <h1 className="font-pixel text-xs sm:text-sm text-slate-100 tracking-wider">
                ALGODUNGEON
              </h1>
            </div>
          </div>

          {/* Current Floor Tag - Only show when on battle screen */}
          {activeBaseScreen === 'battle' && (
            <div className="hidden md:flex items-center gap-2 pl-3 border-l border-slate-700/60 font-mono text-xs">
              <span className="font-pixel text-[10px] text-amber-400 bg-amber-950/60 border border-amber-600/40 px-2 py-0.5 rounded">
                FLOOR {currentFloor}/10
              </span>
              <span className="text-slate-300 font-bold">{currentProblem.title}</span>
              {currentProblem.leetcodeUrl && (
                <a
                  href={currentProblem.leetcodeUrl}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-1 text-[10px] font-pixel text-amber-400/90 hover:text-amber-300 bg-amber-950/40 hover:bg-amber-900/50 border border-amber-600/30 px-2 py-0.5 rounded transition-colors"
                  title={`LeetCode #${currentProblem.leetcodeId}: ${currentProblem.leetcodeTitle}`}
                >
                  <span>LC #{currentProblem.leetcodeId}</span>
                  <ExternalLink className="w-2.5 h-2.5" />
                </a>
              )}
            </div>
          )}
        </div>

        {/* Vital Stats & Global Controls */}
        <div className="flex items-center gap-2 sm:gap-3">
          {/* Gold */}
          <div className="flex items-center gap-1 font-pixel text-xs text-amber-400 bg-dungeon-card px-2.5 py-1.5 rounded-xl border border-slate-700">
            <span>💰</span>
            <span>{stats.gold}</span>
          </div>

          {/* Shop */}
          <button
            onClick={() => setScreen('shop')}
            className={`p-2 sm:px-3 sm:py-1.5 rounded-xl font-pixel text-xs flex items-center gap-1.5 transition-colors border ${
              screen === 'shop'
                ? 'bg-amber-600 text-slate-950 border-amber-400 shadow-md font-bold'
                : 'bg-dungeon-card hover:bg-slate-800 text-amber-400 border-slate-700'
            }`}
            title="Dungeon Merchant Shop"
          >
            <ShoppingBag className="w-4 h-4" />
            <span className="hidden sm:inline">SHOP</span>
          </button>

          {/* Map Nav */}
          <button
            onClick={() => setScreen(activeBaseScreen === 'map' ? 'battle' : 'map')}
            className={`px-3 py-1.5 rounded-xl font-pixel text-xs flex items-center gap-1.5 transition-colors border ${
              activeBaseScreen === 'map'
                ? 'bg-sky-600 text-white border-sky-400 shadow-md'
                : 'bg-dungeon-card text-slate-300 hover:text-white border-slate-700'
            }`}
          >
            <Map className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">{activeBaseScreen === 'map' ? 'ARENA' : 'MAP'}</span>
          </button>

          {/* Audio Mute/Unmute */}
          <button
            onClick={toggleSound}
            className="p-2 rounded-xl bg-dungeon-card hover:bg-slate-800 text-slate-400 hover:text-slate-200 border border-slate-700 transition-colors"
            title={muted ? 'Unmute Sound' : 'Mute Sound'}
          >
            {muted ? <VolumeX className="w-4 h-4 text-rose-400" /> : <Volume2 className="w-4 h-4 text-emerald-400" />}
          </button>
        </div>
      </header>

      {/* Main Content Area */}
      <main className="flex-1 p-3 sm:p-5 max-w-7xl mx-auto w-full">
        {activeBaseScreen === 'map' ? (
          <DungeonMap />
        ) : isLoadingProblem ? (
          <div className="flex flex-col items-center justify-center min-h-[420px] bg-dungeon-dark/95 border border-dungeon-border rounded-xl p-8 text-center space-y-4 shadow-xl">
            <div className="w-16 h-16 rounded-2xl bg-rose-950/80 border border-rose-500/50 flex items-center justify-center text-3xl animate-bounce shadow-[0_0_20px_rgba(244,63,94,0.4)]">
              ⚔️
            </div>
            <div className="space-y-1">
              <h2 className="font-pixel text-sm sm:text-base text-amber-400 tracking-wider">
                SUMMONING FLOOR {currentFloor} ENCOUNTER...
              </h2>
              <p className="font-mono text-xs text-slate-400">
                Streaming challenge schema, test cases & monster state from dungeon vault...
              </p>
            </div>
            <div className="w-48 h-1.5 bg-slate-800 rounded-full overflow-hidden">
              <div className="h-full bg-gradient-to-r from-rose-500 via-amber-400 to-sky-400 animate-pulse rounded-full" />
            </div>
          </div>
        ) : (
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-4 items-start">
            {/* Left Column: Battle Arena + Challenge Description + Data Structure Visualizer */}
            <div className="flex flex-col gap-4">
              {/* Sleek Compact Battle Arena */}
              <BattleArena />

              {/* Challenge Description (Always Extended above Visualizer) */}
              <div className="bg-dungeon-dark/95 border border-dungeon-border rounded-xl p-4 shadow-md space-y-3">
                <div className="flex flex-wrap items-center justify-between pb-2.5 border-b border-slate-800 gap-2">
                  <div className="flex items-center gap-2 font-pixel text-xs text-sky-400 min-w-0">
                    <BookOpen className="w-4 h-4 text-sky-400 flex-shrink-0" />
                    <span>CHALLENGE: {currentProblem.title}</span>
                  </div>
                  <div className="flex items-center gap-2 flex-shrink-0">
                    {currentProblem.leetcodeUrl && (
                      <a
                        href={currentProblem.leetcodeUrl}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-amber-500/10 hover:bg-amber-500/20 border border-amber-500/40 text-amber-400 font-pixel text-[10px] transition-colors shadow-sm group"
                        title={`View on LeetCode: #${currentProblem.leetcodeId} ${currentProblem.leetcodeTitle}`}
                      >
                        <span>LeetCode #{currentProblem.leetcodeId}</span>
                        <ExternalLink className="w-3 h-3 group-hover:translate-x-0.5 group-hover:-translate-y-0.5 transition-transform" />
                      </a>
                    )}
                    <span
                      className={`px-2 py-0.5 rounded text-[10px] font-pixel font-bold uppercase ${
                        currentProblem.difficulty === 'easy'
                          ? 'bg-emerald-950/70 border border-emerald-600/40 text-emerald-400'
                          : currentProblem.difficulty === 'medium'
                          ? 'bg-amber-950/70 border border-amber-600/40 text-amber-400'
                          : 'bg-rose-950/70 border border-rose-600/40 text-rose-400'
                      }`}
                    >
                      {currentProblem.difficulty}
                    </span>
                  </div>
                </div>

                <div className="font-sans text-sm text-slate-200 leading-relaxed space-y-3">
                  <p className="whitespace-pre-line">{currentProblem.description}</p>

                  {/* Examples */}
                  {currentProblem.examples && currentProblem.examples.length > 0 && (
                    <div>
                      <h4 className="font-pixel text-[10px] text-amber-400 mb-1.5 uppercase tracking-wide">
                        Examples:
                      </h4>
                      <div className="space-y-1.5">
                        {currentProblem.examples.map((ex, i) => (
                          <div
                            key={i}
                            className="bg-dungeon-darker/90 p-2.5 rounded-lg border border-slate-800/80 font-mono text-xs space-y-0.5"
                          >
                            <div className="text-slate-400">
                              Input: <span className="text-slate-200">{ex.input}</span>
                            </div>
                            <div className="text-emerald-400">
                              Output: <span className="text-slate-200">{ex.output}</span>
                            </div>
                            {ex.explanation && (
                              <div className="text-slate-500 text-[11px] pt-0.5">{ex.explanation}</div>
                            )}
                          </div>
                        ))}
                      </div>
                    </div>
                  )}

                  {/* Constraints */}
                  {currentProblem.constraints && currentProblem.constraints.length > 0 && (
                    <div>
                      <h4 className="font-pixel text-[10px] text-purple-400 mb-1 uppercase tracking-wide">
                        Constraints:
                      </h4>
                      <ul className="list-disc list-inside font-mono text-xs text-slate-400 space-y-0.5">
                        {currentProblem.constraints.map((c, i) => (
                          <li key={i}>{c}</li>
                        ))}
                      </ul>
                    </div>
                  )}
                </div>
              </div>

              {/* Live Synchronized Algorithm Visualizer */}
              <VisualizerHost />
            </div>

            {/* Right Column: Code Editor + Test Suite Results */}
            <div className="flex flex-col gap-4">
              <CodeEditor />
              <ConsoleOutput />
            </div>
          </div>
        )}
      </main>

      {/* Active Modals with Enter & Dismiss Animations */}
      <AnimatePresence>
        {screen === 'gameover' && <GameOverModal key="modal-gameover" />}
        {screen === 'victory' && <VictoryModal key="modal-victory" />}
        {screen === 'shop' && <ShopModal key="modal-shop" />}
      </AnimatePresence>
    </div>
  );
};

export default App;
