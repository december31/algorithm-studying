"""
Binary Search & Greedy Medium Problems - Part 1 (Floors 411 to 425 - 15 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_bs_greedy_medium_part1():
    problems = []

    # 11. Search in Rotated Sorted Array
    problems.append(make_problem(
        pid="bsg-m-search-rotated-sorted-array", title="Search in Rotated Sorted Array",
        wing_id="binary-search-greedy", floor=411, difficulty="medium", visualizer_type="array",
        monster_name="Rotational Fiend", monster_title="Disruptor of Pivot Axes",
        monster_sprite="imp", monster_color="#ef4444", monster_attack="Pivot Shift",
        monster_quote="Target located within circularly rotated sorted partition!",
        description="Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`. You must write an algorithm with `O(log n)` runtime complexity.",
        examples=[{"input": "nums = [4,5,6,7,0,1,2], target = 0", "output": "4"}, {"input": "nums = [4,5,6,7,0,1,2], target = 3", "output": "-1"}],
        constraints=["1 <= nums.length <= 5000", "All values of nums are unique"],
        function_name="searchRotated",
        starter_code="def searchRotated(nums: list[int], target: int) -> int:\n    pass\n",
        solution_code="def searchRotated(nums: list[int], target: int) -> int:\n    lo, hi = 0, len(nums) - 1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        if nums[mid] == target: return mid\n        # Left half is sorted\n        if nums[lo] <= nums[mid]:\n            if nums[lo] <= target < nums[mid]:\n                hi = mid - 1\n            else:\n                lo = mid + 1\n        # Right half is sorted\n        else:\n            if nums[mid] < target <= nums[hi]:\n                lo = mid + 1\n            else:\n                hi = mid - 1\n    return -1\n",
        test_cases=[{"input": [[4, 5, 6, 7, 0, 1, 2], 0], "expected": 4}, {"input": [[4, 5, 6, 7, 0, 1, 2], 3], "expected": -1}, {"input": [[1], 0], "expected": -1}],
        hints=["Identify which half is cleanly sorted by comparing nums[lo] with nums[mid], then check if target falls in that half."],
        leetcode_id=33
    ))

    # 12. Find Minimum in Rotated Sorted Array
    problems.append(make_problem(
        pid="bsg-m-find-min-rotated-sorted-array", title="Find Minimum in Rotated Sorted Array",
        wing_id="binary-search-greedy", floor=412, difficulty="medium", visualizer_type="array",
        monster_name="Inflection Specter", monster_title="Seeker of the Drop Point",
        monster_sprite="spectre", monster_color="#38bdf8", monster_attack="Drop Point Shear",
        monster_quote="Smallest element at circular inflection boundary found!",
        description="Given the sorted rotated array `nums` of unique elements, return the minimum element of this array. You must write an algorithm that runs in `O(log n)` time.",
        examples=[{"input": "nums = [3,4,5,1,2]", "output": "1"}, {"input": "nums = [4,5,6,7,0,1,2]", "output": "0"}],
        constraints=["n == nums.length", "1 <= n <= 5000"],
        function_name="findMin",
        starter_code="def findMin(nums: list[int]) -> int:\n    pass\n",
        solution_code="def findMin(nums: list[int]) -> int:\n    lo, hi = 0, len(nums) - 1\n    while lo < hi:\n        mid = (lo + hi) // 2\n        if nums[mid] > nums[hi]:\n            lo = mid + 1\n        else:\n            hi = mid\n    return nums[lo]\n",
        test_cases=[{"input": [[3, 4, 5, 1, 2]], "expected": 1}, {"input": [[4, 5, 6, 7, 0, 1, 2]], "expected": 0}, {"input": [[11, 13, 15, 17]], "expected": 11}],
        hints=["Compare nums[mid] to nums[hi]. If nums[mid] > nums[hi], the minimum must lie strictly to the right."],
        leetcode_id=153
    ))

    # 13. Find First and Last Position of Element in Sorted Array
    problems.append(make_problem(
        pid="bsg-m-first-last-position-sorted", title="First and Last Position in Sorted Array",
        wing_id="binary-search-greedy", floor=413, difficulty="medium", visualizer_type="array",
        monster_name="Range Drake", monster_title="Guardian of Target Spans",
        monster_sprite="dragon", monster_color="#8b5cf6", monster_attack="Span Blast",
        monster_quote="Starting and ending index range [first, last] discovered!",
        description="Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value. If target is not found, return `[-1, -1]`. You must write an algorithm with `O(log n)` runtime complexity.",
        examples=[{"input": "nums = [5,7,7,8,8,10], target = 8", "output": "[3,4]"}, {"input": "nums = [5,7,7,8,8,10], target = 6", "output": "[-1,-1]"}],
        constraints=["0 <= nums.length <= 100000"],
        function_name="searchRange",
        starter_code="def searchRange(nums: list[int], target: int) -> list[int]:\n    pass\n",
        solution_code="def searchRange(nums: list[int], target: int) -> list[int]:\n    def find_bound(is_first):\n        lo, hi = 0, len(nums) - 1\n        bound = -1\n        while lo <= hi:\n            mid = (lo + hi) // 2\n            if nums[mid] == target:\n                bound = mid\n                if is_first: hi = mid - 1\n                else: lo = mid + 1\n            elif nums[mid] < target: lo = mid + 1\n            else: hi = mid - 1\n        return bound\n    return [find_bound(True), find_bound(False)]\n",
        test_cases=[{"input": [[5, 7, 7, 8, 8, 10], 8], "expected": [3, 4]}, {"input": [[5, 7, 7, 8, 8, 10], 6], "expected": [-1, -1]}, {"input": [[], 0], "expected": [-1, -1]}],
        hints=["Run two separate binary searches: one biasing left (hi = mid - 1), one biasing right (lo = mid + 1)."],
        leetcode_id=34
    ))

    # 14. Search a 2D Matrix
    problems.append(make_problem(
        pid="bsg-m-search-2d-matrix", title="Search a 2D Matrix (Flattened Bisection)",
        wing_id="binary-search-greedy", floor=414, difficulty="medium", visualizer_type="grid",
        monster_name="Matrix Automaton", monster_title="Surveyor of Monotonic Rows",
        monster_sprite="golem", monster_color="#10b981", monster_attack="Grid Pulse",
        monster_quote="Target presence within strictly sorted 2D grid verified!",
        description="You are given an `m x n` integer matrix `matrix` with the following two properties: Each row is sorted in non-decreasing order. The first integer of each row is greater than the last integer of the previous row. Given an integer `target`, return `True` if `target` is in `matrix` or `False` otherwise.",
        examples=[{"input": "matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3", "output": "True"}],
        constraints=["m == matrix.length", "n == matrix[i].length", "1 <= m, n <= 100"],
        function_name="searchMatrix",
        starter_code="def searchMatrix(matrix: list[list[int]], target: int) -> bool:\n    pass\n",
        solution_code="def searchMatrix(matrix: list[list[int]], target: int) -> bool:\n    if not matrix or not matrix[0]: return False\n    R, C = len(matrix), len(matrix[0])\n    lo, hi = 0, R * C - 1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        val = matrix[mid // C][mid % C]\n        if val == target: return True\n        elif val < target: lo = mid + 1\n        else: hi = mid - 1\n    return False\n",
        test_cases=[{"input": [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3], "expected": True}, {"input": [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13], "expected": False}],
        hints=["Treat the m x n matrix as a virtual 1D array of length m * n, indexing row = mid // C and col = mid % C."],
        leetcode_id=74
    ))

    # 15. Search a 2D Matrix II
    problems.append(make_problem(
        pid="bsg-m-search-2d-matrix-ii", title="Search a 2D Matrix II (Staircase Elimination)",
        wing_id="binary-search-greedy", floor=415, difficulty="medium", visualizer_type="grid",
        monster_name="Corner Wyrm", monster_title="Walker of Top-Right Saddles",
        monster_sprite="dragon", monster_color="#ec4899", monster_attack="Saddle Flare",
        monster_quote="Target found via top-right staircase reduction in O(m + n)!",
        description="Write an efficient algorithm that searches for a value `target` in an `m x n` integer matrix `matrix`. This matrix has the following properties: Integers in each row are sorted in ascending from left to right. Integers in each column are sorted in ascending from top to bottom.",
        examples=[{"input": "matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5", "output": "True"}],
        constraints=["1 <= m, n <= 300"],
        function_name="searchMatrixII",
        starter_code="def searchMatrixII(matrix: list[list[int]], target: int) -> bool:\n    pass\n",
        solution_code="def searchMatrixII(matrix: list[list[int]], target: int) -> bool:\n    if not matrix or not matrix[0]: return False\n    R, C = len(matrix), len(matrix[0])\n    r, c = 0, C - 1\n    while r < R and c >= 0:\n        if matrix[r][c] == target: return True\n        elif matrix[r][c] > target: c -= 1\n        else: r += 1\n    return False\n",
        test_cases=[{"input": [[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5], "expected": True}, {"input": [[[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20], "expected": False}],
        hints=["Start from top-right corner (0, C - 1). Move left if current > target, move down if current < target."],
        leetcode_id=240
    ))

    # 16. Find Peak Element
    problems.append(make_problem(
        pid="bsg-m-find-peak-element", title="Find Peak Element (Strict Greater Neighbor)",
        wing_id="binary-search-greedy", floor=416, difficulty="medium", visualizer_type="array",
        monster_name="Summit Titan", monster_title="Dweller on Any Local Crest",
        monster_sprite="titan", monster_color="#f59e0b", monster_attack="Ridge Tremor",
        monster_quote="Any valid local peak element index returned in O(log n)!",
        description="A peak element is an element that is strictly greater than its neighbors. Given a 0-indexed integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks. You must write an algorithm that runs in `O(log n)` time.",
        examples=[{"input": "nums = [1,2,3,1]", "output": "2"}, {"input": "nums = [1,2,1,3,5,6,4]", "output": "5"}],
        constraints=["1 <= nums.length <= 1000", "nums[i] != nums[i + 1]"],
        function_name="findPeakElement",
        starter_code="def findPeakElement(nums: list[int]) -> int:\n    pass\n",
        solution_code="def findPeakElement(nums: list[int]) -> int:\n    lo, hi = 0, len(nums) - 1\n    while lo < hi:\n        mid = (lo + hi) // 2\n        if nums[mid] < nums[mid + 1]:\n            lo = mid + 1\n        else:\n            hi = mid\n    return lo\n",
        test_cases=[{"input": [[1, 2, 3, 1]], "expected": 2}, {"input": [[1]], "expected": 0}],
        hints=["If nums[mid] < nums[mid + 1], a peak must exist on the right side. Otherwise, a peak exists on the left."],
        leetcode_id=162
    ))

    # 17. Koko Eating Bananas
    problems.append(make_problem(
        pid="bsg-m-koko-eating-bananas", title="Koko Eating Bananas (Binary Search on Answer)",
        wing_id="binary-search-greedy", floor=417, difficulty="medium", visualizer_type="array",
        monster_name="Simian Titan", monster_title="Glutton of Monotonic Speeds",
        monster_sprite="boss", monster_color="#eab308", monster_attack="Banana Barrage",
        monster_quote="Minimum integer eating speed k to finish all piles within h hours!",
        description="Koko loves to eat bananas. There are `n` piles of bananas, the `i`-th pile has `piles[i]` bananas. The guards will come back in `h` hours. Koko can decide her bananas-per-hour eating speed of `k`. Return the minimum integer `k` such that she can eat all the bananas within `h` hours.",
        examples=[{"input": "piles = [3,6,7,11], h = 8", "output": "4"}, {"input": "piles = [30,11,23,4,20], h = 5", "output": "30"}],
        constraints=["piles.length <= h <= 10^9", "1 <= piles[i] <= 10^9"],
        function_name="minEatingSpeed",
        starter_code="def minEatingSpeed(piles: list[int], h: int) -> int:\n    pass\n",
        solution_code="def minEatingSpeed(piles: list[int], h: int) -> int:\n    import math\n    lo, hi = 1, max(piles)\n    ans = hi\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        hours = sum(math.ceil(p / mid) for p in piles)\n        if hours <= h:\n            ans = mid\n            hi = mid - 1\n        else:\n            lo = mid + 1\n    return ans\n",
        test_cases=[{"input": [[3, 6, 7, 11], 8], "expected": 4}, {"input": [[30, 11, 23, 4, 20], 5], "expected": 30}, {"input": [[30, 11, 23, 4, 20], 6], "expected": 23}],
        hints=["Binary search over speed range [1, max(piles)]. Calculate ceil(pile / speed) total hours."],
        leetcode_id=875
    ))

    # 18. Capacity To Ship Packages Within D Days
    problems.append(make_problem(
        pid="bsg-m-capacity-ship-packages", title="Capacity To Ship Packages Within D Days",
        wing_id="binary-search-greedy", floor=418, difficulty="medium", visualizer_type="array",
        monster_name="Conveyor Golem", monster_title="Loader of Daily Freight Quotas",
        monster_sprite="golem", monster_color="#64748b", monster_attack="Cargo Quake",
        monster_quote="Minimum ship weight capacity to transport all packages in D days!",
        description="A conveyor belt has packages that must be shipped within `days` days. The `i`-th package on the conveyor belt has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt (in the order given by weights) without exceeding ship capacity. Return the least weight capacity of the ship.",
        examples=[{"input": "weights = [1,2,3,4,5,6,7,8,9,10], days = 5", "output": "15"}, {"input": "weights = [3,2,2,4,1,4], days = 3", "output": "6"}],
        constraints=["1 <= days <= weights.length <= 50000", "1 <= weights[i] <= 500"],
        function_name="shipWithinDays",
        starter_code="def shipWithinDays(weights: list[int], days: int) -> int:\n    pass\n",
        solution_code="def shipWithinDays(weights: list[int], days: int) -> int:\n    lo, hi = max(weights), sum(weights)\n    ans = hi\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        d_needed = 1\n        curr = 0\n        for w in weights:\n            if curr + w > mid:\n                d_needed += 1\n                curr = w\n            else:\n                curr += w\n        if d_needed <= days:\n            ans = mid\n            hi = mid - 1\n        else:\n            lo = mid + 1\n    return ans\n",
        test_cases=[{"input": [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5], "expected": 15}, {"input": [[3, 2, 2, 4, 1, 4], 3], "expected": 6}],
        hints=["Binary search bounds: lo = max(weights), hi = sum(weights). Check greedy day packing."],
        leetcode_id=1011
    ))

    # 19. Minimum Number of Days to Make m Bouquets
    problems.append(make_problem(
        pid="bsg-m-days-make-m-bouquets", title="Minimum Days to Make m Bouquets",
        wing_id="binary-search-greedy", floor=419, difficulty="medium", visualizer_type="array",
        monster_name="Floral Reaper", monster_title="Harvester of Contiguous Blooms",
        monster_sprite="wraith", monster_color="#22c55e", monster_attack="Petal Cyclone",
        monster_quote="Minimum bloom day to gather m bouquets of k adjacent flowers!",
        description="You are given an integer array `bloomDay`, an integer `m` and an integer `k`. You want to make `m` bouquets. To make a bouquet, you need to use `k` adjacent flowers from the garden. Return the minimum number of days you need to wait to be able to make `m` bouquets from the garden. If it is impossible, return `-1`.",
        examples=[{"input": "bloomDay = [1,10,3,10,2], m = 3, k = 1", "output": "3"}, {"input": "bloomDay = [1,10,3,10,2], m = 3, k = 2", "output": "-1"}],
        constraints=["1 <= bloomDay.length <= 100000", "1 <= m <= 10^6", "1 <= k <= bloomDay.length"],
        function_name="minDays",
        starter_code="def minDays(bloomDay: list[int], m: int, k: int) -> int:\n    pass\n",
        solution_code="def minDays(bloomDay: list[int], m: int, k: int) -> int:\n    if m * k > len(bloomDay): return -1\n    lo, hi = min(bloomDay), max(bloomDay)\n    ans = hi\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        bouquets = 0\n        flowers = 0\n        for day in bloomDay:\n            if day <= mid:\n                flowers += 1\n                if flowers == k:\n                    bouquets += 1\n                    flowers = 0\n            else:\n                flowers = 0\n        if bouquets >= m:\n            ans = mid\n            hi = mid - 1\n        else:\n            lo = mid + 1\n    return ans\n",
        test_cases=[{"input": [[1, 10, 3, 10, 2], 3, 1], "expected": 3}, {"input": [[1, 10, 3, 10, 2], 3, 2], "expected": -1}, {"input": [[7, 7, 7, 7, 12, 7, 7], 2, 3], "expected": 12}],
        hints=["Binary search on days in [min(bloomDay), max(bloomDay)]. Count greedily formed k-contiguous bouquets."],
        leetcode_id=1482
    ))

    # 20. Magnetic Force Between Two Balls
    problems.append(make_problem(
        pid="bsg-m-magnetic-force-balls", title="Magnetic Force Between Two Balls (Max-Min Distance)",
        wing_id="binary-search-greedy", floor=420, difficulty="medium", visualizer_type="array",
        monster_name="Repulsion Core", monster_title="Maximizer of Minimum Spacings",
        monster_sprite="spectre", monster_color="#06b6d4", monster_attack="Magnetic Repulsion",
        monster_quote="Maximum possible minimum distance among m placed balls determined!",
        description="In the universe, there are `n` baskets positioned at `position`. You have `m` balls and need to distribute them into the baskets such that the minimum magnetic force between any two balls is maximized. Return the maximum possible minimum magnetic force.",
        examples=[{"input": "position = [1,2,3,4,7], m = 3", "output": "3"}, {"input": "position = [5,4,3,2,1,1000000000], m = 2", "output": "999999999"}],
        constraints=["n == position.length", "2 <= n <= 100000", "2 <= m <= n"],
        function_name="maxDistance",
        starter_code="def maxDistance(position: list[int], m: int) -> int:\n    pass\n",
        solution_code="def maxDistance(position: list[int], m: int) -> int:\n    position.sort()\n    lo, hi = 1, position[-1] - position[0]\n    ans = 1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        count = 1\n        last = position[0]\n        for p in position[1:]:\n            if p - last >= mid:\n                count += 1\n                last = p\n        if count >= m:\n            ans = mid\n            lo = mid + 1\n        else:\n            hi = mid - 1\n    return ans\n",
        test_cases=[{"input": [[1, 2, 3, 4, 7], 3], "expected": 3}, {"input": [[5, 4, 3, 2, 1, 1000000000], 2], "expected": 999999999}],
        hints=["Sort positions. Binary search the answer distance gap, greedily placing balls."],
        leetcode_id=1552
    ))

    # 21. Jump Game
    problems.append(make_problem(
        pid="bsg-m-jump-game-reachability", title="Jump Game (Furthest Reach)",
        wing_id="binary-search-greedy", floor=421, difficulty="medium", visualizer_type="array",
        monster_name="Horizon Stalker", monster_title="Extender of the Boundary Line",
        monster_sprite="goblin", monster_color="#f59e0b", monster_attack="Leaping Blitz",
        monster_quote="Can the terminal index be reached via forward leaps?",
        description="You are given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position. Return `True` if you can reach the last index, or `False` otherwise.",
        examples=[{"input": "nums = [2,3,1,1,4]", "output": "True"}, {"input": "nums = [3,2,1,0,4]", "output": "False"}],
        constraints=["1 <= nums.length <= 10000"],
        function_name="canJump",
        starter_code="def canJump(nums: list[int]) -> bool:\n    pass\n",
        solution_code="def canJump(nums: list[int]) -> bool:\n    max_reach = 0\n    for i, jump in enumerate(nums):\n        if i > max_reach: return False\n        max_reach = max(max_reach, i + jump)\n    return True\n",
        test_cases=[{"input": [[2, 3, 1, 1, 4]], "expected": True}, {"input": [[3, 2, 1, 0, 4]], "expected": False}],
        hints=["Track max_reach. If current index i exceeds max_reach, return False."],
        leetcode_id=55
    ))

    # 22. Jump Game II
    problems.append(make_problem(
        pid="bsg-m-jump-game-ii-min-steps", title="Jump Game II (Minimum Leaps to Goal)",
        wing_id="binary-search-greedy", floor=422, difficulty="medium", visualizer_type="array",
        monster_name="Bounding Archon", monster_title="Minimizer of Striding Stages",
        monster_sprite="wraith", monster_color="#8b5cf6", monster_attack="Striding Leap",
        monster_quote="Minimum jump count to reach final array index!",
        description="You are given a 0-indexed array of integers `nums` of length `n`. You are initially positioned at `nums[0]`. Return the minimum number of jumps to reach `nums[n - 1]`.",
        examples=[{"input": "nums = [2,3,1,1,4]", "output": "2"}, {"input": "nums = [2,3,0,1,4]", "output": "2"}],
        constraints=["1 <= nums.length <= 10000"],
        function_name="jump",
        starter_code="def jump(nums: list[int]) -> int:\n    pass\n",
        solution_code="def jump(nums: list[int]) -> int:\n    n = len(nums)\n    if n <= 1: return 0\n    jumps = 0\n    curr_end = 0\n    farthest = 0\n    for i in range(n - 1):\n        farthest = max(farthest, i + nums[i])\n        if i == curr_end:\n            jumps += 1\n            curr_end = farthest\n    return jumps\n",
        test_cases=[{"input": [[2, 3, 1, 1, 4]], "expected": 2}, {"input": [[2, 3, 0, 1, 4]], "expected": 2}, {"input": [[0]], "expected": 0}],
        hints=["Greedy BFS window: advance jumps counter each time loop reaches curr_end."],
        leetcode_id=45
    ))

    # 23. Gas Station
    problems.append(make_problem(
        pid="bsg-m-gas-station-tour", title="Gas Station Circular Tour",
        wing_id="binary-search-greedy", floor=423, difficulty="medium", visualizer_type="array",
        monster_name="Fuel Warden", monster_title="Keeper of Circular Reserves",
        monster_sprite="boss", monster_color="#f97316", monster_attack="Fuel Exhaustion",
        monster_quote="Starting gas station index to complete circular tour found!",
        description="There are `n` gas stations along a circular route, where the amount of gas at the `i`-th station is `gas[i]`. Cost to travel to next station is `cost[i]`. Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return `-1`.",
        examples=[{"input": "gas = [1,2,3,4,5], cost = [3,4,5,1,2]", "output": "3"}, {"input": "gas = [2,3,4], cost = [3,4,3]", "output": "-1"}],
        constraints=["n == gas.length == cost.length", "1 <= n <= 100000"],
        function_name="canCompleteCircuit",
        starter_code="def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:\n    pass\n",
        solution_code="def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:\n    if sum(gas) < sum(cost): return -1\n    total_tank = curr_tank = 0\n    start = 0\n    for i in range(len(gas)):\n        diff = gas[i] - cost[i]\n        total_tank += diff\n        curr_tank += diff\n        if curr_tank < 0:\n            start = i + 1\n            curr_tank = 0\n    return start\n",
        test_cases=[{"input": [[1, 2, 3, 4, 5], [3, 4, 5, 1, 2]], "expected": 3}, {"input": [[2, 3, 4], [3, 4, 3]], "expected": -1}],
        hints=["If total gas < total cost, completion is impossible. Whenever running tank drops < 0, reset start to i + 1."],
        leetcode_id=134
    ))

    # 24. Task Scheduler
    problems.append(make_problem(
        pid="bsg-m-task-scheduler-cooldown", title="Task Scheduler with Cooling Intervals",
        wing_id="binary-search-greedy", floor=424, difficulty="medium", visualizer_type="array",
        monster_name="Chronos Overseer", monster_title="Enforcer of Cooling Delays",
        monster_sprite="lich", monster_color="#38bdf8", monster_attack="Cooling Stasis",
        monster_quote="Least total execution cycles under cooldown n calculated!",
        description="Given a characters array `tasks`, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle. However, there is a non-negative integer `n` that represents the cooldown period between two same tasks. Return the least number of units of times that the CPU will take to finish all the given tasks.",
        examples=[{"input": "tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 2", "output": "8"}, {"input": "tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 0", "output": "6"}],
        constraints=["1 <= tasks.length <= 10000", "0 <= n <= 100"],
        function_name="leastInterval",
        starter_code="def leastInterval(tasks: list[str], n: int) -> int:\n    pass\n",
        solution_code="def leastInterval(tasks: list[str], n: int) -> int:\n    from collections import Counter\n    counts = Counter(tasks)\n    max_freq = max(counts.values())\n    max_count = sum(1 for c in counts.values() if c == max_freq)\n    return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)\n",
        test_cases=[{"input": [["A", "A", "A", "B", "B", "B"], 2], "expected": 8}, {"input": [["A", "A", "A", "B", "B", "B"], 0], "expected": 6}, {"input": [["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2], "expected": 16}],
        hints=["Slot highest frequency task first. Formula: max(len(tasks), (max_freq - 1) * (n + 1) + count_of_max_freq)."],
        leetcode_id=621
    ))

    # 25. Non-overlapping Intervals
    problems.append(make_problem(
        pid="bsg-m-non-overlapping-intervals", title="Non-overlapping Intervals (Min Removals)",
        wing_id="binary-search-greedy", floor=425, difficulty="medium", visualizer_type="array",
        monster_name="Chrono Pruner", monster_title="Cutter of Overlapping Spans",
        monster_sprite="imp", monster_color="#ef4444", monster_attack="Interval Shear",
        monster_quote="Minimum intervals removed to make remainder mutually non-overlapping!",
        description="Given an array of intervals `intervals` where `intervals[i] = [starti, endi]`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.",
        examples=[{"input": "intervals = [[1,2],[2,3],[3,4],[1,3]]", "output": "1"}, {"input": "intervals = [[1,2],[1,2],[1,2]]", "output": "2"}],
        constraints=["1 <= intervals.length <= 100000"],
        function_name="eraseOverlapIntervals",
        starter_code="def eraseOverlapIntervals(intervals: list[list[int]]) -> int:\n    pass\n",
        solution_code="def eraseOverlapIntervals(intervals: list[list[int]]) -> int:\n    if not intervals: return 0\n    intervals.sort(key=lambda x: x[1])\n    removals = 0\n    end = intervals[0][1]\n    for i in range(1, len(intervals)):\n        if intervals[i][0] < end:\n            removals += 1\n        else:\n            end = intervals[i][1]\n    return removals\n",
        test_cases=[{"input": [[[1, 2], [2, 3], [3, 4], [1, 3]]], "expected": 1}, {"input": [[[1, 2], [1, 2], [1, 2]]], "expected": 2}, {"input": [[[1, 2], [2, 3]]], "expected": 0}],
        hints=["Sort by end time (interval scheduling). Keep greedily the interval finishing earliest."],
        leetcode_id=435
    ))

    return problems
