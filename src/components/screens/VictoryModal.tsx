import React, { useEffect } from 'react';
import { useGameStore } from '../../store/useGameStore';
import { motion } from 'framer-motion';
import confetti from 'canvas-confetti';
import { Trophy, ArrowRight, Map, Sparkles } from 'lucide-react';

export const VictoryModal: React.FC = () => {
  const { currentProblem, currentFloor, advanceFloor, setScreen, isSolutionUsedForProblem } = useGameStore();

  useEffect(() => {
    // Launch celebratory confetti burst
    confetti({
      particleCount: 80,
      spread: 70,
      origin: { y: 0.6 },
    });
  }, []);

  const isWingBoss = currentFloor === 10;

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      transition={{ duration: 0.25 }}
      className="fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-md p-4"
    >
      <motion.div
        initial={{ scale: 0.85, opacity: 0, y: 20 }}
        animate={{ scale: 1, opacity: 1, y: 0 }}
        exit={{ scale: 0.85, opacity: 0, y: 20 }}
        transition={{ type: 'spring', damping: 25, stiffness: 350 }}
        className="max-w-md w-full bg-dungeon-darkest border-2 border-emerald-500 rounded-2xl p-6 shadow-[0_0_50px_rgba(16,185,129,0.4)] text-center relative overflow-hidden"
      >
        {/* Glow backdrop */}
        <div className="absolute inset-0 bg-gradient-to-b from-emerald-950/30 to-transparent pointer-events-none" />

        <div className="w-16 h-16 mx-auto mb-3 rounded-full bg-emerald-950/80 border-2 border-emerald-400 flex items-center justify-center shadow-lg">
          <Trophy className="w-8 h-8 text-emerald-400 animate-bounce" />
        </div>

        <h1 className="font-pixel text-xl sm:text-2xl text-emerald-400 mb-1 tracking-wider">
          {isWingBoss ? 'WING CLEARED!' : 'FLOOR CONQUERED!'}
        </h1>

        {isSolutionUsedForProblem ? (
          <div className="mb-4 space-y-2">
            <p className="font-mono text-sm text-purple-300">
              You banished <span className="text-rose-400 font-bold">{currentProblem.monster.name}</span> using the <span className="text-purple-400 font-bold">Forbidden Scroll (-25 HP)</span>!
            </p>
            <div className="bg-purple-950/60 border border-purple-500/40 rounded-xl p-3 text-xs font-mono text-purple-200 flex items-start gap-2 text-left">
              <span className="text-base">📜</span>
              <div className="space-y-0.5">
                <div className="font-pixel text-[10px] text-purple-300 font-bold">HEALTH SACRIFICED FOR SOLUTION</div>
                <div className="text-slate-300 text-[11px] leading-relaxed">
                  This problem was <strong>not marked conquered</strong> and <strong>will be shown again</strong> in future dungeon runs so you can conquer it with your own logic!
                </div>
              </div>
            </div>
          </div>
        ) : (
          <p className="font-mono text-sm text-slate-300 mb-4">
            You struck down <span className="text-rose-400 font-bold">{currentProblem.monster.name}</span> with flawless algorithmic logic!
          </p>
        )}

        {/* Monster defeat quote */}
        <div className="bg-dungeon-card p-3 rounded-xl border border-slate-800 text-xs font-mono mb-5 italic text-slate-400">
          "{currentProblem.monster.defeatQuote}"
        </div>

        {/* Rewards Card */}
        <div className="bg-emerald-950/30 border border-emerald-500/30 rounded-xl p-3.5 mb-6 flex justify-around text-xs font-pixel text-slate-200">
          <div className="flex items-center gap-1.5 text-amber-400">
            <span>💰</span>
            <span>+{30 * currentFloor} GOLD</span>
          </div>
          <div className="flex items-center gap-1.5 text-sky-400">
            <span>✨</span>
            <span>+{50 * currentFloor} XP</span>
          </div>
        </div>

        {/* Next Floor / Map Actions */}
        <div className="flex flex-col sm:flex-row gap-3">
          <button
            onClick={async () => {
              if (!isWingBoss) {
                await advanceFloor();
              }
              setScreen('map');
            }}
            className="flex-1 py-3 px-4 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-pixel text-xs flex items-center justify-center gap-2 transition-colors border border-slate-700"
          >
            <Map className="w-4 h-4" />
            <span>DUNGEON MAP</span>
          </button>

          {!isWingBoss && (
            <button
              onClick={advanceFloor}
              className="flex-1 py-3 px-4 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-400 hover:to-teal-500 text-slate-950 font-pixel text-xs font-bold flex items-center justify-center gap-2 shadow-lg shadow-emerald-900/40 transition-all active:scale-95"
            >
              <span>NEXT FLOOR</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          )}
        </div>
      </motion.div>
    </motion.div>
  );
};
