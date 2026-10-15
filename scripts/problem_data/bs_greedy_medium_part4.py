"""
Binary Search & Greedy Medium Problems - Part 4 (Floors 456 to 470 - 15 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_bs_greedy_medium_part4():
    problems = []

    # 56. Maximum Split of Positive Even Integers
    problems.append(make_problem(
        pid="bsg-m-max-split-even-integers", title="Max Split of Positive Even Integers",
        wing_id="binary-search-greedy", floor=456, difficulty="medium", visualizer_type="array",
        monster_name="Even Splitting Fiend", monster_title="Divider into Distinct Even Addends",
        monster_sprite="imp", monster_color="#ef4444", monster_attack="Even Fracture",
        monster_quote="FinalSum decomposed into maximum count of unique even integers!",
        description="You are given an integer `finalSum`. Split it into a sum of a maximum number of unique positive even integers. Return a list of integers that represent a valid split, or `[]` if impossible.",
        examples=[{"input": "finalSum = 12", "output": "[2,4,6]"}, {"input": "finalSum = 7", "output": "[]"}],
        constraints=["1 <= finalSum <= 10^10"],
        function_name="maximumEvenSplit",
        starter_code="def maximumEvenSplit(finalSum: int) -> list[int]:\n    pass\n",
        solution_code="def maximumEvenSplit(finalSum: int) -> list[int]:\n    if finalSum % 2 == 1: return []\n    res = []\n    curr = 2\n    while finalSum >= curr:\n        res.append(curr)\n        finalSum -= curr\n        curr += 2\n    res[-1] += finalSum\n    return res\n",
        test_cases=[{"input": [12], "expected": [2, 4, 6]}, {"input": [7], "expected": []}, {"input": [28], "expected": [2, 4, 6, 16]}],
        hints=["Greedily take smallest even numbers 2, 4, 6, ... and add remaining surplus to the last number."],
        leetcode_id=2178
    ))

    # 57. Minimum Swaps to Make Strings Equal
    problems.append(make_problem(
        pid="bsg-m-min-swaps-strings-equal", title="Min Swaps to Make Strings Equal (x and y)",
        wing_id="binary-search-greedy", floor=457, difficulty="medium", visualizer_type="array",
        monster_name="Inversion Wraith", monster_title="Swapper of Asymmetric Pairs",
        monster_sprite="wraith", monster_color="#38bdf8", monster_attack="Swap Shock",
        monster_quote="Minimum swaps between s1 and s2 to make both equal!",
        description="You are given two strings `s1` and `s2` of equal length consisting of letters `'x'` and `'y'` only. Your task is to make these two strings equal to each other using minimum swaps. Return the minimum number of swaps, or -1 if impossible.",
        examples=[{"input": "s1 = \"xx\", s2 = \"yy\"", "output": "1"}, {"input": "s1 = \"xy\", s2 = \"yx\"", "output": "2"}, {"input": "s1 = \"xx\", s2 = \"xy\"", "output": "-1"}],
        constraints=["1 <= s1.length == s2.length <= 1000"],
        function_name="minimumSwap",
        starter_code="def minimumSwap(s1: str, s2: str) -> int:\n    pass\n",
        solution_code="def minimumSwap(s1: str, s2: str) -> int:\n    xy = yx = 0\n    for c1, c2 in zip(s1, s2):\n        if c1 == 'x' and c2 == 'y': xy += 1\n        elif c1 == 'y' and c2 == 'x': yx += 1\n    if (xy + yx) % 2 == 1: return -1\n    return xy // 2 + yx // 2 + (2 if xy % 2 == 1 else 0)\n",
        test_cases=[{"input": ["xx", "yy"], "expected": 1}, {"input": ["xy", "yx"], "expected": 2}, {"input": ["xx", "xy"], "expected": -1}],
        hints=["Two ('x','y') pairs resolve in 1 swap. One ('x','y') and one ('y','x') pair resolve in 2 swaps."],
        leetcode_id=1247
    ))

    # 58. Minimum Add to Make Parentheses Valid
    problems.append(make_problem(
        pid="bsg-m-min-add-parentheses-valid", title="Min Add to Make Parentheses Valid",
        wing_id="binary-search-greedy", floor=458, difficulty="medium", visualizer_type="stack",
        monster_name="Balance Sylph", monster_title="Weaver of Missing Brackets",
        monster_sprite="spectre", monster_color="#10b981", monster_attack="Parenthesis Bind",
        monster_quote="Minimum number of '(' or ')' added to make string balanced!",
        description="A parentheses string is valid if and only if it is the empty string, can be written as AB, or can be written as (A). Given a parentheses string `s`, return the minimum number of parentheses we must add to make the resulting string valid.",
        examples=[{"input": "s = \"())\"", "output": "1"}, {"input": "s = \"(((\"", "output": "3"}],
        constraints=["1 <= s.length <= 1000"],
        function_name="minAddToMakeValid",
        starter_code="def minAddToMakeValid(s: str) -> int:\n    pass\n",
        solution_code="def minAddToMakeValid(s: str) -> int:\n    open_needed = 0\n    close_needed = 0\n    for ch in s:\n        if ch == '(': close_needed += 1\n        elif ch == ')':\n            if close_needed > 0: close_needed -= 1\n            else: open_needed += 1\n    return open_needed + close_needed\n",
        test_cases=[{"input": ["())"], "expected": 1}, {"input": ["((("], "expected": 3}, {"input": ["()"], "expected": 0}],
        hints=["Track unmatched closing parentheses and unmatched opening parentheses."],
        leetcode_id=921
    ))

    # 59. Minimum Cost to Move Chips to The Same Position
    problems.append(make_problem(
        pid="bsg-m-min-cost-move-chips", title="Move Chips to Same Position (Parity Counting)",
        wing_id="binary-search-greedy", floor=459, difficulty="medium", visualizer_type="array",
        monster_name="Parity Goblin", monster_title="Mover of 2-Step Free Chips",
        monster_sprite="goblin", monster_color="#f59e0b", monster_attack="Parity Slap",
        monster_quote="Least coin cost to move all chips to a single position!",
        description="We have `n` chips. Moving chip from `position[i]` to `position[i] + 2` or `position[i] - 2` costs 0. Moving 1 step costs 1. Return the minimum cost needed to move all chips to the same position.",
        examples=[{"input": "position = [1,2,3]", "output": "1"}, {"input": "position = [2,2,2,3,3]", "output": "2"}],
        constraints=["1 <= position.length <= 100"],
        function_name="minCostToMoveChips",
        starter_code="def minCostToMoveChips(position: list[int]) -> int:\n    pass\n",
        solution_code="def minCostToMoveChips(position: list[int]) -> int:\n    odd = sum(1 for p in position if p % 2 == 1)\n    even = len(position) - odd\n    return min(odd, even)\n",
        test_cases=[{"input": [[1, 2, 3]], "expected": 1}, {"input": [[2, 2, 2, 3, 3]], "expected": 2}, {"input": [[1, 1000000000]], "expected": 1}],
        hints=["Moving between same parities is free. The answer is min(count(even), count(odd))."],
        leetcode_id=1217
    ))

    # 60. Wiggle Subsequence
    problems.append(make_problem(
        pid="bsg-m-wiggle-subsequence-greedy", title="Wiggle Subsequence (Greedy Alternation)",
        wing_id="binary-search-greedy", floor=460, difficulty="medium", visualizer_type="array",
        monster_name="Oscillation Drake", monster_title="Rider of Peak and Valley Waves",
        monster_sprite="dragon", monster_color="#8b5cf6", monster_attack="Wiggle Ripple",
        monster_quote="Longest alternating differences subsequence length found!",
        description="A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. Given an integer array `nums`, return the length of the longest wiggle subsequence of `nums`.",
        examples=[{"input": "nums = [1,7,4,9,2,5]", "output": "6"}, {"input": "nums = [1,17,5,10,13,15,10,5,16,8]", "output": "7"}],
        constraints=["1 <= nums.length <= 1000"],
        function_name="wiggleMaxLength",
        starter_code="def wiggleMaxLength(nums: list[int]) -> int:\n    pass\n",
        solution_code="def wiggleMaxLength(nums: list[int]) -> int:\n    if len(nums) < 2: return len(nums)\n    up = down = 1\n    for i in range(1, len(nums)):\n        if nums[i] > nums[i - 1]: up = down + 1\n        elif nums[i] < nums[i - 1]: down = up + 1\n    return max(up, down)\n",
        test_cases=[{"input": [[1, 7, 4, 9, 2, 5]], "expected": 6}, {"input": [[1, 17, 5, 10, 13, 15, 10, 5, 16, 8]], "expected": 7}, {"input": [[1, 2, 3, 4, 5, 6, 7, 8, 9]], "expected": 2}],
        hints=["Maintain two states: up (last move was up) and down (last move was down)."],
        leetcode_id=376
    ))

    # 61. Monotone Increasing Digits
    problems.append(make_problem(
        pid="bsg-m-monotone-increasing-digits", title="Monotone Increasing Digits",
        wing_id="binary-search-greedy", floor=461, difficulty="medium", visualizer_type="array",
        monster_name="Ascendant Sphinx", monster_title="Pruner of Monotonic Decimals",
        monster_sprite="sphinx", monster_color="#f59e0b", monster_attack="Nines Cascade",
        monster_quote="Largest integer <= n with non-decreasing digits produced!",
        description="An integer has monotone increasing digits if and only if each pair of adjacent digits `x` and `y` satisfy `x <= y`. Given an integer `n`, return the largest number that is less than or equal to `n` with monotone increasing digits.",
        examples=[{"input": "n = 10", "output": "9"}, {"input": "n = 1234", "output": "1234"}, {"input": "n = 332", "output": "299"}],
        constraints=["0 <= n <= 10^9"],
        function_name="monotoneIncreasingDigits",
        starter_code="def monotoneIncreasingDigits(n: int) -> int:\n    pass\n",
        solution_code="def monotoneIncreasingDigits(n: int) -> int:\n    digits = list(str(n))\n    mark = len(digits)\n    for i in range(len(digits) - 1, 0, -1):\n        if digits[i - 1] > digits[i]:\n            digits[i - 1] = str(int(digits[i - 1]) - 1)\n            mark = i\n    for i in range(mark, len(digits)):\n        digits[i] = '9'\n    return int(\"\".join(digits))\n",
        test_cases=[{"input": [10], "expected": 9}, {"input": [1234], "expected": 1234}, {"input": [332], "expected": 299}],
        hints=["Scan right to left: if digits[i-1] > digits[i], decrement digits[i-1] and fill subsequent digits with '9'."],
        leetcode_id=738
    ))

    # 62. Minimum Cost Homecoming of a Robot in a Grid
    problems.append(make_problem(
        pid="bsg-m-robot-homecoming-cost", title="Minimum Cost Homecoming of Robot",
        wing_id="binary-search-greedy", floor=462, difficulty="medium", visualizer_type="grid",
        monster_name="Pathway Sentinel", monster_title="Surveyor of Coordinate Tolls",
        monster_sprite="gargoyle", monster_color="#06b6d4", monster_attack="Toll Gate",
        monster_quote="Cost independent of path geometry computed along monotonic axis lines!",
        description="A robot starts at `startPos = [startRow, startCol]` and must reach `homePos = [homeRow, homeCol]`. Traveling into row r costs `rowCosts[r]`, into col c costs `colCosts[c]`. Return the minimum cost to reach home.",
        examples=[{"input": "startPos = [1,0], homePos = [2,3], rowCosts = [5,4,3], colCosts = [8,2,6,7]", "output": "18"}],
        constraints=["1 <= rowCosts.length, colCosts.length <= 100000"],
        function_name="minCost",
        starter_code="def minCost(startPos: list[int], homePos: list[int], rowCosts: list[int], colCosts: list[int]) -> int:\n    pass\n",
        solution_code="def minCost(startPos: list[int], homePos: list[int], rowCosts: list[int], colCosts: list[int]) -> int:\n    r1, c1 = startPos\n    r2, c2 = homePos\n    ans = 0\n    step_r = 1 if r2 >= r1 else -1\n    for r in range(r1 + step_r, r2 + step_r, step_r):\n        ans += rowCosts[r]\n    step_c = 1 if c2 >= c1 else -1\n    for c in range(c1 + step_c, c2 + step_c, step_c):\n        ans += colCosts[c]\n    return ans\n",
        test_cases=[{"input": [[1, 0], [2, 3], [5, 4, 3], [8, 2, 6, 7]], "expected": 18}, {"input": [[0, 0], [0, 0], [5], [5]], "expected": 0}],
        hints=["Because costs are non-negative, any monotonic Manhattan path pays exactly for every intermediate row and column."],
        leetcode_id=2087
    ))

    # 63. Find K-th Smallest Pair Distance
    problems.append(make_problem(
        pid="bsg-m-kth-smallest-pair-distance", title="K-th Smallest Pair Distance (Two Pointer BS)",
        wing_id="binary-search-greedy", floor=463, difficulty="medium", visualizer_type="array",
        monster_name="Metric Behemoth", monster_title="Measurer of Absolute Distances",
        monster_sprite="boss", monster_color="#ef4444", monster_attack="Distance Compression",
        monster_quote="The k-th absolute difference pair |nums[i] - nums[j]| located!",
        description="The distance of a pair of integers `a` and `b` is defined as the absolute difference `|a - b|`. Given an integer array `nums` and an integer `k`, return the `k`-th smallest distance among all the pairs `nums[i]` and `nums[j]` where `0 <= i < j < nums.length`.",
        examples=[{"input": "nums = [1,3,1], k = 1", "output": "0"}, {"input": "nums = [1,1,1], k = 2", "output": "0"}, {"input": "nums = [1,6,1], k = 3", "output": "5"}],
        constraints=["n == nums.length", "2 <= n <= 10000", "1 <= k <= n * (n - 1) // 2"],
        function_name="smallestDistancePair",
        starter_code="def smallestDistancePair(nums: list[int], k: int) -> int:\n    pass\n",
        solution_code="def smallestDistancePair(nums: list[int], k: int) -> int:\n    nums.sort()\n    lo, hi = 0, nums[-1] - nums[0]\n    def count_pairs(diff):\n        count = 0\n        left = 0\n        for right in range(len(nums)):\n            while nums[right] - nums[left] > diff:\n                left += 1\n            count += right - left\n        return count\n    while lo < hi:\n        mid = (lo + hi) // 2\n        if count_pairs(mid) < k:\n            lo = mid + 1\n        else:\n            hi = mid\n    return lo\n",
        test_cases=[{"input": [[1, 3, 1], 1], "expected": 0}, {"input": [[1, 1, 1], 2], "expected": 0}, {"input": [[1, 6, 1], 3], "expected": 5}],
        hints=["Sort nums. Binary search the distance diff, counting pairs with diff <= mid in O(n) using a sliding window."],
        leetcode_id=719
    ))

    # 64. Minimum Operations to Reduce X to Zero
    problems.append(make_problem(
        pid="bsg-m-reduce-x-to-zero", title="Min Operations to Reduce X to Zero (Target Subarray)",
        wing_id="binary-search-greedy", floor=464, difficulty="medium", visualizer_type="array",
        monster_name="Erosion Fiend", monster_title="Subtractor of Left and Right Flanks",
        monster_sprite="demon", monster_color="#38bdf8", monster_attack="Flank Drain",
        monster_quote="Minimum flank elements removed summing exactly to x!",
        description="You are given an integer array `nums` and an integer `x`. In one operation, you can remove either the leftmost or the rightmost element and subtract its value from `x`. Return the minimum number of operations to reduce `x` to exactly 0, or `-1` if impossible.",
        examples=[{"input": "nums = [1,1,4,2,3], x = 5", "output": "2"}, {"input": "nums = [5,6,7,8,9], x = 4", "output": "-1"}, {"input": "nums = [3,2,20,1,1,3], x = 10", "output": "5"}],
        constraints=["1 <= nums.length <= 100000"],
        function_name="minOperations",
        starter_code="def minOperations(nums: list[int], x: int) -> int:\n    pass\n",
        solution_code="def minOperations(nums: list[int], x: int) -> int:\n    target = sum(nums) - x\n    if target < 0: return -1\n    if target == 0: return len(nums)\n    max_len = -1\n    curr = left = 0\n    for right, val in enumerate(nums):\n        curr += val\n        while curr > target and left <= right:\n            curr -= nums[left]\n            left += 1\n        if curr == target:\n            max_len = max(max_len, right - left + 1)\n    return len(nums) - max_len if max_len != -1 else -1\n",
        test_cases=[{"input": [[1, 1, 4, 2, 3], 5], "expected": 2}, {"input": [[5, 6, 7, 8, 9], 4], "expected": -1}, {"input": [[3, 2, 20, 1, 1, 3], 10], "expected": 5}],
        hints=["Equivalent to finding the longest contiguous subarray with sum == sum(nums) - x."],
        leetcode_id=1658
    ))

    # 65. Furthest Building You Can Reach
    problems.append(make_problem(
        pid="bsg-m-furthest-building-reach", title="Furthest Building You Can Reach",
        wing_id="binary-search-greedy", floor=465, difficulty="medium", visualizer_type="array",
        monster_name="Rooftop Behemoth", monster_title="Hopper of Urban Skylines",
        monster_sprite="titan", monster_color="#8b5cf6", monster_attack="Skyline Slam",
        monster_quote="Furthest building reached greedily saving ladders for largest climbs!",
        description="You are given an integer array `heights` representing heights of buildings, some `bricks`, and some `ladders`. To move from building `i` to `i+1`: if height diff `h[i+1] - h[i] <= 0`, no resource is used. Otherwise, you can use 1 ladder or `h[i+1] - h[i]` bricks. Return the furthest building index you can reach.",
        examples=[{"input": "heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1", "output": "4"}],
        constraints=["1 <= heights.length <= 100000"],
        function_name="furthestBuilding",
        starter_code="def furthestBuilding(heights: list[int], bricks: int, ladders: int) -> int:\n    pass\n",
        solution_code="def furthestBuilding(heights: list[int], bricks: int, ladders: int) -> int:\n    import heapq\n    pq = []\n    for i in range(len(heights) - 1):\n        diff = heights[i + 1] - heights[i]\n        if diff > 0:\n            heapq.heappush(pq, diff)\n            if len(pq) > ladders:\n                bricks -= heapq.heappop(pq)\n                if bricks < 0:\n                    return i\n    return len(heights) - 1\n",
        test_cases=[{"input": [[4, 2, 7, 6, 9, 14, 12], 5, 1], "expected": 4}, {"input": [[4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2], "expected": 7}],
        hints=["Use a min-heap to allocate ladders to the largest height jumps. Use bricks on the remaining jumps."],
        leetcode_id=1642
    ))

    # 66. Reorganize String
    problems.append(make_problem(
        pid="bsg-m-reorganize-string-no-adjacent", title="Reorganize String with No Adjacent Duplicates",
        wing_id="binary-search-greedy", floor=466, difficulty="medium", visualizer_type="array",
        monster_name="Entropy Drake", monster_title="Separator of Adjacent Monograms",
        monster_sprite="dragon", monster_color="#ec4899", monster_attack="Discord Breath",
        monster_quote="String rearranged so no two adjacent letters match!",
        description="Given a string `s`, rearrange the characters of `s` so that any two adjacent characters are not the same. Return any possible rearrangement of `s` or `\"\"` if not possible.",
        examples=[{"input": "s = \"aab\"", "output": "\"aba\""}, {"input": "s = \"aaab\"", "output": "\"\""}],
        constraints=["1 <= s.length <= 500"],
        function_name="reorganizeString",
        starter_code="def reorganizeString(s: str) -> str:\n    pass\n",
        solution_code="def reorganizeString(s: str) -> str:\n    from collections import Counter\n    import heapq\n    counts = Counter(s)\n    if max(counts.values()) > (len(s) + 1) // 2: return \"\"\n    pq = [(-cnt, ch) for ch, cnt in counts.items()]\n    heapq.heapify(pq)\n    res = []\n    prev_cnt, prev_ch = 0, ''\n    while pq:\n        cnt, ch = heapq.heappop(pq)\n        res.append(ch)\n        if prev_cnt < 0:\n            heapq.heappush(pq, (prev_cnt, prev_ch))\n        prev_cnt, prev_ch = cnt + 1, ch\n    return \"\".join(res)\n",
        test_cases=[{"input": ["aab"], "expected": "aba"}, {"input": ["aaab"], "expected": ""}],
        hints=["Max-heap by letter frequency. Always pull the most frequent letter that is not equal to the previous character."],
        leetcode_id=767
    ))

    # 67. Previous Permutation With One Swap
    problems.append(make_problem(
        pid="bsg-m-previous-permutation-one-swap", title="Previous Permutation With One Swap",
        wing_id="binary-search-greedy", floor=467, difficulty="medium", visualizer_type="array",
        monster_name="Permutation Spectre", monster_title="Reverser of Single Inversions",
        monster_sprite="spectre", monster_color="#10b981", monster_attack="Swap Inversion",
        monster_quote="Largest lexicographically smaller array with 1 swap created!",
        description="Given an array of positive integers `arr`, return the lexicographically largest permutation that is smaller than `arr`, that can be made with exactly one swap. If no such permutation exists, return `arr`.",
        examples=[{"input": "arr = [3,2,1]", "output": "[3,1,2]"}, {"input": "arr = [1,1,5]", "output": "[1,1,5]"}, {"input": "arr = [1,9,4,6,7]", "output": "[1,7,4,6,9]"}],
        constraints=["1 <= arr.length <= 10000"],
        function_name="prevPermOpt1",
        starter_code="def prevPermOpt1(arr: list[int]) -> list[int]:\n    pass\n",
        solution_code="def prevPermOpt1(arr: list[int]) -> list[int]:\n    n = len(arr)\n    idx = -1\n    for i in range(n - 2, -1, -1):\n        if arr[i] > arr[i + 1]:\n            idx = i\n            break\n    if idx == -1: return arr\n    # Find largest arr[j] < arr[idx] to the right (smallest index for ties)\n    best_j = idx + 1\n    for j in range(idx + 1, n):\n        if arr[j] < arr[idx] and arr[j] > arr[best_j]:\n            best_j = j\n    arr[idx], arr[best_j] = arr[best_j], arr[idx]\n    return arr\n",
        test_cases=[{"input": [[3, 2, 1]], "expected": [3, 1, 2]}, {"input": [[1, 1, 5]], "expected": [1, 1, 5]}, {"input": [[1, 9, 4, 6, 7]], "expected": [1, 7, 4, 6, 9]}],
        hints=["Find first drop arr[i] > arr[i+1] from right. Swap with largest element to the right that is strictly smaller than arr[i]."],
        leetcode_id=1053
    ))

    # 68. Longest Happy String
    problems.append(make_problem(
        pid="bsg-m-longest-happy-string", title="Longest Happy String (Greedy Trigram Avoidance)",
        wing_id="binary-search-greedy", floor=468, difficulty="medium", visualizer_type="array",
        monster_name="Trigram Sphinx", monster_title="Banisher of Triple Character Repeats",
        monster_sprite="sphinx", monster_color="#f59e0b", monster_attack="Trigram Ward",
        monster_quote="Longest valid string containing no 'aaa', 'bbb', or 'ccc' built!",
        description="A string `s` is called happy if it contains only 'a', 'b', 'c' and does not contain \"aaa\", \"bbb\", or \"ccc\". Given integers `a`, `b`, and `c`, return the longest possible happy string.",
        examples=[{"input": "a = 1, b = 1, c = 7", "output": "\"ccaccbcc\""}, {"input": "a = 7, b = 1, c = 0", "output": "\"aabaa\""}],
        constraints=["0 <= a, b, c <= 100"],
        function_name="longestDiverseString",
        starter_code="def longestDiverseString(a: int, b: int, c: int) -> str:\n    pass\n",
        solution_code="def longestDiverseString(a: int, b: int, c: int) -> str:\n    import heapq\n    pq = []\n    for cnt, ch in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:\n        if cnt < 0: heapq.heappush(pq, (cnt, ch))\n    res = []\n    while pq:\n        cnt1, ch1 = heapq.heappop(pq)\n        if len(res) >= 2 and res[-1] == res[-2] == ch1:\n            if not pq: break\n            cnt2, ch2 = heapq.heappop(pq)\n            res.append(ch2)\n            cnt2 += 1\n            if cnt2 < 0: heapq.heappush(pq, (cnt2, ch2))\n            heapq.heappush(pq, (cnt1, ch1))\n        else:\n            res.append(ch1)\n            cnt1 += 1\n            if cnt1 < 0: heapq.heappush(pq, (cnt1, ch1))\n    return \"\".join(res)\n",
        test_cases=[{"input": [1, 1, 7], "expected": "ccaccbcc"}, {"input": [7, 1, 0], "expected": "aabaa"}],
        hints=["Greedily pick the character with highest remaining count unless it would form three identical consecutive characters."],
        leetcode_id=1405
    ))

    # 69. Candy Distribution
    problems.append(make_problem(
        pid="bsg-m-candy-distribution", title="Candy Distribution (Two-Pass Greedy)",
        wing_id="binary-search-greedy", floor=469, difficulty="medium", visualizer_type="array",
        monster_name="Confection Arbiter", monster_title="Weigher of Relative Merit",
        monster_sprite="lich", monster_color="#ef4444", monster_attack="Sweet Mandate",
        monster_quote="Minimum candies distributed satisfying neighbor rating differentials!",
        description="There are `n` children standing in a line, each assigned a rating. Each child must have at least one candy. Children with a higher rating get more candies than their neighbors. Return the minimum number of candies you need to distribute.",
        examples=[{"input": "ratings = [1,0,2]", "output": "5"}, {"input": "ratings = [1,2,2]", "output": "4"}],
        constraints=["n == ratings.length", "1 <= n <= 20000"],
        function_name="candy",
        starter_code="def candy(ratings: list[int]) -> int:\n    pass\n",
        solution_code="def candy(ratings: list[int]) -> int:\n    n = len(ratings)\n    candies = [1] * n\n    for i in range(1, n):\n        if ratings[i] > ratings[i - 1]:\n            candies[i] = candies[i - 1] + 1\n    for i in range(n - 2, -1, -1):\n        if ratings[i] > ratings[i + 1]:\n            candies[i] = max(candies[i], candies[i + 1] + 1)\n    return sum(candies)\n",
        test_cases=[{"input": [[1, 0, 2]], "expected": 5}, {"input": [[1, 2, 2]], "expected": 4}],
        hints=["Two passes: left-to-right to enforce rightward increases, right-to-left to enforce leftward increases."],
        leetcode_id=135
    ))

    # 70. Maximum Frequency Stack / Greedy Peak Capacity
    problems.append(make_problem(
        pid="bsg-m-car-pooling-capacity", title="Car Pooling (Greedy Capacity Sweep)",
        wing_id="binary-search-greedy", floor=470, difficulty="medium", visualizer_type="array",
        monster_name="Chariot Overseer", monster_title="Inspector of Passenger Overload",
        monster_sprite="boss", monster_color="#38bdf8", monster_attack="Chariot Trample",
        monster_quote="Is car capacity never exceeded across all passenger trips?",
        description="There is a car with `capacity` empty seats. Given `trips` where `trips[i] = [numPassengersi, fromi, toi]`, return `True` if it is possible to pick up and drop off all passengers for all the given trips without exceeding capacity.",
        examples=[{"input": "trips = [[2,1,5],[3,3,7]], capacity = 4", "output": "False"}, {"input": "trips = [[2,1,5],[3,3,7]], capacity = 5", "output": "True"}],
        constraints=["1 <= trips.length <= 1000", "1 <= capacity <= 100000"],
        function_name="carPooling",
        starter_code="def carPooling(trips: list[list[int]], capacity: int) -> bool:\n    pass\n",
        solution_code="def carPooling(trips: list[list[int]], capacity: int) -> bool:\n    diff = [0] * 1001\n    for num, start, end in trips:\n        diff[start] += num\n        diff[end] -= num\n    curr = 0\n    for delta in diff:\n        curr += delta\n        if curr > capacity: return False\n    return True\n",
        test_cases=[{"input": [[[2, 1, 5], [3, 3, 7]], 4], "expected": False}, {"input": [[[2, 1, 5], [3, 3, 7]], 5], "expected": True}],
        hints=["Difference array / line sweep: +passengers at pickup, -passengers at dropoff. Check prefix sum <= capacity."],
        leetcode_id=1094
    ))

    return problems
