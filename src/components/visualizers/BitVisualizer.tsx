import React from 'react';
import { BitFrame } from '../../types/visualizer';
import { motion } from 'framer-motion';

interface Props {
  frame: BitFrame;
}

export const BitVisualizer: React.FC<Props> = ({ frame }) => {
  const primaryBits = frame.binaryString.padStart(8, '0').split('');
  const secondaryBits = frame.secondaryBinary ? frame.secondaryBinary.padStart(8, '0').split('') : null;

  return (
    <div className="w-full h-full flex flex-col items-center justify-center p-4 space-y-4">
      {/* Operation Header */}
      <div className="flex items-center gap-3">
        <span className="font-pixel text-xs text-emerald-400 bg-emerald-950/80 px-2.5 py-1 rounded border border-emerald-600/40">
          REGISTER {primaryBits.length}-BIT
        </span>
        {frame.operation && (
          <span className="font-pixel text-xs text-amber-400 bg-amber-950/80 px-2.5 py-1 rounded border border-amber-600/40">
            OP: {frame.operation}
          </span>
        )}
        <span className="font-mono text-xs text-sky-300 bg-sky-950/80 px-2.5 py-1 rounded border border-sky-600/40 font-bold">
          DEC = {frame.decimalValue} (0x{frame.decimalValue.toString(16).toUpperCase()})
        </span>
      </div>

      {/* Primary Register Grid */}
      <div className="flex flex-col items-center gap-1">
        <div className="text-[10px] font-pixel text-slate-400 mb-0.5">BITS: MSB ➔ LSB</div>
        <div className="flex items-center gap-1.5 flex-wrap justify-center">
          {primaryBits.map((bit, idx) => {
            const bitPower = primaryBits.length - 1 - idx;
            const isHighlighted = frame.highlightIndices?.includes(bitPower) || frame.highlightIndices?.includes(idx);
            const isOne = bit === '1';

            return (
              <motion.div
                key={idx}
                initial={{ scale: 0.9 }}
                animate={{ scale: 1 }}
                className={`flex flex-col items-center justify-center w-9 sm:w-11 h-12 rounded-lg border-2 font-mono transition-all ${
                  isHighlighted
                    ? 'border-amber-400 bg-amber-950/70 text-amber-300 shadow-[0_0_12px_rgba(251,191,36,0.5)]'
                    : isOne
                    ? 'border-emerald-500 bg-emerald-950/60 text-emerald-300 shadow-[0_0_8px_rgba(16,185,129,0.3)]'
                    : 'border-slate-700 bg-slate-900/60 text-slate-500'
                }`}
              >
                <span className="font-pixel text-sm sm:text-base font-bold">{bit}</span>
                <span className="text-[8px] font-pixel text-slate-400">b{bitPower}</span>
              </motion.div>
            );
          })}
        </div>
      </div>

      {/* Secondary Register (if dual operand) */}
      {secondaryBits && (
        <div className="flex flex-col items-center gap-1 pt-1 border-t border-slate-800 w-full max-w-md">
          <div className="text-[10px] font-pixel text-amber-400">
            {frame.operation || 'OPERAND 2'}
          </div>
          <div className="flex items-center gap-1.5 flex-wrap justify-center">
            {secondaryBits.map((bit, idx) => {
              const bitPower = secondaryBits.length - 1 - idx;
              const isOne = bit === '1';

              return (
                <div
                  key={idx}
                  className={`flex flex-col items-center justify-center w-8 sm:w-10 h-10 rounded border font-mono ${
                    isOne
                      ? 'border-sky-500/80 bg-sky-950/50 text-sky-300'
                      : 'border-slate-800 bg-slate-900/40 text-slate-600'
                  }`}
                >
                  <span className="font-pixel text-xs">{bit}</span>
                  <span className="text-[7px] text-slate-500">b{bitPower}</span>
                </div>
              );
            })}
          </div>
        </div>
      )}
    </div>
  );
};
