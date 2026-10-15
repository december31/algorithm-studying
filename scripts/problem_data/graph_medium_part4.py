"""
Graphs Medium Problems - Part 4 (Floors 356 to 370 - 15 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_graph_medium_part4():
    problems = []

    # 56. Count Unreachable Pairs of Nodes
    problems.append(make_problem(
        pid="graph-m-count-unreachable-pairs", title="Count Unreachable Pairs of Nodes",
        wing_id="graphs", floor=356, difficulty="medium", visualizer_type="graph",
        monster_name="Void Severer", monster_title="Tallyer of Disjoint Realms",
        monster_sprite="wraith", monster_color="#8b5cf6", monster_attack="Severing Cleave",
        monster_quote="Total pairs of vertices with no connecting paths counted!",
        description="You are given an integer `n`. There is an undirected graph with `n` nodes, numbered from 0 to `n - 1`. You are given a 2D integer array `edges` where `edges[i] = [ai, bi]`. Return the number of pairs of different nodes that are unreachable from each other.",
        examples=[{"input": "n = 3, edges = [[0,1],[0,2],[1,2]]", "output": "0"}, {"input": "n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]", "output": "14"}],
        constraints=["1 <= n <= 100000", "0 <= edges.length <= 200000"],
        function_name="countPairs",
        starter_code="def countPairs(n: int, edges: list[list[int]]) -> int:\n    pass\n",
        solution_code="def countPairs(n: int, edges: list[list[int]]) -> int:\n    parent = list(range(n))\n    size = [1] * n\n    def find(i):\n        if parent[i] == i: return i\n        parent[i] = find(parent[i])\n        return parent[i]\n    for u, v in edges:\n        ru, rv = find(u), find(v)\n        if ru != rv:\n            parent[ru] = rv\n            size[rv] += size[ru]\n    comp_sizes = [size[i] for i in range(n) if parent[i] == i]\n    ans = 0\n    rem = n\n    for s in comp_sizes:\n        ans += s * (rem - s)\n        rem -= s\n    return ans\n",
        test_cases=[{"input": [3, [[0, 1], [0, 2], [1, 2]]], "expected": 0}, {"input": [7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]], "expected": 14}],
        hints=["Find component sizes using DSU. Sum size * (remaining nodes - size) across components."],
        leetcode_id=2316
    ))

    # 57. Number of Ways to Arrive at Destination
    problems.append(make_problem(
        pid="graph-m-num-ways-arrive-destination", title="Number of Ways to Arrive at Destination",
        wing_id="graphs", floor=357, difficulty="medium", visualizer_type="graph",
        monster_name="Nexus Sovereign", monster_title="Counter of Equidistant Trajectories",
        monster_sprite="boss", monster_color="#38bdf8", monster_attack="Nexus Flash",
        monster_quote="Ways to reach node n - 1 with minimum travel time computed modulo 10^9 + 7!",
        description="You are in a city that consists of `n` intersections numbered from 0 to `n - 1` with bi-directional roads `roads` where `roads[i] = [ui, vi, timei]`. You want to find how many ways there are to travel from intersection 0 to intersection `n - 1` in the shortest amount of time. Return the number of ways modulo `10^9 + 7`.",
        examples=[{"input": "n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]", "output": "4"}],
        constraints=["1 <= n <= 200", "n - 1 <= roads.length <= n * (n - 1) / 2"],
        function_name="countPaths",
        starter_code="def countPaths(n: int, roads: list[list[int]]) -> int:\n    pass\n",
        solution_code="def countPaths(n: int, roads: list[list[int]]) -> int:\n    import heapq\n    from collections import defaultdict\n    MOD = 10**9 + 7\n    graph = defaultdict(list)\n    for u, v, t in roads:\n        graph[u].append((v, t))\n        graph[v].append((u, t))\n    dist = [float('inf')] * n\n    ways = [0] * n\n    dist[0] = 0\n    ways[0] = 1\n    pq = [(0, 0)]\n    while pq:\n        d, u = heapq.heappop(pq)\n        if d > dist[u]: continue\n        for v, t in graph[u]:\n            if d + t < dist[v]:\n                dist[v] = d + t\n                ways[v] = ways[u]\n                heapq.heappush(pq, (dist[v], v))\n            elif d + t == dist[v]:\n                ways[v] = (ways[v] + ways[u]) % MOD\n    return ways[n - 1]\n",
        test_cases=[{"input": [7, [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]], "expected": 4}, {"input": [2, [[1, 0, 10]]], "expected": 1}],
        hints=["Dijkstra tracking both minimum distance and number of shortest paths to each vertex."],
        leetcode_id=1976
    ))

    # 58. Sequence Reconstruction
    problems.append(make_problem(
        pid="graph-m-sequence-reconstruction", title="Sequence Reconstruction (Unique Topological Sort)",
        wing_id="graphs", floor=358, difficulty="medium", visualizer_type="graph",
        monster_name="Linear Arbiter", monster_title="Verifier of Unambiguous Orders",
        monster_sprite="wizard", monster_color="#ec4899", monster_attack="Singular Path Wave",
        monster_quote="Does there exist a unique topological reconstruction of nums?",
        description="You are given an integer array `nums` of length `n` where `nums` is a permutation of integers in the range `[1, n]`. You are also given a 2D integer array `sequences`. Check whether `nums` is the unique shortest supersequence of `sequences`.",
        examples=[{"input": "nums = [1,2,3], sequences = [[1,2],[1,3]]", "output": "False"}, {"input": "nums = [1,2,3], sequences = [[1,2],[2,3]]", "output": "True"}],
        constraints=["n == nums.length", "1 <= n <= 10000"],
        function_name="sequenceReconstruction",
        starter_code="def sequenceReconstruction(nums: list[int], sequences: list[list[int]]) -> bool:\n    pass\n",
        solution_code="def sequenceReconstruction(nums: list[int], sequences: list[list[int]]) -> bool:\n    from collections import defaultdict, deque\n    n = len(nums)\n    adj = defaultdict(set)\n    in_deg = [0] * (n + 1)\n    for seq in sequences:\n        for i in range(len(seq) - 1):\n            u, v = seq[i], seq[i + 1]\n            if 1 <= u <= n and 1 <= v <= n:\n                if v not in adj[u]:\n                    adj[u].add(v)\n                    in_deg[v] += 1\n    q = deque([i for i in range(1, n + 1) if in_deg[i] == 0])\n    res = []\n    while q:\n        if len(q) > 1: return False\n        curr = q.popleft()\n        res.append(curr)\n        for nxt in adj[curr]:\n            in_deg[nxt] -= 1\n            if in_deg[nxt] == 0:\n                q.append(nxt)\n    return res == nums\n",
        test_cases=[{"input": [[1, 2, 3], [[1, 2], [1, 3]]], "expected": False}, {"input": [[1, 2, 3], [[1, 2], [2, 3]]], "expected": True}, {"input": [[1, 2, 3], [[1, 2], [1, 3], [2, 3]]], "expected": True}],
        hints=["During Kahn's topological sort, the queue must never have size greater than 1."],
        leetcode_id=444
    ))

    # 59. Flower Planting With No Adjacent
    problems.append(make_problem(
        pid="graph-m-flower-planting-4-color", title="Garden 4-Coloring with No Adjacent",
        wing_id="graphs", floor=359, difficulty="medium", visualizer_type="graph",
        monster_name="Floral Sylph", monster_title="Harmonizer of Quadrant Blooms",
        monster_sprite="spectre", monster_color="#22c55e", monster_attack="Pollen Swarm",
        monster_quote="4-flower assignment with zero adjacent conflicts completed!",
        description="You have `n` gardens, labeled from 1 to `n`, and an array `paths` where `paths[i] = [x, y]` describes a bidirectional path. Every garden has at most 3 paths coming into or out of it. Choose a flower type from 1 to 4 for each garden such that no two adjacent gardens have the same flower type. Return an array of size `n` representing flower types.",
        examples=[{"input": "n = 3, paths = [[1,2],[2,3],[3,1]]", "output": "[1,2,3]"}],
        constraints=["1 <= n <= 10000", "0 <= paths.length <= 20000"],
        function_name="gardenNoAdj",
        starter_code="def gardenNoAdj(n: int, paths: list[list[int]]) -> list[int]:\n    pass\n",
        solution_code="def gardenNoAdj(n: int, paths: list[list[int]]) -> list[int]:\n    from collections import defaultdict\n    adj = defaultdict(list)\n    for u, v in paths:\n        adj[u].append(v)\n        adj[v].append(u)\n    ans = [0] * n\n    for i in range(1, n + 1):\n        used = {ans[neighbor - 1] for neighbor in adj[i]}\n        for color in range(1, 5):\n            if color not in used:\n                ans[i - 1] = color\n                break\n    return ans\n",
        test_cases=[{"input": [3, [[1, 2], [2, 3], [3, 1]]], "expected": [1, 2, 3]}, {"input": [4, [[1, 2], [3, 4]]], "expected": [1, 2, 1, 2]}],
        hints=["Since each node has at most 3 neighbors, by the Pigeonhole Principle there is always an available color from {1, 2, 3, 4}."],
        leetcode_id=1042
    ))

    # 60. Most Stones Removed with Same Row or Column
    problems.append(make_problem(
        pid="graph-m-remove-stones-row-col", title="Most Stones Removed with Same Row or Col",
        wing_id="graphs", floor=360, difficulty="medium", visualizer_type="graph",
        monster_name="Quarry Behemoth", monster_title="Crusher of Co-linear Monoliths",
        monster_sprite="golem", monster_color="#f59e0b", monster_attack="Megalith Cleave",
        monster_quote="Maximum stones removed leaving 1 per connected coordinate component!",
        description="On a 2D plane, we place `n` stones at some integer coordinate points. Each coordinate point may have at most one stone. A stone can be removed if it shares either the same row or the same column as another stone that has not been removed. Given an array `stones`, return the largest possible number of stones that can be removed.",
        examples=[{"input": "stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]", "output": "5"}, {"input": "stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]", "output": "3"}],
        constraints=["1 <= stones.length <= 1000"],
        function_name="removeStones",
        starter_code="def removeStones(stones: list[list[int]]) -> int:\n    pass\n",
        solution_code="def removeStones(stones: list[list[int]]) -> int:\n    parent = {}\n    def find(x):\n        if parent[x] == x: return x\n        parent[x] = find(parent[x])\n        return parent[x]\n    for r, c in stones:\n        c_key = ~c\n        if r not in parent: parent[r] = r\n        if c_key not in parent: parent[c_key] = c_key\n        parent[find(r)] = find(c_key)\n    roots = {find(x) for x in parent}\n    return len(stones) - len(roots)\n",
        test_cases=[{"input": [[[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]], "expected": 5}, {"input": [[[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]], "expected": 3}],
        hints=["Stones that share a row or col form a connected component. Total removable stones is n minus number of components."],
        leetcode_id=947
    ))

    # 61. Regions Cut By Slashes
    problems.append(make_problem(
        pid="graph-m-regions-cut-by-slashes", title="Regions Cut By Slashes",
        wing_id="graphs", floor=361, difficulty="medium", visualizer_type="grid",
        monster_name="Fracture Drake", monster_title="Divider of Diagonal Subdivisions",
        monster_sprite="dragon", monster_color="#06b6d4", monster_attack="Slash Fracture",
        monster_quote="Number of contiguous regions formed by '/' and '\\' slashes counted!",
        description="An `n x n` grid is composed of `1 x 1` squares where each square consists of `'/'`, `'\\'`, or blank space `' '`. These characters divide the square into contiguous regions. Given the `grid` represented as a string array, return the number of regions.",
        examples=[{"input": "grid = [\" /\",\"/ \"]", "output": "2"}, {"input": "grid = [\" /\",\"  \"]", "output": "1"}],
        constraints=["n == grid.length", "1 <= n <= 30"],
        function_name="regionsBySlashes",
        starter_code="def regionsBySlashes(grid: list[str]) -> int:\n    pass\n",
        solution_code="def regionsBySlashes(grid: list[str]) -> int:\n    n = len(grid)\n    size = 3 * n\n    matrix = [[0] * size for _ in range(size)]\n    for r in range(n):\n        for c in range(n):\n            ch = grid[r][c]\n            if ch == '/':\n                matrix[r * 3][c * 3 + 2] = 1\n                matrix[r * 3 + 1][c * 3 + 1] = 1\n                matrix[r * 3 + 2][c * 3] = 1\n            elif ch == chr(92):\n                matrix[r * 3][c * 3] = 1\n                matrix[r * 3 + 1][c * 3 + 1] = 1\n                matrix[r * 3 + 2][c * 3 + 2] = 1\n    def dfs(r, c):\n        if 0 <= r < size and 0 <= c < size and matrix[r][c] == 0:\n            matrix[r][c] = 1\n            dfs(r + 1, c)\n            dfs(r - 1, c)\n            dfs(r, c + 1)\n            dfs(r, c - 1)\n    regions = 0\n    for r in range(size):\n        for c in range(size):\n            if matrix[r][c] == 0:\n                regions += 1\n                dfs(r, c)\n    return regions\n",
        test_cases=[{"input": [[" /", "/ "]], "expected": 2}, {"input": [[" /", "  "]], "expected": 1}, {"input": [["/" + chr(92), chr(92) + "/"]], "expected": 5}],
        hints=["Upscale each 1x1 cell into a 3x3 pixel matrix and count connected 0-components."],
        leetcode_id=959
    ))

    # 62. Similar String Groups
    problems.append(make_problem(
        pid="graph-m-similar-string-groups", title="Similar String Groups (Connected Components)",
        wing_id="graphs", floor=362, difficulty="medium", visualizer_type="graph",
        monster_name="Anagram Specter", monster_title="Consolidator of 2-Swap Permutations",
        monster_sprite="spectre", monster_color="#6366f1", monster_attack="Permute Pulse",
        monster_quote="Equivalence groups of strings reachable via 2-char swaps determined!",
        description="Two strings `X` and `Y` are similar if we can swap two letters (in different positions) of `X`, so that it equals `Y`. We are given a list `strs` of strings where every string is an anagram of every other string. Return the number of groups of similar strings.",
        examples=[{"input": "strs = [\"tars\",\"rats\",\"arts\",\"star\"]", "output": "2"}, {"input": "strs = [\"omv\",\"ovm\"]", "output": "1"}],
        constraints=["1 <= strs.length <= 300", "1 <= strs[i].length <= 300"],
        function_name="numSimilarGroups",
        starter_code="def numSimilarGroups(strs: list[str]) -> int:\n    pass\n",
        solution_code="def numSimilarGroups(strs: list[str]) -> int:\n    n = len(strs)\n    parent = list(range(n))\n    def find(i):\n        if parent[i] == i: return i\n        parent[i] = find(parent[i])\n        return parent[i]\n    def is_similar(s1, s2):\n        diff = 0\n        for c1, c2 in zip(s1, s2):\n            if c1 != c2:\n                diff += 1\n                if diff > 2: return False\n        return diff == 0 or diff == 2\n    for i in range(n):\n        for j in range(i + 1, n):\n            if is_similar(strs[i], strs[j]):\n                parent[find(i)] = find(j)\n    return len({find(i) for i in range(n)})\n",
        test_cases=[{"input": [["tars", "rats", "arts", "star"]], "expected": 2}, {"input": [["omv", "ovm"]], "expected": 1}],
        hints=["Two anagrams are similar if their Hamming distance is 0 or 2. Connect and count DSU components."],
        leetcode_id=839
    ))

    # 63. Find the City With Smallest Number of Neighbors at a Threshold Distance
    problems.append(make_problem(
        pid="graph-m-city-smallest-neighbors", title="City with Smallest Neighbors within Threshold",
        wing_id="graphs", floor=363, difficulty="medium", visualizer_type="graph",
        monster_name="Isolationist Tyrant", monster_title="Governor of the Remote Frontier",
        monster_sprite="boss", monster_color="#ef4444", monster_attack="Distance Ward",
        monster_quote="City with fewest reachable neighbors within distance threshold selected!",
        description="There are `n` cities numbered from 0 to `n-1`. Given the array `edges` where `edges[i] = [fromi, toi, weighti]` and integer `distanceThreshold`. Return the city with the smallest number of cities that are reachable through some path and whose distance is at most `distanceThreshold`. If there are multiple, return greatest city number.",
        examples=[{"input": "n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4", "output": "3"}],
        constraints=["2 <= n <= 100"],
        function_name="findTheCity",
        starter_code="def findTheCity(n: int, edges: list[list[int]], distanceThreshold: int) -> int:\n    pass\n",
        solution_code="def findTheCity(n: int, edges: list[list[int]], distanceThreshold: int) -> int:\n    dist = [[float('inf')] * n for _ in range(n)]\n    for i in range(n): dist[i][i] = 0\n    for u, v, w in edges:\n        dist[u][v] = w\n        dist[v][u] = w\n    for k in range(n):\n        for i in range(n):\n            for j in range(n):\n                if dist[i][k] + dist[k][j] < dist[i][j]:\n                    dist[i][j] = dist[i][k] + dist[k][j]\n    min_reachable = float('inf')\n    best_city = -1\n    for i in range(n):\n        cnt = sum(1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold)\n        if cnt <= min_reachable:\n            min_reachable = cnt\n            best_city = i\n    return best_city\n",
        test_cases=[{"input": [4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4], "expected": 3}, {"input": [5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2], "expected": 0}],
        hints=["Floyd-Warshall algorithm for all-pairs shortest paths."],
        leetcode_id=1334
    ))

    # 64. All Ancestors of a Node in a Directed Acyclic Graph
    problems.append(make_problem(
        pid="graph-m-all-ancestors-dag", title="All Ancestors of Each Node in DAG",
        wing_id="graphs", floor=364, difficulty="medium", visualizer_type="graph",
        monster_name="Ancestral Spirit", monster_title="Keeper of Lineage Trees",
        monster_sprite="wraith", monster_color="#8b5cf6", monster_attack="Lineage Echo",
        monster_quote="Full list of sorted ancestor nodes for every DAG vertex established!",
        description="You are given a positive integer `n` representing the number of nodes of a Directed Acyclic Graph (DAG) labeled from 0 to `n - 1`. You are also given a 2D integer array `edges` where `edges[i] = [fromi, toi]`. Return a list `answer` of size `n`, where `answer[i]` is the list of ancestors of the `i`-th node, sorted in ascending order.",
        examples=[{"input": "n = 8, edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]", "output": "[[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]"}],
        constraints=["1 <= n <= 1000"],
        function_name="getAncestors",
        starter_code="def getAncestors(n: int, edges: list[list[int]]) -> list[list[int]]:\n    pass\n",
        solution_code="def getAncestors(n: int, edges: list[list[int]]) -> list[list[int]]:\n    from collections import defaultdict\n    adj = defaultdict(list)\n    for u, v in edges:\n        adj[u].append(v)\n    ans = [[] for _ in range(n)]\n    def dfs(curr, ancestor, visited):\n        for nxt in adj[curr]:\n            if nxt not in visited:\n                visited.add(nxt)\n                ans[nxt].append(ancestor)\n                dfs(nxt, ancestor, visited)\n    for i in range(n):\n        dfs(i, i, set())\n    return [sorted(anc) for anc in ans]\n",
        test_cases=[{"input": [8, [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]], "expected": [[], [], [], [0, 1], [0, 2], [0, 1, 3], [0, 1, 2, 3, 4], [0, 1, 2, 3]]}],
        hints=["Run DFS from each node i to mark i as an ancestor for all reachable descendants."],
        leetcode_id=2192
    ))

    # 65. Minimum Fuel Cost to Report to the Capital
    problems.append(make_problem(
        pid="graph-m-min-fuel-cost-capital", title="Minimum Fuel Cost to Report to Capital",
        wing_id="graphs", floor=365, difficulty="medium", visualizer_type="graph",
        monster_name="Fleet Vanguard", monster_title="Consolidator of Carpooling Convoys",
        monster_sprite="gargoyle", monster_color="#10b981", monster_attack="Carpool Rush",
        monster_quote="Minimum fuel liters spent transporting all representatives to node 0!",
        description="There is a tree (a connected undirected graph with no cycles) representing a country with `n` cities and `roads`. City 0 is the capital. There is a representative in every city. There is a car with `seats` capacity in each city. Representatives can carpool. Return the minimum number of liters of fuel needed to bring everyone to the capital.",
        examples=[{"input": "roads = [[0,1],[0,2],[0,3]], seats = 5", "output": "3"}, {"input": "roads = [[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], seats = 2", "output": "7"}],
        constraints=["1 <= n <= 100000", "1 <= seats <= 100000"],
        function_name="minimumFuelCost",
        starter_code="def minimumFuelCost(roads: list[list[int]], seats: int) -> int:\n    pass\n",
        solution_code="def minimumFuelCost(roads: list[list[int]], seats: int) -> int:\n    import math\n    from collections import defaultdict\n    graph = defaultdict(list)\n    for u, v in roads:\n        graph[u].append(v)\n        graph[v].append(u)\n    total_fuel = [0]\n    def dfs(u, p):\n        people = 1\n        for v in graph[u]:\n            if v != p:\n                people += dfs(v, u)\n        if u != 0:\n            total_fuel[0] += math.ceil(people / seats)\n        return people\n    dfs(0, -1)\n    return total_fuel[0]\n",
        test_cases=[{"input": [[[0, 1], [0, 2], [0, 3]], 5], "expected": 3}, {"input": [[[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2], "expected": 7}],
        hints=["DFS from capital 0. For each subtree, liters required along its incoming edge is ceil(subtree_size / seats)."],
        leetcode_id=2477
    ))

    # 66. Loud and Rich
    problems.append(make_problem(
        pid="graph-m-loud-and-rich", title="Loud and Rich (Quiet Person in Wealthy Subgraph)",
        wing_id="graphs", floor=366, difficulty="medium", visualizer_type="graph",
        monster_name="Aristocrat Lich", monster_title="Weigher of Fortunes and Whispers",
        monster_sprite="lich", monster_color="#f59e0b", monster_attack="Golden Silence",
        monster_quote="Quietest person among all equally or wealthier peers identified!",
        description="There is a group of `n` people labeled 0 to `n - 1`. You are given `richer` where `richer[i] = [ai, bi]` indicates that `ai` has more money than `bi`, and `quiet` where `quiet[i]` indicates quietness of person `i`. Return an integer array `answer` where `answer[x]` is the least quiet person among all people who have at least as much money as `x`.",
        examples=[{"input": "richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]", "output": "[5,5,2,5,4,5,6,7]"}],
        constraints=["n == quiet.length", "1 <= n <= 500"],
        function_name="loudAndRich",
        starter_code="def loudAndRich(richer: list[list[int]], quiet: list[int]) -> list[int]:\n    pass\n",
        solution_code="def loudAndRich(richer: list[list[int]], quiet: list[int]) -> list[int]:\n    n = len(quiet)\n    from collections import defaultdict\n    graph = defaultdict(list)\n    for u, v in richer:\n        graph[v].append(u)\n    ans = [-1] * n\n    def dfs(u):\n        if ans[u] != -1: return ans[u]\n        ans[u] = u\n        for v in graph[u]:\n            cand = dfs(v)\n            if quiet[cand] < quiet[ans[u]]:\n                ans[u] = cand\n        return ans[u]\n    for i in range(n):\n        dfs(i)\n    return ans\n",
        test_cases=[{"input": [[[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]], [3, 2, 5, 4, 6, 1, 7, 0]], "expected": [5, 5, 2, 5, 4, 5, 6, 7]}],
        hints=["Memoized DFS traversing directed edges from poorer to richer person."],
        leetcode_id=851
    ))

    # 67. Shortest Path with Alternating Colors
    problems.append(make_problem(
        pid="graph-m-shortest-path-alternating-colors", title="Shortest Path with Alternating Colors",
        wing_id="graphs", floor=367, difficulty="medium", visualizer_type="graph",
        monster_name="Bicolor Sphinx", monster_title="Guardian of Alternating Rainbow Gates",
        monster_sprite="sphinx", monster_color="#ec4899", monster_attack="Prismatic Flux",
        monster_quote="Shortest red-blue alternating step paths to every node mapped!",
        description="You are given an integer `n`, the number of nodes in a directed graph. There are `redEdges` and `blueEdges`. Return an array `answer` of length `n`, where `answer[x]` is the length of the shortest path from node 0 to node `x` such that the edge colors alternate, or -1 if no such path exists.",
        examples=[{"input": "n = 3, redEdges = [[0,1],[1,2]], blueEdges = []", "output": "[0,1,-1]"}, {"input": "n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]", "output": "[0,1,-1]"}],
        constraints=["1 <= n <= 100"],
        function_name="shortestAlternatingPaths",
        starter_code="def shortestAlternatingPaths(n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:\n    pass\n",
        solution_code="def shortestAlternatingPaths(n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:\n    from collections import defaultdict, deque\n    adj = {0: defaultdict(list), 1: defaultdict(list)}\n    for u, v in redEdges: adj[0][u].append(v)\n    for u, v in blueEdges: adj[1][u].append(v)\n    dist = [[float('inf'), float('inf')] for _ in range(n)]\n    dist[0][0] = dist[0][1] = 0\n    q = deque([(0, 0, 0), (0, 1, 0)])  # (u, last_color, steps)\n    while q:\n        u, color, d = q.popleft()\n        next_color = 1 - color\n        for v in adj[next_color][u]:\n            if d + 1 < dist[v][next_color]:\n                dist[v][next_color] = d + 1\n                q.append((v, next_color, d + 1))\n    res = []\n    for i in range(n):\n        m = min(dist[i][0], dist[i][1])\n        res.append(m if m != float('inf') else -1)\n    return res\n",
        test_cases=[{"input": [3, [[0, 1], [1, 2]], []], "expected": [0, 1, -1]}, {"input": [3, [[0, 1]], [[2, 1]]], "expected": [0, 1, -1]}, {"input": [3, [[0, 1]], [[1, 2]]], "expected": [0, 1, 2]}],
        hints=["BFS state is (node, last_edge_color). Explore edges of the opposite color."],
        leetcode_id=1129
    ))

    # 68. Maximum Candies You Can Get from Boxes
    problems.append(make_problem(
        pid="graph-m-max-candies-boxes", title="Maximum Candies You Can Get from Boxes",
        wing_id="graphs", floor=368, difficulty="medium", visualizer_type="graph",
        monster_name="Confection Fiend", monster_title="Opener of Nested Treasure Lockboxes",
        monster_sprite="imp", monster_color="#eab308", monster_attack="Sugar Rush",
        monster_quote="Total candies harvested through discovered keys and openable chests!",
        description="You have `n` boxes labeled from 0 to `n - 1`. You are given `status` (1 = open, 0 = locked), `candies`, `keys`, `containedBoxes`, and `initialBoxes`. You can open an unlocked box or unlock a locked box if you have its key. Return the maximum candies you can collect.",
        examples=[{"input": "status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]", "output": "16"}],
        constraints=["1 <= status.length <= 1000"],
        function_name="maxCandies",
        starter_code="def maxCandies(status: list[int], candies: list[int], keys: list[list[int]], containedBoxes: list[list[int]], initialBoxes: list[int]) -> int:\n    pass\n",
        solution_code="def maxCandies(status: list[int], candies: list[int], keys: list[list[int]], containedBoxes: list[list[int]], initialBoxes: list[int]) -> int:\n    from collections import deque\n    has_box = set(initialBoxes)\n    has_key = set()\n    q = deque([b for b in initialBoxes if status[b] == 1])\n    opened = set()\n    total = 0\n    while q:\n        b = q.popleft()\n        if b in opened: continue\n        opened.add(b)\n        total += candies[b]\n        for k in keys[b]:\n            has_key.add(k)\n            if k in has_box and k not in opened:\n                q.append(k)\n        for cb in containedBoxes[b]:\n            has_box.add(cb)\n            if (status[cb] == 1 or cb in has_key) and cb not in opened:\n                q.append(cb)\n    return total\n",
        test_cases=[{"input": [[1, 0, 1, 0], [7, 5, 4, 100], [[], [], [1], []], [[1, 2], [3], [], []], [0]], "expected": 16}, {"input": [[1, 1, 1], [100, 1, 100], [[], [0, 2], []], [[], [], []], [1]], "expected": 1}],
        hints=["Queue a box as soon as you have BOTH the box and its key (or it was initially open)."],
        leetcode_id=1298
    ))

    # 69. Minimum Spanning Tree Weight
    problems.append(make_problem(
        pid="graph-m-mst-total-weight", title="Minimum Spanning Tree Total Weight (Kruskal)",
        wing_id="graphs", floor=369, difficulty="medium", visualizer_type="graph",
        monster_name="Spanning Titan", monster_title="Binder of Minimal Undirected Trees",
        monster_sprite="titan", monster_color="#38bdf8", monster_attack="Granite Bond",
        monster_quote="Minimal total weight to span all vertices without cycles calculated!",
        description="Given `n` vertices (0 to n - 1) and an undirected weighted edge list `edges` where `edges[i] = [ui, vi, weighti]`, return the total weight of the Minimum Spanning Tree (MST). If the graph is not connected, return -1.",
        examples=[{"input": "n = 4, edges = [[0,1,1],[1,2,2],[2,3,3],[0,3,4],[0,2,5]]", "output": "6"}],
        constraints=["1 <= n <= 1000", "0 <= edges.length <= 5000"],
        function_name="minSpanningTreeWeight",
        starter_code="def minSpanningTreeWeight(n: int, edges: list[list[int]]) -> int:\n    pass\n",
        solution_code="def minSpanningTreeWeight(n: int, edges: list[list[int]]) -> int:\n    if n <= 1: return 0\n    edges.sort(key=lambda x: x[2])\n    parent = list(range(n))\n    def find(i):\n        if parent[i] == i: return i\n        parent[i] = find(parent[i])\n        return parent[i]\n    mst_weight = 0\n    edges_count = 0\n    for u, v, w in edges:\n        ru, rv = find(u), find(v)\n        if ru != rv:\n            parent[ru] = rv\n            mst_weight += w\n            edges_count += 1\n            if edges_count == n - 1: return mst_weight\n    return -1\n",
        test_cases=[{"input": [4, [[0, 1, 1], [1, 2, 2], [2, 3, 3], [0, 3, 4], [0, 2, 5]]], "expected": 6}, {"input": [3, [[0, 1, 5]]], "expected": -1}],
        hints=["Kruskal's algorithm with DSU. Verify n - 1 edges are accepted."],
        leetcode_id=1489
    ))

    # 70. Minimum Degree of a Connected Trio in a Graph
    problems.append(make_problem(
        pid="graph-m-min-trio-degree", title="Minimum Degree of a Connected Trio",
        wing_id="graphs", floor=370, difficulty="medium", visualizer_type="graph",
        monster_name="Triquetra Lich", monster_title="Lord of the 3-Way Cliques",
        monster_sprite="lich", monster_color="#ef4444", monster_attack="Triune Annihilation",
        monster_quote="Trio of mutually connected nodes with minimal external degree found!",
        description="You are given an undirected graph with `n` nodes labeled from 1 to `n` and `edges`. A connected trio is a set of three nodes where there is an edge between every pair. The degree of a connected trio is the number of edges outside the trio incident to any node in the trio. Return the minimum degree of a connected trio in the graph, or -1 if none exists.",
        examples=[{"input": "n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]", "output": "3"}],
        constraints=["2 <= n <= 400", "edges.length <= n * (n - 1) / 2"],
        function_name="minTrioDegree",
        starter_code="def minTrioDegree(n: int, edges: list[list[int]]) -> int:\n    pass\n",
        solution_code="def minTrioDegree(n: int, edges: list[list[int]]) -> int:\n    adj = [[False] * (n + 1) for _ in range(n + 1)]\n    deg = [0] * (n + 1)\n    for u, v in edges:\n        adj[u][v] = adj[v][u] = True\n        deg[u] += 1\n        deg[v] += 1\n    ans = float('inf')\n    for u in range(1, n + 1):\n        for v in range(u + 1, n + 1):\n            if adj[u][v]:\n                for w in range(v + 1, n + 1):\n                    if adj[u][w] and adj[v][w]:\n                        ans = min(ans, deg[u] + deg[v] + deg[w] - 6)\n    return ans if ans != float('inf') else -1\n",
        test_cases=[{"input": [6, [[1, 2], [1, 3], [3, 2], [4, 1], [5, 2], [3, 6]]], "expected": 3}, {"input": [7, [[1, 3], [4, 1], [4, 3], [2, 5], [5, 6], [6, 7], [7, 5], [2, 6]]], "expected": 0}],
        hints=["Iterate all trios (u < v < w). If all three edges exist, external degree is deg[u] + deg[v] + deg[w] - 6."],
        leetcode_id=1761
    ))

    return problems
