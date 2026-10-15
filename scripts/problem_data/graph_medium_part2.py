"""
Graphs Medium Problems - Part 2 (Floors 326 to 340 - 15 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_graph_medium_part2():
    problems = []

    # 26. Network Delay Time
    problems.append(make_problem(
        pid="graph-m-network-delay-time", title="Network Delay Time (Dijkstra)",
        wing_id="graphs", floor=326, difficulty="medium", visualizer_type="graph",
        monster_name="Signal Overseer", monster_title="Broadcaster of Latent Pulses",
        monster_sprite="spectre", monster_color="#38bdf8", monster_attack="Latency Shock",
        monster_quote="Signal transmission to all network nodes calculated!",
        description="You are given a network of `n` nodes, labeled from 1 to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (ui, vi, wi)`, where `ui` is source, `vi` is target, and `wi` is time. We will send a signal from node `k`. Return the minimum time it takes for all `n` nodes to receive the signal. If it is impossible for all nodes to receive the signal, return `-1`.",
        examples=[{"input": "times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2", "output": "2"}, {"input": "times = [[1,2,1]], n = 2, k = 1", "output": "1"}],
        constraints=["1 <= k <= n <= 100", "1 <= times.length <= 6000"],
        function_name="networkDelayTime",
        starter_code="def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:\n    pass\n",
        solution_code="def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:\n    import heapq\n    from collections import defaultdict\n    graph = defaultdict(list)\n    for u, v, w in times:\n        graph[u].append((v, w))\n    dist = {}\n    pq = [(0, k)]\n    while pq:\n        d, u = heapq.heappop(pq)\n        if u in dist: continue\n        dist[u] = d\n        for v, w in graph[u]:\n            if v not in dist:\n                heapq.heappush(pq, (d + w, v))\n    return max(dist.values()) if len(dist) == n else -1\n",
        test_cases=[{"input": [[[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2], "expected": 2}, {"input": [[[1, 2, 1]], 2, 1], "expected": 1}, {"input": [[[1, 2, 1]], 2, 2], "expected": -1}],
        hints=["Use Dijkstra's algorithm with a priority queue starting from node k."],
        leetcode_id=743
    ))

    # 27. Cheapest Flights Within K Stops
    problems.append(make_problem(
        pid="graph-m-cheapest-flights-k-stops", title="Cheapest Flights Within K Stops",
        wing_id="graphs", floor=327, difficulty="medium", visualizer_type="graph",
        monster_name="Aero Harpy", monster_title="Navigator of Constrained Airspace",
        monster_sprite="wraith", monster_color="#f59e0b", monster_attack="Sky Turbulance",
        monster_quote="Cheapest transit cost under K flight stops evaluated!",
        description="There are `n` cities connected by some number of flights. You are given an array `flights` where `flights[i] = [fromi, toi, pricei]`. You are also given three integers `src`, `dst`, and `k`. Return the cheapest price from `src` to `dst` with at most `k` stops. If there is no such route, return -1.",
        examples=[{"input": "n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1", "output": "700"}],
        constraints=["1 <= n <= 100", "0 <= k <= n"],
        function_name="findCheapestPrice",
        starter_code="def findCheapestPrice(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:\n    pass\n",
        solution_code="def findCheapestPrice(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:\n    cost = [float('inf')] * n\n    cost[src] = 0\n    for _ in range(k + 1):\n        temp = list(cost)\n        for u, v, p in flights:\n            if cost[u] != float('inf') and cost[u] + p < temp[v]:\n                temp[v] = cost[u] + p\n        cost = temp\n    return cost[dst] if cost[dst] != float('inf') else -1\n",
        test_cases=[{"input": [4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1], "expected": 700}, {"input": [3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1], "expected": 200}],
        hints=["Bellman-Ford relaxation with k + 1 iterations."],
        leetcode_id=787
    ))

    # 28. All Paths from Source to Target in DAG
    problems.append(make_problem(
        pid="graph-m-all-paths-dag", title="All Paths From Source to Target",
        wing_id="graphs", floor=328, difficulty="medium", visualizer_type="graph",
        monster_name="Pathfinder Sphinx", monster_title="Chronicler of Every Vector",
        monster_sprite="sphinx", monster_color="#8b5cf6", monster_attack="Branching Fate",
        monster_quote="All directed paths from node 0 to node n-1 enumerated!",
        description="Given a directed acyclic graph (DAG) of `n` nodes labeled from 0 to `n - 1`, find all possible paths from node 0 to node `n - 1` and return them in any order. The graph is given as `graph[i]` is a list of all nodes you can visit from node `i`.",
        examples=[{"input": "graph = [[1,2],[3],[3],[]]", "output": "[[0,1,3],[0,2,3]]"}],
        constraints=["n == graph.length", "2 <= n <= 15"],
        function_name="allPathsSourceTarget",
        starter_code="def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:\n    pass\n",
        solution_code="def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:\n    target = len(graph) - 1\n    res = []\n    def dfs(curr, path):\n        if curr == target:\n            res.append(list(path))\n            return\n        for nxt in graph[curr]:\n            path.append(nxt)\n            dfs(nxt, path)\n            path.pop()\n    dfs(0, [0])\n    return res\n",
        test_cases=[{"input": [[[1, 2], [3], [3], []]], "expected": [[0, 1, 3], [0, 2, 3]]}, {"input": [[[4, 3, 1], [3, 2, 4], [3], [4], []]], "expected": [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]}],
        hints=["Standard backtracking DFS since the graph is a DAG with no directed cycles."],
        leetcode_id=797
    ))

    # 29. Keys and Rooms
    problems.append(make_problem(
        pid="graph-m-keys-and-rooms", title="Keys and Rooms Reachability",
        wing_id="graphs", floor=329, difficulty="medium", visualizer_type="graph",
        monster_name="Chamberlain Wraith", monster_title="Keeper of Locked Portals",
        monster_sprite="wraith", monster_color="#ec4899", monster_attack="Keylock Ward",
        monster_quote="Can every room in the sanctuary be unlocked from room 0?",
        description="There are `n` rooms labeled from `0` to `n - 1` and all the rooms are locked, except for room 0. Each room has a list of `keys` in it, and each key has a label on it, denoting which room it unlocks. Return `True` if you can enter all rooms, or `False` otherwise.",
        examples=[{"input": "rooms = [[1],[2],[3],[]]", "output": "True"}, {"input": "rooms = [[1,3],[3,0,1],[2],[0]]", "output": "False"}],
        constraints=["n == rooms.length", "2 <= n <= 1000"],
        function_name="canVisitAllRooms",
        starter_code="def canVisitAllRooms(rooms: list[list[int]]) -> bool:\n    pass\n",
        solution_code="def canVisitAllRooms(rooms: list[list[int]]) -> bool:\n    visited = set([0])\n    stack = [0]\n    while stack:\n        r = stack.pop()\n        for k in rooms[r]:\n            if k not in visited:\n                visited.add(k)\n                stack.append(k)\n    return len(visited) == len(rooms)\n",
        test_cases=[{"input": [[[1], [2], [3], []]], "expected": True}, {"input": [[[1, 3], [3, 0, 1], [2], [0]]], "expected": False}],
        hints=["DFS or BFS starting at room 0. Track visited rooms and compare count to n."],
        leetcode_id=841
    ))

    # 30. Find Eventual Safe States
    problems.append(make_problem(
        pid="graph-m-eventual-safe-states", title="Find Eventual Safe States",
        wing_id="graphs", floor=330, difficulty="medium", visualizer_type="graph",
        monster_name="Terminal Necromancer", monster_title="Banisher of Eternal Cycles",
        monster_sprite="lich", monster_color="#10b981", monster_attack="Terminal Gaze",
        monster_quote="Nodes guaranteed to terminate at terminal states identified!",
        description="There is a directed graph of `n` nodes with each node labeled from 0 to `n - 1`. A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node. Return an array containing all safe nodes of the graph, sorted in ascending order.",
        examples=[{"input": "graph = [[1,2],[2,3],[5],[0],[5],[],[]]", "output": "[2,4,5,6]"}],
        constraints=["1 <= n <= 10000"],
        function_name="eventualSafeNodes",
        starter_code="def eventualSafeNodes(graph: list[list[int]]) -> list[int]:\n    pass\n",
        solution_code="def eventualSafeNodes(graph: list[list[int]]) -> list[int]:\n    n = len(graph)\n    color = [0] * n  # 0=unvisited, 1=visiting, 2=safe\n    def dfs(u):\n        if color[u] > 0:\n            return color[u] == 2\n        color[u] = 1\n        for v in graph[u]:\n            if not dfs(v):\n                return False\n        color[u] = 2\n        return True\n    return [i for i in range(n) if dfs(i)]\n",
        test_cases=[{"input": [[[1, 2], [2, 3], [5], [0], [5], [], []]], "expected": [2, 4, 5, 6]}, {"input": [[[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]], "expected": [4]}],
        hints=["3-color DFS (white, gray, black). Nodes in or leading to a cycle are unsafe."],
        leetcode_id=802
    ))

    # 31. As Far from Land as Possible
    problems.append(make_problem(
        pid="graph-m-as-far-from-land", title="As Far from Land as Possible",
        wing_id="graphs", floor=331, difficulty="medium", visualizer_type="grid",
        monster_name="Abyssal Kraken", monster_title="Lurker in Deepest Waters",
        monster_sprite="leviathan", monster_color="#06b6d4", monster_attack="Abyssal Whirlpool",
        monster_quote="Maximum water-to-nearest-land distance reached!",
        description="Given an `n x n` `grid` containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.",
        examples=[{"input": "grid = [[1,0,1],[0,0,0],[1,0,1]]", "output": "2"}, {"input": "grid = [[1,0,0],[0,0,0],[0,0,0]]", "output": "4"}],
        constraints=["1 <= n <= 100"],
        function_name="maxDistance",
        starter_code="def maxDistance(grid: list[list[int]]) -> int:\n    pass\n",
        solution_code="def maxDistance(grid: list[list[int]]) -> int:\n    n = len(grid)\n    from collections import deque\n    q = deque()\n    for r in range(n):\n        for c in range(n):\n            if grid[r][c] == 1: q.append((r, c))\n    if len(q) == 0 or len(q) == n * n: return -1\n    dist = -1\n    while q:\n        dist += 1\n        for _ in range(len(q)):\n            r, c = q.popleft()\n            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:\n                nr, nc = r + dr, c + dc\n                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:\n                    grid[nr][nc] = 1\n                    q.append((nr, nc))\n    return dist\n",
        test_cases=[{"input": [[[1, 0, 1], [0, 0, 0], [1, 0, 1]]], "expected": 2}, {"input": [[[1, 0, 0], [0, 0, 0], [0, 0, 0]]], "expected": 4}, {"input": [[[0, 0], [0, 0]]], "expected": -1}],
        hints=["Multi-source BFS from all land cells simultaneously."],
        leetcode_id=1162
    ))

    # 32. Open the Lock
    problems.append(make_problem(
        pid="graph-m-open-the-lock", title="Open the Combination Lock",
        wing_id="graphs", floor=332, difficulty="medium", visualizer_type="graph",
        monster_name="Cipher Gargoyle", monster_title="Guardian of Rotational Tumblers",
        monster_sprite="gargoyle", monster_color="#64748b", monster_attack="Tumbler Snap",
        monster_quote="Minimum 4-wheel tumbler turns to avoid deadends and reach target!",
        description="You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0'-'9'. The lock starts at '0000'. You are given a list of `deadends` strings. If the lock displays any of these codes, the lock becomes dead and cannot be turned. Given a `target`, return the minimum total number of turns required to open the lock, or -1 if impossible.",
        examples=[{"input": "deadends = [\"0201\",\"0101\",\"0102\",\"1212\",\"2002\"], target = \"0202\"", "output": "6"}, {"input": "deadends = [\"8888\"], target = \"0009\"", "output": "1"}],
        constraints=["1 <= deadends.length <= 500"],
        function_name="openLock",
        starter_code="def openLock(deadends: list[str], target: str) -> int:\n    pass\n",
        solution_code="def openLock(deadends: list[str], target: str) -> int:\n    dead = set(deadends)\n    if \"0000\" in dead: return -1\n    if target == \"0000\": return 0\n    from collections import deque\n    q = deque([(\"0000\", 0)])\n    visited = set([\"0000\"])\n    while q:\n        curr, d = q.popleft()\n        if curr == target: return d\n        for i in range(4):\n            digit = int(curr[i])\n            for delta in (-1, 1):\n                nxt_digit = (digit + delta) % 10\n                nxt = curr[:i] + str(nxt_digit) + curr[i+1:]\n                if nxt not in dead and nxt not in visited:\n                    visited.add(nxt)\n                    q.append((nxt, d + 1))\n    return -1\n",
        test_cases=[{"input": [["0201", "0101", "0102", "1212", "2002"], "0202"], "expected": 6}, {"input": [["8888"], "0009"], "expected": 1}, {"input": [["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888"], "expected": -1}],
        hints=["Treat each 4-digit string as a node with 8 neighbors in a BFS shortest path search."],
        leetcode_id=752
    ))

    # 33. Word Ladder
    problems.append(make_problem(
        pid="graph-m-word-ladder-length", title="Word Ladder (Shortest Mutation Chain)",
        wing_id="graphs", floor=333, difficulty="medium", visualizer_type="graph",
        monster_name="Lexical Chimera", monster_title="Transformer of Monosyllabic Runes",
        monster_sprite="manticore", monster_color="#ec4899", monster_attack="Rune Shift",
        monster_quote="Shortest sequence of one-letter transformations computed!",
        description="A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that every adjacent pair differs by a single letter, and `endWord == sk`. Return the number of words in the shortest transformation sequence from `beginWord` to `endWord`, or 0 if no such sequence exists.",
        examples=[{"input": "beginWord = \"hit\", endWord = \"cog\", wordList = [\"hot\",\"dot\",\"dog\",\"lot\",\"log\",\"cog\"]", "output": "5"}, {"input": "beginWord = \"hit\", endWord = \"cog\", wordList = [\"hot\",\"dot\",\"dog\",\"lot\",\"log\"]", "output": "0"}],
        constraints=["1 <= beginWord.length <= 10", "1 <= wordList.length <= 5000"],
        function_name="ladderLength",
        starter_code="def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:\n    pass\n",
        solution_code="def ladderLength(beginWord: str, endWord: str, wordList: list[str]) -> int:\n    word_set = set(wordList)\n    if endWord not in word_set: return 0\n    from collections import deque\n    q = deque([(beginWord, 1)])\n    visited = set([beginWord])\n    while q:\n        word, step = q.popleft()\n        if word == endWord: return step\n        for i in range(len(word)):\n            for c in 'abcdefghijklmnopqrstuvwxyz':\n                nxt = word[:i] + c + word[i+1:]\n                if nxt in word_set and nxt not in visited:\n                    visited.add(nxt)\n                    q.append((nxt, step + 1))\n    return 0\n",
        test_cases=[{"input": ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]], "expected": 5}, {"input": ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]], "expected": 0}],
        hints=["BFS exploring all 26 character variations at each letter position."],
        leetcode_id=127
    ))

    # 34. Shortest Bridge
    problems.append(make_problem(
        pid="graph-m-shortest-bridge", title="Shortest Bridge Connecting Two Islands",
        wing_id="graphs", floor=334, difficulty="medium", visualizer_type="grid",
        monster_name="Void Pontiff", monster_title="Bridger of Isolated Atolls",
        monster_sprite="wraith", monster_color="#3b82f6", monster_attack="Pontoons of Shadow",
        monster_quote="Minimum 0-water flips needed to connect the two islands!",
        description="You are given an `n x n` binary matrix `grid` where 1 represents land and 0 represents water. An island is a 4-directionally connected group of 1's. There are exactly two islands in `grid`. Return the smallest number of 0's you must flip to connect the two islands.",
        examples=[{"input": "grid = [[0,1],[1,0]]", "output": "1"}, {"input": "grid = [[0,1,0],[0,0,0],[0,0,1]]", "output": "2"}],
        constraints=["2 <= n <= 100"],
        function_name="shortestBridge",
        starter_code="def shortestBridge(grid: list[list[int]]) -> int:\n    pass\n",
        solution_code="def shortestBridge(grid: list[list[int]]) -> int:\n    n = len(grid)\n    from collections import deque\n    q = deque()\n    found = False\n    def dfs(r, c):\n        grid[r][c] = 2\n        q.append((r, c, 0))\n        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:\n            nr, nc = r + dr, c + dc\n            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:\n                dfs(nr, nc)\n    for r in range(n):\n        if found: break\n        for c in range(n):\n            if grid[r][c] == 1:\n                dfs(r, c)\n                found = True\n                break\n    while q:\n        r, c, d = q.popleft()\n        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:\n            nr, nc = r + dr, c + dc\n            if 0 <= nr < n and 0 <= nc < n:\n                if grid[nr][nc] == 1: return d\n                if grid[nr][nc] == 0:\n                    grid[nr][nc] = 2\n                    q.append((nr, nc, d + 1))\n    return 0\n",
        test_cases=[{"input": [[[0, 1], [1, 0]]], "expected": 1}, {"input": [[[0, 1, 0], [0, 0, 0], [0, 0, 1]]], "expected": 2}],
        hints=["DFS to find and paint the first island, then BFS simultaneously from all its perimeter cells to reach the second island."],
        leetcode_id=934
    ))

    # 35. Time Needed to Inform All Employees
    problems.append(make_problem(
        pid="graph-m-time-inform-employees", title="Time Needed to Inform All Employees",
        wing_id="graphs", floor=335, difficulty="medium", visualizer_type="graph",
        monster_name="Herald Fiend", monster_title="Relayer of Imperial Edicts",
        monster_sprite="demon", monster_color="#f97316", monster_attack="Mandate Cascade",
        monster_quote="Maximum propagation time down hierarchy tree evaluated!",
        description="A company has `n` employees with a unique ID for each employee from 0 to `n - 1`. The head of the company has is `headID`. Each employee `i` has a direct manager `manager[i]`. `manager[headID] = -1`. The head receives urgent news and needs to inform all employees. Employee `i` takes `informTime[i]` minutes to inform all direct subordinates. Return the number of minutes to inform all employees.",
        examples=[{"input": "n = 1, headID = 0, manager = [-1], informTime = [0]", "output": "0"}, {"input": "n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]", "output": "1"}],
        constraints=["1 <= n <= 100000", "0 <= informTime[i] <= 1000"],
        function_name="numOfMinutes",
        starter_code="def numOfMinutes(n: int, headID: int, manager: list[int], informTime: list[int]) -> int:\n    pass\n",
        solution_code="def numOfMinutes(n: int, headID: int, manager: list[int], informTime: list[int]) -> int:\n    from collections import defaultdict\n    tree = defaultdict(list)\n    for emp, mgr in enumerate(manager):\n        if mgr != -1:\n            tree[mgr].append(emp)\n    def dfs(u):\n        return informTime[u] + max([dfs(v) for v in tree[u]], default=0)\n    return dfs(headID)\n",
        test_cases=[{"input": [1, 0, [-1], [0]], "expected": 0}, {"input": [6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]], "expected": 1}],
        hints=["DFS from headID taking the maximum sum of informTime along any root-to-leaf path."],
        leetcode_id=1376
    ))

    # 36. Minimum Height Trees
    problems.append(make_problem(
        pid="graph-m-min-height-trees", title="Minimum Height Trees (Graph Centroids)",
        wing_id="graphs", floor=336, difficulty="medium", visualizer_type="graph",
        monster_name="Centroid Titan", monster_title="Balancing Center of the Forest",
        monster_sprite="titan", monster_color="#8b5cf6", monster_attack="Gravity Well",
        monster_quote="Forest centroids that minimize tree height discovered!",
        description="A tree is an undirected graph in which any two vertices are connected by exactly one path. You are given `n` nodes labeled from 0 to `n - 1` and `edges`. Find all trees that have minimum height and return a list of their root labels in sorted order.",
        examples=[{"input": "n = 4, edges = [[1,0],[1,2],[1,3]]", "output": "[1]"}, {"input": "n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]", "output": "[3,4]"}],
        constraints=["1 <= n <= 20000"],
        function_name="findMinHeightTrees",
        starter_code="def findMinHeightTrees(n: int, edges: list[list[int]]) -> list[int]:\n    pass\n",
        solution_code="def findMinHeightTrees(n: int, edges: list[list[int]]) -> list[int]:\n    if n <= 2: return sorted(list(range(n)))\n    from collections import defaultdict, deque\n    adj = defaultdict(set)\n    for u, v in edges:\n        adj[u].add(v)\n        adj[v].add(u)\n    leaves = deque([i for i in range(n) if len(adj[i]) == 1])\n    remaining = n\n    while remaining > 2:\n        leaves_cnt = len(leaves)\n        remaining -= leaves_cnt\n        for _ in range(leaves_cnt):\n            leaf = leaves.popleft()\n            neighbor = adj[leaf].pop()\n            adj[neighbor].remove(leaf)\n            if len(adj[neighbor]) == 1:\n                leaves.append(neighbor)\n    return sorted(list(leaves))\n",
        test_cases=[{"input": [4, [[1, 0], [1, 2], [1, 3]]], "expected": [1]}, {"input": [6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]], "expected": [3, 4]}, {"input": [1, []], "expected": [0]}],
        hints=["Prune leaves layer by layer (topological peel) until 1 or 2 centroid nodes remain."],
        leetcode_id=310
    ))

    # 37. Evaluate Division
    problems.append(make_problem(
        pid="graph-m-evaluate-division", title="Evaluate Division (Weighted Directed Graph)",
        wing_id="graphs", floor=337, difficulty="medium", visualizer_type="graph",
        monster_name="Ratio Archon", monster_title="Equator of Fractional Variables",
        monster_sprite="gargoyle", monster_color="#10b981", monster_attack="Ratio Cascade",
        monster_quote="Multiplicative path weights evaluated across query pairs!",
        description="You are given an array of variable pairs `equations` and an array of real numbers `values`, where `equations[i] = [Ai, Bi]` and `values[i]` represent `Ai / Bi = values[i]`. You are also given `queries` where `queries[j] = [Cj, Dj]`. Return the answers to all queries. If a single answer cannot be determined, return -1.0.",
        examples=[{"input": "equations = [[\"a\",\"b\"],[\"b\",\"c\"]], values = [2.0,3.0], queries = [[\"a\",\"c\"],[\"b\",\"a\"],[\"a\",\"e\"],[\"a\",\"a\"],[\"x\",\"x\"]]", "output": "[6.0,0.5,-1.0,1.0,-1.0]"}],
        constraints=["1 <= equations.length <= 20", "1 <= queries.length <= 20"],
        function_name="calcEquation",
        starter_code="def calcEquation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:\n    pass\n",
        solution_code="def calcEquation(equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:\n    from collections import defaultdict, deque\n    graph = defaultdict(dict)\n    for (u, v), val in zip(equations, values):\n        graph[u][v] = val\n        graph[v][u] = 1.0 / val\n    res = []\n    for u, v in queries:\n        if u not in graph or v not in graph:\n            res.append(-1.0)\n            continue\n        if u == v:\n            res.append(1.0)\n            continue\n        q = deque([(u, 1.0)])\n        visited = set([u])\n        ans = -1.0\n        while q:\n            curr, prod = q.popleft()\n            if curr == v:\n                ans = prod\n                break\n            for nxt, weight in graph[curr].items():\n                if nxt not in visited:\n                    visited.add(nxt)\n                    q.append((nxt, prod * weight))\n        res.append(ans)\n    return res\n",
        test_cases=[{"input": [[["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]], "expected": [6.0, 0.5, -1.0, 1.0, -1.0]}],
        hints=["Model as a weighted directed graph where edge (u, v) has weight w and edge (v, u) has weight 1/w. Use BFS."],
        leetcode_id=399
    ))

    # 38. Reconstruct Itinerary
    problems.append(make_problem(
        pid="graph-m-reconstruct-itinerary", title="Reconstruct Itinerary (Hierholzer Algorithm)",
        wing_id="graphs", floor=338, difficulty="medium", visualizer_type="graph",
        monster_name="Aero Drake Sovereign", monster_title="Flier of the Lexicographical Euler Trail",
        monster_sprite="dragon", monster_color="#38bdf8", monster_attack="Flight Vortex",
        monster_quote="Eulerian path visiting every flight ticket in lexical order created!",
        description="You are given a list of airline `tickets` where `tickets[i] = [fromi, toi]`. Reconstruct the itinerary in order and return it. All tickets must be used. Itinerary must begin with `'JFK'`. If there are multiple valid itineraries, return the one with smallest lexical order.",
        examples=[{"input": "tickets = [[\"MUC\",\"LHR\"],[\"JFK\",\"MUC\"],[\"SFO\",\"SJC\"],[\"LHR\",\"SFO\"]]", "output": "[\"JFK\",\"MUC\",\"LHR\",\"SFO\",\"SJC\"]"}],
        constraints=["1 <= tickets.length <= 300"],
        function_name="findItinerary",
        starter_code="def findItinerary(tickets: list[list[str]]) -> list[str]:\n    pass\n",
        solution_code="def findItinerary(tickets: list[list[str]]) -> list[str]:\n    from collections import defaultdict\n    graph = defaultdict(list)\n    for u, v in sorted(tickets, reverse=True):\n        graph[u].append(v)\n    route = []\n    def dfs(curr):\n        while graph[curr]:\n            nxt = graph[curr].pop()\n            dfs(nxt)\n        route.append(curr)\n    dfs('JFK')\n    return route[::-1]\n",
        test_cases=[{"input": [[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]], "expected": ["JFK", "MUC", "LHR", "SFO", "SJC"]}],
        hints=["Hierholzer's algorithm: greedily follow smallest lexical edges and post-order reverse."],
        leetcode_id=332
    ))

    # 39. Number of Closed Islands
    problems.append(make_problem(
        pid="graph-m-number-closed-islands", title="Number of Closed Islands",
        wing_id="graphs", floor=339, difficulty="medium", visualizer_type="grid",
        monster_name="Cavern Wraith", monster_title="Dweller of Landlocked Grottos",
        monster_sprite="wraith", monster_color="#10b981", monster_attack="Subterranean Seal",
        monster_quote="Completely landlocked 0-islands isolated and counted!",
        description="Given a 2D `grid` consists of 0s (land) and 1s (water). An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally surrounded by 1s (not touching grid boundaries). Return the number of closed islands.",
        examples=[{"input": "grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]", "output": "2"}],
        constraints=["1 <= grid.length, grid[0].length <= 100"],
        function_name="closedIsland",
        starter_code="def closedIsland(grid: list[list[int]]) -> int:\n    pass\n",
        solution_code="def closedIsland(grid: list[list[int]]) -> int:\n    R, C = len(grid), len(grid[0])\n    def dfs(r, c):\n        if r < 0 or r >= R or c < 0 or c >= C:\n            return False\n        if grid[r][c] == 1:\n            return True\n        grid[r][c] = 1\n        d1 = dfs(r + 1, c)\n        d2 = dfs(r - 1, c)\n        d3 = dfs(r, c + 1)\n        d4 = dfs(r, c - 1)\n        return d1 and d2 and d3 and d4\n    ans = 0\n    for r in range(R):\n        for c in range(C):\n            if grid[r][c] == 0:\n                if dfs(r, c): ans += 1\n    return ans\n",
        test_cases=[{"input": [[[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]], "expected": 2}],
        hints=["Flood fill each component of 0s. If any cell touches the boundary, it is not closed."],
        leetcode_id=1254
    ))

    # 40. Count Sub Islands
    problems.append(make_problem(
        pid="graph-m-count-sub-islands", title="Count Sub Islands",
        wing_id="graphs", floor=340, difficulty="medium", visualizer_type="grid",
        monster_name="Concentric Hydra", monster_title="Subsumer of Nested Landmasses",
        monster_sprite="gargoyle", monster_color="#06b6d4", monster_attack="Enclosing Tide",
        monster_quote="All grid2 islands wholly contained within grid1 islands counted!",
        description="You are given two `m x n` binary matrices `grid1` and `grid2` containing only 0's and 1's. An island is a group of 1's connected 4-directionally. An island in `grid2` is considered a sub-island if there is an island in `grid1` that contains all the cells that make up this island in `grid2`. Return the number of islands in `grid2` that are considered sub-islands.",
        examples=[{"input": "grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]", "output": "3"}],
        constraints=["1 <= m, n <= 500"],
        function_name="countSubIslands",
        starter_code="def countSubIslands(grid1: list[list[int]], grid2: list[list[int]]) -> int:\n    pass\n",
        solution_code="def countSubIslands(grid1: list[list[int]], grid2: list[list[int]]) -> int:\n    R, C = len(grid1), len(grid1[0])\n    def dfs(r, c):\n        if r < 0 or r >= R or c < 0 or c >= C or grid2[r][c] == 0:\n            return True\n        grid2[r][c] = 0\n        is_sub = (grid1[r][c] == 1)\n        d1 = dfs(r + 1, c)\n        d2 = dfs(r - 1, c)\n        d3 = dfs(r, c + 1)\n        d4 = dfs(r, c - 1)\n        return is_sub and d1 and d2 and d3 and d4\n    ans = 0\n    for r in range(R):\n        for c in range(C):\n            if grid2[r][c] == 1:\n                if dfs(r, c): ans += 1\n    return ans\n",
        test_cases=[{"input": [[[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]], [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]], "expected": 3}],
        hints=["DFS grid2 and sink the island. Verify every cell in grid2's island is also 1 in grid1."],
        leetcode_id=1905
    ))

    return problems
