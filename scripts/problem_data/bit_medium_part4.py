"""
Bit Manipulation Medium Problems - Part 4 (Floors 556 to 570 - 15 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_bit_medium_part4():
    problems = []

    # 56. Bitwise XOR of All Pairings
    problems.append(make_problem(
        pid="bit-m-xor-all-pairings", title="Bitwise XOR of All Pairings",
        wing_id="bit-manipulation", floor=556, difficulty="medium", visualizer_type="array",
        monster_name="Cartesian Imp", monster_title="Multiplier of Pairwise XORs",
        monster_sprite="imp", monster_color="#38bdf8", monster_attack="Pairwise XOR",
        monster_quote="XOR sum of all Cartesian pairs (nums1[i] ^ nums2[j]) computed in O(n + m)!",
        description="You are given two 0-indexed arrays, `nums1` and `nums2`, consisting of non-negative integers. There exists another array, `nums3`, which contains the bitwise XOR of all pairings of integers between `nums1` and `nums2`. Return the bitwise XOR of all integers in `nums3`.",
        examples=[{"input": "nums1 = [2,1,3], nums2 = [10,2,5,0]", "output": "13"}, {"input": "nums1 = [1,2], nums2 = [3,4]", "output": "0"}],
        constraints=["1 <= nums1.length, nums2.length <= 100000"],
        function_name="xorAllNums",
        starter_code="def xorAllNums(nums1: list[int], nums2: list[int]) -> int:\n    pass\n",
        solution_code="def xorAllNums(nums1: list[int], nums2: list[int]) -> int:\n    ans = 0\n    if len(nums2) % 2 == 1:\n        for x in nums1: ans ^= x\n    if len(nums1) % 2 == 1:\n        for y in nums2: ans ^= y\n    return ans\n",
        test_cases=[{"input": [[2, 1, 3], [10, 2, 5, 0]], "expected": 13}, {"input": [[1, 2], [3, 4]], "expected": 0}],
        hints=["Each element in nums1 appears len(nums2) times, and each in nums2 appears len(nums1) times. Use parity."],
        leetcode_id=2425
    ))

    # 57. Minimize XOR
    problems.append(make_problem(
        pid="bit-m-minimize-xor-target-bits", title="Minimize XOR with Target Bit Count",
        wing_id="bit-manipulation", floor=557, difficulty="medium", visualizer_type="array",
        monster_name="Hamming Matcher", monster_title="Aligner of Set Bits with Target",
        monster_sprite="wraith", monster_color="#8b5cf6", monster_attack="Hamming Beam",
        monster_quote="Integer x constructed with popcount(num2) bits minimizing x ^ num1!",
        description="Given two positive integers `num1` and `num2`, find the positive integer `x` such that: 1. `x` has the same number of set bits as `num2`, and 2. The value `x XOR num1` is minimal.",
        examples=[{"input": "num1 = 3, num2 = 5", "output": "3"}, {"input": "num1 = 1, num2 = 12", "output": "3"}],
        constraints=["1 <= num1, num2 <= 10^9"],
        function_name="minimizeXor",
        starter_code="def minimizeXor(num1: int, num2: int) -> int:\n    pass\n",
        solution_code="def minimizeXor(num1: int, num2: int) -> int:\n    target_bits = bin(num2).count('1')\n    curr_bits = bin(num1).count('1')\n    res = num1\n    for i in range(32):\n        if curr_bits > target_bits and (res & (1 << i)):\n            res ^= (1 << i)\n            curr_bits -= 1\n        elif curr_bits < target_bits and not (res & (1 << i)):\n            res |= (1 << i)\n            curr_bits += 1\n    return res\n",
        test_cases=[{"input": [3, 5], "expected": 3}, {"input": [1, 12], "expected": 3}],
        hints=["Match num1's bits from highest to lowest. Clear lowest bits if count is too high, set lowest 0-bits if count is too low."],
        leetcode_id=2429
    ))

    # 58. Apply Bitwise Operations to Make Strings Equal
    problems.append(make_problem(
        pid="bit-m-apply-bitwise-ops-equal", title="Make Binary Strings Equal via (OR, XOR)",
        wing_id="bit-manipulation", floor=558, difficulty="medium", visualizer_type="array",
        monster_name="Transition Specter", monster_title="Transformer of Binary Pairs",
        monster_sprite="spectre", monster_color="#10b981", monster_attack="Bit Transition",
        monster_quote="Can s be transformed into target via (s[i]|s[j], s[i]^s[j]) operations?",
        description="You are given two 0-indexed binary strings `s` and `target` of the same length. You can choose two distinct indices `i` and `j` and simultaneously replace `s[i]` with `(s[i] OR s[j])` and `s[j]` with `(s[i] XOR s[j])`. Return `True` if you can make `s` equal to `target`, or `False` otherwise.",
        examples=[{"input": "s = \"1010\", target = \"0110\"", "output": "True"}, {"input": "s = \"00\", target = \"11\"", "output": "False"}],
        constraints=["n == s.length == target.length <= 100000"],
        function_name="makeStringsEqual",
        starter_code="def makeStringsEqual(s: str, target: str) -> bool:\n    pass\n",
        solution_code="def makeStringsEqual(s: str, target: str) -> bool:\n    return ('1' in s) == ('1' in target)\n",
        test_cases=[{"input": ["1010", "0110"], "expected": True}, {"input": ["00", "11"], "expected": False}],
        hints=["The operation can change 10 -> 11, 01 -> 11, 11 -> 10. As long as at least one '1' exists in both strings (or both have no 1s), transformation is possible."],
        leetcode_id=2546
    ))

    # 59. Number of Steps to Reduce a Number to Zero
    problems.append(make_problem(
        pid="bit-m-steps-reduce-to-zero", title="Number of Steps to Reduce to Zero",
        wing_id="bit-manipulation", floor=559, difficulty="medium", visualizer_type="array",
        monster_name="Division Fiend", monster_title="Stepping Down to Zero",
        monster_sprite="imp", monster_color="#ef4444", monster_attack="Step Drain",
        monster_quote="Steps to reduce num to zero using (/2 if even, -1 if odd)!",
        description="Given an integer `num`, return the number of steps to reduce it to zero. In one step, if the current number is even, divide it by 2; otherwise, subtract 1.",
        examples=[{"input": "num = 14", "output": "6"}, {"input": "num = 8", "output": "4"}, {"input": "num = 123", "output": "12"}],
        constraints=["0 <= num <= 10^6"],
        function_name="numberOfSteps",
        starter_code="def numberOfSteps(num: int) -> int:\n    pass\n",
        solution_code="def numberOfSteps(num: int) -> int:\n    if num == 0: return 0\n    b = bin(num)[2:]\n    return len(b) - 1 + b.count('1')\n",
        test_cases=[{"input": [14], "expected": 6}, {"input": [8], "expected": 4}, {"input": [123], "expected": 12}],
        hints=["Bitwise observation: each division by 2 shifts right (len - 1 steps), and each 1-bit requires an extra subtraction."],
        leetcode_id=1342
    ))

    # 60. Prime Number of Set Bits in Binary Representation
    problems.append(make_problem(
        pid="bit-m-prime-set-bits-binary", title="Prime Number of Set Bits in Range",
        wing_id="bit-manipulation", floor=560, difficulty="medium", visualizer_type="array",
        monster_name="Primal Archon", monster_title="Filter of Prime Hamming Weights",
        monster_sprite="wizard", monster_color="#f59e0b", monster_attack="Primal Pulse",
        monster_quote="Numbers with prime Hamming weights in [left, right] counted!",
        description="Given two integers `left` and `right`, return the count of numbers in the inclusive range `[left, right]` having a prime number of set bits in their binary representation.",
        examples=[{"input": "left = 6, right = 10", "output": "4"}, {"input": "left = 10, right = 15", "output": "5"}],
        constraints=["1 <= left <= right <= 10^6", "right - left <= 10000"],
        function_name="countPrimeSetBits",
        starter_code="def countPrimeSetBits(left: int, right: int) -> int:\n    pass\n",
        solution_code="def countPrimeSetBits(left: int, right: int) -> int:\n    primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}\n    return sum(1 for x in range(left, right + 1) if bin(x).count('1') in primes)\n",
        test_cases=[{"input": [6, 10], "expected": 4}, {"input": [10, 15], "expected": 5}],
        hints=["Precompute the set of primes up to 32."],
        leetcode_id=762
    ))

    # 61. Binary Gap
    problems.append(make_problem(
        pid="bit-m-binary-gap-distance", title="Binary Gap (Longest Consecutive 1-Bit Distance)",
        wing_id="bit-manipulation", floor=561, difficulty="medium", visualizer_type="array",
        monster_name="Gap Wyrm", monster_title="Surveyor of Gaps Between Set Bits",
        monster_sprite="dragon", monster_color="#06b6d4", monster_attack="Gap Stride",
        monster_quote="Maximum distance between two consecutive 1-bits found!",
        description="Given a positive integer `n`, find and return the longest distance between any two adjacent 1's in the binary representation of `n`. If there are no two adjacent 1's, return 0.",
        examples=[{"input": "n = 22", "output": "2"}, {"input": "n = 8", "output": "0"}, {"input": "n = 5", "output": "2"}],
        constraints=["1 <= n <= 10^9"],
        function_name="binaryGap",
        starter_code="def binaryGap(n: int) -> int:\n    pass\n",
        solution_code="def binaryGap(n: int) -> int:\n    last = -1\n    max_gap = 0\n    for i in range(32):\n        if (n >> i) & 1:\n            if last != -1:\n                max_gap = max(max_gap, i - last)\n            last = i\n    return max_gap\n",
        test_cases=[{"input": [22], "expected": 2}, {"input": [8], "expected": 0}, {"input": [5], "expected": 2}],
        hints=["Iterate bit indices tracking position of the previous set bit."],
        leetcode_id=868
    ))

    # 62. Complement of Base 10 Integer
    problems.append(make_problem(
        pid="bit-m-complement-base-10", title="Complement of Base 10 Integer",
        wing_id="bit-manipulation", floor=562, difficulty="medium", visualizer_type="array",
        monster_name="Bit Inversion Imp", monster_title="Inverter of Binary Representation",
        monster_sprite="imp", monster_color="#ec4899", monster_attack="Invert Flash",
        monster_quote="Binary complement converted back to base 10 integer!",
        description="The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation. Given an integer `n`, return its complement.",
        examples=[{"input": "n = 5", "output": "2"}, {"input": "n = 7", "output": "0"}, {"input": "n = 10", "output": "5"}],
        constraints=["0 <= n < 10^9"],
        function_name="bitwiseComplement",
        starter_code="def bitwiseComplement(n: int) -> int:\n    pass\n",
        solution_code="def bitwiseComplement(n: int) -> int:\n    if n == 0: return 1\n    mask = (1 << n.bit_length()) - 1\n    return n ^ mask\n",
        test_cases=[{"input": [5], "expected": 2}, {"input": [7], "expected": 0}, {"input": [10], "expected": 5}, {"input": [0], "expected": 1}],
        hints=["XOR with a mask of all 1s having length n.bit_length()."],
        leetcode_id=1009
    ))

    # 63. Maximum XOR After Operations
    problems.append(make_problem(
        pid="bit-m-max-xor-after-operations", title="Maximum XOR After Operations",
        wing_id="bit-manipulation", floor=563, difficulty="medium", visualizer_type="array",
        monster_name="Cumulative Bit Fiend", monster_title="Harvester of Available Bits",
        monster_sprite="demon", monster_color="#38bdf8", monster_attack="Union Ray",
        monster_quote="Maximum bitwise XOR achievable across arbitrary bit deletions!",
        description="You are given a 0-indexed integer array `nums`. In one operation, you may choose any integer `nums[i]` and any integer `x`, and set `nums[i] = nums[i] AND (nums[i] XOR x)`. Return the maximum possible bitwise XOR of all elements of `nums` after applying the operation any number of times.",
        examples=[{"input": "nums = [3,2,4,6]", "output": "7"}, {"input": "nums = [1,2,3,9,2]", "output": "11"}],
        constraints=["1 <= nums.length <= 100000"],
        function_name="maximumXOR",
        starter_code="def maximumXOR(nums: list[int]) -> int:\n    pass\n",
        solution_code="def maximumXOR(nums: list[int]) -> int:\n    ans = 0\n    for x in nums: ans |= x\n    return ans\n",
        test_cases=[{"input": [[3, 2, 4, 6]], "expected": 7}, {"input": [[1, 2, 3, 9, 2]], "expected": 11}],
        hints=["The operation allows clearing any 1-bit from any number. Thus, any bit that appears in at least one number can be preserved as a single 1. Result is the bitwise OR of all numbers."],
        leetcode_id=2317
    ))

    # 64. Sum of XOR of All Subsets
    problems.append(make_problem(
        pid="bit-m-sum-xor-all-subsets", title="Sum of All Subset XOR Totals",
        wing_id="bit-manipulation", floor=564, difficulty="medium", visualizer_type="array",
        monster_name="Subset Summing Titan", monster_title="Accumulator of 2^(N-1) Subsets",
        monster_sprite="titan", monster_color="#ef4444", monster_attack="Subset Slam",
        monster_quote="Sum of XOR totals of every possible subset evaluated!",
        description="The XOR total of an array is the bitwise XOR of all its elements. Given an array `nums`, return the sum of all XOR totals for every subset of `nums`.",
        examples=[{"input": "nums = [1,3]", "output": "6"}, {"input": "nums = [5,1,6]", "output": "28"}],
        constraints=["1 <= nums.length <= 12"],
        function_name="subsetXORSum",
        starter_code="def subsetXORSum(nums: list[int]) -> int:\n    pass\n",
        solution_code="def subsetXORSum(nums: list[int]) -> int:\n    or_sum = 0\n    for x in nums: or_sum |= x\n    return or_sum * (1 << (len(nums) - 1))\n",
        test_cases=[{"input": [[1, 3]], "expected": 6}, {"input": [[5, 1, 6]], "expected": 28}],
        hints=["Each bit present in the bitwise OR of nums appears in exactly 2^(n - 1) subsets. Formula: OR(nums) * 2^(n - 1)."],
        leetcode_id=1863
    ))

    # 65. Gray Code to Binary Converter
    problems.append(make_problem(
        pid="bit-m-gray-to-binary-converter", title="Gray Code to Binary Conversion",
        wing_id="bit-manipulation", floor=565, difficulty="medium", visualizer_type="array",
        monster_name="Decryption Drake", monster_title="Inverter of Reflected Code",
        monster_sprite="dragon", monster_color="#8b5cf6", monster_attack="Binary Decode",
        monster_quote="Gray code integer converted back to natural binary integer!",
        description="Given a non-negative integer `gray` representing an n-bit Gray code value, return its corresponding standard binary integer representation.",
        examples=[{"input": "gray = 3", "output": "2"}, {"input": "gray = 6", "output": "4"}, {"input": "gray = 0", "output": "0"}],
        constraints=["0 <= gray <= 2^31 - 1"],
        function_name="grayToBinary",
        starter_code="def grayToBinary(gray: int) -> int:\n    pass\n",
        solution_code="def grayToBinary(gray: int) -> int:\n    binary = 0\n    while gray > 0:\n        binary ^= gray\n        gray >>= 1\n    return binary\n",
        test_cases=[{"input": [3], "expected": 2}, {"input": [6], "expected": 4}, {"input": [0], "expected": 0}],
        hints=["Binary = gray ^ (gray >> 1) ^ (gray >> 2) ^ ..."],
        leetcode_id=0
    ))

    # 66. Minimum Operations to Form Subsequence With Target Sum
    problems.append(make_problem(
        pid="bit-m-min-ops-subsequence-target", title="Min Splits to Form Subsequence of Target Sum",
        wing_id="bit-manipulation", floor=566, difficulty="medium", visualizer_type="array",
        monster_name="Fission Spectre", monster_title="Halver of Power-of-Two Blocks",
        monster_sprite="wraith", monster_color="#10b981", monster_attack="Power Fission",
        monster_quote="Minimum power-of-two splits to assemble target sum!",
        description="You are given a 0-indexed array `nums` consisting of positive powers of 2, and an integer `target`. In one operation, you can choose any element and split it into two equal powers of 2. Return the minimum number of operations to form a subsequence of `nums` that sums to `target`, or -1 if impossible.",
        examples=[{"input": "nums = [1,2,8], target = 7", "output": "1"}, {"input": "nums = [1,32,1,2], target = 12", "output": "2"}],
        constraints=["1 <= nums.length <= 1000", "1 <= target <= 10^9"],
        function_name="minOperations",
        starter_code="def minOperations(nums: list[int], target: int) -> int:\n    pass\n",
        solution_code="def minOperations(nums: list[int], target: int) -> int:\n    if sum(nums) < target: return -1\n    from collections import Counter\n    counts = Counter(nums)\n    ops = 0\n    i = 0\n    while i < 31:\n        if (target >> i) & 1:\n            if counts[1 << i] > 0:\n                counts[1 << i] -= 1\n            else:\n                j = i\n                while j < 31 and counts[1 << j] == 0:\n                    j += 1\n                counts[1 << j] -= 1\n                for k in range(j, i, -1):\n                    counts[1 << (k - 1)] += 2\n                    ops += 1\n                counts[1 << i] -= 1\n        counts[1 << (i + 1)] += counts[1 << i] // 2\n        i += 1\n    return ops\n",
        test_cases=[{"input": [[1, 2, 8], 7], "expected": 1}, {"input": [[1, 32, 1, 2], 12], "expected": 2}],
        hints=["Simulate bit by bit from bit 0 to 30. If bit i is set in target, satisfy it with power 2^i or split the smallest available power 2^j > 2^i."],
        leetcode_id=2835
    ))

    # 67. Count Number of Teams
    problems.append(make_problem(
        pid="bit-m-count-number-of-teams", title="Count Number of Teams (Binary Indexed Tree / Triplet)",
        wing_id="bit-manipulation", floor=567, difficulty="medium", visualizer_type="array",
        monster_name="Regiment Archon", monster_title="Counter of Strictly Monotonic Trios",
        monster_sprite="gargoyle", monster_color="#f59e0b", monster_attack="Formation Surge",
        monster_quote="Triplets (i < j < k) where rating[i] < rating[j] < rating[k] (or reversed) counted!",
        description="There are `n` soldiers standing in a line. Each soldier is assigned a unique `rating` value. A team of 3 soldiers `(i, j, k)` is valid if: `(rating[i] < rating[j] < rating[k])` or `(rating[i] > rating[j] > rating[k])` with `0 <= i < j < k < n`. Return the number of teams you can form.",
        examples=[{"input": "rating = [2,5,3,4,1]", "output": "3"}, {"input": "rating = [2,1,3]", "output": "0"}],
        constraints=["n == rating.length", "3 <= n <= 1000"],
        function_name="numTeams",
        starter_code="def numTeams(rating: list[int]) -> int:\n    pass\n",
        solution_code="def numTeams(rating: list[int]) -> int:\n    n = len(rating)\n    ans = 0\n    for j in range(1, n - 1):\n        left_less = sum(1 for i in range(j) if rating[i] < rating[j])\n        left_greater = j - left_less\n        right_less = sum(1 for k in range(j + 1, n) if rating[k] < rating[j])\n        right_greater = (n - 1 - j) - right_less\n        ans += left_less * right_greater + left_greater * right_less\n    return ans\n",
        test_cases=[{"input": [[2, 5, 3, 4, 1]], "expected": 3}, {"input": [[2, 1, 3]], "expected": 0}],
        hints=["Fix middle soldier j. Multiply counts of smaller on left by greater on right, and greater on left by smaller on right."],
        leetcode_id=1395
    ))

    # 68. Binary Prefix Divisible By 5
    problems.append(make_problem(
        pid="bit-m-binary-prefix-divisible-5", title="Binary Prefix Divisible By 5",
        wing_id="bit-manipulation", floor=568, difficulty="medium", visualizer_type="array",
        monster_name="Quintet Imp", monster_title="Tester of Modulo 5 Divisibility",
        monster_sprite="imp", monster_color="#06b6d4", monster_attack="Modulo Flare",
        monster_quote="Boolean prefix array where binary value is divisible by 5 generated!",
        description="You are given a binary array `nums`. We define `xi` as the number whose binary representation is the subarray `nums[0..i]`. Return an array of booleans `answer` where `answer[i]` is `True` if `xi` is divisible by 5.",
        examples=[{"input": "nums = [0,1,1]", "output": "[True,False,False]"}, {"input": "nums = [1,0,1]", "output": "[False,False,True]"}],
        constraints=["1 <= nums.length <= 100000"],
        function_name="prefixesDivBy5",
        starter_code="def prefixesDivBy5(nums: list[int]) -> list[bool]:\n    pass\n",
        solution_code="def prefixesDivBy5(nums: list[int]) -> list[bool]:\n    ans = []\n    val = 0\n    for b in nums:\n        val = ((val << 1) | b) % 5\n        ans.append(val == 0)\n    return ans\n",
        test_cases=[{"input": [[0, 1, 1]], "expected": [True, False, False]}, {"input": [[1, 0, 1]], "expected": [False, False, True]}],
        hints=["Maintain running value modulo 5: val = ((val << 1) | b) % 5."],
        leetcode_id=1018
    ))

    # 69. Bitwise AND of All Pairwise ORs
    problems.append(make_problem(
        pid="bit-m-and-of-pairwise-ors", title="Bitwise AND of All Subarray Ranges",
        wing_id="bit-manipulation", floor=569, difficulty="medium", visualizer_type="array",
        monster_name="Monotonic Bit Warden", monster_title="Consolidator of Subarray Bitwise Masks",
        monster_sprite="boss", monster_color="#8b5cf6", monster_attack="Universal AND",
        monster_quote="Combined AND of all contiguous subarray ORs computed!",
        description="Given an integer array `nums`, return the bitwise AND of all elements in `nums`.",
        examples=[{"input": "nums = [1,2,3]", "output": "0"}, {"input": "nums = [7,15,31]", "output": "7"}],
        constraints=["1 <= nums.length <= 100000"],
        function_name="bitwiseAndAll",
        starter_code="def bitwiseAndAll(nums: list[int]) -> int:\n    pass\n",
        solution_code="def bitwiseAndAll(nums: list[int]) -> int:\n    ans = nums[0]\n    for x in nums[1:]: ans &= x\n    return ans\n",
        test_cases=[{"input": [[1, 2, 3]], "expected": 0}, {"input": [[7, 15, 31]], "expected": 7}],
        hints=["A bit is 1 in the bitwise AND of all subarrays if and only if it is set in every element."],
        leetcode_id=0
    ))

    # 70. Find the Longest Substring Containing Vowels (Compact Binary Hash)
    problems.append(make_problem(
        pid="bit-m-vowel-parity-state", title="State Bitmask of Vowel Parity",
        wing_id="bit-manipulation", floor=570, difficulty="medium", visualizer_type="array",
        monster_name="Vocal Harmony Sentinel", monster_title="Watcher of All-Even Vowel Parities",
        monster_sprite="boss", monster_color="#38bdf8", monster_attack="Harmonic Pulse",
        monster_quote="Smallest index where 5-vowel parity mask resets to zero!",
        description="Given a string `s`, return the index of the first character where all 5 vowels ('a', 'e', 'i', 'o', 'u') up to that index have appeared an even number of times (including zero). If never, return -1.",
        examples=[{"input": "s = \"aaeioou\"", "output": "1"}, {"input": "s = \"aeiou\"", "output": "-1"}],
        constraints=["1 <= s.length <= 10000"],
        function_name="firstEvenVowelIndex",
        starter_code="def firstEvenVowelIndex(s: str) -> int:\n    pass\n",
        solution_code="def firstEvenVowelIndex(s: str) -> int:\n    vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}\n    mask = 0\n    for i, ch in enumerate(s):\n        if ch in vowels:\n            mask ^= (1 << vowels[ch])\n        if mask == 0:\n            return i\n    return -1\n",
        test_cases=[{"input": ["aaeioou"], "expected": 1}, {"input": ["aeiou"], "expected": -1}],
        hints=["Track 5-bit vowel parity mask. Return first index i where mask == 0."],
        leetcode_id=0
    ))

    return problems
