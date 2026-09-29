import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { AlertTriangle, X, Flame } from 'lucide-react';

interface SolutionModalProps {
  isOpen: boolean;
  onClose: () => void;
  onConfirm: () => void;
  language: 'python' | 'javascript';
  currentHp: number;
  monsterName: string;
  cost?: number;
}

const FUNNY_ROASTS = [
  "A true 10x engineer would just rewrite it in Rust, but here we are.",
  "Looking at solutions? Even ChatGPT is shaking its neural weights in silence.",
  "The dungeon monster promises not to leak this forfeit to your LinkedIn network.",
  "Sacrificing 25 HP... because time complexity hurts worse than physical trauma.",
  "Ancient dungeon law says: 'Copying without understanding is the purest dark magic.'",
  "Your CPU fans will spin in quiet disappointment, but the scroll is yours.",
  "Somewhere in the ethereal plane, Donald Knuth just felt a cold shiver.",
  "StackOverflow was down, so you resorted to ancient blood magic. Respectable.",
  "The monster whispers: 'First time seeing a Hash Map, hero?'",
  "A small price to pay for salvation... and a shattered ego.",
];

export const SolutionModal: React.FC<SolutionModalProps> = ({
  isOpen,
  onClose,
  onConfirm,
  language,
  currentHp,
  monsterName,
  cost = 25,
}) => {
  const [roast, setRoast] = useState(FUNNY_ROASTS[0]);

  // Pick a fresh funny roast each time the modal opens
  useEffect(() => {
    if (isOpen) {
      const randomIdx = Math.floor(Math.random() * FUNNY_ROASTS.length);
      setRoast(FUNNY_ROASTS[randomIdx]);
    }
  }, [isOpen]);

  const canAfford = currentHp > cost;

  return (
    <AnimatePresence>
      {isOpen && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.2 }}
          className="fixed inset-0 z-50 flex items-center justify-center bg-black/85 backdrop-blur-md p-4"
          onClick={(e) => {
            if (e.target === e.currentTarget) onClose();
          }}
        >
          <motion.div
            initial={{ scale: 0.85, opacity: 0, y: 25, rotate: -2 }}
            animate={{ scale: 1, opacity: 1, y: 0, rotate: 0 }}
            exit={{ scale: 0.85, opacity: 0, y: 25, rotate: 2 }}
            transition={{ type: 'spring', damping: 24, stiffness: 320 }}
            className="max-w-md w-full bg-dungeon-darkest border-2 border-purple-500 rounded-2xl p-6 shadow-[0_0_50px_rgba(168,85,247,0.35)] relative overflow-hidden select-none"
          >
            {/* Dark magic ambient glow */}
            <div className="absolute inset-0 bg-gradient-to-b from-purple-950/40 via-transparent to-rose-950/20 pointer-events-none" />

            {/* Close Button */}
            <button
              onClick={onClose}
              className="absolute top-4 right-4 p-1.5 rounded-lg text-slate-400 hover:text-slate-200 hover:bg-slate-800 transition-colors z-10"
              title="Close"
            >
              <X className="w-4 h-4" />
            </button>

            {/* Demon / Scroll Avatar */}
            <div className="relative mx-auto mb-4 w-16 h-16 rounded-2xl bg-purple-950/90 border-2 border-purple-500 flex items-center justify-center shadow-[0_0_20px_rgba(168,85,247,0.5)]">
              <span className="text-3xl select-none animate-bounce">📜</span>
              <div className="absolute -top-1.5 -right-1.5 bg-rose-600 text-white rounded-full p-0.5 shadow">
                <Flame className="w-3.5 h-3.5 fill-current" />
              </div>
            </div>

            {/* Funny Header Title */}
            <h2 className="font-pixel text-center text-sm sm:text-base text-purple-400 tracking-wider mb-1">
              THE FORBIDDEN SCROLL OF SHAME
            </h2>
            <div className="text-center font-mono text-[11px] text-purple-300/80 mb-4">
              Deal with the Algo-Demons for canonical {language === 'python' ? '🐍 Python' : '⚡ JavaScript'} solution
            </div>

            {/* Roast Box */}
            <div className="bg-purple-950/40 border border-purple-500/30 rounded-xl p-3.5 mb-4 text-center">
              <p className="font-mono text-xs text-purple-200 italic leading-relaxed">
                "{roast}"
              </p>
              <div className="text-[10px] font-pixel text-rose-400 mt-2">
                — {monsterName} watches you smirk
              </div>
            </div>

            {/* HP Sacrifice Cost Breakdown */}
            <div className="bg-dungeon-card p-3 rounded-xl border border-slate-800 mb-5 space-y-1.5 text-xs font-mono">
              <div className="flex justify-between items-center text-slate-400">
                <span>Current Vitality:</span>
                <span className="text-slate-200 font-bold">{currentHp} HP</span>
              </div>
              <div className="flex justify-between items-center text-rose-400">
                <span className="flex items-center gap-1">
                  <AlertTriangle className="w-3.5 h-3.5" /> Blood Price:
                </span>
                <span className="font-bold font-pixel text-rose-500">-{cost} HP</span>
              </div>
              <div className="flex justify-between items-center text-slate-400 pt-1.5 border-t border-slate-800">
                <span>Vitality After Deal:</span>
                <span className={`font-bold ${canAfford ? 'text-emerald-400' : 'text-rose-500 font-pixel'}`}>
                  {canAfford ? `${currentHp - cost} HP` : 'LETHAL (Forbidden)'}
                </span>
              </div>
            </div>

            {/* Action Buttons */}
            <div className="flex flex-col sm:flex-row gap-2.5">
              <button
                onClick={onClose}
                className="flex-1 py-2.5 px-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-pixel text-[11px] transition-colors border border-slate-700 text-center"
              >
                NO! I HAVE DIGNITY
              </button>

              <button
                onClick={() => {
                  if (canAfford) {
                    onConfirm();
                    onClose();
                  }
                }}
                disabled={!canAfford}
                className={`flex-1 py-2.5 px-3 rounded-xl font-pixel text-[11px] font-bold transition-all shadow-lg flex items-center justify-center gap-1.5 ${
                  canAfford
                    ? 'bg-gradient-to-r from-purple-600 to-rose-600 hover:from-purple-500 hover:to-rose-500 text-white shadow-purple-950/60 active:scale-95'
                    : 'bg-slate-800 text-slate-500 border border-slate-700 cursor-not-allowed opacity-50'
                }`}
              >
                <span>🩸</span>
                <span>{canAfford ? `TAKE THE CHEAT (-${cost} HP)` : `NEED ${cost + 1}+ HP`}</span>
              </button>
            </div>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
};
