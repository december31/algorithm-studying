import React, { useState } from 'react';
import { useGameStore } from '../../store/useGameStore';
import { DUNGEON_WINGS } from '../../data/wings';
import { DungeonTopic } from '../../types/game';
import {
  Layers,
  Coins,
  GitCommit,
  GitBranch,
  Network,
  Table,
  ShoppingBag,
  Heart,
  Sparkles,
  Play,
  RotateCcw,
  X,
  Swords,
  ShieldAlert,
  Scale,
} from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

export const DungeonMap: React.FC = () => {
  const { stats, unlockedFloors, activeWingRuns, startNewRun, continueRun, setScreen, healPlayer } = useGameStore();
  const [selectedWingForPrompt, setSelectedWingForPrompt] = useState<DungeonTopic | null>(null);

  const getWingIcon = (icon: string) => {
    switch (icon) {
      case 'Layers': return <Layers className="w-6 h-6" />;
      case 'Coins': return <Coins className="w-6 h-6" />;
      case 'GitCommit': return <GitCommit className="w-6 h-6" />;
      case 'GitBranch': return <GitBranch className="w-6 h-6" />;
      case 'Network': return <Network className="w-6 h-6" />;
      case 'Table': return <Table className="w-6 h-6" />;
      case 'Sparkles': return <Sparkles className="w-6 h-6" />;
      case 'ShieldAlert': return <ShieldAlert className="w-6 h-6" />;
      case 'Scale': return <Scale className="w-6 h-6" />;
      default: return <Layers className="w-6 h-6" />;
    }
  };

  const handleWingClick = (wingId: DungeonTopic) => {
    const activeRun = activeWingRuns[wingId];
    if (activeRun && activeRun.status === 'in_progress' && activeRun.currentFloor >= 1) {
      setSelectedWingForPrompt(wingId);
    } else {
      startNewRun(wingId);
    }
  };

  const promptWingData = selectedWingForPrompt
    ? DUNGEON_WINGS.find((w) => w.id === selectedWingForPrompt)
    : null;
  const promptRunData = selectedWingForPrompt ? activeWingRuns[selectedWingForPrompt] : null;
  const promptFloor = promptRunData?.currentFloor || 1;
  const promptFloorEntry = promptRunData?.currentRunCatalog?.[promptFloor - 1];

  return (
    <div className="w-full max-w-6xl mx-auto p-4 sm:p-6 space-y-6">
      {/* Top Banner / Hero Profile */}
      <div className="bg-dungeon-card/90 border border-dungeon-border p-4 rounded-2xl shadow-xl flex flex-wrap items-center justify-between gap-4">
        <div className="flex items-center gap-3">
          <div className="w-12 h-12 rounded-xl bg-sky-950 border border-sky-500/50 flex items-center justify-center font-pixel text-lg text-sky-400">
            🧙‍♂️
          </div>
          <div>
            <div className="font-pixel text-xs text-sky-400">HERO ARCHMAGE</div>
            <div className="text-xs font-mono text-slate-400">
              Level {stats.level} • {stats.totalSolved} Algorithmic Monsters Banished
            </div>
          </div>
        </div>

        {/* Player Vital Stats */}
        <div className="flex items-center gap-4 flex-wrap">
          {/* Health & Shield Bar */}
          <div className="flex items-center gap-2 bg-dungeon-darkest px-3 py-1.5 rounded-xl border border-slate-800">
            <Heart className="w-4 h-4 fill-rose-500 text-rose-500" />
            <span className="font-mono text-xs text-slate-200 font-bold">
              {stats.hp} <span className="text-slate-500">/ {stats.maxHp} HP</span>
            </span>
            {stats.shieldPassedCount > 0 && (
              <span className="font-pixel text-[9px] text-sky-400 bg-sky-950/80 px-1.5 py-0.5 rounded border border-sky-600/40">
                🛡️ -{stats.shield}%
              </span>
            )}
          </div>

          {/* Gold */}
          <div className="font-pixel text-xs text-amber-400 bg-dungeon-darkest px-3 py-2 rounded-xl border border-slate-800">
            💰 {stats.gold} GOLD
          </div>

          {/* Rest at Camp (Full Heal) when damaged */}
          {stats.hp < stats.maxHp && (
            <button
              onClick={() => healPlayer(stats.maxHp)}
              className="px-3 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-slate-950 font-pixel text-xs font-bold flex items-center gap-1.5 transition-colors shadow"
              title="Rest at Camp to restore full health before your next dungeon run"
            >
              <span>🏕️</span>
              <span>REST (+{stats.maxHp - stats.hp} HP)</span>
            </button>
          )}

          {/* Shop Button */}
          <button
            onClick={() => setScreen('shop')}
            className="px-3 py-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-slate-950 font-pixel text-xs font-bold flex items-center gap-1.5 transition-colors shadow"
          >
            <ShoppingBag className="w-4 h-4" />
            <span>SHOP</span>
          </button>
        </div>
      </div>

      {/* World Map Title */}
      <div className="text-center py-2">
        <h1 className="font-pixel text-xl sm:text-2xl text-slate-100 tracking-wider">
          THE REALMS OF ALGORITHMS
        </h1>
        <p className="font-mono text-xs sm:text-sm text-slate-400 mt-1">
          Select a topic dungeon to venture into the depths (10 Floors: Easy → Medium → Boss)
        </p>
      </div>

      {/* 5 Topic Dungeons Grid (Uniform Cards) */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        {DUNGEON_WINGS.filter((w) => !w.isSpecialTrial).map((wing) => {
          const unlockedFloor = unlockedFloors[wing.id] || 1;
          const activeRun = activeWingRuns[wing.id];
          const hasActiveRun = activeRun && activeRun.status === 'in_progress' && activeRun.currentFloor >= 1;

          return (
            <motion.div
              key={wing.id}
              whileHover={{ y: -4, scale: 1.01 }}
              transition={{ type: 'spring', stiffness: 300, damping: 20 }}
              onClick={() => handleWingClick(wing.id)}
              className={`bg-dungeon-card/90 hover:bg-dungeon-card border-2 rounded-2xl p-5 cursor-pointer shadow-xl flex flex-col justify-between group transition-all relative overflow-hidden ${
                hasActiveRun
                  ? 'border-amber-500/80 shadow-[0_0_25px_rgba(245,158,11,0.2)]'
                  : 'border-dungeon-border hover:border-slate-500'
              }`}
            >
              {/* Subtle Wing Color Accent Stripe */}
              <div
                className="absolute top-0 left-0 right-0 h-1.5 opacity-80"
                style={{ backgroundColor: wing.color }}
              />

              <div>
                {/* Icon & Progress */}
                <div className="flex items-center justify-between mb-3">
                  <div
                    className="p-2.5 rounded-xl text-white shadow-md"
                    style={{ backgroundColor: wing.color }}
                  >
                    {getWingIcon(wing.icon)}
                  </div>
                  {hasActiveRun ? (
                    <span className="font-pixel text-[10px] text-amber-300 bg-amber-950/90 border border-amber-500/70 px-2 py-0.5 rounded shadow-[0_0_10px_rgba(245,158,11,0.3)] animate-pulse flex items-center gap-1">
                      <span>⚔️</span>
                      <span>RESUME FL {activeRun.currentFloor}/{wing.floorsCount}</span>
                    </span>
                  ) : (
                    <span className="font-pixel text-[10px] text-emerald-400 bg-emerald-950/80 border border-emerald-700/50 px-2 py-0.5 rounded">
                      FLOOR {unlockedFloor} / {wing.floorsCount}
                    </span>
                  )}
                </div>

                <h3 className="font-pixel text-xs sm:text-sm text-slate-100 group-hover:text-amber-400 transition-colors mb-1">
                  {wing.name}
                </h3>
                <p className="font-mono text-xs text-slate-400 mb-3 leading-relaxed">
                  {wing.subtitle}
                </p>
              </div>

              {/* Enter Wing CTA */}
              <div
                className={`pt-3 border-t border-slate-800 flex items-center justify-between font-pixel text-[10px] group-hover:translate-x-1 transition-transform ${
                  hasActiveRun ? 'text-amber-400 font-bold' : 'text-sky-400'
                }`}
              >
                <span>{hasActiveRun ? 'CONTINUE OR RESTART' : 'ENTER DUNGEON'}</span>
                <span>➔</span>
              </div>
            </motion.div>
          );
        })}
      </div>

      {/* Visual Section Separator */}
      {DUNGEON_WINGS.some((w) => w.isSpecialTrial) && (
        <>
          <div className="relative py-4 flex items-center justify-center">
            <div className="absolute inset-0 flex items-center">
              <div className="w-full border-t border-slate-800" />
            </div>
            <div className="relative bg-dungeon-darkest px-4 flex items-center gap-2 border border-slate-800 rounded-full py-1.5 text-slate-400 font-pixel text-xs shadow-md">
              <Swords className="w-4 h-4 text-rose-500" />
              <span className="text-slate-200 tracking-wider">SPECIAL BOSS EXPEDITIONS</span>
              <span className="text-[10px] text-rose-400 bg-rose-950/80 px-2 py-0.5 rounded border border-rose-600/40">
                PREREQUISITE TRAILS
              </span>
            </div>
          </div>

          {/* Special Boss Expeditions Section */}
          <div className="space-y-4">
            <div className="text-center sm:text-left">
              <h2 className="font-pixel text-sm sm:text-base text-slate-100 tracking-wide flex items-center justify-center sm:justify-start gap-2">
                <span>👑</span>
                <span>TARGETED ASCENSION TRIALS</span>
              </h2>
              <p className="font-mono text-xs text-slate-400 mt-0.5">
                Curated stepping-stone paths designed to master foundational sub-skills before conquering legendary Hard problems.
              </p>
            </div>

            <div className="grid grid-cols-1 gap-5">
              {DUNGEON_WINGS.filter((w) => w.isSpecialTrial).map((wing) => {
                const unlockedFloor = unlockedFloors[wing.id] || 1;
                const activeRun = activeWingRuns[wing.id];
                const hasActiveRun = activeRun && activeRun.status === 'in_progress' && activeRun.currentFloor >= 1;

                return (
                  <motion.div
                    key={wing.id}
                    whileHover={{ y: -2, scale: 1.005 }}
                    transition={{ type: 'spring', stiffness: 300, damping: 20 }}
                    onClick={() => handleWingClick(wing.id)}
                    className={`bg-dungeon-card/90 hover:bg-dungeon-card border-2 rounded-2xl p-5 sm:p-6 cursor-pointer shadow-xl transition-all relative overflow-hidden group ${
                      hasActiveRun
                        ? 'border-amber-500/80 shadow-[0_0_30px_rgba(245,158,11,0.25)]'
                        : 'border-rose-900/60 hover:border-rose-600/80 shadow-[0_0_20px_rgba(244,63,94,0.1)]'
                    }`}
                  >
                    {/* Accent stripe */}
                    <div
                      className="absolute top-0 left-0 right-0 h-1.5 opacity-90"
                      style={{ backgroundColor: wing.color }}
                    />

                    <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
                      {/* Left Column: Wing Info (5 cols) */}
                      <div className="lg:col-span-5 space-y-3">
                        <div className="flex items-center gap-3">
                          <div
                            className="p-3 rounded-xl text-white shadow-lg flex-shrink-0"
                            style={{ backgroundColor: wing.color }}
                          >
                            {getWingIcon(wing.icon)}
                          </div>
                          <div>
                            {wing.badge && (
                              <span className="font-pixel text-[9px] text-rose-300 bg-rose-950/90 border border-rose-500/60 px-2 py-0.5 rounded shadow-sm inline-block tracking-wide mb-1">
                                {wing.badge}
                              </span>
                            )}
                            <h3 className="font-pixel text-sm sm:text-base text-slate-100 group-hover:text-rose-400 transition-colors">
                              {wing.name}
                            </h3>
                          </div>
                        </div>

                        <p className="font-mono text-xs text-slate-400 leading-relaxed">
                          {wing.description}
                        </p>

                        <div className="flex items-center gap-3 pt-1 flex-wrap">
                          {hasActiveRun ? (
                            <span className="font-pixel text-[11px] text-amber-300 bg-amber-950/90 border border-amber-500/70 px-3 py-1 rounded shadow-md animate-pulse flex items-center gap-1.5">
                              <span>⚔️</span>
                              <span>RESUME FL {activeRun.currentFloor} / {wing.floorsCount}</span>
                            </span>
                          ) : (
                            <span className="font-pixel text-[11px] text-emerald-400 bg-emerald-950/80 border border-emerald-700/50 px-3 py-1 rounded shadow-sm">
                              PROGRESS: FL {unlockedFloor} / {wing.floorsCount}
                            </span>
                          )}

                          <span className={`font-pixel text-[11px] flex items-center gap-1 group-hover:translate-x-1 transition-transform ${
                            hasActiveRun ? 'text-amber-400 font-bold' : 'text-rose-400'
                          }`}>
                            <span>{hasActiveRun ? 'CONTINUE OR RESTART' : 'ENTER TRIAL'}</span>
                            <span>➔</span>
                          </span>
                        </div>
                      </div>

                      {/* Right Column: 5-Floor Ladder (7 cols) */}
                      {wing.steps && (
                        <div className="lg:col-span-7 bg-dungeon-darkest/90 border border-slate-800 rounded-xl p-4 space-y-2">
                          <div className="font-pixel text-[10px] text-rose-400 tracking-wider flex items-center justify-between border-b border-slate-800/80 pb-1.5 mb-2">
                            <span>ASCENSION PROGRESSION LADDER</span>
                            <span className="text-slate-500 font-mono text-[10px]">{wing.floorsCount} FOUNDATIONAL STEPS</span>
                          </div>
                          <div className="space-y-1.5">
                            {wing.steps.map((st, i) => {
                              const floorNum = i + 1;
                              const isBoss = floorNum === wing.floorsCount;
                              const isCurrent = hasActiveRun && activeRun.currentFloor === floorNum;
                              const isPassed = (unlockedFloors[wing.id] || 1) > floorNum;

                              return (
                                <div
                                  key={i}
                                  className={`flex items-center justify-between p-2 rounded-lg font-mono text-xs transition-colors ${
                                    isCurrent
                                      ? 'bg-amber-950/40 border border-amber-500/50 text-amber-300'
                                      : isBoss
                                      ? 'bg-rose-950/20 border border-rose-900/40 text-rose-300'
                                      : 'bg-dungeon-card/60 text-slate-300'
                                  }`}
                                >
                                  <div className="flex items-center gap-2 truncate">
                                    <span className={`font-pixel text-[9px] px-1.5 py-0.5 rounded ${
                                      isBoss
                                        ? 'bg-rose-900/60 text-rose-300 border border-rose-700/50'
                                        : isCurrent
                                        ? 'bg-amber-900/60 text-amber-300 border border-amber-600/50'
                                        : 'bg-slate-800 text-slate-400'
                                    }`}>
                                      {isBoss ? '👑 BOSS' : `FL ${floorNum}`}
                                    </span>
                                    <span className="truncate">{st}</span>
                                  </div>
                                  <span className="text-[10px] font-pixel shrink-0 pl-2">
                                    {isCurrent ? '⚔️ ACTIVE' : isPassed ? '✅ CONQUERED' : isBoss ? '💀 TARGET' : '🔒'}
                                  </span>
                                </div>
                              );
                            })}
                          </div>
                        </div>
                      )}
                    </div>
                  </motion.div>
                );
              })}
            </div>
          </div>
        </>
      )}

      {/* Continue Run vs Start New Run Selection Modal */}
      <AnimatePresence>
        {selectedWingForPrompt && promptWingData && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.2 }}
            className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-md p-4"
          >
            <motion.div
              initial={{ scale: 0.9, opacity: 0, y: 20 }}
              animate={{ scale: 1, opacity: 1, y: 0 }}
              exit={{ scale: 0.9, opacity: 0, y: 20 }}
              transition={{ type: 'spring', damping: 25, stiffness: 350 }}
              className="max-w-md w-full bg-dungeon-darkest border-2 border-amber-500/80 rounded-2xl p-6 shadow-[0_0_50px_rgba(245,158,11,0.3)] relative overflow-hidden"
            >
              {/* Background ambient gradient */}
              <div
                className="absolute inset-0 opacity-15 pointer-events-none"
                style={{
                  background: `radial-gradient(circle at top, ${promptWingData.color}, transparent 70%)`,
                }}
              />

              {/* Dismiss Button */}
              <button
                onClick={() => setSelectedWingForPrompt(null)}
                className="absolute top-4 right-4 text-slate-400 hover:text-white p-1 rounded-lg hover:bg-slate-800 transition-colors"
                title="Close"
              >
                <X className="w-5 h-5" />
              </button>

              {/* Header */}
              <div className="flex items-center gap-3 mb-4">
                <div
                  className="w-12 h-12 rounded-xl flex items-center justify-center text-white shadow-lg flex-shrink-0"
                  style={{ backgroundColor: promptWingData.color }}
                >
                  {getWingIcon(promptWingData.icon)}
                </div>
                <div>
                  <div className="font-pixel text-[10px] text-amber-400 tracking-wider">
                    EXPEDITION IN PROGRESS
                  </div>
                  <h2 className="font-pixel text-sm sm:text-base text-slate-100">
                    {promptWingData.name}
                  </h2>
                </div>
              </div>

              {/* Current Run Details */}
              <div className="bg-dungeon-card/90 border border-slate-800 rounded-xl p-4 mb-5 space-y-2.5 font-mono text-xs">
                <div className="flex items-center justify-between pb-2 border-b border-slate-800/80">
                  <span className="text-slate-400">Current Position:</span>
                  <span className="font-pixel text-amber-400">
                    FLOOR {promptFloor} / {promptWingData.floorsCount}
                  </span>
                </div>

                {promptFloorEntry && (
                  <>
                    <div className="flex items-center justify-between">
                      <span className="text-slate-400">Lurking Fiend:</span>
                      <span className="text-rose-400 font-bold">
                        {promptFloorEntry.monster.name} ({promptFloorEntry.monster.maxHp} HP)
                      </span>
                    </div>
                    <div className="flex items-center justify-between">
                      <span className="text-slate-400">Active Challenge:</span>
                      <span className="text-slate-200 font-bold truncate max-w-[200px]" title={promptFloorEntry.title}>
                        {promptFloorEntry.title}
                      </span>
                    </div>
                  </>
                )}

                <div className="flex items-center justify-between pt-1 text-[11px] text-slate-400">
                  <span>Saved Inventory:</span>
                  <span className="text-slate-300">
                    ❤️ {promptRunData?.hp ?? stats.hp} HP • 💰 {promptRunData?.gold ?? stats.gold} G • 🧪 {promptRunData?.potions ?? stats.potions}
                  </span>
                </div>
              </div>

              {/* Two Choice Actions */}
              <div className="space-y-3">
                {/* 1. Continue Run */}
                <button
                  onClick={() => {
                    const wingId = selectedWingForPrompt;
                    setSelectedWingForPrompt(null);
                    continueRun(wingId);
                  }}
                  className="w-full py-3.5 px-4 rounded-xl bg-gradient-to-r from-amber-500 to-amber-600 hover:from-amber-400 hover:to-amber-500 text-slate-950 font-pixel text-xs font-bold flex items-center justify-center gap-2 shadow-lg shadow-amber-500/20 active:scale-95 transition-all"
                >
                  <Swords className="w-4 h-4 text-slate-950" />
                  <span>CONTINUE EXPEDITION (FLOOR {promptFloor})</span>
                </button>

                {/* 2. Start New Run */}
                <button
                  onClick={() => {
                    const wingId = selectedWingForPrompt;
                    setSelectedWingForPrompt(null);
                    startNewRun(wingId);
                  }}
                  className="w-full py-3 px-4 rounded-xl bg-slate-900/90 hover:bg-rose-950/60 border border-slate-700 hover:border-rose-600/70 text-slate-300 hover:text-rose-200 font-pixel text-xs flex items-center justify-center gap-2 transition-all group"
                >
                  <RotateCcw className="w-3.5 h-3.5 text-slate-400 group-hover:text-rose-400 group-hover:-rotate-90 transition-transform" />
                  <span>START NEW RUN (RESET TO FLOOR 1)</span>
                </button>
              </div>

              {/* Cancel Option */}
              <div className="mt-4 text-center">
                <button
                  onClick={() => setSelectedWingForPrompt(null)}
                  className="font-mono text-xs text-slate-400 hover:text-slate-200 underline transition-colors"
                >
                  Return to Dungeon Map
                </button>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
};

