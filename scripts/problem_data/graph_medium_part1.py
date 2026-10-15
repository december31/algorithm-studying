"""
Graphs Medium Problems - Part 1 (Floors 311 to 325 - 15 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_graph_medium_part1():
    problems = []

    # 11. Number of Islands
    problems.append(make_problem(
        pid="graph-m-num-islands", title="Number of Islands",
        wing_id="graphs", floor=311, difficulty="medium", visualizer_type="grid",
        monster_name="Archipelago Golem", monster_title="Lord of Isolated Archipelagos",
        monster_sprite="golem", monster_color="#10b981", monster_attack="Island Quake",
        monster_quote="Disconnected land masses in the endless ocean counted!",
        description="Given an `m x n` 2D binary grid `grid` which represents a map of `'1'`s (land) and `'0'`s (water), return the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.",
        examples=[{"input": "grid = [[\"1\",\"1\",\"1\",\"1\",\"0\"],[\"1\",\"1\",\"0\",\"1\",\"0\"],[\"1\",\"1\",\"0\",\"0\",\"0\"],[\"0\",\"0\",\"0\",\"0\",\"0\"]", "output": "1"}],
        constraints=["1 <= m, n <= 300", "grid[i][j] is '0' or '1'"],
        function_name="numIslands",
        starter_code="def numIslands(grid: list[list[str]]) -> int:\n    pass\n",
        solution_code="def numIslands(grid: list[list[str]]) -> int:\n    if not grid: return 0\n    R, C = len(grid), len(grid[0])\n    count = 0\n    def dfs(r, c):\n        if 0 <= r < R and 0 <= c < C and grid[r][c] == '1':\n            grid[r][c] = '0'\n            dfs(r + 1, c)\n            dfs(r - 1, c)\n            dfs(r, c + 1)\n            dfs(r, c - 1)\n    for r in range(R):\n        for c in range(C):\n            if grid[r][c] == '1':\n                count += 1\n                dfs(r, c)\n    return count\n",
        test_cases=[{"input": [[["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]], "expected": 1}, {"input": [[["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]], "expected": 3}],
        hints=["Iterate every cell. When '1' is found, increment island count and DFS/BFS sink all adjacent '1's."],
        leetcode_id=200
    ))

    # 12. Max Area of Island
    problems.append(make_problem(
        pid="graph-m-max-area-island", title="Max Area of Island",
        wing_id="graphs", floor=312, difficulty="medium", visualizer_type="grid",
        monster_name="Terran Behemoth", monster_title="Monarch of Vast Landmasses",
        monster_sprite="boss", monster_color="#22c55e", monster_attack="Continental Crush",
        monster_quote="Largest contiguous land component measured!",
        description="You are given an `m x n` binary matrix `grid`. An island is a group of `1`'s connected 4-directionally. The area of an island is the number of cells with a value 1 in the island. Return the maximum area of an island in `grid`. If there is no island, return 0.",
        examples=[{"input": "grid = [[0,0,1,0,0],[1,1,1,0,0],[0,0,0,1,1]]", "output": "4"}],
        constraints=["1 <= m, n <= 50", "grid[i][j] is either 0 or 1"],
        function_name="maxAreaOfIsland",
        starter_code="def maxAreaOfIsland(grid: list[list[int]]) -> int:\n    pass\n",
        solution_code="def maxAreaOfIsland(grid: list[list[int]]) -> int:\n    R, C = len(grid), len(grid[0])\n    def dfs(r, c):\n        if 0 <= r < R and 0 <= c < C and grid[r][c] == 1:\n            grid[r][c] = 0\n            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)\n        return 0\n    ans = 0\n    for r in range(R):\n        for c in range(C):\n            if grid[r][c] == 1:\n                ans = max(ans, dfs(r, c))\n    return ans\n",
        test_cases=[{"input": [[[0, 0, 1, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 1, 1]]], "expected": 4}, {"input": [[[0, 0, 0, 0, 0]]], "expected": 0}],
        hints=["Use DFS to compute component sizes, taking the maximum."],
        leetcode_id=695
    ))

    # 13. Rotting Oranges
    problems.append(make_problem(
        pid="graph-m-rotting-oranges", title="Rotting Oranges Multi-source BFS",
        wing_id="graphs", floor=313, difficulty="medium", visualizer_type="grid",
        monster_name="Decay Stalker", monster_title="Harbinger of Spreading Blight",
        monster_sprite="slime", monster_color="#f97316", monster_attack="Mould Spores",
        monster_quote="Minutes elapsed until every orange decomposed or trapped!",
        description="You are given an `m x n` `grid` where each cell can have one of three values: 0 representing an empty cell, 1 representing a fresh orange, or 2 representing a rotten orange. Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.",
        examples=[{"input": "grid = [[2,1,1],[1,1,0],[0,1,1]]", "output": "4"}, {"input": "grid = [[2,1,1],[0,1,1],[1,0,1]]", "output": "-1"}],
        constraints=["1 <= m, n <= 10"],
        function_name="orangesRotting",
        starter_code="def orangesRotting(grid: list[list[int]]) -> int:\n    pass\n",
        solution_code="def orangesRotting(grid: list[list[int]]) -> int:\n    from collections import deque\n    R, C = len(grid), len(grid[0])\n    queue = deque()\n    fresh = 0\n    for r in range(R):\n        for c in range(C):\n            if grid[r][c] == 2: queue.append((r, c, 0))\n            elif grid[r][c] == 1: fresh += 1\n    mins = 0\n    while queue:\n        r, c, d = queue.popleft()\n        mins = max(mins, d)\n        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:\n            nr, nc = r + dr, c + dc\n            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:\n                grid[nr][nc] = 2\n                fresh -= 1\n                queue.append((nr, nc, d + 1))\n    return mins if fresh == 0 else -1\n",
        test_cases=[{"input": [[[2, 1, 1], [1, 1, 0], [0, 1, 1]]], "expected": 4}, {"input": [[[2, 1, 1], [0, 1, 1], [1, 0, 1]]], "expected": -1}, {"input": [[[0, 2]]], "expected": 0}],
        hints=["Use a multi-source BFS starting with all initially rotten oranges at distance 0."],
        leetcode_id=994
    ))

    # 14. Pacific Atlantic Water Flow
    problems.append(make_problem(
        pid="graph-m-pacific-atlantic", title="Pacific Atlantic Water Flow",
        wing_id="graphs", floor=314, difficulty="medium", visualizer_type="grid",
        monster_name="Aquatic Drake", monster_title="Conduit of Dual Oceans",
        monster_sprite="dragon", monster_color="#38bdf8", monster_attack="Oceanic Deluge",
        monster_quote="Coordinates capable of draining into both Pacific and Atlantic revealed!",
        description="There is an `m x n` rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific touches top and left borders, while Atlantic touches bottom and right borders. Water can flow in 4 directions to equal or lower height cells. Return a list of grid coordinates where water can flow to both oceans.",
        examples=[{"input": "heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]", "output": "[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]"}],
        constraints=["1 <= m, n <= 200"],
        function_name="pacificAtlantic",
        starter_code="def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:\n    pass\n",
        solution_code="def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:\n    if not heights: return []\n    R, C = len(heights), len(heights[0])\n    pac, atl = set(), set()\n    def dfs(r, c, visited):\n        visited.add((r, c))\n        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:\n            nr, nc = r + dr, c + dc\n            if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visited:\n                if heights[nr][nc] >= heights[r][c]:\n                    dfs(nr, nc, visited)\n    for r in range(R):\n        dfs(r, 0, pac)\n        dfs(r, C - 1, atl)\n    for c in range(C):\n        dfs(0, c, pac)\n        dfs(R - 1, c, atl)\n    return sorted([[r, c] for r, c in (pac & atl)])\n",
        test_cases=[{"input": [[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]], "expected": [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]}, {"input": [[[1]]], "expected": [[0, 0]]}],
        hints=["Work backwards: reverse the flow starting from ocean borders moving inward to higher or equal terrain."],
        leetcode_id=417
    ))

    # 15. Surrounded Regions
    problems.append(make_problem(
        pid="graph-m-surrounded-regions", title="Surrounded Regions (Capture O's)",
        wing_id="graphs", floor=315, difficulty="medium", visualizer_type="grid",
        monster_name="Siege Gorgon", monster_title="Encircler of Enclosed Domains",
        monster_sprite="lich", monster_color="#a855f7", monster_attack="Encirclement",
        monster_quote="All 'O' regions not connected to matrix boundaries captured to 'X'!",
        description="Given an `m x n` matrix `board` containing `'X'` and `'O'`, capture all regions that are 4-directionally surrounded by `'X'`. A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region. Return the modified board.",
        examples=[{"input": "board = [[\"X\",\"X\",\"X\",\"X\"],[\"X\",\"O\",\"O\",\"X\"],[\"X\",\"X\",\"O\",\"X\"],[\"X\",\"O\",\"X\",\"X\"]]", "output": "[[\"X\",\"X\",\"X\",\"X\"],[\"X\",\"X\",\"X\",\"X\"],[\"X\",\"X\",\"X\",\"X\"],[\"X\",\"O\",\"X\",\"X\"]]"}],
        constraints=["1 <= m, n <= 200"],
        function_name="solveSurroundedRegions",
        starter_code="def solveSurroundedRegions(board: list[list[str]]) -> list[list[str]]:\n    pass\n",
        solution_code="def solveSurroundedRegions(board: list[list[str]]) -> list[list[str]]:\n    if not board: return board\n    R, C = len(board), len(board[0])\n    def dfs(r, c):\n        if 0 <= r < R and 0 <= c < C and board[r][c] == 'O':\n            board[r][c] = 'E'\n            dfs(r + 1, c)\n            dfs(r - 1, c)\n            dfs(r, c + 1)\n            dfs(r, c - 1)\n    for r in range(R):\n        dfs(r, 0)\n        dfs(r, C - 1)\n    for c in range(C):\n        dfs(0, c)\n        dfs(R - 1, c)\n    for r in range(R):\n        for c in range(C):\n            if board[r][c] == 'O': board[r][c] = 'X'\n            elif board[r][c] == 'E': board[r][c] = 'O'\n    return board\n",
        test_cases=[{"input": [[["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]], "expected": [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]}, {"input": [[["X"]]], "expected": [["X"]]}],
        hints=["Mark border-connected 'O's as escapees 'E'. Flip remaining 'O's to 'X', then 'E' back to 'O'."],
        leetcode_id=130
    ))

    # 16. Course Schedule I
    problems.append(make_problem(
        pid="graph-m-course-schedule-i", title="Course Schedule (Cycle Detection)",
        wing_id="graphs", floor=316, difficulty="medium", visualizer_type="graph",
        monster_name="Academic Lich", monster_title="Enforcer of Circular Curricula",
        monster_sprite="lich", monster_color="#ef4444", monster_attack="Paradox Curse",
        monster_quote="Curriculum graph analyzed for directed cycles!",
        description="There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`. Return `True` if you can finish all courses. Otherwise, return `False`.",
        examples=[{"input": "numCourses = 2, prerequisites = [[1,0]]", "output": "True"}, {"input": "numCourses = 2, prerequisites = [[1,0],[0,1]]", "output": "False"}],
        constraints=["1 <= numCourses <= 2000", "0 <= prerequisites.length <= 5000"],
        function_name="canFinish",
        starter_code="def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:\n    pass\n",
        solution_code="def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:\n    from collections import defaultdict, deque\n    adj = defaultdict(list)\n    in_deg = [0] * numCourses\n    for u, v in prerequisites:\n        adj[v].append(u)\n        in_deg[u] += 1\n    q = deque([i for i in range(numCourses) if in_deg[i] == 0])\n    visited = 0\n    while q:\n        curr = q.popleft()\n        visited += 1\n        for nxt in adj[curr]:\n            in_deg[nxt] -= 1\n            if in_deg[nxt] == 0: q.append(nxt)\n    return visited == numCourses\n",
        test_cases=[{"input": [2, [[1, 0]]], "expected": True}, {"input": [2, [[1, 0], [0, 1]]], "expected": False}],
        hints=["Kahn's algorithm using in-degrees: if total processed nodes equals numCourses, no cycle exists."],
        leetcode_id=207
    ))

    # 17. Course Schedule II
    problems.append(make_problem(
        pid="graph-m-course-schedule-ii", title="Course Schedule II (Topological Order)",
        wing_id="graphs", floor=317, difficulty="medium", visualizer_type="graph",
        monster_name="Grand Chronomancer", monster_title="Architect of Valid Sequences",
        monster_sprite="wizard", monster_color="#8b5cf6", monster_attack="Linear Order Ray",
        monster_quote="Valid topological sorting order of all courses established!",
        description="Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.",
        examples=[{"input": "numCourses = 2, prerequisites = [[1,0]]", "output": "[0,1]"}, {"input": "numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]", "output": "[0,1,2,3]"}],
        constraints=["1 <= numCourses <= 2000"],
        function_name="findOrder",
        starter_code="def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:\n    pass\n",
        solution_code="def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:\n    from collections import defaultdict, deque\n    adj = defaultdict(list)\n    in_deg = [0] * numCourses\n    for u, v in prerequisites:\n        adj[v].append(u)\n        in_deg[u] += 1\n    q = deque([i for i in range(numCourses) if in_deg[i] == 0])\n    order = []\n    while q:\n        curr = q.popleft()\n        order.append(curr)\n        for nxt in adj[curr]:\n            in_deg[nxt] -= 1\n            if in_deg[nxt] == 0: q.append(nxt)\n    return order if len(order) == numCourses else []\n",
        test_cases=[{"input": [2, [[1, 0]]], "expected": [0, 1]}, {"input": [4, [[1, 0], [2, 0], [3, 1], [3, 2]]], "expected": [0, 1, 2, 3]}, {"input": [2, [[0, 1], [1, 0]]], "expected": []}],
        hints=["Accumulate the popped elements in Kahn's algorithm."],
        leetcode_id=210
    ))

    # 18. Number of Provinces
    problems.append(make_problem(
        pid="graph-m-number-of-provinces", title="Number of Provinces",
        wing_id="graphs", floor=318, difficulty="medium", visualizer_type="graph",
        monster_name="Feudal Sovereign", monster_title="Ruler of Fractured Kingdoms",
        monster_sprite="boss", monster_color="#06b6d4", monster_attack="Sovereign Claim",
        monster_quote="Count of connected city components determined!",
        description="There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`. A province is a group of directly or indirectly connected cities. Given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if cities `i` and `j` are connected and `isConnected[i][j] = 0` otherwise, return the total number of provinces.",
        examples=[{"input": "isConnected = [[1,1,0],[1,1,0],[0,0,1]]", "output": "2"}, {"input": "isConnected = [[1,0,0],[0,1,0],[0,0,1]]", "output": "3"}],
        constraints=["1 <= n <= 200"],
        function_name="findCircleNum",
        starter_code="def findCircleNum(isConnected: list[list[int]]) -> int:\n    pass\n",
        solution_code="def findCircleNum(isConnected: list[list[int]]) -> int:\n    n = len(isConnected)\n    visited = [False] * n\n    provinces = 0\n    def dfs(u):\n        visited[u] = True\n        for v in range(n):\n            if isConnected[u][v] == 1 and not visited[v]:\n                dfs(v)\n    for i in range(n):\n        if not visited[i]:\n            provinces += 1\n            dfs(i)\n    return provinces\n",
        test_cases=[{"input": [[[1, 1, 0], [1, 1, 0], [0, 0, 1]]], "expected": 2}, {"input": [[[1, 0, 0], [0, 1, 0], [0, 0, 1]]], "expected": 3}],
        hints=["Standard connected components count on an adjacency matrix via DFS or DSU."],
        leetcode_id=547
    ))

    # 19. Clone Graph (Adjacency List Form)
    problems.append(make_problem(
        pid="graph-m-clone-graph-adj", title="Clone Graph Adjacency Structure",
        wing_id="graphs", floor=319, difficulty="medium", visualizer_type="graph",
        monster_name="Doppelganger Fiend", monster_title="Mirrorer of Graph Topologies",
        monster_sprite="demon", monster_color="#ec4899", monster_attack="Mirror Replication",
        monster_quote="Deep clone of all node pointers and adjacency lists generated!",
        description="Given an adjacency list `adjList` of an undirected graph where `adjList[i]` contains the 1-indexed neighbors of node `i + 1`, create a deep copy of the adjacency list structure, preserving all original edge relationships.",
        examples=[{"input": "adjList = [[2,4],[1,3],[2,4],[1,3]]", "output": "[[2,4],[1,3],[2,4],[1,3]]"}],
        constraints=["0 <= adjList.length <= 100"],
        function_name="cloneGraphAdj",
        starter_code="def cloneGraphAdj(adjList: list[list[int]]) -> list[list[int]]:\n    pass\n",
        solution_code="def cloneGraphAdj(adjList: list[list[int]]) -> list[list[int]]:\n    if not adjList: return []\n    return [list(neighbors) for neighbors in adjList]\n",
        test_cases=[{"input": [[[2, 4], [1, 3], [2, 4], [1, 3]]], "expected": [[2, 4], [1, 3], [2, 4], [1, 3]]}, {"input": [[]], "expected": []}, {"input": [[[]]], "expected": [[]]}],
        hints=["Deep copy the nested neighbor lists."],
        leetcode_id=133
    ))

    # 20. Graph Valid Tree
    problems.append(make_problem(
        pid="graph-m-graph-valid-tree", title="Graph Valid Tree Check",
        wing_id="graphs", floor=320, difficulty="medium", visualizer_type="graph",
        monster_name="Arboreal Arbiter", monster_title="Judge of Acyclic Spanning Trees",
        monster_sprite="gargoyle", monster_color="#10b981", monster_attack="Root Constriction",
        monster_quote="Exactly n - 1 edges and single connected component validated!",
        description="Given `n` nodes labeled from `0` to `n - 1` and a list of undirected `edges`, determine if these edges form a valid tree. (A valid tree has exactly `n - 1` edges and is fully connected with no cycles).",
        examples=[{"input": "n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]", "output": "True"}, {"input": "n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]", "output": "False"}],
        constraints=["1 <= n <= 2000", "0 <= edges.length <= 5000"],
        function_name="validTree",
        starter_code="def validTree(n: int, edges: list[list[int]]) -> bool:\n    pass\n",
        solution_code="def validTree(n: int, edges: list[list[int]]) -> bool:\n    if len(edges) != n - 1: return False\n    parent = list(range(n))\n    def find(i):\n        if parent[i] == i: return i\n        parent[i] = find(parent[i])\n        return parent[i]\n    for u, v in edges:\n        root_u = find(u)\n        root_v = find(v)\n        if root_u == root_v: return False\n        parent[root_u] = root_v\n    return True\n",
        test_cases=[{"input": [5, [[0, 1], [0, 2], [0, 3], [1, 4]]], "expected": True}, {"input": [5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]], "expected": False}],
        hints=["A graph of n nodes is a tree if and only if it has n - 1 edges and no cycles."],
        leetcode_id=261
    ))

    # 21. Walls and Gates
    problems.append(make_problem(
        pid="graph-m-walls-and-gates", title="Walls and Gates Distance Matrix",
        wing_id="graphs", floor=321, difficulty="medium", visualizer_type="grid",
        monster_name="Dungeon Architect", monster_title="Mason of Portals and Ramparts",
        monster_sprite="golem", monster_color="#64748b", monster_attack="Stone Enclosure",
        monster_quote="Shortest distance from empty rooms to nearest gate marked!",
        description="You are given an `m x n` grid `rooms` initialized with three possible values: `-1` is a wall, `0` is a gate, and `2147483647` (INF) is an empty room. Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should remain INF.",
        examples=[{"input": "rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]", "output": "[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]"}],
        constraints=["1 <= m, n <= 250"],
        function_name="wallsAndGates",
        starter_code="def wallsAndGates(rooms: list[list[int]]) -> list[list[int]]:\n    pass\n",
        solution_code="def wallsAndGates(rooms: list[list[int]]) -> list[list[int]]:\n    if not rooms: return rooms\n    R, C = len(rooms), len(rooms[0])\n    from collections import deque\n    q = deque()\n    for r in range(R):\n        for c in range(C):\n            if rooms[r][c] == 0:\n                q.append((r, c))\n    while q:\n        r, c = q.popleft()\n        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:\n            nr, nc = r + dr, c + dc\n            if 0 <= nr < R and 0 <= nc < C and rooms[nr][nc] == 2147483647:\n                rooms[nr][nc] = rooms[r][c] + 1\n                q.append((nr, nc))\n    return rooms\n",
        test_cases=[{"input": [[[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1], [2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]], "expected": [[3, -1, 0, 1], [2, 2, 1, -1], [1, -1, 2, -1], [0, -1, 3, 4]]}],
        hints=["Multi-source BFS originating simultaneously from all gates (value 0)."],
        leetcode_id=286
    ))

    # 22. 01 Matrix
    problems.append(make_problem(
        pid="graph-m-01-matrix", title="01 Matrix (Distance to Nearest Zero)",
        wing_id="graphs", floor=322, difficulty="medium", visualizer_type="grid",
        monster_name="Binary Apparition", monster_title="Attractor to Void Zeroes",
        monster_sprite="spectre", monster_color="#38bdf8", monster_attack="Null Radiance",
        monster_quote="Distance of each cell to nearest 0 calculated!",
        description="Given an `m x n` binary matrix `mat`, return the distance of the nearest `0` for each cell. The distance between two adjacent cells is 1.",
        examples=[{"input": "mat = [[0,0,0],[0,1,0],[0,0,0]]", "output": "[[0,0,0],[0,1,0],[0,0,0]]"}, {"input": "mat = [[0,0,0],[0,1,0],[1,1,1]]", "output": "[[0,0,0],[0,1,0],[1,2,1]]"}],
        constraints=["1 <= m, n <= 10000"],
        function_name="updateMatrix",
        starter_code="def updateMatrix(mat: list[list[int]]) -> list[list[int]]:\n    pass\n",
        solution_code="def updateMatrix(mat: list[list[int]]) -> list[list[int]]:\n    R, C = len(mat), len(mat[0])\n    from collections import deque\n    dist = [[-1] * C for _ in range(R)]\n    q = deque()\n    for r in range(R):\n        for c in range(C):\n            if mat[r][c] == 0:\n                dist[r][c] = 0\n                q.append((r, c))\n    while q:\n        r, c = q.popleft()\n        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:\n            nr, nc = r + dr, c + dc\n            if 0 <= nr < R and 0 <= nc < C and dist[nr][nc] == -1:\n                dist[nr][nc] = dist[r][c] + 1\n                q.append((nr, nc))\n    return dist\n",
        test_cases=[{"input": [[[0, 0, 0], [0, 1, 0], [0, 0, 0]]], "expected": [[0, 0, 0], [0, 1, 0], [0, 0, 0]]}, {"input": [[[0, 0, 0], [0, 1, 0], [1, 1, 1]]], "expected": [[0, 0, 0], [0, 1, 0], [1, 2, 1]]}],
        hints=["Initialize queue with all zeroes, then propagate outwards with BFS."],
        leetcode_id=542
    ))

    # 23. Shortest Path in Binary Matrix
    problems.append(make_problem(
        pid="graph-m-shortest-path-binary-matrix", title="Shortest Path in 8-Directional Binary Matrix",
        wing_id="graphs", floor=323, difficulty="medium", visualizer_type="grid",
        monster_name="Diagonal Stalker", monster_title="Hunter of 8-Directional Paths",
        monster_sprite="wraith", monster_color="#eab308", monster_attack="Diagonal Cleave",
        monster_quote="Shortest clear 8-way traversal from top-left to bottom-right!",
        description="Given an `n x n` binary matrix `grid`, return the length of the shortest clear path in the matrix. If there is no clear path, return -1. A clear path is an 8-directionally connected sequence of 0-cells from `(0, 0)` to `(n - 1, n - 1)`.",
        examples=[{"input": "grid = [[0,1],[1,0]]", "output": "2"}, {"input": "grid = [[0,0,0],[1,1,0],[1,1,0]]", "output": "4"}, {"input": "grid = [[1,0,0],[1,1,0],[1,1,0]]", "output": "-1"}],
        constraints=["1 <= n <= 100"],
        function_name="shortestPathBinaryMatrix",
        starter_code="def shortestPathBinaryMatrix(grid: list[list[int]]) -> int:\n    pass\n",
        solution_code="def shortestPathBinaryMatrix(grid: list[list[int]]) -> int:\n    n = len(grid)\n    if grid[0][0] != 0 or grid[n - 1][n - 1] != 0: return -1\n    if n == 1: return 1\n    from collections import deque\n    q = deque([(0, 0, 1)])\n    grid[0][0] = 1\n    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]\n    while q:\n        r, c, d = q.popleft()\n        if r == n - 1 and c == n - 1: return d\n        for dr, dc in dirs:\n            nr, nc = r + dr, c + dc\n            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:\n                grid[nr][nc] = 1\n                q.append((nr, nc, d + 1))\n    return -1\n",
        test_cases=[{"input": [[[0, 1], [1, 0]]], "expected": 2}, {"input": [[[0, 0, 0], [1, 1, 0], [1, 1, 0]]], "expected": 4}, {"input": [[[1, 0, 0], [1, 1, 0], [1, 1, 0]]], "expected": -1}],
        hints=["BFS exploring all 8 neighboring directions."],
        leetcode_id=1091
    ))

    # 24. Is Graph Bipartite?
    problems.append(make_problem(
        pid="graph-m-is-graph-bipartite", title="Is Graph Bipartite?",
        wing_id="graphs", floor=324, difficulty="medium", visualizer_type="graph",
        monster_name="Dichotomy Fiend", monster_title="Divider of Disjoint Vertex Sets",
        monster_sprite="imp", monster_color="#d946ef", monster_attack="Color Discord",
        monster_quote="2-colorability of disconnected graph components checked!",
        description="There is an undirected graph with `n` nodes, where each node is numbered between `0` and `n - 1`. You are given a 2D array `graph`, where `graph[u]` is an array of nodes that node `u` is adjacent to. Return `True` if and only if it is bipartite.",
        examples=[{"input": "graph = [[1,2,3],[0,2],[0,1,3],[0,2]]", "output": "False"}, {"input": "graph = [[1,3],[0,2],[1,3],[0,2]]", "output": "True"}],
        constraints=["1 <= graph.length <= 100"],
        function_name="isBipartite",
        starter_code="def isBipartite(graph: list[list[int]]) -> bool:\n    pass\n",
        solution_code="def isBipartite(graph: list[list[int]]) -> bool:\n    n = len(graph)\n    color = [-1] * n\n    from collections import deque\n    for i in range(n):\n        if color[i] != -1: continue\n        color[i] = 0\n        q = deque([i])\n        while q:\n            u = q.popleft()\n            for v in graph[u]:\n                if color[v] == -1:\n                    color[v] = 1 - color[u]\n                    q.append(v)\n                elif color[v] == color[u]:\n                    return False\n    return True\n",
        test_cases=[{"input": [[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]], "expected": False}, {"input": [[[1, 3], [0, 2], [1, 3], [0, 2]]], "expected": True}],
        hints=["Use BFS/DFS with 2 colors. Color each unvisited component starting with color 0."],
        leetcode_id=785
    ))

    # 25. Redundant Connection
    problems.append(make_problem(
        pid="graph-m-redundant-connection", title="Redundant Connection (Cycle Forming Edge)",
        wing_id="graphs", floor=325, difficulty="medium", visualizer_type="graph",
        monster_name="Ring Sentry", monster_title="Guardian of Spanning Trees",
        monster_sprite="skeleton", monster_color="#ef4444", monster_attack="Cycle Sever",
        monster_quote="The redundant edge completing the undirected cycle found!",
        description="In this problem, a tree is an undirected graph that is connected and has no cycles. You are given a graph that started as a tree with `n` nodes labeled from 1 to `n`, with one additional edge added. The added edge has two different vertices chosen from 1 to `n`, and was not an edge that already existed. Return an edge that can be removed so that the resulting graph is a tree of `n` nodes. If there are multiple answers, return the answer that occurs last in the input.",
        examples=[{"input": "edges = [[1,2],[1,3],[2,3]]", "output": "[2,3]"}, {"input": "edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]", "output": "[1,4]"}],
        constraints=["3 <= edges.length <= 1000"],
        function_name="findRedundantConnection",
        starter_code="def findRedundantConnection(edges: list[list[int]]) -> list[int]:\n    pass\n",
        solution_code="def findRedundantConnection(edges: list[list[int]]) -> list[int]:\n    n = len(edges)\n    parent = list(range(n + 1))\n    def find(i):\n        if parent[i] == i: return i\n        parent[i] = find(parent[i])\n        return parent[i]\n    for u, v in edges:\n        ru, rv = find(u), find(v)\n        if ru == rv: return [u, v]\n        parent[ru] = rv\n    return []\n",
        test_cases=[{"input": [[[1, 2], [1, 3], [2, 3]]], "expected": [2, 3]}, {"input": [[[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]], "expected": [1, 4]}],
        hints=["Use Disjoint Set Union (Union-Find). The first edge whose vertices already share a root is the redundant edge."],
        leetcode_id=684
    ))

    return problems
