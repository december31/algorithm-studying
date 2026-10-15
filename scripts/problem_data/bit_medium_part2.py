"""
Bit Manipulation Medium Problems - Part 2 (Floors 526 to 540 - 15 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_bit_medium_part2():
    problems = []

    # 26. Maximum XOR of Two Numbers in an Array
    problems.append(make_problem(
        pid="bit-m-max-xor-two-numbers", title="Maximum XOR of Two Numbers in Array",
        wing_id="bit-manipulation", floor=526, difficulty="medium", visualizer_type="array",
        monster_name="XOR Titan", monster_title="Maximizer of Opposite Bit Alignments",
        monster_sprite="titan", monster_color="#8b5cf6", monster_attack="Max XOR Smash",
        monster_quote="Maximum pairwise XOR value constructed bit by bit!",
        description="Given an integer array `nums`, return the maximum result of `nums[i] XOR nums[j]`, where `0 <= i <= j < n`.",
        examples=[{"input": "nums = [3,10,5,25,2,8]", "output": "28"}, {"input": "nums = [14,70,53,83,49,91,36,80,92,51,66,70]", "output": "127"}],
        constraints=["1 <= nums.length <= 200000", "0 <= nums[i] <= 2^31 - 1"],
        function_name="findMaximumXOR",
        starter_code="def findMaximumXOR(nums: list[int]) -> int:\n    pass\n",
        solution_code="def findMaximumXOR(nums: list[int]) -> int:\n    max_xor = 0\n    mask = 0\n    for i in range(31, -1, -1):\n        mask |= (1 << i)\n        prefixes = {num & mask for num in nums}\n        candidate = max_xor | (1 << i)\n        if any(candidate ^ p in prefixes for p in prefixes):\n            max_xor = candidate\n    return max_xor\n",
        test_cases=[{"input": [[3, 10, 5, 25, 2, 8]], "expected": 28}, {"input": [[14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70]], "expected": 127}],
        hints=["Bitwise greedy search from bit 31 down to 0 using prefix sets. Target candidate ^ prefix in prefixes."],
        leetcode_id=421
    ))

    # 27. Sum of Two Integers
    problems.append(make_problem(
        pid="bit-m-sum-two-integers-bitwise", title="Sum of Two Integers (Bitwise Full Adder)",
        wing_id="bit-manipulation", floor=527, difficulty="medium", visualizer_type="array",
        monster_name="Arithmetic Automaton", monster_title="Calculator Without Plus or Minus Operators",
        monster_sprite="golem", monster_color="#f59e0b", monster_attack="Adder Pulse",
        monster_quote="Addition executed using bitwise XOR and carry AND shifts!",
        description="Given two integers `a` and `b`, return the sum of the two integers without using the operators `+` and `-`.",
        examples=[{"input": "a = 1, b = 2", "output": "3"}, {"input": "a = 2, b = 3", "output": "5"}],
        constraints=["-1000 <= a, b <= 1000"],
        function_name="getSum",
        starter_code="def getSum(a: int, b: int) -> int:\n    pass\n",
        solution_code="def getSum(a: int, b: int) -> int:\n    MASK = 0xFFFFFFFF\n    MAX_INT = 0x7FFFFFFF\n    while b != 0:\n        carry = (a & b) << 1\n        a = (a ^ b) & MASK\n        b = carry & MASK\n    return a if a <= MAX_INT else ~(a ^ MASK)\n",
        test_cases=[{"input": [1, 2], "expected": 3}, {"input": [2, 3], "expected": 5}, {"input": [-1, 1], "expected": 0}],
        hints=["Simulate hardware adder: sum_without_carry = a ^ b, carry = (a & b) << 1."],
        leetcode_id=371
    ))

    # 28. Integer Replacement
    problems.append(make_problem(
        pid="bit-m-integer-replacement", title="Integer Replacement (Min Operations to 1)",
        wing_id="bit-manipulation", floor=528, difficulty="medium", visualizer_type="array",
        monster_name="Collatz Spectre", monster_title="Optimizer of Parity Reductions",
        monster_sprite="spectre", monster_color="#38bdf8", monster_attack="Parity Reduction",
        monster_quote="Minimum operations to reduce n to 1 with (n/2, n+1, n-1)!",
        description="Given a positive integer `n`, you can apply one of the following operations: 1. If `n` is even, replace `n` with `n / 2`. 2. If `n` is odd, replace `n` with either `n + 1` or `n - 1`. Return the minimum number of operations needed for `n` to become 1.",
        examples=[{"input": "n = 8", "output": "3"}, {"input": "n = 7", "output": "4"}, {"input": "n = 4", "output": "2"}],
        constraints=["1 <= n <= 2^31 - 1"],
        function_name="integerReplacement",
        starter_code="def integerReplacement(n: int) -> int:\n    pass\n",
        solution_code="def integerReplacement(n: int) -> int:\n    ops = 0\n    while n > 1:\n        if n % 2 == 0:\n            n //= 2\n        elif n == 3 or (n & 3) == 1:\n            n -= 1\n        else:\n            n += 1\n        ops += 1\n    return ops\n",
        test_cases=[{"input": [8], "expected": 3}, {"input": [7], "expected": 4}, {"input": [4], "expected": 2}],
        hints=["If n is odd, choose n + 1 or n - 1 to make the next number divisible by 4 (except when n == 3, choose n - 1)."],
        leetcode_id=397
    ))

    # 29. UTF-8 Validation
    problems.append(make_problem(
        pid="bit-m-utf8-validation", title="UTF-8 Validation (Byte Masking)",
        wing_id="bit-manipulation", floor=529, difficulty="medium", visualizer_type="array",
        monster_name="Encoding Sentinel", monster_title="Validator of Multi-Byte Byte Sequences",
        monster_sprite="boss", monster_color="#10b981", monster_attack="Byte Check",
        monster_quote="UTF-8 multi-byte encoding validity verified!",
        description="Given an integer array `data` representing the data, return whether it is a valid utf-8 encoding. A character in UTF8 can be from 1 to 4 bytes long.",
        examples=[{"input": "data = [197,130,1]", "output": "True"}, {"input": "data = [235,140,4]", "output": "False"}],
        constraints=["1 <= data.length <= 20000", "0 <= data[i] <= 255"],
        function_name="validUtf8",
        starter_code="def validUtf8(data: list[int]) -> bool:\n    pass\n",
        solution_code="def validUtf8(data: list[int]) -> bool:\n    remaining = 0\n    for byte in data:\n        byte &= 0xFF\n        if remaining == 0:\n            if (byte >> 7) == 0: continue\n            elif (byte >> 5) == 0b110: remaining = 1\n            elif (byte >> 4) == 0b1110: remaining = 2\n            elif (byte >> 3) == 0b11110: remaining = 3\n            else: return False\n        else:\n            if (byte >> 6) != 0b10: return False\n            remaining -= 1\n    return remaining == 0\n",
        test_cases=[{"input": [[197, 130, 1]], "expected": True}, {"input": [[235, 140, 4]], "expected": False}],
        hints=["Check leading bits of header byte: 0xxxxxxx (1 byte), 110xxxxx (2 bytes), 1110xxxx (3 bytes), 11110xxx (4 bytes). Continuation bytes start with 10xxxxxx."],
        leetcode_id=393
    ))

    # 30. Maximum XOR for Each Query
    problems.append(make_problem(
        pid="bit-m-max-xor-each-query", title="Maximum XOR for Each Query",
        wing_id="bit-manipulation", floor=530, difficulty="medium", visualizer_type="array",
        monster_name="Bitwise Inverter", monster_title="Maximizer of Fixed-Bit Range XOR",
        monster_sprite="imp", monster_color="#ef4444", monster_attack="Max Bit Inversion",
        monster_quote="Array of maximum k answers maximizing XOR with prefix values generated!",
        description="You are given a sorted array `nums` of `n` non-negative integers and an integer `maximumBit`. For each query, find `k < 2^maximumBit` such that `(nums[0] ^ ... ^ nums[last]) ^ k` is maximized. Then remove last element. Return the answers to all queries.",
        examples=[{"input": "nums = [0,1,1,3], maximumBit = 2", "output": "[0,3,2,3]"}, {"input": "nums = [2,3,4,7], maximumBit = 3", "output": "[5,2,6,5]"}],
        constraints=["1 <= nums.length <= 100000", "1 <= maximumBit <= 20"],
        function_name="getMaximumXor",
        starter_code="def getMaximumXor(nums: list[int], maximumBit: int) -> list[int]:\n    pass\n",
        solution_code="def getMaximumXor(nums: list[int], maximumBit: int) -> list[int]:\n    max_val = (1 << maximumBit) - 1\n    curr_xor = 0\n    for x in nums: curr_xor ^= x\n    res = []\n    for x in reversed(nums):\n        res.append(curr_xor ^ max_val)\n        curr_xor ^= x\n    return res\n",
        test_cases=[{"input": [[0, 1, 1, 3], 2], "expected": [0, 3, 2, 3]}, {"input": [[2, 3, 4, 7], 3], "expected": [5, 2, 6, 5]}],
        hints=["The optimal k is curr_xor ^ ((1 << maximumBit) - 1)."],
        leetcode_id=1829
    ))

    # 31. Count Number of Maximum Bitwise-OR Subsets
    problems.append(make_problem(
        pid="bit-m-count-max-or-subsets", title="Count Max Bitwise-OR Subsets",
        wing_id="bit-manipulation", floor=531, difficulty="medium", visualizer_type="array",
        monster_name="Saturation Fiend", monster_title="Accumulator of All-1 Bit Fields",
        monster_sprite="demon", monster_color="#ec4899", monster_attack="OR Saturation",
        monster_quote="Number of non-empty subsets achieving the theoretical maximum bitwise OR!",
        description="Given an integer array `nums`, find the maximum possible bitwise OR of a subset of `nums` and return the number of different non-empty subsets with the maximum bitwise OR.",
        examples=[{"input": "nums = [3,1]", "output": "2"}, {"input": "nums = [2,2,2]", "output": "7"}, {"input": "nums = [3,2,1,5]", "output": "6"}],
        constraints=["1 <= nums.length <= 16"],
        function_name="countMaxOrSubsets",
        starter_code="def countMaxOrSubsets(nums: list[int]) -> int:\n    pass\n",
        solution_code="def countMaxOrSubsets(nums: list[int]) -> int:\n    max_or = 0\n    for x in nums: max_or |= x\n    ans = [0]\n    def backtrack(idx, curr_or):\n        if idx == len(nums):\n            if curr_or == max_or: ans[0] += 1\n            return\n        backtrack(idx + 1, curr_or | nums[idx])\n        backtrack(idx + 1, curr_or)\n    backtrack(0, 0)\n    return ans[0]\n",
        test_cases=[{"input": [[3, 1]], "expected": 2}, {"input": [[2, 2, 2]], "expected": 7}, {"input": [[3, 2, 1, 5]], "expected": 6}],
        hints=["Max possible OR is the bitwise OR of all elements. Backtrack over 2^n subsets counting matches."],
        leetcode_id=2044
    ))

    # 32. Bitwise ORs of Subarrays
    problems.append(make_problem(
        pid="bit-m-bitwise-ors-subarrays", title="Bitwise ORs of Subarrays (Set Propagation)",
        wing_id="bit-manipulation", floor=532, difficulty="medium", visualizer_type="array",
        monster_name="Cumulative Hydra", monster_title="Expander of Monotonic OR Fronts",
        monster_sprite="gargoyle", monster_color="#06b6d4", monster_attack="OR Front",
        monster_quote="Number of distinct bitwise OR results from all continuous subarrays!",
        description="Given an integer array `arr`, return the number of distinct bitwise ORs of all the non-empty subarrays of `arr`.",
        examples=[{"input": "arr = [0]", "output": "1"}, {"input": "arr = [1,1,2]", "output": "3"}, {"input": "arr = [1,2,4]", "output": "6"}],
        constraints=["1 <= arr.length <= 50000", "0 <= arr[i] <= 10^9"],
        function_name="subarrayBitwiseORs",
        starter_code="def subarrayBitwiseORs(arr: list[int]) -> int:\n    pass\n",
        solution_code="def subarrayBitwiseORs(arr: list[int]) -> int:\n    ans = set()\n    curr = set()\n    for x in arr:\n        curr = {x | y for y in curr} | {x}\n        ans |= curr\n    return len(ans)\n",
        test_cases=[{"input": [[0]], "expected": 1}, {"input": [[1, 1, 2]], "expected": 3}, {"input": [[1, 2, 4]], "expected": 6}],
        hints=["Since an integer has at most 30 bits, curr set has size at most 30 at each step."],
        leetcode_id=898
    ))

    # 33. Concatenation of Consecutive Binary Numbers
    problems.append(make_problem(
        pid="bit-m-concatenated-binary", title="Concatenation of Consecutive Binary Numbers",
        wing_id="bit-manipulation", floor=533, difficulty="medium", visualizer_type="array",
        monster_name="Concatenation Wyrm", monster_title="Chainer of Binary Integer Representations",
        monster_sprite="dragon", monster_color="#8b5cf6", monster_attack="Binary Chain",
        monster_quote="Decimal value of 1..n concatenated binary representations modulo 10^9+7!",
        description="Given an integer `n`, return the decimal value of the binary string formed by concatenating the binary representations of `1` to `n` in order, modulo `10^9 + 7`.",
        examples=[{"input": "n = 1", "output": "1"}, {"input": "n = 3", "output": "27"}, {"input": "n = 12", "output": "505370210"}],
        constraints=["1 <= n <= 100000"],
        function_name="concatenatedBinary",
        starter_code="def concatenatedBinary(n: int) -> int:\n    pass\n",
        solution_code="def concatenatedBinary(n: int) -> int:\n    MOD = 10**9 + 7\n    ans = 0\n    length = 0\n    for i in range(1, n + 1):\n        # Check if i is a power of 2\n        if (i & (i - 1)) == 0:\n            length += 1\n        ans = ((ans << length) | i) % MOD\n    return ans\n",
        test_cases=[{"input": [1], "expected": 1}, {"input": [3], "expected": 27}, {"input": [12], "expected": 505379714}],
        hints=["The bit length increments whenever i is a power of 2 ((i & (i - 1)) == 0). Shift ans left by length and OR with i."],
        leetcode_id=1680
    ))

    # 34. Score After Flipping Matrix
    problems.append(make_problem(
        pid="bit-m-score-flipping-matrix", title="Score After Flipping Matrix (Row/Col Flips)",
        wing_id="bit-manipulation", floor=534, difficulty="medium", visualizer_type="grid",
        monster_name="Inversion Sovereign", monster_title="Maximizer of Binary Row Scores",
        monster_sprite="boss", monster_color="#f59e0b", monster_attack="Matrix Inversion",
        monster_quote="Maximum binary row score achieved after optimal row and column flips!",
        description="You are given an `m x n` binary matrix `grid`. A move consists of choosing any row or column and toggling each value. Every row of the matrix is interpreted as a binary number, and the score is the sum of these numbers. Return the highest possible score.",
        examples=[{"input": "grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]", "output": "39"}, {"input": "grid = [[0]]", "output": "1"}],
        constraints=["1 <= m, n <= 20"],
        function_name="matrixScore",
        starter_code="def matrixScore(grid: list[list[int]]) -> int:\n    pass\n",
        solution_code="def matrixScore(grid: list[list[int]]) -> int:\n    R, C = len(grid), len(grid[0])\n    # Flip any row whose first element is 0\n    for r in range(R):\n        if grid[r][0] == 0:\n            for c in range(C): grid[r][c] ^= 1\n    ans = 0\n    for c in range(C):\n        col_ones = sum(grid[r][c] for r in range(R))\n        best_ones = max(col_ones, R - col_ones)\n        ans += best_ones * (1 << (C - 1 - c))\n    return ans\n",
        test_cases=[{"input": [[[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]], "expected": 39}, {"input": [[[0]]], "expected": 1}],
        hints=["Ensure every row starts with 1 by flipping if needed. For subsequent columns, choose max(col_ones, R - col_ones)."],
        leetcode_id=861
    ))

    # 35. Minimum One Bit Operations to Make Integers Zero
    problems.append(make_problem(
        pid="bit-m-min-one-bit-operations-zero", title="Minimum One Bit Operations to Make Zero",
        wing_id="bit-manipulation", floor=535, difficulty="medium", visualizer_type="array",
        monster_name="Gray Code Demon", monster_title="Inverter of Gray Code Encoding",
        monster_sprite="demon", monster_color="#ef4444", monster_attack="Gray Inversion",
        monster_quote="Operations to reach 0 computed via inverse Gray code mapping!",
        description="Given an integer `n`, you must transform it into 0 using operations: flip the 0th bit, or flip the `(i+1)`-th bit if the `i`-th bit is 1 and all lower bits are 0. Return the minimum number of operations to transform `n` into `0`.",
        examples=[{"input": "n = 3", "output": "2"}, {"input": "n = 6", "output": "4"}],
        constraints=["0 <= n <= 10^9"],
        function_name="minimumOneBitOperations",
        starter_code="def minimumOneBitOperations(n: int) -> int:\n    pass\n",
        solution_code="def minimumOneBitOperations(n: int) -> int:\n    ans = 0\n    while n > 0:\n        ans ^= n\n        n >>= 1\n    return ans\n",
        test_cases=[{"input": [3], "expected": 2}, {"input": [6], "expected": 4}, {"input": [0], "expected": 0}],
        hints=["This problem is equivalent to converting from Gray code back to standard binary: ans ^= (n >> shift)."],
        leetcode_id=1611
    ))

    # 36. Circular Permutation in Binary Representation
    problems.append(make_problem(
        pid="bit-m-circular-permutation-binary", title="Circular Permutation in Binary Representation",
        wing_id="bit-manipulation", floor=536, difficulty="medium", visualizer_type="array",
        monster_name="Orbital Specter", monster_title="Rotator of the Gray Ring",
        monster_sprite="spectre", monster_color="#38bdf8", monster_attack="Orbital Shift",
        monster_quote="Circular single-bit permutation starting from given start integer!",
        description="Given 2 integers `n` and `start`. A circular permutation `p` of length `2^n` satisfies: `p[0] == start`, adjacent elements differ by 1 bit, and first and last elements differ by 1 bit. Return the permutation.",
        examples=[{"input": "n = 2, start = 3", "output": "[3,2,0,1]"}, {"input": "n = 3, start = 2", "output": "[2,6,7,5,4,0,1,3]"}],
        constraints=["1 <= n <= 16", "0 <= start < 2^n"],
        function_name="circularPermutation",
        starter_code="def circularPermutation(n: int, start: int) -> list[int]:\n    pass\n",
        solution_code="def circularPermutation(n: int, start: int) -> list[int]:\n    return [start ^ (i ^ (i >> 1)) for i in range(1 << n)]\n",
        test_cases=[{"input": [2, 3], "expected": [3, 2, 0, 1]}, {"input": [3, 2], "expected": [2, 3, 1, 0, 4, 5, 7, 6]}],
        hints=["XOR every element of the standard Gray code sequence with `start`."],
        leetcode_id=1238
    ))

    # 37. Find Kth Bit in Nth Binary String
    problems.append(make_problem(
        pid="bit-m-find-kth-bit-binary-string", title="Find Kth Bit in Nth Binary String",
        wing_id="bit-manipulation", floor=537, difficulty="medium", visualizer_type="array",
        monster_name="Fractal Sphinx", monster_title="Oracle of the Inverted Recursive String",
        monster_sprite="sphinx", monster_color="#10b981", monster_attack="Fractal Inversion",
        monster_quote="The k-th bit of recursive string S_n isolated!",
        description="Given two positive integers `n` and `k`, the binary string `Sn` is formed as: `S1 = \"0\"`, `Si = S_{i-1} + \"1\" + reverse(invert(S_{i-1}))`. Return the `k`-th bit in `Sn`.",
        examples=[{"input": "n = 3, k = 1", "output": "\"0\""}, {"input": "n = 4, k = 11", "output": "\"1\""}],
        constraints=["1 <= n <= 20", "1 <= k <= 2^n - 1"],
        function_name="findKthBit",
        starter_code="def findKthBit(n: int, k: int) -> str:\n    pass\n",
        solution_code="def findKthBit(n: int, k: int) -> str:\n    if n == 1: return \"0\"\n    length = (1 << n) - 1\n    mid = (length + 1) // 2\n    if k == mid: return \"1\"\n    elif k < mid: return findKthBit(n - 1, k)\n    else:\n        bit = findKthBit(n - 1, length - k + 1)\n        return \"1\" if bit == \"0\" else \"0\"\n",
        test_cases=[{"input": [3, 1], "expected": "0"}, {"input": [4, 11], "expected": "1"}],
        hints=["Use divide and conquer: mid is always '1'. If k > mid, mirror position and invert."],
        leetcode_id=1545
    ))

    # 38. Longest Subarray With Maximum Bitwise AND
    problems.append(make_problem(
        pid="bit-m-longest-subarray-max-and", title="Longest Subarray with Maximum Bitwise AND",
        wing_id="bit-manipulation", floor=538, difficulty="medium", visualizer_type="array",
        monster_name="AND Peak Fiend", monster_title="Seeker of Max Contiguous Value Runs",
        monster_sprite="imp", monster_color="#f59e0b", monster_attack="Max AND Stride",
        monster_quote="Longest contiguous run of the maximum array value found!",
        description="Given an integer array `nums`. Consider the maximum possible bitwise AND of a subarray of `nums`. Return the length of the longest subarray that has this maximum bitwise AND.",
        examples=[{"input": "nums = [1,2,3,3,2,2]", "output": "2"}, {"input": "nums = [1,2,3,4]", "output": "1"}],
        constraints=["1 <= nums.length <= 100000"],
        function_name="longestSubarray",
        starter_code="def longestSubarray(nums: list[int]) -> int:\n    pass\n",
        solution_code="def longestSubarray(nums: list[int]) -> int:\n    max_val = max(nums)\n    max_len = curr_len = 0\n    for x in nums:\n        if x == max_val:\n            curr_len += 1\n            max_len = max(max_len, curr_len)\n        else:\n            curr_len = 0\n    return max_len\n",
        test_cases=[{"input": [[1, 2, 3, 3, 2, 2]], "expected": 2}, {"input": [[1, 2, 3, 4]], "expected": 1}],
        hints=["The maximum possible bitwise AND of any subarray is simply max(nums). Find the longest consecutive run of max(nums)."],
        leetcode_id=2419
    ))

    # 39. Smallest Subarrays With Maximum Bitwise OR
    problems.append(make_problem(
        pid="bit-m-smallest-subarrays-max-or", title="Smallest Subarrays with Maximum Bitwise OR",
        wing_id="bit-manipulation", floor=539, difficulty="medium", visualizer_type="array",
        monster_name="Bit Reach Archon", monster_title="Surveyor of Rightward Bit Frontiers",
        monster_sprite="wraith", monster_color="#06b6d4", monster_attack="Reach Flare",
        monster_quote="Shortest subarray starting at index i achieving maximum possible OR!",
        description="Given a 0-indexed array `nums` of `n` non-negative integers. Return an integer array `answer` of size `n` where `answer[i]` is the length of the shortest non-empty subarray starting at index `i` with maximum possible bitwise OR.",
        examples=[{"input": "nums = [1,0,2,1,3]", "output": "[3,3,2,2,1]"}, {"input": "nums = [1,2]", "output": "[2,1]"}],
        constraints=["1 <= nums.length <= 100000"],
        function_name="smallestSubarrays",
        starter_code="def smallestSubarrays(nums: list[int]) -> list[int]:\n    pass\n",
        solution_code="def smallestSubarrays(nums: list[int]) -> list[int]:\n    n = len(nums)\n    last_pos = [-1] * 32\n    ans = [1] * n\n    for i in range(n - 1, -1, -1):\n        for b in range(32):\n            if (nums[i] >> b) & 1:\n                last_pos[b] = i\n        max_reach = max([last_pos[b] for b in range(32) if last_pos[b] != -1], default=i)\n        ans[i] = max(1, max_reach - i + 1)\n    return ans\n",
        test_cases=[{"input": [[1, 0, 2, 1, 3]], "expected": [3, 3, 2, 2, 1]}, {"input": [[1, 2]], "expected": [2, 1]}],
        hints=["Iterate from right to left tracking the last seen index of each bit 0..31."],
        leetcode_id=2411
    ))

    # 40. Minimum Flips to Reverse Bit String
    problems.append(make_problem(
        pid="bit-m-min-bit-flips-alternating", title="Min Flips to Make Binary String Alternating",
        wing_id="bit-manipulation", floor=540, difficulty="medium", visualizer_type="array",
        monster_name="Chrono Flipping Imp", monster_title="Rotator of Type 1 and Type 2 Flips",
        monster_sprite="imp", monster_color="#8b5cf6", monster_attack="Type-2 Inversion",
        monster_quote="Minimum Type-2 character flips to make string alternating under cyclic shifts!",
        description="Given a binary string `s`. You are allowed to: 1. Move first character to end. 2. Flip any '0' to '1' or '1' to '0'. Return the minimum number of Type-2 flips to make `s` alternating.",
        examples=[{"input": "s = \"111000\"", "output": "2"}, {"input": "s = \"010\"", "output": "0"}, {"input": "s = \"1110\"", "output": "1"}],
        constraints=["1 <= s.length <= 100000"],
        function_name="minFlipsAlternating",
        starter_code="def minFlipsAlternating(s: str) -> int:\n    pass\n",
        solution_code="def minFlipsAlternating(s: str) -> int:\n    n = len(s)\n    s2 = s + s\n    target1 = \"01\" * n\n    target2 = \"10\" * n\n    diff1 = diff2 = 0\n    ans = n\n    for i in range(2 * n):\n        if s2[i] != target1[i]: diff1 += 1\n        if s2[i] != target2[i]: diff2 += 1\n        if i >= n:\n            if s2[i - n] != target1[i - n]: diff1 -= 1\n            if s2[i - n] != target2[i - n]: diff2 -= 1\n        if i >= n - 1:\n            ans = min(ans, diff1, diff2)\n    return ans\n",
        test_cases=[{"input": ["111000"], "expected": 2}, {"input": ["010"], "expected": 0}, {"input": ["1110"], "expected": 1}],
        hints=["Double string to s + s to simulate cyclic rotations. Slide a window of length n comparing to \"010101...\" and \"101010...\"."],
        leetcode_id=1888
    ))

    return problems
