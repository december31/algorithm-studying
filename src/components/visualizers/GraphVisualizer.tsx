import React from 'react';
import { motion } from 'framer-motion';
import { GraphFrame } from '../../types/visualizer';

interface Props {
  frame: GraphFrame;
}

export const GraphVisualizer: React.FC<Props> = ({ frame }) => {
  const { nodes, edges, activeNodeId, queueOrStack } = frame;

  const nodeMap = new Map(nodes.map((n) => [n.id, n]));

  return (
    <div className="w-full flex flex-col items-center justify-center p-2 min-h-[220px]">
      <div className="relative w-full max-w-[480px] h-[220px] bg-dungeon-darker/60 rounded-xl border border-dungeon-border/50 p-2 overflow-hidden shadow-inner">
        {/* Graph Edges */}
        <svg className="absolute inset-0 w-full h-full pointer-events-none">
          {edges.map((e, idx) => {
            const fromNode = nodeMap.get(e.from);
            const toNode = nodeMap.get(e.to);
            if (!fromNode || !toNode) return null;

            return (
              <line
                key={`edge-${idx}-${e.from}-${e.to}`}
                x1={`${fromNode.x || 30}%`}
                y1={`${fromNode.y || 30}%`}
                x2={`${toNode.x || 70}%`}
                y2={`${toNode.y || 70}%`}
                stroke={e.active ? '#ec4899' : '#475569'}
                strokeWidth={e.active ? '3' : '1.5'}
                strokeDasharray={e.active ? undefined : '3 3'}
                className="transition-colors duration-300"
              />
            );
          })}
        </svg>

        {/* Graph Nodes */}
        {nodes.map((n) => {
          const isActive = activeNodeId === n.id;
          const isVisited = n.status === 'visited';

          return (
            <motion.div
              key={n.id}
              layout
              transition={{ type: 'spring', stiffness: 300, damping: 25 }}
              style={{
                left: `${n.x || 50}%`,
                top: `${n.y || 50}%`,
                transform: 'translate(-50%, -50%)',
              }}
              className={`absolute px-2.5 py-1.5 rounded-lg border-2 font-mono font-bold text-xs flex items-center justify-center shadow-lg transition-all ${
                isActive
                  ? 'border-pink-400 bg-pink-500/30 text-pink-200 shadow-[0_0_20px_rgba(236,72,153,0.7)] scale-110 z-10'
                  : isVisited
                  ? 'border-emerald-600 bg-emerald-950/60 text-emerald-300'
                  : 'border-slate-700 bg-dungeon-card text-slate-300'
              }`}
            >
              <span>{n.label}</span>
            </motion.div>
          );
        })}

        {/* Traversal Queue / Stack Badge */}
        {queueOrStack && queueOrStack.length > 0 && (
          <div className="absolute bottom-2 left-2 flex items-center gap-1.5 bg-dungeon-card/90 border border-slate-700 px-2 py-1 rounded text-[10px] font-mono">
            <span className="text-slate-400 font-pixel text-[8px]">QUEUE:</span>
            <span className="text-pink-300">[{queueOrStack.join(', ')}]</span>
          </div>
        )}
      </div>
    </div>
  );
};
