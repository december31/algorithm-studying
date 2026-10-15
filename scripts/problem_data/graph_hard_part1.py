"""
Graphs Hard Problems - Part 1 (Floors 371 to 385 - 15 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_graph_hard_part1():
    problems = []

    # 71. Alien Dictionary
    problems.append(make_problem(
        pid="graph-h-alien-dictionary", title="Alien Dictionary Topological Sort",
        wing_id="graphs", floor=371, difficulty="hard", visualizer_type="graph",
        monster_name="Xenoglossic Archon", monster_title="Decipherer of Extraterrestrial Alphabets",
        monster_sprite="beholder", monster_color="#ec4899", monster_attack="Lexical Distortion",
        monster_quote="Alien lexicographical character order deciphered!",
        description="There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you. You are given a list of strings `words` from the alien language's dictionary, where the strings are claimed to be sorted lexicographically according to this alien language. Return a string of the unique letters in the new alien language sorted in lexicographically increasing order. If the order is invalid, return `\"\"`.",
        examples=[{"input": "words = [\"wrt\",\"wrf\",\"er\",\"ett\",\"rftt\"]", "output": "\"wertf\""}, {"input": "words = [\"z\",\"x\"]", "output": "\"zx\""}, {"input": "words = [\"z\",\"x\",\"z\"]", "output": "\"\""}],
        constraints=["1 <= words.length <= 100", "1 <= words[i].length <= 100"],
        function_name="alienOrder",
        starter_code="def alienOrder(words: list[str]) -> str:\n    pass\n",
        solution_code="def alienOrder(words: list[str]) -> str:\n    from collections import defaultdict, deque\n    adj = defaultdict(set)\n    in_deg = {c: 0 for w in words for c in w}\n    for i in range(len(words) - 1):\n        w1, w2 = words[i], words[i + 1]\n        min_len = min(len(w1), len(w2))\n        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:\n            return \"\"\n        for j in range(min_len):\n            if w1[j] != w2[j]:\n                if w2[j] not in adj[w1[j]]:\n                    adj[w1[j]].add(w2[j])\n                    in_deg[w2[j]] += 1\n                break\n    q = deque([c for c, deg in in_deg.items() if deg == 0])\n    res = []\n    while q:\n        c = q.popleft()\n        res.append(c)\n        for nxt in adj[c]:\n            in_deg[nxt] -= 1\n            if in_deg[nxt] == 0: q.append(nxt)\n    return \"\".join(res) if len(res) == len(in_deg) else \"\"\n",
        test_cases=[{"input": [["wrt", "wrf", "er", "ett", "rftt"]], "expected": "wertf"}, {"input": [["z", "x"]], "expected": "zx"}, {"input": [["z", "x", "z"]], "expected": ""}],
        hints=["Compare adjacent words to extract directed character precedence edges. Kahn's topological sort determines order."],
        leetcode_id=269
    ))

    # 72. Critical Connections in a Network
    problems.append(make_problem(
        pid="graph-h-critical-connections", title="Critical Connections in Network (Bridges)",
        wing_id="graphs", floor=372, difficulty="hard", visualizer_type="graph",
        monster_name="Bridge Severer", monster_title="Destroyer of Non-Redundant Arteries",
        monster_sprite="demon", monster_color="#ef4444", monster_attack="Bridge Fracture",
        monster_quote="All critical bridges whose removal disconnects the network isolated!",
        description="There are `n` servers numbered from 0 to `n - 1` connected by undirected server-to-server `connections`. A critical connection is a connection that, if removed, will make some servers unable to reach some other server. Return all critical connections in the network in sorted order.",
        examples=[{"input": "n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]", "output": "[[1,3]]"}],
        constraints=["2 <= n <= 100000", "n - 1 <= connections.length <= 100000"],
        function_name="criticalConnections",
        starter_code="def criticalConnections(n: int, connections: list[list[int]]) -> list[list[int]]:\n    pass\n",
        solution_code="def criticalConnections(n: int, connections: list[list[int]]) -> list[list[int]]:\n    from collections import defaultdict\n    graph = defaultdict(list)\n    for u, v in connections:\n        graph[u].append(v)\n        graph[v].append(u)\n    tin = [-1] * n\n    low = [-1] * n\n    timer = [0]\n    bridges = []\n    def dfs(u, p):\n        tin[u] = low[u] = timer[0]\n        timer[0] += 1\n        for v in graph[u]:\n            if v == p: continue\n            if tin[v] != -1:\n                low[u] = min(low[u], tin[v])\n            else:\n                dfs(v, u)\n                low[u] = min(low[u], low[v])\n                if low[v] > tin[u]:\n                    bridges.append(sorted([u, v]))\n    dfs(0, -1)\n    return sorted(bridges)\n",
        test_cases=[{"input": [4, [[0, 1], [1, 2], [2, 0], [1, 3]]], "expected": [[1, 3]]}, {"input": [2, [[0, 1]]], "expected": [[0, 1]]}],
        hints=["Tarjan's bridge-finding algorithm using entry discovery times and low values."],
        leetcode_id=1192
    ))

    # 73. Trapping Rain Water II
    problems.append(make_problem(
        pid="graph-h-trapping-rain-water-ii", title="Trapping Rain Water II (3D Elevation)",
        wing_id="graphs", floor=373, difficulty="hard", visualizer_type="grid",
        monster_name="Aquatic Colossus", monster_title="Reservoir of 3D Fluid Basins",
        monster_sprite="golem", monster_color="#06b6d4", monster_attack="Fluid Compression",
        monster_quote="Total cubic units of water trapped inside 3D elevation map!",
        description="Given an `m x n` integer matrix `heightMap` representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.",
        examples=[{"input": "heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]", "output": "4"}],
        constraints=["1 <= m, n <= 200", "0 <= heightMap[i][j] <= 20000"],
        function_name="trapRainWater",
        starter_code="def trapRainWater(heightMap: list[list[int]]) -> int:\n    pass\n",
        solution_code="def trapRainWater(heightMap: list[list[int]]) -> int:\n    if not heightMap or not heightMap[0]: return 0\n    R, C = len(heightMap), len(heightMap[0])\n    import heapq\n    visited = [[False] * C for _ in range(R)]\n    pq = []\n    for r in range(R):\n        for c in range(C):\n            if r == 0 or r == R - 1 or c == 0 or c == C - 1:\n                heapq.heappush(pq, (heightMap[r][c], r, c))\n                visited[r][c] = True\n    water = 0\n    while pq:\n        h, r, c = heapq.heappop(pq)\n        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:\n            nr, nc = r + dr, c + dc\n            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:\n                visited[nr][nc] = True\n                if heightMap[nr][nc] < h:\n                    water += h - heightMap[nr][nc]\n                heapq.heappush(pq, (max(h, heightMap[nr][nc]), nr, nc))\n    return water\n",
        test_cases=[{"input": [[[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]], "expected": 4}, {"input": [[[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]], "expected": 10}],
        hints=["Push all boundary cells into a min-heap, popping the lowest boundary to drain water inwards."],
        leetcode_id=407
    ))

    # 74. Making A Large Island
    problems.append(make_problem(
        pid="graph-h-making-large-island", title="Making A Large Island (Single Flip)",
        wing_id="graphs", floor=374, difficulty="hard", visualizer_type="grid",
        monster_name="Pangea Overlord", monster_title="Uniter of Separated Continents",
        monster_sprite="boss", monster_color="#10b981", monster_attack="Continental Shift",
        monster_quote="Maximum island area formed by changing at most one 0 to 1!",
        description="You are given an `n x n` binary matrix `grid`. You are allowed to change at most one `0` to be `1`. Return the size of the largest island in `grid` after applying this operation.",
        examples=[{"input": "grid = [[1,0],[0,1]]", "output": "3"}, {"input": "grid = [[1,1],[1,0]]", "output": "4"}, {"input": "grid = [[1,1],[1,1]]", "output": "4"}],
        constraints=["n == grid.length", "1 <= n <= 500"],
        function_name="largestIsland",
        starter_code="def largestIsland(grid: list[list[int]]) -> int:\n    pass\n",
        solution_code="def largestIsland(grid: list[list[int]]) -> int:\n    n = len(grid)\n    island_id = 2\n    area = {}\n    def dfs(r, c, i_id):\n        grid[r][c] = i_id\n        size = 1\n        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:\n            nr, nc = r + dr, c + dc\n            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:\n                size += dfs(nr, nc, i_id)\n        return size\n    for r in range(n):\n        for c in range(n):\n            if grid[r][c] == 1:\n                area[island_id] = dfs(r, c, island_id)\n                island_id += 1\n    ans = max(area.values(), default=0)\n    if ans < n * n: ans = max(ans, 1)\n    for r in range(n):\n        for c in range(n):\n            if grid[r][c] == 0:\n                seen_islands = set()\n                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:\n                    nr, nc = r + dr, c + dc\n                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:\n                        seen_islands.add(grid[nr][nc])\n                potential = 1 + sum(area[i] for i in seen_islands)\n                ans = max(ans, potential)\n    return ans\n",
        test_cases=[{"input": [[[1, 0], [0, 1]]], "expected": 3}, {"input": [[[1, 1], [1, 0]]], "expected": 4}, {"input": [[[1, 1], [1, 1]]], "expected": 4}],
        hints=["Label existing islands with unique IDs and compute their areas. For each 0 cell, sum the areas of adjacent unique islands plus 1."],
        leetcode_id=827
    ))

    # 75. Shortest Path Visiting All Nodes
    problems.append(make_problem(
        pid="graph-h-shortest-path-visiting-all-nodes", title="Shortest Path Visiting All Nodes (Bitmask BFS)",
        wing_id="graphs", floor=375, difficulty="hard", visualizer_type="graph",
        monster_name="Travelling Ouroboros", monster_title="Serpent Traversing All World Nodes",
        monster_sprite="dragon", monster_color="#8b5cf6", monster_attack="Coiling Infinity",
        monster_quote="Shortest walk visiting all graph vertices computed!",
        description="You have an undirected, connected graph of `n` nodes (0 to n - 1), given as `graph` where `graph[i]` is a list of all nodes with an edge between node `i` and `graph[i][j]`. Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.",
        examples=[{"input": "graph = [[1,2,3],[0],[0],[0]]", "output": "4"}, {"input": "graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]", "output": "4"}],
        constraints=["1 <= n <= 12"],
        function_name="shortestPathLength",
        starter_code="def shortestPathLength(graph: list[list[int]]) -> int:\n    pass\n",
        solution_code="def shortestPathLength(graph: list[list[int]]) -> int:\n    n = len(graph)\n    if n <= 1: return 0\n    from collections import deque\n    target_mask = (1 << n) - 1\n    q = deque([(i, 1 << i, 0) for i in range(n)])\n    visited = {(i, 1 << i) for i in range(n)}\n    while q:\n        u, mask, dist = q.popleft()\n        if mask == target_mask: return dist\n        for v in graph[u]:\n            nxt_mask = mask | (1 << v)\n            if (v, nxt_mask) not in visited:\n                visited.add((v, nxt_mask))\n                q.append((v, nxt_mask, dist + 1))\n    return 0\n",
        test_cases=[{"input": [[[1, 2, 3], [0], [0], [0]]], "expected": 4}, {"input": [[[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]], "expected": 4}],
        hints=["State in BFS is (current_node, visited_bitmask). Multi-source queue starting with all (i, 1<<i)."],
        leetcode_id=847
    ))

    # 76. Bus Routes
    problems.append(make_problem(
        pid="graph-h-bus-routes", title="Bus Routes (Minimum Transfers)",
        wing_id="graphs", floor=376, difficulty="hard", visualizer_type="graph",
        monster_name="Transit Gargoyle", monster_title="Conductor of Interlocking Lines",
        monster_sprite="gargoyle", monster_color="#f59e0b", monster_attack="Ticket Barrier",
        monster_quote="Least number of buses to travel from source stop to target stop!",
        description="You are given an array `routes` representing bus routes where `routes[i]` is a bus route that the `i`-th bus repeats forever. You start at the bus stop `source` and want to go to the bus stop `target`. You can travel between bus stops by buses only. Return the least number of buses you must take to travel from `source` to `target`. If it is not possible, return `-1`.",
        examples=[{"input": "routes = [[1,2,7],[3,6,7]], source = 1, target = 6", "output": "2"}, {"input": "routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12", "output": "-1"}],
        constraints=["1 <= routes.length <= 500", "source, target are integers"],
        function_name="numBusesToDestination",
        starter_code="def numBusesToDestination(routes: list[list[int]], source: int, target: int) -> int:\n    pass\n",
        solution_code="def numBusesToDestination(routes: list[list[int]], source: int, target: int) -> int:\n    if source == target: return 0\n    from collections import defaultdict, deque\n    stop_to_buses = defaultdict(list)\n    for bus_idx, route in enumerate(routes):\n        for stop in route:\n            stop_to_buses[stop].append(bus_idx)\n    if source not in stop_to_buses or target not in stop_to_buses: return -1\n    visited_buses = set()\n    visited_stops = {source}\n    q = deque([(source, 0)])\n    while q:\n        stop, buses_taken = q.popleft()\n        if stop == target: return buses_taken\n        for bus in stop_to_buses[stop]:\n            if bus not in visited_buses:\n                visited_buses.add(bus)\n                for nxt_stop in routes[bus]:\n                    if nxt_stop not in visited_stops:\n                        visited_stops.add(nxt_stop)\n                        q.append((nxt_stop, buses_taken + 1))\n    return -1\n",
        test_cases=[{"input": [[[1, 2, 7], [3, 6, 7]], 1, 6], "expected": 2}, {"input": [[[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12], "expected": -1}],
        hints=["Treat each bus as a hyperedge or node. BFS over buses rather than individual stops."],
        leetcode_id=815
    ))

    # 77. Cut Off Trees for Golf Event
    problems.append(make_problem(
        pid="graph-h-cut-off-trees-golf", title="Cut Off Trees for Golf Event",
        wing_id="graphs", floor=377, difficulty="hard", visualizer_type="grid",
        monster_name="Forest Golem", monster_title="Keeper of Ordered Timber",
        monster_sprite="golem", monster_color="#22c55e", monster_attack="Lumber Quake",
        monster_quote="Minimum steps walking to cut trees in ascending height order!",
        description="You are given an `m x n` grid of non-negative integers representing the coordinates of a forest: 0 is an obstacle, 1 is empty flat ground, values > 1 are trees with their height. You must cut down all trees in order from shortest to tallest, starting from (0, 0). Return the minimum steps you need to walk to cut off all trees, or -1 if impossible.",
        examples=[{"input": "forest = [[1,2,3],[0,0,4],[7,6,5]]", "output": "6"}, {"input": "forest = [[1,2,3],[0,0,0],[7,6,5]]", "output": "-1"}],
        constraints=["1 <= m, n <= 50"],
        function_name="cutOffTree",
        starter_code="def cutOffTree(forest: list[list[int]]) -> int:\n    pass\n",
        solution_code="def cutOffTree(forest: list[list[int]]) -> int:\n    R, C = len(forest), len(forest[0])\n    trees = []\n    for r in range(R):\n        for c in range(C):\n            if forest[r][c] > 1:\n                trees.append((forest[r][c], r, c))\n    trees.sort()\n    from collections import deque\n    def bfs(sr, sc, tr, tc):\n        if sr == tr and sc == tc: return 0\n        q = deque([(sr, sc, 0)])\n        visited = {(sr, sc)}\n        while q:\n            r, c, d = q.popleft()\n            if r == tr and c == tc: return d\n            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:\n                nr, nc = r + dr, c + dc\n                if 0 <= nr < R and 0 <= nc < C and forest[nr][nc] != 0 and (nr, nc) not in visited:\n                    visited.add((nr, nc))\n                    q.append((nr, nc, d + 1))\n        return -1\n    curr_r, curr_c = 0, 0\n    total_steps = 0\n    for h, tr, tc in trees:\n        d = bfs(curr_r, curr_c, tr, tc)\n        if d == -1: return -1\n        total_steps += d\n        curr_r, curr_c = tr, tc\n    return total_steps\n",
        test_cases=[{"input": [[[1, 2, 3], [0, 0, 4], [7, 6, 5]]], "expected": 6}, {"input": [[[1, 2, 3], [0, 0, 0], [7, 6, 5]]], "expected": -1}],
        hints=["Sort trees by height. Run BFS between consecutive target trees to compute travel distances."],
        leetcode_id=675
    ))

    # 78. Remove Max Number of Edges to Keep Graph Fully Traversable
    problems.append(make_problem(
        pid="graph-h-remove-max-edges-traversable", title="Keep Graph Fully Traversable (Max Removable Edges)",
        wing_id="graphs", floor=378, difficulty="hard", visualizer_type="graph",
        monster_name="Dual Path Archon", monster_title="Balancer of Alice and Bob Corridors",
        monster_sprite="spectre", monster_color="#38bdf8", monster_attack="Bridge Dissolution",
        monster_quote="Maximum redundant edges eliminated while keeping graph traversable for both travelers!",
        description="Alice and Bob have an undirected graph of `n` nodes and 3 types of edges: Type 1 can be traversed by Alice only, Type 2 by Bob only, Type 3 by both. Return the maximum number of edges you can remove such that the graph remains fully traversable for both Alice and Bob. If impossible, return -1.",
        examples=[{"input": "n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]", "output": "2"}],
        constraints=["1 <= n <= 100000", "1 <= edges.length <= 100000"],
        function_name="maxNumEdgesToRemove",
        starter_code="def maxNumEdgesToRemove(n: int, edges: list[list[int]]) -> int:\n    pass\n",
        solution_code="def maxNumEdgesToRemove(n: int, edges: list[list[int]]) -> int:\n    parent_a = list(range(n + 1))\n    parent_b = list(range(n + 1))\n    def find(p, i):\n        if p[i] == i: return i\n        p[i] = find(p, p[i])\n        return p[i]\n    def union(p, u, v):\n        ru, rv = find(p, u), find(p, v)\n        if ru == rv: return False\n        p[ru] = rv\n        return True\n    used = 0\n    comp_a = comp_b = n\n    # Process type 3 edges first\n    for t, u, v in edges:\n        if t == 3:\n            ua = union(parent_a, u, v)\n            ub = union(parent_b, u, v)\n            if ua or ub:\n                used += 1\n                comp_a -= 1\n                comp_b -= 1\n    for t, u, v in edges:\n        if t == 1:\n            if union(parent_a, u, v):\n                used += 1\n                comp_a -= 1\n        elif t == 2:\n            if union(parent_b, u, v):\n                used += 1\n                comp_b -= 1\n    if comp_a == 1 and comp_b == 1:\n        return len(edges) - used\n    return -1\n",
        test_cases=[{"input": [4, [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]], "expected": 2}, {"input": [4, [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]], "expected": 0}, {"input": [4, [[3, 2, 3], [1, 1, 2], [2, 3, 4]]], "expected": -1}],
        hints=["Greedily use Type 3 edges first in two separate DSU structures."],
        leetcode_id=1579
    ))

    # 79. Reachable Nodes In Subdivided Graph
    problems.append(make_problem(
        pid="graph-h-reachable-nodes-subdivided", title="Reachable Nodes in Subdivided Graph",
        wing_id="graphs", floor=379, difficulty="hard", visualizer_type="graph",
        monster_name="Micro-Node Spectre", monster_title="Surveyor of Subdivided Edge Nodes",
        monster_sprite="wraith", monster_color="#ec4899", monster_attack="Subdivision Swarm",
        monster_quote="Total original and subdivision nodes reachable within maxMoves!",
        description="You are given an undirected graph of `n` nodes (0 to n - 1). Each `edges[i] = [ui, vi, cnti]` indicates an edge subdivided into `cnti` new nodes. You start at node 0 and have `maxMoves` moves. Return the number of nodes you can reach in the subdivided graph.",
        examples=[{"input": "edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3", "output": "13"}],
        constraints=["0 <= edges.length <= 10000", "1 <= n <= 3000"],
        function_name="reachableNodes",
        starter_code="def reachableNodes(edges: list[list[int]], maxMoves: int, n: int) -> int:\n    pass\n",
        solution_code="def reachableNodes(edges: list[list[int]], maxMoves: int, n: int) -> int:\n    import heapq\n    from collections import defaultdict\n    graph = defaultdict(dict)\n    for u, v, w in edges:\n        graph[u][v] = w\n        graph[v][u] = w\n    pq = [(0, 0)]\n    dist = {}\n    while pq:\n        d, u = heapq.heappop(pq)\n        if u in dist: continue\n        dist[u] = d\n        for v, w in graph[u].items():\n            if v not in dist and d + w + 1 <= maxMoves:\n                heapq.heappush(pq, (d + w + 1, v))\n    ans = len(dist)\n    for u, v, w in edges:\n        c1 = max(0, maxMoves - dist[u]) if u in dist else 0\n        c2 = max(0, maxMoves - dist[v]) if v in dist else 0\n        ans += min(w, c1 + c2)\n    return ans\n",
        test_cases=[{"input": [[[0, 1, 10], [0, 2, 1], [1, 2, 2]], 6, 3], "expected": 13}, {"input": [[[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]], 10, 4], "expected": 23}],
        hints=["Run Dijkstra on major nodes where edge weight is cnt + 1. Then calculate remaining steps used along each edge."],
        leetcode_id=882
    ))

    # 80. Parallel Courses III
    problems.append(make_problem(
        pid="graph-h-parallel-courses-iii", title="Parallel Courses III (Critical Path Time)",
        wing_id="graphs", floor=380, difficulty="hard", visualizer_type="graph",
        monster_name="Concurrence Titan", monster_title="Scheduler of Critical Paths",
        monster_sprite="titan", monster_color="#8b5cf6", monster_attack="Critical Path Quake",
        monster_quote="Minimum total completion time under dependency graph constraints!",
        description="You are given an integer `n`, which indicates that there are `n` courses labeled from 1 to `n`. You are also given a 2D integer array `relations` where `relations[j] = [prevCoursej, nextCoursej]` and an integer array `time` where `time[i]` denotes months to complete the `(i+1)`-th course. Any number of courses can be taken in parallel if prerequisites are met. Return the minimum number of months needed to complete all the courses.",
        examples=[{"input": "n = 3, relations = [[1,3],[2,3]], time = [3,2,5]", "output": "8"}, {"input": "n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5]", "output": "12"}],
        constraints=["1 <= n <= 50000", "0 <= relations.length <= 50000"],
        function_name="minimumTime",
        starter_code="def minimumTime(n: int, relations: list[list[int]], time: list[int]) -> int:\n    pass\n",
        solution_code="def minimumTime(n: int, relations: list[list[int]], time: list[int]) -> int:\n    from collections import defaultdict, deque\n    adj = defaultdict(list)\n    in_deg = [0] * (n + 1)\n    for u, v in relations:\n        adj[u].append(v)\n        in_deg[v] += 1\n    dp = [0] * (n + 1)\n    q = deque([i for i in range(1, n + 1) if in_deg[i] == 0])\n    for i in q:\n        dp[i] = time[i - 1]\n    while q:\n        u = q.popleft()\n        for v in adj[u]:\n            dp[v] = max(dp[v], dp[u] + time[v - 1])\n            in_deg[v] -= 1\n            if in_deg[v] == 0:\n                q.append(v)\n    return max(dp)\n",
        test_cases=[{"input": [3, [[1, 3], [2, 3]], [3, 2, 5]], "expected": 8}, {"input": [5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5]], "expected": 12}],
        hints=["Topological sort DP: dp[v] = max(dp[v], dp[u] + time[v])."],
        leetcode_id=2050
    ))

    # 81. Build a Matrix With Conditions
    problems.append(make_problem(
        pid="graph-h-build-matrix-with-conditions", title="Build a Matrix With Conditions",
        wing_id="graphs", floor=381, difficulty="hard", visualizer_type="grid",
        monster_name="Orthogonal Lich", monster_title="Weaver of Row and Column Topologies",
        monster_sprite="lich", monster_color="#06b6d4", monster_attack="Orthogonal Grid Bind",
        monster_quote="Matrix satisfying both row and col precedence rules generated!",
        description="You are given a positive integer `k`. You are also given a 2D integer array `rowConditions` and `colConditions`. You want to build a `k x k` matrix that contains each of the numbers from 1 to `k` exactly once (other cells are 0) such that the relative row order matches `rowConditions` and column order matches `colConditions`. Return any valid matrix, or an empty matrix if none exists.",
        examples=[{"input": "k = 3, rowConditions = [[1,2],[3,2]], colConditions = [[2,1],[3,2]]", "output": "[[3,0,0],[0,0,1],[0,2,0]]"}],
        constraints=["2 <= k <= 400"],
        function_name="buildMatrix",
        starter_code="def buildMatrix(k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:\n    pass\n",
        solution_code="def buildMatrix(k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:\n    from collections import defaultdict, deque\n    def topo_sort(edges):\n        adj = defaultdict(list)\n        in_deg = [0] * (k + 1)\n        for u, v in edges:\n            adj[u].append(v)\n            in_deg[v] += 1\n        q = deque([i for i in range(1, k + 1) if in_deg[i] == 0])\n        res = []\n        while q:\n            u = q.popleft()\n            res.append(u)\n            for v in adj[u]:\n                in_deg[v] -= 1\n                if in_deg[v] == 0: q.append(v)\n        return res if len(res) == k else []\n    row_order = topo_sort(rowConditions)\n    col_order = topo_sort(colConditions)\n    if not row_order or not col_order: return []\n    row_pos = {val: i for i, val in enumerate(row_order)}\n    col_pos = {val: i for i, val in enumerate(col_order)}\n    mat = [[0] * k for _ in range(k)]\n    for num in range(1, k + 1):\n        mat[row_pos[num]][col_pos[num]] = num\n    return mat\n",
        test_cases=[{"input": [3, [[1, 2], [3, 2]], [[2, 1], [3, 2]]], "expected": [[0, 0, 1], [3, 0, 0], [0, 2, 0]]}],
        hints=["Independent topological sorts on rows and columns."],
        leetcode_id=2392
    ))

    # 82. Sort Items by Groups Respecting Dependencies
    problems.append(make_problem(
        pid="graph-h-sort-items-by-groups", title="Sort Items by Groups Respecting Dependencies",
        wing_id="graphs", floor=382, difficulty="hard", visualizer_type="graph",
        monster_name="Hierarchical Archon", monster_title="Master of Two-Tier Topological Ordering",
        monster_sprite="boss", monster_color="#ec4899", monster_attack="Two-Tier Decree",
        monster_quote="Nested group-item dependencies resolved topologically!",
        description="There are `n` items each belonging to zero or one of `m` groups. Items that belong to the same group should be adjacent in the sorted array. Dependencies are specified by `beforeItems`. Return a sorted list of items such that all conditions are met, or `[]` if impossible.",
        examples=[{"input": "n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]", "output": "[6,3,4,1,5,2,0,7]"}],
        constraints=["1 <= m <= n <= 30000"],
        function_name="sortItems",
        starter_code="def sortItems(n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:\n    pass\n",
        solution_code="def sortItems(n: int, m: int, group: list[int], beforeItems: list[list[int]]) -> list[int]:\n    from collections import defaultdict, deque\n    # Assign lone items their own unique group\n    next_group = m\n    for i in range(n):\n        if group[i] == -1:\n            group[i] = next_group\n            next_group += 1\n    item_adj = defaultdict(list)\n    item_in = [0] * n\n    group_adj = defaultdict(set)\n    group_in = [0] * next_group\n    for u in range(n):\n        for v in beforeItems[u]:\n            item_adj[v].append(u)\n            item_in[u] += 1\n            if group[u] != group[v]:\n                if group[u] not in group_adj[group[v]]:\n                    group_adj[group[v]].add(group[u])\n                    group_in[group[u]] += 1\n    def topo(nodes, adj, in_deg):\n        q = deque([x for x in nodes if in_deg[x] == 0])\n        res = []\n        while q:\n            curr = q.popleft()\n            res.append(curr)\n            for nxt in adj[curr]:\n                in_deg[nxt] -= 1\n                if in_deg[nxt] == 0: q.append(nxt)\n        return res if len(res) == len(nodes) else []\n    sorted_groups = topo(list(range(next_group)), group_adj, group_in)\n    sorted_items = topo(list(range(n)), item_adj, item_in)\n    if not sorted_groups or not sorted_items: return []\n    group_to_items = defaultdict(list)\n    for item in sorted_items:\n        group_to_items[group[item]].append(item)\n    res = []\n    for g in sorted_groups:\n        res.extend(group_to_items[g])\n    return res\n",
        test_cases=[{"input": [8, 2, [-1, -1, 1, 0, 0, 1, 0, -1], [[], [6], [5], [6], [3, 6], [], [], []]], "expected": [6, 3, 4, 5, 2, 0, 7, 1]}],
        hints=["Two-level topological sort: first sort groups, then sort items within each group."],
        leetcode_id=1203
    ))

    # 83. Minimum Cost to Make at Least One Valid Path in a Grid
    problems.append(make_problem(
        pid="graph-h-min-cost-valid-path-grid", title="Min Cost to Make at Least One Valid Path (0-1 BFS)",
        wing_id="graphs", floor=383, difficulty="hard", visualizer_type="grid",
        monster_name="Conveyor Automaton", monster_title="Overhauler of Misdirected Signs",
        monster_sprite="gargoyle", monster_color="#10b981", monster_attack="Arrow Reversal",
        monster_quote="Minimum arrow modifications to reach bottom-right corner!",
        description="Given an `m x n` grid. Each cell has a sign pointing right (1), left (2), lower (3), or upper (4). In each step you can follow the sign for cost 0, or change the sign for cost 1. Return the minimum cost to make at least one valid path from `(0, 0)` to `(m - 1, n - 1)`.",
        examples=[{"input": "grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]", "output": "3"}, {"input": "grid = [[1,1,3],[3,2,2],[1,1,4]]", "output": "0"}],
        constraints=["1 <= m, n <= 100"],
        function_name="minCost",
        starter_code="def minCost(grid: list[list[int]]) -> int:\n    pass\n",
        solution_code="def minCost(grid: list[list[int]]) -> int:\n    R, C = len(grid), len(grid[0])\n    from collections import deque\n    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]\n    dist = [[float('inf')] * C for _ in range(R)]\n    dist[0][0] = 0\n    dq = deque([(0, 0)])\n    while dq:\n        r, c = dq.popleft()\n        if r == R - 1 and c == C - 1: return dist[r][c]\n        for i, (dr, dc) in enumerate(dirs, 1):\n            nr, nc = r + dr, c + dc\n            if 0 <= nr < R and 0 <= nc < C:\n                w = 0 if grid[r][c] == i else 1\n                if dist[r][c] + w < dist[nr][nc]:\n                    dist[nr][nc] = dist[r][c] + w\n                    if w == 0: dq.appendleft((nr, nc))\n                    else: dq.append((nr, nc))\n    return 0\n",
        test_cases=[{"input": [[[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]], "expected": 3}, {"input": [[[1, 1, 3], [3, 2, 2], [1, 1, 4]]], "expected": 0}],
        hints=["Use 0-1 BFS with a deque: push cost 0 transitions to left, cost 1 transitions to right."],
        leetcode_id=1368
    ))

    # 84. Shortest Path to Get All Keys
    problems.append(make_problem(
        pid="graph-h-shortest-path-all-keys", title="Shortest Path to Get All Keys (Bitmask Maze)",
        wing_id="graphs", floor=384, difficulty="hard", visualizer_type="grid",
        monster_name="Keymaster Behemoth", monster_title="Keeper of Alphabetic Vaults",
        monster_sprite="boss", monster_color="#ef4444", monster_attack="Master Key Smite",
        monster_quote="Least steps to collect all lowercase keys avoiding uppercase doors!",
        description="You are given an `m x n` grid of strings `grid` where '@' is starting point, '.' empty, '#' wall, 'a'-'f' keys, 'A'-'F' locks. Return the lowest number of moves to acquire all keys. If impossible, return -1.",
        examples=[{"input": "grid = [\"@.a..\",\"###.#\",\"b.A.B\"]", "output": "8"}],
        constraints=["1 <= m, n <= 30"],
        function_name="shortestPathAllKeys",
        starter_code="def shortestPathAllKeys(grid: list[str]) -> int:\n    pass\n",
        solution_code="def shortestPathAllKeys(grid: list[str]) -> int:\n    R, C = len(grid), len(grid[0])\n    from collections import deque\n    total_keys = 0\n    sr = sc = 0\n    for r in range(R):\n        for c in range(C):\n            ch = grid[r][c]\n            if ch == '@': sr, sc = r, c\n            elif ch.islower(): total_keys += 1\n    target_mask = (1 << total_keys) - 1\n    q = deque([(sr, sc, 0, 0)])  # (r, c, keys_mask, steps)\n    visited = {(sr, sc, 0)}\n    while q:\n        r, c, mask, d = q.popleft()\n        if mask == target_mask: return d\n        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:\n            nr, nc = r + dr, c + dc\n            if 0 <= nr < R and 0 <= nc < C:\n                ch = grid[nr][nc]\n                if ch == '#': continue\n                if ch.isupper() and not (mask & (1 << (ord(ch) - ord('A')))):\n                    continue\n                nxt_mask = mask\n                if ch.islower():\n                    nxt_mask |= (1 << (ord(ch) - ord('a')))\n                if (nr, nc, nxt_mask) not in visited:\n                    visited.add((nr, nc, nxt_mask))\n                    q.append((nr, nc, nxt_mask, d + 1))\n    return -1\n",
        test_cases=[{"input": [["@.a..", "###.#", "b.A.B"]], "expected": 8}, {"input": [["@..aA", "..B#.", "....b"]], "expected": 6}],
        hints=["State BFS with (r, c, collected_keys_bitmask)."],
        leetcode_id=864
    ))

    # 85. Minimum Weighted Subgraph With the Required Paths
    problems.append(make_problem(
        pid="graph-h-min-subgraph-required-paths", title="Minimum Subgraph with Required Paths (3-way Dijkstra)",
        wing_id="graphs", floor=385, difficulty="hard", visualizer_type="graph",
        monster_name="Tri-Convergent Phantom", monster_title="Meeting Point of Divided Paths",
        monster_sprite="spectre", monster_color="#38bdf8", monster_attack="Trident Convergence",
        monster_quote="Smallest total weight of directed edges containing paths src1->dest and src2->dest!",
        description="You are given an integer `n` and a 2D integer array `edges` where `edges[i] = [fromi, toi, weighti]`. You are also given three distinct integers `src1`, `src2`, and `dest`. Return the minimum weight of a subgraph such that there is a path from `src1` to `dest` and from `src2` to `dest`. If impossible, return -1.",
        examples=[{"input": "n = 6, edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], src1 = 0, src2 = 1, dest = 5", "output": "9"}],
        constraints=["3 <= n <= 100000", "0 <= edges.length <= 100000"],
        function_name="minimumWeight",
        starter_code="def minimumWeight(n: int, edges: list[list[int]], src1: int, src2: int, dest: int) -> int:\n    pass\n",
        solution_code="def minimumWeight(n: int, edges: list[list[int]], src1: int, src2: int, dest: int) -> int:\n    import heapq\n    from collections import defaultdict\n    graph = defaultdict(list)\n    rev_graph = defaultdict(list)\n    for u, v, w in edges:\n        graph[u].append((v, w))\n        rev_graph[v].append((u, w))\n    def dijkstra(start, adj):\n        dist = [float('inf')] * n\n        dist[start] = 0\n        pq = [(0, start)]\n        while pq:\n            d, u = heapq.heappop(pq)\n            if d > dist[u]: continue\n            for v, w in adj[u]:\n                if d + w < dist[v]:\n                    dist[v] = d + w\n                    heapq.heappush(pq, (dist[v], v))\n        return dist\n    d1 = dijkstra(src1, graph)\n    d2 = dijkstra(src2, graph)\n    dd = dijkstra(dest, rev_graph)\n    ans = float('inf')\n    for mid in range(n):\n        if d1[mid] != float('inf') and d2[mid] != float('inf') and dd[mid] != float('inf'):\n            ans = min(ans, d1[mid] + d2[mid] + dd[mid])\n    return ans if ans != float('inf') else -1\n",
        test_cases=[{"input": [6, [[0, 2, 2], [0, 5, 6], [1, 0, 3], [1, 4, 5], [2, 1, 1], [2, 3, 3], [2, 3, 4], [3, 4, 2], [4, 5, 1]], 0, 1, 5], "expected": 9}],
        hints=["Pick an intermediate rendezvous node x. Subgraph weight is dist(src1, x) + dist(src2, x) + rev_dist(dest, x)."],
        leetcode_id=2203
    ))

    return problems
