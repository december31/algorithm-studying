import React from 'react';
import { motion } from 'framer-motion';
import { TreeFrame, TreeNodeData } from '../../types/visualizer';

interface Props {
  frame: TreeFrame;
}

export const TreeVisualizer: React.FC<Props> = ({ frame }) => {
  const { nodes, activeNodeId } = frame;

  // Simple hierarchical layout for up to 3 levels (root, 2 children, 4 grandchildren)
  const nodeMap = new Map<string, TreeNodeData>();
  nodes.forEach((n) => nodeMap.set(n.id, n));

  const getNodePos = (idx: number, total: number) => {
    // If idx = 0 (root): centered
    if (idx === 0) return { x: 50, y: 15 };
    if (idx === 1) return { x: 28, y: 45 };
    if (idx === 2) return { x: 72, y: 45 };
    if (idx === 3) return { x: 16, y: 78 };
    if (idx === 4) return { x: 38, y: 78 };
    if (idx === 5) return { x: 62, y: 78 };
    if (idx === 6) return { x: 84, y: 78 };
    return { x: 10 + (idx * 12) % 80, y: 80 };
  };

  return (
    <div className="w-full flex flex-col items-center justify-center p-2 min-h-[220px]">
      <div className="relative w-full max-w-[460px] h-[220px] bg-dungeon-darker/60 rounded-xl border border-dungeon-border/50 p-2 overflow-hidden shadow-inner">
        {/* SVG Branch Lines */}
        <svg className="absolute inset-0 w-full h-full pointer-events-none">
          {nodes.map((n, i) => {
            const pos = getNodePos(i, nodes.length);
            const leftChild = n.leftId ? nodeMap.get(n.leftId) : null;
            const rightChild = n.rightId ? nodeMap.get(n.rightId) : null;

            const lines = [];
            if (leftChild) {
              const childIdx = nodes.findIndex((x) => x.id === leftChild.id);
              if (childIdx >= 0) {
                const childPos = getNodePos(childIdx, nodes.length);
                lines.push(
                  <line
                    key={`line-${n.id}-${leftChild.id}`}
                    x1={`${pos.x}%`}
                    y1={`${pos.y}%`}
                    x2={`${childPos.x}%`}
                    y2={`${childPos.y}%`}
                    stroke="#8b5cf6"
                    strokeWidth="2"
                    strokeDasharray="4 2"
                    opacity="0.6"
                  />
                );
              }
            }
            if (rightChild) {
              const childIdx = nodes.findIndex((x) => x.id === rightChild.id);
              if (childIdx >= 0) {
                const childPos = getNodePos(childIdx, nodes.length);
                lines.push(
                  <line
                    key={`line-${n.id}-${rightChild.id}`}
                    x1={`${pos.x}%`}
                    y1={`${pos.y}%`}
                    x2={`${childPos.x}%`}
                    y2={`${childPos.y}%`}
                    stroke="#8b5cf6"
                    strokeWidth="2"
                    strokeDasharray="4 2"
                    opacity="0.6"
                  />
                );
              }
            }
            return lines;
          })}
        </svg>

        {/* Tree Nodes */}
        {nodes.map((n, i) => {
          const pos = getNodePos(i, nodes.length);
          const isActive = activeNodeId === n.id;

          return (
            <motion.div
              key={n.id}
              layout
              transition={{ type: 'spring', stiffness: 350, damping: 25 }}
              style={{
                left: `${pos.x}%`,
                top: `${pos.y}%`,
                transform: 'translate(-50%, -50%)',
              }}
              className={`absolute w-10 h-10 sm:w-12 sm:h-12 rounded-full border-2 flex items-center justify-center font-mono font-bold text-xs sm:text-sm shadow-md transition-all ${
                isActive
                  ? 'border-purple-400 bg-purple-500/30 text-purple-200 shadow-[0_0_20px_rgba(168,85,247,0.7)] scale-110 z-10'
                  : 'border-purple-800 bg-dungeon-card text-purple-300'
              }`}
            >
              {n.val}
            </motion.div>
          );
        })}

        {nodes.length === 0 && (
          <div className="h-full flex items-center justify-center text-xs font-pixel text-slate-500">
            [EMPTY TREE]
          </div>
        )}
      </div>
    </div>
  );
};
