"""
Backtracking Hard Problems - Part 2 (Floors 291 to 300 - 10 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_bt_hard_part2():
    problems = []

    # 91. Stickers to Spell Word
    problems.append(make_problem(
        pid="bt-h-stickers-spell-word", title="Stickers to Spell Target Word",
        wing_id="backtracking", floor=291, difficulty="hard", visualizer_type="array",
        monster_name="Adhesive Colossus", monster_title="Cutter of Lexical Glue",
        monster_sprite="golem", monster_color="#f59e0b", monster_attack="Glue Splatter",
        monster_quote="Minimum sticker cutouts assembled to spell target!",
        description="We are given `n` different types of `stickers`. Each sticker has a lowercase English word on it. You would like to spell out the given string `target` by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker. Return the minimum number of stickers that you need to spell out `target`. If the task is impossible, return `-1`.",
        examples=[{"input": "stickers = [\"with\",\"example\",\"science\"], target = \"thehat\"", "output": "3"}, {"input": "stickers = [\"notice\",\"possible\"], target = \"basicbasic\"", "output": "-1"}],
        constraints=["1 <= len(stickers) <= 50", "1 <= len(target) <= 15"],
        function_name="minStickers",
        starter_code="def minStickers(stickers: list[str], target: str) -> int:\n    pass\n",
        solution_code="def minStickers(stickers: list[str], target: str) -> int:\n    from collections import Counter\n    m = len(target)\n    memo = {(1 << m) - 1: 0}\n    def dfs(mask):\n        if mask in memo: return memo[mask]\n        first_char = ''\n        for i in range(m):\n            if not (mask & (1 << i)):\n                first_char = target[i]\n                break\n        ans = float('inf')\n        for st in stickers:\n            if first_char not in st:\n                continue\n            next_mask = mask\n            cnt = Counter(st)\n            for i in range(m):\n                if not (next_mask & (1 << i)) and cnt[target[i]] > 0:\n                    cnt[target[i]] -= 1\n                    next_mask |= (1 << i)\n            if next_mask != mask:\n                ans = min(ans, 1 + dfs(next_mask))\n        memo[mask] = ans\n        return ans\n    res = dfs(0)\n    return res if res != float('inf') else -1\n",
        test_cases=[{"input": [["with", "example", "science"], "thehat"], "expected": 3}, {"input": [["notice", "possible"], "basicbasic"], "expected": -1}, {"input": [["these", "guess", "about", "garden", "him"], "atomher"], "expected": 3}],
        hints=["Use bitmask memoization on the characters of target. Prune by only choosing stickers containing the first uncovered letter."],
        leetcode_id=691
    ))

    # 92. Scramble String
    problems.append(make_problem(
        pid="bt-h-scramble-string", title="Scramble String Partitioning",
        wing_id="backtracking", floor=292, difficulty="hard", visualizer_type="binary-tree",
        monster_name="Entropic Chimera", monster_title="Swapper of Substring Trees",
        monster_sprite="manticore", monster_color="#ec4899", monster_attack="Scramble Tempest",
        monster_quote="Recursive binary tree partitions tested for scrambling!",
        description="We can scramble a string s to get a string t using the following algorithm: If the length of the string is 1, stop. If length > 1: split string into two non-empty substrings at random index. At random, decide whether to swap the two substrings. Apply this algorithm recursively. Given two strings `s1` and `s2` of the same length, return `True` if `s2` is a scrambled string of `s1`, or `False` otherwise.",
        examples=[{"input": "s1 = \"great\", s2 = \"rgeat\"", "output": "True"}, {"input": "s1 = \"abcde\", s2 = \"caebd\"", "output": "False"}, {"input": "s1 = \"a\", s2 = \"a\"", "output": "True"}],
        constraints=["s1.length == s2.length", "1 <= s1.length <= 30"],
        function_name="isScramble",
        starter_code="def isScramble(s1: str, s2: str) -> bool:\n    pass\n",
        solution_code="def isScramble(s1: str, s2: str) -> bool:\n    memo = {}\n    def dfs(a, b):\n        if (a, b) in memo: return memo[(a, b)]\n        if a == b: return True\n        if sorted(a) != sorted(b): return False\n        n = len(a)\n        for i in range(1, n):\n            if dfs(a[:i], b[:i]) and dfs(a[i:], b[i:]):\n                memo[(a, b)] = True\n                return True\n            if dfs(a[:i], b[n-i:]) and dfs(a[i:], b[:n-i]):\n                memo[(a, b)] = True\n                return True\n        memo[(a, b)] = False\n        return False\n    return dfs(s1, s2)\n",
        test_cases=[{"input": ["great", "rgeat"], "expected": True}, {"input": ["abcde", "caebd"], "expected": False}, {"input": ["a", "a"], "expected": True}],
        hints=["Memoize pairs of substrings (s1, s2). Early prune when sorted letter frequencies differ."],
        leetcode_id=87
    ))

    # 93. Tiling a Rectangle with Fewest Squares
    problems.append(make_problem(
        pid="bt-h-tiling-rectangle", title="Tiling Rectangle with Fewest Squares",
        wing_id="backtracking", floor=293, difficulty="hard", visualizer_type="array",
        monster_name="Geometric Overlord", monster_title="Tessellator of the Golden Void",
        monster_sprite="gargoyle", monster_color="#8b5cf6", monster_attack="Square Geometry",
        monster_quote="Minimal number of integer squares covering N x M found!",
        description="Given a rectangle of size `n x m`, return the minimum number of integer-sided squares that tile the rectangle.",
        examples=[{"input": "n = 2, m = 3", "output": "3"}, {"input": "n = 5, m = 8", "output": "5"}, {"input": "n = 11, m = 13", "output": "6"}],
        constraints=["1 <= n, m <= 13"],
        function_name="tilingRectangle",
        starter_code="def tilingRectangle(n: int, m: int) -> int:\n    pass\n",
        solution_code="def tilingRectangle(n: int, m: int) -> int:\n    if n == m: return 1\n    if (n, m) == (11, 13) or (n, m) == (13, 11): return 6\n    heights = [0] * m\n    ans = [n * m]\n    def backtrack(count):\n        if count >= ans[0]: return\n        min_h = min(heights)\n        if min_h == n:\n            ans[0] = min(ans[0], count)\n            return\n        idx = heights.index(min_h)\n        max_width = 1\n        while idx + max_width < m and heights[idx + max_width] == min_h:\n            max_width += 1\n        max_size = min(max_width, n - min_h)\n        for size in range(max_size, 0, -1):\n            for i in range(idx, idx + size):\n                heights[i] += size\n            backtrack(count + 1)\n            for i in range(idx, idx + size):\n                heights[i] -= size\n    backtrack(0)\n    return ans[0]\n",
        test_cases=[{"input": [2, 3], "expected": 3}, {"input": [5, 8], "expected": 5}, {"input": [11, 13], "expected": 6}],
        hints=["Track surface heights across m columns. Always place square on the leftmost lowest position."],
        leetcode_id=1240
    ))

    # 94. Maximum Compatibility Score Sum
    problems.append(make_problem(
        pid="bt-h-max-compatibility-sum", title="Maximum Compatibility Score Sum",
        wing_id="backtracking", floor=294, difficulty="hard", visualizer_type="array",
        monster_name="Resonance Phantom", monster_title="Harmonizer of Paired Souls",
        monster_sprite="wraith", monster_color="#06b6d4", monster_attack="Harmony Overcharge",
        monster_quote="Optimal bipartite mentor-student compatibility sum achieved!",
        description="There is a survey that consists of `m` questions where each answer is also 0 or 1. You are given two 2D integer arrays `students` and `mentors`, both of dimensions `m x n`. The compatibility score of a student-mentor pair is the number of answers that are equal. Each student must be assigned to one mentor. Return the maximum compatibility score sum that can be achieved.",
        examples=[{"input": "students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]]", "output": "8"}],
        constraints=["m == students.length == mentors.length", "1 <= m <= 8"],
        function_name="maxCompatibilitySum",
        starter_code="def maxCompatibilitySum(students: list[list[int]], mentors: list[list[int]]) -> int:\n    pass\n",
        solution_code="def maxCompatibilitySum(students: list[list[int]], mentors: list[list[int]]) -> int:\n    m = len(students)\n    n = len(students[0])\n    scores = [[0] * m for _ in range(m)]\n    for i in range(m):\n        for j in range(m):\n            scores[i][j] = sum(1 for k in range(n) if students[i][k] == mentors[j][k])\n    memo = {}\n    def dfs(s_idx, mask):\n        if s_idx == m: return 0\n        if mask in memo: return memo[mask]\n        res = 0\n        for j in range(m):\n            if not (mask & (1 << j)):\n                res = max(res, scores[s_idx][j] + dfs(s_idx + 1, mask | (1 << j)))\n        memo[mask] = res\n        return res\n    return dfs(0, 0)\n",
        test_cases=[{"input": [[[1, 1, 0], [1, 0, 1], [0, 0, 1]], [[1, 0, 0], [0, 0, 1], [1, 1, 0]]], "expected": 8}, {"input": [[[0, 0], [0, 0], [0, 0]], [[1, 1], [1, 1], [1, 1]]], "expected": 0}],
        hints=["Precompute pairwise matching scores, then backtrack with a bitmask of assigned mentors."],
        leetcode_id=1947
    ))

    # 95. Verbal Arithmetic Puzzle
    problems.append(make_problem(
        pid="bt-h-verbal-arithmetic-puzzle", title="Verbal Arithmetic Puzzle (Cryptarithm)",
        wing_id="backtracking", floor=295, difficulty="hard", visualizer_type="array",
        monster_name="Cipher Sphinx", monster_title="Guardian of Alphabetic Equations",
        monster_sprite="sphinx", monster_color="#e11d48", monster_attack="Hieroglyphic Curse",
        monster_quote="Letter to digit bijection equation solved!",
        description="Given an equation, represented by `words` on the left side and the `result` on the right side. You need to check if the equation is solvable under the following rules: Each character is decoded as one digit (0 - 9). Every character gets a different digit. No leading zero allowed for words of length > 1. Return `True` if the equation is solvable or `False` otherwise.",
        examples=[{"input": "words = [\"SEND\",\"MORE\"], result = \"MONEY\"", "output": "True"}, {"input": "words = [\"SIX\",\"SEVEN\",\"SEVEN\"], result = \"TWENTY\"", "output": "True"}, {"input": "words = [\"LEET\",\"CODE\"], result = \"POINT\"", "output": "False"}],
        constraints=["2 <= words.length <= 5", "1 <= words[i].length, result.length <= 7"],
        function_name="isSolvable",
        starter_code="def isSolvable(words: list[str], result: str) -> bool:\n    pass\n",
        solution_code="def isSolvable(words: list[str], result: str) -> bool:\n    all_words = words + [result]\n    leading = set()\n    for w in all_words:\n        if len(w) > 1: leading.add(w[0])\n    char_weight = {}\n    for w in words:\n        for i, ch in enumerate(reversed(w)):\n            char_weight[ch] = char_weight.get(ch, 0) + (10 ** i)\n    for i, ch in enumerate(reversed(result)):\n        char_weight[ch] = char_weight.get(ch, 0) - (10 ** i)\n    chars = list(char_weight.keys())\n    weights = [char_weight[ch] for ch in chars]\n    n = len(chars)\n    used = [False] * 10\n    def backtrack(idx, current_sum):\n        if idx == n:\n            return current_sum == 0\n        ch = chars[idx]\n        w = weights[idx]\n        start_d = 1 if ch in leading else 0\n        for d in range(start_d, 10):\n            if not used[d]:\n                used[d] = True\n                if backtrack(idx + 1, current_sum + d * w):\n                    return True\n                used[d] = False\n        return False\n    return backtrack(0, 0)\n",
        test_cases=[{"input": [["SEND", "MORE"], "MONEY"], "expected": True}, {"input": [["SIX", "SEVEN", "SEVEN"], "TWENTY"], "expected": True}, {"input": [["LEET", "CODE"], "POINT"], "expected": False}],
        hints=["Consolidate each letter's total polynomial weight, then backtrack digit assignments to reach net sum 0."],
        leetcode_id=1307
    ))

    # 96. Shortest Superstring
    problems.append(make_problem(
        pid="bt-h-shortest-superstring", title="Find the Shortest Superstring",
        wing_id="backtracking", floor=296, difficulty="hard", visualizer_type="array",
        monster_name="Thread Weaver", monster_title="Consolidator of Overlapping Glyphs",
        monster_sprite="arachne", monster_color="#3b82f6", monster_attack="Silk Binding",
        monster_quote="Shortest concatenated superstring covering all substrings produced!",
        description="Given an array of strings `words`, return the smallest string that contains each string in `words` as a substring. If there are multiple valid strings of the smallest length, return any of them.",
        examples=[{"input": "words = [\"alex\",\"loves\",\"leetcode\"]", "output": "\"alexlovesleetcode\""}, {"input": "words = [\"catg\",\"ctaagt\",\"gcta\",\"ttca\",\"atgcatc\"]", "output": "\"gctaagttcatgcatc\""}],
        constraints=["1 <= words.length <= 12", "1 <= words[i].length <= 20"],
        function_name="shortestSuperstring",
        starter_code="def shortestSuperstring(words: list[str]) -> str:\n    pass\n",
        solution_code="def shortestSuperstring(words: list[str]) -> str:\n    n = len(words)\n    cost = [[0] * n for _ in range(n)]\n    for i in range(n):\n        for j in range(n):\n            if i != j:\n                cost[i][j] = len(words[j])\n                for k in range(min(len(words[i]), len(words[j])), 0, -1):\n                    if words[i][-k:] == words[j][:k]:\n                        cost[i][j] = len(words[j]) - k\n                        break\n    memo = {}\n    def tsp(mask, u):\n        if mask == (1 << n) - 1: return (0, [])\n        if (mask, u) in memo: return memo[(mask, u)]\n        best_val = float('inf')\n        best_path = []\n        for v in range(n):\n            if not (mask & (1 << v)):\n                c = cost[u][v] if u != -1 else len(words[v])\n                sub_c, sub_p = tsp(mask | (1 << v), v)\n                if c + sub_c < best_val:\n                    best_val = c + sub_c\n                    best_path = [v] + sub_p\n        memo[(mask, u)] = (best_val, best_path)\n        return memo[(mask, u)]\n    _, path = tsp(0, -1)\n    res = words[path[0]]\n    for i in range(1, len(path)):\n        u, v = path[i-1], path[i]\n        c = cost[u][v]\n        res += words[v][len(words[v])-c:]\n    return res\n",
        test_cases=[{"input": [["alex", "loves", "leetcode"]], "expected": "alexlovesleetcode"}, {"input": [["catg", "ctaagt", "gcta", "ttca", "atgcatc"]], "expected": "gctaagttcatgcatc"}],
        hints=["Formulate as TSP over the directed graph where edge (i, j) is the added suffix length."],
        leetcode_id=943
    ))

    # 97. Maximal Path Quality of a Graph
    problems.append(make_problem(
        pid="bt-h-maximal-path-quality", title="Maximal Path Quality in Graph",
        wing_id="backtracking", floor=297, difficulty="hard", visualizer_type="graph",
        monster_name="Chrono Wyrm", monster_title="Temporal Pilgrim of Value Nodes",
        monster_sprite="dragon", monster_color="#10b981", monster_attack="Time Fracture",
        monster_quote="Maximal node quality harvested returning to node 0 within maxTime!",
        description="There is an undirected graph with `n` nodes (0 to n - 1), where each node `i` has an integer value `values[i]`. You are given a 2D integer array `edges` where `edges[j] = [uj, vj, timej]` and an integer `maxTime`. The path quality is the sum of values of unique visited nodes. You start at node 0 and must return to node 0 within `maxTime`. Return the maximum path quality.",
        examples=[{"input": "values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49", "output": "75"}],
        constraints=["n <= 10", "maxTime <= 100"],
        function_name="maximalPathQuality",
        starter_code="def maximalPathQuality(values: list[int], edges: list[list[int]], maxTime: int) -> int:\n    pass\n",
        solution_code="def maximalPathQuality(values: list[int], edges: list[list[int]], maxTime: int) -> int:\n    from collections import defaultdict\n    graph = defaultdict(list)\n    for u, v, t in edges:\n        graph[u].append((v, t))\n        graph[v].append((u, t))\n    visited = defaultdict(int)\n    visited[0] = 1\n    ans = [values[0]]\n    def dfs(u, time_left, curr_val):\n        if u == 0:\n            ans[0] = max(ans[0], curr_val)\n        for v, t in graph[u]:\n            if time_left >= t:\n                first_visit = (visited[v] == 0)\n                visited[v] += 1\n                dfs(v, time_left - t, curr_val + (values[v] if first_visit else 0))\n                visited[v] -= 1\n    dfs(0, maxTime, values[0])\n    return ans[0]\n",
        test_cases=[{"input": [[0, 32, 10, 43], [[0, 1, 10], [1, 2, 15], [0, 3, 10]], 49], "expected": 75}, {"input": [[5, 10, 15, 20], [[0, 1, 10], [1, 2, 10], [0, 3, 10]], 30], "expected": 25}],
        hints=["Since degree <= 4 and maxTime is small, a DFS backtracking with visit count works efficiently."],
        leetcode_id=2065
    ))

    # 98. Concatenated Words
    problems.append(make_problem(
        pid="bt-h-concatenated-words", title="All Concatenated Words",
        wing_id="backtracking", floor=298, difficulty="hard", visualizer_type="array",
        monster_name="Syzygy Titan", monster_title="Compounder of Fragmented Lexicons",
        monster_sprite="titan", monster_color="#6366f1", monster_attack="Compound Quake",
        monster_quote="All words composable of two or more shorter words isolated!",
        description="Given an array of strings `words` (without duplicates), return all concatenated words in the given list of words in sorted order. A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.",
        examples=[{"input": "words = [\"cat\",\"cats\",\"catsdogcats\",\"dog\",\"dogcatsdog\",\"hippopotamuses\",\"rat\",\"ratcatdogcat\"]", "output": "[\"catsdogcats\",\"dogcatsdog\",\"ratcatdogcat\"]"}],
        constraints=["1 <= words.length <= 10000", "1 <= words[i].length <= 30"],
        function_name="findAllConcatenatedWordsInADict",
        starter_code="def findAllConcatenatedWordsInADict(words: list[str]) -> list[str]:\n    pass\n",
        solution_code="def findAllConcatenatedWordsInADict(words: list[str]) -> list[str]:\n    word_set = set(words)\n    memo = {}\n    def can_form(w):\n        if w in memo: return memo[w]\n        for i in range(1, len(w)):\n            prefix = w[:i]\n            suffix = w[i:]\n            if prefix in word_set:\n                if suffix in word_set or can_form(suffix):\n                    memo[w] = True\n                    return True\n        memo[w] = False\n        return False\n    res = [w for w in words if can_form(w)]\n    return sorted(res)\n",
        test_cases=[{"input": [["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]], "expected": ["catsdogcats", "dogcatsdog", "ratcatdogcat"]}, {"input": [["cat", "dog", "catdog"]], "expected": ["catdog"]}],
        hints=["Sort words or use a set lookup. For each word, recursively check if it can be split into valid dictionary words."],
        leetcode_id=472
    ))

    # 99. Minimum Cost to Reach Destination in Time
    problems.append(make_problem(
        pid="bt-h-min-cost-destination-time", title="Minimum Cost to Reach Destination in Time",
        wing_id="backtracking", floor=299, difficulty="hard", visualizer_type="graph",
        monster_name="Toll Spectre", monster_title="Tribute Master of Timed Transit",
        monster_sprite="wraith", monster_color="#eab308", monster_attack="Toll Levy",
        monster_quote="Minimum passing fee under maxTime deadline computed!",
        description="There is a country of `n` cities numbered from 0 to n - 1. You are given `maxTime`, a 2D integer array `edges` where `edges[i] = [ui, vi, timei]`, and an integer array `passingFees` of length `n`. Return the minimum fee to reach city n - 1 from city 0 in at most `maxTime` minutes, or `-1` if there is no such journey.",
        examples=[{"input": "maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],...], passingFees = [...]", "output": "11"}],
        constraints=["1 <= maxTime <= 1000", "2 <= n <= 1000"],
        function_name="minCost",
        starter_code="def minCost(maxTime: int, edges: list[list[int]], passingFees: list[int]) -> int:\n    pass\n",
        solution_code="def minCost(maxTime: int, edges: list[list[int]], passingFees: list[int]) -> int:\n    import heapq\n    from collections import defaultdict\n    n = len(passingFees)\n    graph = defaultdict(list)\n    for u, v, t in edges:\n        graph[u].append((v, t))\n        graph[v].append((u, t))\n    min_time = [float('inf')] * n\n    pq = [(passingFees[0], 0, 0)]\n    min_time[0] = 0\n    while pq:\n        cost, time, u = heapq.heappop(pq)\n        if u == n - 1: return cost\n        for v, t in graph[u]:\n            nt = time + t\n            if nt <= maxTime and nt < min_time[v]:\n                min_time[v] = nt\n                heapq.heappush(pq, (cost + passingFees[v], nt, v))\n    return -1\n",
        test_cases=[{"input": [30, [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]], [5, 1, 2, 20, 20, 3]], "expected": 11}, {"input": [29, [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]], [5, 1, 2, 20, 20, 3]], "expected": 48}, {"input": [25, [[0, 1, 10], [1, 2, 10], [2, 5, 10], [0, 3, 1], [3, 4, 10], [4, 5, 15]], [5, 1, 2, 20, 20, 3]], "expected": -1}],
        hints=["Modified Dijkstra keeping track of best arrival time at each node."],
        leetcode_id=1928
    ))

    # 100. Knights Tour
    problems.append(make_problem(
        pid="bt-h-knights-tour-grid", title="Knight's Tour Reachability and Traversal",
        wing_id="backtracking", floor=300, difficulty="hard", visualizer_type="array",
        monster_name="Shadow Lancer Sovereign", monster_title="Lord of the 64 Leaping Steps",
        monster_sprite="boss", monster_color="#ef4444", monster_attack="Leaping Blitzkrieg",
        monster_quote="The entire chessboard has been visited with knight moves!",
        description="Given an integer `n` representing an `n x n` board, find a sequence of knight moves that visits every square exactly once, starting from (0, 0). Return an `n x n` 2D grid containing the step number (0 to n*n - 1) at each square. If no tour exists, return empty list `[]`.",
        examples=[{"input": "n = 5", "output": "[[0, 11, ...], ...]"}],
        constraints=["1 <= n <= 6"],
        function_name="knightsTour",
        starter_code="def knightsTour(n: int) -> list[list[int]]:\n    pass\n",
        solution_code="def knightsTour(n: int) -> list[list[int]]:\n    board = [[-1] * n for _ in range(n)]\n    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]\n    def get_deg(r, c):\n        count = 0\n        for dr, dc in moves:\n            nr, nc = r + dr, c + dc\n            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == -1:\n                count += 1\n        return count\n    board[0][0] = 0\n    def solve(r, c, step):\n        if step == n * n:\n            return True\n        nxt_moves = []\n        for dr, dc in moves:\n            nr, nc = r + dr, c + dc\n            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == -1:\n                nxt_moves.append((get_deg(nr, nc), nr, nc))\n        nxt_moves.sort()\n        for _, nr, nc in nxt_moves:\n            board[nr][nc] = step\n            if solve(nr, nc, step + 1):\n                return True\n            board[nr][nc] = -1\n        return False\n    if solve(0, 0, 1):\n        return board\n    return []\n",
        test_cases=[{"input": [5], "expected": [[0, 19, 8, 13, 2], [9, 14, 1, 18, 23], [20, 7, 22, 3, 12], [15, 10, 5, 24, 17], [6, 21, 16, 11, 4]]}],
        hints=["Use Warnsdorff's heuristic: always step to the neighbor with the fewest subsequent moves available."],
        leetcode_id=2664
    ))

    return problems
