import React from 'react';
import { useGameStore } from '../../store/useGameStore';
import { motion } from 'framer-motion';
import { Skull, RotateCcw } from 'lucide-react';

export const GameOverModal: React.FC = () => {
  const { currentProblem, currentFloor, restartRunOnPermadeath } = useGameStore();

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      transition={{ duration: 0.25 }}
      className="fixed inset-0 z-50 flex items-center justify-center bg-black/85 backdrop-blur-md p-4"
    >
      <motion.div
        initial={{ scale: 0.85, opacity: 0, y: 30 }}
        animate={{ scale: 1, opacity: 1, y: 0 }}
        exit={{ scale: 0.85, opacity: 0, y: 30 }}
        transition={{ type: 'spring', damping: 25, stiffness: 350 }}
        className="max-w-md w-full bg-dungeon-darkest border-2 border-rose-600 rounded-2xl p-6 shadow-[0_0_50px_rgba(225,29,72,0.5)] text-center relative overflow-hidden"
      >
        {/* Blood vignette overlay */}
        <div className="absolute inset-0 bg-gradient-to-b from-rose-950/30 to-transparent pointer-events-none" />

        {/* Skull Icon */}
        <div className="w-20 h-20 mx-auto mb-4 rounded-full bg-rose-950/80 border-2 border-rose-500 flex items-center justify-center shadow-lg">
          <Skull className="w-10 h-10 text-rose-500 animate-pulse" />
        </div>

        <h1 className="font-pixel text-2xl sm:text-3xl text-rose-500 mb-2 tracking-widest drop-shadow-[0_4px_10px_rgba(244,63,94,0.6)]">
          YOU DIED
        </h1>

        <p className="font-mono text-sm text-slate-300 mb-6">
          Your logic shattered against <span className="text-rose-400 font-bold">{currentProblem.monster.name}</span> on Floor {currentFloor}.
        </p>

        <div className="bg-dungeon-card p-4 rounded-xl border border-slate-800 text-xs font-mono mb-6 space-y-2 text-left">
          <div className="flex justify-between">
            <span className="text-slate-400">Challenge:</span>
            <span className="text-slate-200 font-bold">{currentProblem.title}</span>
          </div>
          <div className="flex justify-between">
            <span className="text-slate-400">Cause of Defeat:</span>
            <span className="text-rose-400 font-bold">Health Depleted (0 HP)</span>
          </div>
          <div className="flex justify-between">
            <span className="text-slate-400">Roguelike Rule:</span>
            <span className="text-amber-400">Randomized 10-problem run re-rolled!</span>
          </div>
        </div>

        <button
          onClick={restartRunOnPermadeath}
          className="w-full py-3.5 px-6 rounded-xl bg-gradient-to-r from-rose-600 to-amber-600 hover:from-rose-500 hover:to-amber-500 text-white font-pixel text-xs font-bold tracking-wider shadow-lg shadow-rose-950/50 flex items-center justify-center gap-2 transition-all active:scale-95"
        >
          <RotateCcw className="w-4 h-4" />
          <span>RE-ROLL DUNGEON & TRY AGAIN (FLOOR 1)</span>
        </button>
      </motion.div>
    </motion.div>
  );
};
