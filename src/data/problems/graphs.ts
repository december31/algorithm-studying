import { Problem } from '../../types/problem';
import { GraphFrame, ArrayFrame } from '../../types/visualizer';

export const graphProblems: Problem[] = [
  // 🟢 EASY (6 Problems)
  {
    id: 'flood-fill',
    wingId: 'graphs',
    floor: 1,
    title: 'Flood Fill (Pixel Coordinate Traversal)',
    difficulty: 'easy',
    visualizerType: 'graph',
    monster: {
      id: 'venom-spider',
      name: 'Venomfang the Broodmother',
      title: 'Matriarch of the Webbed Chamber',
      maxHp: 3,
      hp: 3,
      sprite: 'spider',
      color: '#10b981',
      attackName: 'Neurotoxic Webbing',
      attackPower: 1,
      defeatQuote: 'The flood of color dissolved my silken domain...',
    },
    description: `An image is represented by an \`m x n\` integer grid \`image\` where \`image[i][j]\` represents the pixel value. You are also given three integers \`sr\`, \`sc\`, and \`color\`. You should perform a flood fill on the image starting from the pixel \`image[sr][sc]\`.`,
    examples: [
      { input: 'image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2', output: '[[2,2,2],[2,2,0],[2,0,1]]' },
      { input: 'image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0', output: '[[0,0,0],[0,0,0]]' },
    ],
    constraints: ['m == image.length, n == image[i].length', '1 <= m, n <= 50', '0 <= color < 2^16'],
    starterCode: `function floodFill(image, sr, sc, color) {
  return image;
}`,
    solutionCode: `function floodFill(image, sr, sc, color) {
  const orig = image[sr][sc];
  if (orig === color) return image;
  const m = image.length, n = image[0].length;
  function dfs(r, c) {
    if (r < 0 || r >= m || c < 0 || c >= n || image[r][c] !== orig) return;
    image[r][c] = color;
    dfs(r + 1, c);
    dfs(r - 1, c);
    dfs(r, c + 1);
    dfs(r, c - 1);
  }
  dfs(sr, sc);
  return image;
}`,
    functionName: 'floodFill',
    testCases: [
      { id: 1, input: [[[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2], expected: [[2, 2, 2], [2, 2, 0], [2, 0, 1]], inputDisplay: 'image = 3x3, sr = 1, sc = 1, color = 2', expectedDisplay: '[[2,2,2],[2,2,0],[2,0,1]]' },
      { id: 2, input: [[[0, 0, 0], [0, 0, 0]], 0, 0, 0], expected: [[0, 0, 0], [0, 0, 0]], inputDisplay: 'image = 2x3 all 0, color = 0', expectedDisplay: '[[0,0,0],[0,0,0]]' },
      { id: 3, input: [[[0, 0, 0], [0, 1, 1]], 1, 1, 1], expected: [[0, 0, 0], [0, 1, 1]], inputDisplay: 'image = 2x3, color same', expectedDisplay: '[[0,0,0],[0,1,1]]' },
    ],
    hints: ['Save the original starting color. If it matches target color, return immediately. Otherwise DFS 4 directions.'],
    generateDefaultFrames: (tc) => [{ type: 'graph', nodes: [], edges: [], message: 'Flood filling 4-directionally from start coordinate' }],
  },
  {
    id: 'island-perimeter',
    wingId: 'graphs',
    floor: 2,
    title: 'Island Perimeter (Grid Edge Inspection)',
    difficulty: 'easy',
    visualizerType: 'graph',
    monster: {
      id: 'reef-slime',
      name: 'Coralis the Reef Slime',
      title: 'Scout of the Shoreline Boundary',
      maxHp: 3,
      hp: 3,
      sprite: 'slime',
      color: '#38bdf8',
      attackName: 'Tidal Splash',
      attackPower: 1,
      defeatQuote: 'My perimeter boundaries were surveyed completely...',
    },
    description: `You are given \`row x col\` \`grid\` representing a map where \`grid[i][j] = 1\` represents land and \`grid[i][j] = 0\` represents water.

Grid cells are connected horizontally/vertically. Determine the perimeter of the island.`,
    examples: [
      { input: 'grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]', output: '16' },
      { input: 'grid = [[1]]', output: '4' },
      { input: 'grid = [[1,0]]', output: '4' },
    ],
    constraints: ['row == grid.length, col == grid[i].length', '1 <= row, col <= 100', 'grid[i][j] is 0 or 1'],
    starterCode: `function islandPerimeter(grid) {
  return 0;
}`,
    solutionCode: `function islandPerimeter(grid) {
  const m = grid.length, n = grid[0].length;
  let perimeter = 0;
  for (let r = 0; r < m; r++) {
    for (let c = 0; c < n; c++) {
      if (grid[r][c] === 1) {
        perimeter += 4;
        if (r > 0 && grid[r - 1][c] === 1) perimeter -= 2;
        if (c > 0 && grid[r][c - 1] === 1) perimeter -= 2;
      }
    }
  }
  return perimeter;
}`,
    functionName: 'islandPerimeter',
    testCases: [
      { id: 1, input: [[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]], expected: 16, inputDisplay: 'grid = 4x4 island', expectedDisplay: '16' },
      { id: 2, input: [[[1]]], expected: 4, inputDisplay: 'grid = [[1]]', expectedDisplay: '4' },
      { id: 3, input: [[[1, 0]]], expected: 4, inputDisplay: 'grid = [[1, 0]]', expectedDisplay: '4' },
    ],
    hints: ['Each land cell adds 4 edges. Subtract 2 for every adjacent neighbor (top and left).'],
    generateDefaultFrames: (tc) => [{ type: 'graph', nodes: [], edges: [], message: 'Scanning grid to calculate perimeter border edges' }],
  },
  {
    id: 'find-if-path-exists-in-graph',
    wingId: 'graphs',
    floor: 3,
    title: 'Find if Path Exists in Graph (BFS / DFS)',
    difficulty: 'easy',
    visualizerType: 'graph',
    monster: {
      id: 'bridge-gargoyle',
      name: 'Vael the Gate Gargoyle',
      title: 'Warden of the Connected Ruins',
      maxHp: 3,
      hp: 3,
      sprite: 'gargoyle',
      color: '#64748b',
      attackName: 'Chasm Stun',
      attackPower: 1,
      defeatQuote: 'A valid path was charted through my ruins...',
    },
    description: `There is a bi-directional graph with \`n\` vertices. Given the edges and source, destination vertices, determine if there is a valid path that exists from \`source\` to \`destination\`.`,
    examples: [
      { input: 'n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2', output: 'true' },
      { input: 'n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5', output: 'false' },
    ],
    constraints: ['1 <= n <= 2 * 10^5', '0 <= edges.length <= 2 * 10^5', '0 <= source, destination < n'],
    starterCode: `function validPath(n, edges, source, destination) {
  return false;
}`,
    solutionCode: `function validPath(n, edges, source, destination) {
  if (source === destination) return true;
  const adj = Array.from({ length: n }, () => []);
  for (const [u, v] of edges) {
    adj[u].push(v);
    adj[v].push(u);
  }
  const visited = new Set([source]);
  const queue = [source];
  while (queue.length > 0) {
    const node = queue.shift();
    if (node === destination) return true;
    for (const neighbor of adj[node]) {
      if (!visited.has(neighbor)) {
        visited.add(neighbor);
        queue.push(neighbor);
      }
    }
  }
  return false;
}`,
    functionName: 'validPath',
    testCases: [
      { id: 1, input: [3, [[0, 1], [1, 2], [2, 0]], 0, 2], expected: true, inputDisplay: 'n = 3, edges = 3, 0 -> 2', expectedDisplay: 'true' },
      { id: 2, input: [6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5], expected: false, inputDisplay: 'n = 6, disconnected components, 0 -> 5', expectedDisplay: 'false' },
      { id: 3, input: [1, [], 0, 0], expected: true, inputDisplay: 'n = 1, single node, 0 -> 0', expectedDisplay: 'true' },
    ],
    hints: ['Build an adjacency list and run BFS with a visited Set starting from source.'],
    generateDefaultFrames: (tc) => [{ type: 'graph', nodes: [], edges: [], message: `Exploring graph BFS from node ${tc.input[2]} to ${tc.input[3]}` }],
  },
  {
    id: 'average-of-levels-in-binary-tree',
    wingId: 'graphs',
    floor: 4,
    title: 'Average of Levels in Binary Tree (Level-Order BFS)',
    difficulty: 'easy',
    visualizerType: 'tree',
    monster: {
      id: 'mean-specter',
      name: 'Equus the Average Specter',
      title: 'Tallyman of Tree Layers',
      maxHp: 3,
      hp: 3,
      sprite: 'wraith',
      color: '#a855f7',
      attackName: 'Layered Drain',
      attackPower: 1,
      defeatQuote: 'Each level of my spectral tree was averaged...',
    },
    description: `Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.`,
    examples: [
      { input: 'root = [3, 9, 20, null, null, 15, 7]', output: '[3, 14.5, 11]' },
      { input: 'root = [3, 9, 20, 15, 7]', output: '[3, 14.5, 11]' },
    ],
    constraints: ['The number of nodes in the tree is in the range [1, 10^4].'],
    starterCode: `function averageOfLevels(root) {
  return [];
}`,
    solutionCode: `function averageOfLevels(root) {
  if (!root || root.length === 0 || root[0] === null) return [];
  const result = [];
  const queue = [0]; // indices
  while (queue.length > 0) {
    const size = queue.length;
    let sum = 0;
    for (let i = 0; i < size; i++) {
      const idx = queue.shift();
      sum += root[idx];
      const left = 2 * idx + 1;
      const right = 2 * idx + 2;
      if (left < root.length && root[left] !== null && root[left] !== undefined) queue.push(left);
      if (right < root.length && root[right] !== null && root[right] !== undefined) queue.push(right);
    }
    result.push(Number((sum / size).toFixed(5)));
  }
  return result;
}`,
    functionName: 'averageOfLevels',
    testCases: [
      { id: 1, input: [[3, 9, 20, null, null, 15, 7]], expected: [3, 14.5, 11], inputDisplay: 'root = [3, 9, 20, null, null, 15, 7]', expectedDisplay: '[3, 14.5, 11]' },
      { id: 2, input: [[1, 2, 3]], expected: [1, 2.5], inputDisplay: 'root = [1, 2, 3]', expectedDisplay: '[1, 2.5]' },
      { id: 3, input: [[5]], expected: [5], inputDisplay: 'root = [5]', expectedDisplay: '[5]' },
    ],
    hints: ['Use standard queue BFS: loop over queue.length to process one level at a time.'],
    generateDefaultFrames: (tc) => [{ type: 'tree', nodes: [], rootId: '0', message: 'Computing level-by-level average with BFS queue' }],
  },
  {
    id: 'univalued-binary-tree',
    wingId: 'graphs',
    floor: 5,
    title: 'Univalued Binary Tree (Uniform Property DFS)',
    difficulty: 'easy',
    visualizerType: 'tree',
    monster: {
      id: 'mono-slime',
      name: 'Unus the Pure Slime',
      title: 'Embodiment of Single-Valued Essence',
      maxHp: 3,
      hp: 3,
      sprite: 'slime',
      color: '#22c55e',
      attackName: 'Uniform Ooze Surge',
      attackPower: 1,
      defeatQuote: 'The uniform essence was confirmed...',
    },
    description: `A binary tree is uni-valued if every node in the tree has the same value. Given the root of a binary tree, return \`true\` if the given tree is uni-valued, or \`false\` otherwise.`,
    examples: [
      { input: 'root = [1, 1, 1, 1, 1, null, 1]', output: 'true' },
      { input: 'root = [2, 2, 2, 5, 2]', output: 'false' },
    ],
    constraints: ['The number of nodes in the tree is in the range [1, 100].'],
    starterCode: `function isUnivalTree(root) {
  return true;
}`,
    solutionCode: `function isUnivalTree(root) {
  if (!root || root.length === 0 || root[0] === null) return true;
  const val = root[0];
  for (let i = 0; i < root.length; i++) {
    if (root[i] !== null && root[i] !== undefined && root[i] !== val) return false;
  }
  return true;
}`,
    functionName: 'isUnivalTree',
    testCases: [
      { id: 1, input: [[1, 1, 1, 1, 1, null, 1]], expected: true, inputDisplay: 'root = [1, 1, 1, 1, 1, null, 1]', expectedDisplay: 'true' },
      { id: 2, input: [[2, 2, 2, 5, 2]], expected: false, inputDisplay: 'root = [2, 2, 2, 5, 2]', expectedDisplay: 'false' },
      { id: 3, input: [[9]], expected: true, inputDisplay: 'root = [9]', expectedDisplay: 'true' },
    ],
    hints: ['Check that every non-null node matches the root value.'],
    generateDefaultFrames: (tc) => [{ type: 'tree', nodes: [], rootId: '0', message: 'Checking uniformity against root value' }],
  },
  {
    id: 'cousins-in-binary-tree',
    wingId: 'graphs',
    floor: 6,
    title: 'Cousins in Binary Tree (Depth & Parent Scan)',
    difficulty: 'easy',
    visualizerType: 'tree',
    monster: {
      id: 'kin-skeleton',
      name: 'Kin the Linked Skeleton',
      title: 'Tracker of Tree Lineages',
      maxHp: 3,
      hp: 3,
      sprite: 'skeleton',
      color: '#e2e8f0',
      attackName: 'Bone Relic Pierce',
      attackPower: 1,
      defeatQuote: 'Different parents, same depth confirmed...',
    },
    description: `In a binary tree, the root node is at depth 0. Two nodes of a binary tree are cousins if they have the same depth with different parents. Return \`true\` if \`x\` and \`y\` are cousins.`,
    examples: [
      { input: 'root = [1, 2, 3, 4], x = 4, y = 3', output: 'false' },
      { input: 'root = [1, 2, 3, null, 4, null, 5], x = 5, y = 4', output: 'true' },
    ],
    constraints: ['The number of nodes in the tree will be between 2 and 100.'],
    starterCode: `function isCousins(root, x, y) {
  return false;
}`,
    solutionCode: `function isCousins(root, x, y) {
  let xInfo = null, yInfo = null;
  function dfs(idx, depth, parent) {
    if (idx >= root.length || root[idx] === null || root[idx] === undefined) return;
    const val = root[idx];
    if (val === x) xInfo = { depth, parent };
    if (val === y) yInfo = { depth, parent };
    dfs(2 * idx + 1, depth + 1, val);
    dfs(2 * idx + 2, depth + 1, val);
  }
  dfs(0, 0, null);
  return xInfo && yInfo && xInfo.depth === yInfo.depth && xInfo.parent !== yInfo.parent;
}`,
    functionName: 'isCousins',
    testCases: [
      { id: 1, input: [[1, 2, 3, 4], 4, 3], expected: false, inputDisplay: 'root = [1, 2, 3, 4], x = 4, y = 3', expectedDisplay: 'false' },
      { id: 2, input: [[1, 2, 3, null, 4, null, 5], 5, 4], expected: true, inputDisplay: 'root = [1,2,3,null,4,null,5], x = 5, y = 4', expectedDisplay: 'true' },
      { id: 3, input: [[1, 2, 3, null, 4], 2, 3], expected: false, inputDisplay: 'x = 2, y = 3 (siblings)', expectedDisplay: 'false' },
    ],
    hints: ['Record the depth and parent of both target nodes via DFS, then compare.'],
    generateDefaultFrames: (tc) => [{ type: 'tree', nodes: [], rootId: '0', message: `Tracking depth and parent for ${tc.input[1]} and ${tc.input[2]}` }],
  },

  // 🟡 MEDIUM (6 Problems)
  {
    id: 'number-of-islands',
    wingId: 'graphs',
    floor: 7,
    title: 'Number of Islands (Connected Components)',
    difficulty: 'medium',
    visualizerType: 'graph',
    monster: {
      id: 'archipelago-beast',
      name: 'Charybdis the Island Lurker',
      title: 'Terror of the Flooded Archipelagos',
      maxHp: 3,
      hp: 3,
      sprite: 'dragon',
      color: '#0284c7',
      attackName: 'Tidal Landmass Rupture',
      attackPower: 2,
      defeatQuote: 'All my islands were sunken into single components...',
    },
    description: `Given an \`m x n\` 2D binary grid \`grid\` which represents a map of '1's (land) and '0's (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.`,
    examples: [
      { input: 'grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]', output: '1' },
      { input: 'grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]', output: '3' },
    ],
    constraints: ['m == grid.length, n == grid[i].length', '1 <= m, n <= 300', 'grid[i][j] is \'0\' or \'1\'.'],
    starterCode: `function numIslands(grid) {
  return 0;
}`,
    solutionCode: `function numIslands(grid) {
  if (!grid || grid.length === 0) return 0;
  const m = grid.length, n = grid[0].length;
  let count = 0;
  function sink(r, c) {
    if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] === '0') return;
    grid[r][c] = '0';
    sink(r + 1, c);
    sink(r - 1, c);
    sink(r, c + 1);
    sink(r, c - 1);
  }
  for (let r = 0; r < m; r++) {
    for (let c = 0; c < n; c++) {
      if (grid[r][c] === '1') {
        count++;
        sink(r, c);
      }
    }
  }
  return count;
}`,
    functionName: 'numIslands',
    testCases: [
      { id: 1, input: [[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]], expected: 1, inputDisplay: 'grid = 4x5, 1 large island', expectedDisplay: '1' },
      { id: 2, input: [[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]], expected: 3, inputDisplay: 'grid = 4x5, 3 islands', expectedDisplay: '3' },
      { id: 3, input: [[["0","0"],["0","0"]]], expected: 0, inputDisplay: 'grid = 2x2 all water', expectedDisplay: '0' },
    ],
    hints: ['Iterate through cells. When finding "1", increment count and sink all adjacent connected "1"s.'],
    generateDefaultFrames: (tc) => [{ type: 'graph', nodes: [], edges: [], message: 'Exploring connected land components via DFS flood fill' }],
  },
  {
    id: 'rotting-oranges',
    wingId: 'graphs',
    floor: 8,
    title: 'Rotting Oranges (Multi-Source BFS)',
    difficulty: 'medium',
    visualizerType: 'graph',
    monster: {
      id: 'blight-treant',
      name: 'Putrid the Blight Treant',
      title: 'Spreader of Citrus Decay',
      maxHp: 3,
      hp: 3,
      sprite: 'treant',
      color: '#f97316',
      attackName: 'Spore Contagion Blast',
      attackPower: 2,
      defeatQuote: 'The infection wavefront was halted...',
    },
    description: `You are given an \`m x n\` grid where each cell can have one of three values: 0 = empty, 1 = fresh orange, 2 = rotten orange. Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. Return the minimum number of minutes until no fresh orange remains, or -1 if impossible.`,
    examples: [
      { input: 'grid = [[2,1,1],[1,1,0],[0,1,1]]', output: '4' },
      { input: 'grid = [[2,1,1],[0,1,1],[1,0,1]]', output: '-1' },
      { input: 'grid = [[0,2]]', output: '0' },
    ],
    constraints: ['m == grid.length, n == grid[i].length', '1 <= m, n <= 10', 'grid[i][j] is 0, 1, or 2.'],
    starterCode: `function orangesRotting(grid) {
  return 0;
}`,
    solutionCode: `function orangesRotting(grid) {
  const m = grid.length, n = grid[0].length;
  let fresh = 0;
  const queue = [];
  for (let r = 0; r < m; r++) {
    for (let c = 0; c < n; c++) {
      if (grid[r][c] === 2) queue.push([r, c, 0]);
      else if (grid[r][c] === 1) fresh++;
    }
  }
  let minutes = 0;
  const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
  while (queue.length > 0) {
    const [r, c, time] = queue.shift();
    minutes = Math.max(minutes, time);
    for (const [dr, dc] of dirs) {
      const nr = r + dr, nc = c + dc;
      if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] === 1) {
        grid[nr][nc] = 2;
        fresh--;
        queue.push([nr, nc, time + 1]);
      }
    }
  }
  return fresh === 0 ? minutes : -1;
}`,
    functionName: 'orangesRotting',
    testCases: [
      { id: 1, input: [[[2,1,1],[1,1,0],[0,1,1]]], expected: 4, inputDisplay: 'grid = 3x3 with rotten at (0,0)', expectedDisplay: '4' },
      { id: 2, input: [[[2,1,1],[0,1,1],[1,0,1]]], expected: -1, inputDisplay: 'grid with unreachable fresh orange', expectedDisplay: '-1' },
      { id: 3, input: [[[0,2]]], expected: 0, inputDisplay: 'grid = [[0,2]]', expectedDisplay: '0' },
    ],
    hints: ['Initialize queue with all rotten oranges at time 0 (multi-source BFS).'],
    generateDefaultFrames: (tc) => [{ type: 'graph', nodes: [], edges: [], message: 'Multi-source BFS decay propagation' }],
  },
  {
    id: 'max-area-of-island',
    wingId: 'graphs',
    floor: 9,
    title: 'Max Area of Island (Accumulator Flood Fill)',
    difficulty: 'medium',
    visualizerType: 'graph',
    monster: {
      id: 'landmass-golem',
      name: 'Terran the Continent Golem',
      title: 'Colossus of Maximal Landmass',
      maxHp: 3,
      hp: 3,
      sprite: 'golem',
      color: '#15803d',
      attackName: 'Continental Shrewd',
      attackPower: 2,
      defeatQuote: 'The maximum landmass was conquered...',
    },
    description: `You are given an \`m x n\` binary matrix \`grid\`. An island is a group of '1's connected 4-directionally. The area of an island is the number of cells with a value 1 in the island. Return the maximum area of an island in \`grid\`. If there is no island, return 0.`,
    examples: [
      { input: 'grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],...]', output: '6' },
      { input: 'grid = [[0,0,0,0,0,0,0,0]]', output: '0' },
    ],
    constraints: ['m == grid.length, n == grid[i].length', '1 <= m, n <= 50'],
    starterCode: `function maxAreaOfIsland(grid) {
  return 0;
}`,
    solutionCode: `function maxAreaOfIsland(grid) {
  const m = grid.length, n = grid[0].length;
  let maxArea = 0;
  function dfs(r, c) {
    if (r < 0 || r >= m || c < 0 || c >= n || grid[r][c] === 0) return 0;
    grid[r][c] = 0;
    return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1);
  }
  for (let r = 0; r < m; r++) {
    for (let c = 0; c < n; c++) {
      if (grid[r][c] === 1) {
        maxArea = Math.max(maxArea, dfs(r, c));
      }
    }
  }
  return maxArea;
}`,
    functionName: 'maxAreaOfIsland',
    testCases: [
      { id: 1, input: [[[0,0,1,0],[1,1,1,0],[0,1,0,0]]], expected: 5, inputDisplay: 'grid = 3x4 with island area 5', expectedDisplay: '5' },
      { id: 2, input: [[[0,0,0],[0,0,0]]], expected: 0, inputDisplay: 'grid = all water', expectedDisplay: '0' },
      { id: 3, input: [[[1,1],[1,1]]], expected: 4, inputDisplay: 'grid = 2x2 all land', expectedDisplay: '4' },
    ],
    hints: ['Return 1 + sum of DFS calls on 4 directions to accumulate island size.'],
    generateDefaultFrames: (tc) => [{ type: 'graph', nodes: [], edges: [], message: 'Summing connected cell counts via recursive DFS' }],
  },
  {
    id: 'shortest-path-in-binary-matrix',
    wingId: 'graphs',
    floor: 10,
    title: 'Shortest Path in Binary Matrix (8-Directional BFS)',
    difficulty: 'medium',
    visualizerType: 'graph',
    monster: {
      id: 'abyssal-behemoth',
      name: 'Nihilus the Abyssal Behemoth',
      title: 'Devourer of 8-Directional Space',
      maxHp: 3,
      hp: 3,
      sprite: 'dragon',
      color: '#9333ea',
      attackName: 'Void Singularity Rupture',
      attackPower: 2,
      defeatQuote: 'Your shortest path pierced straight through my event horizon...',
    },
    description: `Given an \`n x n\` binary matrix \`grid\`, return the length of the shortest clear path in the matrix. If there is no clear path, return -1. 8-directionally connected.`,
    examples: [
      { input: 'grid = [[0,1],[1,0]]', output: '2' },
      { input: 'grid = [[0,0,0],[1,1,0],[1,1,0]]', output: '4' },
    ],
    constraints: ['n == grid.length == grid[i].length', '1 <= n <= 100', 'grid[i][j] is 0 or 1'],
    starterCode: `function shortestPathBinaryMatrix(grid) {
  return -1;
}`,
    solutionCode: `function shortestPathBinaryMatrix(grid) {
  const n = grid.length;
  if (grid[0][0] !== 0 || grid[n - 1][n - 1] !== 0) return -1;
  if (n === 1) return 1;
  const dirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]];
  const queue = [[0, 0, 1]];
  grid[0][0] = 1;
  while (queue.length > 0) {
    const [r, c, dist] = queue.shift();
    if (r === n - 1 && c === n - 1) return dist;
    for (const [dr, dc] of dirs) {
      const nr = r + dr, nc = c + dc;
      if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] === 0) {
        grid[nr][nc] = 1;
        queue.push([nr, nc, dist + 1]);
      }
    }
  }
  return -1;
}`,
    functionName: 'shortestPathBinaryMatrix',
    testCases: [
      { id: 1, input: [[[0, 1], [1, 0]]], expected: 2, inputDisplay: 'grid = [[0,1],[1,0]]', expectedDisplay: '2' },
      { id: 2, input: [[[0,0,0],[1,1,0],[1,1,0]]], expected: 4, inputDisplay: 'grid = 3x3 path around obstacles', expectedDisplay: '4' },
      { id: 3, input: [[[1,0],[0,0]]], expected: -1, inputDisplay: 'start blocked grid', expectedDisplay: '-1' },
    ],
    hints: ['BFS guaranteed to find shortest path. Explore all 8 adjacent neighbors.'],
    generateDefaultFrames: (tc) => [{ type: 'graph', nodes: [], edges: [], message: '8-directional BFS path routing' }],
  },
  {
    id: 'course-schedule',
    wingId: 'graphs',
    floor: 11,
    title: 'Course Schedule (Cycle Detection / Topological Sort)',
    difficulty: 'medium',
    visualizerType: 'graph',
    monster: {
      id: 'chrono-lich',
      name: 'Chronos the Cycle Necromancer',
      title: 'Weaver of Endless Prerequisite Loops',
      maxHp: 3,
      hp: 3,
      sprite: 'lich',
      color: '#e11d48',
      attackName: 'Temporal Loop Curse',
      attackPower: 2,
      defeatQuote: 'The DAG was resolved without cycle loops...',
    },
    description: `There are a total of \`numCourses\` courses you have to take, labeled from 0 to \`numCourses - 1\`. You are given an array \`prerequisites\` where \`prerequisites[i] = [a, b]\` indicates that you must take \`b\` first if you want to take \`a\`. Return \`true\` if you can finish all courses, or \`false\` otherwise.`,
    examples: [
      { input: 'numCourses = 2, prerequisites = [[1,0]]', output: 'true' },
      { input: 'numCourses = 2, prerequisites = [[1,0],[0,1]]', output: 'false' },
    ],
    constraints: ['1 <= numCourses <= 2000', '0 <= prerequisites.length <= 5000'],
    starterCode: `function canFinish(numCourses, prerequisites) {
  return true;
}`,
    solutionCode: `function canFinish(numCourses, prerequisites) {
  const inDegree = new Array(numCourses).fill(0);
  const adj = Array.from({ length: numCourses }, () => []);
  for (const [course, pre] of prerequisites) {
    adj[pre].push(course);
    inDegree[course]++;
  }
  const queue = [];
  for (let i = 0; i < numCourses; i++) {
    if (inDegree[i] === 0) queue.push(i);
  }
  let count = 0;
  while (queue.length > 0) {
    const curr = queue.shift();
    count++;
    for (const next of adj[curr]) {
      inDegree[next]--;
      if (inDegree[next] === 0) queue.push(next);
    }
  }
  return count === numCourses;
}`,
    functionName: 'canFinish',
    testCases: [
      { id: 1, input: [2, [[1, 0]]], expected: true, inputDisplay: '2 courses, 1 -> 0', expectedDisplay: 'true' },
      { id: 2, input: [2, [[1, 0], [0, 1]]], expected: false, inputDisplay: '2 courses, mutual cycle', expectedDisplay: 'false' },
      { id: 3, input: [3, [[0, 1], [0, 2], [1, 2]]], expected: true, inputDisplay: '3 courses DAG', expectedDisplay: 'true' },
    ],
    hints: ['Kahn\'s algorithm: maintain in-degrees of each course, enqueue 0-indegree nodes.'],
    generateDefaultFrames: (tc) => [{ type: 'graph', nodes: [], edges: [], message: 'Topological sort via in-degree queue BFS' }],
  },
  {
    id: 'clone-graph',
    wingId: 'graphs',
    floor: 12,
    title: 'Clone Graph (Deep Copy via Map)',
    difficulty: 'medium',
    visualizerType: 'graph',
    monster: {
      id: 'mirror-shade',
      name: 'Spectro the Duplicate Wraith',
      title: 'Cloner of Interconnected Souls',
      maxHp: 3,
      hp: 3,
      sprite: 'wraith',
      color: '#6366f1',
      attackName: 'Spectral Duplicate Shock',
      attackPower: 2,
      defeatQuote: 'The graph replica mirrored every edge flawlessly...',
    },
    description: `Given a representation of an undirected graph as an adjacency list \`adjList\`, return a deep copy (clone) of the adjacency list.`,
    examples: [
      { input: 'adjList = [[2,4],[1,3],[2,4],[1,3]]', output: '[[2,4],[1,3],[2,4],[1,3]]' },
      { input: 'adjList = [[]]', output: '[[]]' },
    ],
    constraints: ['The number of nodes in the graph is in the range [0, 100].'],
    starterCode: `function cloneGraph(adjList) {
  return adjList;
}`,
    solutionCode: `function cloneGraph(adjList) {
  if (!adjList || adjList.length === 0) return [];
  return adjList.map((neighbors) => [...neighbors]);
}`,
    functionName: 'cloneGraph',
    testCases: [
      { id: 1, input: [[[2,4],[1,3],[2,4],[1,3]]], expected: [[2,4],[1,3],[2,4],[1,3]], inputDisplay: 'adjList = 4 nodes cycle', expectedDisplay: '[[2,4],[1,3],[2,4],[1,3]]' },
      { id: 2, input: [[[]]], expected: [[]], inputDisplay: 'adjList = [[]]', expectedDisplay: '[[]]' },
      { id: 3, input: [[]], expected: [], inputDisplay: 'adjList = []', expectedDisplay: '[]' },
    ],
    hints: ['Use a Map to store oldNode -> newNode mappings to avoid cloning nodes multiple times.'],
    generateDefaultFrames: (tc) => [{ type: 'graph', nodes: [], edges: [], message: 'Cloning graph topology and neighbor lists' }],
  },

  // 🔴 HARD (3 Problems - Boss Candidates)
  {
    id: 'word-ladder',
    wingId: 'graphs',
    floor: 13,
    title: 'Boss Chamber: Word Ladder (Shortest Path Transformation)',
    difficulty: 'hard',
    visualizerType: 'graph',
    monster: {
      id: 'lexicon-dragon',
      name: 'Verbis the Word Serpent',
      title: 'Devourer of Orthographic Mutations',
      maxHp: 4,
      hp: 4,
      sprite: 'dragon',
      color: '#dc2626',
      attackName: 'Morphological Inferno',
      attackPower: 3,
      defeatQuote: 'Your shortest transformation sequence pierced my vocabulary...',
    },
    description: `A transformation sequence from \`beginWord\` to \`endWord\` using a dictionary \`wordList\` is a sequence of words where every adjacent pair differs by a single letter. Return the number of words in the shortest transformation sequence from \`beginWord\` to \`endWord\`, or 0 if no such sequence exists.`,
    examples: [
      { input: 'beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]', output: '5' },
      { input: 'beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]', output: '0' },
    ],
    constraints: ['1 <= beginWord.length <= 10', '1 <= wordList.length <= 5000'],
    starterCode: `function ladderLength(beginWord, endWord, wordList) {
  return 0;
}`,
    solutionCode: `function ladderLength(beginWord, endWord, wordList) {
  const words = new Set(wordList);
  if (!words.has(endWord)) return 0;
  const queue = [[beginWord, 1]];
  const visited = new Set([beginWord]);

  while (queue.length > 0) {
    const [curr, level] = queue.shift();
    if (curr === endWord) return level;
    for (let i = 0; i < curr.length; i++) {
      for (let c = 97; c <= 122; c++) {
        const next = curr.slice(0, i) + String.fromCharCode(c) + curr.slice(i + 1);
        if (words.has(next) && !visited.has(next)) {
          visited.add(next);
          queue.push([next, level + 1]);
        }
      }
    }
  }
  return 0;
}`,
    functionName: 'ladderLength',
    testCases: [
      { id: 1, input: ["hit", "cog", ["hot","dot","dog","lot","log","cog"]], expected: 5, inputDisplay: 'hit -> cog via 6 words', expectedDisplay: '5' },
      { id: 2, input: ["hit", "cog", ["hot","dot","dog","lot","log"]], expected: 0, inputDisplay: 'endWord not in wordList', expectedDisplay: '0' },
      { id: 3, input: ["a", "c", ["a", "b", "c"]], expected: 2, inputDisplay: 'a -> c', expectedDisplay: '2' },
    ],
    hints: ['Treat words as nodes and 1-letter differences as edges. BFS finds shortest path.'],
    generateDefaultFrames: (tc) => [{ type: 'graph', nodes: [], edges: [], message: `Transforming "${tc.input[0]}" to "${tc.input[1]}" via BFS` }],
  },
  {
    id: 'making-a-large-island',
    wingId: 'graphs',
    floor: 14,
    title: 'Boss Chamber: Making A Large Island (Component Expansion)',
    difficulty: 'hard',
    visualizerType: 'graph',
    monster: {
      id: 'gargoyle-king',
      name: 'Malakor the Continental King',
      title: 'Fusioner of Shattered Landmasses',
      maxHp: 4,
      hp: 4,
      sprite: 'gargoyle',
      color: '#eab308',
      attackName: 'Tectonic Fusion Quake',
      attackPower: 3,
      defeatQuote: 'Changing one single tile united an unstoppable landmass...',
    },
    description: `You are given an \`n x n\` binary matrix grid. You are allowed to change at most one 0 to be 1. Return the size of the largest island in grid after applying this operation.`,
    examples: [
      { input: 'grid = [[1,0],[0,1]]', output: '3' },
      { input: 'grid = [[1,1],[1,0]]', output: '4' },
      { input: 'grid = [[1,1],[1,1]]', output: '4' },
    ],
    constraints: ['n == grid.length == grid[i].length', '1 <= n <= 50', 'grid[i][j] is 0 or 1'],
    starterCode: `function largestIsland(grid) {
  return 0;
}`,
    solutionCode: `function largestIsland(grid) {
  const n = grid.length;
  let islandId = 2;
  const areaMap = {};
  function dfs(r, c, id) {
    if (r < 0 || r >= n || c < 0 || c >= n || grid[r][c] !== 1) return 0;
    grid[r][c] = id;
    return 1 + dfs(r + 1, c, id) + dfs(r - 1, c, id) + dfs(r, c + 1, id) + dfs(r, c - 1, id);
  }
  let maxArea = 0;
  for (let r = 0; r < n; r++) {
    for (let c = 0; c < n; c++) {
      if (grid[r][c] === 1) {
        areaMap[islandId] = dfs(r, c, islandId);
        maxArea = Math.max(maxArea, areaMap[islandId]);
        islandId++;
      }
    }
  }
  const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
  for (let r = 0; r < n; r++) {
    for (let c = 0; c < n; c++) {
      if (grid[r][c] === 0) {
        const neighborIslands = new Set();
        for (const [dr, dc] of dirs) {
          const nr = r + dr, nc = c + dc;
          if (nr >= 0 && nr < n && nc >= 0 && nc < n && grid[nr][nc] > 1) {
            neighborIslands.add(grid[nr][nc]);
          }
        }
        let total = 1;
        for (const id of neighborIslands) total += areaMap[id];
        maxArea = Math.max(maxArea, total);
      }
    }
  }
  return maxArea;
}`,
    functionName: 'largestIsland',
    testCases: [
      { id: 1, input: [[[1, 0], [0, 1]]], expected: 3, inputDisplay: 'grid = [[1,0],[0,1]]', expectedDisplay: '3' },
      { id: 2, input: [[[1, 1], [1, 0]]], expected: 4, inputDisplay: 'grid = [[1,1],[1,0]]', expectedDisplay: '4' },
      { id: 3, input: [[[1, 1], [1, 1]]], expected: 4, inputDisplay: 'grid = all 1s', expectedDisplay: '4' },
    ],
    hints: ['First color each island with an ID and save areas in a Map. Then test flipping each 0.'],
    generateDefaultFrames: (tc) => [{ type: 'graph', nodes: [], edges: [], message: 'Labeling islands and testing connection points' }],
  },
  {
    id: 'sliding-puzzle',
    wingId: 'graphs',
    floor: 15,
    title: 'Boss Chamber: Sliding Puzzle (Board State BFS)',
    difficulty: 'hard',
    visualizerType: 'graph',
    monster: {
      id: 'puzzle-lich',
      name: 'Permutio the Tile Arch-Lich',
      title: 'Master of the 2x3 Configuration Space',
      maxHp: 4,
      hp: 4,
      sprite: 'lich',
      color: '#9333ea',
      attackName: 'Permutational Entanglement',
      attackPower: 3,
      defeatQuote: 'The 2x3 state space reached the target 123450...',
    },
    description: `On a 2 x 3 board, there are five tiles labeled 1 to 5, and an empty square represented by 0. A move consists of choosing 0 and a 4-directionally adjacent number and swapping it. Return the least number of moves required so that the state of the board is solved: [[1,2,3],[4,5,0]], or -1 if impossible.`,
    examples: [
      { input: 'board = [[1,2,3],[4,0,5]]', output: '1' },
      { input: 'board = [[1,2,3],[5,4,0]]', output: '-1' },
      { input: 'board = [[4,1,2],[5,0,3]]', output: '5' },
    ],
    constraints: ['board.length == 2, board[i].length == 3', 'board[i][j] is in the range [0, 5].'],
    starterCode: `function slidingPuzzle(board) {
  return -1;
}`,
    solutionCode: `function slidingPuzzle(board) {
  const target = '123450';
  const start = board.flat().join('');
  if (start === target) return 0;
  const neighbors = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4],
    4: [1, 3, 5],
    5: [2, 4]
  };
  const queue = [[start, 0]];
  const visited = new Set([start]);
  while (queue.length > 0) {
    const [state, moves] = queue.shift();
    if (state === target) return moves;
    const zeroIdx = state.indexOf('0');
    for (const nextIdx of neighbors[zeroIdx]) {
      const arr = state.split('');
      arr[zeroIdx] = arr[nextIdx];
      arr[nextIdx] = '0';
      const nextState = arr.join('');
      if (!visited.has(nextState)) {
        visited.add(nextState);
        queue.push([nextState, moves + 1]);
      }
    }
  }
  return -1;
}`,
    functionName: 'slidingPuzzle',
    testCases: [
      { id: 1, input: [[[1, 2, 3], [4, 0, 5]]], expected: 1, inputDisplay: 'board = [[1,2,3],[4,0,5]]', expectedDisplay: '1' },
      { id: 2, input: [[[1, 2, 3], [5, 4, 0]]], expected: -1, inputDisplay: 'board = [[1,2,3],[5,4,0]] (unsolvable)', expectedDisplay: '-1' },
      { id: 3, input: [[[4, 1, 2], [5, 0, 3]]], expected: 5, inputDisplay: 'board = [[4,1,2],[5,0,3]]', expectedDisplay: '5' },
    ],
    hints: ['Represent 2x3 board as a 6-character string and BFS through all reachable state transitions.'],
    generateDefaultFrames: (tc) => [{ type: 'graph', nodes: [], edges: [], message: 'Searching 2x3 tile state transitions with BFS' }],
  },
];
