"""
Binary Search & Greedy Hard Problems - Part 2 (Floors 486 to 500 - 15 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_bs_greedy_hard_part2():
    problems = []

    # 86. Maximum Profit in Job Scheduling
    problems.append(make_problem(
        pid="bsg-h-max-profit-job-scheduling", title="Job Scheduling (Binary Search DP)",
        wing_id="binary-search-greedy", floor=486, difficulty="hard", visualizer_type="array",
        monster_name="Opportunity Lich", monster_title="Scheduler of Maximum Profit Intervals",
        monster_sprite="lich", monster_color="#8b5cf6", monster_attack="Profit Nexus",
        monster_quote="Max non-overlapping job profit scheduled with binary search DP!",
        description="We have `n` jobs, where every job is scheduled to be done from `startTime[i]` to `endTime[i]`, obtaining a profit of `profit[i]`. You're given the `startTime`, `endTime` and `profit` arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.",
        examples=[{"input": "startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]", "output": "120"}, {"input": "startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]", "output": "150"}],
        constraints=["1 <= startTime.length == endTime.length == profit.length <= 50000"],
        function_name="jobScheduling",
        starter_code="def jobScheduling(startTime: list[int], endTime: list[int], profit: list[int]) -> int:\n    pass\n",
        solution_code="def jobScheduling(startTime: list[int], endTime: list[int], profit: list[int]) -> int:\n    import bisect\n    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])\n    dp = [(0, 0)]  # (endTime, maxProfit)\n    for s, e, p in jobs:\n        # Binary search for job finishing <= s\n        idx = bisect.bisect_right(dp, (s, float('inf'))) - 1\n        total_profit = dp[idx][1] + p\n        if total_profit > dp[-1][1]:\n            dp.append((e, total_profit))\n    return dp[-1][1]\n",
        test_cases=[{"input": [[1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]], "expected": 120}, {"input": [[1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]], "expected": 150}],
        hints=["Sort by end times. For each job, binary search the latest non-overlapping job in DP array."],
        leetcode_id=1235
    ))

    # 87. Maximum Performance of a Team
    problems.append(make_problem(
        pid="bsg-h-max-performance-team", title="Maximum Performance of a Team",
        wing_id="binary-search-greedy", floor=487, difficulty="hard", visualizer_type="array",
        monster_name="Efficiency Titan", monster_title="Amplifier of Synergistic Output",
        monster_sprite="titan", monster_color="#38bdf8", monster_attack="Synergy Slam",
        monster_quote="Maximum performance sum(speeds) * min(efficiencies) modulo 10^9+7!",
        description="You are given two integers `n` and `k` and two integer arrays `speed` and `efficiency` of length `n`. Return the maximum performance of a team of at most `k` engineers modulo `10^9 + 7`.",
        examples=[{"input": "n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2", "output": "60"}, {"input": "n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3", "output": "68"}],
        constraints=["1 <= k <= n <= 100000"],
        function_name="maxPerformance",
        starter_code="def maxPerformance(n: int, speed: list[int], efficiency: list[int], k: int) -> int:\n    pass\n",
        solution_code="def maxPerformance(n: int, speed: list[int], efficiency: list[int], k: int) -> int:\n    import heapq\n    MOD = 10**9 + 7\n    engineers = sorted(zip(efficiency, speed), reverse=True)\n    speed_heap = []\n    speed_sum = 0\n    best = 0\n    for eff, spd in engineers:\n        heapq.heappush(speed_heap, spd)\n        speed_sum += spd\n        if len(speed_heap) > k:\n            speed_sum -= heapq.heappop(speed_heap)\n        best = max(best, speed_sum * eff)\n    return best % MOD\n",
        test_cases=[{"input": [6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2], "expected": 60}, {"input": [6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3], "expected": 68}],
        hints=["Sort descending by efficiency. Iterate each engineer as the minimum efficiency in the team, tracking top k speeds with a min-heap."],
        leetcode_id=1383
    ))

    # 88. Count of Smaller Numbers After Self
    problems.append(make_problem(
        pid="bsg-h-count-smaller-after-self", title="Count of Smaller Numbers After Self",
        wing_id="binary-search-greedy", floor=488, difficulty="hard", visualizer_type="array",
        monster_name="Fenwick Specter", monster_title="Inversion Counter of the Trailing Veil",
        monster_sprite="spectre", monster_color="#ec4899", monster_attack="Inversion Flare",
        monster_quote="For each nums[i], count of smaller elements to its right tallied!",
        description="Given an integer array `nums`, return an integer array `counts` where `counts[i]` is the number of smaller elements to the right of `nums[i]`.",
        examples=[{"input": "nums = [5,2,6,1]", "output": "[2,1,1,0]"}, {"input": "nums = [-1]", "output": "[0]"}, {"input": "nums = [-1,-1]", "output": "[0,0]"}],
        constraints=["1 <= nums.length <= 100000"],
        function_name="countSmaller",
        starter_code="def countSmaller(nums: list[int]) -> list[int]:\n    pass\n",
        solution_code="def countSmaller(nums: list[int]) -> list[int]:\n    import bisect\n    sorted_list = []\n    ans = []\n    for x in reversed(nums):\n        idx = bisect.bisect_left(sorted_list, x)\n        ans.append(idx)\n        sorted_list.insert(idx, x)\n    return ans[::-1]\n",
        test_cases=[{"input": [[5, 2, 6, 1]], "expected": [2, 1, 1, 0]}, {"input": [[-1]], "expected": [0]}, {"input": [[-1, -1]], "expected": [0, 0]}],
        hints=["Iterate from right to left, using binary search (bisect_left) to find position in sorted seen numbers."],
        leetcode_id=315
    ))

    # 89. Reverse Pairs
    problems.append(make_problem(
        pid="bsg-h-reverse-pairs-mergesort", title="Reverse Pairs (nums[i] > 2 * nums[j])",
        wing_id="binary-search-greedy", floor=489, difficulty="hard", visualizer_type="array",
        monster_name="Doubling Hydra", monster_title="Harvester of Significant Inversions",
        monster_sprite="gargoyle", monster_color="#ef4444", monster_attack="Double Cleave",
        monster_quote="Count of index pairs (i < j) where nums[i] > 2 * nums[j] computed!",
        description="Given an integer array `nums`, return the number of reverse pairs in the array. A reverse pair is a pair `(i, j)` where `0 <= i < j < nums.length` and `nums[i] > 2 * nums[j]`.",
        examples=[{"input": "nums = [1,3,2,3,1]", "output": "2"}, {"input": "nums = [2,4,3,5,1]", "output": "3"}],
        constraints=["1 <= nums.length <= 50000"],
        function_name="reversePairs",
        starter_code="def reversePairs(nums: list[int]) -> int:\n    pass\n",
        solution_code="def reversePairs(nums: list[int]) -> int:\n    import bisect\n    seen = []\n    count = 0\n    for x in nums:\n        # count elements in seen that are > 2 * x\n        idx = bisect.bisect_right(seen, 2 * x)\n        count += len(seen) - idx\n        bisect.insort(seen, x)\n    return count\n",
        test_cases=[{"input": [[1, 3, 2, 3, 1]], "expected": 2}, {"input": [[2, 4, 3, 5, 1]], "expected": 3}],
        hints=["Maintain a sorted list of previously processed numbers. Count elements strictly greater than 2 * x using bisect_right."],
        leetcode_id=493
    ))

    # 90. Minimum Cost to Make Array Equal
    problems.append(make_problem(
        pid="bsg-h-min-cost-make-array-equal", title="Min Cost to Make Array Equal (Weighted Median)",
        wing_id="binary-search-greedy", floor=490, difficulty="hard", visualizer_type="array",
        monster_name="Equilibrium Archon", monster_title="Aligner of Weighted Centroids",
        monster_sprite="wizard", monster_color="#10b981", monster_attack="Centroid Convergence",
        monster_quote="Minimum cost to equalize all elements to weighted median computed!",
        description="You are given two 0-indexed integer arrays `nums` and `cost`, both of size `n`. You can increase or decrease any element in `nums` by 1. The cost of doing this on `nums[i]` is `cost[i]`. Return the minimum total cost to make all elements of `nums` equal.",
        examples=[{"input": "nums = [1,3,5,2], cost = [2,3,1,14]", "output": "8"}, {"input": "nums = [2,2,2,2,2], cost = [4,2,8,1,3]", "output": "0"}],
        constraints=["n == nums.length == cost.length", "1 <= n <= 100000"],
        function_name="minCost",
        starter_code="def minCost(nums: list[int], cost: list[int]) -> int:\n    pass\n",
        solution_code="def minCost(nums: list[int], cost: list[int]) -> int:\n    pairs = sorted(zip(nums, cost))\n    total_cost = sum(cost)\n    median = 0\n    cum = 0\n    for x, c in pairs:\n        cum += c\n        if cum >= (total_cost + 1) // 2:\n            median = x\n            break\n    return sum(abs(x - median) * c for x, c in zip(nums, cost))\n",
        test_cases=[{"input": [[1, 3, 5, 2], [2, 3, 1, 14]], "expected": 8}, {"input": [[2, 2, 2, 2, 2], [4, 2, 8, 1, 3]], "expected": 0}],
        hints=["The optimal target value is the weighted median of nums."],
        leetcode_id=2448
    ))

    # 91. Maximum Value at a Given Index in a Bounded Array
    problems.append(make_problem(
        pid="bsg-h-max-value-given-index-bounded", title="Maximum Value at Given Index in Bounded Array",
        wing_id="binary-search-greedy", floor=491, difficulty="hard", visualizer_type="array",
        monster_name="Pyramidal Behemoth", monster_title="Architect of the Monotonic Peak",
        monster_sprite="boss", monster_color="#f59e0b", monster_attack="Apex Quake",
        monster_quote="Max peak value at index such that adjacent diffs <= 1 and sum <= maxSum!",
        description="You are given three positive integers: `n`, `index`, and `maxSum`. Construct an array `nums` of length `n` of positive integers such that `|nums[i] - nums[i+1]| <= 1` and `sum(nums) <= maxSum`. Return the maximum value of `nums[index]`.",
        examples=[{"input": "n = 4, index = 2, maxSum = 6", "output": "2"}, {"input": "n = 6, index = 1, maxSum = 10", "output": "3"}],
        constraints=["1 <= n <= maxSum <= 10^9", "0 <= index < n"],
        function_name="maxValue",
        starter_code="def maxValue(n: int, index: int, maxSum: int) -> int:\n    pass\n",
        solution_code="def maxValue(n: int, index: int, maxSum: int) -> int:\n    def get_sum(peak, count):\n        if count == 0: return 0\n        if peak >= count:\n            return (peak + peak - count + 1) * count // 2\n        return (peak + 1) * peak // 2 + (count - peak)\n    lo, hi = 1, maxSum\n    ans = 1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        left_sum = get_sum(mid - 1, index)\n        right_sum = get_sum(mid - 1, n - 1 - index)\n        if left_sum + mid + right_sum <= maxSum:\n            ans = mid\n            lo = mid + 1\n        else:\n            hi = mid - 1\n    return ans\n",
        test_cases=[{"input": [4, 2, 6], "expected": 2}, {"input": [6, 1, 10], "expected": 3}],
        hints=["Binary search peak value mid in [1, maxSum]. Use arithmetic progression sum on left and right wings."],
        leetcode_id=1802
    ))

    # 92. Minimum Swaps to Arrange a Binary Grid
    problems.append(make_problem(
        pid="bsg-m-min-swaps-binary-grid", title="Minimum Swaps to Arrange Binary Grid",
        wing_id="binary-search-greedy", floor=492, difficulty="hard", visualizer_type="grid",
        monster_name="Matrix Rotator", monster_title="Bubbler of Upper-Triangular Rows",
        monster_sprite="golem", monster_color="#06b6d4", monster_attack="Row Inversion",
        monster_quote="Minimum adjacent row swaps to form all-zero upper triangular matrix!",
        description="Given an `n x n` binary `grid`, in one step you can choose two adjacent rows of the grid and swap them. A grid is said to be valid if all the cells above the main diagonal are zeros. Return the minimum number of steps needed to make the grid valid, or -1 if impossible.",
        examples=[{"input": "grid = [[0,0,1],[1,1,0],[1,0,0]]", "output": "3"}, {"input": "grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]", "output": "-1"}],
        constraints=["n == grid.length", "1 <= n <= 200"],
        function_name="minSwaps",
        starter_code="def minSwaps(grid: list[list[int]]) -> int:\n    pass\n",
        solution_code="def minSwaps(grid: list[list[int]]) -> int:\n    n = len(grid)\n    trailing_zeros = []\n    for row in grid:\n        count = 0\n        for val in reversed(row):\n            if val == 0: count += 1\n            else: break\n        trailing_zeros.append(count)\n    swaps = 0\n    for i in range(n):\n        req = n - 1 - i\n        found = -1\n        for j in range(i, n):\n            if trailing_zeros[j] >= req:\n                found = j\n                break\n        if found == -1: return -1\n        swaps += found - i\n        val = trailing_zeros.pop(found)\n        trailing_zeros.insert(i, val)\n    return swaps\n",
        test_cases=[{"input": [[[0, 0, 1], [1, 1, 0], [1, 0, 0]]], "expected": 3}, {"input": [[[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]], "expected": -1}, {"input": [[[1, 0, 0], [1, 1, 0], [1, 1, 1]]], "expected": 0}],
        hints=["Compute trailing zeroes per row. Row i requires >= n - 1 - i trailing zeroes. Greedily bubble the first qualifying row upwards."],
        leetcode_id=1536
    ))

    # 93. Minimum Number of Taps to Open to Water a Garden
    problems.append(make_problem(
        pid="bsg-h-min-taps-water-garden", title="Minimum Taps to Water Garden",
        wing_id="binary-search-greedy", floor=493, difficulty="hard", visualizer_type="array",
        monster_name="Hydration Titan", monster_title="Opener of Spanning Irrigation Taps",
        monster_sprite="titan", monster_color="#38bdf8", monster_attack="Hydro Cannon",
        monster_quote="Minimum taps opened to irrigate garden interval [0, n]!",
        description="There is a 1D garden on the x-axis from 0 to `n`. There are `n + 1` taps at points `[0, 1, ..., n]`. The `i`-th tap can water `[i - ranges[i], i + ranges[i]]`. Return the minimum number of taps to water the whole garden, or -1 if impossible.",
        examples=[{"input": "n = 5, ranges = [3,4,1,1,0,0]", "output": "1"}, {"input": "n = 3, ranges = [0,0,0,0]", "output": "-1"}],
        constraints=["1 <= n <= 10000", "ranges.length == n + 1"],
        function_name="minTaps",
        starter_code="def minTaps(n: int, ranges: list[int]) -> int:\n    pass\n",
        solution_code="def minTaps(n: int, ranges: list[int]) -> int:\n    max_reach = [0] * (n + 1)\n    for i, r in enumerate(ranges):\n        left = max(0, i - r)\n        right = min(n, i + r)\n        max_reach[left] = max(max_reach[left], right)\n    curr_end = farthest = taps = 0\n    for i in range(n):\n        farthest = max(farthest, max_reach[i])\n        if i == curr_end:\n            taps += 1\n            curr_end = farthest\n            if curr_end <= i: return -1\n    return taps\n",
        test_cases=[{"input": [5, [3, 4, 1, 1, 0, 0]], "expected": 1}, {"input": [3, [0, 0, 0, 0]], "expected": -1}],
        hints=["Convert each tap to interval [left, right], track max_reach[left] = right, then run Jump Game II."],
        leetcode_id=1326
    ))

    # 94. Earliest Possible Day of Full Bloom
    problems.append(make_problem(
        pid="bsg-h-earliest-possible-full-bloom", title="Earliest Possible Day of Full Bloom",
        wing_id="binary-search-greedy", floor=494, difficulty="hard", visualizer_type="array",
        monster_name="Botanical Archon", monster_title="Optimizer of Concurrent Growth Days",
        monster_sprite="spectre", monster_color="#22c55e", monster_attack="Bloom Burst",
        monster_quote="Earliest day when every seed has bloomed achieved!",
        description="You have `n` flower seeds. To plant seed `i`, you need `plantTime[i]` continuous days. Once planted, it takes `growTime[i]` days to bloom (grows concurrently with other activities). Return the earliest possible day where all seeds are blooming.",
        examples=[{"input": "plantTime = [1,4,3], growTime = [2,3,1]", "output": "9"}, {"input": "plantTime = [1,2,3,2], growTime = [2,1,2,1]", "output": "9"}],
        constraints=["n == plantTime.length == growTime.length", "1 <= n <= 100000"],
        function_name="earliestFullBloom",
        starter_code="def earliestFullBloom(plantTime: list[int], growTime: list[int]) -> int:\n    pass\n",
        solution_code="def earliestFullBloom(plantTime: list[int], growTime: list[int]) -> int:\n    seeds = sorted(zip(growTime, plantTime), reverse=True)\n    curr_day = 0\n    max_bloom = 0\n    for g, p in seeds:\n        curr_day += p\n        max_bloom = max(max_bloom, curr_day + g)\n    return max_bloom\n",
        test_cases=[{"input": [[1, 4, 3], [2, 3, 1]], "expected": 9}, {"input": [[1, 2, 3, 2], [2, 1, 2, 1]], "expected": 9}],
        hints=["Greedy strategy: always plant the seed with the longest growth time first."],
        leetcode_id=2136
    ))

    # 95. Stamping the Sequence
    problems.append(make_problem(
        pid="bsg-h-stamping-the-sequence", title="Stamping the Sequence (Greedy Reverse Stamping)",
        wing_id="binary-search-greedy", floor=495, difficulty="hard", visualizer_type="array",
        monster_name="Impression Spectre", monster_title="Inverter of Overlapping Stamps",
        monster_sprite="wraith", monster_color="#8b5cf6", monster_attack="Stamp Impression",
        monster_quote="Stamp positions to transform ????? into target string assembled!",
        description="You are given two strings `stamp` and `target`. Initially, there is a string of length `target.length` filled with `'?'`. In each turn, you may place the stamp on top of the string. Return an array of the index of the left-most letter being stamped at each turn to produce `target`. If impossible, return `[]`.",
        examples=[{"input": "stamp = \"abc\", target = \"ababc\"", "output": "[0,2]"}, {"input": "stamp = \"abca\", target = \"aabcaca\"", "output": "[3,0,1]"}],
        constraints=["1 <= stamp.length <= target.length <= 1000"],
        function_name="movesToStamp",
        starter_code="def movesToStamp(stamp: str, target: str) -> list[int]:\n    pass\n",
        solution_code="def movesToStamp(stamp: str, target: str) -> list[int]:\n    S, T = len(stamp), len(target)\n    target_list = list(target)\n    moves = []\n    stars = 0\n    visited = [False] * (T - S + 1)\n    def can_stamp(idx):\n        changed = False\n        for i in range(S):\n            if target_list[idx + i] == '?': continue\n            if target_list[idx + i] != stamp[i]: return False\n            changed = True\n        return changed\n    while stars < T:\n        stamped = False\n        for i in range(T - S + 1):\n            if not visited[i] and can_stamp(i):\n                visited[i] = True\n                stamped = True\n                moves.append(i)\n                for j in range(S):\n                    if target_list[i + j] != '?':\n                        target_list[i + j] = '?'\n                        stars += 1\n        if not stamped: return []\n    return moves[::-1]\n",
        test_cases=[{"input": ["abc", "ababc"], "expected": [0, 2]}, {"input": ["abca", "aabcaca"], "expected": [3, 0, 1]}],
        hints=["Work backwards from target: repeatedly replace matching stamp substrings with '?'."],
        leetcode_id=936
    ))

    # 96. Minimum Days to Disconnect Island
    problems.append(make_problem(
        pid="bsg-h-min-days-disconnect-island", title="Minimum Days to Disconnect Island",
        wing_id="binary-search-greedy", floor=496, difficulty="hard", visualizer_type="grid",
        monster_name="Severance Archon", monster_title="Isolator of Contiguous Archipelagos",
        monster_sprite="boss", monster_color="#ef4444", monster_attack="Articulation Cleave",
        monster_quote="Island disconnected in at most 2 flips!",
        description="Given an `m x n` binary grid `grid` where 1 represents land and 0 represents water. An island is a 4-directionally connected group of 1s. A grid is disconnected if it has 0 islands or more than 1 island. In one day you can change any land cell to water. Return the minimum number of days to disconnect the grid. (Note: answer is always 0, 1, or 2).",
        examples=[{"input": "grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]", "output": "2"}, {"input": "grid = [[1,1]]", "output": "2"}],
        constraints=["1 <= m, n <= 30"],
        function_name="minDaysDisconnect",
        starter_code="def minDaysDisconnect(grid: list[list[int]]) -> int:\n    pass\n",
        solution_code="def minDaysDisconnect(grid: list[list[int]]) -> int:\n    R, C = len(grid), len(grid[0])\n    def count_islands():\n        visited = set()\n        islands = 0\n        def dfs(r, c):\n            visited.add((r, c))\n            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:\n                nr, nc = r + dr, c + dc\n                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1 and (nr, nc) not in visited:\n                    dfs(nr, nc)\n        for r in range(R):\n            for c in range(C):\n                if grid[r][c] == 1 and (r, c) not in visited:\n                    islands += 1\n                    dfs(r, c)\n        return islands\n    if count_islands() != 1: return 0\n    # Try removing 1 cell\n    for r in range(R):\n        for c in range(C):\n            if grid[r][c] == 1:\n                grid[r][c] = 0\n                if count_islands() != 1:\n                    grid[r][c] = 1\n                    return 1\n                grid[r][c] = 1\n    return 2\n",
        test_cases=[{"input": [[[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]], "expected": 2}, {"input": [[[1, 1]]], "expected": 2}, {"input": [[[1, 0], [0, 1]]], "expected": 0}],
        hints=["Any island can be disconnected in at most 2 operations (removing corner neighbors). Test 0, 1, then default to 2."],
        leetcode_id=1568
    ))

    # 97. Equal Rational Numbers
    problems.append(make_problem(
        pid="bsg-h-equal-rational-numbers", title="Equal Rational Numbers",
        wing_id="binary-search-greedy", floor=497, difficulty="hard", visualizer_type="array",
        monster_name="Fractional Sphinx", monster_title="Unmasker of Repeating Decimal Equivalence",
        monster_sprite="sphinx", monster_color="#06b6d4", monster_attack="Geometric Sum",
        monster_quote="Repeating decimal representations evaluated for exact equality!",
        description="Given two strings `s` and `t`, each representing a rational number, return `True` if and only if they represent the same number. Decimals may have non-repeating and repeating parts like `0.(52)`.",
        examples=[{"input": "s = \"0.(52)\", t = \"0.5(25)\"", "output": "True"}, {"input": "s = \"0.1666(6)\", t = \"0.166(66)\"", "output": "True"}, {"input": "s = \"0.9(9)\", t = \"1.\"", "output": "True"}],
        constraints=["Each string is at most 30 characters long."],
        function_name="isRationalEqual",
        starter_code="def isRationalEqual(s: str, t: str) -> bool:\n    pass\n",
        solution_code="def isRationalEqual(s: str, t: str) -> bool:\n    from fractions import Fraction\n    def parse(val):\n        if '(' not in val:\n            return Fraction(val)\n        dot = val.find('.')\n        left_paren = val.find('(')\n        integer_part = val[:dot] if dot != -1 else val[:left_paren]\n        non_repeat = val[dot + 1:left_paren] if dot != -1 else \"\"\n        repeat = val[left_paren + 1:-1]\n        res = Fraction(int(integer_part) if integer_part else 0, 1)\n        if non_repeat:\n            res += Fraction(int(non_repeat), 10 ** len(non_repeat))\n        repeat_frac = Fraction(int(repeat), (10 ** len(repeat) - 1) * (10 ** len(non_repeat)))\n        res += repeat_frac\n        return res\n    return parse(s) == parse(t)\n",
        test_cases=[{"input": ["0.(52)", "0.5(25)"], "expected": True}, {"input": ["0.1666(6)", "0.166(66)"], "expected": True}, {"input": ["0.9(9)", "1."], "expected": True}],
        hints=["Convert repeating decimal into exact Fraction using infinite geometric series formula."],
        leetcode_id=972
    ))

    # 98. Minimum Space Wasted From Packaging
    problems.append(make_problem(
        pid="bsg-h-min-space-wasted-packaging", title="Minimum Space Wasted From Packaging",
        wing_id="binary-search-greedy", floor=498, difficulty="hard", visualizer_type="array",
        monster_name="Volumetric Golem", monster_title="Compressor of Empty Box Space",
        monster_sprite="golem", monster_color="#f59e0b", monster_attack="Volume Clamp",
        monster_quote="Supplier with minimum total wasted box space selected!",
        description="You have `n` packages with given `packages` weights. You are given `m` suppliers, each offering different box sizes `boxes[j]`. A package fits in a box if weight <= box size. Each package must be packed in a box. Return the minimum total wasted space modulo `10^9 + 7`, or `-1` if no supplier can package all packages.",
        examples=[{"input": "packages = [2,3,5], boxes = [[4,8],[2,8]]", "output": "6"}, {"input": "packages = [2,3,5], boxes = [[1,4],[2,3],[3,4]]", "output": "-1"}],
        constraints=["1 <= packages.length <= 100000", "1 <= boxes.length <= 100000"],
        function_name="minWastedSpace",
        starter_code="def minWastedSpace(packages: list[int], boxes: list[list[int]]) -> int:\n    pass\n",
        solution_code="def minWastedSpace(packages: list[int], boxes: list[list[int]]) -> int:\n    import bisect\n    MOD = 10**9 + 7\n    packages.sort()\n    total_pkg = sum(packages)\n    ans = float('inf')\n    for supplier in boxes:\n        supplier.sort()\n        if supplier[-1] < packages[-1]: continue\n        prev_idx = 0\n        total_box_space = 0\n        for b in supplier:\n            idx = bisect.bisect_right(packages, b)\n            count = idx - prev_idx\n            total_box_space += count * b\n            prev_idx = idx\n            if idx == len(packages): break\n        ans = min(ans, total_box_space - total_pkg)\n    return ans % MOD if ans != float('inf') else -1\n",
        test_cases=[{"input": [[2, 3, 5], [[4, 8], [2, 8]]], "expected": 6}, {"input": [[2, 3, 5], [[1, 4], [2, 3], [3, 4]]], "expected": -1}],
        hints=["Sort packages. For each box size, binary search how many packages it can cover and accumulate."],
        leetcode_id=1889
    ))

    # 99. Swim in Rising Water (Binary Search Variant)
    problems.append(make_problem(
        pid="bsg-h-swim-rising-water-bs", title="Swim in Rising Water (Binary Search BFS)",
        wing_id="binary-search-greedy", floor=499, difficulty="hard", visualizer_type="grid",
        monster_name="Submersion Drake", monster_title="Ruler of Rising Water Heights",
        monster_sprite="dragon", monster_color="#38bdf8", monster_attack="High Water Torrent",
        monster_quote="Least water level found via binary search on matrix heights!",
        description="On an `n x n` grid, find the least time t such that you can reach bottom-right from top-left without exceeding elevation t.",
        examples=[{"input": "grid = [[0,2],[1,3]]", "output": "3"}, {"input": "grid = [[0,1,2],[5,4,3],[6,7,8]]", "output": "8"}],
        constraints=["n == grid.length", "1 <= n <= 50"],
        function_name="swimInWaterBS",
        starter_code="def swimInWaterBS(grid: list[list[int]]) -> int:\n    pass\n",
        solution_code="def swimInWaterBS(grid: list[list[int]]) -> int:\n    n = len(grid)\n    from collections import deque\n    def can_reach(t):\n        if grid[0][0] > t: return False\n        q = deque([(0, 0)])\n        visited = {(0, 0)}\n        while q:\n            r, c = q.popleft()\n            if r == n - 1 and c == n - 1: return True\n            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:\n                nr, nc = r + dr, c + dc\n                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] <= t:\n                    visited.add((nr, nc))\n                    q.append((nr, nc))\n        return False\n    lo, hi = 0, n * n - 1\n    ans = hi\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        if can_reach(mid):\n            ans = mid\n            hi = mid - 1\n        else:\n            lo = mid + 1\n    return ans\n",
        test_cases=[{"input": [[[0, 2], [1, 3]]], "expected": 3}, {"input": [[[0, 1, 2], [5, 4, 3], [6, 7, 8]]], "expected": 8}],
        hints=["Binary search water height t in [0, n*n-1]. Check reachability via standard BFS."],
        leetcode_id=778
    ))

    # 100. Binary Search & Greedy Final Boss: Maximum Building Height
    problems.append(make_problem(
        pid="bsg-h-boss-max-building-height", title="Maximum Building Height (Two-Pass Clamp)",
        wing_id="binary-search-greedy", floor=500, difficulty="hard", visualizer_type="array",
        monster_name="Apex Architect Sovereign", monster_title="Master of All 100 Binary Search & Greedy Floors",
        monster_sprite="boss", monster_color="#ef4444", monster_attack="Apex Spire Cleave",
        monster_quote="The absolute maximum skyscraper height across n plots constructed!",
        description="You want to build `n` buildings in a row. Restrictions give max height at certain buildings: `restrictions[i] = [idi, maxHeighti]`. Building 1 has height 0, and adjacent heights differ by at most 1. Return the maximum possible height of the tallest building.",
        examples=[{"input": "n = 5, restrictions = [[2,1],[4,1]]", "output": "2"}, {"input": "n = 6, restrictions = []", "output": "5"}, {"input": "n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]", "output": "5"}],
        constraints=["2 <= n <= 10^9", "0 <= restrictions.length <= 100000"],
        function_name="maxBuilding",
        starter_code="def maxBuilding(n: int, restrictions: list[list[int]]) -> int:\n    pass\n",
        solution_code="def maxBuilding(n: int, restrictions: list[list[int]]) -> int:\n    r = [[1, 0]] + sorted(restrictions) + [[n, n - 1]]\n    m = len(r)\n    # Left-to-right pass\n    for i in range(1, m):\n        dist = r[i][0] - r[i - 1][0]\n        r[i][1] = min(r[i][1], r[i - 1][1] + dist)\n    # Right-to-left pass\n    for i in range(m - 2, -1, -1):\n        dist = r[i + 1][0] - r[i][0]\n        r[i][1] = min(r[i][1], r[i + 1][1] + dist)\n    # Compute max peak between consecutive restrictions\n    ans = 0\n    for i in range(1, m):\n        x1, h1 = r[i - 1]\n        x2, h2 = r[i]\n        peak = (h1 + h2 + x2 - x1) // 2\n        ans = max(ans, peak)\n    return ans\n",
        test_cases=[{"input": [5, [[2, 1], [4, 1]]], "expected": 2}, {"input": [6, []], "expected": 5}, {"input": [10, [[5, 3], [2, 5], [7, 4], [10, 3]]], "expected": 5}],
        hints=["Two-pass greedy height relaxation (left-to-right, right-to-left). Max peak between adjacent points is (h1 + h2 + x2 - x1) // 2."],
        leetcode_id=1840
    ))

    return problems
