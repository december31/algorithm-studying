import React from 'react';
import { useGameStore } from '../../store/useGameStore';
import { HeroView } from './HeroView';
import { MonsterView } from './MonsterView';
import { ParticleCanvas } from './ParticleCanvas';
import { motion, AnimatePresence } from 'framer-motion';

export const BattleArena: React.FC = () => {
  const {
    currentProblem,
    screenShake,
    floatingTexts,
    heroAnim,
  } = useGameStore();

  return (
    <div
      className={`relative w-full rounded-2xl border-2 border-dungeon-border bg-gradient-to-b from-dungeon-darker via-dungeon-card to-dungeon-darkest overflow-hidden shadow-xl p-3 transition-transform ${
        screenShake ? 'animate-shake' : ''
      }`}
    >
      {/* Background Dungeon Stone Texture */}
      <div className="absolute inset-0 opacity-10 pointer-events-none bg-[radial-gradient(#3b82f6_1px,transparent_1px)] [background-size:16px_16px]" />
      
      {/* Dynamic Spell / Slash Particles */}
      <ParticleCanvas
        triggerAttack={heroAnim === 'cast'}
        type={heroAnim === 'cast' ? 'spell' : 'hit'}
      />

      {/* Center Stage: Hero vs Monster Encounter */}
      <div className="relative z-10 flex items-center justify-around py-3 px-4 min-h-[140px]">
        {/* Hero Left Side */}
        <HeroView />

        {/* VS Center Clashing Icon */}
        <div className="flex flex-col items-center">
          <div className="w-9 h-9 rounded-full bg-dungeon-darkest border border-amber-500/50 flex items-center justify-center font-pixel text-xs text-amber-400 shadow-[0_0_15px_rgba(245,158,11,0.3)]">
            VS
          </div>
          <span className="text-[8px] font-pixel text-slate-500 mt-1 uppercase">
            {currentProblem.difficulty}
          </span>
        </div>

        {/* Monster Right Side */}
        <MonsterView />
      </div>

      {/* Floating Combat Damage & Status Texts */}
      <div className="absolute inset-0 pointer-events-none flex items-center justify-center z-30">
        <AnimatePresence>
          {floatingTexts.map((txt) => (
            <motion.div
              key={txt.id}
              initial={{ y: 20, opacity: 1, scale: 0.8 }}
              animate={{ y: -60, opacity: 0, scale: 1.2 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 1.2, ease: 'easeOut' }}
              style={{ color: txt.color }}
              className="absolute font-pixel text-xs sm:text-sm font-bold drop-shadow-[0_2px_4px_rgba(0,0,0,0.9)] bg-black/60 px-3 py-1 rounded border border-white/20"
            >
              {txt.text}
            </motion.div>
          ))}
        </AnimatePresence>
      </div>
    </div>
  );
};
