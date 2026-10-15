"""
Graphs Hard Problems - Part 2 (Floors 386 to 400 - 15 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_graph_hard_part2():
    problems = []

    # 86. Longest Increasing Path in a Matrix
    problems.append(make_problem(
        pid="graph-h-longest-increasing-path-matrix", title="Longest Increasing Path in Matrix",
        wing_id="graphs", floor=386, difficulty="hard", visualizer_type="grid",
        monster_name="Ascendant Behemoth", monster_title="Ascender of Monotonic Summits",
        monster_sprite="boss", monster_color="#8b5cf6", monster_attack="Ascension Surge",
        monster_quote="Maximum length of strictly increasing continuous grid path found!",
        description="Given an `m x n` integers matrix, return the length of the longest increasing path in matrix. From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or outside the boundary.",
        examples=[{"input": "matrix = [[9,9,4],[6,6,8],[2,1,1]]", "output": "4"}, {"input": "matrix = [[3,4,5],[3,2,6],[2,2,1]]", "output": "4"}],
        constraints=["1 <= m, n <= 200"],
        function_name="longestIncreasingPath",
        starter_code="def longestIncreasingPath(matrix: list[list[int]]) -> int:\n    pass\n",
        solution_code="def longestIncreasingPath(matrix: list[list[int]]) -> int:\n    if not matrix: return 0\n    R, C = len(matrix), len(matrix[0])\n    memo = {}\n    def dfs(r, c):\n        if (r, c) in memo: return memo[(r, c)]\n        best = 1\n        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:\n            nr, nc = r + dr, c + dc\n            if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] > matrix[r][c]:\n                best = max(best, 1 + dfs(nr, nc))\n        memo[(r, c)] = best\n        return best\n    return max(dfs(r, c) for r in range(R) for c in range(C))\n",
        test_cases=[{"input": [[[9, 9, 4], [6, 6, 8], [2, 1, 1]]], "expected": 4}, {"input": [[[3, 4, 5], [3, 2, 6], [2, 2, 1]]], "expected": 4}, {"input": [[[1]]], "expected": 1}],
        hints=["Since strictly increasing moves cannot form cycles, this is a DAG. Use DFS with memoization."],
        leetcode_id=329
    ))

    # 87. Word Ladder II
    problems.append(make_problem(
        pid="graph-h-word-ladder-ii-all-chains", title="Word Ladder II (All Shortest Transformation Chains)",
        wing_id="graphs", floor=387, difficulty="hard", visualizer_type="graph",
        monster_name="Polyglot Hydra", monster_title="Weaver of All Optimal Lexical Bridges",
        monster_sprite="manticore", monster_color="#ec4899", monster_attack="Mutation Tempest",
        monster_quote="Every minimal-length transformation chain from beginWord to endWord assembled!",
        description="A transformation sequence from `beginWord` to `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that every adjacent pair differs by a single letter. Given `beginWord`, `endWord` and `wordList`, return all the shortest transformation sequences from `beginWord` to `endWord` in lexicographical order.",
        examples=[{"input": "beginWord = \"hit\", endWord = \"cog\", wordList = [\"hot\",\"dot\",\"dog\",\"lot\",\"log\",\"cog\"]", "output": "[[\"hit\",\"hot\",\"dot\",\"dog\",\"cog\"],[\"hit\",\"hot\",\"lot\",\"log\",\"cog\"]]"}],
        constraints=["1 <= beginWord.length <= 5", "1 <= wordList.length <= 500"],
        function_name="findLadders",
        starter_code="def findLadders(beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:\n    pass\n",
        solution_code="def findLadders(beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:\n    word_set = set(wordList)\n    if endWord not in word_set: return []\n    from collections import defaultdict, deque\n    parents = defaultdict(set)\n    dist = {beginWord: 0}\n    q = deque([beginWord])\n    found = False\n    while q and not found:\n        for _ in range(len(q)):\n            w = q.popleft()\n            if w == endWord: found = True\n            for i in range(len(w)):\n                for c in 'abcdefghijklmnopqrstuvwxyz':\n                    nxt = w[:i] + c + w[i+1:]\n                    if nxt in word_set:\n                        if nxt not in dist:\n                            dist[nxt] = dist[w] + 1\n                            parents[nxt].add(w)\n                            q.append(nxt)\n                        elif dist[nxt] == dist[w] + 1:\n                            parents[nxt].add(w)\n    if not found: return []\n    res = []\n    def backtrack(curr, path):\n        if curr == beginWord:\n            res.append(path[::-1])\n            return\n        for p in parents[curr]:\n            backtrack(p, path + [p])\n    backtrack(endWord, [endWord])\n    return sorted(res)\n",
        test_cases=[{"input": ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]], "expected": [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]}, {"input": ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]], "expected": []}],
        hints=["Use level-by-level BFS to construct DAG of predecessor pointers, then backtrack from endWord."],
        leetcode_id=126
    ))

    # 88. Minimize Malware Spread
    problems.append(make_problem(
        pid="graph-h-minimize-malware-spread", title="Minimize Malware Spread (DSU Component Size)",
        wing_id="graphs", floor=388, difficulty="hard", visualizer_type="graph",
        monster_name="Plague Overlord", monster_title="Infector of Isolated Networks",
        monster_sprite="lich", monster_color="#ef4444", monster_attack="Malware Inoculation",
        monster_quote="Initial virus node chosen whose removal saves largest component!",
        description="You are given a network of `n` nodes represented by an `n x n` adjacency matrix `graph`. An initial list of infected nodes `initial` is given. If a node is infected, all nodes in its component become infected. Return the node from `initial` that, when removed, minimizes the total infected count. If multiple nodes save the same count, return the one with the smallest index.",
        examples=[{"input": "graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]", "output": "0"}, {"input": "graph = [[1,0,0],[0,1,0],[0,0,1]], initial = [0,2]", "output": "0"}],
        constraints=["1 <= graph.length <= 300"],
        function_name="minMalwareSpread",
        starter_code="def minMalwareSpread(graph: list[list[int]], initial: list[int]) -> int:\n    pass\n",
        solution_code="def minMalwareSpread(graph: list[list[int]], initial: list[int]) -> int:\n    n = len(graph)\n    parent = list(range(n))\n    size = [1] * n\n    def find(i):\n        if parent[i] == i: return i\n        parent[i] = find(parent[i])\n        return parent[i]\n    for i in range(n):\n        for j in range(i + 1, n):\n            if graph[i][j] == 1:\n                ri, rj = find(i), find(j)\n                if ri != rj:\n                    parent[ri] = rj\n                    size[rj] += size[ri]\n    from collections import Counter\n    initial.sort()\n    infected_count = Counter(find(i) for i in initial)\n    best_node = initial[0]\n    max_saved = -1\n    for node in initial:\n        r = find(node)\n        if infected_count[r] == 1:\n            if size[r] > max_saved:\n                max_saved = size[r]\n                best_node = node\n    return best_node\n",
        test_cases=[{"input": [[[1, 1, 0], [1, 1, 0], [0, 0, 1]], [0, 1]], "expected": 0}, {"input": [[[1, 0, 0], [0, 1, 0], [0, 0, 1]], [0, 2]], "expected": 0}],
        hints=["A component is only saved if exactly one infected node belongs to it. Pick the node in the largest such component."],
        leetcode_id=924
    ))

    # 89. Minimize Malware Spread II
    problems.append(make_problem(
        pid="graph-h-minimize-malware-spread-ii", title="Minimize Malware Spread II (Node Deletion)",
        wing_id="graphs", floor=389, difficulty="hard", visualizer_type="graph",
        monster_name="Quarantine Warden", monster_title="Physically Severing Infected Relays",
        monster_sprite="gargoyle", monster_color="#f59e0b", monster_attack="Total Quarantine",
        monster_quote="Node completely deleted from network to minimize infection spread!",
        description="In this variation, when a node from `initial` is removed, it is completely removed from the graph along with all its incident edges. Return the node that minimizes total infected nodes.",
        examples=[{"input": "graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]", "output": "0"}],
        constraints=["1 <= graph.length <= 300"],
        function_name="minMalwareSpreadII",
        starter_code="def minMalwareSpreadII(graph: list[list[int]], initial: list[int]) -> int:\n    pass\n",
        solution_code="def minMalwareSpreadII(graph: list[list[int]], initial: list[int]) -> int:\n    n = len(graph)\n    from collections import deque\n    initial_set = set(initial)\n    best_node = min(initial)\n    min_infected = float('inf')\n    for candidate in sorted(initial):\n        # BFS to count infected without candidate\n        infected = set(initial) - {candidate}\n        q = deque(list(infected))\n        visited = set(infected)\n        while q:\n            u = q.popleft()\n            for v in range(n):\n                if v != candidate and graph[u][v] == 1 and v not in visited:\n                    visited.add(v)\n                    q.append(v)\n        if len(visited) < min_infected:\n            min_infected = len(visited)\n            best_node = candidate\n    return best_node\n",
        test_cases=[{"input": [[[1, 1, 0], [1, 1, 0], [0, 0, 1]], [0, 1]], "expected": 0}, {"input": [[[1, 1, 0], [1, 1, 1], [0, 1, 1]], [0, 1]], "expected": 1}],
        hints=["Since n <= 300, simulate removing each node from initial and run BFS."],
        leetcode_id=928
    ))

    # 90. Cracking the Safe
    problems.append(make_problem(
        pid="graph-h-cracking-the-safe", title="Cracking the Safe (De Bruijn Euler Walk)",
        wing_id="graphs", floor=390, difficulty="hard", visualizer_type="graph",
        monster_name="Vault Sovereign", monster_title="Opener of De Bruijn Torus Codes",
        monster_sprite="demon", monster_color="#38bdf8", monster_attack="Vault Breaker",
        monster_quote="Shortest string containing all k^n combinations of length n constructed!",
        description="There is a safe protected by a password with `n` digits where each digit is one of `k` digits: `0, 1, ..., k - 1`. The safe unlocks if the password is entered as a substring of recent keystrokes. Return any sequence of keystrokes of minimum length that is guaranteed to unlock the safe.",
        examples=[{"input": "n = 1, k = 2", "output": "\"10\""}, {"input": "n = 2, k = 2", "output": "\"01100\""}],
        constraints=["1 <= n <= 4", "1 <= k <= 10", "k^n <= 4096"],
        function_name="crackSafe",
        starter_code="def crackSafe(n: int, k: int) -> str:\n    pass\n",
        solution_code="def crackSafe(n: int, k: int) -> str:\n    if n == 1:\n        return \"\".join(str(i) for i in range(k))\n    visited = set()\n    res = []\n    def dfs(node):\n        for x in range(k):\n            edge = node + str(x)\n            if edge not in visited:\n                visited.add(edge)\n                dfs(edge[1:])\n                res.append(str(x))\n    start = \"0\" * (n - 1)\n    dfs(start)\n    return start + \"\".join(res[::-1])\n",
        test_cases=[{"input": [1, 2], "expected": "01"}, {"input": [2, 2], "expected": "00110"}],
        hints=["Eulerian circuit on De Bruijn graph where nodes are prefixes of length n-1 and edges are transitions."],
        leetcode_id=753
    ))

    # 91. Check if There is a Valid Path in a Grid
    problems.append(make_problem(
        pid="graph-h-valid-path-pipe-grid", title="Valid Path in Pipe Grid",
        wing_id="graphs", floor=391, difficulty="hard", visualizer_type="grid",
        monster_name="Plumber Specter", monster_title="Connector of Sealed Pipelines",
        monster_sprite="spectre", monster_color="#06b6d4", monster_attack="Pipe Rupture",
        monster_quote="Continuous valid pipeline connecting (0, 0) to (m-1, n-1) checked!",
        description="Given an `m x n` grid of street pieces (1 to 6). Determine if there is a valid path from the top-left cell `(0, 0)` to the bottom-right cell `(m - 1, n - 1)` such that all pipes along the path connect mutually.",
        examples=[{"input": "grid = [[2,4,3],[6,5,2]]", "output": "True"}, {"input": "grid = [[1,2,1],[1,2,1]]", "output": "False"}],
        constraints=["1 <= m, n <= 300"],
        function_name="hasValidPath",
        starter_code="def hasValidPath(grid: list[list[int]]) -> bool:\n    pass\n",
        solution_code="def hasValidPath(grid: list[list[int]]) -> bool:\n    R, C = len(grid), len(grid[0])\n    # Dirs: 0=up, 1=down, 2=left, 3=right\n    pipe = {\n        1: {2: (0, -1, 3), 3: (0, 1, 2)},\n        2: {0: (-1, 0, 1), 1: (1, 0, 0)},\n        3: {2: (0, -1, 3), 1: (1, 0, 0)},\n        4: {3: (0, 1, 2), 1: (1, 0, 0)},\n        5: {2: (0, -1, 3), 0: (-1, 0, 1)},\n        6: {3: (0, 1, 2), 0: (-1, 0, 1)}\n    }\n    visited = [[False] * C for _ in range(R)]\n    from collections import deque\n    q = deque([(0, 0)])\n    visited[0][0] = True\n    while q:\n        r, c = q.popleft()\n        if r == R - 1 and c == C - 1: return True\n        for dir_out, (dr, dc, req_in) in pipe[grid[r][c]].items():\n            nr, nc = r + dr, c + dc\n            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:\n                if req_in in pipe[grid[nr][nc]]:\n                    visited[nr][nc] = True\n                    q.append((nr, nc))\n    return False\n",
        test_cases=[{"input": [[[2, 4, 3], [6, 5, 2]]], "expected": True}, {"input": [[[1, 2, 1], [1, 2, 1]]], "expected": False}],
        hints=["Ensure mutual connectivity: current pipe can exit in direction d, and next pipe has an opening facing -d."],
        leetcode_id=1391
    ))

    # 92. Contain Virus
    problems.append(make_problem(
        pid="graph-h-contain-virus", title="Contain Virus (Quarantine Firewall Walls)",
        wing_id="graphs", floor=392, difficulty="hard", visualizer_type="grid",
        monster_name="Quarantine Sentinel", monster_title="Builder of Antiviral Firewalls",
        monster_sprite="golem", monster_color="#ef4444", monster_attack="Firewall Barrier",
        monster_quote="Number of firewall sections erected to neutralize pandemic outbreaks!",
        description="A virus is spreading in an `m x n` grid where 0 is uninfected and 1 is infected. Each day, you can install firewall walls around the single infected region that threatens the most uninfected cells. Uncontained regions then expand into adjacent uninfected cells. Return the number of walls installed until the virus is completely contained.",
        examples=[{"input": "isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]", "output": "10"}],
        constraints=["1 <= m, n <= 50"],
        function_name="containVirus",
        starter_code="def containVirus(isInfected: list[list[int]]) -> int:\n    pass\n",
        solution_code="def containVirus(isInfected: list[list[int]]) -> int:\n    R, C = len(isInfected), len(isInfected[0])\n    def get_regions():\n        visited = set()\n        regions = []\n        for r in range(R):\n            for c in range(C):\n                if isInfected[r][c] == 1 and (r, c) not in visited:\n                    cells = set()\n                    threatened = set()\n                    walls = 0\n                    stack = [(r, c)]\n                    visited.add((r, c))\n                    while stack:\n                        cr, cc = stack.pop()\n                        cells.add((cr, cc))\n                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:\n                            nr, nc = cr + dr, cc + dc\n                            if 0 <= nr < R and 0 <= nc < C:\n                                if isInfected[nr][nc] == 1 and (nr, nc) not in visited:\n                                    visited.add((nr, nc))\n                                    stack.append((nr, nc))\n                                elif isInfected[nr][nc] == 0:\n                                    walls += 1\n                                    threatened.add((nr, nc))\n                    regions.append((cells, threatened, walls))\n        return regions\n    total_walls = 0\n    while True:\n        regions = get_regions()\n        if not regions: break\n        regions.sort(key=lambda x: len(x[1]))\n        target = regions.pop()\n        total_walls += target[2]\n        for r, c in target[0]:\n            isInfected[r][c] = -1\n        if not regions: break\n        for cells, threatened, _ in regions:\n            for r, c in threatened:\n                isInfected[r][c] = 1\n    return total_walls\n",
        test_cases=[{"input": [[[0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]]], "expected": 10}],
        hints=["Simulate day by day. Greedily quarantine the cluster threatening the most unique uninfected cells."],
        leetcode_id=749
    ))

    # 93. Escape a Large Maze
    problems.append(make_problem(
        pid="graph-h-escape-large-maze", title="Escape a Large Maze (Bounded Enclosure)",
        wing_id="graphs", floor=393, difficulty="hard", visualizer_type="grid",
        monster_name="Labyrinth Titan", monster_title="Entrapper in 10^6 x 10^6 Grids",
        monster_sprite="titan", monster_color="#8b5cf6", monster_attack="Enclosure Labyrinth",
        monster_quote="Is escape possible on a massive 10^6 x 10^6 coordinate plane?",
        description="There is a 10^6 x 10^6 grid. You are given `blocked` squares, `source`, and `target`. Return `True` if and only if it is possible to walk from `source` to `target`.",
        examples=[{"input": "blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]", "output": "False"}, {"input": "blocked = [], source = [0,0], target = [999999,999999]", "output": "True"}],
        constraints=["0 <= blocked.length <= 200"],
        function_name="isEscapePossible",
        starter_code="def isEscapePossible(blocked: list[list[int]], source: list[int], target: list[int]) -> bool:\n    pass\n",
        solution_code="def isEscapePossible(blocked: list[list[int]], source: list[int], target: list[int]) -> bool:\n    if not blocked: return True\n    blocked_set = set(map(tuple, blocked))\n    B = len(blocked)\n    limit = B * (B - 1) // 2\n    from collections import deque\n    def bfs(src, dest):\n        q = deque([tuple(src)])\n        visited = {tuple(src)}\n        while q:\n            if len(visited) > limit: return True\n            r, c = q.popleft()\n            if (r, c) == tuple(dest): return True\n            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:\n                nr, nc = r + dr, c + dc\n                if 0 <= nr < 10**6 and 0 <= nc < 10**6 and (nr, nc) not in blocked_set and (nr, nc) not in visited:\n                    visited.add((nr, nc))\n                    q.append((nr, nc))\n        return False\n    return bfs(source, target) and bfs(target, source)\n",
        test_cases=[{"input": [[[0, 1], [1, 0]], [0, 0], [0, 2]], "expected": False}, {"input": [[], [0, 0], [999999, 999999]], "expected": True}],
        hints=["B obstacles can trap at most B*(B-1)//2 cells. If BFS explores more than that threshold, the source is free."],
        leetcode_id=1036
    ))

    # 94. Longest Cycle in a Directed Graph
    problems.append(make_problem(
        pid="graph-h-longest-cycle-directed", title="Longest Cycle in a Directed Graph",
        wing_id="graphs", floor=394, difficulty="hard", visualizer_type="graph",
        monster_name="Vicious Ouroboros", monster_title="Emperor of Endless Recursions",
        monster_sprite="dragon", monster_color="#ef4444", monster_attack="Infinite Ring",
        monster_quote="Longest simple cycle in directed functional graph identified!",
        description="You are given a directed graph of `n` nodes labeled from 0 to `n - 1`, where each node has at most one outgoing edge. The graph is represented with an integer array `edges` where `edges[i]` denotes directed edge from node `i` to `edges[i]`. If node `i` has no outgoing edge, `edges[i] = -1`. Return the length of the longest cycle in the graph. If no cycle exists, return -1.",
        examples=[{"input": "edges = [3,3,4,2,3]", "output": "3"}, {"input": "edges = [2,-1,3,1]", "output": "-1"}],
        constraints=["n == edges.length", "2 <= n <= 100000"],
        function_name="longestCycle",
        starter_code="def longestCycle(edges: list[int]) -> int:\n    pass\n",
        solution_code="def longestCycle(edges: list[int]) -> int:\n    n = len(edges)\n    visited = [False] * n\n    ans = -1\n    for i in range(n):\n        if visited[i]: continue\n        path = {}\n        curr = i\n        step = 0\n        while curr != -1 and not visited[curr]:\n            visited[curr] = True\n            path[curr] = step\n            step += 1\n            curr = edges[curr]\n        if curr != -1 and curr in path:\n            ans = max(ans, step - path[curr])\n    return ans\n",
        test_cases=[{"input": [[3, 3, 4, 2, 3]], "expected": 3}, {"input": [[2, -1, 3, 1]], "expected": -1}],
        hints=["Functional graph cycle detection: track step numbers along current exploration path."],
        leetcode_id=2360
    ))

    # 95. Valid Arrangement of Pairs
    problems.append(make_problem(
        pid="graph-h-valid-arrangement-pairs", title="Valid Arrangement of Pairs (Eulerian Trail)",
        wing_id="graphs", floor=395, difficulty="hard", visualizer_type="graph",
        monster_name="Domino Sovereign", monster_title="Chainer of Head-to-Tail Pairs",
        monster_sprite="wraith", monster_color="#10b981", monster_attack="Domino Collapse",
        monster_quote="Consecutive arrangement where end of pair i equals start of pair i+1 formed!",
        description="You are given a 2D integer array `pairs` where `pairs[i] = [starti, endi]`. An arrangement of `pairs` is valid if `pairs[i][1] == pairs[i + 1][0]` for all `0 <= i < pairs.length - 1`. Return any valid arrangement of `pairs`.",
        examples=[{"input": "pairs = [[5,1],[4,5],[11,9],[9,4]]", "output": "[[11,9],[9,4],[4,5],[5,1]]"}],
        constraints=["1 <= pairs.length <= 100000"],
        function_name="validArrangement",
        starter_code="def validArrangement(pairs: list[list[int]]) -> list[list[int]]:\n    pass\n",
        solution_code="def validArrangement(pairs: list[list[int]]) -> list[list[int]]:\n    from collections import defaultdict\n    graph = defaultdict(list)\n    out_deg = defaultdict(int)\n    in_deg = defaultdict(int)\n    for u, v in pairs:\n        graph[u].append(v)\n        out_deg[u] += 1\n        in_deg[v] += 1\n    start = pairs[0][0]\n    for node in out_deg:\n        if out_deg[node] - in_deg[node] == 1:\n            start = node\n            break\n    trail = []\n    def dfs(u):\n        while graph[u]:\n            v = graph[u].pop()\n            dfs(v)\n        trail.append(u)\n    dfs(start)\n    trail.reverse()\n    return [[trail[i], trail[i + 1]] for i in range(len(trail) - 1)]\n",
        test_cases=[{"input": [[[5, 1], [4, 5], [11, 9], [9, 4]]], "expected": [[11, 9], [9, 4], [4, 5], [5, 1]]}],
        hints=["Eulerian path algorithm (Hierholzer). Start at vertex with out_degree - in_degree == 1."],
        leetcode_id=2097
    ))

    # 96. Strongly Connected Components Count
    problems.append(make_problem(
        pid="graph-h-scc-count-tarjan", title="Strongly Connected Components (Tarjan SCC)",
        wing_id="graphs", floor=396, difficulty="hard", visualizer_type="graph",
        monster_name="Tarjan Wyrm", monster_title="Surveyor of Mutually Reachable Subgraphs",
        monster_sprite="dragon", monster_color="#ec4899", monster_attack="Cyclic Condensation",
        monster_quote="Count of maximal strongly connected components calculated!",
        description="Given a directed graph with `n` nodes (0 to n - 1) and directed `edges`, return the number of strongly connected components (SCCs) in the graph.",
        examples=[{"input": "n = 5, edges = [[0,1],[1,2],[2,0],[1,3],[3,4],[4,3]]", "output": "2"}],
        constraints=["1 <= n <= 1000", "0 <= edges.length <= 5000"],
        function_name="countStronglyConnectedComponents",
        starter_code="def countStronglyConnectedComponents(n: int, edges: list[list[int]]) -> int:\n    pass\n",
        solution_code="def countStronglyConnectedComponents(n: int, edges: list[list[int]]) -> int:\n    from collections import defaultdict\n    adj = defaultdict(list)\n    for u, v in edges:\n        adj[u].append(v)\n    tin = [-1] * n\n    low = [-1] * n\n    on_stack = [False] * n\n    stack = []\n    timer = [0]\n    scc_count = [0]\n    def dfs(u):\n        tin[u] = low[u] = timer[0]\n        timer[0] += 1\n        stack.append(u)\n        on_stack[u] = True\n        for v in adj[u]:\n            if tin[v] == -1:\n                dfs(v)\n                low[u] = min(low[u], low[v])\n            elif on_stack[v]:\n                low[u] = min(low[u], tin[v])\n        if low[u] == tin[u]:\n            scc_count[0] += 1\n            while True:\n                w = stack.pop()\n                on_stack[w] = False\n                if w == u: break\n    for i in range(n):\n        if tin[i] == -1:\n            dfs(i)\n    return scc_count[0]\n",
        test_cases=[{"input": [5, [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 3]]], "expected": 2}, {"input": [3, [[0, 1], [1, 2]]], "expected": 3}],
        hints=["Tarjan's SCC algorithm with dfs timestamps, low links, and an exploration stack."],
        leetcode_id=0
    ))

    # 97. Number of Distinct Islands
    problems.append(make_problem(
        pid="graph-h-num-distinct-islands", title="Number of Distinct Islands (Shape Invariance)",
        wing_id="graphs", floor=397, difficulty="hard", visualizer_type="grid",
        monster_name="Topological Sculptor", monster_title="Caster of Congruent Landmass Shapes",
        monster_sprite="beholder", monster_color="#38bdf8", monster_attack="Congruence Scan",
        monster_quote="Number of distinct island shapes invariant under translation isolated!",
        description="Given an `m x n` binary matrix `grid`. An island is a 4-directionally connected group of 1s. Two islands are considered the same if and only if one island can be translated (not rotated or reflected) to coincide with the other. Return the number of distinct islands.",
        examples=[{"input": "grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]", "output": "1"}, {"input": "grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]", "output": "3"}],
        constraints=["1 <= m, n <= 50"],
        function_name="numDistinctIslands",
        starter_code="def numDistinctIslands(grid: list[list[int]]) -> int:\n    pass\n",
        solution_code="def numDistinctIslands(grid: list[list[int]]) -> int:\n    R, C = len(grid), len(grid[0])\n    shapes = set()\n    def dfs(r, c, r0, c0, shape):\n        grid[r][c] = 0\n        shape.append((r - r0, c - c0))\n        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:\n            nr, nc = r + dr, c + dc\n            if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:\n                dfs(nr, nc, r0, c0, shape)\n    for r in range(R):\n        for c in range(C):\n            if grid[r][c] == 1:\n                shape = []\n                dfs(r, c, r, c, shape)\n                shapes.add(tuple(shape))\n    return len(shapes)\n",
        test_cases=[{"input": [[[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]], "expected": 1}, {"input": [[[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]], "expected": 3}],
        hints=["Normalize coordinates of each island relative to top-left starting cell (r - r0, c - c0)."],
        leetcode_id=694
    ))

    # 98. Minimum Cost Flight Transit
    problems.append(make_problem(
        pid="graph-h-min-cost-flight-transit", title="Flight Transit with Passing Fees and Max Time",
        wing_id="graphs", floor=398, difficulty="hard", visualizer_type="graph",
        monster_name="Toll Spectre Overlord", monster_title="Harvester of Passing Fees",
        monster_sprite="spectre", monster_color="#f59e0b", monster_attack="Fee Exaction",
        monster_quote="Optimal path under strict travel deadline computed!",
        description="There is a country of `n` cities (0 to n - 1). Return the minimum fee to reach city n - 1 from city 0 in at most `maxTime` minutes, or -1 if impossible.",
        examples=[{"input": "maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]", "output": "11"}],
        constraints=["1 <= maxTime <= 1000", "2 <= passingFees.length <= 1000"],
        function_name="minCostFlightTransit",
        starter_code="def minCostFlightTransit(maxTime: int, edges: list[list[int]], passingFees: list[int]) -> int:\n    pass\n",
        solution_code="def minCostFlightTransit(maxTime: int, edges: list[list[int]], passingFees: list[int]) -> int:\n    import heapq\n    from collections import defaultdict\n    n = len(passingFees)\n    graph = defaultdict(list)\n    for u, v, t in edges:\n        graph[u].append((v, t))\n        graph[v].append((u, t))\n    min_time = [float('inf')] * n\n    pq = [(passingFees[0], 0, 0)]\n    min_time[0] = 0\n    while pq:\n        cost, time, u = heapq.heappop(pq)\n        if u == n - 1: return cost\n        for v, t in graph[u]:\n            nt = time + t\n            if nt <= maxTime and nt < min_time[v]:\n                min_time[v] = nt\n                heapq.heappush(pq, (cost + passingFees[v], nt, v))\n    return -1\n",
        test_cases=[{"input": [30, [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]], [5, 1, 2, 20, 20, 3]], "expected": 11}, {"input": [25, [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]], [5, 1, 2, 20, 20, 3]], "expected": -1}],
        hints=["Modified Dijkstra prioritizing min fee while pruning non-improving arrival times."],
        leetcode_id=1928
    ))

    # 99. Minimum Reverse Operations
    problems.append(make_problem(
        pid="graph-h-min-reverse-operations", title="Minimum Subarray Reverse Operations",
        wing_id="graphs", floor=399, difficulty="hard", visualizer_type="array",
        monster_name="Parity Inversion Archon", monster_title="Shifter of Even and Odd Jump Bands",
        monster_sprite="lich", monster_color="#8b5cf6", monster_attack="Parity Jump",
        monster_quote="Shortest operations to shift the 1 to all target indices!",
        description="You are given an integer `n` and an integer `p` in the range `[0, n - 1]`. Representing an array `arr` of size `n` with 1 at index `p` and 0 elsewhere. You can reverse any subarray of length `k` not containing indices in `banned`. Return an array `ans` where `ans[i]` is the minimum number of reverse operations needed to bring 1 to index `i`, or -1 if impossible.",
        examples=[{"input": "n = 4, p = 0, banned = [1,2], k = 4", "output": "[0,-1,-1,1]"}, {"input": "n = 5, p = 0, banned = [2,4], k = 3", "output": "[0,-1,-1,-1,-1]"}],
        constraints=["1 <= n <= 1000", "0 <= p < n"],
        function_name="minReverseOperations",
        starter_code="def minReverseOperations(n: int, p: int, banned: list[int], k: int) -> list[int]:\n    pass\n",
        solution_code="def minReverseOperations(n: int, p: int, banned: list[int], k: int) -> list[int]:\n    from collections import deque\n    ans = [-1] * n\n    banned_set = set(banned)\n    # Unvisited available nodes split by parity\n    avail = {0: set(i for i in range(n) if i % 2 == 0 and i not in banned_set and i != p),\n             1: set(i for i in range(n) if i % 2 == 1 and i not in banned_set and i != p)}\n    q = deque([(p, 0)])\n    ans[p] = 0\n    while q:\n        curr, d = q.popleft()\n        # New positions after reversing subarray of length k covering curr\n        min_j = max(0, curr - k + 1)\n        max_j = min(n - k, curr)\n        # Target range of curr reversed: 2*j + k - 1 - curr\n        low = 2 * min_j + k - 1 - curr\n        high = 2 * max_j + k - 1 - curr\n        target_parity = (curr + k - 1) % 2\n        to_remove = []\n        for nxt in avail[target_parity]:\n            if low <= nxt <= high:\n                ans[nxt] = d + 1\n                q.append((nxt, d + 1))\n                to_remove.append(nxt)\n        for r in to_remove:\n            avail[target_parity].remove(r)\n    return ans\n",
        test_cases=[{"input": [4, 0, [1, 2], 4], "expected": [0, -1, -1, 1]}, {"input": [5, 0, [2, 4], 3], "expected": [0, -1, -1, -1, -1]}],
        hints=["The reversed index range has the same parity (curr + k - 1) % 2. Prune visited nodes with sets."],
        leetcode_id=2612
    ))

    # 100. Graph Wing Final Boss: Minimum Cost Walk Covering All Target Vertices
    problems.append(make_problem(
        pid="graph-h-boss-min-cost-walk-all", title="Titan of Connected Topology (Steiner Walk)",
        wing_id="graphs", floor=400, difficulty="hard", visualizer_type="graph",
        monster_name="Topology Overlord Rex", monster_title="Master of All 100 Graph Floors",
        monster_sprite="boss", monster_color="#ef4444", monster_attack="Topology Annihilation",
        monster_quote="The entire labyrinth of graph vertices has been conquered!",
        description="Given `n` nodes (0 to n - 1) and undirected weighted `edges` where `edges[i] = [ui, vi, weighti]`. Find the minimum total weight of a walk starting at node 0 that visits every single node at least once and can end at any node. If the graph is not connected, return -1.",
        examples=[{"input": "n = 3, edges = [[0,1,1],[1,2,2],[0,2,4]]", "output": "3"}],
        constraints=["1 <= n <= 10"],
        function_name="minCostWalkAll",
        starter_code="def minCostWalkAll(n: int, edges: list[list[int]]) -> int:\n    pass\n",
        solution_code="def minCostWalkAll(n: int, edges: list[list[int]]) -> int:\n    import heapq\n    # All-pairs shortest paths via Floyd-Warshall\n    dist = [[float('inf')] * n for _ in range(n)]\n    for i in range(n): dist[i][i] = 0\n    for u, v, w in edges:\n        dist[u][v] = min(dist[u][v], w)\n        dist[v][u] = min(dist[v][u], w)\n    for k in range(n):\n        for i in range(n):\n            for j in range(n):\n                if dist[i][k] + dist[k][j] < dist[i][j]:\n                    dist[i][j] = dist[i][k] + dist[k][j]\n    # Check if all nodes reachable from 0\n    if any(dist[0][i] == float('inf') for i in range(n)):\n        return -1\n    # TSP over metric completion starting from 0\n    memo = {}\n    target = (1 << n) - 1\n    def tsp(u, mask):\n        if mask == target: return 0\n        if (u, mask) in memo: return memo[(u, mask)]\n        res = float('inf')\n        for v in range(n):\n            if not (mask & (1 << v)):\n                res = min(res, dist[u][v] + tsp(v, mask | (1 << v)))\n        memo[(u, mask)] = res\n        return res\n    return tsp(0, 1)\n",
        test_cases=[{"input": [3, [[0, 1, 1], [1, 2, 2], [0, 2, 4]]], "expected": 3}, {"input": [4, [[0, 1, 1], [1, 2, 1], [2, 3, 1]]], "expected": 3}, {"input": [3, [[0, 1, 1]]], "expected": -1}],
        hints=["Compute all-pairs shortest paths with Floyd-Warshall to form metric completion, then run Bitmask TSP starting at 0."],
        leetcode_id=847
    ))

    return problems
