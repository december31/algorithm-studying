import React from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { ArrayFrame } from '../../types/visualizer';

interface Props {
  frame: ArrayFrame;
}

export const ArrayVisualizer: React.FC<Props> = ({ frame }) => {
  const { array, pointers = [], highlights = [] } = frame;

  const getHighlightColor = (idx: number) => {
    for (const h of highlights) {
      if (h.indices.includes(idx)) {
        switch (h.color) {
          case 'active':
            return 'border-amber-400 bg-amber-500/20 text-amber-200 shadow-[0_0_15px_rgba(245,158,11,0.5)]';
          case 'compare':
            return 'border-sky-400 bg-sky-500/20 text-sky-200 shadow-[0_0_15px_rgba(56,189,248,0.5)]';
          case 'swap':
            return 'border-purple-400 bg-purple-500/30 text-purple-200 shadow-[0_0_20px_rgba(168,85,247,0.6)]';
          case 'found':
          case 'target':
            return 'border-emerald-400 bg-emerald-500/30 text-emerald-200 shadow-[0_0_20px_rgba(16,185,129,0.7)]';
        }
      }
    }
    return 'border-dungeon-border bg-dungeon-card/80 text-slate-200';
  };

  // Find max value to normalize height if numbers
  const numericValues = array.filter((v): v is number => typeof v === 'number');
  const maxVal = numericValues.length > 0 ? Math.max(...numericValues, 1) : 10;

  return (
    <div className="w-full flex flex-col items-center justify-center p-4 min-h-[220px]">
      {/* Array Bars & Pointers Container */}
      <div className="flex items-end justify-center gap-2 sm:gap-3 flex-wrap max-w-full pt-10 pb-4">
        {array.map((item, idx) => {
          const itemPointers = pointers.filter((p) => p.index === idx);
          const barHeight = typeof item === 'number'
            ? Math.max(36, Math.min(130, Math.round((Math.abs(item) / maxVal) * 120)))
            : 50;

          return (
            <div key={`item-${idx}`} className="flex flex-col items-center relative group">
              {/* Floating Pointers (e.g. L, R, Mid, i) */}
              <div className="absolute -top-9 flex flex-col items-center gap-0.5">
                <AnimatePresence>
                  {itemPointers.map((p) => (
                    <motion.div
                      key={p.name}
                      initial={{ y: -10, opacity: 0 }}
                      animate={{ y: 0, opacity: 1 }}
                      exit={{ y: -10, opacity: 0 }}
                      transition={{ type: 'spring', stiffness: 350, damping: 25 }}
                      style={{ backgroundColor: p.color || '#38bdf8' }}
                      className="px-2 py-0.5 rounded text-[10px] font-pixel font-bold text-slate-900 shadow-lg flex items-center gap-1"
                    >
                      <span>{p.name}</span>
                      <span className="text-[8px]">▼</span>
                    </motion.div>
                  ))}
                </AnimatePresence>
              </div>

              {/* Data Structure Element Bar */}
              <motion.div
                layout
                transition={{ type: 'spring', stiffness: 300, damping: 24 }}
                style={{ height: `${barHeight}px` }}
                className={`w-11 sm:w-14 rounded-t-md border-2 flex flex-col items-center justify-end pb-2 font-mono font-bold text-sm sm:text-base transition-colors ${getHighlightColor(
                  idx
                )}`}
              >
                <span>{item}</span>
              </motion.div>

              {/* Index Subscript */}
              <div className="mt-1 font-pixel text-[10px] text-slate-400">
                [{idx}]
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
