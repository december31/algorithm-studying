"""
Graphs Easy Problems (Floors 301-310 - 10 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_graph_easy():
    problems = []

    # 1. Flood Fill
    problems.append(make_problem(
        pid="graph-e-flood-fill", title="Flood Fill Pixel Canvas",
        wing_id="graphs", floor=301, difficulty="easy", visualizer_type="grid",
        monster_name="Slime Ooze", monster_title="Spreader of Corrosive Pigment",
        monster_sprite="slime", monster_color="#10b981", monster_attack="Pigment Surge",
        monster_quote="All 4-directionally connected matching pixels transformed!",
        description="An image is represented by an `m x n` integer grid `image` where `image[i][j]` represents the pixel value. You are also given three integers `sr`, `sc`, and `color`. Perform a flood fill on the image starting from the pixel `image[sr][sc]`. Change the color of the starting pixel and all adjacent pixels of the same starting color.",
        examples=[{"input": "image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2", "output": "[[2,2,2],[2,2,0],[2,0,1]]"}],
        constraints=["1 <= m, n <= 50", "0 <= image[i][j], color < 65536"],
        function_name="floodFill",
        starter_code="def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:\n    pass\n",
        solution_code="def floodFill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:\n    orig = image[sr][sc]\n    if orig == color: return image\n    R, C = len(image), len(image[0])\n    def dfs(r, c):\n        if 0 <= r < R and 0 <= c < C and image[r][c] == orig:\n            image[r][c] = color\n            dfs(r + 1, c)\n            dfs(r - 1, c)\n            dfs(r, c + 1)\n            dfs(r, c - 1)\n    dfs(sr, sc)\n    return image\n",
        test_cases=[{"input": [[[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2], "expected": [[2, 2, 2], [2, 2, 0], [2, 0, 1]]}, {"input": [[[0, 0, 0], [0, 0, 0]], 0, 0, 0], "expected": [[0, 0, 0], [0, 0, 0]]}],
        hints=["Use DFS or BFS. Guard against the infinite recursion case where original color equals target color."],
        leetcode_id=733
    ))

    # 2. Island Perimeter
    problems.append(make_problem(
        pid="graph-e-island-perimeter", title="Island Coastline Perimeter",
        wing_id="graphs", floor=302, difficulty="easy", visualizer_type="grid",
        monster_name="Reef Lurker", monster_title="Surveyor of Submerged Boundaries",
        monster_sprite="goblin", monster_color="#3b82f6", monster_attack="Tidal Erosion",
        monster_quote="Perimeter length along land-water edges measured!",
        description="You are given `row x col` `grid` representing a map where `grid[i][j] = 1` represents land and `grid[i][j] = 0` represents water. Grid cells are connected horizontally/vertically. The grid is completely surrounded by water. There is exactly one island. Determine the perimeter of the island.",
        examples=[{"input": "grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]", "output": "16"}],
        constraints=["1 <= row, col <= 100", "grid[i][j] is 0 or 1"],
        function_name="islandPerimeter",
        starter_code="def islandPerimeter(grid: list[list[int]]) -> int:\n    pass\n",
        solution_code="def islandPerimeter(grid: list[list[int]]) -> int:\n    ans = 0\n    R, C = len(grid), len(grid[0])\n    for r in range(R):\n        for c in range(C):\n            if grid[r][c] == 1:\n                ans += 4\n                if r > 0 and grid[r - 1][c] == 1: ans -= 2\n                if c > 0 and grid[r][c - 1] == 1: ans -= 2\n    return ans\n",
        test_cases=[{"input": [[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]], "expected": 16}, {"input": [[[1]]], "expected": 4}, {"input": [[[1, 0]]], "expected": 4}],
        hints=["Each land cell adds 4 edges, minus 2 for every adjacent neighbor sharing an edge."],
        leetcode_id=463
    ))

    # 3. Find the Town Judge
    problems.append(make_problem(
        pid="graph-e-find-town-judge", title="Find the Town Judge",
        wing_id="graphs", floor=303, difficulty="easy", visualizer_type="graph",
        monster_name="Shadow Magistrate", monster_title="Unanimous Arbiter of Trust",
        monster_sprite="ghost", monster_color="#8b5cf6", monster_attack="Verdict of Silence",
        monster_quote="The sole citizen trusted by all who trusts none uncovered!",
        description="In a town of `n` people labeled `1` to `n`, there is a rumor that one of these people is secretly the town judge. If the judge exists: 1. The town judge trusts nobody. 2. Everybody else trusts the town judge. 3. There is exactly one person that satisfies properties 1 and 2. Given `trust` array where `trust[i] = [ai, bi]`, return the label of the town judge if they exist, or `-1`.",
        examples=[{"input": "n = 2, trust = [[1,2]]", "output": "2"}, {"input": "n = 3, trust = [[1,3],[2,3]]", "output": "3"}, {"input": "n = 3, trust = [[1,3],[2,3],[3,1]]", "output": "-1"}],
        constraints=["1 <= n <= 1000", "0 <= trust.length <= 10000"],
        function_name="findJudge",
        starter_code="def findJudge(n: int, trust: list[list[int]]) -> int:\n    pass\n",
        solution_code="def findJudge(n: int, trust: list[list[int]]) -> int:\n    net_trust = [0] * (n + 1)\n    for a, b in trust:\n        net_trust[a] -= 1\n        net_trust[b] += 1\n    for i in range(1, n + 1):\n        if net_trust[i] == n - 1:\n            return i\n    return -1\n",
        test_cases=[{"input": [2, [[1, 2]]], "expected": 2}, {"input": [3, [[1, 3], [2, 3]]], "expected": 3}, {"input": [3, [[1, 3], [2, 3], [3, 1]]], "expected": -1}],
        hints=["Track in-degree minus out-degree for each person. The judge must have net degree n - 1."],
        leetcode_id=997
    ))

    # 4. Find if Path Exists in Graph
    problems.append(make_problem(
        pid="graph-e-path-exists-in-graph", title="Find if Path Exists in Graph",
        wing_id="graphs", floor=304, difficulty="easy", visualizer_type="graph",
        monster_name="Wandering Imp", monster_title="Strider of Connected Trails",
        monster_sprite="imp", monster_color="#f59e0b", monster_attack="Trail Snare",
        monster_quote="Connectivity between source and destination verified!",
        description="There is a bi-directional graph with `n` vertices, where each vertex is labeled from `0` to `n - 1`. Given a 2D integer array `edges` where each `edges[i] = [ui, vi]`, determine if there is a valid path that exists from `source` to `destination`.",
        examples=[{"input": "n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2", "output": "True"}],
        constraints=["1 <= n <= 200000", "0 <= edges.length <= 200000"],
        function_name="validPath",
        starter_code="def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:\n    pass\n",
        solution_code="def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:\n    if source == destination: return True\n    parent = list(range(n))\n    def find(i):\n        if parent[i] == i: return i\n        parent[i] = find(parent[i])\n        return parent[i]\n    for u, v in edges:\n        parent[find(u)] = find(v)\n    return find(source) == find(destination)\n",
        test_cases=[{"input": [3, [[0, 1], [1, 2], [2, 0]], 0, 2], "expected": True}, {"input": [6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5], "expected": False}],
        hints=["Disjoint Set Union (Union-Find) or BFS/DFS determines if source and destination share a component."],
        leetcode_id=1971
    ))

    # 5. Center of Star Graph
    problems.append(make_problem(
        pid="graph-e-center-star-graph", title="Find Center of Star Graph",
        wing_id="graphs", floor=305, difficulty="easy", visualizer_type="graph",
        monster_name="Astral Core", monster_title="Nexus of Radiant Edges",
        monster_sprite="spectre", monster_color="#ec4899", monster_attack="Star Flare",
        monster_quote="Universal hub node connected to all other nodes identified!",
        description="There is an undirected star graph consisting of `n` nodes labeled from `1` to `n`. A star graph is a graph where there is one center node and exactly `n - 1` edges that connect the center node with every other node. Given the 2D integer array `edges` where each `edges[i] = [ui, vi]`, return the center of the given star graph.",
        examples=[{"input": "edges = [[1,2],[2,3],[4,2]]", "output": "2"}, {"input": "edges = [[1,2],[5,1],[1,3],[1,4]]", "output": "1"}],
        constraints=["3 <= n <= 100000", "edges.length == n - 1"],
        function_name="findCenter",
        starter_code="def findCenter(edges: list[list[int]]) -> int:\n    pass\n",
        solution_code="def findCenter(edges: list[list[int]]) -> int:\n    if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:\n        return edges[0][0]\n    return edges[0][1]\n",
        test_cases=[{"input": [[[1, 2], [2, 3], [4, 2]]], "expected": 2}, {"input": [[[1, 2], [5, 1], [1, 3], [1, 4]]], "expected": 1}],
        hints=["The center node must appear in every edge, so it appears in both the first and second edge."],
        leetcode_id=1791
    ))

    # 6. Count Connected Components Count for Matrix Graph
    problems.append(make_problem(
        pid="graph-e-count-isolated-nodes", title="Count Isolated Vertices",
        wing_id="graphs", floor=306, difficulty="easy", visualizer_type="graph",
        monster_name="Solitary Wraith", monster_title="Dweller in Severed Silence",
        monster_sprite="wraith", monster_color="#94a3b8", monster_attack="Isolation Chill",
        monster_quote="Vertices with degree zero tallied!",
        description="Given an integer `n` representing nodes labeled `0` to `n - 1`, and a list of undirected `edges`, return the number of isolated vertices (nodes having a degree of 0).",
        examples=[{"input": "n = 5, edges = [[0,1],[1,2]]", "output": "2"}],
        constraints=["1 <= n <= 1000", "0 <= edges.length <= 5000"],
        function_name="countIsolatedVertices",
        starter_code="def countIsolatedVertices(n: int, edges: list[list[int]]) -> int:\n    pass\n",
        solution_code="def countIsolatedVertices(n: int, edges: list[list[int]]) -> int:\n    deg = [0] * n\n    for u, v in edges:\n        deg[u] += 1\n        deg[v] += 1\n    return sum(1 for d in deg if d == 0)\n",
        test_cases=[{"input": [5, [[0, 1], [1, 2]]], "expected": 2}, {"input": [4, [[0, 1], [2, 3]]], "expected": 0}, {"input": [3, []], "expected": 3}],
        hints=["Count degrees for each node from 0 to n - 1."],
        leetcode_id=323
    ))

    # 7. Check if Directed Graph has Self Loop
    problems.append(make_problem(
        pid="graph-e-has-self-loop", title="Detect Self-Loops in Directed Graph",
        wing_id="graphs", floor=307, difficulty="easy", visualizer_type="graph",
        monster_name="Ouroboros Worm", monster_title="Devourer of Its Own Tail",
        monster_sprite="skeleton", monster_color="#ef4444", monster_attack="Loop Fang",
        monster_quote="Self-directed edge (u, u) found!",
        description="Given a list of directed `edges` where each edge is represented as `[u, v]`, return `True` if any edge forms a self-loop (an edge connecting a vertex to itself), or `False` otherwise.",
        examples=[{"input": "edges = [[0,1],[1,2],[2,2]]", "output": "True"}, {"input": "edges = [[0,1],[1,2],[2,0]]", "output": "False"}],
        constraints=["1 <= edges.length <= 1000"],
        function_name="hasSelfLoop",
        starter_code="def hasSelfLoop(edges: list[list[int]]) -> bool:\n    pass\n",
        solution_code="def hasSelfLoop(edges: list[list[int]]) -> bool:\n    return any(u == v for u, v in edges)\n",
        test_cases=[{"input": [[[0, 1], [1, 2], [2, 2]]], "expected": True}, {"input": [[[0, 1], [1, 2], [2, 0]]], "expected": False}],
        hints=["A self loop simply means u == v in edge [u, v]."],
        leetcode_id=0
    ))

    # 8. Maximum Degree of Node
    problems.append(make_problem(
        pid="graph-e-max-node-degree", title="Maximum Vertex Degree in Graph",
        wing_id="graphs", floor=308, difficulty="easy", visualizer_type="graph",
        monster_name="Hydra Sentinel", monster_title="Bearer of Boundless Tendrils",
        monster_sprite="gargoyle", monster_color="#06b6d4", monster_attack="Tendril Lash",
        monster_quote="The maximum degree among all graph nodes computed!",
        description="Given an integer `n` (the number of vertices from 0 to n - 1) and a list of undirected `edges`, return the maximum vertex degree in the graph.",
        examples=[{"input": "n = 4, edges = [[0,1],[0,2],[0,3]]", "output": "3"}],
        constraints=["1 <= n <= 1000", "0 <= edges.length <= 5000"],
        function_name="maxDegree",
        starter_code="def maxDegree(n: int, edges: list[list[int]]) -> int:\n    pass\n",
        solution_code="def maxDegree(n: int, edges: list[list[int]]) -> int:\n    if n == 0: return 0\n    deg = [0] * n\n    for u, v in edges:\n        deg[u] += 1\n        deg[v] += 1\n    return max(deg) if deg else 0\n",
        test_cases=[{"input": [4, [[0, 1], [0, 2], [0, 3]]], "expected": 3}, {"input": [3, [[0, 1]]], "expected": 1}, {"input": [2, []], "expected": 0}],
        hints=["Accumulate incident edges for each vertex."],
        leetcode_id=0
    ))

    # 9. Verify Bipartite 2-Coloring on Tree
    problems.append(make_problem(
        pid="graph-e-is-tree-bipartite", title="Tree Always Bipartite Validation",
        wing_id="graphs", floor=309, difficulty="easy", visualizer_type="graph",
        monster_name="Dual Shade", monster_title="Alternating Weaver of Black and White",
        monster_sprite="wraith", monster_color="#6366f1", monster_attack="Dichotomy Wave",
        monster_quote="All trees are bipartite with 2-coloring verified!",
        description="Given an undirected tree represented as `n` vertices (0 to n - 1) and `edges` (length n - 1), return a 2-coloring array `colors` of length `n` containing values `0` and `1` such that no adjacent nodes share the same color. Root node 0 should be colored `0`.",
        examples=[{"input": "n = 3, edges = [[0,1],[1,2]]", "output": "[0,1,0]"}],
        constraints=["1 <= n <= 1000", "edges.length == n - 1"],
        function_name="colorTreeBipartite",
        starter_code="def colorTreeBipartite(n: int, edges: list[list[int]]) -> list[int]:\n    pass\n",
        solution_code="def colorTreeBipartite(n: int, edges: list[list[int]]) -> list[int]:\n    from collections import defaultdict, deque\n    adj = defaultdict(list)\n    for u, v in edges:\n        adj[u].append(v)\n        adj[v].append(u)\n    color = [-1] * n\n    color[0] = 0\n    q = deque([0])\n    while q:\n        curr = q.popleft()\n        for nxt in adj[curr]:\n            if color[nxt] == -1:\n                color[nxt] = 1 - color[curr]\n                q.append(nxt)\n    return color\n",
        test_cases=[{"input": [3, [[0, 1], [1, 2]]], "expected": [0, 1, 0]}, {"input": [4, [[0, 1], [0, 2], [0, 3]]], "expected": [0, 1, 1, 1]}],
        hints=["A BFS from node 0 assigns alternate 0/1 colors to adjacent levels."],
        leetcode_id=785
    ))

    # 10. Check if All Nodes Have Even Degree (Eulerian Circuit Precondition)
    problems.append(make_problem(
        pid="graph-e-all-even-degrees", title="Eulerian Cycle Precondition Check",
        wing_id="graphs", floor=310, difficulty="easy", visualizer_type="graph",
        monster_name="Ring Keeper", monster_title="Guardian of Closed Loops",
        monster_sprite="boss", monster_color="#f97316", monster_attack="Loop Convergence",
        monster_quote="Eulerian degree condition checked across all graph vertices!",
        description="Given `n` vertices (0 to n - 1) and an undirected edge list `edges`, determine whether all vertices in the graph have an even degree. (This is a necessary condition for an undirected graph to contain an Eulerian circuit).",
        examples=[{"input": "n = 3, edges = [[0,1],[1,2],[2,0]]", "output": "True"}, {"input": "n = 3, edges = [[0,1],[1,2]]", "output": "False"}],
        constraints=["1 <= n <= 1000", "0 <= edges.length <= 5000"],
        function_name="allEvenDegrees",
        starter_code="def allEvenDegrees(n: int, edges: list[list[int]]) -> bool:\n    pass\n",
        solution_code="def allEvenDegrees(n: int, edges: list[list[int]]) -> bool:\n    deg = [0] * n\n    for u, v in edges:\n        deg[u] += 1\n        deg[v] += 1\n    return all(d % 2 == 0 for d in deg)\n",
        test_cases=[{"input": [3, [[0, 1], [1, 2], [2, 0]]], "expected": True}, {"input": [3, [[0, 1], [1, 2]]], "expected": False}],
        hints=["Check if degree % 2 == 0 for every vertex 0 through n - 1."],
        leetcode_id=0
    ))

    return problems
