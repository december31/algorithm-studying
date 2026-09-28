import React from 'react';
import { motion } from 'framer-motion';
import { DPFrame } from '../../types/visualizer';

interface Props {
  frame: DPFrame;
}

export const DPVisualizer: React.FC<Props> = ({ frame }) => {
  const { grid, colLabels = [], activeCell, dependencyCells = [] } = frame;

  const isDependency = (r: number, c: number) => {
    return dependencyCells.some((cell) => cell.row === r && cell.col === c);
  };

  const isActive = (r: number, c: number) => {
    return activeCell?.row === r && activeCell?.col === c;
  };

  return (
    <div className="w-full flex flex-col items-center justify-center p-3 min-h-[220px]">
      <div className="flex flex-col items-center max-w-full overflow-x-auto p-2">
        <div className="text-[10px] font-pixel text-cyan-400 mb-2 tracking-wider">
          MEMOIZATION TABLE (SUBPROBLEMS)
        </div>

        {/* 1D / 2D DP Grid Table */}
        <div className="flex flex-col gap-1.5 bg-dungeon-darker/80 p-3 rounded-xl border border-cyan-800/40 shadow-inner">
          {/* Column Headers */}
          {colLabels.length > 0 && (
            <div className="flex gap-1.5 pb-1 border-b border-slate-700/50">
              {colLabels.map((lbl, idx) => (
                <div
                  key={`col-${idx}`}
                  className="w-12 sm:w-14 text-center font-pixel text-[9px] text-slate-400 truncate"
                  title={lbl}
                >
                  {lbl}
                </div>
              ))}
            </div>
          )}

          {/* Grid Rows */}
          {grid.map((row, rIdx) => (
            <div key={`row-${rIdx}`} className="flex gap-1.5 items-center">
              {row.map((val, cIdx) => {
                const active = isActive(rIdx, cIdx);
                const dep = isDependency(rIdx, cIdx);

                return (
                  <motion.div
                    key={`cell-${rIdx}-${cIdx}`}
                    layout
                    transition={{ type: 'spring', stiffness: 350, damping: 25 }}
                    className={`w-12 h-11 sm:w-14 sm:h-12 rounded-lg border-2 flex items-center justify-center font-mono font-bold text-xs sm:text-sm transition-all ${
                      active
                        ? 'border-cyan-400 bg-cyan-500/30 text-cyan-100 shadow-[0_0_18px_rgba(6,182,212,0.6)] scale-105 z-10'
                        : dep
                        ? 'border-amber-400/80 bg-amber-500/20 text-amber-200'
                        : 'border-slate-700 bg-dungeon-card/90 text-slate-300'
                    }`}
                  >
                    <span>{val ?? '-'}</span>
                  </motion.div>
                );
              })}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
