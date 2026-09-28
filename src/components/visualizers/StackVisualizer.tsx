import React from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { StackFrame } from '../../types/visualizer';

interface Props {
  frame: StackFrame;
}

export const StackVisualizer: React.FC<Props> = ({ frame }) => {
  const { stack, action, activeItem } = frame;

  return (
    <div className="w-full flex flex-col sm:flex-row items-center justify-around gap-6 p-4 min-h-[220px]">
      {/* Stack Chamber Container */}
      <div className="flex flex-col items-center">
        <div className="text-xs font-pixel text-slate-300 mb-2 flex items-center gap-2">
          <span>LIFO STACK CHAMBER</span>
          <span className="text-[10px] text-amber-400 font-mono">[{stack.length} items]</span>
        </div>

        {/* Vertical Stack Tube */}
        <div className="w-44 sm:w-56 h-48 border-x-2 border-b-2 border-amber-500/60 bg-dungeon-darker/80 rounded-b-xl p-2 flex flex-col-reverse gap-1.5 overflow-hidden shadow-[inset_0_0_20px_rgba(245,158,11,0.15)] relative">
          {/* Top Indicator */}
          {stack.length > 0 && (
            <div className="absolute top-2 right-2 text-[9px] font-pixel text-amber-400 bg-amber-950/80 border border-amber-600/50 px-1.5 py-0.5 rounded">
              TOP
            </div>
          )}

          <AnimatePresence mode="popLayout">
            {stack.map((item, idx) => {
              const isTop = idx === stack.length - 1;
              return (
                <motion.div
                  key={`stack-${idx}-${item}`}
                  initial={{ y: -60, opacity: 0, scale: 0.8 }}
                  animate={{ y: 0, opacity: 1, scale: 1 }}
                  exit={{ y: -40, opacity: 0, scale: 0.6 }}
                  transition={{ type: 'spring', stiffness: 400, damping: 25 }}
                  className={`w-full py-1.5 px-3 rounded border font-mono font-bold text-center text-xs sm:text-sm flex items-center justify-between ${
                    isTop
                      ? 'border-amber-400 bg-amber-500/20 text-amber-200 shadow-[0_0_12px_rgba(245,158,11,0.4)]'
                      : 'border-slate-700 bg-dungeon-card/90 text-slate-300'
                  }`}
                >
                  <span className="text-[10px] text-slate-500 font-pixel">#{idx}</span>
                  <span className="truncate">{item}</span>
                  {isTop ? (
                    <span className="text-[9px] text-amber-300 font-pixel">▲</span>
                  ) : (
                    <span className="w-2" />
                  )}
                </motion.div>
              );
            })}
          </AnimatePresence>

          {stack.length === 0 && (
            <div className="h-full flex items-center justify-center text-xs font-pixel text-slate-500 italic">
              [EMPTY STACK]
            </div>
          )}
        </div>
      </div>

      {/* Action Indicator / Operation Badge */}
      {action && (
        <div className="flex flex-col items-center gap-2">
          <div className="text-[10px] font-pixel text-slate-400 uppercase">Operation</div>
          <div
            className={`px-4 py-2 rounded-lg border-2 font-pixel text-xs tracking-wider uppercase shadow-lg ${
              action === 'push'
                ? 'border-emerald-500 bg-emerald-950/70 text-emerald-300 shadow-emerald-900/50'
                : 'border-rose-500 bg-rose-950/70 text-rose-300 shadow-rose-900/50'
            }`}
          >
            {action} {activeItem !== undefined ? `(${activeItem})` : ''}
          </div>
        </div>
      )}
    </div>
  );
};
