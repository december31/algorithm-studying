import React from 'react';
import { useGameStore } from '../../store/useGameStore';
import { Heart, Shield } from 'lucide-react';
import { motion } from 'framer-motion';

export const HealthBar: React.FC = () => {
  const { stats, usePotion } = useGameStore();
  const { maxHp, hp, shield, shieldPassedCount, potions } = stats;

  const hpPercent = Math.max(0, Math.min(100, (hp / maxHp) * 100));

  const getHpColor = () => {
    if (hpPercent > 50) return 'from-emerald-500 via-teal-400 to-cyan-400';
    if (hpPercent > 25) return 'from-amber-500 to-yellow-400';
    return 'from-rose-600 to-red-500 animate-pulse';
  };

  return (
    <div className="flex items-center gap-2 sm:gap-3 bg-dungeon-card/90 border border-dungeon-border/80 px-2.5 sm:px-3 py-1.5 rounded-xl shadow-lg">
      {/* 100 HP Bar Display */}
      <div className="flex flex-col gap-0.5">
        <div className="flex items-center justify-between text-[10px] font-pixel text-slate-300">
          <span className="flex items-center gap-1 text-rose-400">
            <Heart className="w-3 h-3 fill-rose-500 text-rose-500" />
            <span>HP</span>
          </span>
          <span className="font-mono font-bold text-slate-200">
            {hp} <span className="text-slate-500">/ {maxHp}</span>
          </span>
        </div>

        {/* Dynamic HP Bar */}
        <div className="w-24 sm:w-32 h-2.5 bg-dungeon-darkest border border-slate-700/80 rounded-full overflow-hidden p-[1px] relative shadow-inner">
          <motion.div
            animate={{ width: `${hpPercent}%` }}
            transition={{ type: 'spring', stiffness: 200, damping: 20 }}
            className={`h-full bg-gradient-to-r ${getHpColor()} rounded-full shadow-[0_0_8px_rgba(16,185,129,0.4)]`}
          />
        </div>
      </div>

      {/* Test Case Shield Indicator */}
      {shieldPassedCount > 0 ? (
        <div
          className="flex items-center gap-1 px-2 py-1 rounded-lg bg-sky-950/80 border border-sky-500/50 text-sky-300 font-pixel text-[9px] shadow-sm animate-pulse"
          title={`Shield Active: ${shieldPassedCount} passed test cases reduce incoming damage by ${shield}%!`}
        >
          <Shield className="w-3 h-3 fill-sky-400 text-sky-400" />
          <span className="hidden sm:inline">SHIELD</span>
          <span>-{shield}%</span>
        </div>
      ) : (
        <div
          className="hidden md:flex items-center gap-1 px-1.5 py-1 rounded-lg bg-slate-900/60 border border-slate-800 text-slate-500 font-pixel text-[8px]"
          title="Passing test cases grants damage-reducing shields against monster counterattacks!"
        >
          <Shield className="w-2.5 h-2.5" />
          <span>NO SHIELD</span>
        </div>
      )}

      {/* Potion Button */}
      <div className="flex items-center border-l border-slate-700/60 pl-2">
        <button
          onClick={usePotion}
          disabled={potions === 0 || hp >= maxHp}
          className="relative px-2 py-1 rounded-lg bg-emerald-600/80 hover:bg-emerald-500 border border-emerald-400/50 text-white font-pixel text-[10px] flex items-center gap-1 disabled:opacity-40 disabled:cursor-not-allowed transition-all shadow-md group"
          title="Use Health Potion to restore +35 HP"
        >
          <span className="text-sm leading-none">🧪</span>
          <span className="hidden sm:inline">HEAL</span>
          <span className="px-1 py-0.2 bg-emerald-950 rounded text-emerald-300 font-mono text-[10px] font-bold border border-emerald-500/40">
            {potions}
          </span>
        </button>
      </div>
    </div>
  );
};
