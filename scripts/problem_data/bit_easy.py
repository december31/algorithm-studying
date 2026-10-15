"""
Bit Manipulation Easy Problems (Floors 501-510 - 10 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_bit_easy():
    problems = []

    # 1. Single Number
    problems.append(make_problem(
        pid="bit-e-single-number", title="Single Number (XOR Cancellation)",
        wing_id="bit-manipulation", floor=501, difficulty="easy", visualizer_type="array",
        monster_name="XOR Goblin", monster_title="Canceler of Identical Pairs",
        monster_sprite="goblin", monster_color="#38bdf8", monster_attack="Null Pulse",
        monster_quote="Every paired number cancels to zero, leaving the solitary integer!",
        description="Given a non-empty array of integers `nums`, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space.",
        examples=[{"input": "nums = [2,2,1]", "output": "1"}, {"input": "nums = [4,1,2,1,2]", "output": "4"}, {"input": "nums = [1]", "output": "1"}],
        constraints=["1 <= nums.length <= 30000"],
        function_name="singleNumber",
        starter_code="def singleNumber(nums: list[int]) -> int:\n    pass\n",
        solution_code="def singleNumber(nums: list[int]) -> int:\n    ans = 0\n    for x in nums:\n        ans ^= x\n    return ans\n",
        test_cases=[{"input": [[2, 2, 1]], "expected": 1}, {"input": [[4, 1, 2, 1, 2]], "expected": 4}, {"input": [[1]], "expected": 1}],
        hints=["XOR of any number with itself is 0 (a ^ a = 0). XOR of any number with 0 is itself (a ^ 0 = a)."],
        leetcode_id=136
    ))

    # 2. Number of 1 Bits
    problems.append(make_problem(
        pid="bit-e-number-of-1-bits", title="Number of 1 Bits (Hamming Weight)",
        wing_id="bit-manipulation", floor=502, difficulty="easy", visualizer_type="array",
        monster_name="Binary Imp", monster_title="Counter of Set Bits",
        monster_sprite="imp", monster_color="#10b981", monster_attack="Bit Spark",
        monster_quote="Hamming weight (number of set 1-bits) computed!",
        description="Write a function that takes the binary representation of a positive integer and returns the number of set bits it has (also known as the Hamming weight).",
        examples=[{"input": "n = 11", "output": "3"}, {"input": "n = 128", "output": "1"}, {"input": "n = 2147483645", "output": "30"}],
        constraints=["1 <= n <= 2^31 - 1"],
        function_name="hammingWeight",
        starter_code="def hammingWeight(n: int) -> int:\n    pass\n",
        solution_code="def hammingWeight(n: int) -> int:\n    count = 0\n    while n > 0:\n        n &= (n - 1)\n        count += 1\n    return count\n",
        test_cases=[{"input": [11], "expected": 3}, {"input": [128], "expected": 1}, {"input": [2147483645], "expected": 30}],
        hints=["Brian Kernighan's trick: `n &= (n - 1)` clears the lowest set bit in O(1)."],
        leetcode_id=191
    ))

    # 3. Counting Bits
    problems.append(make_problem(
        pid="bit-e-counting-bits", title="Counting Bits (DP Power of 2)",
        wing_id="bit-manipulation", floor=503, difficulty="easy", visualizer_type="array",
        monster_name="Bit Array Spectre", monster_title="Weaver of Prefix Hamming Weights",
        monster_sprite="spectre", monster_color="#8b5cf6", monster_attack="Bit Array Surge",
        monster_quote="Array of 1-bit counts for all integers 0 to n generated!",
        description="Given an integer `n`, return an array `ans` of length `n + 1` such that for each `i` (`0 <= i <= n`), `ans[i]` is the number of `1`'s in the binary representation of `i`.",
        examples=[{"input": "n = 2", "output": "[0,1,1]"}, {"input": "n = 5", "output": "[0,1,1,2,1,2]"}],
        constraints=["0 <= n <= 100000"],
        function_name="countBits",
        starter_code="def countBits(n: int) -> list[int]:\n    pass\n",
        solution_code="def countBits(n: int) -> list[int]:\n    ans = [0] * (n + 1)\n    for i in range(1, n + 1):\n        ans[i] = ans[i >> 1] + (i & 1)\n    return ans\n",
        test_cases=[{"input": [2], "expected": [0, 1, 1]}, {"input": [5], "expected": [0, 1, 1, 2, 1, 2]}, {"input": [0], "expected": [0]}],
        hints=["ans[i] = ans[i >> 1] + (i & 1)."],
        leetcode_id=338
    ))

    # 4. Reverse Bits
    problems.append(make_problem(
        pid="bit-e-reverse-bits", title="Reverse Bits (32-bit Integer)",
        wing_id="bit-manipulation", floor=504, difficulty="easy", visualizer_type="array",
        monster_name="Mirror Wraith", monster_title="Inverter of 32-bit Words",
        monster_sprite="wraith", monster_color="#ec4899", monster_attack="Mirror Inversion",
        monster_quote="All 32 binary bits mirrored end to end!",
        description="Reverse bits of a given 32 bits unsigned integer.",
        examples=[{"input": "n = 43261596", "output": "964176192"}],
        constraints=["n is a 32-bit unsigned integer"],
        function_name="reverseBits",
        starter_code="def reverseBits(n: int) -> int:\n    pass\n",
        solution_code="def reverseBits(n: int) -> int:\n    res = 0\n    for _ in range(32):\n        res = (res << 1) | (n & 1)\n        n >>= 1\n    return res\n",
        test_cases=[{"input": [43261596], "expected": 964176192}],
        hints=["Extract lowest bit of n with (n & 1), shift into result with (res << 1), and shift n right."],
        leetcode_id=190
    ))

    # 5. Missing Number
    problems.append(make_problem(
        pid="bit-e-missing-number", title="Missing Number (Index XOR)",
        wing_id="bit-manipulation", floor=505, difficulty="easy", visualizer_type="array",
        monster_name="Void Imp", monster_title="Eater of Single Permutation Elements",
        monster_sprite="imp", monster_color="#f59e0b", monster_attack="Omission Flash",
        monster_quote="The sole missing number in range [0, n] identified!",
        description="Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.",
        examples=[{"input": "nums = [3,0,1]", "output": "2"}, {"input": "nums = [0,1]", "output": "2"}, {"input": "nums = [9,6,4,2,3,5,7,0,1]", "output": "8"}],
        constraints=["n == nums.length", "1 <= n <= 10000"],
        function_name="missingNumber",
        starter_code="def missingNumber(nums: list[int]) -> int:\n    pass\n",
        solution_code="def missingNumber(nums: list[int]) -> int:\n    ans = len(nums)\n    for i, x in enumerate(nums):\n        ans ^= i ^ x\n    return ans\n",
        test_cases=[{"input": [[3, 0, 1]], "expected": 2}, {"input": [[0, 1]], "expected": 2}, {"input": [[9, 6, 4, 2, 3, 5, 7, 0, 1]], "expected": 8}],
        hints=["XOR all indices 0..n and all array values. The duplicate pairs cancel, leaving the missing number."],
        leetcode_id=268
    ))

    # 6. Power of Two
    problems.append(make_problem(
        pid="bit-e-power-of-two", title="Power of Two (Single Set Bit)",
        wing_id="bit-manipulation", floor=506, difficulty="easy", visualizer_type="array",
        monster_name="Binary Sentinel", monster_title="Guardian of Solitary Bits",
        monster_sprite="boss", monster_color="#ef4444", monster_attack="Power Beam",
        monster_quote="Is n a power of two verified in O(1) bit operations?",
        description="Given an integer `n`, return `True` if it is a power of two. Otherwise, return `False`.",
        examples=[{"input": "n = 1", "output": "True"}, {"input": "n = 16", "output": "True"}, {"input": "n = 3", "output": "False"}],
        constraints=["-2^31 <= n <= 2^31 - 1"],
        function_name="isPowerOfTwo",
        starter_code="def isPowerOfTwo(n: int) -> bool:\n    pass\n",
        solution_code="def isPowerOfTwo(n: int) -> bool:\n    return n > 0 and (n & (n - 1)) == 0\n",
        test_cases=[{"input": [1], "expected": True}, {"input": [16], "expected": True}, {"input": [3], "expected": False}, {"input": [0], "expected": False}],
        hints=["A positive integer n is a power of two if and only if n & (n - 1) == 0."],
        leetcode_id=231
    ))

    # 7. Power of Four
    problems.append(make_problem(
        pid="bit-e-power-of-four", title="Power of Four (Even Bit Mask)",
        wing_id="bit-manipulation", floor=507, difficulty="easy", visualizer_type="array",
        monster_name="Quaternary Fiend", monster_title="Watcher of Even Bit Positions",
        monster_sprite="demon", monster_color="#06b6d4", monster_attack="Quaternary Burst",
        monster_quote="Power of four verified with even-index bitmask 0x55555555!",
        description="Given an integer `n`, return `True` if it is a power of four. Otherwise, return `False`.",
        examples=[{"input": "n = 16", "output": "True"}, {"input": "n = 5", "output": "False"}, {"input": "n = 1", "output": "True"}],
        constraints=["-2^31 <= n <= 2^31 - 1"],
        function_name="isPowerOfFour",
        starter_code="def isPowerOfFour(n: int) -> bool:\n    pass\n",
        solution_code="def isPowerOfFour(n: int) -> bool:\n    return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0\n",
        test_cases=[{"input": [16], "expected": True}, {"input": [5], "expected": False}, {"input": [1], "expected": True}, {"input": [8], "expected": False}],
        hints=["Must be a power of two, and the single 1-bit must be located at an even bit position (mask 0x55555555)."],
        leetcode_id=342
    ))

    # 8. Hamming Distance
    problems.append(make_problem(
        pid="bit-e-hamming-distance", title="Hamming Distance",
        wing_id="bit-manipulation", floor=508, difficulty="easy", visualizer_type="array",
        monster_name="Disparity Imp", monster_title="Counter of Differing Bit Positions",
        monster_sprite="imp", monster_color="#38bdf8", monster_attack="XOR Disparity",
        monster_quote="Number of bit positions where x and y differ computed!",
        description="The Hamming distance between two integers is the number of positions at which the corresponding bits are different. Given two integers `x` and `y`, return the Hamming distance between them.",
        examples=[{"input": "x = 1, y = 4", "output": "2"}, {"input": "x = 3, y = 1", "output": "1"}],
        constraints=["0 <= x, y <= 2^31 - 1"],
        function_name="hammingDistance",
        starter_code="def hammingDistance(x: int, y: int) -> int:\n    pass\n",
        solution_code="def hammingDistance(x: int, y: int) -> int:\n    xor = x ^ y\n    count = 0\n    while xor > 0:\n        xor &= (xor - 1)\n        count += 1\n    return count\n",
        test_cases=[{"input": [1, 4], "expected": 2}, {"input": [3, 1], "expected": 1}],
        hints=["Compute x ^ y to isolate differing bits, then count set bits."],
        leetcode_id=461
    ))

    # 9. Add Binary
    problems.append(make_problem(
        pid="bit-e-add-binary", title="Add Binary Strings",
        wing_id="bit-manipulation", floor=509, difficulty="easy", visualizer_type="array",
        monster_name="Carry Golem", monster_title="Propagator of Binary Carries",
        monster_sprite="golem", monster_color="#f59e0b", monster_attack="Carry Shock",
        monster_quote="Sum of two binary strings computed with carry logic!",
        description="Given two binary strings `a` and `b`, return their sum as a binary string.",
        examples=[{"input": "a = \"11\", b = \"1\"", "output": "\"100\""}, {"input": "a = \"1010\", b = \"1011\"", "output": "\"10101\""}],
        constraints=["1 <= a.length, b.length <= 10000", "a and b consist only of '0' or '1' characters"],
        function_name="addBinary",
        starter_code="def addBinary(a: str, b: str) -> str:\n    pass\n",
        solution_code="def addBinary(a: str, b: str) -> str:\n    i, j = len(a) - 1, len(b) - 1\n    carry = 0\n    res = []\n    while i >= 0 or j >= 0 or carry:\n        total = carry\n        if i >= 0:\n            total += int(a[i])\n            i -= 1\n        if j >= 0:\n            total += int(b[j])\n            j -= 1\n        res.append(str(total % 2))\n        carry = total // 2\n    return \"\".join(res[::-1])\n",
        test_cases=[{"input": ["11", "1"], "expected": "100"}, {"input": ["1010", "1011"], "expected": "10101"}],
        hints=["Simulate column addition from right to left with carry."],
        leetcode_id=67
    ))

    # 10. Binary Number with Alternating Bits
    problems.append(make_problem(
        pid="bit-e-alternating-bits", title="Binary Number with Alternating Bits",
        wing_id="bit-manipulation", floor=510, difficulty="easy", visualizer_type="array",
        monster_name="Alternation Sentinel", monster_title="Inspector of Adjacent Bit Flips",
        monster_sprite="boss", monster_color="#8b5cf6", monster_attack="Alternating Wave",
        monster_quote="Does n have strictly alternating bits without adjacent identical bits?",
        description="Given a positive integer `n`, check whether it has alternating bits: namely, if two adjacent bits will always have different values.",
        examples=[{"input": "n = 5", "output": "True"}, {"input": "n = 7", "output": "False"}, {"input": "n = 11", "output": "False"}],
        constraints=["1 <= n <= 2^31 - 1"],
        function_name="hasAlternatingBits",
        starter_code="def hasAlternatingBits(n: int) -> bool:\n    pass\n",
        solution_code="def hasAlternatingBits(n: int) -> bool:\n    x = n ^ (n >> 1)\n    return (x & (x + 1)) == 0\n",
        test_cases=[{"input": [5], "expected": True}, {"input": [7], "expected": False}, {"input": [11], "expected": False}],
        hints=["If n has alternating bits, n ^ (n >> 1) produces all 1s (like 111...1). Then x & (x + 1) == 0."],
        leetcode_id=693
    ))

    return problems
