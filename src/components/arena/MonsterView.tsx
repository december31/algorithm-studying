import React from 'react';
import { motion } from 'framer-motion';
import { useGameStore } from '../../store/useGameStore';

export const MonsterView: React.FC = () => {
  const { currentProblem, monsterAnim, monsterHp, maxMonsterHp } = useGameStore();
  const monster = currentProblem.monster;

  const getAnimationProps = (): any => {
    switch (monsterAnim) {
      case 'attack':
        return {
          x: [0, -50, 0],
          scale: [1, 1.2, 1],
          opacity: 1,
          transition: { duration: 0.4 },
        };
      case 'hurt':
        return {
          x: [0, 30, -10, 0],
          scale: 1,
          opacity: 1,
          transition: { duration: 0.3 },
        };
      case 'defeated':
        return {
          scale: [1, 0.8, 0],
          opacity: [1, 0.5, 0],
          y: [0, 30],
          transition: { duration: 0.8 },
        };
      default:
        return {
          y: [0, -5, 0],
          scale: 1,
          opacity: 1,
          transition: { repeat: Infinity, duration: 2.5, ease: 'easeInOut' },
        };
    }
  };

  const renderMonsterPixelArt = () => {
    switch (monster.sprite) {
      case 'dragon':
        return (
          <svg className="w-full h-full" viewBox="0 0 32 32" fill="none">
            {/* Dragon Wings */}
            <polygon points="4,8 14,14 8,24" fill="#991b1b" />
            <polygon points="28,8 18,14 24,24" fill="#991b1b" />
            {/* Body */}
            <rect x="11" y="10" width="10" height="15" rx="3" fill="#dc2626" />
            {/* Belly scales */}
            <rect x="13" y="14" width="6" height="9" fill="#f87171" />
            {/* Horns & Head */}
            <polygon points="12,4 14,8 10,8" fill="#fef08a" />
            <polygon points="20,4 22,8 18,8" fill="#fef08a" />
            <rect x="10" y="7" width="12" height="7" fill="#b91c1c" />
            {/* Fiery Eyes */}
            <rect x="12" y="9" width="2" height="2" fill="#fef08a" />
            <rect x="18" y="9" width="2" height="2" fill="#fef08a" />
            {/* Fangs */}
            <polygon points="13,14 14,16 15,14" fill="#ffffff" />
            <polygon points="17,14 18,16 19,14" fill="#ffffff" />
          </svg>
        );

      case 'lich':
        return (
          <svg className="w-full h-full" viewBox="0 0 32 32" fill="none">
            {/* Dark Cowl */}
            <polygon points="16,2 8,16 24,16" fill="#4c1d95" />
            <rect x="10" y="15" width="12" height="15" fill="#581c87" />
            {/* Skull Face */}
            <rect x="12" y="9" width="8" height="7" fill="#e2e8f0" />
            <rect x="13" y="11" width="2" height="2" fill="#000000" />
            <rect x="17" y="11" width="2" height="2" fill="#000000" />
            {/* Glowing Rune Orb */}
            <circle cx="24" cy="18" r="4" fill="#a855f7" />
            <circle cx="24" cy="18" r="2" fill="#f3e8ff" />
          </svg>
        );

      case 'orc':
        return (
          <svg className="w-full h-full" viewBox="0 0 32 32" fill="none">
            {/* Spiked Iron Shoulders */}
            <rect x="6" y="12" width="6" height="6" rx="1" fill="#4b5563" />
            <rect x="20" y="12" width="6" height="6" rx="1" fill="#4b5563" />
            {/* Muscular Orc Torso */}
            <rect x="10" y="13" width="12" height="14" rx="2" fill="#15803d" />
            <rect x="11" y="15" width="10" height="9" fill="#166534" />
            {/* Iron Belt */}
            <rect x="10" y="21" width="12" height="3" fill="#374151" />
            <rect x="15" y="21" width="2" height="3" fill="#eab308" />
            {/* Orc Head */}
            <rect x="10" y="7" width="12" height="8" rx="2" fill="#15803d" />
            {/* Horned Iron Helm */}
            <polygon points="9,7 11,4 12,7" fill="#9ca3af" />
            <polygon points="23,7 21,4 20,7" fill="#9ca3af" />
            <rect x="10" y="6" width="12" height="3" fill="#4b5563" />
            {/* Fierce Red Eyes */}
            <rect x="12" y="9" width="2" height="1.5" fill="#ef4444" />
            <rect x="18" y="9" width="2" height="1.5" fill="#ef4444" />
            {/* Underbite Tusks */}
            <polygon points="12,13 13,10 14,13" fill="#ffffff" />
            <polygon points="18,13 19,10 20,13" fill="#ffffff" />
            {/* Heavy Stone Pillar Club */}
            <rect x="23" y="6" width="5" height="18" rx="1" fill="#78716c" />
            <rect x="22" y="8" width="7" height="3" fill="#57534e" />
          </svg>
        );

      case 'goblin':
        return (
          <svg className="w-full h-full" viewBox="0 0 32 32" fill="none">
            {/* Goblin Body */}
            <rect x="10" y="12" width="12" height="14" rx="2" fill="#15803d" />
            {/* Ears */}
            <polygon points="6,10 10,12 8,15" fill="#22c55e" />
            <polygon points="26,10 22,12 24,15" fill="#22c55e" />
            {/* Head */}
            <rect x="10" y="8" width="12" height="8" rx="1" fill="#22c55e" />
            {/* Evil Red Eyes */}
            <rect x="12" y="10" width="2" height="2" fill="#ef4444" />
            <rect x="18" y="10" width="2" height="2" fill="#ef4444" />
            {/* Underbite Fangs */}
            <rect x="13" y="14" width="2" height="2" fill="#ffffff" />
            <rect x="17" y="14" width="2" height="2" fill="#ffffff" />
            {/* Spiked Club */}
            <rect x="23" y="10" width="3" height="14" fill="#78350f" rx="1" />
          </svg>
        );

      case 'gargoyle':
        return (
          <svg className="w-full h-full" viewBox="0 0 32 32" fill="none">
            {/* Stone Bat Wings */}
            <polygon points="4,6 12,12 6,22" fill="#475569" />
            <polygon points="28,6 20,12 26,22" fill="#475569" />
            {/* Gargoyle Stone Body */}
            <rect x="10" y="11" width="12" height="14" rx="2" fill="#64748b" />
            {/* Horns & Head */}
            <polygon points="10,5 12,9 9,9" fill="#334155" />
            <polygon points="22,5 20,9 23,9" fill="#334155" />
            <rect x="10" y="8" width="12" height="8" rx="2" fill="#475569" />
            {/* Glowing Amber Eyes */}
            <rect x="12" y="10" width="2" height="2" fill="#f59e0b" />
            <rect x="18" y="10" width="2" height="2" fill="#f59e0b" />
            {/* Stone Fangs */}
            <polygon points="13,15 14,17 15,15" fill="#f1f5f9" />
            <polygon points="17,15 18,17 19,15" fill="#f1f5f9" />
            {/* Clawed Feet */}
            <rect x="10" y="24" width="4" height="3" fill="#334155" />
            <rect x="18" y="24" width="4" height="3" fill="#334155" />
          </svg>
        );

      case 'skeleton':
        return (
          <svg className="w-full h-full" viewBox="0 0 32 32" fill="none">
            {/* Skull */}
            <rect x="11" y="6" width="10" height="9" rx="2" fill="#f1f5f9" />
            <rect x="13" y="9" width="2" height="2" fill="#0f172a" />
            <rect x="17" y="9" width="2" height="2" fill="#0f172a" />
            <rect x="14" y="13" width="4" height="2" fill="#0f172a" />
            {/* Ribcage */}
            <rect x="15" y="15" width="2" height="10" fill="#cbd5e1" />
            <rect x="11" y="17" width="10" height="2" fill="#cbd5e1" />
            <rect x="12" y="20" width="8" height="2" fill="#cbd5e1" />
            {/* Sword */}
            <rect x="23" y="7" width="2" height="18" fill="#94a3b8" />
            <rect x="21" y="20" width="6" height="2" fill="#475569" />
          </svg>
        );

      case 'wraith':
        return (
          <svg className="w-full h-full" viewBox="0 0 32 32" fill="none">
            {/* Phantom Shroud */}
            <polygon points="16,3 8,16 24,16" fill="#1e1b4b" />
            <path d="M8 15 C8 24 10 28 16 28 C22 28 24 24 24 15 Z" fill="#312e81" />
            {/* Ghostly Void Face */}
            <rect x="12" y="10" width="8" height="7" rx="2" fill="#0f172a" />
            {/* Glowing Cyan Spectral Eyes */}
            <circle cx="14" cy="13" r="1.5" fill="#22d3ee" />
            <circle cx="18" cy="13" r="1.5" fill="#22d3ee" />
            {/* Floating Spectral Flame Wisps */}
            <circle cx="6" cy="18" r="2" fill="#06b6d4" opacity="0.8" />
            <circle cx="26" cy="18" r="2" fill="#06b6d4" opacity="0.8" />
            <circle cx="16" cy="27" r="1.5" fill="#38bdf8" opacity="0.7" />
          </svg>
        );

      case 'treant':
        return (
          <svg className="w-full h-full" viewBox="0 0 32 32" fill="none">
            {/* Leafy Green Canopy */}
            <circle cx="16" cy="7" r="6" fill="#15803d" />
            <circle cx="11" cy="9" r="4" fill="#16a34a" />
            <circle cx="21" cy="9" r="4" fill="#16a34a" />
            {/* Ancient Knotted Wood Trunk */}
            <rect x="11" y="11" width="10" height="15" rx="2" fill="#78350f" />
            {/* Branch Arms */}
            <polygon points="6,12 11,14 11,17 6,15" fill="#92400e" />
            <polygon points="26,12 21,14 21,17 26,15" fill="#92400e" />
            {/* Glowing Amber Sap Eyes */}
            <rect x="13" y="14" width="2" height="2" fill="#fbbf24" />
            <rect x="17" y="14" width="2" height="2" fill="#fbbf24" />
            {/* Bark Mouth */}
            <rect x="14" y="18" width="4" height="2" fill="#451a03" />
            {/* Roots */}
            <rect x="9" y="24" width="4" height="3" fill="#78350f" />
            <rect x="19" y="24" width="4" height="3" fill="#78350f" />
          </svg>
        );

      case 'spider':
        return (
          <svg className="w-full h-full" viewBox="0 0 32 32" fill="none">
            {/* Spider Legs */}
            <path d="M6 10 L12 16 M6 16 L12 18 M6 22 L12 20" stroke="#ec4899" strokeWidth="2" />
            <path d="M26 10 L20 16 M26 16 L20 18 M26 22 L20 20" stroke="#ec4899" strokeWidth="2" />
            {/* Abdomen & Head */}
            <circle cx="16" cy="18" r="6" fill="#831843" />
            <circle cx="16" cy="12" r="4" fill="#9d174d" />
            {/* Multiple Glowing Eyes */}
            <circle cx="14" cy="11" r="1" fill="#f43f5e" />
            <circle cx="18" cy="11" r="1" fill="#f43f5e" />
            <circle cx="15" cy="13" r="0.8" fill="#fb7185" />
            <circle cx="17" cy="13" r="0.8" fill="#fb7185" />
          </svg>
        );

      case 'golem':
        return (
          <svg className="w-full h-full" viewBox="0 0 32 32" fill="none">
            {/* Stone Boulder Shoulders */}
            <rect x="5" y="10" width="7" height="7" rx="2" fill="#78716c" />
            <rect x="20" y="10" width="7" height="7" rx="2" fill="#78716c" />
            {/* Heavy Stone Fists */}
            <rect x="4" y="16" width="6" height="8" rx="1.5" fill="#57534e" />
            <rect x="22" y="16" width="6" height="8" rx="1.5" fill="#57534e" />
            {/* Stone Torso */}
            <rect x="10" y="11" width="12" height="15" rx="3" fill="#44403c" />
            {/* Carved Rune Core Glowing Gold */}
            <rect x="13" y="14" width="6" height="6" rx="1" fill="#eab308" />
            <circle cx="16" cy="17" r="1.5" fill="#fef08a" />
            {/* Golem Stone Head */}
            <rect x="11" y="5" width="10" height="7" rx="2" fill="#78716c" />
            {/* Glowing Amber Eyes */}
            <rect x="13" y="8" width="2" height="1.5" fill="#fbbf24" />
            <rect x="17" y="8" width="2" height="1.5" fill="#fbbf24" />
            {/* Ancient Moss patches */}
            <rect x="12" y="19" width="3" height="2" fill="#15803d" />
            <rect x="18" y="21" width="3" height="2" fill="#15803d" />
          </svg>
        );

      case 'slime':
      default:
        // Gelatinous Slime / Blob
        return (
          <svg className="w-full h-full" viewBox="0 0 32 32" fill="none">
            <path
              d="M8 24 C8 14 12 8 16 8 C20 8 24 14 24 24 C24 26 22 28 16 28 C10 28 8 26 8 24 Z"
              fill={monster.color || '#a855f7'}
            />
            {/* Cute Glistening Big Eyes */}
            <ellipse cx="14" cy="18" rx="2" ry="3" fill="#ffffff" />
            <circle cx="14" cy="18" r="1" fill="#0f172a" />
            <ellipse cx="18" cy="18" rx="2" ry="3" fill="#ffffff" />
            <circle cx="18" cy="18" r="1" fill="#0f172a" />
            {/* Sparkle Reflection */}
            <circle cx="12" cy="12" r="1" fill="#ffffff" opacity="0.6" />
          </svg>
        );
    }
  };

  return (
    <div className="flex flex-col items-center select-none">
      {/* Monster Title & Name */}
      <div className="text-center h-8 flex flex-col justify-center mb-1">
        <div className="font-pixel text-[9px] text-rose-400 tracking-wider uppercase truncate max-w-[140px] sm:max-w-[170px]" title={monster.name}>
          {monster.name}
        </div>
        <div className="text-[10px] text-slate-400 font-mono italic truncate max-w-[140px] sm:max-w-[170px]" title={monster.title}>
          {monster.title}
        </div>
      </div>

      {/* Monster HP Bar */}
      <div className="w-32 sm:w-44 h-3 bg-dungeon-darkest border border-rose-900 rounded-full overflow-hidden p-0.5 mb-1 shadow-inner relative">
        <motion.div
          animate={{ width: `${Math.max(0, Math.min(100, (monsterHp / maxMonsterHp) * 100))}%` }}
          transition={{ type: 'spring', stiffness: 200, damping: 20 }}
          className="h-full bg-gradient-to-r from-rose-600 via-rose-500 to-amber-500 rounded-full shadow-[0_0_8px_rgba(244,63,94,0.5)]"
        />
      </div>

      {/* HP Value & Damage Status */}
      <div className="flex items-center justify-center gap-1.5 h-4 mb-2 font-mono text-[9px]">
        <span className="text-slate-300 font-bold">{monsterHp} / {maxMonsterHp} HP</span>
        {monsterHp < maxMonsterHp && (
          <span className="text-rose-400 font-pixel text-[8px] bg-rose-950/80 px-1 rounded border border-rose-600/40 animate-pulse">
            -{maxMonsterHp - monsterHp}
          </span>
        )}
      </div>

      {/* Monster Sprite */}
      <motion.div
        key={`monster-sprite-${monster.id}`}
        animate={getAnimationProps()}
        className="relative w-20 h-24 sm:w-24 sm:h-28 flex items-center justify-center"
      >
        <div
          className={`w-full h-full flex items-center justify-center rounded-lg p-2 transition-all ${
            monsterAnim === 'hurt'
              ? 'bg-rose-500/40 filter drop-shadow-[0_0_20px_rgba(244,63,94,0.9)]'
              : 'filter drop-shadow-[0_0_12px_rgba(239,68,68,0.3)]'
          }`}
        >
          {renderMonsterPixelArt()}
        </div>

        {/* Monster Shadow */}
        <div className="absolute -bottom-1.5 w-16 h-3 bg-black/40 rounded-full blur-xs pointer-events-none" />
      </motion.div>

      {/* Attack Intent Indicator */}
      <div className="h-6 mt-2 flex items-center justify-center">
        <div className="px-2.5 py-0.5 rounded-md bg-rose-950/80 border border-rose-800/60 font-pixel text-[8px] text-rose-300 flex items-center gap-1 shadow">
          <span>⚔️</span>
          <span className="truncate max-w-[110px] sm:max-w-[140px]">{monster.attackName}</span>
        </div>
      </div>
    </div>
  );
};
