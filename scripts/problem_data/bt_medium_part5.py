"""
Backtracking Medium Problems Part 5 (Problems 61 to 70 - 10 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_bt_medium_part5():
    problems = []

    # 61. Subsets with Exact Sum K
    problems.append(make_problem(
        pid="bt-m-subsets-sum-k", title="Subsets with Exact Sum K",
        wing_id="backtracking", floor=261, difficulty="medium", visualizer_type="array",
        monster_name="Exact Sum Golem", monster_title="Weigher of Exact Subset Balance",
        monster_sprite="golem", monster_color="#10b981", monster_attack="Balance Beam",
        monster_quote="Every subset matching target sum k identified!",
        description="Given an array of integers `nums` and an integer `k`, return all subsets of `nums` that sum to exactly `k`, sorted by length and then elements.",
        examples=[{"input": "nums = [1,2,3,4,5], k = 5", "output": "[[5],[1,4],[2,3]]"}],
        constraints=["1 <= len(nums) <= 12", "1 <= nums[i] <= 100", "1 <= k <= 500"],
        function_name="subsetsSumK",
        starter_code="def subsetsSumK(nums: list[int], k: int) -> list[list[int]]:\n    pass\n",
        solution_code="def subsetsSumK(nums: list[int], k: int) -> list[list[int]]:\n    nums.sort()\n    res = []\n    def backtrack(idx, rem, path):\n        if rem == 0:\n            res.append(list(path))\n            return\n        for i in range(idx, len(nums)):\n            if nums[i] > rem: break\n            path.append(nums[i])\n            backtrack(i + 1, rem - nums[i], path)\n            path.pop()\n    backtrack(0, k, [])\n    res.sort(key=lambda s: (len(s), s))\n    return res\n",
        test_cases=[{"input": [[1, 2, 3, 4, 5], 5], "expected": [[5], [1, 4], [2, 3]]}, {"input": [[2, 4, 6], 5], "expected": []}, {"input": [[3], 3], "expected": [[3]]}],
        hints=["Sort nums to break early when nums[i] > rem."],
        leetcode_id=None
    ))

    # 62. Palindromic Permutations
    problems.append(make_problem(
        pid="bt-m-generate-palindromes", title="Palindromic Permutations Generator",
        wing_id="backtracking", floor=262, difficulty="medium", visualizer_type="array",
        monster_name="Mirror Banshee", monster_title="Reconstructor of Symmetric Words",
        monster_sprite="wraith", monster_color="#ec4899", monster_attack="Mirror Wail",
        monster_quote="All palindromic permutations assembled around the central axis!",
        description="Given a string `s`, return all the palindromic permutations (without duplicates) of `s`. If no palindromic permutation could be form, return an empty list.",
        examples=[{"input": "s = \"aabb\"", "output": "[\"abba\",\"baab\"]"}, {"input": "s = \"abc\"", "output": "[]"}],
        constraints=["1 <= len(s) <= 12"],
        function_name="generatePalindromes",
        starter_code="def generatePalindromes(s: str) -> list[str]:\n    pass\n",
        solution_code="def generatePalindromes(s: str) -> list[str]:\n    from collections import Counter\n    counts = Counter(s)\n    odd_chars = [ch for ch, c in counts.items() if c % 2 == 1]\n    if len(odd_chars) > 1: return []\n    mid = odd_chars[0] if odd_chars else ''\n    half = []\n    for ch, c in counts.items():\n        half.extend([ch] * (c // 2))\n    half.sort()\n    res = []\n    used = [False] * len(half)\n    def backtrack(curr):\n        if len(curr) == len(half):\n            prefix = ''.join(curr)\n            res.append(prefix + mid + prefix[::-1])\n            return\n        for i in range(len(half)):\n            if used[i]: continue\n            if i > 0 and half[i] == half[i - 1] and not used[i - 1]: continue\n            used[i] = True\n            curr.append(half[i])\n            backtrack(curr)\n            curr.pop()\n            used[i] = False\n    backtrack([])\n    return res\n",
        test_cases=[{"input": ["aabb"], "expected": ["abba", "baab"]}, {"input": ["abc"], "expected": []}, {"input": ["a"], "expected": ["a"]}],
        hints=["Permute the first half of the characters and mirror across the single odd character."],
        leetcode_id=267
    ))

    # 63. Permutations with Adjacent Difference
    problems.append(make_problem(
        pid="bt-m-permute-diff-two", title="Permutations with Delta >= 2",
        wing_id="backtracking", floor=263, difficulty="medium", visualizer_type="array",
        monster_name="Spacing Drake", monster_title="Separater of Consecutive Neighbours",
        monster_sprite="dragon", monster_color="#38bdf8", monster_attack="Spacing Breath",
        monster_quote="Adjacent values differed by at least 2 throughout the sequence!",
        description="Given an integer `n`, return all permutations of integers `[1, ..., n]` such that for every adjacent pair of numbers, `abs(perm[i] - perm[i+1]) >= 2`. Return results in sorted order.",
        examples=[{"input": "n = 4", "output": "[[2,4,1,3],[3,1,4,2]]"}, {"input": "n = 3", "output": "[]"}],
        constraints=["1 <= n <= 7"],
        function_name="permuteDiffTwo",
        starter_code="def permuteDiffTwo(n: int) -> list[list[int]]:\n    pass\n",
        solution_code="def permuteDiffTwo(n: int) -> list[list[int]]:\n    nums = list(range(1, n + 1))\n    res = []\n    used = [False] * n\n    def backtrack(curr):\n        if len(curr) == n:\n            res.append(list(curr))\n            return\n        for i in range(n):\n            if not used[i]:\n                if not curr or abs(curr[-1] - nums[i]) >= 2:\n                    used[i] = True\n                    curr.append(nums[i])\n                    backtrack(curr)\n                    curr.pop()\n                    used[i] = False\n    backtrack([])\n    return sorted(res)\n",
        test_cases=[{"input": [4], "expected": [[2, 4, 1, 3], [3, 1, 4, 2]]}, {"input": [3], "expected": []}, {"input": [1], "expected": [[1]]}],
        hints=["Enforce abs(curr[-1] - nums[i]) >= 2 when picking candidate i."],
        leetcode_id=None
    ))

    # 64. Count Word Occurrences in Grid
    problems.append(make_problem(
        pid="bt-m-word-search-count", title="Count Word Paths in Grid",
        wing_id="backtracking", floor=264, difficulty="medium", visualizer_type="graph",
        monster_name="Grid Hound", monster_title="Sniffer of Multiple Word Paths",
        monster_sprite="demon", monster_color="#ef4444", monster_attack="Multi-Scent Claw",
        monster_quote="All distinct paths constructing the word counted!",
        description="Given an `m x n` grid of characters `board` and a string `word`, return the total number of distinct non-intersecting grid paths that spell `word`.",
        examples=[{"input": "board = [[\"A\",\"B\"],[\"B\",\"A\"]], word = \"AB\"", "output": "4"}],
        constraints=["1 <= len(board), len(board[0]) <= 5", "1 <= len(word) <= 6"],
        function_name="countWordGrid",
        starter_code="def countWordGrid(board: list[list[str]], word: str) -> int:\n    pass\n",
        solution_code="def countWordGrid(board: list[list[str]], word: str) -> int:\n    m, n = len(board), len(board[0])\n    def dfs(r, c, idx):\n        if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[idx]: return 0\n        if idx == len(word) - 1: return 1\n        temp = board[r][c]\n        board[r][c] = '#'\n        total = dfs(r+1, c, idx+1) + dfs(r-1, c, idx+1) + dfs(r, c+1, idx+1) + dfs(r, c-1, idx+1)\n        board[r][c] = temp\n        return total\n    ans = 0\n    for i in range(m):\n        for j in range(n):\n            ans += dfs(i, j, 0)\n    return ans\n",
        test_cases=[{"input": [[["A", "B"], ["B", "A"]], "AB"], "expected": 4}, {"input": [[["A", "A"], ["A", "A"]], "AA"], "expected": 8}, {"input": [[["A", "B"], ["C", "D"]], "ACD"], "expected": 1}],
        hints=["Sum returns of dfs in 4 directions instead of early return on True."],
        leetcode_id=None
    ))

    # 65. Combination Lock Turns
    problems.append(make_problem(
        pid="bt-m-combination-lock-turns", title="Minimum Turns to Unlock Code",
        wing_id="backtracking", floor=265, difficulty="medium", visualizer_type="array",
        monster_name="Dial Fiend", monster_title="Tumbler of Multi-Dial Tumblers",
        monster_sprite="golem", monster_color="#f59e0b", monster_attack="Dial Twist",
        monster_quote="Circular rotation distance on each dial minimized!",
        description="A circular dial has digits `0` through `9`. Given a starting code `start` and a target code `target` of the same length, return the minimum total turns needed to rotate the dials from start to target.",
        examples=[{"input": "start = \"1234\", target = \"2468\"", "output": "10"}, {"input": "start = \"0000\", target = \"5555\"", "output": "20"}],
        constraints=["len(start) == len(target) <= 10"],
        function_name="minTurnsLock",
        starter_code="def minTurnsLock(start: str, target: str) -> int:\n    pass\n",
        solution_code="def minTurnsLock(start: str, target: str) -> int:\n    total = 0\n    for s, t in zip(start, target):\n        diff = abs(int(s) - int(t))\n        total += min(diff, 10 - diff)\n    return total\n",
        test_cases=[{"input": ["1234", "2468"], "expected": 10}, {"input": ["0000", "5555"], "expected": 20}, {"input": ["0", "9"], "expected": 1}],
        hints=["Distance between digits a and b on circular 0-9 dial is min(abs(a-b), 10 - abs(a-b))."],
        leetcode_id=None
    ))

    # 66. Subsets in Sum Range [L, R]
    problems.append(make_problem(
        pid="bt-m-subset-sums-target-range", title="Subsets in Sum Range [L, R]",
        wing_id="backtracking", floor=266, difficulty="medium", visualizer_type="array",
        monster_name="Bandpass Specter", monster_title="Filterer of Interval Energy",
        monster_sprite="wraith", monster_color="#8b5cf6", monster_attack="Bandpass Flare",
        monster_quote="Subsets falling strictly between L and R counted!",
        description="Given an array of integers `nums` and two integers `low` and `high`, return the number of non-empty subsets whose sum lies in `[low, high]` inclusive.",
        examples=[{"input": "nums = [1,2,3], low = 3, high = 5", "output": "4"}],
        constraints=["1 <= len(nums) <= 12", "low <= high"],
        function_name="subsetsInSumRange",
        starter_code="def subsetsInSumRange(nums: list[int], low: int, high: int) -> int:\n    pass\n",
        solution_code="def subsetsInSumRange(nums: list[int], low: int, high: int) -> int:\n    count = 0\n    def dfs(idx, curr_sum, picked):\n        nonlocal count\n        if idx == len(nums):\n            if picked and low <= curr_sum <= high: count += 1\n            return\n        dfs(idx + 1, curr_sum, picked)\n        dfs(idx + 1, curr_sum + nums[idx], True)\n    dfs(0, 0, False)\n    return count\n",
        test_cases=[{"input": [[1, 2, 3], 3, 5], "expected": 4}, {"input": [[2, 4], 1, 3], "expected": 1}, {"input": [[5], 6, 10], "expected": 0}],
        hints=["Track sum of picked elements. Verify low <= sum <= high at terminal state."],
        leetcode_id=None
    ))

    # 67. Climbing Stairs Variable Steps
    problems.append(make_problem(
        pid="bt-m-climbing-stairs-variable", title="Climbing Stairs with Custom Steps",
        wing_id="backtracking", floor=267, difficulty="medium", visualizer_type="array",
        monster_name="Stairway Chimera", monster_title="Leaper of Multi-Step Risers",
        monster_sprite="demon", monster_color="#10b981", monster_attack="Riser Strike",
        monster_quote="All distinct step sequences reaching the top floor found!",
        description="You are climbing a staircase of `n` steps. You are given an array of allowed step sizes `steps`. In each step, you can climb any number of steps listed in `steps`. Return all unique paths to reach step `n` sorted lexicographically.",
        examples=[{"input": "n = 4, steps = [1,2]", "output": "[[1,1,1,1],[1,1,2],[1,2,1],[2,1,1],[2,2]]"}],
        constraints=["1 <= n <= 10", "1 <= len(steps) <= 4"],
        function_name="climbStairsVariable",
        starter_code="def climbStairsVariable(n: int, steps: list[int]) -> list[list[int]]:\n    pass\n",
        solution_code="def climbStairsVariable(n: int, steps: list[int]) -> list[list[int]]:\n    steps.sort()\n    res = []\n    def dfs(rem, path):\n        if rem == 0:\n            res.append(list(path))\n            return\n        for s in steps:\n            if s <= rem:\n                dfs(rem - s, path + [s])\n    dfs(n, [])\n    return res\n",
        test_cases=[{"input": [4, [1, 2]], "expected": [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]}, {"input": [3, [1, 3]], "expected": [[1, 1, 1], [3]]}],
        hints=["Backtrack over allowed step sizes until rem == 0."],
        leetcode_id=None
    ))

    # 68. Derangements of Array
    problems.append(make_problem(
        pid="bt-m-generate-derangements", title="Array Derangements (Subhat)",
        wing_id="backtracking", floor=268, difficulty="medium", visualizer_type="array",
        monster_name="Derangement Lich", monster_title="Inverter of Natural Order",
        monster_sprite="lich", monster_color="#ec4899", monster_attack="Chaos Spell",
        monster_quote="No element stayed in its original position in any derangement!",
        description="A derangement of `[1, 2, ..., n]` is a permutation `P` where no element appears in its original position (i.e., `P[i] != i + 1` for all `i`). Return all derangements of length `n` in sorted order.",
        examples=[{"input": "n = 3", "output": "[[2,3,1],[3,1,2]]"}, {"input": "n = 2", "output": "[[2,1]]"}],
        constraints=["1 <= n <= 5"],
        function_name="generateDerangements",
        starter_code="def generateDerangements(n: int) -> list[list[int]]:\n    pass\n",
        solution_code="def generateDerangements(n: int) -> list[list[int]]:\n    nums = list(range(1, n + 1))\n    res = []\n    used = [False] * n\n    def backtrack(pos, curr):\n        if pos == n:\n            res.append(list(curr))\n            return\n        for i in range(n):\n            if not used[i] and nums[i] != pos + 1:\n                used[i] = True\n                curr.append(nums[i])\n                backtrack(pos + 1, curr)\n                curr.pop()\n                used[i] = False\n    backtrack(0, [])\n    return res\n",
        test_cases=[{"input": [3], "expected": [[2, 3, 1], [3, 1, 2]]}, {"input": [2], "expected": [[2, 1]]}, {"input": [1], "expected": []}],
        hints=["Permutation condition: nums[i] != pos + 1."],
        leetcode_id=None
    ))

    # 69. Combination Sum with 4 Coins
    problems.append(make_problem(
        pid="bt-m-combination-sum-coins", title="Combination Sum with 4 Coins",
        wing_id="backtracking", floor=269, difficulty="medium", visualizer_type="array",
        monster_name="Quarter Warden", monster_title="Coin Changer of Exact Denominations",
        monster_sprite="golem", monster_color="#f59e0b", monster_attack="Coin Smash",
        monster_quote="Combinations of [1, 5, 10, 25] coins totaled exact change!",
        description="Given an integer `target`, return all combinations of coin denominations `[1, 5, 10, 25]` that sum up to `target`. Each coin may be used an unlimited number of times.",
        examples=[{"input": "target = 10", "output": "[[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,5],[5,5],[10]]"}],
        constraints=["1 <= target <= 30"],
        function_name="combinationSumCoins",
        starter_code="def combinationSumCoins(target: int) -> list[list[int]]:\n    pass\n",
        solution_code="def combinationSumCoins(target: int) -> list[list[int]]:\n    coins = [1, 5, 10, 25]\n    res = []\n    def backtrack(idx, rem, path):\n        if rem == 0:\n            res.append(list(path))\n            return\n        for i in range(idx, len(coins)):\n            if coins[i] > rem: break\n            path.append(coins[i])\n            backtrack(i, rem - coins[i], path)\n            path.pop()\n    backtrack(0, target, [])\n    res.sort(key=lambda c: (len(c), c))\n    return res\n",
        test_cases=[{"input": [10], "expected": [[10], [5, 5], [1, 1, 1, 1, 1, 5], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]}, {"input": [5], "expected": [[5], [1, 1, 1, 1, 1]]}],
        hints=["Unbounded knapsack combination sum with sorted coin denominations."],
        leetcode_id=None
    ))

    # 70. Target Sum with Multiplication and Addition
    problems.append(make_problem(
        pid="bt-m-target-sum-mult-add", title="Target Sum with (+ and *)",
        wing_id="backtracking", floor=270, difficulty="medium", visualizer_type="array",
        monster_name="Arithmetic Gorgon", monster_title="Weaver of Plus and Times Trees",
        monster_sprite="slime", monster_color="#8b5cf6", monster_attack="Arithmetic Ray",
        monster_quote="Every + and * combination reaching target evaluated!",
        description="Given an array of positive integers `nums` and an integer `target`, insert either `'+'` or `'*'` between every adjacent pair of numbers (evaluating left-to-right). Return the count of assignments that equal `target`.",
        examples=[{"input": "nums = [2,3,4], target = 10", "output": "1"}, {"input": "nums = [2,2,2], target = 8", "output": "1"}],
        constraints=["2 <= len(nums) <= 8", "1 <= nums[i] <= 10"],
        function_name="targetSumOps",
        starter_code="def targetSumOps(nums: list[int], target: int) -> int:\n    pass\n",
        solution_code="def targetSumOps(nums: list[int], target: int) -> int:\n    count = 0\n    def dfs(idx, curr_val):\n        nonlocal count\n        if idx == len(nums):\n            if curr_val == target: count += 1\n            return\n        dfs(idx + 1, curr_val + nums[idx])\n        dfs(idx + 1, curr_val * nums[idx])\n    dfs(1, nums[0])\n    return count\n",
        test_cases=[{"input": [[2, 3, 4], 10], "expected": 1}, {"input": [[2, 2, 2], 8], "expected": 2}, {"input": [[2, 2, 2], 6], "expected": 2}],
        hints=["Branch on + and * at each step evaluating sequentially from left to right."],
        leetcode_id=None
    ))

    return problems
