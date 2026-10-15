"""
Backtracking Medium Problems Part 4 (Problems 51 to 70 - 20 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_bt_medium_part4():
    problems = []

    # 51. Maximum Score Words Formed by Letters
    problems.append(make_problem(
        pid="bt-m-maximum-score-words", title="Maximum Score Words Formed by Letters",
        wing_id="backtracking", floor=251, difficulty="medium", visualizer_type="array",
        monster_name="Scrabble Titan", monster_title="Maximized Word Score Calculator",
        monster_sprite="golem", monster_color="#f59e0b", monster_attack="Score Slam",
        monster_quote="Letter inventory tracked and highest-scoring subset found!",
        description="Given a list of `words`, list of single `letters` (might be repeating) and `score` of every character. Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used multiple times).",
        examples=[{"input": "words = [\"dog\",\"cat\",\"dad\",\"good\"], letters = [\"a\",\"a\",\"c\",\"d\",\"d\",\"d\",\"g\",\"o\",\"o\"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]", "output": "23"}],
        constraints=["1 <= len(words) <= 14", "len(score) == 26"],
        function_name="maxScoreWords",
        starter_code="def maxScoreWords(words: list[str], letters: list[str], score: list[int]) -> int:\n    pass\n",
        solution_code="def maxScoreWords(words: list[str], letters: list[str], score: list[int]) -> int:\n    from collections import Counter\n    letter_counts = Counter(letters)\n    def word_val(w):\n        return sum(score[ord(ch) - 97] for ch in w)\n    def dfs(idx, counts):\n        if idx == len(words): return 0\n        # Skip word\n        res = dfs(idx + 1, counts)\n        # Try taking word\n        w = words[idx]\n        w_counts = Counter(w)\n        if all(counts[ch] >= w_counts[ch] for ch in w_counts):\n            new_counts = Counter(counts)\n            for ch in w_counts: new_counts[ch] -= w_counts[ch]\n            res = max(res, word_val(w) + dfs(idx + 1, new_counts))\n        return res\n    return dfs(0, letter_counts)\n",
        test_cases=[{"input": [["dog", "cat", "dad", "good"], ["a", "a", "c", "d", "d", "d", "g", "o", "o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]], "expected": 23}, {"input": [["xxxz", "ax", "bx", "cx"], ["z", "a", "b", "c", "x", "x", "x"], [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]], "expected": 27}],
        hints=["Recursive branch: either skip words[idx] or take it if remaining letter counts allow."],
        leetcode_id=1255
    ))

    # 52. Optimal Account Balancing
    problems.append(make_problem(
        pid="bt-m-optimal-account-balancing", title="Optimal Account Balancing",
        wing_id="backtracking", floor=252, difficulty="medium", visualizer_type="array",
        monster_name="Debt Minotaur", monster_title="Settler of Intersecting Debts",
        monster_sprite="demon", monster_color="#ef4444", monster_attack="Debt Horns",
        monster_quote="Minimum transactions required to zero all balances achieved!",
        description="You are given an array of transactions `transactions` where `transactions[i] = [fromi, toi, amount]`. Return the minimum number of transactions required to settle the debt.",
        examples=[{"input": "transactions = [[0,1,10],[2,0,5]]", "output": "2"}, {"input": "transactions = [[0,1,10],[1,0,1],[1,2,5],[2,0,5]]", "output": "1"}],
        constraints=["1 <= len(transactions) <= 8"],
        function_name="minTransfers",
        starter_code="def minTransfers(transactions: list[list[int]]) -> int:\n    pass\n",
        solution_code="def minTransfers(transactions: list[list[int]]) -> int:\n    from collections import defaultdict\n    bal = defaultdict(int)\n    for u, v, amt in transactions:\n        bal[u] -= amt\n        bal[v] += amt\n    debts = [v for v in bal.values() if v != 0]\n    def dfs(idx):\n        while idx < len(debts) and debts[idx] == 0:\n            idx += 1\n        if idx == len(debts): return 0\n        res = float('inf')\n        for j in range(idx + 1, len(debts)):\n            if debts[idx] * debts[j] < 0:\n                debts[j] += debts[idx]\n                res = min(res, 1 + dfs(idx + 1))\n                debts[j] -= debts[idx]\n        return res\n    return dfs(0)\n",
        test_cases=[{"input": [[[0, 1, 10], [2, 0, 5]]], "expected": 2}, {"input": [[[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]], "expected": 1}],
        hints=["Calculate net debt per person. Pair negative balances with positive balances recursively."],
        leetcode_id=465
    ))

    # 53. Validate Partial Sudoku Board
    problems.append(make_problem(
        pid="bt-m-sudoku-valid-board", title="Validate Partial Sudoku Board",
        wing_id="backtracking", floor=253, difficulty="medium", visualizer_type="array",
        monster_name="Sudoku Arbiter", monster_title="Judge of 3x3 Grid Integrity",
        monster_sprite="golem", monster_color="#8b5cf6", monster_attack="Sudoku Shield",
        monster_quote="Every row, column, and 3x3 box checked without duplicate digits!",
        description="Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the standard Sudoku rules: each row must contain 1-9 without repetition, each column 1-9, and each 3x3 sub-box 1-9.",
        examples=[{"input": "board = [[\"5\",\"3\",\".\",\".\",\"7\",\".\",\".\",\".\",\".\"],[\"6\",\".\",\".\",\"1\",\"9\",\"5\",\".\",\".\",\".\"],[\".\",\"9\",\"8\",\".\",\".\",\".\",\".\",\"6\",\".\"],[\"8\",\".\",\".\",\".\",\"6\",\".\",\".\",\".\",\"3\"],[\"4\",\".\",\".\",\"8\",\".\",\"3\",\".\",\".\",\"1\"],[\"7\",\".\",\".\",\".\",\"2\",\".\",\".\",\".\",\"6\"],[\".\",\"6\",\".\",\".\",\".\",\".\",\"2\",\"8\",\".\"],[\".\",\".\",\".\",\"4\",\"1\",\"9\",\".\",\".\",\"5\"],[\".\",\".\",\".\",\".\",\"8\",\".\",\".\",\"7\",\"9\"]]", "output": "True"}],
        constraints=["board.length == 9", "board[i].length == 9"],
        function_name="isValidSudoku",
        starter_code="def isValidSudoku(board: list[list[str]]) -> bool:\n    pass\n",
        solution_code="def isValidSudoku(board: list[list[str]]) -> bool:\n    seen = set()\n    for r in range(9):\n        for c in range(9):\n            val = board[r][c]\n            if val != '.':\n                r_tag = (r, val)\n                c_tag = (val, c)\n                b_tag = (r // 3, c // 3, val)\n                if r_tag in seen or c_tag in seen or b_tag in seen:\n                    return False\n                seen.add(r_tag)\n                seen.add(c_tag)\n                seen.add(b_tag)\n    return True\n",
        test_cases=[{"input": [[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."], [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]], "expected": True}, {"input": [[["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."], [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]], "expected": False}],
        hints=["Use tuple markers in a single set: (r, val), (val, c), (r//3, c//3, val)."],
        leetcode_id=36
    ))

    # 54. First N-Queens Board
    problems.append(make_problem(
        pid="bt-m-n-queens-first-solution", title="First Valid N-Queens Placement",
        wing_id="backtracking", floor=254, difficulty="medium", visualizer_type="array",
        monster_name="Matriarch Queen", monster_title="Ruler of Non-Attacking Diagonals",
        monster_sprite="lich", monster_color="#ec4899", monster_attack="Royal Check",
        monster_quote="First non-attacking queen column vector located!",
        description="Given integer `n`, return the first valid placement of `n` non-attacking queens on an `n x n` board as an array of column indices for each row `0` through `n-1`, or `[]` if none exists.",
        examples=[{"input": "n = 4", "output": "[1,3,0,2]"}, {"input": "n = 1", "output": "[0]"}],
        constraints=["1 <= n <= 10"],
        function_name="firstNQueens",
        starter_code="def firstNQueens(n: int) -> list[int]:\n    pass\n",
        solution_code="def firstNQueens(n: int) -> list[int]:\n    cols = set()\n    diag1 = set()\n    diag2 = set()\n    board = [-1] * n\n    def backtrack(r):\n        if r == n: return True\n        for c in range(n):\n            if c not in cols and (r - c) not in diag1 and (r + c) not in diag2:\n                cols.add(c)\n                diag1.add(r - c)\n                diag2.add(r + c)\n                board[r] = c\n                if backtrack(r + 1): return True\n                cols.remove(c)\n                diag1.remove(r - c)\n                diag2.remove(r + c)\n        return False\n    if backtrack(0): return board\n    return []\n",
        test_cases=[{"input": [4], "expected": [1, 3, 0, 2]}, {"input": [1], "expected": [0]}, {"input": [2], "expected": []}],
        hints=["Place queen row by row. Track cols, r - c, and r + c diagonals."],
        leetcode_id=51
    ))

    # 55. Subsets with Product Less Than K
    problems.append(make_problem(
        pid="bt-m-subsets-product-k", title="Subsets with Product < K",
        wing_id="backtracking", floor=255, difficulty="medium", visualizer_type="array",
        monster_name="Product Banshee", monster_title="Keeper of Multiplicative Bounds",
        monster_sprite="wraith", monster_color="#06b6d4", monster_attack="Product Hex",
        monster_quote="All subsets strictly bounded by product k counted!",
        description="Given an array of positive integers `nums` and an integer `k`, return the number of non-empty subsets whose product of elements is strictly less than `k`.",
        examples=[{"input": "nums = [2,3,5], k = 15", "output": "5"}, {"input": "nums = [2,3], k = 5", "output": "2"}],
        constraints=["1 <= len(nums) <= 12", "1 <= nums[i] <= 100", "1 <= k <= 10^5"],
        function_name="subsetsProductK",
        starter_code="def subsetsProductK(nums: list[int], k: int) -> int:\n    pass\n",
        solution_code="def subsetsProductK(nums: list[int], k: int) -> int:\n    count = 0\n    def dfs(idx, curr_prod, picked):\n        nonlocal count\n        if idx == len(nums):\n            if picked and curr_prod < k:\n                count += 1\n            return\n        dfs(idx + 1, curr_prod, picked)\n        if curr_prod * nums[idx] < k:\n            dfs(idx + 1, curr_prod * nums[idx], True)\n    dfs(0, 1, False)\n    return count\n",
        test_cases=[{"input": [[2, 3, 5], 15], "expected": 5}, {"input": [[2, 3], 5], "expected": 2}, {"input": [[10], 5], "expected": 0}],
        hints=["Recursive branching with pick and skip; prune whenever curr_prod * nums[idx] >= k."],
        leetcode_id=None
    ))

    # 56. Tiling 2xN Grid
    problems.append(make_problem(
        pid="bt-m-tiling-grid-2xn", title="Tiling 2xN Grid with Dominoes",
        wing_id="backtracking", floor=256, difficulty="medium", visualizer_type="array",
        monster_name="Domino Gargoyle", monster_title="Plaver of 2x1 Domino Blocks",
        monster_sprite="golem", monster_color="#10b981", monster_attack="Tiling Smash",
        monster_quote="Fibonacci recurrence tiled the 2xn grid completely!",
        description="You have a `2 x n` board and `2 x 1` domino tiles. Return the number of ways to tile the board completely modulo `10^9 + 7`.",
        examples=[{"input": "n = 3", "output": "3"}, {"input": "n = 4", "output": "5"}],
        constraints=["1 <= n <= 1000"],
        function_name="tileGrid2xN",
        starter_code="def tileGrid2xN(n: int) -> int:\n    pass\n",
        solution_code="def tileGrid2xN(n: int) -> int:\n    MOD = 10**9 + 7\n    if n <= 1: return 1\n    a, b = 1, 1\n    for _ in range(n - 1):\n        a, b = b, (a + b) % MOD\n    return b\n",
        test_cases=[{"input": [3], "expected": 3}, {"input": [4], "expected": 5}, {"input": [1], "expected": 1}],
        hints=["Ways to tile 2xn is Fibonacci sequence: f(n) = f(n-1) + f(n-2)."],
        leetcode_id=790
    ))

    # 57. Permutations Divisible by K
    problems.append(make_problem(
        pid="bt-m-permutations-divisible-k", title="Permutations Divisible by K",
        wing_id="backtracking", floor=257, difficulty="medium", visualizer_type="array",
        monster_name="Arithmetic Lich", monster_title="Weigher of Permutation Divisibility",
        monster_sprite="lich", monster_color="#e11d48", monster_attack="Modulo Hex",
        monster_quote="Multi-digit integer permutations divisible by k verified!",
        description="Given an array of distinct digits `digits`, form all permutations into integer numbers. Return the count of permutations that form a number divisible by `k`.",
        examples=[{"input": "digits = [1,2,3], k = 3", "output": "6"}, {"input": "digits = [1,2,4], k = 2", "output": "4"}],
        constraints=["1 <= len(digits) <= 8", "1 <= k <= 100"],
        function_name="permutationsDivByK",
        starter_code="def permutationsDivByK(digits: list[int], k: int) -> int:\n    pass\n",
        solution_code="def permutationsDivByK(digits: list[int], k: int) -> int:\n    used = [False] * len(digits)\n    count = 0\n    def backtrack(curr_val, length):\n        nonlocal count\n        if length == len(digits):\n            if curr_val % k == 0: count += 1\n            return\n        for i in range(len(digits)):\n            if not used[i]:\n                used[i] = True\n                backtrack(curr_val * 10 + digits[i], length + 1)\n                used[i] = False\n    backtrack(0, 0)\n    return count\n",
        test_cases=[{"input": [[1, 2, 3], 3], "expected": 6}, {"input": [[1, 2, 4], 2], "expected": 4}, {"input": [[5], 5], "expected": 1}],
        hints=["Accumulate integer value on each branch and check modulo k at full depth."],
        leetcode_id=None
    ))

    # 58. Word Transform Possible
    problems.append(make_problem(
        pid="bt-m-word-transform-possible", title="One-Letter Word Transform Path",
        wing_id="backtracking", floor=258, difficulty="medium", visualizer_type="graph",
        monster_name="Lexical Chimera", monster_title="Shifter of Single Characters",
        monster_sprite="demon", monster_color="#38bdf8", monster_attack="Mutation Claw",
        monster_quote="Valid one-letter mutation chain from start to end discovered!",
        description="Given two words, `startWord` and `endWord`, and a dictionary of valid words `wordList`, return `True` if there exists a mutation sequence such that each adjacent word differs by exactly 1 character and all intermediate words are in `wordList`.",
        examples=[{"input": "startWord = \"hit\", endWord = \"cog\", wordList = [\"hot\",\"dot\",\"dog\",\"lot\",\"log\",\"cog\"]", "output": "True"}],
        constraints=["1 <= len(startWord) <= 10", "1 <= len(wordList) <= 50"],
        function_name="wordTransformPossible",
        starter_code="def wordTransformPossible(startWord: str, endWord: str, wordList: list[str]) -> bool:\n    pass\n",
        solution_code="def wordTransformPossible(startWord: str, endWord: str, wordList: list[str]) -> bool:\n    if endWord not in wordList: return False\n    from collections import deque\n    words = set(wordList)\n    queue = deque([startWord])\n    visited = {startWord}\n    while queue:\n        curr = queue.popleft()\n        if curr == endWord: return True\n        for i in range(len(curr)):\n            for c in 'abcdefghijklmnopqrstuvwxyz':\n                nxt = curr[:i] + c + curr[i+1:]\n                if nxt in words and nxt not in visited:\n                    visited.add(nxt)\n                    queue.append(nxt)\n    return False\n",
        test_cases=[{"input": ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]], "expected": True}, {"input": ["hit", "cog", ["hot", "dot", "dog", "lot", "log"]], "expected": False}],
        hints=["Breadth-First Search (BFS) explores one-letter mutation neighbors level by level."],
        leetcode_id=127
    ))

    # 59. Subsets with Sum Divisible by D
    problems.append(make_problem(
        pid="bt-m-subsets-sum-divisible-d", title="Subsets with Sum Divisible by D",
        wing_id="backtracking", floor=259, difficulty="medium", visualizer_type="array",
        monster_name="Divisor Golem", monster_title="Tallyman of Modular Partitions",
        monster_sprite="golem", monster_color="#f59e0b", monster_attack="Modulo Hammer",
        monster_quote="Every subset with sum divisible by d accounted for!",
        description="Given an array of integers `nums` and an integer `d`, return the number of non-empty subsets whose sum is divisible by `d`.",
        examples=[{"input": "nums = [1,2,3], d = 3", "output": "3"}, {"input": "nums = [2,4,6], d = 2", "output": "7"}],
        constraints=["1 <= len(nums) <= 12", "1 <= nums[i] <= 100", "1 <= d <= 100"],
        function_name="subsetsSumDivD",
        starter_code="def subsetsSumDivD(nums: list[int], d: int) -> int:\n    pass\n",
        solution_code="def subsetsSumDivD(nums: list[int], d: int) -> int:\n    count = 0\n    def dfs(idx, curr_sum, picked):\n        nonlocal count\n        if idx == len(nums):\n            if picked and curr_sum % d == 0: count += 1\n            return\n        dfs(idx + 1, curr_sum, picked)\n        dfs(idx + 1, curr_sum + nums[idx], True)\n    dfs(0, 0, False)\n    return count\n",
        test_cases=[{"input": [[1, 2, 3], 3], "expected": 3}, {"input": [[2, 4, 6], 2], "expected": 7}, {"input": [[5], 2], "expected": 0}],
        hints=["Track running sum mod d and count when picked is True and sum % d == 0."],
        leetcode_id=None
    ))

    # 60. Knight Tour on Small Grid
    problems.append(make_problem(
        pid="bt-m-knight-tour-mini", title="Knight Moves Reachability",
        wing_id="backtracking", floor=260, difficulty="medium", visualizer_type="graph",
        monster_name="Equestrian Shade", monster_title="Rider of the L-Shaped Leap",
        monster_sprite="wraith", monster_color="#8b5cf6", monster_attack="Knight Trample",
        monster_quote="L-shaped chess leaps traversed all reachable grid tiles!",
        description="Given an `n x n` chessboard and starting coordinate `(r, c)`, return the number of distinct squares a knight can reach in at most `k` moves.",
        examples=[{"input": "n = 3, r = 0, c = 0, k = 1", "output": "3"}, {"input": "n = 3, r = 0, c = 0, k = 2", "output": "5"}],
        constraints=["1 <= n <= 8", "0 <= k <= 4"],
        function_name="knightTourSmall",
        starter_code="def knightTourSmall(n: int, r: int, c: int, k: int) -> int:\n    pass\n",
        solution_code="def knightTourSmall(n: int, r: int, c: int, k: int) -> int:\n    visited = {(r, c)}\n    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]\n    curr_level = {(r, c)}\n    for _ in range(k):\n        next_level = set()\n        for cr, cc in curr_level:\n            for dr, dc in moves:\n                nr, nc = cr + dr, cc + dc\n                if 0 <= nr < n and 0 <= nc < n:\n                    next_level.add((nr, nc))\n                    visited.add((nr, nc))\n        curr_level = next_level\n    return len(visited)\n",
        test_cases=[{"input": [3, 0, 0, 1], "expected": 3}, {"input": [3, 0, 0, 2], "expected": 5}, {"input": [1, 0, 0, 1], "expected": 1}],
        hints=["Simulate BFS step-by-step applying the 8 standard knight moves."],
        leetcode_id=None
    ))

    return problems
