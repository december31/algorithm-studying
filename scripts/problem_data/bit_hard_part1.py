from scripts.problem_data.common import make_problem
from bisect import bisect_left
from collections import Counter
import math

def get_bit_hard_part1():
    problems = []

    # 71. Maximum XOR with an Element From Array (LC 1707)
    problems.append(make_problem(
        pid="bit-h-max-xor-element-bound", title="Bounded Maximum XOR",
        wing_id="bit-manipulation", floor=571, difficulty="hard", visualizer_type="array",
        monster_name="XOR Threshold Behemoth", monster_title="Guardian of the Upper Limit",
        monster_sprite="dragon", monster_color="#dc2626", monster_attack="Capped Voltage Burst",
        monster_quote="Exceed the bound mi and your XOR shall be denied!",
        description="Given an array `nums` of non-negative integers and a 2D array `queries` where `queries[i] = [xi, mi]`. The answer to query `i` is the maximum bitwise XOR value of `xi` with any element in `nums` that is `<= mi`. If all elements in `nums` are `> mi`, the answer is `-1`. Return an array of the answers to all queries.",
        examples=[
            {"input": "nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]", "output": "[3,3,7]"},
            {"input": "nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]", "output": "[15,-1,5]"}
        ],
        constraints=["1 <= nums.length, queries.length <= 10^5", "0 <= nums[j], xi, mi <= 10^9"],
        function_name="maximizeXor",
        starter_code="def maximizeXor(nums: list[int], queries: list[list[int]]) -> list[int]:\n    pass\n",
        solution_code="def maximizeXor(nums: list[int], queries: list[list[int]]) -> list[int]:\n    nums.sort()\n    indexed_q = sorted([(m, x, i) for i, (x, m) in enumerate(queries)])\n    ans = [-1] * len(queries)\n    trie = {}\n    idx = 0\n    n = len(nums)\n    def insert(num):\n        node = trie\n        for b in range(30, -1, -1):\n            bit = (num >> b) & 1\n            if bit not in node: node[bit] = {}\n            node = node[bit]\n    def query_max(x):\n        if not trie: return -1\n        node = trie\n        res = 0\n        for b in range(30, -1, -1):\n            bit = (x >> b) & 1\n            opp = 1 - bit\n            if opp in node:\n                res |= (1 << b)\n                node = node[opp]\n            else:\n                node = node[bit]\n        return res\n    for m, x, orig_idx in indexed_q:\n        while idx < n and nums[idx] <= m:\n            insert(nums[idx])\n            idx += 1\n        ans[orig_idx] = query_max(x)\n    return ans\n",
        test_cases=[
            {"input": [[0,1,2,3,4], [[3,1],[1,3],[5,6]]], "expected": [3, 3, 7]},
            {"input": [[5,2,4,6,6,3], [[12,4],[8,1],[6,3]]], "expected": [15, -1, 5]}
        ],
        hints=["Sort queries by mi and nums in ascending order. Add elements into a 0-1 Trie as mi increases."],
        leetcode_id=1707
    ))

    # 72. Find Shortest Superstring Length (LC 943)
    problems.append(make_problem(
        pid="bit-h-shortest-superstring-len", title="Shortest Superstring Length",
        wing_id="bit-manipulation", floor=572, difficulty="hard", visualizer_type="array",
        monster_name="String Stitcher Wyrm", monster_title="Weaver of Overlapping Runes",
        monster_sprite="golem", monster_color="#a855f7", monster_attack="Prefix Suffix Merge",
        monster_quote="Merge our ancient fragments with optimal bitmask overlap!",
        description="Given an array of strings `words`, return the length of the shortest string that contains each string in `words` as a substring. (You may assume no string in `words` is a substring of another).",
        examples=[
            {"input": "words = [\"alex\",\"loves\",\"leetcode\"]", "output": "17"},
            {"input": "words = [\"catg\",\"ctaagt\",\"gcta\",\"ttca\",\"atgcatc\"]", "output": "16"}
        ],
        constraints=["1 <= words.length <= 12", "1 <= words[i].length <= 20"],
        function_name="shortestSuperstringLength",
        starter_code="def shortestSuperstringLength(words: list[str]) -> int:\n    pass\n",
        solution_code="def shortestSuperstringLength(words: list[str]) -> int:\n    n = len(words)\n    cost = [[0] * n for _ in range(n)]\n    for i in range(n):\n        for j in range(n):\n            if i != j:\n                for k in range(min(len(words[i]), len(words[j])), 0, -1):\n                    if words[i].endswith(words[j][:k]):\n                        cost[i][j] = k\n                        break\n    dp = [[float('inf')] * n for _ in range(1 << n)]\n    for i in range(n):\n        dp[1 << i][i] = len(words[i])\n    for mask in range(1 << n):\n        for last in range(n):\n            if not (mask & (1 << last)) or dp[mask][last] == float('inf'): continue\n            for nxt in range(n):\n                if not (mask & (1 << nxt)):\n                    new_mask = mask | (1 << nxt)\n                    new_len = dp[mask][last] + len(words[nxt]) - cost[last][nxt]\n                    if new_len < dp[new_mask][nxt]:\n                        dp[new_mask][nxt] = new_len\n    return min(dp[(1 << n) - 1])\n",
        test_cases=[
            {"input": [["alex","loves","leetcode"]], "expected": 17},
            {"input": [["catg","ctaagt","gcta","ttca","atgcatc"]], "expected": 16}
        ],
        hints=["Precompute overlap between word pairs. Use bitmask DP dp[mask][last] representing min length visited mask ending with last."],
        leetcode_id=943
    ))

    # 73. Number of Valid Words for Each Puzzle (LC 1178)
    problems.append(make_problem(
        pid="bit-h-valid-words-puzzle", title="Valid Words for Each Puzzle",
        wing_id="bit-manipulation", floor=573, difficulty="hard", visualizer_type="array",
        monster_name="Puzzle Sphinx", monster_title="Keeper of Key Characters",
        monster_sprite="ghost", monster_color="#6366f1", monster_attack="Riddle of the Submasks",
        monster_quote="First letter must stand firm, all other runes must match the puzzle!",
        description="Given words and puzzles. A word is valid for a puzzle if:\n1. It contains the first letter of the puzzle.\n2. Every letter in word is present in puzzle.\nReturn an array `ans` where `ans[i]` is the number of words valid for `puzzles[i]`.",
        examples=[
            {"input": "words = [\"aaaa\",\"asas\",\"able\",\"ability\",\"actt\",\"actor\",\"access\"], puzzles = [\"aboveyz\",\"abrodyz\",\"abslute\",\"absoryz\",\"actresz\",\"gaswxyz\"]", "output": "[1,1,3,2,4,0]"}
        ],
        constraints=["1 <= words.length <= 10^5", "puzzles[i].length == 7"],
        function_name="findNumOfValidWords",
        starter_code="def findNumOfValidWords(words: list[str], puzzles: list[str]) -> list[int]:\n    pass\n",
        solution_code="def findNumOfValidWords(words: list[str], puzzles: list[str]) -> list[int]:\n    from collections import Counter\n    word_counts = Counter()\n    for w in words:\n        mask = 0\n        for ch in set(w):\n            mask |= (1 << (ord(ch) - ord('a')))\n        if bin(mask).count('1') <= 7:\n            word_counts[mask] += 1\n    ans = []\n    for p in puzzles:\n        first = 1 << (ord(p[0]) - ord('a'))\n        rest_mask = 0\n        for ch in p[1:]:\n            rest_mask |= (1 << (ord(ch) - ord('a')))\n        count = 0\n        submask = rest_mask\n        while True:\n            count += word_counts[submask | first]\n            if submask == 0: break\n            submask = (submask - 1) & rest_mask\n        ans.append(count)\n    return ans\n",
        test_cases=[
            {"input": [["aaaa","asas","able","ability","actt","actor","access"], ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]], "expected": [1, 1, 3, 2, 4, 0]}
        ],
        hints=["Since each puzzle has only 7 letters, iterate over all 2^6 = 64 submasks of the remaining 6 letters combined with the first letter."],
        leetcode_id=1178
    ))

    # 74. Count Subtrees With Max Distance Between Cities (LC 1617)
    problems.append(make_problem(
        pid="bit-h-subtrees-max-distance", title="Subtrees with Maximum Distance",
        wing_id="bit-manipulation", floor=574, difficulty="hard", visualizer_type="graph",
        monster_name="Arboreal Leviathan", monster_title="Ruler of Tree Subgraph Diameters",
        monster_sprite="boss", monster_color="#ef4444", monster_attack="Branch Distance Shockwave",
        monster_quote="Every subset of nodes forms a realm; measure their furthest reaches!",
        description="There are `n` cities numbered `1` to `n`. You are given an integer `n` and an array `edges` where `edges[i] = [u, v]` represents a bidirectional edge between `u` and `v` forming a tree. Return an array of size `n - 1` where the `d-th` element (1-indexed) is the number of subtrees in which the maximum distance between any two cities in the subtree is equal to `d`.",
        examples=[
            {"input": "n = 4, edges = [[1,2],[2,3],[2,4]]", "output": "[3,4,0]"},
            {"input": "n = 2, edges = [[1,2]]", "output": "[1]"}
        ],
        constraints=["2 <= n <= 15", "edges.length == n - 1"],
        function_name="countSubgraphsForEachDiameter",
        starter_code="def countSubgraphsForEachDiameter(n: int, edges: list[list[int]]) -> list[int]:\n    pass\n",
        solution_code="def countSubgraphsForEachDiameter(n: int, edges: list[list[int]]) -> list[int]:\n    dist = [[float('inf')] * n for _ in range(n)]\n    for i in range(n): dist[i][i] = 0\n    adj = [[] for _ in range(n)]\n    for u, v in edges:\n        u -= 1; v -= 1\n        dist[u][v] = dist[v][u] = 1\n        adj[u].append(v); adj[v].append(u)\n    for k in range(n):\n        for i in range(n):\n            for j in range(n):\n                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])\n    ans = [0] * (n - 1)\n    for mask in range(1, 1 << n):\n        nodes = [i for i in range(n) if (mask & (1 << i))]\n        if len(nodes) < 2: continue\n        edge_count = 0\n        for u, v in edges:\n            if (mask & (1 << (u - 1))) and (mask & (1 << (v - 1))):\n                edge_count += 1\n        if edge_count != len(nodes) - 1: continue\n        q = [nodes[0]]\n        visited = {nodes[0]}\n        while q:\n            curr = q.pop(0)\n            for neighbor in adj[curr]:\n                if (mask & (1 << neighbor)) and neighbor not in visited:\n                    visited.add(neighbor)\n                    q.append(neighbor)\n        if len(visited) != len(nodes): continue\n        max_d = 0\n        for i in nodes:\n            for j in nodes:\n                max_d = max(max_d, dist[i][j])\n        if 1 <= max_d <= n - 1:\n            ans[max_d - 1] += 1\n    return ans\n",
        test_cases=[
            {"input": [4, [[1,2],[2,3],[2,4]]], "expected": [3, 4, 0]},
            {"input": [2, [[1,2]]], "expected": [1]}
        ],
        hints=["Enumerate all 2^n masks. Verify that mask induces a connected tree (num_edges == num_nodes - 1 and connected), then calculate diameter using Floyd-Warshall distances."],
        leetcode_id=1617
    ))

    # 75. Minimum Incompatibility (LC 1681)
    problems.append(make_problem(
        pid="bit-h-min-incompatibility", title="Minimum Incompatibility Partition",
        wing_id="bit-manipulation", floor=575, difficulty="hard", visualizer_type="array",
        monster_name="Partition Chimera", monster_title="Distributor of Equal Factions",
        monster_sprite="dragon", monster_color="#f59e0b", monster_attack="Spread Difference",
        monster_quote="Partition with unique elements or face infinite discord!",
        description="You are given an integer array `nums` of length `n` and an integer `k`. You need to distribute `nums` into `k` subsets each of size `n / k` such that no two elements in the same subset are equal. The incompatibility of a subset is `max - min`. Return the minimum total incompatibility of the `k` subsets, or `-1` if it is impossible.",
        examples=[
            {"input": "nums = [1,2,1,4], k = 2", "output": "4"},
            {"input": "nums = [6,3,8,1,3,1,2,2], k = 4", "output": "6"},
            {"input": "nums = [5,5,5,5], k = 2", "output": "-1"}
        ],
        constraints=["1 <= k <= nums.length <= 16", "nums.length is divisible by k"],
        function_name="minimumIncompatibility",
        starter_code="def minimumIncompatibility(nums: list[int], k: int) -> int:\n    pass\n",
        solution_code="def minimumIncompatibility(nums: list[int], k: int) -> int:\n    from collections import Counter\n    counts = Counter(nums)\n    if any(c > k for c in counts.values()): return -1\n    n = len(nums)\n    sz = n // k\n    if sz == 1: return 0\n    valid_subsets = {}\n    for mask in range(1 << n):\n        if bin(mask).count('1') == sz:\n            elements = [nums[i] for i in range(n) if (mask & (1 << i))]\n            if len(set(elements)) == sz:\n                valid_subsets[mask] = max(elements) - min(elements)\n    dp = {0: 0}\n    for mask in range(1 << n):\n        if mask not in dp: continue\n        first_unset = 0\n        while first_unset < n and (mask & (1 << first_unset)):\n            first_unset += 1\n        if first_unset == n: continue\n        for submask, cost in valid_subsets.items():\n            if (submask & (1 << first_unset)) and (mask & submask) == 0:\n                nxt = mask | submask\n                if nxt not in dp or dp[mask] + cost < dp[nxt]:\n                    dp[nxt] = dp[mask] + cost\n    target = (1 << n) - 1\n    return dp.get(target, -1)\n",
        test_cases=[
            {"input": [[1,2,1,4], 2], "expected": 4},
            {"input": [[6,3,8,1,3,1,2,2], 4], "expected": 6},
            {"input": [[5,5,5,5], 2], "expected": -1}
        ],
        hints=["Precompute valid subsets of size n//k with distinct values. Fix the first unset element to avoid permutation redundancy in bitmask DP."],
        leetcode_id=1681
    ))

    # 76. Chalkboard XOR Game (LC 810)
    problems.append(make_problem(
        pid="bit-h-chalkboard-xor-game", title="Chalkboard XOR Game",
        wing_id="bit-manipulation", floor=576, difficulty="hard", visualizer_type="array",
        monster_name="Nim Chalkboard Titan", monster_title="Arbiter of Parity and Nil-Sum",
        monster_sprite="boss", monster_color="#8b5cf6", monster_attack="Erasure Paradox",
        monster_quote="If the initial XOR is zero, or the count is even, victory belongs to Alice!",
        description="Alice and Bob play a game on a chalkboard containing an array `nums`. In each turn, a player chooses an integer from chalkboard and erases it. If erasing a number causes the bitwise XOR sum of all remaining numbers on chalkboard to become `0`, that player loses. Also, if the initial XOR sum of all numbers is already `0`, Alice wins immediately. Given `nums`, return `True` if Alice wins assuming both players play optimally, or `False` otherwise.",
        examples=[
            {"input": "nums = [1,1,2]", "output": "False"},
            {"input": "nums = [0,1]", "output": "True"},
            {"input": "nums = [1,2,3]", "output": "True"}
        ],
        constraints=["1 <= nums.length <= 1000", "0 <= nums[i] < 2^16"],
        function_name="xorGame",
        starter_code="def xorGame(nums: list[int]) -> bool:\n    pass\n",
        solution_code="def xorGame(nums: list[int]) -> bool:\n    total_xor = 0\n    for x in nums: total_xor ^= x\n    return total_xor == 0 or len(nums) % 2 == 0\n",
        test_cases=[
            {"input": [[1, 1, 2]], "expected": False},
            {"input": [[0, 1]], "expected": True},
            {"input": [[1, 2, 3]], "expected": True}
        ],
        hints=["If total XOR == 0, Alice wins right away. If len(nums) is even and total XOR != 0, Alice can always pick a number such that remaining XOR != 0."],
        leetcode_id=810
    ))

    # 77. Minimum Cost to Connect Two Groups of Points (LC 1595)
    problems.append(make_problem(
        pid="bit-h-min-cost-connect-groups", title="Minimum Cost to Connect Two Groups",
        wing_id="bit-manipulation", floor=577, difficulty="hard", visualizer_type="grid",
        monster_name="Bipartite Bridge Giant", monster_title="Binder of Disconnected Realities",
        monster_sprite="golem", monster_color="#10b981", monster_attack="Group Tether",
        monster_quote="Every point on both sides must be bound to at least one counterpart!",
        description="You are given two groups of points: group 1 with `sz1` points and group 2 with `sz2` points (`sz1 >= sz2`). `cost[i][j]` is the cost of connecting point `i` of group 1 to point `j` of group 2. Every point in both groups must be connected to at least one point in the other group. Return the minimum cost to achieve this.",
        examples=[
            {"input": "cost = [[15,96],[36,2]]", "output": "17"},
            {"input": "cost = [[1,3,5],[4,1,1],[1,5,3]]", "output": "4"}
        ],
        constraints=["1 <= sz1 <= 12", "1 <= sz2 <= 12", "1 <= cost[i][j] <= 100"],
        function_name="connectTwoGroups",
        starter_code="def connectTwoGroups(cost: list[list[int]]) -> int:\n    pass\n",
        solution_code="def connectTwoGroups(cost: list[list[int]]) -> int:\n    sz1 = len(cost)\n    sz2 = len(cost[0])\n    min_group2 = [min(cost[i][j] for i in range(sz1)) for j in range(sz2)]\n    memo = {}\n    def dp(i, mask):\n        state = (i, mask)\n        if state in memo: return memo[state]\n        if i == sz1:\n            ans = 0\n            for j in range(sz2):\n                if not (mask & (1 << j)):\n                    ans += min_group2[j]\n            return ans\n        res = float('inf')\n        for j in range(sz2):\n            res = min(res, cost[i][j] + dp(i + 1, mask | (1 << j)))\n        memo[state] = res\n        return res\n    return dp(0, 0)\n",
        test_cases=[
            {"input": [[[15, 96], [36, 2]]], "expected": 17},
            {"input": [[[1, 3, 5], [4, 1, 1], [1, 5, 3]]], "expected": 4}
        ],
        hints=["Use DP dp(i, mask) where i is group 1 index and mask is group 2 visited nodes. When i reaches sz1, add min connecting cost for remaining unvisited group 2 nodes."],
        leetcode_id=1595
    ))

    # 78. Parallel Courses II (LC 1494)
    problems.append(make_problem(
        pid="bit-h-parallel-courses-ii", title="Parallel Courses II",
        wing_id="bit-manipulation", floor=578, difficulty="hard", visualizer_type="graph",
        monster_name="Semester Chronomancer", monster_title="Master of Prerequisite Timelines",
        monster_sprite="witch", monster_color="#3b82f6", monster_attack="Semester Leap",
        monster_quote="At most k courses per semester; order your dependencies wisely!",
        description="You are given an integer `n` (courses numbered `1` to `n`), an array `relations` where `relations[i] = [prevCourse, nextCourse]`, and an integer `k`. In one semester, you can take at most `k` courses as long as their prerequisites have all been taken in previous semesters. Return the minimum number of semesters needed to take all courses.",
        examples=[
            {"input": "n = 4, relations = [[2,1],[3,1],[1,4]], k = 2", "output": "3"},
            {"input": "n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2", "output": "4"}
        ],
        constraints=["1 <= n <= 15", "1 <= k <= n", "0 <= relations.length <= n * (n - 1) / 2"],
        function_name="minNumberOfSemesters",
        starter_code="def minNumberOfSemesters(n: int, relations: list[list[int]], k: int) -> int:\n    pass\n",
        solution_code="def minNumberOfSemesters(n: int, relations: list[list[int]], k: int) -> int:\n    prereq = [0] * n\n    for u, v in relations:\n        prereq[v - 1] |= (1 << (u - 1))\n    dp = [float('inf')] * (1 << n)\n    dp[0] = 0\n    for mask in range(1 << n):\n        if dp[mask] == float('inf'): continue\n        available = 0\n        for i in range(n):\n            if not (mask & (1 << i)) and (mask & prereq[i]) == prereq[i]:\n                available |= (1 << i)\n        avail_list = [i for i in range(n) if (available & (1 << i))]\n        from itertools import combinations\n        if len(avail_list) <= k:\n            nxt = mask | available\n            dp[nxt] = min(dp[nxt], dp[mask] + 1)\n        else:\n            for comb in combinations(avail_list, k):\n                submask = sum(1 << i for i in comb)\n                nxt = mask | submask\n                dp[nxt] = min(dp[nxt], dp[mask] + 1)\n    return dp[(1 << n) - 1]\n",
        test_cases=[
            {"input": [4, [[2,1],[3,1],[1,4]], 2], "expected": 3},
            {"input": [5, [[2,1],[3,1],[4,1],[1,5]], 2], "expected": 4}
        ],
        hints=["Store prerequisites as bitmasks. For each reachable state, find all available courses whose prerequisites are satisfied and take up to k of them."],
        leetcode_id=1494
    ))

    # 79. Maximum Students Taking Exam (LC 1349)
    problems.append(make_problem(
        pid="bit-h-max-students-exam", title="Maximum Students Taking Exam",
        wing_id="bit-manipulation", floor=579, difficulty="hard", visualizer_type="grid",
        monster_name="Proctor Specter", monster_title="Inquisitor of Sightlines and Cheating",
        monster_sprite="ghost", monster_color="#ec4899", monster_attack="Cheating Blindspot",
        monster_quote="No student may see the work of left, right, or diagonal peers!",
        description="Given an `m x n` matrix `seats` representing a classroom. If a seat is broken, it is denoted by `'#'`. Otherwise, it is denoted by `'.'`. Students cannot see each other's test sheets. A student can see answers of students sitting directly left, directly right, upper-left, and upper-right. Return the maximum number of students that can take the exam together.",
        examples=[
            {"input": "seats = [[\"#\",\".\",\"#\",\"#\",\".\",\"#\"],[\".\",\"#\",\"#\",\"#\",\"#\",\".\"],[\"#\",\".\",\"#\",\"#\",\".\",\"#\"]]", "output": "4"},
            {"input": "seats = [[\".\",\"#\"],[\"#\",\"#\"],[\"#\",\".\"],[\"#\",\"#\"],[\".\",\"#\"]]", "output": "3"}
        ],
        constraints=["1 <= seats.length, seats[0].length <= 8"],
        function_name="maxStudents",
        starter_code="def maxStudents(seats: list[list[str]]) -> int:\n    pass\n",
        solution_code="def maxStudents(seats: list[list[str]]) -> int:\n    m = len(seats)\n    n = len(seats[0])\n    broken = [0] * m\n    for r in range(m):\n        for c in range(n):\n            if seats[r][c] == '#': broken[r] |= (1 << c)\n    memo = {}\n    def dp(row, prev_mask):\n        if row == m: return 0\n        state = (row, prev_mask)\n        if state in memo: return memo[state]\n        ans = 0\n        for mask in range(1 << n):\n            if (mask & broken[row]) != 0: continue\n            if (mask & (mask >> 1)) != 0: continue\n            if (mask & (prev_mask >> 1)) != 0: continue\n            if (mask & (prev_mask << 1)) != 0: continue\n            ans = max(ans, bin(mask).count('1') + dp(row + 1, mask))\n        memo[state] = ans\n        return ans\n    return dp(0, 0)\n",
        test_cases=[
            {"input": [[["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]], "expected": 4},
            {"input": [[[".","#"],["#","#"],["#","."],["#","#"],[".","#"]]], "expected": 3}
        ],
        hints=["Since n <= 8, use row-by-row bitmask DP. Verify no adjacent bits within the current row, and no diagonal conflicts with prev_mask."],
        leetcode_id=1349
    ))

    # 80. Maximum AND Sum of Array (LC 2172)
    problems.append(make_problem(
        pid="bit-h-max-and-sum-array", title="Maximum AND Sum of Array",
        wing_id="bit-manipulation", floor=580, difficulty="hard", visualizer_type="array",
        monster_name="Trit Slot Overlord", monster_title="Keeper of Base-3 Compartments",
        monster_sprite="boss", monster_color="#f97316", monster_attack="Bitwise Slot Fusion",
        monster_quote="Each slot holds at most two runes, blending powers under bitwise AND!",
        description="You are given an integer array `nums` and an integer `numSlots` such that `2 * numSlots >= nums.length`. There are `numSlots` slots numbered `1` to `numSlots`. Each slot can hold at most `2` numbers. The AND sum of an allocation is the sum of `(x & slot)` for each number `x` placed in slot `slot`. Return the maximum possible AND sum.",
        examples=[
            {"input": "nums = [1,2,3,4,5,6], numSlots = 3", "output": "9"},
            {"input": "nums = [1,3,10,4,7,1], numSlots = 9", "output": "24"}
        ],
        constraints=["1 <= numSlots <= 9", "1 <= nums.length <= 2 * numSlots", "1 <= nums[i] <= 15"],
        function_name="maximumANDSum",
        starter_code="def maximumANDSum(nums: list[int], numSlots: int) -> int:\n    pass\n",
        solution_code="def maximumANDSum(nums: list[int], numSlots: int) -> int:\n    memo = {}\n    n = len(nums)\n    def dp(i, mask):\n        if i == n: return 0\n        state = (i, mask)\n        if state in memo: return memo[state]\n        ans = 0\n        for slot in range(1, numSlots + 1):\n            slot_base = 3 ** (slot - 1)\n            slot_count = (mask // slot_base) % 3\n            if slot_count < 2:\n                val = (nums[i] & slot) + dp(i + 1, mask + slot_base)\n                if val > ans: ans = val\n        memo[state] = ans\n        return ans\n    return dp(0, 0)\n",
        test_cases=[
            {"input": [[1,2,3,4,5,6], 3], "expected": 9},
            {"input": [[1,3,10,4,7,1], 9], "expected": 24}
        ],
        hints=["Represent slot occupancy in base-3 (values 0, 1, or 2). Memoize dp(i, base3_mask)."],
        leetcode_id=2172
    ))

    # 81. Number of Ways to Wear Different Hats (LC 1434)
    problems.append(make_problem(
        pid="bit-h-wear-different-hats", title="Number of Ways to Wear Different Hats",
        wing_id="bit-manipulation", floor=581, difficulty="hard", visualizer_type="array",
        monster_name="Milliner Phantom", monster_title="Distributor of the 40 Enchanted Hats",
        monster_sprite="wizard", monster_color="#8b5cf6", monster_attack="Millinery Mirage",
        monster_quote="40 hats, 10 persons; every hero must don their favored unique helm!",
        description="There are `n` people and `40` types of hats labeled `1` to `40`. Given a list of lists `hats` where `hats[i]` is a list of all hats preferred by the `i-th` person. Return the number of ways that the `n` people can wear different hats. Since the answer may be large, return it modulo `10^9 + 7`.",
        examples=[
            {"input": "hats = [[3,4],[4,5],[5]]", "output": "1"},
            {"input": "hats = [[3,5,1],[3,5]]", "output": "4"},
            {"input": "hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]", "output": "24"}
        ],
        constraints=["n == hats.length <= 10", "1 <= hats[i].length <= 40"],
        function_name="numberWays",
        starter_code="def numberWays(hats: list[list[int]]) -> int:\n    pass\n",
        solution_code="def numberWays(hats: list[list[int]]) -> int:\n    MOD = 10**9 + 7\n    n = len(hats)\n    hat_to_people = [[] for _ in range(41)]\n    for person, preferred in enumerate(hats):\n        for h in preferred:\n            hat_to_people[h].append(person)\n    memo = {}\n    def dp(hat_id, mask):\n        if mask == (1 << n) - 1: return 1\n        if hat_id > 40: return 0\n        state = (hat_id, mask)\n        if state in memo: return memo[state]\n        res = dp(hat_id + 1, mask)\n        for person in hat_to_people[hat_id]:\n            if not (mask & (1 << person)):\n                res = (res + dp(hat_id + 1, mask | (1 << person))) % MOD\n        memo[state] = res\n        return res\n    return dp(1, 0)\n",
        test_cases=[
            {"input": [[[3,4],[4,5],[5]]], "expected": 1},
            {"input": [[[3,5,1],[3,5]]], "expected": 4},
            {"input": [[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]], "expected": 24}
        ],
        hints=["Since n <= 10 is small while hats <= 40 is larger, invert the DP: iterate over hat IDs from 1 to 40, tracking the mask of persons who have been assigned a hat."],
        leetcode_id=1434
    ))

    # 82. Minimum XOR Sum of Two Arrays (LC 1879)
    problems.append(make_problem(
        pid="bit-h-min-xor-sum-two-arrays", title="Minimum XOR Sum of Two Arrays",
        wing_id="bit-manipulation", floor=582, difficulty="hard", visualizer_type="array",
        monster_name="Bipartite XOR Weaver", monster_title="Harmonizer of Paired Bitwise Energy",
        monster_sprite="golem", monster_color="#06b6d4", monster_attack="Resonant XOR Pair",
        monster_quote="Pair every element of the first array to a unique twin in the second!",
        description="You are given two integer arrays `nums1` and `nums2` of length `n`. Rearrange the elements of `nums2` such that the sum of `nums1[i] ^ nums2[i]` for `0 <= i < n` is minimized. Return the minimum XOR sum.",
        examples=[
            {"input": "nums1 = [1,2], nums2 = [2,3]", "output": "2"},
            {"input": "nums1 = [1,0,3], nums2 = [5,3,4]", "output": "8"}
        ],
        constraints=["n == nums1.length == nums2.length <= 14", "0 <= nums1[i], nums2[i] <= 10^7"],
        function_name="minimumXORSum",
        starter_code="def minimumXORSum(nums1: list[int], nums2: list[int]) -> int:\n    pass\n",
        solution_code="def minimumXORSum(nums1: list[int], nums2: list[int]) -> int:\n    n = len(nums1)\n    memo = {}\n    def dp(mask):\n        i = bin(mask).count('1')\n        if i == n: return 0\n        if mask in memo: return memo[mask]\n        res = float('inf')\n        for j in range(n):\n            if not (mask & (1 << j)):\n                res = min(res, (nums1[i] ^ nums2[j]) + dp(mask | (1 << j)))\n        memo[mask] = res\n        return res\n    return dp(0)\n",
        test_cases=[
            {"input": [[1,2], [2,3]], "expected": 2},
            {"input": [[1,0,3], [5,3,4]], "expected": 8}
        ],
        hints=["Since n <= 14, use bitmask DP dp(mask) where the number of set bits in mask indicates how many elements of nums1 have been paired."],
        leetcode_id=1879
    ))

    # 83. Find Minimum Time to Finish All Jobs (LC 1723)
    problems.append(make_problem(
        pid="bit-h-min-time-finish-jobs", title="Minimum Time to Finish All Jobs",
        wing_id="bit-manipulation", floor=583, difficulty="hard", visualizer_type="array",
        monster_name="Workload Arbiter", monster_title="Equalizer of Labor Shifts",
        monster_sprite="boss", monster_color="#e11d48", monster_attack="Load Balancing Strike",
        monster_quote="Distribute all burdens across k workers to minimize the maximum load!",
        description="You are given an integer array `jobs`, where `jobs[i]` is the amount of time it takes to complete the `i-th` job, and an integer `k`. There are `k` workers. Every job should be assigned to exactly one worker. A worker's working time is the sum of times of all jobs assigned to that worker. Return the minimum possible maximum working time of any assignment.",
        examples=[
            {"input": "jobs = [3,2,3], k = 3", "output": "3"},
            {"input": "jobs = [1,2,4,7,8], k = 2", "output": "11"}
        ],
        constraints=["1 <= k <= jobs.length <= 12", "1 <= jobs[i] <= 10^7"],
        function_name="minimumTimeRequired",
        starter_code="def minimumTimeRequired(jobs: list[int], k: int) -> int:\n    pass\n",
        solution_code="def minimumTimeRequired(jobs: list[int], k: int) -> int:\n    jobs.sort(reverse=True)\n    workers = [0] * k\n    best = sum(jobs)\n    def backtrack(idx):\n        nonlocal best\n        if idx == len(jobs):\n            best = min(best, max(workers))\n            return\n        seen = set()\n        for w in range(k):\n            if workers[w] in seen or workers[w] + jobs[idx] >= best:\n                continue\n            seen.add(workers[w])\n            workers[w] += jobs[idx]\n            backtrack(idx + 1)\n            workers[w] -= jobs[idx]\n            if workers[w] == 0: break\n    backtrack(0)\n    return best\n",
        test_cases=[
            {"input": [[3,2,3], 3], "expected": 3},
            {"input": [[1,2,4,7,8], 2], "expected": 11}
        ],
        hints=["Sort jobs descending. Backtrack across workers with symmetry breaking (skip empty workers if one already failed, and prune by current best)."],
        leetcode_id=1723
    ))

    # 84. Distribute Repeating Integers (LC 1655)
    problems.append(make_problem(
        pid="bit-h-distribute-repeating-integers", title="Distribute Repeating Integers",
        wing_id="bit-manipulation", floor=584, difficulty="hard", visualizer_type="array",
        monster_name="Inventory Dragon", monster_title="Hoarder of Uniform Commodities",
        monster_sprite="dragon", monster_color="#ca8a04", monster_attack="Batch Fulfillment",
        monster_quote="Each customer requires identical treasures; fulfill their entire orders!",
        description="You are given an array of integers `nums` and an integer array `quantity` of length `m`. The `i-th` customer requires `quantity[i]` copies of any integer in `nums`. Each customer must receive all copies of the same integer. Return `True` if it is possible to satisfy all `m` customers, or `False` otherwise.",
        examples=[
            {"input": "nums = [1,2,3,4], quantity = [2]", "output": "False"},
            {"input": "nums = [1,2,3,3], quantity = [2]", "output": "True"},
            {"input": "nums = [1,1,2,2], quantity = [2,2]", "output": "True"}
        ],
        constraints=["1 <= nums.length <= 10^5", "1 <= m == quantity.length <= 10", "1 <= quantity[i] <= 10^5"],
        function_name="canDistribute",
        starter_code="def canDistribute(nums: list[int], quantity: list[int]) -> bool:\n    pass\n",
        solution_code="def canDistribute(nums: list[int], quantity: list[int]) -> bool:\n    from collections import Counter\n    counts = sorted(list(Counter(nums).values()), reverse=True)\n    m = len(quantity)\n    quantity.sort(reverse=True)\n    submask_sum = [0] * (1 << m)\n    for mask in range(1 << m):\n        for i in range(m):\n            if mask & (1 << i):\n                submask_sum[mask] += quantity[i]\n    memo = {}\n    def dp(idx, mask):\n        if mask == (1 << m) - 1: return True\n        if idx == len(counts): return False\n        state = (idx, mask)\n        if state in memo: return memo[state]\n        unallocated = ((1 << m) - 1) ^ mask\n        submask = unallocated\n        while submask > 0:\n            if submask_sum[submask] <= counts[idx]:\n                if dp(idx + 1, mask | submask):\n                    memo[state] = True\n                    return True\n            submask = (submask - 1) & unallocated\n        if dp(idx + 1, mask):\n            memo[state] = True\n            return True\n        memo[state] = False\n        return False\n    return dp(0, 0)\n",
        test_cases=[
            {"input": [[1,2,3,4], [2]], "expected": False},
            {"input": [[1,2,3,3], [2]], "expected": True},
            {"input": [[1,1,2,2], [2,2]], "expected": True}
        ],
        hints=["Since m <= 10, use submask enumeration. For each unique count, satisfy a valid subset of customers whose sum does not exceed that count."],
        leetcode_id=1655
    ))

    # 85. Closest Subsequence Sum (LC 1755)
    problems.append(make_problem(
        pid="bit-h-closest-subsequence-sum", title="Closest Subsequence Sum",
        wing_id="bit-manipulation", floor=585, difficulty="hard", visualizer_type="array",
        monster_name="Bifurcated Sum Golem", monster_title="Twin Splitter of Binary Subsets",
        monster_sprite="golem", monster_color="#475569", monster_attack="Meet-in-the-Middle Wave",
        monster_quote="Split forty elements in twain, conquer both halves with binary search!",
        description="You are given an integer array `nums` and an integer `goal`. You want to choose a subsequence of `nums` such that the sum of its elements is closest to `goal`. That is, if the sum of elements is `s`, you want to minimize the absolute difference `abs(s - goal)`. Return the minimum value of `abs(s - goal)`.",
        examples=[
            {"input": "nums = [5,-7,3,5], goal = 6", "output": "0"},
            {"input": "nums = [7,-9,15,-2], goal = -5", "output": "1"},
            {"input": "nums = [1,2,3], goal = -7", "output": "7"}
        ],
        constraints=["1 <= nums.length <= 40", "-10^7 <= nums[i] <= 10^7", "-10^9 <= goal <= 10^9"],
        function_name="minAbsDifference",
        starter_code="def minAbsDifference(nums: list[int], goal: int) -> int:\n    pass\n",
        solution_code="def minAbsDifference(nums: list[int], goal: int) -> int:\n    from bisect import bisect_left\n    n = len(nums)\n    mid = n // 2\n    left, right = nums[:mid], nums[mid:]\n    def get_sums(arr):\n        sums = {0}\n        for x in arr:\n            sums |= {s + x for s in sums}\n        return sorted(list(sums))\n    s1 = get_sums(left)\n    s2 = get_sums(right)\n    ans = abs(goal)\n    for x in s1:\n        target = goal - x\n        idx = bisect_left(s2, target)\n        if idx < len(s2):\n            ans = min(ans, abs(x + s2[idx] - goal))\n        if idx > 0:\n            ans = min(ans, abs(x + s2[idx - 1] - goal))\n    return ans\n",
        test_cases=[
            {"input": [[5,-7,3,5], 6], "expected": 0},
            {"input": [[7,-9,15,-2], -5], "expected": 1},
            {"input": [[1,2,3], -7], "expected": 7}
        ],
        hints=["Meet-in-the-middle: split nums into two halves of length <= 20. Generate all 2^20 subset sums for each half, sort the second, and binary search."],
        leetcode_id=1755
    ))

    return problems
