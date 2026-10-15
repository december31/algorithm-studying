"""
Binary Search & Greedy Medium Problems - Part 2 (Floors 426 to 440 - 15 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_bs_greedy_medium_part2():
    problems = []

    # 26. Minimum Number of Arrows to Burst Balloons
    problems.append(make_problem(
        pid="bsg-m-min-arrows-burst-balloons", title="Min Arrows to Burst Balloons",
        wing_id="binary-search-greedy", floor=426, difficulty="medium", visualizer_type="array",
        monster_name="Ballistics Imp", monster_title="Piercer of Spherical Intervals",
        monster_sprite="imp", monster_color="#ef4444", monster_attack="Arrow Skewer",
        monster_quote="Minimum vertical arrow shots piercing all balloons calculated!",
        description="There are spherical balloons taped to a flat wall. The coordinates are represented by `points` where `points[i] = [xstart, xend]`. An arrow shot at x bursts all balloons satisfying `xstart <= x <= xend`. Return the minimum number of arrows that must be shot to burst all balloons.",
        examples=[{"input": "points = [[10,16],[2,8],[1,6],[7,12]]", "output": "2"}, {"input": "points = [[1,2],[3,4],[5,6],[7,8]]", "output": "4"}],
        constraints=["1 <= points.length <= 100000"],
        function_name="findMinArrowShots",
        starter_code="def findMinArrowShots(points: list[list[int]]) -> int:\n    pass\n",
        solution_code="def findMinArrowShots(points: list[list[int]]) -> int:\n    if not points: return 0\n    points.sort(key=lambda x: x[1])\n    arrows = 1\n    arrow_pos = points[0][1]\n    for i in range(1, len(points)):\n        if points[i][0] > arrow_pos:\n            arrows += 1\n            arrow_pos = points[i][1]\n    return arrows\n",
        test_cases=[{"input": [[[10, 16], [2, 8], [1, 6], [7, 12]]], "expected": 2}, {"input": [[[1, 2], [3, 4], [5, 6], [7, 8]]], "expected": 4}],
        hints=["Sort by end coordinate. Shoot arrow at end of earliest-finishing balloon."],
        leetcode_id=452
    ))

    # 27. Queue Reconstruction by Height
    problems.append(make_problem(
        pid="bsg-m-queue-reconstruction-height", title="Queue Reconstruction by Height",
        wing_id="binary-search-greedy", floor=427, difficulty="medium", visualizer_type="array",
        monster_name="Stature Archon", monster_title="Sorter of Tallness and Precedence",
        monster_sprite="wraith", monster_color="#8b5cf6", monster_attack="Height Alignment",
        monster_quote="Queue reconstructed satisfying exact [h, k] visibility criteria!",
        description="You are given an array of people `people` where `people[i] = [hi, ki]` represents the `i`-th person of height `hi` with exactly `ki` other people in front who have height greater than or equal to `hi`. Reconstruct and return the queue that is represented by the input array `people`.",
        examples=[{"input": "people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]", "output": "[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]"}],
        constraints=["1 <= people.length <= 2000"],
        function_name="reconstructQueue",
        starter_code="def reconstructQueue(people: list[list[int]]) -> list[list[int]]:\n    pass\n",
        solution_code="def reconstructQueue(people: list[list[int]]) -> list[list[int]]:\n    # Sort descending by height, ascending by k\n    people.sort(key=lambda x: (-x[0], x[1]))\n    res = []\n    for p in people:\n        res.insert(p[1], p)\n    return res\n",
        test_cases=[{"input": [[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]], "expected": [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]}],
        hints=["Sort tallest first. Shorter people inserted at index k do not disrupt taller peoples' k-counts."],
        leetcode_id=406
    ))

    # 28. Partition Labels
    problems.append(make_problem(
        pid="bsg-m-partition-labels", title="Partition Labels (Greedy Character Scope)",
        wing_id="binary-search-greedy", floor=428, difficulty="medium", visualizer_type="array",
        monster_name="Boundary Cleaver", monster_title="Divider of Disjoint Alphabet Scopes",
        monster_sprite="goblin", monster_color="#10b981", monster_attack="Scope Sever",
        monster_quote="String segmented into maximum number of parts with unique character scopes!",
        description="You are given a string `s`. We want to partition the string into as many parts as possible so that each letter appears in at most one part. Return a list of integers representing the size of these parts.",
        examples=[{"input": "s = \"ababcbacadefegdehijhklij\"", "output": "[9,7,8]"}, {"input": "s = \"eccbbbbdec\"", "output": "[10]"}],
        constraints=["1 <= s.length <= 500"],
        function_name="partitionLabels",
        starter_code="def partitionLabels(s: str) -> list[int]:\n    pass\n",
        solution_code="def partitionLabels(s: str) -> list[int]:\n    last = {c: i for i, c in enumerate(s)}\n    res = []\n    anchor = j = 0\n    for i, c in enumerate(s):\n        j = max(j, last[c])\n        if i == j:\n            res.append(i - anchor + 1)\n            anchor = i + 1\n    return res\n",
        test_cases=[{"input": ["ababcbacadefegdehijhklij"], "expected": [9, 7, 8]}, {"input": ["eccbbbbdec"], "expected": [10]}],
        hints=["Record the last occurrence of each character. Greedily extend partition boundary to max last occurrence."],
        leetcode_id=763
    ))

    # 29. Boats to Save People
    problems.append(make_problem(
        pid="bsg-m-boats-save-people", title="Boats to Save People (Two Pointer Greedy)",
        wing_id="binary-search-greedy", floor=429, difficulty="medium", visualizer_type="array",
        monster_name="Ferry Spectre", monster_title="Captain of the Underworld Pontoons",
        monster_sprite="spectre", monster_color="#38bdf8", monster_attack="Tide Escort",
        monster_quote="Minimum boats needed to ferry all passengers safely!",
        description="You are given an array `people` where `people[i]` is the weight of the `i`-th person, and an integer `limit`. Each boat can carry at most two people at the same time, provided the sum of their weight is at most `limit`. Return the minimum number of boats to carry every given person.",
        examples=[{"input": "people = [1,2], limit = 3", "output": "1"}, {"input": "people = [3,2,2,1], limit = 3", "output": "3"}, {"input": "people = [3,5,3,4], limit = 5", "output": "4"}],
        constraints=["1 <= people.length <= 50000", "people[i] <= limit <= 30000"],
        function_name="numRescueBoats",
        starter_code="def numRescueBoats(people: list[int], limit: int) -> int:\n    pass\n",
        solution_code="def numRescueBoats(people: list[int], limit: int) -> int:\n    people.sort()\n    i, j = 0, len(people) - 1\n    boats = 0\n    while i <= j:\n        if people[i] + people[j] <= limit:\n            i += 1\n        j -= 1\n        boats += 1\n    return boats\n",
        test_cases=[{"input": [[1, 2], 3], "expected": 1}, {"input": [[3, 2, 2, 1], 3], "expected": 3}, {"input": [[3, 5, 3, 4], 5], "expected": 4}],
        hints=["Sort people. Greedily pair the heaviest person with the lightest person if possible."],
        leetcode_id=881
    ))

    # 30. Advantage Shuffle
    problems.append(make_problem(
        pid="bsg-m-advantage-shuffle", title="Advantage Shuffle (Tian Ji Horse Race)",
        wing_id="binary-search-greedy", floor=430, difficulty="medium", visualizer_type="array",
        monster_name="Tournament Master", monster_title="Orchestrator of the Steed Jousts",
        monster_sprite="boss", monster_color="#eab308", monster_attack="Joust Gambit",
        monster_quote="Permutation of nums1 maximizing elements exceeding nums2 created!",
        description="You are given two integer arrays `nums1` and `nums2` both of the same length. The advantage of `nums1` with respect to `nums2` is the number of indices `i` for which `nums1[i] > nums2[i]`. Return any permutation of `nums1` that maximizes its advantage with respect to `nums2`.",
        examples=[{"input": "nums1 = [2,7,11,15], nums2 = [1,10,4,11]", "output": "[2,11,7,15]"}, {"input": "nums1 = [12,24,8,32], nums2 = [13,25,32,11]", "output": "[24,32,8,12]"}],
        constraints=["1 <= nums1.length == nums2.length <= 100000"],
        function_name="advantageCount",
        starter_code="def advantageCount(nums1: list[int], nums2: list[int]) -> list[int]:\n    pass\n",
        solution_code="def advantageCount(nums1: list[int], nums2: list[int]) -> list[int]:\n    from collections import deque\n    sorted1 = deque(sorted(nums1))\n    order2 = sorted(range(len(nums2)), key=lambda x: nums2[x])\n    res = [0] * len(nums1)\n    for idx in order2:\n        if sorted1[-1] > nums2[idx]:\n            # find smallest in sorted1 > nums2[idx]\n            for i in range(len(sorted1)):\n                if sorted1[i] > nums2[idx]:\n                    res[idx] = sorted1[i]\n                    del sorted1[i]\n                    break\n        else:\n            res[idx] = sorted1.popleft()\n    return res\n",
        test_cases=[{"input": [[2, 7, 11, 15], [1, 10, 4, 11]], "expected": [2, 11, 7, 15]}, {"input": [[12, 24, 8, 32], [13, 25, 32, 11]], "expected": [24, 32, 8, 12]}],
        hints=["Tian Ji's horse racing strategy: match smallest winning card, otherwise sacrifice smallest losing card."],
        leetcode_id=870
    ))

    # 31. Two City Scheduling
    problems.append(make_problem(
        pid="bsg-m-two-city-scheduling", title="Two City Scheduling",
        wing_id="binary-search-greedy", floor=431, difficulty="medium", visualizer_type="array",
        monster_name="Bifurcation Imp", monster_title="Dispatcher of Divided Flights",
        monster_sprite="imp", monster_color="#06b6d4", monster_attack="Fare Differential",
        monster_quote="Cost minimized sending exactly n people to City A and n to City B!",
        description="A company is planning to interview `2n` people. Given the array `costs` where `costs[i] = [aCosti, bCosti]`. Return the minimum cost to fly every person to a city such that exactly `n` people arrive in each city.",
        examples=[{"input": "costs = [[10,20],[30,200],[400,50],[30,20]]", "output": "110"}],
        constraints=["costs.length == 2 * n", "1 <= n <= 50"],
        function_name="twoCitySchedCost",
        starter_code="def twoCitySchedCost(costs: list[list[int]]) -> int:\n    pass\n",
        solution_code="def twoCitySchedCost(costs: list[list[int]]) -> int:\n    # Sort by differential: costA - costB\n    costs.sort(key=lambda x: x[0] - x[1])\n    n = len(costs) // 2\n    return sum(costs[i][0] for i in range(n)) + sum(costs[i][1] for i in range(n, 2 * n))\n",
        test_cases=[{"input": [[[10, 20], [30, 200], [400, 50], [30, 20]]], "expected": 110}],
        hints=["Sort by (aCost - bCost). First n go to city A, second n go to city B."],
        leetcode_id=1029
    ))

    # 32. Bag of Tokens
    problems.append(make_problem(
        pid="bsg-m-bag-of-tokens", title="Bag of Tokens (Power and Score Trade)",
        wing_id="binary-search-greedy", floor=432, difficulty="medium", visualizer_type="array",
        monster_name="Token Gambler", monster_title="Arbitrager of Energy and Points",
        monster_sprite="goblin", monster_color="#f59e0b", monster_attack="Token Cascade",
        monster_quote="Max score achieved by buying cheap tokens and selling expensive ones!",
        description="You have initial `power`, initial `score = 0`, and `tokens`. Face-up: spend `tokens[i]` power to gain 1 score. Face-down: spend 1 score to gain `tokens[i]` power. Return the maximum possible score you can achieve.",
        examples=[{"input": "tokens = [100], power = 50", "output": "0"}, {"input": "tokens = [100,200], power = 150", "output": "1"}, {"input": "tokens = [100,200,300,400], power = 200", "output": "2"}],
        constraints=["0 <= tokens.length <= 1000", "0 <= power <= 10000"],
        function_name="bagOfTokensScore",
        starter_code="def bagOfTokensScore(tokens: list[int], power: int) -> int:\n    pass\n",
        solution_code="def bagOfTokensScore(tokens: list[int], power: int) -> int:\n    tokens.sort()\n    i, j = 0, len(tokens) - 1\n    score = max_score = 0\n    while i <= j:\n        if power >= tokens[i]:\n            power -= tokens[i]\n            score += 1\n            i += 1\n            max_score = max(max_score, score)\n        elif score > 0:\n            power += tokens[j]\n            score -= 1\n            j -= 1\n        else:\n            break\n    return max_score\n",
        test_cases=[{"input": [[100], 50], "expected": 0}, {"input": [[100, 200], 150], "expected": 1}, {"input": [[100, 200, 300, 400], 200], "expected": 2}],
        hints=["Two pointers: buy cheapest token at i with power, sell most expensive token at j for power."],
        leetcode_id=948
    ))

    # 33. Broken Calculator
    problems.append(make_problem(
        pid="bsg-m-broken-calculator", title="Broken Calculator (Greedy Reverse Operations)",
        wing_id="binary-search-greedy", floor=433, difficulty="medium", visualizer_type="array",
        monster_name="Arithmancy Wraith", monster_title="Tinkerer with Faulty Operations",
        monster_sprite="wraith", monster_color="#ec4899", monster_attack="Parity Split",
        monster_quote="Minimum steps to reach target from startValue with (*2, -1) buttons!",
        description="There is a broken calculator that has the following two operations: Multiply the number on display by 2, or subtract 1 from the number on display. Given two integers `startValue` and `target`, return the minimum number of operations needed to display `target`.",
        examples=[{"input": "startValue = 2, target = 3", "output": "2"}, {"input": "startValue = 5, target = 8", "output": "2"}, {"input": "startValue = 3, target = 10", "output": "3"}],
        constraints=["1 <= startValue, target <= 10^9"],
        function_name="brokenCalc",
        starter_code="def brokenCalc(startValue: int, target: int) -> int:\n    pass\n",
        solution_code="def brokenCalc(startValue: int, target: int) -> int:\n    ops = 0\n    while target > startValue:\n        ops += 1\n        if target % 2 == 1: target += 1\n        else: target //= 2\n    return ops + (startValue - target)\n",
        test_cases=[{"input": [2, 3], "expected": 2}, {"input": [5, 8], "expected": 2}, {"input": [3, 10], "expected": 3}],
        hints=["Work backwards from target: if target is odd, add 1; if even, divide by 2."],
        leetcode_id=991
    ))

    # 34. Find the Duplicate Number (Binary Search on Value Range)
    problems.append(make_problem(
        pid="bsg-m-find-duplicate-number-bs", title="Find Duplicate Number (Range Bisection)",
        wing_id="binary-search-greedy", floor=434, difficulty="medium", visualizer_type="array",
        monster_name="Clone Apparition", monster_title="Harbinger of Duplicate Identities",
        monster_sprite="spectre", monster_color="#8b5cf6", monster_attack="Clone Shock",
        monster_quote="Duplicate integer in [1, n] isolated without modifying array!",
        description="Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive. There is only one repeated number in `nums`, return this repeated number without modifying the array `nums` and using only constant extra space.",
        examples=[{"input": "nums = [1,3,4,2,2]", "output": "2"}, {"input": "nums = [3,1,3,4,2]", "output": "3"}],
        constraints=["1 <= n <= 100000", "nums.length == n + 1"],
        function_name="findDuplicate",
        starter_code="def findDuplicate(nums: list[int]) -> int:\n    pass\n",
        solution_code="def findDuplicate(nums: list[int]) -> int:\n    lo, hi = 1, len(nums) - 1\n    ans = -1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        count = sum(1 for x in nums if x <= mid)\n        if count > mid:\n            ans = mid\n            hi = mid - 1\n        else:\n            lo = mid + 1\n    return ans\n",
        test_cases=[{"input": [[1, 3, 4, 2, 2]], "expected": 2}, {"input": [[3, 1, 3, 4, 2]], "expected": 3}],
        hints=["Binary search the value domain [1, n]. Count elements <= mid. If count > mid, duplicate is <= mid."],
        leetcode_id=287
    ))

    # 35. Single Element in a Sorted Array
    problems.append(make_problem(
        pid="bsg-m-single-element-sorted-array", title="Single Element in a Sorted Array",
        wing_id="binary-search-greedy", floor=435, difficulty="medium", visualizer_type="array",
        monster_name="Solitary Drake", monster_title="Unpaired Entity in Duplicated Lands",
        monster_sprite="dragon", monster_color="#38bdf8", monster_attack="Singular Beam",
        monster_quote="Single unpaired element in sorted array found in O(log n)!",
        description="You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Return the single element that appears only once in `O(log n)` time and `O(1)` space.",
        examples=[{"input": "nums = [1,1,2,3,3,4,4,8,8]", "output": "2"}, {"input": "nums = [3,3,7,7,10,11,11]", "output": "10"}],
        constraints=["1 <= nums.length <= 100000"],
        function_name="singleNonDuplicate",
        starter_code="def singleNonDuplicate(nums: list[int]) -> int:\n    pass\n",
        solution_code="def singleNonDuplicate(nums: list[int]) -> int:\n    lo, hi = 0, len(nums) - 1\n    while lo < hi:\n        mid = (lo + hi) // 2\n        if mid % 2 == 1: mid -= 1\n        if nums[mid] == nums[mid + 1]:\n            lo = mid + 2\n        else:\n            hi = mid\n    return nums[lo]\n",
        test_cases=[{"input": [[1, 1, 2, 3, 3, 4, 4, 8, 8]], "expected": 2}, {"input": [[3, 3, 7, 7, 10, 11, 11]], "expected": 10}],
        hints=["Before the single element, pairs start at even indices (mid % 2 == 0). After it, pairs start at odd indices."],
        leetcode_id=540
    ))

    # 36. Search in Rotated Sorted Array II (With Duplicates)
    problems.append(make_problem(
        pid="bsg-m-search-rotated-duplicates", title="Search in Rotated Sorted Array II (Duplicates)",
        wing_id="binary-search-greedy", floor=436, difficulty="medium", visualizer_type="array",
        monster_name="Ambiguity Fiend", monster_title="Concealer of Identical Rotated Boundaries",
        monster_sprite="imp", monster_color="#ef4444", monster_attack="Duplicate Blur",
        monster_quote="Presence of target verified amidst duplicate values!",
        description="There is an integer array `nums` sorted in non-decreasing order (not necessarily with distinct values) rotated at an unknown pivot. Given `target`, return `True` if `target` is in `nums`, or `False` if it is not in `nums`.",
        examples=[{"input": "nums = [2,5,6,0,0,1,2], target = 0", "output": "True"}, {"input": "nums = [2,5,6,0,0,1,2], target = 3", "output": "False"}],
        constraints=["1 <= nums.length <= 5000"],
        function_name="searchRotatedWithDuplicates",
        starter_code="def searchRotatedWithDuplicates(nums: list[int], target: int) -> bool:\n    pass\n",
        solution_code="def searchRotatedWithDuplicates(nums: list[int], target: int) -> bool:\n    lo, hi = 0, len(nums) - 1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        if nums[mid] == target: return True\n        if nums[lo] == nums[mid] == nums[hi]:\n            lo += 1\n            hi -= 1\n        elif nums[lo] <= nums[mid]:\n            if nums[lo] <= target < nums[mid]: hi = mid - 1\n            else: lo = mid + 1\n        else:\n            if nums[mid] < target <= nums[hi]: lo = mid + 1\n            else: hi = mid - 1\n    return False\n",
        test_cases=[{"input": [[2, 5, 6, 0, 0, 1, 2], 0], "expected": True}, {"input": [[2, 5, 6, 0, 0, 1, 2], 3], "expected": False}],
        hints=["When nums[lo] == nums[mid] == nums[hi], shrink bounds (lo += 1, hi -= 1)."],
        leetcode_id=81
    ))

    # 37. Find Minimum in Rotated Sorted Array II (With Duplicates)
    problems.append(make_problem(
        pid="bsg-m-find-min-rotated-duplicates", title="Find Minimum in Rotated Sorted Array II",
        wing_id="binary-search-greedy", floor=437, difficulty="medium", visualizer_type="array",
        monster_name="Duplicate Mirage", monster_title="Obscurer of the True Minimal Point",
        monster_sprite="spectre", monster_color="#64748b", monster_attack="Mirage Shift",
        monster_quote="True minimal element found despite plateau duplicates!",
        description="Given the sorted rotated array `nums` that may contain duplicates, return the minimum element of this array.",
        examples=[{"input": "nums = [1,3,5]", "output": "1"}, {"input": "nums = [2,2,2,0,1]", "output": "0"}],
        constraints=["n == nums.length", "1 <= n <= 5000"],
        function_name="findMinWithDuplicates",
        starter_code="def findMinWithDuplicates(nums: list[int]) -> int:\n    pass\n",
        solution_code="def findMinWithDuplicates(nums: list[int]) -> int:\n    lo, hi = 0, len(nums) - 1\n    while lo < hi:\n        mid = (lo + hi) // 2\n        if nums[mid] > nums[hi]:\n            lo = mid + 1\n        elif nums[mid] < nums[hi]:\n            hi = mid\n        else:\n            hi -= 1\n    return nums[lo]\n",
        test_cases=[{"input": [[1, 3, 5]], "expected": 1}, {"input": [[2, 2, 2, 0, 1]], "expected": 0}],
        hints=["When nums[mid] == nums[hi], safely decrement hi."],
        leetcode_id=154
    ))

    # 38. H-Index II
    problems.append(make_problem(
        pid="bsg-m-h-index-ii-sorted", title="H-Index II (Sorted Citations)",
        wing_id="binary-search-greedy", floor=438, difficulty="medium", visualizer_type="array",
        monster_name="Citation Scholar", monster_title="Measurer of Academic Impact",
        monster_sprite="wizard", monster_color="#10b981", monster_attack="Scholar Quill",
        monster_quote="H-Index computed in logarithmic time on pre-sorted citations!",
        description="Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `i`-th paper and `citations` is sorted in ascending order, return the researcher's h-index.",
        examples=[{"input": "citations = [0,1,3,5,6]", "output": "3"}, {"input": "citations = [1,2,100]", "output": "2"}],
        constraints=["1 <= citations.length <= 100000"],
        function_name="hIndex",
        starter_code="def hIndex(citations: list[int]) -> int:\n    pass\n",
        solution_code="def hIndex(citations: list[int]) -> int:\n    n = len(citations)\n    lo, hi = 0, n - 1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        if citations[mid] == n - mid:\n            return n - mid\n        elif citations[mid] < n - mid:\n            lo = mid + 1\n        else:\n            hi = mid - 1\n    return n - lo\n",
        test_cases=[{"input": [[0, 1, 3, 5, 6]], "expected": 3}, {"input": [[1, 2, 100]], "expected": 2}],
        hints=["Binary search for the index where citations[mid] >= n - mid."],
        leetcode_id=275
    ))

    # 39. Divide Two Integers
    problems.append(make_problem(
        pid="bsg-m-divide-two-integers-doubling", title="Divide Two Integers (Bit Shift Doubling)",
        wing_id="binary-search-greedy", floor=439, difficulty="medium", visualizer_type="array",
        monster_name="Quotient Colossus", monster_title="Subtractor of Exponential Powers",
        monster_sprite="golem", monster_color="#f59e0b", monster_attack="Bit Shift Quake",
        monster_quote="Integer quotient computed without multiplication, division, or modulo!",
        description="Given two integers `dividend` and `divisor`, divide two integers without using multiplication, division, and mod operator. Return the quotient after dividing dividend by divisor. Clamp within `[-2^31, 2^31 - 1]`.",
        examples=[{"input": "dividend = 10, divisor = 3", "output": "3"}, {"input": "dividend = 7, divisor = -3", "output": "-2"}],
        constraints=["-2^31 <= dividend, divisor <= 2^31 - 1", "divisor != 0"],
        function_name="divide",
        starter_code="def divide(dividend: int, divisor: int) -> int:\n    pass\n",
        solution_code="def divide(dividend: int, divisor: int) -> int:\n    if dividend == -2**31 and divisor == -1: return 2**31 - 1\n    sign = 1 if (dividend > 0) == (divisor > 0) else -1\n    a, b = abs(dividend), abs(divisor)\n    ans = 0\n    while a >= b:\n        temp, multiple = b, 1\n        while a >= (temp << 1):\n            temp <<= 1\n            multiple <<= 1\n        a -= temp\n        ans += multiple\n    return sign * ans\n",
        test_cases=[{"input": [10, 3], "expected": 3}, {"input": [7, -3], "expected": -2}],
        hints=["Repeatedly double the divisor using bit shifts until it exceeds dividend, then subtract."],
        leetcode_id=29
    ))

    # 40. Find K Closest Elements
    problems.append(make_problem(
        pid="bsg-m-find-k-closest-elements", title="Find K Closest Elements",
        wing_id="binary-search-greedy", floor=440, difficulty="medium", visualizer_type="array",
        monster_name="Proximity Shade", monster_title="Gatherer of Nearest Numbers",
        monster_sprite="wraith", monster_color="#38bdf8", monster_attack="Proximity Bind",
        monster_quote="K closest sorted elements to target x isolated!",
        description="Given a sorted integer array `arr`, two integers `k` and `x`, return the `k` closest integers to `x` in the array. The result should also be sorted in ascending order.",
        examples=[{"input": "arr = [1,2,3,4,5], k = 4, x = 3", "output": "[1,2,3,4]"}, {"input": "arr = [1,2,3,4,5], k = 4, x = -1", "output": "[1,2,3,4]"}],
        constraints=["1 <= k <= arr.length <= 10000"],
        function_name="findClosestElements",
        starter_code="def findClosestElements(arr: list[int], k: int, x: int) -> list[int]:\n    pass\n",
        solution_code="def findClosestElements(arr: list[int], k: int, x: int) -> list[int]:\n    lo, hi = 0, len(arr) - k\n    while lo < hi:\n        mid = (lo + hi) // 2\n        if x - arr[mid] > arr[mid + k] - x:\n            lo = mid + 1\n        else:\n            hi = mid\n    return arr[lo:lo + k]\n",
        test_cases=[{"input": [[1, 2, 3, 4, 5], 4, 3], "expected": [1, 2, 3, 4]}, {"input": [[1, 2, 3, 4, 5], 4, -1], "expected": [1, 2, 3, 4]}],
        hints=["Binary search for the starting index lo of the k-length window."],
        leetcode_id=658
    ))

    return problems
