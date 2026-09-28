import { Problem } from '../../types/problem';
import { TreeFrame, ArrayFrame } from '../../types/visualizer';

export const backtrackingProblems: Problem[] = [
  // 🟢 EASY (7 Problems)
  {
    id: 'binary-tree-paths',
    wingId: 'backtracking',
    floor: 1,
    title: 'Binary Tree Paths (Leaf Route Exploration)',
    difficulty: 'easy',
    visualizerType: 'tree',
    monster: {
      id: 'path-imp',
      name: 'Twig the Root Imp',
      title: 'Scout of the Branching Trails',
      maxHp: 3,
      hp: 3,
      sprite: 'slime',
      color: '#10b981',
      attackName: 'Briar Thorn Whip',
      attackPower: 1,
      defeatQuote: 'All my branch trails were navigated...',
    },
    description: `Given the root of a binary tree represented as an array in level-order, return all root-to-leaf paths in any order. A leaf is a node with no children.`,
    examples: [
      { input: 'root = [1, 2, 3, null, 5]', output: '["1->2->5","1->3"]' },
      { input: 'root = [1]', output: '["1"]' },
    ],
    constraints: ['The number of nodes in the tree is in the range [1, 100].', '-100 <= Node.val <= 100'],
    starterCode: `function binaryTreePaths(root) {
  return [];
}`,
    solutionCode: `function binaryTreePaths(root) {
  if (!root || root.length === 0 || root[0] === null) return [];
  const paths = [];
  function dfs(idx, currPath) {
    if (idx >= root.length || root[idx] === null || root[idx] === undefined) return;
    const next = currPath === '' ? String(root[idx]) : currPath + '->' + root[idx];
    const leftIdx = 2 * idx + 1;
    const rightIdx = 2 * idx + 2;
    const isLeaf = (leftIdx >= root.length || root[leftIdx] === null || root[leftIdx] === undefined) &&
                   (rightIdx >= root.length || root[rightIdx] === null || root[rightIdx] === undefined);
    if (isLeaf) {
      paths.push(next);
      return;
    }
    dfs(leftIdx, next);
    dfs(rightIdx, next);
  }
  dfs(0, '');
  return paths;
}`,
    functionName: 'binaryTreePaths',
    testCases: [
      { id: 1, input: [[1, 2, 3, null, 5]], expected: ["1->2->5", "1->3"], inputDisplay: 'root = [1, 2, 3, null, 5]', expectedDisplay: '["1->2->5", "1->3"]' },
      { id: 2, input: [[1]], expected: ["1"], inputDisplay: 'root = [1]', expectedDisplay: '["1"]' },
      { id: 3, input: [[1, 2, null]], expected: ["1->2"], inputDisplay: 'root = [1, 2, null]', expectedDisplay: '["1->2"]' },
    ],
    hints: ['Recursively traverse downwards passing the current path string until reaching a leaf node.'],
    generateDefaultFrames: (tc) => {
      const arr = tc.input[0];
      return [{
        type: 'tree',
        nodes: arr.map((v: any, i: number) => ({
          id: `n-${i}`,
          val: v ?? 'null',
          leftId: 2 * i + 1 < arr.length ? `n-${2 * i + 1}` : null,
          rightId: 2 * i + 2 < arr.length ? `n-${2 * i + 2}` : null,
        })),
        rootId: 'n-0',
        message: 'Exploring tree branches from root down to leaves',
      }];
    },
  },
  {
    id: 'sum-of-all-subset-xor-totals',
    wingId: 'backtracking',
    floor: 2,
    title: 'Sum of All Subset XOR Totals (Power-Set Search)',
    difficulty: 'easy',
    visualizerType: 'array',
    monster: {
      id: 'xor-specter',
      name: 'Vael the Combinatorial Specter',
      title: 'Summoner of Power-Set States',
      maxHp: 3,
      hp: 3,
      sprite: 'wraith',
      color: '#8b5cf6',
      attackName: 'Bitwise Phase Strike',
      attackPower: 1,
      defeatQuote: 'The power-set XOR sum unraveled my form...',
    },
    description: `The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

Given an array \`nums\`, return the sum of all XOR totals for every subset of \`nums\`.`,
    examples: [
      { input: 'nums = [1, 3]', output: '6' },
      { input: 'nums = [5, 1, 6]', output: '28' },
    ],
    constraints: ['1 <= nums.length <= 12', '1 <= nums[i] <= 20'],
    starterCode: `function subsetXORSum(nums) {
  return 0;
}`,
    solutionCode: `function subsetXORSum(nums) {
  let total = 0;
  function backtrack(idx, currentXor) {
    if (idx === nums.length) {
      total += currentXor;
      return;
    }
    // Include nums[idx]
    backtrack(idx + 1, currentXor ^ nums[idx]);
    // Exclude nums[idx]
    backtrack(idx + 1, currentXor);
  }
  backtrack(0, 0);
  return total;
}`,
    functionName: 'subsetXORSum',
    testCases: [
      { id: 1, input: [[1, 3]], expected: 6, inputDisplay: 'nums = [1, 3]', expectedDisplay: '6' },
      { id: 2, input: [[5, 1, 6]], expected: 28, inputDisplay: 'nums = [5, 1, 6]', expectedDisplay: '28' },
      { id: 3, input: [[3, 4, 5, 6, 7, 8]], expected: 480, inputDisplay: 'nums = [3, 4, 5, 6, 7, 8]', expectedDisplay: '480' },
    ],
    hints: ['At each element, branch into two choices: include in the XOR total or exclude it.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], message: 'Exploring 2^N subset combinations with recursive branching' }],
  },
  {
    id: 'invert-binary-tree',
    wingId: 'backtracking',
    floor: 3,
    title: 'Invert Binary Tree (Complete Search & Swap)',
    difficulty: 'easy',
    visualizerType: 'tree',
    monster: {
      id: 'mirror-treant',
      name: 'Oakbeard the Inverted Ent',
      title: 'Mirrorer of Ancient Foliage',
      maxHp: 3,
      hp: 3,
      sprite: 'treant',
      color: '#15803d',
      attackName: 'Reversed Branch Slam',
      attackPower: 1,
      defeatQuote: 'My canopy has been mirrored into perfection...',
    },
    description: `Given the root of a binary tree represented as an array in level-order, invert the tree, and return its level-order array representation.`,
    examples: [
      { input: 'root = [4, 2, 7, 1, 3, 6, 9]', output: '[4, 7, 2, 9, 6, 3, 1]' },
      { input: 'root = [2, 1, 3]', output: '[2, 3, 1]' },
    ],
    constraints: ['The number of nodes in the tree is in the range [0, 100].', '-100 <= Node.val <= 100'],
    starterCode: `function invertTree(root) {
  return [];
}`,
    solutionCode: `function invertTree(root) {
  if (!root || root.length === 0) return [];
  class Node {
    constructor(val) {
      this.val = val;
      this.left = null;
      this.right = null;
    }
  }
  const rootNode = new Node(root[0]);
  const q = [rootNode];
  let i = 1;
  while (q.length && i < root.length) {
    const curr = q.shift();
    if (i < root.length && root[i] !== null) {
      curr.left = new Node(root[i]);
      q.push(curr.left);
    }
    i++;
    if (i < root.length && root[i] !== null) {
      curr.right = new Node(root[i]);
      q.push(curr.right);
    }
    i++;
  }
  function invert(node) {
    if (!node) return null;
    const temp = node.left;
    node.left = invert(node.right);
    node.right = invert(temp);
    return node;
  }
  invert(rootNode);
  const res = [];
  const outQ = [rootNode];
  while (outQ.length) {
    const curr = outQ.shift();
    if (curr) {
      res.push(curr.val);
      outQ.push(curr.left);
      outQ.push(curr.right);
    }
  }
  return res;
}`,
    functionName: 'invertTree',
    testCases: [
      { id: 1, input: [[4, 2, 7, 1, 3, 6, 9]], expected: [4, 7, 2, 9, 6, 3, 1], inputDisplay: 'root = [4, 2, 7, 1, 3, 6, 9]', expectedDisplay: '[4, 7, 2, 9, 6, 3, 1]' },
      { id: 2, input: [[2, 1, 3]], expected: [2, 3, 1], inputDisplay: 'root = [2, 1, 3]', expectedDisplay: '[2, 3, 1]' },
      { id: 3, input: [[]], expected: [], inputDisplay: 'root = []', expectedDisplay: '[]' },
    ],
    hints: ['Recursively swap left and right subtrees for every node in the tree.'],
    generateDefaultFrames: (tc) => [{ type: 'tree', nodes: [], rootId: '0', message: 'Inverting left and right children recursively' }],
  },
  {
    id: 'path-sum',
    wingId: 'backtracking',
    floor: 4,
    title: 'Path Sum (Target Subtraction Backtracking)',
    difficulty: 'easy',
    visualizerType: 'tree',
    monster: {
      id: 'sum-gargoyle',
      name: 'Petra the Weighted Gargoyle',
      title: 'Sentinel of the Exact Total',
      maxHp: 3,
      hp: 3,
      sprite: 'gargoyle',
      color: '#475569',
      attackName: 'Stone Pressure Crush',
      attackPower: 1,
      defeatQuote: 'The path sum matched the runic lock...',
    },
    description: `Given the root of a binary tree and an integer \`targetSum\`, return \`true\` if the tree has a root-to-leaf path such that adding up all the values along the path equals \`targetSum\`.`,
    examples: [
      { input: 'root = [5, 4, 8, 11, null, 13, 4, 7, 2], targetSum = 22', output: 'true' },
      { input: 'root = [1, 2, 3], targetSum = 5', output: 'false' },
    ],
    constraints: ['The number of nodes in the tree is in the range [0, 5000].', '-1000 <= targetSum <= 1000'],
    starterCode: `function hasPathSum(root, targetSum) {
  return false;
}`,
    solutionCode: `function hasPathSum(root, targetSum) {
  if (!root || root.length === 0 || root[0] === null) return false;
  function dfs(idx, remaining) {
    if (idx >= root.length || root[idx] === null || root[idx] === undefined) return false;
    const current = remaining - root[idx];
    const left = 2 * idx + 1;
    const right = 2 * idx + 2;
    const isLeaf = (left >= root.length || root[left] === null || root[left] === undefined) &&
                   (right >= root.length || root[right] === null || root[right] === undefined);
    if (isLeaf) return current === 0;
    return dfs(left, current) || dfs(right, current);
  }
  return dfs(0, targetSum);
}`,
    functionName: 'hasPathSum',
    testCases: [
      { id: 1, input: [[5, 4, 8, 11, null, 13, 4, 7, 2], 22], expected: true, inputDisplay: 'root = [5,4,8,...], targetSum = 22', expectedDisplay: 'true' },
      { id: 2, input: [[1, 2, 3], 5], expected: false, inputDisplay: 'root = [1, 2, 3], targetSum = 5', expectedDisplay: 'false' },
      { id: 3, input: [[], 0], expected: false, inputDisplay: 'root = [], targetSum = 0', expectedDisplay: 'false' },
    ],
    hints: ['Subtract current node value from targetSum and check if leaf reaches exactly 0.'],
    generateDefaultFrames: (tc) => [{ type: 'tree', nodes: [], rootId: '0', message: `Verifying path sum against target ${tc.input[1]}` }],
  },
  {
    id: 'maximum-depth-of-binary-tree',
    wingId: 'backtracking',
    floor: 5,
    title: 'Maximum Depth of Binary Tree (Height Search)',
    difficulty: 'easy',
    visualizerType: 'tree',
    monster: {
      id: 'altitude-spider',
      name: 'Silas the Tower Web Spinner',
      title: 'Weaver of Tree Altitudes',
      maxHp: 3,
      hp: 3,
      sprite: 'spider',
      color: '#0284c7',
      attackName: 'Silken Descent',
      attackPower: 1,
      defeatQuote: 'My tallest branch could not evade you...',
    },
    description: `Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.`,
    examples: [
      { input: 'root = [3, 9, 20, null, null, 15, 7]', output: '3' },
      { input: 'root = [1, null, 2]', output: '2' },
    ],
    constraints: ['The number of nodes in the tree is in the range [0, 10^4].', '-100 <= Node.val <= 100'],
    starterCode: `function maxDepth(root) {
  return 0;
}`,
    solutionCode: `function maxDepth(root) {
  if (!root || root.length === 0 || root[0] === null) return 0;
  function getDepth(idx) {
    if (idx >= root.length || root[idx] === null || root[idx] === undefined) return 0;
    return 1 + Math.max(getDepth(2 * idx + 1), getDepth(2 * idx + 2));
  }
  return getDepth(0);
}`,
    functionName: 'maxDepth',
    testCases: [
      { id: 1, input: [[3, 9, 20, null, null, 15, 7]], expected: 3, inputDisplay: 'root = [3, 9, 20, null, null, 15, 7]', expectedDisplay: '3' },
      { id: 2, input: [[1, null, 2]], expected: 2, inputDisplay: 'root = [1, null, 2]', expectedDisplay: '2' },
      { id: 3, input: [[]], expected: 0, inputDisplay: 'root = []', expectedDisplay: '0' },
    ],
    hints: ['Depth of node = 1 + max(depth(left), depth(right)). Base case returns 0.'],
    generateDefaultFrames: (tc) => [{ type: 'tree', nodes: [], rootId: '0', message: 'Measuring max depth with recursive post-order' }],
  },
  {
    id: 'same-tree',
    wingId: 'backtracking',
    floor: 6,
    title: 'Same Tree (Dual Structure Equivalence)',
    difficulty: 'easy',
    visualizerType: 'tree',
    monster: {
      id: 'mirror-lich',
      name: 'Twin-Soul the Dual Lich',
      title: 'Conjurer of Duplicate Phylacteries',
      maxHp: 3,
      hp: 3,
      sprite: 'lich',
      color: '#6366f1',
      attackName: 'Synchronous Ray',
      attackPower: 1,
      defeatQuote: 'Our dual structures were validated identical...',
    },
    description: `Given the roots of two binary trees \`p\` and \`q\`, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.`,
    examples: [
      { input: 'p = [1, 2, 3], q = [1, 2, 3]', output: 'true' },
      { input: 'p = [1, 2], q = [1, null, 2]', output: 'false' },
    ],
    constraints: ['The number of nodes in both trees is in the range [0, 100].'],
    starterCode: `function isSameTree(p, q) {
  return true;
}`,
    solutionCode: `function isSameTree(p, q) {
  if (p.length !== q.length) return false;
  for (let i = 0; i < p.length; i++) {
    if (p[i] !== q[i]) return false;
  }
  return true;
}`,
    functionName: 'isSameTree',
    testCases: [
      { id: 1, input: [[1, 2, 3], [1, 2, 3]], expected: true, inputDisplay: 'p = [1,2,3], q = [1,2,3]', expectedDisplay: 'true' },
      { id: 2, input: [[1, 2], [1, null, 2]], expected: false, inputDisplay: 'p = [1,2], q = [1,null,2]', expectedDisplay: 'false' },
      { id: 3, input: [[1, 2, 1], [1, 1, 2]], expected: false, inputDisplay: 'p = [1,2,1], q = [1,1,2]', expectedDisplay: 'false' },
    ],
    hints: ['Compare both trees node-by-node simultaneously.'],
    generateDefaultFrames: (tc) => [{ type: 'tree', nodes: [], rootId: '0', message: 'Comparing dual tree nodes for structural identity' }],
  },
  {
    id: 'binary-tree-inorder-traversal',
    wingId: 'backtracking',
    floor: 7,
    title: 'Binary Tree Inorder Traversal (LVR)',
    difficulty: 'easy',
    visualizerType: 'tree',
    monster: {
      id: 'order-skeleton',
      name: 'Ossis the Inorder Skeleton',
      title: 'Guardian of Left-Root-Right Sequence',
      maxHp: 3,
      hp: 3,
      sprite: 'skeleton',
      color: '#cbd5e1',
      attackName: 'Sorted Bone Slash',
      attackPower: 1,
      defeatQuote: 'The in-order traversal broke my spine...',
    },
    description: `Given the root of a binary tree, return the inorder traversal of its nodes' values. (Left -> Visit Node -> Right).`,
    examples: [
      { input: 'root = [1, null, 2, 3]', output: '[1, 3, 2]' },
      { input: 'root = []', output: '[]' },
      { input: 'root = [1]', output: '[1]' },
    ],
    constraints: ['The number of nodes in the tree is in the range [0, 100].'],
    starterCode: `function inorderTraversal(root) {
  return [];
}`,
    solutionCode: `function inorderTraversal(root) {
  if (!root || root.length === 0 || root[0] === null) return [];
  const result = [];
  function traverse(idx) {
    if (idx >= root.length || root[idx] === null || root[idx] === undefined) return;
    traverse(2 * idx + 1);
    result.push(root[idx]);
    traverse(2 * idx + 2);
  }
  traverse(0);
  return result;
}`,
    functionName: 'inorderTraversal',
    testCases: [
      { id: 1, input: [[1, null, 2, null, null, 3]], expected: [1, 3, 2], inputDisplay: 'root = [1, null, 2, 3]', expectedDisplay: '[1, 3, 2]' },
      { id: 2, input: [[]], expected: [], inputDisplay: 'root = []', expectedDisplay: '[]' },
      { id: 3, input: [[1]], expected: [1], inputDisplay: 'root = [1]', expectedDisplay: '[1]' },
    ],
    hints: ['Recursively visit the left subtree, process current node, then visit right subtree.'],
    generateDefaultFrames: (tc) => [{ type: 'tree', nodes: [], rootId: '0', message: 'Inorder traversal: Left -> Node -> Right' }],
  },

  // 🟡 MEDIUM (7 Problems)
  {
    id: 'subsets',
    wingId: 'backtracking',
    floor: 8,
    title: 'Subsets (Power Set Tree)',
    difficulty: 'medium',
    visualizerType: 'array',
    monster: {
      id: 'subset-sorcerer',
      name: 'Morvath the Subset Sorcerer',
      title: 'Conjuror of Combinatorial Trees',
      maxHp: 3,
      hp: 3,
      sprite: 'lich',
      color: '#8b5cf6',
      attackName: 'Power-Set Nova',
      attackPower: 2,
      defeatQuote: 'All 2^N subsets were mapped and extracted...',
    },
    description: `Given an integer array \`nums\` of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.`,
    examples: [
      { input: 'nums = [1, 2, 3]', output: '[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]' },
      { input: 'nums = [0]', output: '[[],[0]]' },
    ],
    constraints: ['1 <= nums.length <= 10', '-10 <= nums[i] <= 10', 'All elements of nums are unique.'],
    starterCode: `function subsets(nums) {
  return [];
}`,
    solutionCode: `function subsets(nums) {
  const result = [];
  function backtrack(start, current) {
    result.push([...current]);
    for (let i = start; i < nums.length; i++) {
      current.push(nums[i]);
      backtrack(i + 1, current);
      current.pop();
    }
  }
  backtrack(0, []);
  return result;
}`,
    functionName: 'subsets',
    testCases: [
      { id: 1, input: [[1, 2, 3]], expected: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]], inputDisplay: 'nums = [1, 2, 3]', expectedDisplay: '[[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]' },
      { id: 2, input: [[0]], expected: [[], [0]], inputDisplay: 'nums = [0]', expectedDisplay: '[[], [0]]' },
      { id: 3, input: [[1, 2]], expected: [[], [1], [1, 2], [2]], inputDisplay: 'nums = [1, 2]', expectedDisplay: '[[], [1], [1, 2], [2]]' },
    ],
    hints: ['For each index, branch by including the element and recursing, then backtrack (pop).'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], message: 'Exploring 2^N subsets using backtracking choose/explore/unchoose' }],
  },
  {
    id: 'permutations',
    wingId: 'backtracking',
    floor: 9,
    title: 'Permutations (Exhaustive Ordering Tree)',
    difficulty: 'medium',
    visualizerType: 'array',
    monster: {
      id: 'permutation-wraith',
      name: 'Vortex the Permutation Wraith',
      title: 'Spinner of Factorial Fates',
      maxHp: 3,
      hp: 3,
      sprite: 'wraith',
      color: '#d946ef',
      attackName: 'Factorial Spiral',
      attackPower: 2,
      defeatQuote: 'All N! arrangements were conquered...',
    },
    description: `Given an array \`nums\` of distinct integers, return all the possible permutations. You can return the answer in any order.`,
    examples: [
      { input: 'nums = [1, 2, 3]', output: '[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]' },
      { input: 'nums = [0, 1]', output: '[[0,1],[1,0]]' },
    ],
    constraints: ['1 <= nums.length <= 6', '-10 <= nums[i] <= 10', 'All the integers of nums are unique.'],
    starterCode: `function permute(nums) {
  return [];
}`,
    solutionCode: `function permute(nums) {
  const result = [];
  const used = new Array(nums.length).fill(false);
  function backtrack(current) {
    if (current.length === nums.length) {
      result.push([...current]);
      return;
    }
    for (let i = 0; i < nums.length; i++) {
      if (used[i]) continue;
      used[i] = true;
      current.push(nums[i]);
      backtrack(current);
      current.pop();
      used[i] = false;
    }
  }
  backtrack([]);
  return result;
}`,
    functionName: 'permute',
    testCases: [
      { id: 1, input: [[1, 2, 3]], expected: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]], inputDisplay: 'nums = [1, 2, 3]', expectedDisplay: '[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]' },
      { id: 2, input: [[0, 1]], expected: [[0,1],[1,0]], inputDisplay: 'nums = [0, 1]', expectedDisplay: '[[0,1],[1,0]]' },
      { id: 3, input: [[1]], expected: [[1]], inputDisplay: 'nums = [1]', expectedDisplay: '[[1]]' },
    ],
    hints: ['Track visited elements with a boolean array. Choose, recurse, then unchoose.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], message: 'Permuting elements with visited tracking array' }],
  },
  {
    id: 'combination-sum',
    wingId: 'backtracking',
    floor: 10,
    title: 'Combination Sum (Infinite Reuse Branching)',
    difficulty: 'medium',
    visualizerType: 'array',
    monster: {
      id: 'forge-golem',
      name: 'Volcanus the Combinatorial Golem',
      title: 'Smelter of Target Sums',
      maxHp: 3,
      hp: 3,
      sprite: 'golem',
      color: '#f97316',
      attackName: 'Molten Coin Volley',
      attackPower: 2,
      defeatQuote: 'The target sum was formed from the molten crucible...',
    },
    description: `Given an array of distinct integers \`candidates\` and a target integer \`target\`, return a list of all unique combinations of \`candidates\` where the chosen numbers sum to \`target\`. The same number may be chosen an unlimited number of times.`,
    examples: [
      { input: 'candidates = [2, 3, 6, 7], target = 7', output: '[[2,2,3],[7]]' },
      { input: 'candidates = [2, 3, 5], target = 8', output: '[[2,2,2,2],[2,3,3],[3,5]]' },
    ],
    constraints: ['1 <= candidates.length <= 30', '2 <= candidates[i] <= 40', '1 <= target <= 40'],
    starterCode: `function combinationSum(candidates, target) {
  return [];
}`,
    solutionCode: `function combinationSum(candidates, target) {
  const result = [];
  candidates.sort((a, b) => a - b);
  function backtrack(start, remain, current) {
    if (remain === 0) {
      result.push([...current]);
      return;
    }
    for (let i = start; i < candidates.length; i++) {
      if (candidates[i] > remain) break;
      current.push(candidates[i]);
      backtrack(i, remain - candidates[i], current);
      current.pop();
    }
  }
  backtrack(0, target, []);
  return result;
}`,
    functionName: 'combinationSum',
    testCases: [
      { id: 1, input: [[2, 3, 6, 7], 7], expected: [[2, 2, 3], [7]], inputDisplay: 'candidates = [2,3,6,7], target = 7', expectedDisplay: '[[2,2,3],[7]]' },
      { id: 2, input: [[2, 3, 5], 8], expected: [[2,2,2,2],[2,3,3],[3,5]], inputDisplay: 'candidates = [2,3,5], target = 8', expectedDisplay: '[[2,2,2,2],[2,3,3],[3,5]]' },
      { id: 3, input: [[2], 1], expected: [], inputDisplay: 'candidates = [2], target = 1', expectedDisplay: '[]' },
    ],
    hints: ['Sort candidates to prune early when candidate exceeds remaining sum. Pass `i` to allow reuse of same element.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], message: `Finding combinations summing to target ${tc.input[1]}` }],
  },
  {
    id: 'combinations',
    wingId: 'backtracking',
    floor: 11,
    title: 'Combinations (Length-Bounded Search)',
    difficulty: 'medium',
    visualizerType: 'array',
    monster: {
      id: 'combo-shade',
      name: 'Chrono the Bounded Shade',
      title: 'Keeper of n Choose k',
      maxHp: 3,
      hp: 3,
      sprite: 'wraith',
      color: '#3b82f6',
      attackName: 'Binomial Vortex',
      attackPower: 2,
      defeatQuote: 'All combinations of length K were extracted...',
    },
    description: `Given two integers \`n\` and \`k\`, return all possible combinations of \`k\` numbers chosen from the range \`[1, n]\`. You may return the answer in any order.`,
    examples: [
      { input: 'n = 4, k = 2', output: '[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]' },
      { input: 'n = 1, k = 1', output: '[[1]]' },
    ],
    constraints: ['1 <= n <= 20', '1 <= k <= n'],
    starterCode: `function combine(n, k) {
  return [];
}`,
    solutionCode: `function combine(n, k) {
  const result = [];
  function backtrack(start, current) {
    if (current.length === k) {
      result.push([...current]);
      return;
    }
    for (let i = start; i <= n; i++) {
      current.push(i);
      backtrack(i + 1, current);
      current.pop();
    }
  }
  backtrack(1, []);
  return result;
}`,
    functionName: 'combine',
    testCases: [
      { id: 1, input: [4, 2], expected: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]], inputDisplay: 'n = 4, k = 2', expectedDisplay: '[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]' },
      { id: 2, input: [1, 1], expected: [[1]], inputDisplay: 'n = 1, k = 1', expectedDisplay: '[[1]]' },
      { id: 3, input: [3, 3], expected: [[1, 2, 3]], inputDisplay: 'n = 3, k = 3', expectedDisplay: '[[1, 2, 3]]' },
    ],
    hints: ['Recursively choose next number from start to n, then backtrack.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: Array.from({ length: tc.input[0] }, (_, i) => i + 1), message: `Selecting ${tc.input[1]} numbers from 1..${tc.input[0]}` }],
  },
  {
    id: 'generate-parentheses',
    wingId: 'backtracking',
    floor: 12,
    title: 'Generate Parentheses (Constraint Pruning)',
    difficulty: 'medium',
    visualizerType: 'stack',
    monster: {
      id: 'parenthesis-djinn',
      name: 'Zul the Balance Djinn',
      title: 'Architect of Well-Formed Pairs',
      maxHp: 3,
      hp: 3,
      sprite: 'slime',
      color: '#06b6d4',
      attackName: 'Resonant Closure',
      attackPower: 2,
      defeatQuote: 'The opening and closing brackets reached equilibrium...',
    },
    description: `Given \`n\` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.`,
    examples: [
      { input: 'n = 3', output: '["((()))","(()())","(())()","()(())","()()()"]' },
      { input: 'n = 1', output: '["()"]' },
    ],
    constraints: ['1 <= n <= 8'],
    starterCode: `function generateParenthesis(n) {
  return [];
}`,
    solutionCode: `function generateParenthesis(n) {
  const result = [];
  function backtrack(open, close, current) {
    if (current.length === 2 * n) {
      result.push(current);
      return;
    }
    if (open < n) backtrack(open + 1, close, current + '(');
    if (close < open) backtrack(open, close + 1, current + ')');
  }
  backtrack(0, 0, '');
  return result;
}`,
    functionName: 'generateParenthesis',
    testCases: [
      { id: 1, input: [3], expected: ["((()))","(()())","(())()","()(())","()()()"], inputDisplay: 'n = 3', expectedDisplay: '["((()))","(()())","(())()","()(())","()()()"]' },
      { id: 2, input: [1], expected: ["()"], inputDisplay: 'n = 1', expectedDisplay: '["()"]' },
      { id: 3, input: [2], expected: ["(())", "()()"], inputDisplay: 'n = 2', expectedDisplay: '["(())", "()()"]' },
    ],
    hints: ['Only add "(" if open < n; only add ")" if close < open.'],
    generateDefaultFrames: (tc) => [{ type: 'stack', stack: [], message: `Generating valid parenthesis trees for n = ${tc.input[0]}` }],
  },
  {
    id: 'subsets-ii',
    wingId: 'backtracking',
    floor: 13,
    title: 'Subsets II (Duplicate Pruning)',
    difficulty: 'medium',
    visualizerType: 'array',
    monster: {
      id: 'clone-specter',
      name: 'Mirage the Duplicate Specter',
      title: 'Pruner of Redundant Branches',
      maxHp: 3,
      hp: 3,
      sprite: 'wraith',
      color: '#a855f7',
      attackName: 'Phantasmal Echo',
      attackPower: 2,
      defeatQuote: 'Duplicate subsets were pruned from the branch tree...',
    },
    description: `Given an integer array \`nums\` that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.`,
    examples: [
      { input: 'nums = [1, 2, 2]', output: '[[],[1],[1,2],[1,2,2],[2],[2,2]]' },
      { input: 'nums = [0]', output: '[[],[0]]' },
    ],
    constraints: ['1 <= nums.length <= 10', '-10 <= nums[i] <= 10'],
    starterCode: `function subsetsWithDup(nums) {
  return [];
}`,
    solutionCode: `function subsetsWithDup(nums) {
  const result = [];
  nums.sort((a, b) => a - b);
  function backtrack(start, current) {
    result.push([...current]);
    for (let i = start; i < nums.length; i++) {
      if (i > start && nums[i] === nums[i - 1]) continue;
      current.push(nums[i]);
      backtrack(i + 1, current);
      current.pop();
    }
  }
  backtrack(0, []);
  return result;
}`,
    functionName: 'subsetsWithDup',
    testCases: [
      { id: 1, input: [[1, 2, 2]], expected: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]], inputDisplay: 'nums = [1, 2, 2]', expectedDisplay: '[[],[1],[1,2],[1,2,2],[2],[2,2]]' },
      { id: 2, input: [[0]], expected: [[], [0]], inputDisplay: 'nums = [0]', expectedDisplay: '[[], [0]]' },
      { id: 3, input: [[4, 4, 4]], expected: [[], [4], [4, 4], [4, 4, 4]], inputDisplay: 'nums = [4, 4, 4]', expectedDisplay: '[[], [4], [4, 4], [4, 4, 4]]' },
    ],
    hints: ['Sort the array. Skip elements if nums[i] === nums[i-1] when i > start.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], message: 'Pruning duplicate branches in subset generation' }],
  },
  {
    id: 'word-search',
    wingId: 'backtracking',
    floor: 14,
    title: 'Word Search (Grid Cell Backtracking)',
    difficulty: 'medium',
    visualizerType: 'graph',
    monster: {
      id: 'labyrinth-spider',
      name: 'Arachne the Word Weaver',
      title: 'Trap-Setter of the Rune Matrix',
      maxHp: 3,
      hp: 3,
      sprite: 'spider',
      color: '#eab308',
      attackName: 'Venom Glyph Web',
      attackPower: 2,
      defeatQuote: 'You traced the word through my web without crossing paths...',
    },
    description: `Given an \`m x n\` grid of characters \`board\` and a string \`word\`, return \`true\` if \`word\` exists in the grid. The word can be constructed from letters of sequentially adjacent cells (horizontally or vertically). The same letter cell may not be used more than once.`,
    examples: [
      { input: 'board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"', output: 'true' },
      { input: 'board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"', output: 'true' },
    ],
    constraints: ['m == board.length, n = board[i].length', '1 <= m, n <= 6', '1 <= word.length <= 15'],
    starterCode: `function exist(board, word) {
  return false;
}`,
    solutionCode: `function exist(board, word) {
  const m = board.length;
  const n = board[0].length;
  function dfs(r, c, idx) {
    if (idx === word.length) return true;
    if (r < 0 || r >= m || c < 0 || c >= n || board[r][c] !== word[idx]) return false;
    const temp = board[r][c];
    board[r][c] = '#';
    const found = dfs(r + 1, c, idx + 1) ||
                  dfs(r - 1, c, idx + 1) ||
                  dfs(r, c + 1, idx + 1) ||
                  dfs(r, c - 1, idx + 1);
    board[r][c] = temp;
    return found;
  }
  for (let r = 0; r < m; r++) {
    for (let c = 0; c < n; c++) {
      if (dfs(r, c, 0)) return true;
    }
  }
  return false;
}`,
    functionName: 'exist',
    testCases: [
      { id: 1, input: [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"], expected: true, inputDisplay: 'board = 3x4, word = "ABCCED"', expectedDisplay: 'true' },
      { id: 2, input: [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"], expected: true, inputDisplay: 'board = 3x4, word = "SEE"', expectedDisplay: 'true' },
      { id: 3, input: [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"], expected: false, inputDisplay: 'board = 3x4, word = "ABCB"', expectedDisplay: 'false' },
    ],
    hints: ['Temporarily mark visited cells with "#" during recursion and restore on backtrack.'],
    generateDefaultFrames: (tc) => [{ type: 'graph', nodes: [], edges: [], message: `Searching for "${tc.input[1]}" in grid with 4-directional DFS` }],
  },

  // 🔴 HARD (3 Problems - Boss Candidates)
  {
    id: 'n-queens',
    wingId: 'backtracking',
    floor: 15,
    title: 'Boss Chamber: N-Queens (Diagonal Conflict Bit-Tracking)',
    difficulty: 'hard',
    visualizerType: 'array',
    monster: {
      id: 'queen-dragon',
      name: 'Tiamat the Chess Sovereign',
      title: 'Empress of the 8-Directional Diagonal',
      maxHp: 4,
      hp: 4,
      sprite: 'dragon',
      color: '#dc2626',
      attackName: 'Checkmate Breath',
      attackPower: 3,
      defeatQuote: 'All N queens peacefully ruled their diagonals... Checkmate.',
    },
    description: `The n-queens puzzle is the problem of placing \`n\` queens on an \`n x n\` chessboard such that no two queens attack each other.

Given an integer \`n\`, return all distinct solutions to the n-queens puzzle. You may return the answer in any order. Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space.`,
    examples: [
      { input: 'n = 4', output: '[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]' },
      { input: 'n = 1', output: '[["Q"]]' },
    ],
    constraints: ['1 <= n <= 9'],
    starterCode: `function solveNQueens(n) {
  return [];
}`,
    solutionCode: `function solveNQueens(n) {
  const result = [];
  const cols = new Set();
  const diag1 = new Set(); // r - c
  const diag2 = new Set(); // r + c
  const board = Array.from({ length: n }, () => Array(n).fill('.'));

  function backtrack(row) {
    if (row === n) {
      result.push(board.map((r) => r.join('')));
      return;
    }
    for (let col = 0; col < n; col++) {
      if (cols.has(col) || diag1.has(row - col) || diag2.has(row + col)) continue;
      cols.add(col);
      diag1.add(row - col);
      diag2.add(row + col);
      board[row][col] = 'Q';
      backtrack(row + 1);
      board[row][col] = '.';
      cols.delete(col);
      diag1.delete(row - col);
      diag2.delete(row + col);
    }
  }
  backtrack(0);
  return result;
}`,
    functionName: 'solveNQueens',
    testCases: [
      { id: 1, input: [4], expected: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]], inputDisplay: 'n = 4', expectedDisplay: '2 solutions found' },
      { id: 2, input: [1], expected: [["Q"]], inputDisplay: 'n = 1', expectedDisplay: '[["Q"]]' },
      { id: 3, input: [2], expected: [], inputDisplay: 'n = 2', expectedDisplay: '[] (impossible)' },
    ],
    hints: ['Maintain sets for occupied columns, positive diagonals (r + c), and negative diagonals (r - c).'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: [tc.input[0]], message: `Solving N-Queens for N = ${tc.input[0]} with diagonal pruning` }],
  },
  {
    id: 'n-queens-ii',
    wingId: 'backtracking',
    floor: 16,
    title: 'Boss Chamber: N-Queens II (Solution Count Optimizer)',
    difficulty: 'hard',
    visualizerType: 'array',
    monster: {
      id: 'grandmaster-lich',
      name: 'Mortis the Grandmaster',
      title: 'Arch-Lich of Combinatorial Checkmates',
      maxHp: 4,
      hp: 4,
      sprite: 'lich',
      color: '#9333ea',
      attackName: 'Perpetual Diagonal Ray',
      attackPower: 3,
      defeatQuote: 'The total solution tally dispelled my curse...',
    },
    description: `The n-queens puzzle is the problem of placing \`n\` queens on an \`n x n\` chessboard such that no two queens attack each other.

Given an integer \`n\`, return the number of distinct solutions to the n-queens puzzle.`,
    examples: [
      { input: 'n = 4', output: '2' },
      { input: 'n = 1', output: '1' },
    ],
    constraints: ['1 <= n <= 9'],
    starterCode: `function totalNQueens(n) {
  return 0;
}`,
    solutionCode: `function totalNQueens(n) {
  let count = 0;
  const cols = new Set();
  const diag1 = new Set();
  const diag2 = new Set();

  function backtrack(row) {
    if (row === n) {
      count++;
      return;
    }
    for (let col = 0; col < n; col++) {
      if (cols.has(col) || diag1.has(row - col) || diag2.has(row + col)) continue;
      cols.add(col);
      diag1.add(row - col);
      diag2.add(row + col);
      backtrack(row + 1);
      cols.delete(col);
      diag1.delete(row - col);
      diag2.delete(row + col);
    }
  }
  backtrack(0);
  return count;
}`,
    functionName: 'totalNQueens',
    testCases: [
      { id: 1, input: [4], expected: 2, inputDisplay: 'n = 4', expectedDisplay: '2' },
      { id: 2, input: [1], expected: 1, inputDisplay: 'n = 1', expectedDisplay: '1' },
      { id: 3, input: [5], expected: 10, inputDisplay: 'n = 5', expectedDisplay: '10' },
    ],
    hints: ['Count valid full placements at row === n instead of building string boards.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: [tc.input[0]], message: `Counting valid N-Queens configurations for N = ${tc.input[0]}` }],
  },
  {
    id: 'sudoku-solver',
    wingId: 'backtracking',
    floor: 17,
    title: 'Boss Chamber: Sudoku Solver (Row/Col/Box Exhaustive Search)',
    difficulty: 'hard',
    visualizerType: 'graph',
    monster: {
      id: 'puzzle-titan',
      name: 'Runic-Titan of the 9x9 Seal',
      title: 'Architect of Inviolable Matrices',
      maxHp: 4,
      hp: 4,
      sprite: 'golem',
      color: '#eab308',
      attackName: 'Matrix Lock Pulse',
      attackPower: 3,
      defeatQuote: 'The 9x9 seal resolved with pristine mathematical harmony...',
    },
    description: `Write a program to solve a Sudoku puzzle by filling the empty cells. A sudoku solution must satisfy: each of the digits 1-9 must occur exactly once in each row, column, and 3x3 sub-box. Return the solved board.`,
    examples: [
      { input: 'Standard 9x9 board with valid solution', output: 'Fully filled 9x9 board' },
    ],
    constraints: ['board.length == 9, board[i].length == 9', 'Each board contains only digits 1-9 and "."'],
    starterCode: `function solveSudoku(board) {
  return board;
}`,
    solutionCode: `function solveSudoku(board) {
  function isValid(r, c, ch) {
    for (let i = 0; i < 9; i++) {
      if (board[r][i] === ch) return false;
      if (board[i][c] === ch) return false;
      const boxR = 3 * Math.floor(r / 3) + Math.floor(i / 3);
      const boxC = 3 * Math.floor(c / 3) + (i % 3);
      if (board[boxR][boxC] === ch) return false;
    }
    return true;
  }
  function solve() {
    for (let r = 0; r < 9; r++) {
      for (let c = 0; c < 9; c++) {
        if (board[r][c] === '.') {
          for (let d = 1; d <= 9; d++) {
            const ch = String(d);
            if (isValid(r, c, ch)) {
              board[r][c] = ch;
              if (solve()) return true;
              board[r][c] = '.';
            }
          }
          return false;
        }
      }
    }
    return true;
  }
  solve();
  return board;
}`,
    functionName: 'solveSudoku',
    testCases: [
      {
        id: 1,
        input: [[
          ["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]
        ]],
        expected: [
          ["5","3","4","6","7","8","9","1","2"],
          ["6","7","2","1","9","5","3","4","8"],
          ["1","9","8","3","4","2","5","6","7"],
          ["8","5","9","7","6","1","4","2","3"],
          ["4","2","6","8","5","3","7","9","1"],
          ["7","1","3","9","2","4","8","5","6"],
          ["9","6","1","5","3","7","2","8","4"],
          ["2","8","7","4","1","9","6","3","5"],
          ["3","4","5","2","8","6","1","7","9"]
        ],
        inputDisplay: 'board = standard 9x9 Sudoku',
        expectedDisplay: 'Complete 9x9 solved matrix',
      },
      {
        id: 2,
        input: [[
          ["1",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."],
          [".",".",".",".",".",".",".",".","."]
        ]],
        expected: [
          ["1","2","3","4","5","6","7","8","9"],
          ["4","5","6","7","8","9","1","2","3"],
          ["7","8","9","1","2","3","4","5","6"],
          ["2","1","4","3","6","5","8","9","7"],
          ["3","6","5","8","9","7","2","1","4"],
          ["8","9","7","2","1","4","3","6","5"],
          ["5","3","1","6","4","2","9","7","8"],
          ["6","4","2","9","7","8","5","3","1"],
          ["9","7","8","5","3","1","6","4","2"]
        ],
        inputDisplay: 'board with top-left "1"',
        expectedDisplay: 'Complete valid solved matrix',
      },
    ],
    hints: ['Check row, column, and 3x3 block constraints before placing each digit.'],
    generateDefaultFrames: (tc) => [{ type: 'graph', nodes: [], edges: [], message: 'Backtracking 9x9 Sudoku grid cells' }],
  },
];
