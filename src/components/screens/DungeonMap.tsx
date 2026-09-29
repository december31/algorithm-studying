import React from 'react';
import { useGameStore } from '../../store/useGameStore';
import { DUNGEON_WINGS } from '../../data/wings';
import { DungeonTopic } from '../../types/game';
import { Layers, Coins, GitCommit, GitBranch, Network, Table, ShoppingBag, Shield, Heart, Sparkles } from 'lucide-react';
import { motion } from 'framer-motion';

export const DungeonMap: React.FC = () => {
  const { stats, unlockedFloors, selectWing, setScreen, healPlayer } = useGameStore();

  const getWingIcon = (icon: string) => {
    switch (icon) {
      case 'Layers': return <Layers className="w-6 h-6" />;
      case 'Coins': return <Coins className="w-6 h-6" />;
      case 'GitCommit': return <GitCommit className="w-6 h-6" />;
      case 'GitBranch': return <GitBranch className="w-6 h-6" />;
      case 'Network': return <Network className="w-6 h-6" />;
      case 'Table': return <Table className="w-6 h-6" />;
      case 'Sparkles': return <Sparkles className="w-6 h-6" />;
      default: return <Layers className="w-6 h-6" />;
    }
  };

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

      {/* 5 Dungeon Wings Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        {DUNGEON_WINGS.map((wing, idx) => {
          const unlockedFloor = unlockedFloors[wing.id] || 1;

          return (
            <motion.div
              key={wing.id}
              whileHover={{ y: -4, scale: 1.01 }}
              transition={{ type: 'spring', stiffness: 300, damping: 20 }}
              onClick={() => selectWing(wing.id)}
              className="bg-dungeon-card/90 hover:bg-dungeon-card border-2 border-dungeon-border hover:border-slate-500 rounded-2xl p-5 cursor-pointer shadow-xl flex flex-col justify-between group transition-all relative overflow-hidden"
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
                  <span className="font-pixel text-[10px] text-emerald-400 bg-emerald-950/80 border border-emerald-700/50 px-2 py-0.5 rounded">
                    FLOOR {unlockedFloor} / {wing.floorsCount}
                  </span>
                </div>

                <h3 className="font-pixel text-xs sm:text-sm text-slate-100 group-hover:text-amber-400 transition-colors mb-1">
                  {wing.name}
                </h3>
                <p className="font-mono text-xs text-slate-400 mb-3 leading-relaxed">
                  {wing.subtitle}
                </p>
              </div>

              {/* Enter Wing CTA */}
              <div className="pt-3 border-t border-slate-800 flex items-center justify-between font-pixel text-[10px] text-sky-400 group-hover:translate-x-1 transition-transform">
                <span>ENTER DUNGEON</span>
                <span>➔</span>
              </div>
            </motion.div>
          );
        })}
      </div>
    </div>
  );
};
