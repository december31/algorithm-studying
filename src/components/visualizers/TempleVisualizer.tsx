import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { TempleFrame } from '../../types/visualizer';
import { Sparkles, RotateCcw, Hand } from 'lucide-react';
import { sfx } from '../../engine/sfx';

interface Props {
  frame: TempleFrame;
}

export const TempleVisualizer: React.FC<Props> = ({ frame }) => {
  const { grid: initialGrid, activeTile, neighborsToggled = [], touchesCount = 0, status, target } = frame;

  // Local interactive state allowing the user to click and toggle tiles directly
  const [interactiveGrid, setInteractiveGrid] = useState<number[][]>(() =>
    initialGrid.map((r) => [...r])
  );
  const [manualTouches, setManualTouches] = useState<number>(0);

  // Sync when frame changes
  useEffect(() => {
    setInteractiveGrid(initialGrid.map((r) => [...r]));
    setManualTouches(0);
  }, [initialGrid]);

  const n = interactiveGrid.length;

  // Check if grid is uniform
  const flat = interactiveGrid.flat();
  const litCount = flat.filter((x) => x === 1).length;
  const isUniform = litCount === 0 || litCount === flat.length;

  const handleTileClick = (r: number, c: number) => {
    sfx.playStep();
    setInteractiveGrid((prev) => {
      const next = prev.map((row) => [...row]);
      next[r][c] ^= 1;
      const deltas = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1],
      ];
      for (const [dr, dc] of deltas) {
        const nr = r + dr;
        const nc = c + dc;
        if (nr >= 0 && nr < n && nc >= 0 && nc < n) {
          next[nr][nc] ^= 1;
        }
      }
      return next;
    });
    setManualTouches((m) => m + 1);
  };

  const handleResetManual = () => {
    sfx.playStep();
    setInteractiveGrid(initialGrid.map((r) => [...r]));
    setManualTouches(0);
  };

  const isNeighbor = (r: number, c: number) => {
    return neighborsToggled.some((cell) => cell.row === r && cell.col === c);
  };

  const isActive = (r: number, c: number) => {
    return activeTile?.row === r && activeTile?.col === c;
  };

  // Determine cell sizing based on grid dimension
  const getCellSize = () => {
    if (n <= 3) return 'w-14 h-14 sm:w-16 sm:h-16 text-lg';
    if (n === 4) return 'w-11 h-11 sm:w-13 sm:h-13 text-sm';
    return 'w-9 h-9 sm:w-10 sm:h-10 text-xs';
  };

  const runes = ['ᚱ', 'ᚲ', 'ᚷ', 'ᚹ', 'ᚺ', 'ᛃ', 'ᛈ', 'ᛉ', 'ᛊ', 'ᛏ', 'ᛒ', 'ᛖ', 'ᛗ', 'ᛚ'];

  return (
    <div className="w-full flex flex-col items-center justify-center p-3 select-none">
      {/* Top Status Bar */}
      <div className="w-full max-w-md flex items-center justify-between gap-2 mb-3 px-2">
        <div className="flex items-center gap-2">
          <div className="flex items-center gap-1 font-pixel text-[10px] text-amber-400 bg-amber-950/60 border border-amber-600/40 px-2 py-0.5 rounded">
            <Sparkles className="w-3 h-3 text-amber-400" />
            <span>TOUCHES: {touchesCount + manualTouches}</span>
          </div>
          {target !== undefined && (
            <span className="font-mono text-[10px] text-slate-400">
              Target: <strong className="text-amber-300">{target === 1 ? 'All 1s' : 'All 0s'}</strong>
            </span>
          )}
        </div>

        <div className="flex items-center gap-2">
          <span
            className={`font-pixel text-[10px] px-2 py-0.5 rounded border ${
              isUniform
                ? 'bg-emerald-950 text-emerald-300 border-emerald-500 animate-pulse'
                : 'bg-slate-900 text-slate-400 border-slate-700'
            }`}
          >
            {isUniform ? 'UNLOCKED ✨' : 'LOCKED 🔒'}
          </span>
          {manualTouches > 0 && (
            <button
              onClick={handleResetManual}
              className="p-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs flex items-center gap-1"
              title="Reset manual clicks"
            >
              <RotateCcw className="w-3 h-3" />
            </button>
          )}
        </div>
      </div>

      {/* Grid Platform Frame */}
      <div className="relative p-4 rounded-2xl bg-gradient-to-b from-stone-900 via-stone-950 to-slate-950 border-2 border-amber-900/60 shadow-[0_0_25px_rgba(245,158,11,0.15)] flex flex-col items-center">
        {/* Stone Grid */}
        <div className="flex flex-col gap-2">
          {interactiveGrid.map((row, r) => (
            <div key={`row-${r}`} className="flex gap-2">
              {row.map((val, c) => {
                const active = isActive(r, c);
                const neighbor = isNeighbor(r, c);
                const isLit = val === 1;
                const runeChar = runes[(r * n + c) % runes.length];

                return (
                  <motion.button
                    key={`tile-${r}-${c}`}
                    whileHover={{ scale: 1.05 }}
                    whileTap={{ scale: 0.95 }}
                    onClick={() => handleTileClick(r, c)}
                    title={`Tile (${r}, ${c}) - Click to touch!`}
                    className={`${getCellSize()} rounded-xl border-2 flex flex-col items-center justify-center font-pixel font-bold relative transition-all cursor-pointer ${
                      active
                        ? 'border-emerald-400 bg-emerald-950 shadow-[0_0_20px_rgba(52,211,153,0.8)] scale-110 z-20 ring-2 ring-emerald-300'
                        : neighbor
                        ? 'border-amber-400 bg-amber-950/70 shadow-[0_0_15px_rgba(251,191,36,0.6)] z-10'
                        : isLit
                        ? 'border-amber-500/80 bg-gradient-to-br from-amber-600/30 to-yellow-500/20 text-amber-200 shadow-[0_0_12px_rgba(245,158,11,0.4)]'
                        : 'border-slate-800 bg-slate-900/90 text-slate-600 hover:border-slate-600'
                    }`}
                  >
                    {/* Rune Symbol */}
                    <span
                      className={`text-base sm:text-lg transition-colors ${
                        isLit ? 'text-amber-300 drop-shadow-[0_0_8px_rgba(251,191,36,0.8)]' : 'text-slate-600'
                      }`}
                    >
                      {runeChar}
                    </span>

                    {/* Numeric Value 0 / 1 */}
                    <span className="font-mono text-[9px] opacity-75">{val}</span>

                    {/* Active Touch Indicator Badge */}
                    <AnimatePresence>
                      {active && (
                        <motion.div
                          initial={{ scale: 0, opacity: 0 }}
                          animate={{ scale: 1, opacity: 1 }}
                          exit={{ scale: 0, opacity: 0 }}
                          className="absolute -top-2.5 -right-2 bg-emerald-500 text-slate-950 font-pixel text-[8px] px-1 rounded-sm shadow-md flex items-center gap-0.5"
                        >
                          <Hand className="w-2.5 h-2.5" />
                          <span>TOUCH</span>
                        </motion.div>
                      )}
                    </AnimatePresence>
                  </motion.button>
                );
              })}
            </div>
          ))}
        </div>

        {/* Interactive Helper Hint */}
        <div className="mt-3 flex items-center gap-1.5 font-mono text-[10px] text-slate-400">
          <Hand className="w-3 h-3 text-amber-400" />
          <span>Click any stone rune to physically test tile inverting!</span>
        </div>
      </div>
    </div>
  );
};
