"""
Data Structures Medium Problems Part 3 (Problems 21 to 40).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_data_structures_medium_part3():
    problems = []

    # 21. Product of Array Except Self
    problems.append(make_problem(
        pid="ds-m-product-except-self", title="Product of Array Except Self",
        wing_id="data-structures", floor=131, difficulty="medium", visualizer_type="array",
        monster_name="Multiplicative Gorgon", monster_title="Drainer of Single Factors",
        monster_sprite="slime", monster_color="#06b6d4", monster_attack="Product Beam",
        monster_quote="Prefix and suffix products dissolved my immunity!",
        description="Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. Do it in O(n) without division.",
        examples=[{"input": "nums = [1,2,3,4]", "output": "[24,12,8,6]"}, {"input": "nums = [-1,1,0,-3,3]", "output": "[0,0,9,0,0]"}],
        constraints=["2 <= len(nums) <= 10^5", "-30 <= nums[i] <= 30"],
        function_name="productExceptSelf",
        starter_code="def productExceptSelf(nums: list[int]) -> list[int]:\n    pass\n",
        solution_code="def productExceptSelf(nums: list[int]) -> list[int]:\n    n = len(nums)\n    res = [1] * n\n    p = 1\n    for i in range(n):\n        res[i] = p\n        p *= nums[i]\n    s = 1\n    for i in range(n - 1, -1, -1):\n        res[i] *= s\n        s *= nums[i]\n    return res\n",
        test_cases=[{"input": [[1, 2, 3, 4]], "expected": [24, 12, 8, 6]}, {"input": [[-1, 1, 0, -3, 3]], "expected": [0, 0, 9, 0, 0]}, {"input": [[2, 3]], "expected": [3, 2]}],
        hints=["Maintain running prefix and suffix product accumulators."],
        leetcode_id=238
    ))

    # 22. Maximum Product Subarray
    problems.append(make_problem(
        pid="ds-m-max-product-subarray", title="Maximum Product Subarray",
        wing_id="data-structures", floor=132, difficulty="medium", visualizer_type="array",
        monster_name="Sign-Flipping Fiend", monster_title="Lord of Inverted Negatives",
        monster_sprite="demon", monster_color="#f97316", monster_attack="Negative Inversion",
        monster_quote="Tracking both max and min products neutralized my parity flips!",
        description="Given an integer array `nums`, find a subarray that has the largest product, and return the product.",
        examples=[{"input": "nums = [2,3,-2,4]", "output": "6"}, {"input": "nums = [-2,0,-1]", "output": "0"}],
        constraints=["1 <= len(nums) <= 2 * 10^4", "-10 <= nums[i] <= 10"],
        function_name="maxProductSubarray",
        starter_code="def maxProductSubarray(nums: list[int]) -> int:\n    pass\n",
        solution_code="def maxProductSubarray(nums: list[int]) -> int:\n    if not nums: return 0\n    res = curr_max = curr_min = nums[0]\n    for n in nums[1:]:\n        if n < 0:\n            curr_max, curr_min = curr_min, curr_max\n        curr_max = max(n, curr_max * n)\n        curr_min = min(n, curr_min * n)\n        res = max(res, curr_max)\n    return res\n",
        test_cases=[{"input": [[2, 3, -2, 4]], "expected": 6}, {"input": [[-2, 0, -1]], "expected": 0}, {"input": [[-2, 3, -4]], "expected": 24}, {"input": [[-2]], "expected": -2}],
        hints=["Track current maximum and minimum product at each step since multiplying by a negative swaps them."],
        leetcode_id=152
    ))

    # 23. Subarray Product Less Than K
    problems.append(make_problem(
        pid="ds-m-subarray-product-less-than-k", title="Subarray Product Less Than K",
        wing_id="data-structures", floor=133, difficulty="medium", visualizer_type="array",
        monster_name="Window Constrictor", monster_title="Tamer of Exponential Growth",
        monster_sprite="slime", monster_color="#84cc16", monster_attack="Growth Constrict",
        monster_quote="Sliding window counted all valid intervals cleanly!",
        description="Given an array of integers `nums` and an integer `k`, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than `k`.",
        examples=[{"input": "nums = [10,5,2,6], k = 100", "output": "8"}, {"input": "nums = [1,2,3], k = 0", "output": "0"}],
        constraints=["1 <= len(nums) <= 3 * 10^4", "1 <= nums[i] <= 1000", "0 <= k <= 10^6"],
        function_name="numSubarrayProductLessThanK",
        starter_code="def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:\n    pass\n",
        solution_code="def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:\n    if k <= 1: return 0\n    prod = 1\n    ans = left = 0\n    for right, val in enumerate(nums):\n        prod *= val\n        while prod >= k:\n            prod //= nums[left]\n            left += 1\n        ans += right - left + 1\n    return ans\n",
        test_cases=[{"input": [[10, 5, 2, 6], 100], "expected": 8}, {"input": [[1, 2, 3], 0], "expected": 0}, {"input": [[1, 1, 1], 2], "expected": 6}, {"input": [[5], 10], "expected": 1}],
        hints=["Use a sliding window. At each right pointer, add (right - left + 1) to answer."],
        leetcode_id=713
    ))

    # 24. Longest Repeating Character Replacement
    problems.append(make_problem(
        pid="ds-m-character-replacement", title="Longest Repeating Character Replacement",
        wing_id="data-structures", floor=134, difficulty="medium", visualizer_type="array",
        monster_name="Substitution Wraith", monster_title="Mutator of String Frequencies",
        monster_sprite="wraith", monster_color="#ec4899", monster_attack="Mutate Blast",
        monster_quote="Your window length minus max frequency never exceeded k!",
        description="You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character at most `k` times. Return the length of the longest substring containing the same letter you can get after performing the above operations.",
        examples=[{"input": "s = \"ABAB\", k = 2", "output": "4"}, {"input": "s = \"AABABBA\", k = 1", "output": "4"}],
        constraints=["1 <= len(s) <= 10^5", "0 <= k <= len(s)", "s consists of only uppercase English letters"],
        function_name="characterReplacement",
        starter_code="def characterReplacement(s: str, k: int) -> int:\n    pass\n",
        solution_code="def characterReplacement(s: str, k: int) -> int:\n    from collections import defaultdict\n    count = defaultdict(int)\n    max_f = 0\n    left = 0\n    res = 0\n    for right in range(len(s)):\n        count[s[right]] += 1\n        max_f = max(max_f, count[s[right]])\n        while (right - left + 1) - max_f > k:\n            count[s[left]] -= 1\n            left += 1\n        res = max(res, right - left + 1)\n    return res\n",
        test_cases=[{"input": ["ABAB", 2], "expected": 4}, {"input": ["AABABBA", 1], "expected": 4}, {"input": ["AAAA", 2], "expected": 4}, {"input": ["ABCDE", 1], "expected": 2}],
        hints=["Sliding window condition: window length minus max frequency in window <= k."],
        leetcode_id=424
    ))

    # 25. Permutation in String
    problems.append(make_problem(
        pid="ds-m-check-inclusion", title="Permutation in String",
        wing_id="data-structures", floor=135, difficulty="medium", visualizer_type="array",
        monster_name="Anagram Hound", monster_title="Sniffer of Substring Scrambles",
        monster_sprite="demon", monster_color="#e11d48", monster_attack="Scent Shred",
        monster_quote="The fixed sliding window frequency match was unmistakable!",
        description="Given two strings `s1` and `s2`, return `True` if `s2` contains a permutation of `s1`, or `False` otherwise.",
        examples=[{"input": "s1 = \"ab\", s2 = \"eidbaooo\"", "output": "True"}, {"input": "s1 = \"ab\", s2 = \"eidboaoo\"", "output": "False"}],
        constraints=["1 <= len(s1), len(s2) <= 10^4", "s1 and s2 consist of lowercase English letters"],
        function_name="checkInclusion",
        starter_code="def checkInclusion(s1: str, s2: str) -> bool:\n    pass\n",
        solution_code="def checkInclusion(s1: str, s2: str) -> bool:\n    from collections import Counter\n    n1, n2 = len(s1), len(s2)\n    if n1 > n2: return False\n    c1 = Counter(s1)\n    c2 = Counter(s2[:n1])\n    if c1 == c2: return True\n    for i in range(n1, n2):\n        c2[s2[i]] += 1\n        old = s2[i - n1]\n        c2[old] -= 1\n        if c2[old] == 0: del c2[old]\n        if c1 == c2: return True\n    return False\n",
        test_cases=[{"input": ["ab", "eidbaooo"], "expected": True}, {"input": ["ab", "eidboaoo"], "expected": False}, {"input": ["a", "a"], "expected": True}, {"input": ["hello", "ooolleoooleh"], "expected": False}],
        hints=["Use a fixed-size sliding window of length len(s1) and compare frequency counts."],
        leetcode_id=567
    ))

    # 26. Fruit Into Baskets
    problems.append(make_problem(
        pid="ds-m-total-fruit", title="Fruit Into Baskets (Two Varieties)",
        wing_id="data-structures", floor=136, difficulty="medium", visualizer_type="array",
        monster_name="Orchard Ogre", monster_title="Glutton of Two Tree Types",
        monster_sprite="orc", monster_color="#eab308", monster_attack="Club Bash",
        monster_quote="You restricted the pick to at most 2 distinct fruits perfectly!",
        description="You are visiting a farm that has a single row of fruit trees represented by an integer array `fruits` where `fruits[i]` is the type of fruit the `i-th` tree produces. You have two baskets, and each basket can only hold a single type of fruit. Return the maximum number of fruits you can pick.",
        examples=[{"input": "fruits = [1,2,1]", "output": "3"}, {"input": "fruits = [0,1,2,2]", "output": "3"}, {"input": "fruits = [1,2,3,2,2]", "output": "4"}],
        constraints=["1 <= len(fruits) <= 10^5", "0 <= fruits[i] < len(fruits)"],
        function_name="totalFruit",
        starter_code="def totalFruit(fruits: list[int]) -> int:\n    pass\n",
        solution_code="def totalFruit(fruits: list[int]) -> int:\n    from collections import defaultdict\n    count = defaultdict(int)\n    left = 0\n    res = 0\n    for right in range(len(fruits)):\n        count[fruits[right]] += 1\n        while len(count) > 2:\n            count[fruits[left]] -= 1\n            if count[fruits[left]] == 0:\n                del count[fruits[left]]\n            left += 1\n        res = max(res, right - left + 1)\n    return res\n",
        test_cases=[{"input": [[1, 2, 1]], "expected": 3}, {"input": [[0, 1, 2, 2]], "expected": 3}, {"input": [[1, 2, 3, 2, 2]], "expected": 4}, {"input": [[3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]], "expected": 5}],
        hints=["Longest contiguous subarray with at most 2 distinct integers."],
        leetcode_id=904
    ))

    # 27. Max Consecutive Ones III
    problems.append(make_problem(
        pid="ds-m-longest-ones", title="Max Consecutive Ones III",
        wing_id="data-structures", floor=137, difficulty="medium", visualizer_type="array",
        monster_name="Binary Lich", monster_title="Inverter of Zero Bit Tombs",
        monster_sprite="lich", monster_color="#38bdf8", monster_attack="Zero Ray",
        monster_quote="Flipping k zeroes yielded the maximum streak!",
        description="Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`s in the array if you can flip at most `k` `0`s.",
        examples=[{"input": "nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2", "output": "6"}, {"input": "nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3", "output": "10"}],
        constraints=["1 <= len(nums) <= 10^5", "nums[i] is either 0 or 1", "0 <= k <= len(nums)"],
        function_name="longestOnes",
        starter_code="def longestOnes(nums: list[int], k: int) -> int:\n    pass\n",
        solution_code="def longestOnes(nums: list[int], k: int) -> int:\n    left = 0\n    zeroes = 0\n    res = 0\n    for right in range(len(nums)):\n        if nums[right] == 0:\n            zeroes += 1\n        while zeroes > k:\n            if nums[left] == 0:\n                zeroes -= 1\n            left += 1\n        res = max(res, right - left + 1)\n    return res\n",
        test_cases=[{"input": [[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2], "expected": 6}, {"input": [[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3], "expected": 10}, {"input": [[0, 0, 0], 1], "expected": 1}],
        hints=["Sliding window with at most k zeroes."],
        leetcode_id=1004
    ))

    # 28. Minimum Size Subarray Sum
    problems.append(make_problem(
        pid="ds-m-min-sub-array-len", title="Minimum Size Subarray Sum",
        wing_id="data-structures", floor=138, difficulty="medium", visualizer_type="array",
        monster_name="Sum Strangler", monster_title="Compressor of Target Bounds",
        monster_sprite="golem", monster_color="#a855f7", monster_attack="Target Squeeze",
        monster_quote="The minimal window satisfying target sum was found!",
        description="Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.",
        examples=[{"input": "target = 7, nums = [2,3,1,2,4,3]", "output": "2"}, {"input": "target = 4, nums = [1,4,4]", "output": "1"}, {"input": "target = 11, nums = [1,1,1,1,1,1,1,1]", "output": "0"}],
        constraints=["1 <= target <= 10^9", "1 <= len(nums) <= 10^5", "1 <= nums[i] <= 10^4"],
        function_name="minSubArrayLen",
        starter_code="def minSubArrayLen(target: int, nums: list[int]) -> int:\n    pass\n",
        solution_code="def minSubArrayLen(target: int, nums: list[int]) -> int:\n    left = 0\n    curr_sum = 0\n    min_len = float('inf')\n    for right in range(len(nums)):\n        curr_sum += nums[right]\n        while curr_sum >= target:\n            min_len = min(min_len, right - left + 1)\n            curr_sum -= nums[left]\n            left += 1\n    return min_len if min_len != float('inf') else 0\n",
        test_cases=[{"input": [7, [2, 3, 1, 2, 4, 3]], "expected": 2}, {"input": [4, [1, 4, 4]], "expected": 1}, {"input": [11, [1, 1, 1, 1, 1, 1, 1, 1]], "expected": 0}, {"input": [6, [10]], "expected": 1}],
        hints=["Expand right to satisfy sum >= target, shrink left to minimize window."],
        leetcode_id=209
    ))

    # 29. Shortest Unsorted Continuous Subarray
    problems.append(make_problem(
        pid="ds-m-find-unsorted-subarray", title="Shortest Unsorted Subarray",
        wing_id="data-structures", floor=139, difficulty="medium", visualizer_type="array",
        monster_name="Disorder Imp", monster_title="Chaos Shuffler of Monotonic Rays",
        monster_sprite="goblin", monster_color="#ef4444", monster_attack="Entropy Dagger",
        monster_quote="The disorder window was pinned between left and right boundaries!",
        description="Given an integer array `nums`, you need to find one continuous subarray such that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order. Return the shortest such subarray's length.",
        examples=[{"input": "nums = [2,6,4,8,10,9,15]", "output": "5"}, {"input": "nums = [1,2,3,4]", "output": "0"}, {"input": "nums = [1]", "output": "0"}],
        constraints=["1 <= len(nums) <= 10^4", "-10^5 <= nums[i] <= 10^5"],
        function_name="findUnsortedSubarray",
        starter_code="def findUnsortedSubarray(nums: list[int]) -> int:\n    pass\n",
        solution_code="def findUnsortedSubarray(nums: list[int]) -> int:\n    sorted_nums = sorted(nums)\n    start = len(nums)\n    end = 0\n    for i in range(len(nums)):\n        if nums[i] != sorted_nums[i]:\n            start = min(start, i)\n            end = max(end, i)\n    return (end - start + 1) if end >= start else 0\n",
        test_cases=[{"input": [[2, 6, 4, 8, 10, 9, 15]], "expected": 5}, {"input": [[1, 2, 3, 4]], "expected": 0}, {"input": [[1]], "expected": 0}, {"input": [[1, 3, 2, 2, 2]], "expected": 4}],
        hints=["Compare array with sorted version to find leftmost and rightmost mismatched indices."],
        leetcode_id=581
    ))

    # 30. Spiral Matrix
    problems.append(make_problem(
        pid="ds-m-spiral-matrix", title="Spiral Matrix Order",
        wing_id="data-structures", floor=140, difficulty="medium", visualizer_type="array",
        monster_name="Vortex Titan", monster_title="Guardian of Inward Spirals",
        monster_sprite="golem", monster_color="#f59e0b", monster_attack="Centripetal Slam",
        monster_quote="The concentric boundaries wound inwards without missing a tile!",
        description="Given an `m x n` `matrix`, return all elements of the `matrix` in spiral order.",
        examples=[{"input": "matrix = [[1,2,3],[4,5,6],[7,8,9]]", "output": "[1,2,3,6,9,8,7,4,5]"}, {"input": "matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]", "output": "[1,2,3,4,8,12,11,10,9,5,6,7]"}],
        constraints=["m == len(matrix)", "n == len(matrix[i])", "1 <= m, n <= 10", "-100 <= matrix[i][j] <= 100"],
        function_name="spiralOrder",
        starter_code="def spiralOrder(matrix: list[list[int]]) -> list[int]:\n    pass\n",
        solution_code="def spiralOrder(matrix: list[list[int]]) -> list[int]:\n    if not matrix or not matrix[0]: return []\n    res = []\n    top, bottom = 0, len(matrix) - 1\n    left, right = 0, len(matrix[0]) - 1\n    while top <= bottom and left <= right:\n        for c in range(left, right + 1): res.append(matrix[top][c])\n        top += 1\n        for r in range(top, bottom + 1): res.append(matrix[r][right])\n        right -= 1\n        if top <= bottom:\n            for c in range(right, left - 1, -1): res.append(matrix[bottom][c])\n            bottom -= 1\n        if left <= right:\n            for r in range(bottom, top - 1, -1): res.append(matrix[r][left])\n            left += 1\n    return res\n",
        test_cases=[{"input": [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], "expected": [1, 2, 3, 6, 9, 8, 7, 4, 5]}, {"input": [[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]], "expected": [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]}, {"input": [[[1]]], "expected": [1]}],
        hints=["Maintain top, bottom, left, right bounds and shrink them inward after each direction."],
        leetcode_id=54
    ))

    # 31. Rotate Image
    problems.append(make_problem(
        pid="ds-m-rotate-image", title="Rotate Matrix 90 Degrees Clockwise",
        wing_id="data-structures", floor=141, difficulty="medium", visualizer_type="array",
        monster_name="Gyroscopic Drake", monster_title="Rotator of Spatial Grids",
        monster_sprite="dragon", monster_color="#10b981", monster_attack="Torque Breath",
        monster_quote="Transpose followed by reflection turned the board 90 degrees!",
        description="You are given an `n x n` 2D `matrix` representing an image, rotate the image by 90 degrees (clockwise) in-place. Return the rotated matrix.",
        examples=[{"input": "matrix = [[1,2,3],[4,5,6],[7,8,9]]", "output": "[[7,4,1],[8,5,2],[9,6,3]]"}],
        constraints=["n == len(matrix) == len(matrix[i])", "1 <= n <= 20", "-1000 <= matrix[i][j] <= 1000"],
        function_name="rotateImage",
        starter_code="def rotateImage(matrix: list[list[int]]) -> list[list[int]]:\n    pass\n",
        solution_code="def rotateImage(matrix: list[list[int]]) -> list[list[int]]:\n    n = len(matrix)\n    for i in range(n):\n        for j in range(i + 1, n):\n            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]\n    for r in range(n):\n        matrix[r].reverse()\n    return matrix\n",
        test_cases=[{"input": [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], "expected": [[7, 4, 1], [8, 5, 2], [9, 6, 3]]}, {"input": [[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]], "expected": [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]}, {"input": [[[1]]], "expected": [[1]]}],
        hints=["Transpose the matrix across its main diagonal, then reverse each row."],
        leetcode_id=48
    ))

    # 32. Set Matrix Zeroes
    problems.append(make_problem(
        pid="ds-m-set-matrix-zeroes", title="Set Matrix Zeroes",
        wing_id="data-structures", floor=142, difficulty="medium", visualizer_type="array",
        monster_name="Nullifying Shade", monster_title="Eraser of Rows and Columns",
        monster_sprite="wraith", monster_color="#64748b", monster_attack="Null Pulse",
        monster_quote="Zero markers kept track of zero propagation in constant extra space!",
        description="Given an `m x n` integer matrix `matrix`, if an element is `0`, set its entire row and column to `0`'s in-place. Return the modified matrix.",
        examples=[{"input": "matrix = [[1,1,1],[1,0,1],[1,1,1]]", "output": "[[1,0,1],[0,0,0],[1,0,1]]"}],
        constraints=["m == len(matrix)", "n == len(matrix[0])", "1 <= m, n <= 200"],
        function_name="setZeroes",
        starter_code="def setZeroes(matrix: list[list[int]]) -> list[list[int]]:\n    pass\n",
        solution_code="def setZeroes(matrix: list[list[int]]) -> list[list[int]]:\n    m, n = len(matrix), len(matrix[0])\n    first_row_zero = any(matrix[0][j] == 0 for j in range(n))\n    first_col_zero = any(matrix[i][0] == 0 for i in range(m))\n    for i in range(1, m):\n        for j in range(1, n):\n            if matrix[i][j] == 0:\n                matrix[i][0] = 0\n                matrix[0][j] = 0\n    for i in range(1, m):\n        for j in range(1, n):\n            if matrix[i][0] == 0 or matrix[0][j] == 0:\n                matrix[i][j] = 0\n    if first_row_zero:\n        for j in range(n): matrix[0][j] = 0\n    if first_col_zero:\n        for i in range(m): matrix[i][0] = 0\n    return matrix\n",
        test_cases=[{"input": [[[1, 1, 1], [1, 0, 1], [1, 1, 1]]], "expected": [[1, 0, 1], [0, 0, 0], [1, 0, 1]]}, {"input": [[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]], "expected": [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]}],
        hints=["Use first row and first column as marker flags."],
        leetcode_id=73
    ))

    # 33. Game of Life Next Generation
    problems.append(make_problem(
        pid="ds-m-game-of-life", title="Game of Life Next State",
        wing_id="data-structures", floor=143, difficulty="medium", visualizer_type="array",
        monster_name="Conway Cell Core", monster_title="Automaton of Birth and Death",
        monster_sprite="slime", monster_color="#06b6d4", monster_attack="Cellular Pulse",
        monster_quote="In-place bit transitions calculated the next generation perfectly!",
        description="Given an `m x n` grid of 0s (dead) and 1s (live), compute the next state according to Conway's Game of Life: any live cell with fewer than 2 or more than 3 live neighbors dies; with 2 or 3 live neighbors lives; any dead cell with exactly 3 live neighbors becomes a live cell. Return the updated grid.",
        examples=[{"input": "board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]", "output": "[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]"}],
        constraints=["m == len(board)", "n == len(board[i])", "1 <= m, n <= 25"],
        function_name="gameOfLifeNext",
        starter_code="def gameOfLifeNext(board: list[list[int]]) -> list[list[int]]:\n    pass\n",
        solution_code="def gameOfLifeNext(board: list[list[int]]) -> list[list[int]]:\n    m, n = len(board), len(board[0])\n    # Encode transitions: 0->0: 0, 1->1: 1, 1->0: 2, 0->1: 3\n    for r in range(m):\n        for c in range(n):\n            live_neighbors = 0\n            for dr in [-1, 0, 1]:\n                for dc in [-1, 0, 1]:\n                    if dr == 0 and dc == 0: continue\n                    nr, nc = r + dr, c + dc\n                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in (1, 2):\n                        live_neighbors += 1\n            if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):\n                board[r][c] = 2\n            elif board[r][c] == 0 and live_neighbors == 3:\n                board[r][c] = 3\n    for r in range(m):\n        for c in range(n):\n            board[r][c] = 1 if board[r][c] in (1, 3) else 0\n    return board\n",
        test_cases=[{"input": [[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]], "expected": [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]}, {"input": [[[1, 1], [1, 0]]], "expected": [[1, 1], [1, 1]]}],
        hints=["Use 2-bit states to encode both past and future states in-place."],
        leetcode_id=289
    ))

    # 34. Diagonal Traverse Order
    problems.append(make_problem(
        pid="ds-m-find-diagonal-order", title="Diagonal Traverse Order",
        wing_id="data-structures", floor=144, difficulty="medium", visualizer_type="array",
        monster_name="Zigzag Wyrm", monster_title="Slitherer of Diagonal Strides",
        monster_sprite="dragon", monster_color="#8b5cf6", monster_attack="Zigzag Constrict",
        monster_quote="Diagonals grouped by r + c and flipped on alternating turns!",
        description="Given an `m x n` matrix `mat`, return an array of all the elements of the array in a diagonal order.",
        examples=[{"input": "mat = [[1,2,3],[4,5,6],[7,8,9]]", "output": "[1,2,4,7,5,3,6,8,9]"}, {"input": "mat = [[1,2],[3,4]]", "output": "[1,2,3,4]"}],
        constraints=["m == len(mat)", "n == len(mat[i])", "1 <= m, n <= 10^4", "1 <= m * n <= 10^4"],
        function_name="findDiagonalOrder",
        starter_code="def findDiagonalOrder(mat: list[list[int]]) -> list[int]:\n    pass\n",
        solution_code="def findDiagonalOrder(mat: list[list[int]]) -> list[int]:\n    if not mat or not mat[0]: return []\n    from collections import defaultdict\n    diags = defaultdict(list)\n    m, n = len(mat), len(mat[0])\n    for r in range(m):\n        for c in range(n):\n            diags[r + c].append(mat[r][c])\n    res = []\n    for k in range(m + n - 1):\n        if k % 2 == 0:\n            res.extend(reversed(diags[k]))\n        else:\n            res.extend(diags[k])\n    return res\n",
        test_cases=[{"input": [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], "expected": [1, 2, 4, 7, 5, 3, 6, 8, 9]}, {"input": [[[1, 2], [3, 4]]], "expected": [1, 2, 3, 4]}, {"input": [[[5]]], "expected": [5]}],
        hints=["Notice that elements on the same diagonal share the same r + c sum."],
        leetcode_id=498
    ))

    # 35. Count Number of Nice Subarrays (K Odds)
    problems.append(make_problem(
        pid="ds-m-number-of-subarrays", title="Count Nice Subarrays (K Odd Numbers)",
        wing_id="data-structures", floor=145, difficulty="medium", visualizer_type="array",
        monster_name="Parity Specter", monster_title="Tallyman of Odd Number Pulses",
        monster_sprite="wraith", monster_color="#ec4899", monster_attack="Odd Pulse",
        monster_quote="Prefix odd counts revealed all matching intervals!",
        description="Given an array of integers `nums` and an integer `k`. A continuous subarray is called nice if there are `k` odd numbers on it. Return the number of nice sub-arrays.",
        examples=[{"input": "nums = [1,1,2,1,1], k = 3", "output": "2"}, {"input": "nums = [2,4,6], k = 1", "output": "0"}, {"input": "nums = [2,2,2,1,2,2,1,2,2,2], k = 2", "output": "16"}],
        constraints=["1 <= len(nums) <= 50000", "1 <= nums[i] <= 10^5", "1 <= k <= len(nums)"],
        function_name="numberOfSubarrays",
        starter_code="def numberOfSubarrays(nums: list[int], k: int) -> int:\n    pass\n",
        solution_code="def numberOfSubarrays(nums: list[int], k: int) -> int:\n    from collections import defaultdict\n    count = defaultdict(int)\n    count[0] = 1\n    curr = 0\n    ans = 0\n    for n in nums:\n        curr += (n % 2)\n        ans += count[curr - k]\n        count[curr] += 1\n    return ans\n",
        test_cases=[{"input": [[1, 1, 2, 1, 1], 3], "expected": 2}, {"input": [[2, 4, 6], 1], "expected": 0}, {"input": [[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2], "expected": 16}, {"input": [[1], 1], "expected": 1}],
        hints=["Convert to 0s and 1s (n % 2) and use a prefix sum map for sum equals k."],
        leetcode_id=1248
    ))

    # 36. Maximum Points You Can Obtain from Cards
    problems.append(make_problem(
        pid="ds-m-max-score-cards", title="Maximum Points From Cards",
        wing_id="data-structures", floor=146, difficulty="medium", visualizer_type="array",
        monster_name="Deck Leviathan", monster_title="Dealer of Edge-Card Draws",
        monster_sprite="hydra", monster_color="#10b981", monster_attack="Card Barrage",
        monster_quote="Finding the minimum remaining middle window maximized card sum!",
        description="There are several cards arranged in a row, and each card has an associated number of points. In one step, you can take one card from the beginning or from the end of the row. You have to take exactly `k` cards. Your score is the sum of the points of the cards you have taken. Return the maximum score you can obtain.",
        examples=[{"input": "cardPoints = [1,2,3,4,5,6,1], k = 3", "output": "12"}, {"input": "cardPoints = [2,2,2], k = 2", "output": "4"}, {"input": "cardPoints = [9,7,7,9,7,7,9], k = 7", "output": "55"}],
        constraints=["1 <= len(cardPoints) <= 10^5", "1 <= cardPoints[i] <= 10^4", "1 <= k <= len(cardPoints)"],
        function_name="maxScoreCards",
        starter_code="def maxScoreCards(cardPoints: list[int], k: int) -> int:\n    pass\n",
        solution_code="def maxScoreCards(cardPoints: list[int], k: int) -> int:\n    n = len(cardPoints)\n    window_size = n - k\n    total = sum(cardPoints)\n    if window_size == 0: return total\n    curr = sum(cardPoints[:window_size])\n    min_window = curr\n    for i in range(window_size, n):\n        curr += cardPoints[i] - cardPoints[i - window_size]\n        min_window = min(min_window, curr)\n    return total - min_window\n",
        test_cases=[{"input": [[1, 2, 3, 4, 5, 6, 1], 3], "expected": 12}, {"input": [[2, 2, 2], 2], "expected": 4}, {"input": [[9, 7, 7, 9, 7, 7, 9], 7], "expected": 55}, {"input": [[1, 1000, 1], 1], "expected": 1}],
        hints=["Taking k cards from the ends is equivalent to leaving a contiguous window of size n - k with minimal sum."],
        leetcode_id=1423
    ))

    # 37. Continuous Subarray Sum (Multiple of K)
    problems.append(make_problem(
        pid="ds-m-check-subarray-sum", title="Continuous Subarray Sum Multiple",
        wing_id="data-structures", floor=147, difficulty="medium", visualizer_type="array",
        monster_name="Modular Golem", monster_title="Clockwork Keeper of Modulo Rings",
        monster_sprite="golem", monster_color="#f59e0b", monster_attack="Modulo Quake",
        monster_quote="Matching remainder seen at least 2 steps prior proved divisibility!",
        description="Given an integer array `nums` and an integer `k`, return `True` if `nums` has a good subarray of length at least 2 whose sum is a multiple of `k`, or `False` otherwise.",
        examples=[{"input": "nums = [23,2,4,6,7], k = 6", "output": "True"}, {"input": "nums = [23,2,6,4,7], k = 6", "output": "True"}, {"input": "nums = [23,2,6,4,7], k = 13", "output": "False"}],
        constraints=["1 <= len(nums) <= 10^5", "0 <= nums[i] <= 10^9", "1 <= k <= 2^31 - 1"],
        function_name="checkSubarraySum",
        starter_code="def checkSubarraySum(nums: list[int], k: int) -> bool:\n    pass\n",
        solution_code="def checkSubarraySum(nums: list[int], k: int) -> bool:\n    rem_map = {0: -1}\n    curr = 0\n    for i, n in enumerate(nums):\n        curr = (curr + n) % k\n        if curr in rem_map:\n            if i - rem_map[curr] >= 2:\n                return True\n        else:\n            rem_map[curr] = i\n    return False\n",
        test_cases=[{"input": [[23, 2, 4, 6, 7], 6], "expected": True}, {"input": [[23, 2, 6, 4, 7], 6], "expected": True}, {"input": [[23, 2, 6, 4, 7], 13], "expected": False}, {"input": [[5, 0, 0, 0], 3], "expected": True}],
        hints=["Store earliest index of each prefix remainder mod k. If same remainder occurs at index j with j - i >= 2, the subarray sum is divisible by k."],
        leetcode_id=523
    ))

    # 38. Subarray Sums Divisible by K
    problems.append(make_problem(
        pid="ds-m-subarrays-div-by-k", title="Subarray Sums Divisible by K",
        wing_id="data-structures", floor=148, difficulty="medium", visualizer_type="array",
        monster_name="Ring Divisor Demon", monster_title="Harvester of Exact Modular Cycles",
        monster_sprite="demon", monster_color="#8b5cf6", monster_attack="Cycle Drain",
        monster_quote="Combinations of identical remainders summed up all divisible subarrays!",
        description="Given an integer array `nums` and an integer `k`, return the number of non-empty subarrays that have a sum divisible by `k`.",
        examples=[{"input": "nums = [4,5,0,-2,-3,1], k = 5", "output": "7"}, {"input": "nums = [5], k = 9", "output": "0"}],
        constraints=["1 <= len(nums) <= 3 * 10^4", "-10^4 <= nums[i] <= 10^4", "2 <= k <= 10^4"],
        function_name="subarraysDivByK",
        starter_code="def subarraysDivByK(nums: list[int], k: int) -> int:\n    pass\n",
        solution_code="def subarraysDivByK(nums: list[int], k: int) -> int:\n    from collections import defaultdict\n    count = defaultdict(int)\n    count[0] = 1\n    curr = 0\n    ans = 0\n    for n in nums:\n        curr = (curr + n) % k\n        ans += count[curr]\n        count[curr] += 1\n    return ans\n",
        test_cases=[{"input": [[4, 5, 0, -2, -3, 1], 5], "expected": 7}, {"input": [[5], 9], "expected": 0}, {"input": [[-1, 2, 9], 2], "expected": 2}, {"input": [[0, 0], 3], "expected": 3}],
        hints=["Keep a count of prefix sum remainders modulo k."],
        leetcode_id=974
    ))

    # 39. Contiguous Array (Equal 0s and 1s)
    problems.append(make_problem(
        pid="ds-m-find-max-length", title="Contiguous Array with Equal 0s and 1s",
        wing_id="data-structures", floor=149, difficulty="medium", visualizer_type="array",
        monster_name="Equilibrium Sphinx", monster_title="Examiner of Balanced Polarities",
        monster_sprite="beholder", monster_color="#ec4899", monster_attack="Polarity Gaze",
        monster_quote="Replacing 0 with -1 reduced the problem to finding identical prefix sums!",
        description="Given a binary array `nums`, return the maximum length of a contiguous subarray with an equal number of `0` and `1`.",
        examples=[{"input": "nums = [0,1]", "output": "2"}, {"input": "nums = [0,1,0]", "output": "2"}],
        constraints=["1 <= len(nums) <= 10^5", "nums[i] is either 0 or 1"],
        function_name="findMaxLength",
        starter_code="def findMaxLength(nums: list[int]) -> int:\n    pass\n",
        solution_code="def findMaxLength(nums: list[int]) -> int:\n    seen = {0: -1}\n    curr = 0\n    max_len = 0\n    for i, n in enumerate(nums):\n        curr += (1 if n == 1 else -1)\n        if curr in seen:\n            max_len = max(max_len, i - seen[curr])\n        else:\n            seen[curr] = i\n    return max_len\n",
        test_cases=[{"input": [[0, 1]], "expected": 2}, {"input": [[0, 1, 0]], "expected": 2}, {"input": [[0, 0, 1, 0, 0, 0, 1, 1]], "expected": 6}, {"input": [[0]], "expected": 0}],
        hints=["Treat 0 as -1 and find the longest subarray with sum 0 using a hash map of first seen indices."],
        leetcode_id=525
    ))

    # 40. Longest Well-Performing Interval
    problems.append(make_problem(
        pid="ds-m-longest-wpi", title="Longest Well-Performing Interval",
        wing_id="data-structures", floor=150, difficulty="medium", visualizer_type="array",
        monster_name="Overtime Lich", monster_title="Counter of Tiresome Shifts",
        monster_sprite="lich", monster_color="#e11d48", monster_attack="Fatigue Hex",
        monster_quote="Score strictly greater than 0 identified the longest interval!",
        description="We are given `hours`, a list of the number of hours worked per day for a given employee. A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than `8`. A well-performing interval is an interval of days on which the number of tiring days is strictly larger than the number of non-tiring days. Return the length of the longest well-performing interval.",
        examples=[{"input": "hours = [9,9,6,0,6,6,9]", "output": "3"}, {"input": "hours = [6,6,6]", "output": "0"}],
        constraints=["1 <= len(hours) <= 10^4", "0 <= hours[i] <= 16"],
        function_name="longestWPI",
        starter_code="def longestWPI(hours: list[int]) -> int:\n    pass\n",
        solution_code="def longestWPI(hours: list[int]) -> int:\n    res = curr = 0\n    seen = {}\n    for i, h in enumerate(hours):\n        curr += (1 if h > 8 else -1)\n        if curr > 0:\n            res = i + 1\n        else:\n            if curr not in seen:\n                seen[curr] = i\n            if curr - 1 in seen:\n                res = max(res, i - seen[curr - 1])\n    return res\n",
        test_cases=[{"input": [[9, 9, 6, 0, 6, 6, 9]], "expected": 3}, {"input": [[6, 6, 6]], "expected": 0}, {"input": [[9, 9, 9]], "expected": 3}, {"input": [[6, 9, 9]], "expected": 3}],
        hints=["Convert days with >8h to +1, else -1. Look for intervals where prefix sum difference > 0."],
        leetcode_id=1124
    ))

    return problems
