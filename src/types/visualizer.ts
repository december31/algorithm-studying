export type VisualizerType = 'array' | 'stack' | 'linkedList' | 'tree' | 'graph' | 'dp' | 'temple' | 'bits';

export interface ArrayPointer {
  name: string; // e.g. 'left', 'right', 'mid', 'i', 'j'
  index: number;
  color?: string;
}

export interface ArrayFrame {
  type: 'array';
  array: (number | string)[];
  pointers?: ArrayPointer[];
  highlights?: {
    indices: number[];
    color: 'compare' | 'swap' | 'active' | 'found' | 'target';
  }[];
  secondaryArray?: (number | string)[];
  message: string;
}

export interface StackFrame {
  type: 'stack';
  stack: (string | number)[];
  queue?: (string | number)[];
  action?: 'push' | 'pop' | 'peek' | 'enqueue' | 'dequeue';
  activeItem?: string | number;
  message: string;
}

export interface LinkedListNode {
  id: string;
  val: number | string;
  nextId: string | null;
  isHead?: boolean;
  isTail?: boolean;
}

export interface LinkedListFrame {
  type: 'linkedList';
  nodes: LinkedListNode[];
  pointers?: {
    name: string;
    nodeId: string | null;
    color?: string;
  }[];
  activeNodeId?: string | null;
  message: string;
}

export interface TreeNodeData {
  id: string;
  val: number | string;
  leftId?: string | null;
  rightId?: string | null;
  status?: 'default' | 'active' | 'visited' | 'matched' | 'invalid';
}

export interface TreeFrame {
  type: 'tree';
  nodes: TreeNodeData[];
  rootId: string | null;
  activeNodeId?: string | null;
  traversalOrder?: (number | string)[];
  message: string;
}

export interface GraphNodeData {
  id: string;
  label: string;
  x?: number;
  y?: number;
  status?: 'unvisited' | 'queued' | 'active' | 'visited';
}

export interface GraphEdgeData {
  from: string;
  to: string;
  weight?: number;
  active?: boolean;
}

export interface GraphFrame {
  type: 'graph';
  nodes: GraphNodeData[];
  edges: GraphEdgeData[];
  activeNodeId?: string | null;
  queueOrStack?: string[];
  message: string;
}

export interface DPFrame {
  type: 'dp';
  dimensions: '1D' | '2D';
  rowLabels?: string[];
  colLabels?: string[];
  grid: (number | string | null)[][];
  activeCell?: { row: number; col: number };
  dependencyCells?: { row: number; col: number }[];
  message: string;
}

export interface TempleFrame {
  type: 'temple';
  grid: number[][]; // 0 or 1
  target?: 0 | 1;
  activeTile?: { row: number; col: number };
  neighborsToggled?: { row: number; col: number }[];
  touchesCount?: number;
  totalTouches?: number;
  status?: 'evaluating' | 'touched' | 'uniform' | 'failed';
  message: string;
}

export interface BitFrame {
  type: 'bits';
  binaryString: string;
  decimalValue: number;
  highlightIndices?: number[];
  operation?: string;
  secondaryBinary?: string;
  message: string;
}

export type VisualizerFrame =
  | ArrayFrame
  | StackFrame
  | LinkedListFrame
  | TreeFrame
  | GraphFrame
  | DPFrame
  | TempleFrame
  | BitFrame;
