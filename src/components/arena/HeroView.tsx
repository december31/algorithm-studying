import React from 'react';
import { motion } from 'framer-motion';
import { useGameStore } from '../../store/useGameStore';

export const HeroView: React.FC = () => {
  const { heroAnim, stats, usePotion } = useGameStore();

  const getAnimationProps = (): any => {
    switch (heroAnim) {
      case 'cast':
        return {
          x: [0, 40, 20, 0],
          scale: [1, 1.15, 1],
          transition: { duration: 0.5 },
        };
      case 'hurt':
        return {
          x: [0, -25, 0],
          rotate: [0, -10, 0],
          transition: { duration: 0.3 },
        };
      default:
        return {
          y: [0, -4, 0],
          transition: { repeat: Infinity, duration: 2.2, ease: 'easeInOut' },
        };
    }
  };

  return (
    <div className="flex flex-col items-center select-none">
      {/* Hero Title & Level */}
      <div className="text-center h-8 flex flex-col justify-center mb-1">
        <div className="font-pixel text-[9px] text-emerald-400 tracking-wider uppercase truncate max-w-[140px] sm:max-w-[170px]">
          ALGO-HERO (YOU)
        </div>
        <div className="text-[10px] text-slate-400 font-mono italic truncate max-w-[140px] sm:max-w-[170px]">
          LVL {stats.level} ALGO-MAGE
        </div>
      </div>

      {/* Player HP Bar */}
      <div className="w-32 sm:w-44 h-3 bg-dungeon-darkest border border-emerald-800 rounded-full overflow-hidden p-0.5 mb-1 shadow-inner relative">
        <motion.div
          animate={{ width: `${Math.max(0, Math.min(100, (stats.hp / stats.maxHp) * 100))}%` }}
          transition={{ type: 'spring', stiffness: 200, damping: 20 }}
          className="h-full bg-gradient-to-r from-emerald-500 via-teal-400 to-cyan-400 rounded-full shadow-[0_0_8px_rgba(16,185,129,0.5)]"
        />
      </div>

      {/* HP Value & Shield Status */}
      <div className="flex items-center justify-center gap-1.5 h-4 mb-2 font-mono text-[9px]">
        <span className="text-slate-300 font-bold">{stats.hp} / {stats.maxHp} HP</span>
        {stats.shieldPassedCount > 0 && (
          <span className="text-sky-400 font-pixel text-[8px] bg-sky-950/80 px-1 rounded border border-sky-600/40 animate-pulse">
            🛡️ -{stats.shield}%
          </span>
        )}
      </div>

      {/* Hero Sprite Container */}
      <motion.div
        animate={getAnimationProps()}
        className="relative w-20 h-24 sm:w-24 sm:h-28 flex items-center justify-center"
      >
        {/* Arcane Cast Aura Glow */}
        {heroAnim === 'cast' && (
          <div className="absolute inset-0 w-24 h-24 -left-2 -top-2 rounded-full bg-sky-500/40 blur-xl animate-pulse" />
        )}

        {/* 8-bit Pixel Character Canvas / SVG */}
        <div
          className={`w-full h-full flex items-center justify-center rounded-lg p-2 relative transition-all ${
            heroAnim === 'hurt'
              ? 'bg-rose-500/30 filter drop-shadow-[0_0_15px_rgba(244,63,94,0.8)]'
              : 'filter drop-shadow-[0_0_12px_rgba(56,189,248,0.4)]'
          }`}
        >
          {/* Custom 8-bit Mage Pixel Art SVG */}
          <svg
            className="w-full h-full"
            viewBox="0 0 32 32"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            style={{ imageRendering: 'pixelated' }}
          >
            {/* Mage Robe */}
            <rect x="10" y="14" width="12" height="15" fill="#3b82f6" />
            <rect x="12" y="14" width="8" height="15" fill="#2563eb" />
            <rect x="14" y="16" width="4" height="13" fill="#60a5fa" />
            {/* Belt & Pouch */}
            <rect x="10" y="21" width="12" height="2" fill="#d97706" />
            <rect x="15" y="21" width="2" height="2" fill="#fef08a" />
            {/* Wizard Hat */}
            <polygon points="16,2 8,14 24,14" fill="#1e3a8a" />
            <rect x="6" y="13" width="20" height="2" fill="#1e40af" />
            <rect x="15" y="5" width="2" height="2" fill="#fbbf24" />
            {/* Face & Eyes */}
            <rect x="11" y="11" width="10" height="3" fill="#fde047" />
            <rect x="13" y="12" width="2" height="1" fill="#0f172a" />
            <rect x="17" y="12" width="2" height="1" fill="#0f172a" />
            {/* Arcane Staff */}
            <rect x="23" y="8" width="2" height="22" fill="#78350f" />
            <circle cx="24" cy="7" r="3" fill="#38bdf8" />
            <circle cx="24" cy="7" r="1.5" fill="#ffffff" />
          </svg>
        </div>

        {/* Hero Shadow */}
        <div className="absolute -bottom-1.5 w-16 h-3 bg-black/40 rounded-full blur-xs pointer-events-none" />
      </motion.div>

      {/* Hero Action Intent (Quick Potion Use) */}
      <div className="h-6 mt-2 flex items-center justify-center">
        <button
          onClick={usePotion}
          disabled={stats.potions === 0 || stats.hp >= stats.maxHp}
          className="px-2.5 py-0.5 rounded-md bg-emerald-950/80 hover:bg-emerald-900 border border-emerald-800/60 font-pixel text-[8px] text-emerald-300 flex items-center gap-1 shadow transition-colors disabled:opacity-40 disabled:cursor-not-allowed"
          title="Drink health potion to restore +35 HP"
        >
          <span>🧪</span>
          <span>HEAL ({stats.potions})</span>
        </button>
      </div>
    </div>
  );
};
