"""
Graphs Medium Problems - Part 3 (Floors 341 to 355 - 15 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_graph_medium_part3():
    problems = []

    # 41. Min Cost to Connect All Points
    problems.append(make_problem(
        pid="graph-m-min-cost-connect-points", title="Min Cost to Connect All Points (Prim's MST)",
        wing_id="graphs", floor=341, difficulty="medium", visualizer_type="graph",
        monster_name="Magnetic Colossus", monster_title="Forging Minimum Spanning Networks",
        monster_sprite="golem", monster_color="#8b5cf6", monster_attack="Manhattan Pulse",
        monster_quote="Minimum Manhattan spanning tree constructed across all coordinates!",
        description="You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`. The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the Manhattan distance: `|xi - xj| + |yi - yj|`. Return the minimum cost to make all points connected.",
        examples=[{"input": "points = [[0,0],[2,2],[3,10],[5,2],[7,0]]", "output": "20"}, {"input": "points = [[3,12],[-2,5],[-4,1]]", "output": "18"}],
        constraints=["1 <= points.length <= 1000", "-10^6 <= xi, yi <= 10^6"],
        function_name="minCostConnectPoints",
        starter_code="def minCostConnectPoints(points: list[list[int]]) -> int:\n    pass\n",
        solution_code="def minCostConnectPoints(points: list[list[int]]) -> int:\n    n = len(points)\n    import heapq\n    visited = [False] * n\n    pq = [(0, 0)]\n    total_cost = 0\n    connected = 0\n    while pq and connected < n:\n        cost, u = heapq.heappop(pq)\n        if visited[u]: continue\n        visited[u] = True\n        total_cost += cost\n        connected += 1\n        x1, y1 = points[u]\n        for v in range(n):\n            if not visited[v]:\n                x2, y2 = points[v]\n                heapq.heappush(pq, (abs(x1 - x2) + abs(y1 - y2), v))\n    return total_cost\n",
        test_cases=[{"input": [[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]], "expected": 20}, {"input": [[[3, 12], [-2, 5], [-4, 1]]], "expected": 18}],
        hints=["Prim's or Kruskal's algorithm on complete graph with Manhattan weights."],
        leetcode_id=1584
    ))

    # 42. Path with Minimum Effort
    problems.append(make_problem(
        pid="graph-m-path-min-effort", title="Path with Minimum Effort (Minimax Dijkstra)",
        wing_id="graphs", floor=342, difficulty="medium", visualizer_type="grid",
        monster_name="Crag Wyrm", monster_title="Navigator of Rugged Elevations",
        monster_sprite="dragon", monster_color="#ef4444", monster_attack="Altitude Shear",
        monster_quote="Route minimizing maximum single-step elevation jump found!",
        description="You are a hiker preparing for an upcoming hike. You are given `heights`, a 2D array of size `rows x columns`. A route's effort is the maximum absolute difference in heights between two consecutive cells of the route. Return the minimum effort required to travel from `(0, 0)` to `(rows-1, columns-1)`.",
        examples=[{"input": "heights = [[1,2,2],[3,8,2],[5,3,5]]", "output": "2"}, {"input": "heights = [[1,2,3],[3,8,4],[5,3,5]]", "output": "1"}],
        constraints=["1 <= rows, columns <= 100"],
        function_name="minimumEffortPath",
        starter_code="def minimumEffortPath(heights: list[list[int]]) -> int:\n    pass\n",
        solution_code="def minimumEffortPath(heights: list[list[int]]) -> int:\n    R, C = len(heights), len(heights[0])\n    import heapq\n    dist = [[float('inf')] * C for _ in range(R)]\n    dist[0][0] = 0\n    pq = [(0, 0, 0)]\n    while pq:\n        d, r, c = heapq.heappop(pq)\n        if r == R - 1 and c == C - 1: return d\n        if d > dist[r][c]: continue\n        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:\n            nr, nc = r + dr, c + dc\n            if 0 <= nr < R and 0 <= nc < C:\n                effort = max(d, abs(heights[r][c] - heights[nr][nc]))\n                if effort < dist[nr][nc]:\n                    dist[nr][nc] = effort\n                    heapq.heappush(pq, (effort, nr, nc))\n    return 0\n",
        test_cases=[{"input": [[[1, 2, 2], [3, 8, 2], [5, 3, 5]]], "expected": 2}, {"input": [[[1, 2, 3], [3, 8, 4], [5, 3, 5]]], "expected": 1}],
        hints=["Modified Dijkstra where edge relaxation uses max(d, abs(diff))."],
        leetcode_id=1631
    ))

    # 43. Swim in Rising Water
    problems.append(make_problem(
        pid="graph-m-swim-rising-water", title="Swim in Rising Water",
        wing_id="graphs", floor=343, difficulty="medium", visualizer_type="grid",
        monster_name="Tide Warden", monster_title="Commander of Inundation Levels",
        monster_sprite="boss", monster_color="#06b6d4", monster_attack="Rising Surge",
        monster_quote="Least water level time required to reach bottom-right corner!",
        description="You are given an `n x n` integer matrix `grid` where each value `grid[i][j]` represents the elevation at that point. At time `t`, the depth of the water everywhere is `t`. You can swim from a square to an adjacent square if both are submerged (elevation <= t). You start at `(0, 0)`. Return the least time until you can reach `(n - 1, n - 1)`.",
        examples=[{"input": "grid = [[0,2],[1,3]]", "output": "3"}, {"input": "grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]", "output": "16"}],
        constraints=["n == grid.length", "1 <= n <= 50"],
        function_name="swimInWater",
        starter_code="def swimInWater(grid: list[list[int]]) -> int:\n    pass\n",
        solution_code="def swimInWater(grid: list[list[int]]) -> int:\n    n = len(grid)\n    import heapq\n    visited = [[False] * n for _ in range(n)]\n    visited[0][0] = True\n    pq = [(grid[0][0], 0, 0)]\n    while pq:\n        t, r, c = heapq.heappop(pq)\n        if r == n - 1 and c == n - 1: return t\n        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:\n            nr, nc = r + dr, c + dc\n            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:\n                visited[nr][nc] = True\n                heapq.heappush(pq, (max(t, grid[nr][nc]), nr, nc))\n    return 0\n",
        test_cases=[{"input": [[[0, 2], [1, 3]]], "expected": 3}, {"input": [[[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]], "expected": 16}],
        hints=["Use Dijkstra's algorithm prioritizing minimum bottleneck elevation."],
        leetcode_id=778
    ))

    # 44. Satisfiability of Equality Equations
    problems.append(make_problem(
        pid="graph-m-equality-equations", title="Satisfiability of Equality Equations",
        wing_id="graphs", floor=344, difficulty="medium", visualizer_type="graph",
        monster_name="Logic Arbiter", monster_title="Evaluator of Transitive Equivalence",
        monster_sprite="wizard", monster_color="#38bdf8", monster_attack="Identity Collapse",
        monster_quote="Equivalence classes and inequality contradictions analyzed!",
        description="You are given an array of strings `equations` that represent relationships between variables where each string has length 4: `\"a==b\"` or `\"a!=b\"`. Here `a` and `b` are lowercase letters. Return `True` if it is possible to assign integers to variable names so as to satisfy all the given equations, or `False` otherwise.",
        examples=[{"input": "equations = [\"a==b\",\"b!=a\"]", "output": "False"}, {"input": "equations = [\"b==a\",\"a==b\"]", "output": "True"}, {"input": "equations = [\"a==b\",\"b==c\",\"a==c\"]", "output": "True"}],
        constraints=["1 <= equations.length <= 500"],
        function_name="equationsPossible",
        starter_code="def equationsPossible(equations: list[str]) -> bool:\n    pass\n",
        solution_code="def equationsPossible(equations: list[str]) -> bool:\n    parent = {chr(c): chr(c) for c in range(ord('a'), ord('z') + 1)}\n    def find(x):\n        if parent[x] == x: return x\n        parent[x] = find(parent[x])\n        return parent[x]\n    for eq in equations:\n        if eq[1] == '=':\n            parent[find(eq[0])] = find(eq[3])\n    for eq in equations:\n        if eq[1] == '!':\n            if find(eq[0]) == find(eq[3]):\n                return False\n    return True\n",
        test_cases=[{"input": [["a==b", "b!=a"]], "expected": False}, {"input": [["b==a", "a==b"]], "expected": True}, {"input": [["a==b", "b==c", "a==c"]], "expected": True}],
        hints=["Union all equality pairs first, then check if any inequality pair belongs to the same set."],
        leetcode_id=990
    ))

    # 45. Possible Bipartition
    problems.append(make_problem(
        pid="graph-m-possible-bipartition", title="Possible Bipartition (Dislike Graph)",
        wing_id="graphs", floor=345, difficulty="medium", visualizer_type="graph",
        monster_name="Faction Splitter", monster_title="Polarizer of Divided Clans",
        monster_sprite="imp", monster_color="#f59e0b", monster_attack="Discord Flare",
        monster_quote="Partitioning people into two non-conflicting groups verified!",
        description="We want to split a group of `n` people (labeled from 1 to `n`) into two groups of any size. Each person may dislike some other people. Given `dislikes` where `dislikes[i] = [ai, bi]`, return `True` if it is possible to split everyone into two groups such that no two people that dislike each other are in the same group.",
        examples=[{"input": "n = 4, dislikes = [[1,2],[1,3],[2,4]]", "output": "True"}, {"input": "n = 3, dislikes = [[1,2],[1,3],[2,3]]", "output": "False"}],
        constraints=["1 <= n <= 2000", "0 <= dislikes.length <= 10000"],
        function_name="possibleBipartition",
        starter_code="def possibleBipartition(n: int, dislikes: list[list[int]]) -> bool:\n    pass\n",
        solution_code="def possibleBipartition(n: int, dislikes: list[list[int]]) -> bool:\n    from collections import defaultdict, deque\n    adj = defaultdict(list)\n    for u, v in dislikes:\n        adj[u].append(v)\n        adj[v].append(u)\n    color = {}\n    for i in range(1, n + 1):\n        if i not in color:\n            color[i] = 0\n            q = deque([i])\n            while q:\n                u = q.popleft()\n                for v in adj[u]:\n                    if v not in color:\n                        color[v] = 1 - color[u]\n                        q.append(v)\n                    elif color[v] == color[u]:\n                        return False\n    return True\n",
        test_cases=[{"input": [4, [[1, 2], [1, 3], [2, 4]]], "expected": True}, {"input": [3, [[1, 2], [1, 3], [2, 3]]], "expected": False}],
        hints=["Check if the dislike graph is bipartite (2-colorable)."],
        leetcode_id=886
    ))

    # 46. Number of Operations to Make Network Connected
    problems.append(make_problem(
        pid="graph-m-make-network-connected", title="Make Network Connected (Cable Transfer)",
        wing_id="graphs", floor=346, difficulty="medium", visualizer_type="graph",
        monster_name="Conduit Weaver", monster_title="Re-Router of Spare Relays",
        monster_sprite="spectre", monster_color="#10b981", monster_attack="Network Patch",
        monster_quote="Redundant cables moved to connect disconnected server clusters!",
        description="There are `n` computers numbered from 0 to `n - 1` connected by ethernet cables `connections`. You can extract in-place redundant cables and re-route them between any pair of disconnected computers. Return the minimum number of times you need to do this to make all computers connected. If it is impossible, return -1.",
        examples=[{"input": "n = 4, connections = [[0,1],[0,2],[1,2]]", "output": "1"}, {"input": "n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]", "output": "2"}, {"input": "n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]", "output": "-1"}],
        constraints=["1 <= n <= 100000", "1 <= connections.length <= 100000"],
        function_name="makeConnected",
        starter_code="def makeConnected(n: int, connections: list[list[int]]) -> int:\n    pass\n",
        solution_code="def makeConnected(n: int, connections: list[list[int]]) -> int:\n    if len(connections) < n - 1: return -1\n    parent = list(range(n))\n    def find(i):\n        if parent[i] == i: return i\n        parent[i] = find(parent[i])\n        return parent[i]\n    components = n\n    for u, v in connections:\n        ru, rv = find(u), find(v)\n        if ru != rv:\n            parent[ru] = rv\n            components -= 1\n    return components - 1\n",
        test_cases=[{"input": [4, [[0, 1], [0, 2], [1, 2]]], "expected": 1}, {"input": [6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]], "expected": 2}, {"input": [6, [[0, 1], [0, 2], [0, 3], [1, 2]]], "expected": -1}],
        hints=["Need at least n - 1 cables. Result is the number of disconnected components minus 1."],
        leetcode_id=1319
    ))

    # 47. Accounts Merge
    problems.append(make_problem(
        pid="graph-m-accounts-merge", title="Accounts Merge (Email Graph Components)",
        wing_id="graphs", floor=347, difficulty="medium", visualizer_type="graph",
        monster_name="Identity Chimera", monster_title="Consolidator of Alias Personas",
        monster_sprite="manticore", monster_color="#ec4899", monster_attack="Alias Union",
        monster_quote="All connected email aliases merged under unified account names!",
        description="Given a list of `accounts` where each element `accounts[i]` is a list of strings, where the first element `accounts[i][0]` is a name, and the rest of the elements are emails representing emails of the account. Two accounts belong to the same person if there is some common email. Merge the accounts: each merged account will have the name followed by sorted emails.",
        examples=[{"input": "accounts = [[\"John\",\"johnsmith@mail.com\",\"john_newyork@mail.com\"],[\"John\",\"johnsmith@mail.com\",\"john00@mail.com\"],[\"Mary\",\"mary@mail.com\"],[\"John\",\"johnnybravo@mail.com\"]]", "output": "[[\"John\",\"john00@mail.com\",\"john_newyork@mail.com\",\"johnsmith@mail.com\"],[\"Mary\",\"mary@mail.com\"],[\"John\",\"johnnybravo@mail.com\"]]"}],
        constraints=["1 <= accounts.length <= 1000"],
        function_name="accountsMerge",
        starter_code="def accountsMerge(accounts: list[list[str]]) -> list[list[str]]:\n    pass\n",
        solution_code="def accountsMerge(accounts: list[list[str]]) -> list[list[str]]:\n    from collections import defaultdict\n    parent = {}\n    email_to_name = {}\n    def find(x):\n        if parent[x] == x: return x\n        parent[x] = find(parent[x])\n        return parent[x]\n    for acc in accounts:\n        name = acc[0]\n        first_email = acc[1]\n        for email in acc[1:]:\n            if email not in parent: parent[email] = email\n            email_to_name[email] = name\n            parent[find(email)] = find(first_email)\n    groups = defaultdict(list)\n    for email in parent:\n        groups[find(email)].append(email)\n    res = []\n    for root, emails in groups.items():\n        res.append([email_to_name[root]] + sorted(emails))\n    return sorted(res)\n",
        test_cases=[{"input": [[["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]], "expected": [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]}],
        hints=["Union emails within each account. Group all emails by set representative."],
        leetcode_id=721
    ))

    # 48. Snakes and Ladders
    problems.append(make_problem(
        pid="graph-m-snakes-and-ladders", title="Snakes and Ladders BFS",
        wing_id="graphs", floor=348, difficulty="medium", visualizer_type="grid",
        monster_name="Viper King", monster_title="Coiler of Boustrophedon Boards",
        monster_sprite="boss", monster_color="#eab308", monster_attack="Venomous Slide",
        monster_quote="Least dice rolls to reach the final square computed!",
        description="You are given an `n x n` integer matrix `board` where the cells are labeled from 1 to `n^2` in a Boustrophedon (zigzag) style from bottom-left. Return the least number of dice rolls required to reach cell `n^2`. If it is not possible, return -1.",
        examples=[{"input": "board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]", "output": "4"}],
        constraints=["2 <= n <= 20"],
        function_name="snakesAndLadders",
        starter_code="def snakesAndLadders(board: list[list[int]]) -> int:\n    pass\n",
        solution_code="def snakesAndLadders(board: list[list[int]]) -> int:\n    n = len(board)\n    def get_rc(sq):\n        r = (sq - 1) // n\n        c = (sq - 1) % n\n        if r % 2 == 1: c = n - 1 - c\n        return n - 1 - r, c\n    from collections import deque\n    q = deque([(1, 0)])\n    visited = {1}\n    while q:\n        sq, moves = q.popleft()\n        if sq == n * n: return moves\n        for nxt in range(sq + 1, min(sq + 6, n * n) + 1):\n            r, c = get_rc(nxt)\n            dest = board[r][c] if board[r][c] != -1 else nxt\n            if dest not in visited:\n                visited.add(dest)\n                q.append((dest, moves + 1))\n    return -1\n",
        test_cases=[{"input": [[[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]], "expected": 4}, {"input": [[[-1, -1], [-1, 3]]], "expected": 1}],
        hints=["BFS from square 1. Convert square index to (row, col) handling alternating directions."],
        leetcode_id=909
    ))

    # 49. Jump Game III
    problems.append(make_problem(
        pid="graph-m-jump-game-iii", title="Jump Game III (Reach Zero Value)",
        wing_id="graphs", floor=349, difficulty="medium", visualizer_type="array",
        monster_name="Hopping Spectre", monster_title="Leaper of Symmetric Offsets",
        monster_sprite="wraith", monster_color="#38bdf8", monster_attack="Elastic Warp",
        monster_quote="Can an element of value 0 be reached via +/- arr[i] leaps?",
        description="Given an array of non-negative integers `arr`, and you are initially positioned at `start` index of the array. When you are at index `i`, you can jump to `i + arr[i]` or `i - arr[i]`. Check if you can reach any index with the value 0.",
        examples=[{"input": "arr = [4,2,3,0,3,1,2], start = 5", "output": "True"}, {"input": "arr = [4,2,3,0,3,1,2], start = 0", "output": "True"}, {"input": "arr = [3,0,2,1,2], start = 2", "output": "False"}],
        constraints=["1 <= arr.length <= 50000", "0 <= start < arr.length"],
        function_name="canReach",
        starter_code="def canReach(arr: list[int], start: int) -> bool:\n    pass\n",
        solution_code="def canReach(arr: list[int], start: int) -> bool:\n    from collections import deque\n    n = len(arr)\n    q = deque([start])\n    visited = {start}\n    while q:\n        curr = q.popleft()\n        if arr[curr] == 0: return True\n        for nxt in (curr + arr[curr], curr - arr[curr]):\n            if 0 <= nxt < n and nxt not in visited:\n                visited.add(nxt)\n                q.append(nxt)\n    return False\n",
        test_cases=[{"input": [[4, 2, 3, 0, 3, 1, 2], 5], "expected": True}, {"input": [[4, 2, 3, 0, 3, 1, 2], 0], "expected": True}, {"input": [[3, 0, 2, 1, 2], 2], "expected": False}],
        hints=["Standard BFS/DFS on directed graph where each node i has edges to i + arr[i] and i - arr[i]."],
        leetcode_id=1306
    ))

    # 50. Minimum Jumps to Reach Home
    problems.append(make_problem(
        pid="graph-m-min-jumps-home", title="Minimum Jumps to Reach Home (Forward/Backward)",
        wing_id="graphs", floor=350, difficulty="medium", visualizer_type="array",
        monster_name="Bounder Goblin", monster_title="Skipper of Forbidden Trapdoors",
        monster_sprite="goblin", monster_color="#10b981", monster_attack="Leaping Trample",
        monster_quote="Shortest jump sequence to target location x without double back-jumps!",
        description="A certain bug's home is at position `x` on the number line. It starts at position 0. It can jump forward `a` steps or backward `b` steps. It cannot jump backward twice in a row. It cannot visit positions in `forbidden` or negative positions. Return the minimum number of jumps needed to reach `x`, or -1 if impossible.",
        examples=[{"input": "forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9", "output": "3"}, {"input": "forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11", "output": "-1"}],
        constraints=["1 <= forbidden.length <= 1000", "1 <= a, b, x <= 2000"],
        function_name="minimumJumps",
        starter_code="def minimumJumps(forbidden: list[int], a: int, b: int, x: int) -> int:\n    pass\n",
        solution_code="def minimumJumps(forbidden: list[int], a: int, b: int, x: int) -> int:\n    from collections import deque\n    forbid = set(forbidden)\n    limit = 6000\n    q = deque([(0, 0, False)])  # (pos, steps, just_backed)\n    visited = {(0, False)}\n    while q:\n        pos, steps, backed = q.popleft()\n        if pos == x: return steps\n        # Jump forward\n        nxt_f = pos + a\n        if nxt_f <= limit and nxt_f not in forbid and (nxt_f, False) not in visited:\n            visited.add((nxt_f, False))\n            q.append((nxt_f, steps + 1, False))\n        # Jump backward\n        if not backed:\n            nxt_b = pos - b\n            if nxt_b >= 0 and nxt_b not in forbid and (nxt_b, True) not in visited:\n                visited.add((nxt_b, True))\n                q.append((nxt_b, steps + 1, True))\n    return -1\n",
        test_cases=[{"input": [[14, 4, 18, 1, 15], 3, 15, 9], "expected": 3}, {"input": [[8, 3, 16, 6, 12, 20], 15, 13, 11], "expected": -1}],
        hints=["BFS state is (position, did_jump_back_just_now). Upper bound is max(x, max(forbidden)) + a + b."],
        leetcode_id=1654
    ))

    # 51. Longest Path in DAG
    problems.append(make_problem(
        pid="graph-m-longest-path-dag", title="Longest Path in Directed Acyclic Graph",
        wing_id="graphs", floor=351, difficulty="medium", visualizer_type="graph",
        monster_name="Chronos Wyrm", monster_title="Extender of Directed Temporal Horizons",
        monster_sprite="dragon", monster_color="#8b5cf6", monster_attack="Acyclic Stretch",
        monster_quote="Maximum length of a directed simple path in the DAG computed!",
        description="Given a directed acyclic graph (DAG) of `n` nodes (0 to n - 1) and directed `edges`, return the maximum length (number of edges) of any directed path in the DAG.",
        examples=[{"input": "n = 4, edges = [[0,1],[1,2],[2,3],[0,2]]", "output": "3"}],
        constraints=["1 <= n <= 1000", "0 <= edges.length <= 5000"],
        function_name="longestPathDAG",
        starter_code="def longestPathDAG(n: int, edges: list[list[int]]) -> int:\n    pass\n",
        solution_code="def longestPathDAG(n: int, edges: list[list[int]]) -> int:\n    from collections import defaultdict\n    adj = defaultdict(list)\n    for u, v in edges:\n        adj[u].append(v)\n    memo = {}\n    def dfs(u):\n        if u in memo: return memo[u]\n        ans = 0\n        for v in adj[u]:\n            ans = max(ans, 1 + dfs(v))\n        memo[u] = ans\n        return ans\n    return max([dfs(i) for i in range(n)], default=0)\n",
        test_cases=[{"input": [4, [[0, 1], [1, 2], [2, 3], [0, 2]]], "expected": 3}, {"input": [3, [[0, 1], [0, 2]]], "expected": 1}, {"input": [2, []], "expected": 0}],
        hints=["Memoized DFS or DP along topological ordering."],
        leetcode_id=0
    ))

    # 52. Shortest Cycle Length in Undirected Graph
    problems.append(make_problem(
        pid="graph-m-shortest-cycle-length", title="Shortest Cycle in Undirected Graph (Girth)",
        wing_id="graphs", floor=352, difficulty="medium", visualizer_type="graph",
        monster_name="Ouroboros Golem", monster_title="Measurer of Minimal Loops",
        monster_sprite="golem", monster_color="#ef4444", monster_attack="Girth Clench",
        monster_quote="The girth (minimum cycle length) of the graph found!",
        description="Given `n` nodes (0 to n - 1) and undirected `edges`, return the length of the shortest cycle in the graph. If no cycle exists, return -1.",
        examples=[{"input": "n = 4, edges = [[0,1],[0,2],[1,2],[0,3]]", "output": "3"}, {"input": "n = 4, edges = [[0,1],[1,2],[2,3]]", "output": "-1"}],
        constraints=["1 <= n <= 1000", "edges.length <= 1000"],
        function_name="shortestCycleLength",
        starter_code="def shortestCycleLength(n: int, edges: list[list[int]]) -> int:\n    pass\n",
        solution_code="def shortestCycleLength(n: int, edges: list[list[int]]) -> int:\n    from collections import defaultdict, deque\n    adj = defaultdict(list)\n    for u, v in edges:\n        adj[u].append(v)\n        adj[v].append(u)\n    ans = float('inf')\n    for i in range(n):\n        dist = {i: 0}\n        q = deque([(i, -1)])\n        while q:\n            u, parent = q.popleft()\n            for v in adj[u]:\n                if v not in dist:\n                    dist[v] = dist[u] + 1\n                    q.append((v, u))\n                elif v != parent:\n                    ans = min(ans, dist[u] + dist[v] + 1)\n    return ans if ans != float('inf') else -1\n",
        test_cases=[{"input": [4, [[0, 1], [0, 2], [1, 2], [0, 3]]], "expected": 3}, {"input": [4, [[0, 1], [1, 2], [2, 3]]], "expected": -1}],
        hints=["Run BFS from each node to find the shortest back-edge cycle."],
        leetcode_id=2608
    ))

    # 53. Find All Groups of Farmland
    problems.append(make_problem(
        pid="graph-m-groups-of-farmland", title="Find All Groups of Farmland",
        wing_id="graphs", floor=353, difficulty="medium", visualizer_type="grid",
        monster_name="Harvest Fiend", monster_title="Reaper of Rectangular Plots",
        monster_sprite="demon", monster_color="#22c55e", monster_attack="Scythe Cleave",
        monster_quote="Bounding coordinates [r1, c1, r2, c2] for every farmland rectangular plot mapped!",
        description="You are given an `m x n` binary matrix `land` where 0 represents forest and 1 represents farmland. Farmland forms contiguous rectangular groups. Return a 2D array containing the 4-index coordinates `[r1, c1, r2, c2]` of each farmland group in sorted order.",
        examples=[{"input": "land = [[1,0,0],[0,1,1],[0,1,1]]", "output": "[[0,0,0,0],[1,1,2,2]]"}],
        constraints=["1 <= m, n <= 300"],
        function_name="findFarmland",
        starter_code="def findFarmland(land: list[list[int]]) -> list[list[int]]:\n    pass\n",
        solution_code="def findFarmland(land: list[list[int]]) -> list[list[int]]:\n    R, C = len(land), len(land[0])\n    res = []\n    for r in range(R):\n        for c in range(C):\n            if land[r][c] == 1:\n                if (r > 0 and land[r - 1][c] == 1) or (c > 0 and land[r][c - 1] == 1):\n                    continue\n                r2, c2 = r, c\n                while r2 + 1 < R and land[r2 + 1][c] == 1: r2 += 1\n                while c2 + 1 < C and land[r][c2 + 1] == 1: c2 += 1\n                res.append([r, c, r2, c2])\n    return res\n",
        test_cases=[{"input": [[[1, 0, 0], [0, 1, 1], [0, 1, 1]]], "expected": [[0, 0, 0, 0], [1, 1, 2, 2]]}, {"input": [[[0, 0], [0, 0]]], "expected": []}],
        hints=["Identify the top-left corner of each rectangle (has 0 or border above and left) and extend down and right."],
        leetcode_id=1992
    ))

    # 54. Detonate the Maximum Bombs
    problems.append(make_problem(
        pid="graph-m-detonate-max-bombs", title="Detonate Maximum Bombs (Chain Reaction)",
        wing_id="graphs", floor=354, difficulty="medium", visualizer_type="graph",
        monster_name="Combustion Fiend", monster_title="Igniter of Chain Blasts",
        monster_sprite="beholder", monster_color="#ef4444", monster_attack="Blast Cascade",
        monster_quote="Maximum explosive chain reaction count detonated!",
        description="You are given a list of `bombs`. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the contents of `bombs[i] = [xi, yi, ri]`. If a bomb detonates, it triggers all other bombs within its blast radius. Return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.",
        examples=[{"input": "bombs = [[2,1,3],[6,1,4]]", "output": "2"}, {"input": "bombs = [[1,1,5],[10,10,5]]", "output": "1"}],
        constraints=["1 <= bombs.length <= 100"],
        function_name="maximumDetonation",
        starter_code="def maximumDetonation(bombs: list[list[int]]) -> int:\n    pass\n",
        solution_code="def maximumDetonation(bombs: list[list[int]]) -> int:\n    n = len(bombs)\n    from collections import defaultdict\n    adj = defaultdict(list)\n    for i in range(n):\n        x1, y1, r1 = bombs[i]\n        for j in range(n):\n            if i != j:\n                x2, y2, _ = bombs[j]\n                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1 ** 2:\n                    adj[i].append(j)\n    def dfs(u, visited):\n        visited.add(u)\n        for v in adj[u]:\n            if v not in visited:\n                dfs(v, visited)\n    ans = 0\n    for i in range(n):\n        vis = set()\n        dfs(i, vis)\n        ans = max(ans, len(vis))\n    return ans\n",
        test_cases=[{"input": [[[2, 1, 3], [6, 1, 4]]], "expected": 2}, {"input": [[[1, 1, 5], [10, 10, 5]]], "expected": 1}, {"input": [[[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]], "expected": 5}],
        hints=["Directed reachability graph where edge i -> j exists if dist(i, j) <= r_i. Run DFS from each bomb."],
        leetcode_id=2101
    ))

    # 55. Minimum Score of a Path Between Two Cities
    problems.append(make_problem(
        pid="graph-m-min-score-path-cities", title="Minimum Score of a Path Between Two Cities",
        wing_id="graphs", floor=355, difficulty="medium", visualizer_type="graph",
        monster_name="Lowest Valley Spirit", monster_title="Seeker of Minimum Road Clearance",
        monster_sprite="wraith", monster_color="#06b6d4", monster_attack="Depression Mist",
        monster_quote="Smallest edge weight in the connected component containing cities 1 and n found!",
        description="You are given a positive integer `n` representing `n` cities numbered from 1 to `n`. You are also given a 2D array `roads` where `roads[i] = [ui, vi, distancei]`. The score of a path is defined as the minimum distance of a road in this path. Return the minimum possible score of a path between city 1 and city `n`.",
        examples=[{"input": "n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]", "output": "5"}],
        constraints=["2 <= n <= 100000", "1 <= roads.length <= 100000"],
        function_name="minScore",
        starter_code="def minScore(n: int, roads: list[list[int]]) -> int:\n    pass\n",
        solution_code="def minScore(n: int, roads: list[list[int]]) -> int:\n    from collections import defaultdict, deque\n    adj = defaultdict(list)\n    for u, v, d in roads:\n        adj[u].append((v, d))\n        adj[v].append((u, d))\n    visited = set([1])\n    q = deque([1])\n    min_dist = float('inf')\n    while q:\n        u = q.popleft()\n        for v, d in adj[u]:\n            min_dist = min(min_dist, d)\n            if v not in visited:\n                visited.add(v)\n                q.append(v)\n    return min_dist\n",
        test_cases=[{"input": [4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]], "expected": 5}, {"input": [4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]]], "expected": 2}],
        hints=["Since paths can revisit edges freely, the answer is simply the minimum weight among all edges in the connected component of 1."],
        leetcode_id=2492
    ))

    return problems
