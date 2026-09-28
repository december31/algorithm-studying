import React from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { LinkedListFrame } from '../../types/visualizer';

interface Props {
  frame: LinkedListFrame;
}

export const LinkedListVisualizer: React.FC<Props> = ({ frame }) => {
  const { nodes, pointers = [], activeNodeId } = frame;

  return (
    <div className="w-full flex flex-col items-center justify-center p-4 min-h-[220px] overflow-x-auto">
      <div className="flex items-center gap-2 sm:gap-4 flex-nowrap py-10 px-4">
        {nodes.map((node, idx) => {
          const nodePointers = pointers.filter((p) => p.nodeId === node.id);
          const isActive = activeNodeId === node.id;

          return (
            <React.Fragment key={node.id}>
              {/* Linked List Node Item */}
              <div className="flex flex-col items-center relative group flex-shrink-0">
                {/* Floating Pointer tags */}
                <div className="absolute -top-10 flex flex-col items-center gap-1">
                  <AnimatePresence>
                    {nodePointers.map((p) => (
                      <motion.div
                        key={p.name}
                        initial={{ y: -6, opacity: 0 }}
                        animate={{ y: 0, opacity: 1 }}
                        exit={{ y: -6, opacity: 0 }}
                        style={{ backgroundColor: p.color || '#10b981' }}
                        className="px-2 py-0.5 rounded text-[9px] font-pixel font-bold text-slate-900 shadow-md flex items-center gap-0.5"
                      >
                        <span>{p.name}</span>
                        <span>▼</span>
                      </motion.div>
                    ))}
                  </AnimatePresence>
                </div>

                {/* Node Box */}
                <motion.div
                  layout
                  transition={{ type: 'spring', stiffness: 300, damping: 25 }}
                  className={`w-14 h-14 sm:w-16 sm:h-16 rounded-lg border-2 flex flex-col items-center justify-center font-mono font-bold text-base transition-colors ${
                    isActive
                      ? 'border-emerald-400 bg-emerald-500/20 text-emerald-200 shadow-[0_0_18px_rgba(16,185,129,0.5)]'
                      : 'border-slate-600 bg-dungeon-card/90 text-slate-200'
                  }`}
                >
                  <span className="text-sm sm:text-base">{node.val}</span>
                  <span className="text-[9px] text-slate-500 font-pixel mt-0.5">
                    {node.isHead ? 'HEAD' : node.isTail ? 'TAIL' : `node`}
                  </span>
                </motion.div>

                {/* Index / ID caption */}
                <div className="mt-1 font-pixel text-[9px] text-slate-400">
                  [{idx}]
                </div>
              </div>

              {/* Connecting Arrow to next node */}
              {idx < nodes.length - 1 ? (
                <div className="flex items-center text-emerald-400/80 px-0.5">
                  <svg className="w-6 h-6 stroke-current stroke-2 fill-none" viewBox="0 0 24 24">
                    <path d="M5 12h14M13 6l6 6-6 6" />
                  </svg>
                </div>
              ) : (
                <div className="flex items-center text-rose-400/70 font-mono text-xs px-2 font-bold">
                  → NULL
                </div>
              )}
            </React.Fragment>
          );
        })}

        {nodes.length === 0 && (
          <div className="text-slate-500 font-pixel text-xs py-8">
            [EMPTY LINKED LIST]
          </div>
        )}
      </div>
    </div>
  );
};
