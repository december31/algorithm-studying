"""
Binary Search & Greedy Hard Problems - Part 1 (Floors 471 to 485 - 15 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_bs_greedy_hard_part1():
    problems = []

    # 71. Median of Two Sorted Arrays
    problems.append(make_problem(
        pid="bsg-h-median-two-sorted-arrays", title="Median of Two Sorted Arrays",
        wing_id="binary-search-greedy", floor=471, difficulty="hard", visualizer_type="array",
        monster_name="Dual Array Leviathan", monster_title="Lord of the Two Sorted Streams",
        monster_sprite="boss", monster_color="#8b5cf6", monster_attack="Median Partition",
        monster_quote="Combined median evaluated in logarithmic O(log(min(m, n))) time!",
        description="Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays. The overall run time complexity should be `O(log (m+n))`.",
        examples=[{"input": "nums1 = [1,3], nums2 = [2]", "output": "2.0"}, {"input": "nums1 = [1,2], nums2 = [3,4]", "output": "2.5"}],
        constraints=["nums1.length == m", "nums2.length == n", "0 <= m, n <= 1000"],
        function_name="findMedianSortedArrays",
        starter_code="def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:\n    pass\n",
        solution_code="def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:\n    if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1\n    m, n = len(nums1), len(nums2)\n    lo, hi = 0, m\n    half = (m + n + 1) // 2\n    while lo <= hi:\n        i = (lo + hi) // 2\n        j = half - i\n        max_left1 = float('-inf') if i == 0 else nums1[i - 1]\n        min_right1 = float('inf') if i == m else nums1[i]\n        max_left2 = float('-inf') if j == 0 else nums2[j - 1]\n        min_right2 = float('inf') if j == n else nums2[j]\n        if max_left1 <= min_right2 and max_left2 <= min_right1:\n            if (m + n) % 2 == 1:\n                return float(max(max_left1, max_left2))\n            return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0\n        elif max_left1 > min_right2:\n            hi = i - 1\n        else:\n            lo = i + 1\n    return 0.0\n",
        test_cases=[{"input": [[1, 3], [2]], "expected": 2.0}, {"input": [[1, 2], [3, 4]], "expected": 2.5}, {"input": [[], [1]], "expected": 1.0}],
        hints=["Binary search partition index i in shorter array nums1, setting j = (m + n + 1) // 2 - i."],
        leetcode_id=4
    ))

    # 72. Split Array Largest Sum
    problems.append(make_problem(
        pid="bsg-h-split-array-largest-sum", title="Split Array Largest Sum",
        wing_id="binary-search-greedy", floor=472, difficulty="hard", visualizer_type="array",
        monster_name="Bifurcation Behemoth", monster_title="Minimizer of Maximal Subarray Sums",
        monster_sprite="golem", monster_color="#ef4444", monster_attack="Subarray Crush",
        monster_quote="Minimized maximum subarray sum for k partitions found!",
        description="Given an integer array `nums` and an integer `k`, split `nums` into `k` non-empty subarrays such that the largest sum of any subarray is minimized. Return the minimized largest sum of the split.",
        examples=[{"input": "nums = [7,2,5,10,8], k = 2", "output": "18"}, {"input": "nums = [1,2,3,4,5], k = 2", "output": "9"}],
        constraints=["1 <= nums.length <= 1000", "1 <= k <= min(50, nums.length)"],
        function_name="splitArray",
        starter_code="def splitArray(nums: list[int], k: int) -> int:\n    pass\n",
        solution_code="def splitArray(nums: list[int], k: int) -> int:\n    lo, hi = max(nums), sum(nums)\n    ans = hi\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        splits = 1\n        curr = 0\n        for x in nums:\n            if curr + x > mid:\n                splits += 1\n                curr = x\n            else:\n                curr += x\n        if splits <= k:\n            ans = mid\n            hi = mid - 1\n        else:\n            lo = mid + 1\n    return ans\n",
        test_cases=[{"input": [[7, 2, 5, 10, 8], 2], "expected": 18}, {"input": [[1, 2, 3, 4, 5], 2], "expected": 9}],
        hints=["Binary search target sum in [max(nums), sum(nums)]. Greedily pack subarrays."],
        leetcode_id=410
    ))

    # 73. Russian Doll Envelopes
    problems.append(make_problem(
        pid="bsg-h-russian-doll-envelopes", title="Russian Doll Envelopes (2D LIS)",
        wing_id="binary-search-greedy", floor=473, difficulty="hard", visualizer_type="array",
        monster_name="Nesting Empress", monster_title="Embalmer of Nested Dimensions",
        monster_sprite="lich", monster_color="#ec4899", monster_attack="Nesting Seal",
        monster_quote="Maximum nesting sequence length of strictly smaller envelopes computed!",
        description="You are given a 2D array of integers `envelopes` where `envelopes[i] = [wi, hi]` represents the width and height of an envelope. One envelope can fit into another if and only if both the width and height of one envelope are strictly greater than the other envelope. Return the maximum number of envelopes you can Russian doll.",
        examples=[{"input": "envelopes = [[5,4],[6,4],[6,7],[2,3]]", "output": "3"}, {"input": "envelopes = [[1,1],[1,1],[1,1]]", "output": "1"}],
        constraints=["1 <= envelopes.length <= 100000"],
        function_name="maxEnvelopes",
        starter_code="def maxEnvelopes(envelopes: list[list[int]]) -> int:\n    pass\n",
        solution_code="def maxEnvelopes(envelopes: list[list[int]]) -> int:\n    import bisect\n    # Sort ascending by width, descending by height for ties\n    envelopes.sort(key=lambda x: (x[0], -x[1]))\n    tails = []\n    for _, h in envelopes:\n        idx = bisect.bisect_left(tails, h)\n        if idx == len(tails):\n            tails.append(h)\n        else:\n            tails[idx] = h\n    return len(tails)\n",
        test_cases=[{"input": [[[5, 4], [6, 4], [6, 7], [2, 3]]], "expected": 3}, {"input": [[[1, 1], [1, 1], [1, 1]]], "expected": 1}],
        hints=["Sort width ascending, height descending. Then compute LIS on heights using patience sorting (bisect_left)."],
        leetcode_id=354
    ))

    # 74. Patching Array
    problems.append(make_problem(
        pid="bsg-h-patching-array", title="Patching Array (Greedy Miss Doubling)",
        wing_id="binary-search-greedy", floor=474, difficulty="hard", visualizer_type="array",
        monster_name="Missing Sum Phantom", monster_title="Exploiter of Gaps in Reachable Sums",
        monster_sprite="spectre", monster_color="#f59e0b", monster_attack="Gap Fracture",
        monster_quote="Minimum numbers patched to cover all consecutive sums [1, n]!",
        description="Given a sorted integer array `nums` and an integer `n`, add/patch elements to the array such that any number in the range `[1, n]` inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.",
        examples=[{"input": "nums = [1,3], n = 6", "output": "1"}, {"input": "nums = [1,5,10], n = 20", "output": "2"}, {"input": "nums = [1,2,2], n = 5", "output": "0"}],
        constraints=["1 <= nums.length <= 1000", "1 <= n <= 2^31 - 1"],
        function_name="minPatches",
        starter_code="def minPatches(nums: list[int], n: int) -> int:\n    pass\n",
        solution_code="def minPatches(nums: list[int], n: int) -> int:\n    miss = 1\n    patches = 0\n    i = 0\n    while miss <= n:\n        if i < len(nums) and nums[i] <= miss:\n            miss += nums[i]\n            i += 1\n        else:\n            miss += miss\n            patches += 1\n    return patches\n",
        test_cases=[{"input": [[1, 3], 6], "expected": 1}, {"input": [[1, 5, 10], 20], "expected": 2}, {"input": [[1, 2, 2], 5], "expected": 0}],
        hints=["Maintain the smallest unreachable sum `miss`. If nums[i] <= miss, extend range to miss + nums[i]; otherwise patch `miss`."],
        leetcode_id=330
    ))

    # 75. Create Maximum Number
    problems.append(make_problem(
        pid="bsg-h-create-maximum-number", title="Create Maximum Number",
        wing_id="binary-search-greedy", floor=475, difficulty="hard", visualizer_type="array",
        monster_name="Greedy Synthesizer", monster_title="Extractor of Maximal Sub-digits",
        monster_sprite="demon", monster_color="#ef4444", monster_attack="Digit Extrusion",
        monster_quote="Lexicographically largest k-digit number combined from two arrays!",
        description="You are given two integer arrays `nums1` and `nums2` of lengths `m` and `n` representing digits of two numbers. You are also given an integer `k <= m + n`. Create the maximum number of length `k` from digits of the two numbers preserving relative order within each array.",
        examples=[{"input": "nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5", "output": "[9,8,6,5,3]"}],
        constraints=["1 <= k <= len(nums1) + len(nums2) <= 1000"],
        function_name="maxNumber",
        starter_code="def maxNumber(nums1: list[int], nums2: list[int], k: int) -> list[int]:\n    pass\n",
        solution_code="def maxNumber(nums1: list[int], nums2: list[int], k: int) -> list[int]:\n    def max_sub(nums, length):\n        stack = []\n        drop = len(nums) - length\n        for num in nums:\n            while drop and stack and stack[-1] < num:\n                stack.pop()\n                drop -= 1\n            stack.append(num)\n        return stack[:length]\n    def merge(s1, s2):\n        res = []\n        i = j = 0\n        while i < len(s1) or j < len(s2):\n            if s1[i:] > s2[j:]:\n                res.append(s1[i])\n                i += 1\n            else:\n                res.append(s2[j])\n                j += 1\n        return res\n    best = []\n    for len1 in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):\n        len2 = k - len1\n        s1 = max_sub(nums1, len1)\n        s2 = max_sub(nums2, len2)\n        cand = merge(s1, s2)\n        if cand > best:\n            best = cand\n    return best\n",
        test_cases=[{"input": [[3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5], "expected": [9, 8, 6, 5, 3]}, {"input": [[6, 7], [6, 0, 4], 5], "expected": [6, 7, 6, 0, 4]}],
        hints=["Iterate partition sizes (i, k - i). Use monotonic stack to extract best sub-sequence from each array and merge greedily."],
        leetcode_id=321
    ))

    # 76. Course Schedule III
    problems.append(make_problem(
        pid="bsg-h-course-schedule-iii", title="Course Schedule III (Deadline Priority Queue)",
        wing_id="binary-search-greedy", floor=476, difficulty="hard", visualizer_type="array",
        monster_name="Academic Sovereign", monster_title="Arbiter of Strict Deadlines",
        monster_sprite="wizard", monster_color="#8b5cf6", monster_attack="Deadline Enforcer",
        monster_quote="Maximum number of courses completed before individual deadlines!",
        description="There are `n` different online courses numbered from 1 to `n`. You are given an array `courses` where `courses[i] = [durationi, lastDayi]`. You start on day 1. Return the maximum number of courses that you can take.",
        examples=[{"input": "courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]", "output": "3"}, {"input": "courses = [[1,2]]", "output": "1"}],
        constraints=["1 <= courses.length <= 10000"],
        function_name="scheduleCourse",
        starter_code="def scheduleCourse(courses: list[list[int]]) -> int:\n    pass\n",
        solution_code="def scheduleCourse(courses: list[list[int]]) -> int:\n    import heapq\n    courses.sort(key=lambda x: x[1])\n    total_time = 0\n    max_heap = []\n    for dur, last_day in courses:\n        if total_time + dur <= last_day:\n            total_time += dur\n            heapq.heappush(max_heap, -dur)\n        elif max_heap and -max_heap[0] > dur:\n            total_time += dur + heapq.heappop(max_heap)\n            heapq.heappush(max_heap, -dur)\n    return len(max_heap)\n",
        test_cases=[{"input": [[[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]], "expected": 3}, {"input": [[[1, 2]]], "expected": 1}, {"input": [[[3, 2], [4, 3]]], "expected": 0}],
        hints=["Sort courses by deadline lastDay. If a course causes total_time > lastDay, swap it with the longest scheduled course if shorter."],
        leetcode_id=630
    ))

    # 77. IPO
    problems.append(make_problem(
        pid="bsg-h-ipo-capital-maximization", title="IPO Capital Maximization",
        wing_id="binary-search-greedy", floor=477, difficulty="hard", visualizer_type="array",
        monster_name="Venture Baron", monster_title="Maximizer of IPO Equity",
        monster_sprite="boss", monster_color="#f59e0b", monster_attack="Capital Shock",
        monster_quote="Capital maximized after selecting at most k feasible projects!",
        description="You have initial capital `w` and can complete at most `k` distinct projects. Given `profits` and `capital`, you can only start a project if your current capital is at least `capital[i]`. Finishing a project adds `profits[i]` to your capital. Return the maximized final capital.",
        examples=[{"input": "k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]", "output": "4"}, {"input": "k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]", "output": "6"}],
        constraints=["1 <= k <= 100000", "0 <= w <= 10^9"],
        function_name="findMaximizedCapital",
        starter_code="def findMaximizedCapital(k: int, w: int, profits: list[int], capital: list[int]) -> int:\n    pass\n",
        solution_code="def findMaximizedCapital(k: int, w: int, profits: list[int], capital: list[int]) -> int:\n    import heapq\n    projects = sorted(zip(capital, profits))\n    pq = []\n    idx = 0\n    n = len(projects)\n    for _ in range(k):\n        while idx < n and projects[idx][0] <= w:\n            heapq.heappush(pq, -projects[idx][1])\n            idx += 1\n        if not pq: break\n        w += -heapq.heappop(pq)\n    return w\n",
        test_cases=[{"input": [2, 0, [1, 2, 3], [0, 1, 1]], "expected": 4}, {"input": [3, 0, [1, 2, 3], [0, 1, 2]], "expected": 6}],
        hints=["Two heaps / sorted array + max-heap: push all projects affordable with current capital into max-heap, then take highest profit."],
        leetcode_id=502
    ))

    # 78. Minimum Number of Refueling Stops
    problems.append(make_problem(
        pid="bsg-h-min-refuel-stops", title="Minimum Number of Refueling Stops",
        wing_id="binary-search-greedy", floor=478, difficulty="hard", visualizer_type="array",
        monster_name="Wasteland Marauder", monster_title="Siphoner of Fuel Depots",
        monster_sprite="goblin", monster_color="#ef4444", monster_attack="Fuel Siphon",
        monster_quote="Minimum stops to reach target mileage without running dry!",
        description="A car travels from position 0 to `target`. It starts with `startFuel` liters of fuel. Each station `stations[i] = [positioni, fueli]`. What is the least number of refueling stops the car must make to reach its destination? If impossible, return -1.",
        examples=[{"input": "target = 1, startFuel = 1, stations = []", "output": "0"}, {"input": "target = 100, startFuel = 1, stations = [[10,100]]", "output": "-1"}, {"input": "target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]", "output": "2"}],
        constraints=["1 <= target, startFuel <= 10^9", "0 <= stations.length <= 500"],
        function_name="minRefuelStops",
        starter_code="def minRefuelStops(target: int, startFuel: int, stations: list[list[int]]) -> int:\n    pass\n",
        solution_code="def minRefuelStops(target: int, startFuel: int, stations: list[list[int]]) -> int:\n    import heapq\n    pq = []\n    curr_fuel = startFuel\n    stops = 0\n    stations.append([target, 0])\n    for pos, fuel in stations:\n        while pq and curr_fuel < pos:\n            curr_fuel += -heapq.heappop(pq)\n            stops += 1\n        if curr_fuel < pos: return -1\n        heapq.heappush(pq, -fuel)\n    return stops\n",
        test_cases=[{"input": [1, 1, []], "expected": 0}, {"input": [100, 1, [[10, 100]]], "expected": -1}, {"input": [100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]], "expected": 2}],
        hints=["Drive as far as possible. When running out of fuel before next station, retroactively take the largest fuel available from visited stations."],
        leetcode_id=871
    ))

    # 79. Strong Password Checker
    problems.append(make_problem(
        pid="bsg-h-strong-password-checker", title="Strong Password Checker (Greedy Edits)",
        wing_id="binary-search-greedy", floor=479, difficulty="hard", visualizer_type="array",
        monster_name="Cryptographic Sphinx", monster_title="Judge of Password Robustness",
        monster_sprite="sphinx", monster_color="#ec4899", monster_attack="Entropy Test",
        monster_quote="Minimum operations to satisfy length, case, digit, and repeat criteria!",
        description="Return the minimum number of steps to make a password strong: length between 6 and 20, at least 1 lowercase, 1 uppercase, 1 digit, and no three repeating characters.",
        examples=[{"input": "password = \"a\"", "output": "5"}, {"input": "password = \"aA1\"", "output": "3"}, {"input": "password = \"1337C0d3\"", "output": "0"}],
        constraints=["1 <= password.length <= 50"],
        function_name="strongPasswordChecker",
        starter_code="def strongPasswordChecker(password: str) -> int:\n    pass\n",
        solution_code="def strongPasswordChecker(password: str) -> int:\n    n = len(password)\n    has_lower = any(c.islower() for c in password)\n    has_upper = any(c.isupper() for c in password)\n    has_digit = any(c.isdigit() for c in password)\n    missing_types = (0 if has_lower else 1) + (0 if has_upper else 1) + (0 if has_digit else 1)\n    if n < 6:\n        return max(6 - n, missing_types)\n    # Count runs of length >= 3\n    repeats = []\n    i = 2\n    while i < n:\n        if password[i] == password[i - 1] == password[i - 2]:\n            length = 2\n            while i < n and password[i] == password[i - 1]:\n                length += 1\n                i += 1\n            repeats.append(length)\n        else:\n            i += 1\n    if n <= 20:\n        replace_needed = sum(k // 3 for k in repeats)\n        return max(replace_needed, missing_types)\n    # n > 20: prioritize deletions\n    delete_needed = n - 20\n    rem_delete = delete_needed\n    # Prioritize modulo 0 runs (save 1 replace with 1 delete)\n    for mod in range(3):\n        for idx in range(len(repeats)):\n            if repeats[idx] >= 3 and repeats[idx] % 3 == mod:\n                cost = mod + 1\n                if rem_delete >= cost:\n                    rem_delete -= cost\n                    repeats[idx] -= cost\n    replace_needed = sum(max(0, k // 3) for k in repeats)\n    if rem_delete > 0:\n        replace_needed -= rem_delete // 3\n    return delete_needed + max(replace_needed, missing_types)\n",
        test_cases=[{"input": ["a"], "expected": 5}, {"input": ["aA1"], "expected": 3}, {"input": ["1337C0d3"], "expected": 0}],
        hints=["Cases based on length: < 6, [6, 20], > 20. When > 20, greedily delete from runs with length % 3 == 0 first."],
        leetcode_id=420
    ))

    # 80. Set Intersection Size At Least Two
    problems.append(make_problem(
        pid="bsg-h-set-intersection-size-two", title="Set Intersection Size At Least Two",
        wing_id="binary-search-greedy", floor=480, difficulty="hard", visualizer_type="array",
        monster_name="Dual Pin Spectre", monster_title="Planter of Overlapping Interval Pins",
        monster_sprite="wraith", monster_color="#38bdf8", monster_attack="Needle Impale",
        monster_quote="Smallest set S having at least 2 intersection elements with each interval!",
        description="An integer interval `[a, b]` (with `a < b`) is a set of all integers from `a` to `b`. You are given a 2D integer array `intervals` where `intervals[i] = [starti, endi]`. Find the minimum size of a set `S` such that for every interval `[starti, endi]`, the intersection of `S` with the interval has size at least two.",
        examples=[{"input": "intervals = [[1,3],[1,4],[2,5],[3,5]]", "output": "3"}, {"input": "intervals = [[1,2],[2,3],[2,4],[4,5]]", "output": "5"}],
        constraints=["1 <= intervals.length <= 3000"],
        function_name="intersectionSizeTwo",
        starter_code="def intersectionSizeTwo(intervals: list[list[int]]) -> int:\n    pass\n",
        solution_code="def intersectionSizeTwo(intervals: list[list[int]]) -> int:\n    intervals.sort(key=lambda x: (x[1], -x[0]))\n    p1, p2 = -1, -1\n    ans = 0\n    for start, end in intervals:\n        if start > p2:\n            ans += 2\n            p1, p2 = end - 1, end\n        elif start > p1:\n            ans += 1\n            p1, p2 = p2, end\n    return ans\n",
        test_cases=[{"input": [[[1, 3], [1, 4], [2, 5], [3, 5]]], "expected": 3}, {"input": [[[1, 2], [2, 3], [2, 4], [4, 5]]], "expected": 5}],
        hints=["Sort by end coordinate ascending, start coordinate descending. Greedily place points at the end of intervals."],
        leetcode_id=757
    ))

    # 81. Super Egg Drop
    problems.append(make_problem(
        pid="bsg-h-super-egg-drop", title="Super Egg Drop (Binary Search / Inverted DP)",
        wing_id="binary-search-greedy", floor=481, difficulty="hard", visualizer_type="array",
        monster_name="Ovoid Colossus", monster_title="Tester of Critical Impact Thresholds",
        monster_sprite="golem", monster_color="#10b981", monster_attack="Egg Shell Shock",
        monster_quote="Minimum drop attempts needed to discover critical floor f with certainty!",
        description="You are given `k` identical eggs and you have access to a building with `n` floors labeled from 1 to `n`. Return the minimum number of moves that you need to determine with certainty what the value of `f` is (the highest floor from which an egg does not break).",
        examples=[{"input": "k = 1, n = 2", "output": "2"}, {"input": "k = 2, n = 6", "output": "3"}, {"input": "k = 3, n = 14", "output": "4"}],
        constraints=["1 <= k <= 100", "1 <= n <= 10000"],
        function_name="superEggDrop",
        starter_code="def superEggDrop(k: int, n: int) -> int:\n    pass\n",
        solution_code="def superEggDrop(k: int, n: int) -> int:\n    dp = [0] * (k + 1)\n    moves = 0\n    while dp[k] < n:\n        moves += 1\n        for i in range(k, 0, -1):\n            dp[i] = dp[i] + dp[i - 1] + 1\n    return moves\n",
        test_cases=[{"input": [1, 2], "expected": 2}, {"input": [2, 6], "expected": 3}, {"input": [3, 14], "expected": 4}],
        hints=["Invert the DP: dp[m][k] = maximum floors testable with m moves and k eggs. dp[m][k] = dp[m-1][k-1] + dp[m-1][k] + 1."],
        leetcode_id=887
    ))

    # 82. Preimage Size of Factorial Zeroes Function
    problems.append(make_problem(
        pid="bsg-h-preimage-factorial-zeroes", title="Preimage Size of Factorial Zeroes",
        wing_id="binary-search-greedy", floor=482, difficulty="hard", visualizer_type="array",
        monster_name="Legendre Archon", monster_title="Counter of Factorial Factors of 5",
        monster_sprite="wizard", monster_color="#06b6d4", monster_attack="Zero Multiplicity",
        monster_quote="Count of integers x whose x! ends in exactly k zeroes evaluated!",
        description="Let `f(x)` be the number of zeroes at the end of `x!`. Given `k`, find the number of non-negative integers `x` have the property that `f(x) = k`. (Note: the answer is always either 0 or 5).",
        examples=[{"input": "k = 0", "output": "5"}, {"input": "k = 5", "output": "0"}, {"input": "k = 3", "output": "5"}],
        constraints=["0 <= k <= 10^9"],
        function_name="preimageSizeFZF",
        starter_code="def preimageSizeFZF(k: int) -> int:\n    pass\n",
        solution_code="def preimageSizeFZF(k: int) -> int:\n    def trailing_zeroes(x):\n        res = 0\n        while x > 0:\n            res += x // 5\n            x //= 5\n        return res\n    lo, hi = 0, 5 * (k + 1)\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        tz = trailing_zeroes(mid)\n        if tz == k: return 5\n        elif tz < k: lo = mid + 1\n        else: hi = mid - 1\n    return 0\n",
        test_cases=[{"input": [0], "expected": 5}, {"input": [5], "expected": 0}, {"input": [3], "expected": 5}],
        hints=["Binary search for any x where trailing_zeroes(x) == k. If found, exactly 5 numbers share this count."],
        leetcode_id=793
    ))

    # 83. Minimum Cost to Hire K Workers
    problems.append(make_problem(
        pid="bsg-h-min-cost-hire-k-workers", title="Min Cost to Hire K Workers (Ratio Sort + Heap)",
        wing_id="binary-search-greedy", floor=483, difficulty="hard", visualizer_type="array",
        monster_name="Guild Treasurer", monster_title="Equator of Proportional Wages",
        monster_sprite="boss", monster_color="#eab308", monster_attack="Wage Equilibrium",
        monster_quote="Least total wage spent to hire k workers proportionally!",
        description="There are `n` workers. Given `quality` and `wage`. You want to hire exactly `k` workers. Every worker must be paid at least their minimum wage expectation and in direct proportion to their quality. Return the least amount of money needed to form a paying group satisfying these conditions.",
        examples=[{"input": "quality = [10,20,5], wage = [70,50,30], k = 2", "output": "105.0"}, {"input": "quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3", "output": "30.66667"}],
        constraints=["1 <= k <= quality.length == wage.length <= 10000"],
        function_name="mincostToHireWorkers",
        starter_code="def mincostToHireWorkers(quality: list[int], wage: list[int], k: int) -> float:\n    pass\n",
        solution_code="def mincostToHireWorkers(quality: list[int], wage: list[int], k: int) -> float:\n    import heapq\n    workers = sorted([(w / q, q) for w, q in zip(wage, quality)])\n    pq = []\n    sum_q = 0\n    min_cost = float('inf')\n    for ratio, q in workers:\n        heapq.heappush(pq, -q)\n        sum_q += q\n        if len(pq) > k:\n            sum_q += heapq.heappop(pq)\n        if len(pq) == k:\n            min_cost = min(min_cost, ratio * sum_q)\n    return round(min_cost, 5)\n",
        test_cases=[{"input": [[10, 20, 5], [70, 50, 30], 2], "expected": 105.0}, {"input": [[3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3], "expected": 30.66667}],
        hints=["Sort by wage/quality ratio. The worker with the highest ratio sets the scale; choose k workers with lowest qualities using a max-heap."],
        leetcode_id=857
    ))

    # 84. Video Stitching
    problems.append(make_problem(
        pid="bsg-h-video-stitching", title="Video Stitching (Minimum Overlapping Clips)",
        wing_id="binary-search-greedy", floor=484, difficulty="hard", visualizer_type="array",
        monster_name="Film Director Spectre", monster_title="Splicer of Continuous Reels",
        monster_sprite="spectre", monster_color="#38bdf8", monster_attack="Splice Cut",
        monster_quote="Minimum clips stitched to cover time interval [0, time]!",
        description="You are given a series of video clips from a sporting event that lasted `time` seconds. These video clips are represented as `clips` where `clips[i] = [starti, endi]`. Return the minimum number of clips needed so that we can cut the clips into a single continuous video covering `[0, time]`. If impossible, return -1.",
        examples=[{"input": "clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10", "output": "3"}, {"input": "clips = [[0,1],[1,2]], time = 5", "output": "-1"}],
        constraints=["1 <= clips.length <= 100", "1 <= time <= 100"],
        function_name="videoStitching",
        starter_code="def videoStitching(clips: list[list[int]], time: int) -> int:\n    pass\n",
        solution_code="def videoStitching(clips: list[list[int]], time: int) -> int:\n    max_reach = [0] * (time + 1)\n    for s, e in clips:\n        if s <= time:\n            max_reach[s] = max(max_reach[s], min(time, e))\n    curr_end = farthest = count = 0\n    for i in range(time):\n        farthest = max(farthest, max_reach[i])\n        if i == curr_end:\n            count += 1\n            curr_end = farthest\n            if curr_end <= i: return -1\n    return count\n",
        test_cases=[{"input": [[[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]], 10], "expected": 3}, {"input": [[[0, 1], [1, 2]], 5], "expected": -1}],
        hints=["Jump Game II greedy window logic mapped to continuous intervals."],
        leetcode_id=1024
    ))

    # 85. Jump Game IV
    problems.append(make_problem(
        pid="bsg-h-jump-game-iv-equal-teleport", title="Jump Game IV (Teleportation Purging BFS)",
        wing_id="binary-search-greedy", floor=485, difficulty="hard", visualizer_type="array",
        monster_name="Teleportation Warden", monster_title="Purger of Value Indices",
        monster_sprite="demon", monster_color="#ef4444", monster_attack="Teleport Rupture",
        monster_quote="Minimum jumps to last index utilizing equal value teleports!",
        description="Given an array of integers `arr`, you are initially at the first index of the array. In one step you can jump from index `i` to: `i + 1`, `i - 1`, or any `j` where `arr[i] == arr[j]`. Return the minimum number of steps to reach the last index of the array.",
        examples=[{"input": "arr = [100,-23,-23,404,100,23,23,23,3,404]", "output": "3"}, {"input": "arr = [7]", "output": "0"}, {"input": "arr = [7,6,9,6,9,6,9,7]", "output": "1"}],
        constraints=["1 <= arr.length <= 50000"],
        function_name="minJumps",
        starter_code="def minJumps(arr: list[int]) -> int:\n    pass\n",
        solution_code="def minJumps(arr: list[int]) -> int:\n    n = len(arr)\n    if n <= 1: return 0\n    from collections import defaultdict, deque\n    val_indices = defaultdict(list)\n    for i, x in enumerate(arr): val_indices[x].append(i)\n    q = deque([(0, 0)])\n    visited = {0}\n    while q:\n        curr, steps = q.popleft()\n        if curr == n - 1: return steps\n        # Step to neighbors\n        for nxt in (curr - 1, curr + 1):\n            if 0 <= nxt < n and nxt not in visited:\n                visited.add(nxt)\n                q.append((nxt, steps + 1))\n        # Teleport to all same values\n        if arr[curr] in val_indices:\n            for nxt in val_indices[arr[curr]]:\n                if nxt not in visited:\n                    visited.add(nxt)\n                    q.append((nxt, steps + 1))\n            del val_indices[arr[curr]]  # Greedy purge to avoid O(N^2) cycles\n    return -1\n",
        test_cases=[{"input": [[100, -23, -23, 404, 100, 23, 23, 23, 3, 404]], "expected": 3}, {"input": [[7]], "expected": 0}, {"input": [[7, 6, 9, 6, 9, 6, 9, 7]], "expected": 1}],
        hints=["Greedy index purging: once all indices for value arr[curr] have been added to the queue, delete the key from the dictionary."],
        leetcode_id=1345
    ))

    return problems
