"""
Bit Manipulation Medium Problems - Part 1 (Floors 511 to 525 - 15 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_bit_medium_part1():
    problems = []

    # 11. Single Number II
    problems.append(make_problem(
        pid="bit-m-single-number-ii", title="Single Number II (Modulo 3 Bit Count)",
        wing_id="bit-manipulation", floor=511, difficulty="medium", visualizer_type="array",
        monster_name="Triad Golem", monster_title="Canceler of Triplicate Bits",
        monster_sprite="golem", monster_color="#8b5cf6", monster_attack="Triad Cleave",
        monster_quote="Single number appearing once amid elements appearing three times found!",
        description="Given an integer array `nums` where every element appears three times except for one, which appears exactly once. Find the single element and return it.",
        examples=[{"input": "nums = [2,2,3,2]", "output": "3"}, {"input": "nums = [0,1,0,1,0,1,99]", "output": "99"}],
        constraints=["1 <= nums.length <= 30000", "-2^31 <= nums[i] <= 2^31 - 1"],
        function_name="singleNumberII",
        starter_code="def singleNumberII(nums: list[int]) -> int:\n    pass\n",
        solution_code="def singleNumberII(nums: list[int]) -> int:\n    ones = twos = 0\n    for x in nums:\n        ones = (ones ^ x) & ~twos\n        twos = (twos ^ x) & ~ones\n    return ones\n",
        test_cases=[{"input": [[2, 2, 3, 2]], "expected": 3}, {"input": [[0, 1, 0, 1, 0, 1, 99]], "expected": 99}, {"input": [[-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]], "expected": -4}],
        hints=["Digital logic state machine: track bits appearing 1 time (ones) and 2 times (twos). Modulo 3 resets both."],
        leetcode_id=137
    ))

    # 12. Single Number III
    problems.append(make_problem(
        pid="bit-m-single-number-iii", title="Single Number III (Two Solitary Elements)",
        wing_id="bit-manipulation", floor=512, difficulty="medium", visualizer_type="array",
        monster_name="Bifurcated Spectre", monster_title="Separator of the Two Solitary Souls",
        monster_sprite="spectre", monster_color="#ec4899", monster_attack="Bifurcation Beam",
        monster_quote="The two unique elements appearing exactly once separated and sorted!",
        description="Given an integer array `nums`, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once, returning them in ascending order.",
        examples=[{"input": "nums = [1,2,1,3,2,5]", "output": "[3,5]"}, {"input": "nums = [-1,0]", "output": "[-1,0]"}, {"input": "nums = [0,1]", "output": "[0,1]"}],
        constraints=["2 <= nums.length <= 30000"],
        function_name="singleNumberIII",
        starter_code="def singleNumberIII(nums: list[int]) -> list[int]:\n    pass\n",
        solution_code="def singleNumberIII(nums: list[int]) -> list[int]:\n    xor_all = 0\n    for x in nums: xor_all ^= x\n    diff_bit = xor_all & (-xor_all)\n    a = b = 0\n    for x in nums:\n        if x & diff_bit:\n            a ^= x\n        else:\n            b ^= x\n    return sorted([a, b])\n",
        test_cases=[{"input": [[1, 2, 1, 3, 2, 5]], "expected": [3, 5]}, {"input": [[-1, 0]], "expected": [-1, 0]}, {"input": [[0, 1]], "expected": [0, 1]}],
        hints=["XOR all numbers to get a ^ b. Find lowest differing bit (diff & -diff) and divide nums into two groups."],
        leetcode_id=260
    ))

    # 13. Bitwise AND of Numbers Range
    problems.append(make_problem(
        pid="bit-m-bitwise-and-range", title="Bitwise AND of Numbers Range",
        wing_id="bit-manipulation", floor=513, difficulty="medium", visualizer_type="array",
        monster_name="Range Void Imp", monster_title="Consumer of Non-Common Bit Suffixes",
        monster_sprite="imp", monster_color="#38bdf8", monster_attack="Suffix Cleave",
        monster_quote="Common bit prefix of left and right boundaries isolated!",
        description="Given two integers `left` and `right` that represent the range `[left, right]`, return the bitwise AND of all numbers in this range, inclusive.",
        examples=[{"input": "left = 5, right = 7", "output": "4"}, {"input": "left = 0, right = 0", "output": "0"}, {"input": "left = 1, right = 2147483647", "output": "0"}],
        constraints=["0 <= left <= right <= 2^31 - 1"],
        function_name="rangeBitwiseAnd",
        starter_code="def rangeBitwiseAnd(left: int, right: int) -> int:\n    pass\n",
        solution_code="def rangeBitwiseAnd(left: int, right: int) -> int:\n    shift = 0\n    while left < right:\n        left >>= 1\n        right >>= 1\n        shift += 1\n    return left << shift\n",
        test_cases=[{"input": [5, 7], "expected": 4}, {"input": [0, 0], "expected": 0}, {"input": [1, 2147483647], "expected": 0}],
        hints=["The result is simply the common binary prefix of left and right, with all lower bits zeroed."],
        leetcode_id=201
    ))

    # 14. Subsets via Bitmask
    problems.append(make_problem(
        pid="bit-m-subsets-bitmask", title="Subsets Generation (Bitmask Power Set)",
        wing_id="bit-manipulation", floor=514, difficulty="medium", visualizer_type="array",
        monster_name="Combinatorial Fiend", monster_title="Enumerator of the 2^N States",
        monster_sprite="demon", monster_color="#10b981", monster_attack="Power Set Cascade",
        monster_quote="All 2^N subsets generated using integer bitmasks 0 to 2^n - 1!",
        description="Given an integer array `nums` of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in sorted order.",
        examples=[{"input": "nums = [1,2,3]", "output": "[[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]]"}],
        constraints=["1 <= nums.length <= 10"],
        function_name="subsetsBitmask",
        starter_code="def subsetsBitmask(nums: list[int]) -> list[list[int]]:\n    pass\n",
        solution_code="def subsetsBitmask(nums: list[int]) -> list[list[int]]:\n    n = len(nums)\n    res = []\n    for mask in range(1 << n):\n        subset = [nums[i] for i in range(n) if (mask & (1 << i))]\n        res.append(subset)\n    return sorted(res)\n",
        test_cases=[{"input": [[1, 2, 3]], "expected": [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]}, {"input": [[0]], "expected": [[], [0]]}],
        hints=["Iterate mask from 0 to (1 << n) - 1. Include nums[i] if the i-th bit is set."],
        leetcode_id=78
    ))

    # 15. Gray Code
    problems.append(make_problem(
        pid="bit-m-gray-code-sequence", title="Gray Code (Single Bit Flips)",
        wing_id="bit-manipulation", floor=515, difficulty="medium", visualizer_type="array",
        monster_name="Reflected Code Archon", monster_title="Architect of Single-Bit Transitions",
        monster_sprite="wizard", monster_color="#f59e0b", monster_attack="Gray Pulse",
        monster_quote="N-bit Gray code sequence where successive values differ by exactly 1 bit!",
        description="An n-bit Gray code sequence is a sequence of `2^n` integers where: 1. Every integer is in the inclusive range `[0, 2^n - 1]`. 2. The first integer is 0. 3. The binary representation of adjacent integers differs by exactly one bit. Given an integer `n`, return any valid n-bit Gray code sequence.",
        examples=[{"input": "n = 2", "output": "[0,1,3,2]"}, {"input": "n = 1", "output": "[0,1]"}],
        constraints=["1 <= n <= 16"],
        function_name="grayCode",
        starter_code="def grayCode(n: int) -> list[int]:\n    pass\n",
        solution_code="def grayCode(n: int) -> list[int]:\n    return [i ^ (i >> 1) for i in range(1 << n)]\n",
        test_cases=[{"input": [2], "expected": [0, 1, 3, 2]}, {"input": [1], "expected": [0, 1]}],
        hints=["Direct formula: the i-th Gray code element is i ^ (i >> 1)."],
        leetcode_id=89
    ))

    # 16. Total Hamming Distance
    problems.append(make_problem(
        pid="bit-m-total-hamming-distance", title="Total Hamming Distance",
        wing_id="bit-manipulation", floor=516, difficulty="medium", visualizer_type="array",
        monster_name="Cross-Bit Colossus", monster_title="Accumulator of Bit Differentials",
        monster_sprite="golem", monster_color="#ef4444", monster_attack="Bit Matrix Slam",
        monster_quote="Sum of Hamming distances between all pairs of integers evaluated in O(32 * n)!",
        description="The Hamming distance between two integers is the number of positions at which the corresponding bits are different. Given an integer array `nums`, return the sum of Hamming distances between all the pairs of the integers in `nums`.",
        examples=[{"input": "nums = [4,14,2]", "output": "6"}, {"input": "nums = [4,14,4]", "output": "4"}],
        constraints=["1 <= nums.length <= 10000", "0 <= nums[i] <= 10^9"],
        function_name="totalHammingDistance",
        starter_code="def totalHammingDistance(nums: list[int]) -> int:\n    pass\n",
        solution_code="def totalHammingDistance(nums: list[int]) -> int:\n    total = 0\n    n = len(nums)\n    for bit in range(32):\n        ones = sum((x >> bit) & 1 for x in nums)\n        total += ones * (n - ones)\n    return total\n",
        test_cases=[{"input": [[4, 14, 2]], "expected": 6}, {"input": [[4, 14, 4]], "expected": 4}],
        hints=["Inspect each bit position independently: if `ones` numbers have a 1 and `n - ones` have a 0, they contribute ones * (n - ones)."],
        leetcode_id=477
    ))

    # 17. Maximum Product of Word Lengths
    problems.append(make_problem(
        pid="bit-m-max-product-word-lengths", title="Max Product of Word Lengths",
        wing_id="bit-manipulation", floor=517, difficulty="medium", visualizer_type="array",
        monster_name="Lexical Mask Sphinx", monster_title="Tester of Disjoint Alphabet Sets",
        monster_sprite="sphinx", monster_color="#06b6d4", monster_attack="Disjoint Flare",
        monster_quote="Maximum length product of two words sharing no common letters!",
        description="Given a string array `words`, return the maximum value of `length(word[i]) * length(word[j])` where the two words do not share common letters. If no such two words exist, return 0.",
        examples=[{"input": "words = [\"abcw\",\"baz\",\"foo\",\"bar\",\"xtfn\",\"abcdef\"]", "output": "16"}, {"input": "words = [\"a\",\"ab\",\"abc\",\"d\",\"cd\",\"bcd\",\"abcd\"]", "output": "4"}, {"input": "words = [\"a\",\"aa\",\"aaa\",\"aaaa\"]", "output": "0"}],
        constraints=["2 <= words.length <= 1000", "1 <= words[i].length <= 1000"],
        function_name="maxProduct",
        starter_code="def maxProduct(words: list[str]) -> int:\n    pass\n",
        solution_code="def maxProduct(words: list[str]) -> int:\n    masks = {}\n    for w in words:\n        mask = 0\n        for c in w: mask |= (1 << (ord(c) - ord('a')))\n        masks[mask] = max(masks.get(mask, 0), len(w))\n    max_prod = 0\n    for m1, len1 in masks.items():\n        for m2, len2 in masks.items():\n            if (m1 & m2) == 0:\n                max_prod = max(max_prod, len1 * len2)\n    return max_prod\n",
        test_cases=[{"input": [["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]], "expected": 16}, {"input": [["a", "ab", "abc", "d", "cd", "bcd", "abcd"]], "expected": 4}, {"input": [["a", "aa", "aaa", "aaaa"]], "expected": 0}],
        hints=["Encode character sets of each word as a 26-bit bitmask. Two words are disjoint if mask1 & mask2 == 0."],
        leetcode_id=318
    ))

    # 18. Repeated DNA Sequences
    problems.append(make_problem(
        pid="bit-m-repeated-dna-sequences", title="Repeated DNA Sequences (Bitmask Rolling Hash)",
        wing_id="bit-manipulation", floor=518, difficulty="medium", visualizer_type="array",
        monster_name="Genetic Spectre", monster_title="Extractor of Duplicate 10-mers",
        monster_sprite="wraith", monster_color="#10b981", monster_attack="Gene Duplication",
        monster_quote="10-letter nucleotide substrings appearing more than once identified!",
        description="The DNA sequence is composed of a series of nucleotides: 'A', 'C', 'G', and 'T'. Given a string `s` that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule in sorted order.",
        examples=[{"input": "s = \"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT\"", "output": "[\"AAAAACCCCC\",\"CCCCCAAAAA\"]"}, {"input": "s = \"AAAAAAAAAAAAA\"", "output": "[\"AAAAAAAAAA\"]"}],
        constraints=["1 <= s.length <= 100000"],
        function_name="findRepeatedDnaSequences",
        starter_code="def findRepeatedDnaSequences(s: str) -> list[str]:\n    pass\n",
        solution_code="def findRepeatedDnaSequences(s: str) -> list[str]:\n    if len(s) < 10: return []\n    mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}\n    seen = set()\n    repeated = set()\n    mask = 0\n    for i in range(9):\n        mask = (mask << 2) | mapping[s[i]]\n    for i in range(9, len(s)):\n        mask = ((mask << 2) & 0xFFFFF) | mapping[s[i]]\n        sub = s[i - 9:i + 1]\n        if mask in seen:\n            repeated.add(sub)\n        else:\n            seen.add(mask)\n    return sorted(list(repeated))\n",
        test_cases=[{"input": ["AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"], "expected": ["AAAAACCCCC", "CCCCCAAAAA"]}, {"input": ["AAAAAAAAAAAAA"], "expected": ["AAAAAAAAAA"]}],
        hints=["Represent each nucleotide as 2 bits ('A'=00, 'C'=01, 'G'=10, 'T'=11). A 10-mer fits in a 20-bit mask."],
        leetcode_id=187
    ))

    # 19. Count Triplets That Can Form Two Arrays of Equal XOR
    problems.append(make_problem(
        pid="bit-m-count-triplets-equal-xor", title="Count Triplets of Equal Subarray XOR",
        wing_id="bit-manipulation", floor=519, difficulty="medium", visualizer_type="array",
        monster_name="Tri-XOR Drake", monster_title="Balancing Equal XOR Partitions",
        monster_sprite="dragon", monster_color="#8b5cf6", monster_attack="Null Subarray Beam",
        monster_quote="Triplets (i < j <= k) where XOR(i..j-1) == XOR(j..k) counted!",
        description="Given an array of integers `arr`. We want to select three indices `i`, `j` and `k` with `0 <= i < j <= k < arr.length`. Where `a = arr[i] ^ ... ^ arr[j - 1]` and `b = arr[j] ^ ... ^ arr[k]`. Return the number of triplets such that `a == b`.",
        examples=[{"input": "arr = [2,3,1,6,7]", "output": "4"}, {"input": "arr = [1,1,1,1,1]", "output": "10"}],
        constraints=["1 <= arr.length <= 300"],
        function_name="countTriplets",
        starter_code="def countTriplets(arr: list[int]) -> int:\n    pass\n",
        solution_code="def countTriplets(arr: list[int]) -> int:\n    n = len(arr)\n    prefix = [0] * (n + 1)\n    for i in range(n): prefix[i + 1] = prefix[i] ^ arr[i]\n    count = 0\n    for i in range(n):\n        for k in range(i + 1, n):\n            if prefix[i] == prefix[k + 1]:\n                count += (k - i)\n    return count\n",
        test_cases=[{"input": [[2, 3, 1, 6, 7]], "expected": 4}, {"input": [[1, 1, 1, 1, 1]], "expected": 10}],
        hints=["a == b is equivalent to a ^ b == 0, which means prefix[i] == prefix[k + 1]. Any j between i+1 and k works (k - i choices)."],
        leetcode_id=1442
    ))

    # 20. Decode XORed Permutation
    problems.append(make_problem(
        pid="bit-m-decode-xored-permutation", title="Decode XORed Permutation",
        wing_id="bit-manipulation", floor=520, difficulty="medium", visualizer_type="array",
        monster_name="Decryption Archon", monster_title="Reconstructor of the 1 to N Permutation",
        monster_sprite="boss", monster_color="#ef4444", monster_attack="Decryption Ray",
        monster_quote="Original permutation of [1, n] decoded from adjacent XOR differences!",
        description="There is an integer array `perm` that is a permutation of the first `n` positive integers, where `n` is always odd. It was encoded into an array `encoded` of length `n - 1` where `encoded[i] = perm[i] ^ perm[i + 1]`. Given `encoded`, return original `perm`.",
        examples=[{"input": "encoded = [3,1]", "output": "[1,2,3]"}, {"input": "encoded = [6,5,4,6]", "output": "[2,4,1,5,3]"}],
        constraints=["3 <= encoded.length <= 100000", "encoded.length is even"],
        function_name="decode",
        starter_code="def decode(encoded: list[int]) -> list[int]:\n    pass\n",
        solution_code="def decode(encoded: list[int]) -> list[int]:\n    n = len(encoded) + 1\n    total_xor = 0\n    for i in range(1, n + 1): total_xor ^= i\n    odd_xor = 0\n    for i in range(1, len(encoded), 2):\n        odd_xor ^= encoded[i]\n    perm0 = total_xor ^ odd_xor\n    res = [perm0]\n    for x in encoded:\n        res.append(res[-1] ^ x)\n    return res\n",
        test_cases=[{"input": [[3, 1]], "expected": [1, 2, 3]}, {"input": [[6, 5, 4, 6]], "expected": [2, 4, 1, 5, 3]}],
        hints=["total_xor is XOR(1..n). XOR of encoded[1], encoded[3], ... gives XOR(perm[1..n-1]). Thus perm[0] = total_xor ^ odd_xor."],
        leetcode_id=1734
    ))

    # 21. XOR Queries of a Subarray
    problems.append(make_problem(
        pid="bit-m-xor-queries-subarray", title="XOR Queries of Subarrays (Prefix XOR)",
        wing_id="bit-manipulation", floor=521, difficulty="medium", visualizer_type="array",
        monster_name="Prefix Voidling", monster_title="Answerer of Range XOR Queries",
        monster_sprite="imp", monster_color="#38bdf8", monster_attack="Prefix Slash",
        monster_quote="Subarray XOR ranges answered in O(1) query time!",
        description="You are given an array `arr` of positive integers. You are also given the array `queries` where `queries[i] = [lefti, righti]`. For each query `i`, compute the XOR of elements from `lefti` to `righti`. Return an array containing the results.",
        examples=[{"input": "arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]", "output": "[2,7,14,8]"}],
        constraints=["1 <= arr.length, queries.length <= 30000"],
        function_name="xorQueries",
        starter_code="def xorQueries(arr: list[int], queries: list[list[int]]) -> list[int]:\n    pass\n",
        solution_code="def xorQueries(arr: list[int], queries: list[list[int]]) -> list[int]:\n    prefix = [0] * (len(arr) + 1)\n    for i, x in enumerate(arr): prefix[i + 1] = prefix[i] ^ x\n    return [prefix[r + 1] ^ prefix[l] for l, r in queries]\n",
        test_cases=[{"input": [[1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]], "expected": [2, 7, 14, 8]}],
        hints=["Compute prefix XOR: range XOR [L, R] is prefix[R + 1] ^ prefix[L]."],
        leetcode_id=1310
    ))

    # 22. Minimum Flips to Make a OR b Equal to c
    problems.append(make_problem(
        pid="bit-m-min-flips-or-equal-c", title="Minimum Flips to Make (a OR b == c)",
        wing_id="bit-manipulation", floor=522, difficulty="medium", visualizer_type="array",
        monster_name="Logic Gatekeeper", monster_title="Aligner of Binary OR Gates",
        monster_sprite="spectre", monster_color="#f59e0b", monster_attack="Bit Inversion",
        monster_quote="Minimum bit flips in a and b to satisfy a | b == c!",
        description="Given 3 positives numbers `a`, `b` and `c`. Return the minimum flips needed in some bits of `a` and to make `(a OR b == c)`. Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.",
        examples=[{"input": "a = 2, b = 6, c = 5", "output": "3"}, {"input": "a = 4, b = 2, c = 7", "output": "1"}, {"input": "a = 1, b = 2, c = 3", "output": "0"}],
        constraints=["1 <= a, b, c <= 10^9"],
        function_name="minFlips",
        starter_code="def minFlips(a: int, b: int, c: int) -> int:\n    pass\n",
        solution_code="def minFlips(a: int, b: int, c: int) -> int:\n    flips = 0\n    for i in range(32):\n        bit_a = (a >> i) & 1\n        bit_b = (b >> i) & 1\n        bit_c = (c >> i) & 1\n        if bit_c == 1:\n            if bit_a == 0 and bit_b == 0: flips += 1\n        else:\n            flips += bit_a + bit_b\n    return flips\n",
        test_cases=[{"input": [2, 6, 5], "expected": 3}, {"input": [4, 2, 7], "expected": 1}, {"input": [1, 2, 3], "expected": 0}],
        hints=["Examine each bit: if bit_c == 1 and neither a nor b has 1, add 1. If bit_c == 0, add bit_a + bit_b."],
        leetcode_id=1318
    ))

    # 23. Find The Original Array of Prefix XOR
    problems.append(make_problem(
        pid="bit-m-original-array-prefix-xor", title="Find Original Array from Prefix XOR",
        wing_id="bit-manipulation", floor=523, difficulty="medium", visualizer_type="array",
        monster_name="Inverse Prefix Drake", monster_title="Differentiator of Cumulative XOR",
        monster_sprite="dragon", monster_color="#06b6d4", monster_attack="Cumulative Slash",
        monster_quote="Original array reconstructed from prefix XOR values!",
        description="You are given an integer array `pref` of size `n`. Find and return the array `arr` of size `n` that satisfies: `pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]`. It can be proven that the answer is unique.",
        examples=[{"input": "pref = [5,2,0,3,1]", "output": "[5,7,2,3,2]"}, {"input": "pref = [13]", "output": "[13]"}],
        constraints=["1 <= pref.length <= 100000"],
        function_name="findArray",
        starter_code="def findArray(pref: list[int]) -> list[int]:\n    pass\n",
        solution_code="def findArray(pref: list[int]) -> list[int]:\n    res = [pref[0]]\n    for i in range(1, len(pref)):\n        res.append(pref[i] ^ pref[i - 1])\n    return res\n",
        test_cases=[{"input": [[5, 2, 0, 3, 1]], "expected": [5, 7, 2, 3, 2]}, {"input": [[13]], "expected": [13]}],
        hints=["Since pref[i] = pref[i - 1] ^ arr[i], XORing both sides by pref[i - 1] gives arr[i] = pref[i] ^ pref[i - 1]."],
        leetcode_id=2433
    ))

    # 24. Number of Steps to Reduce a Number in Binary to One
    problems.append(make_problem(
        pid="bit-m-steps-reduce-binary-to-one", title="Reduce Binary Representation to One",
        wing_id="bit-manipulation", floor=524, difficulty="medium", visualizer_type="array",
        monster_name="Binary Collatz Imp", monster_title="Reducer of Binary Strings",
        monster_sprite="imp", monster_color="#ec4899", monster_attack="Collatz Shift",
        monster_quote="Steps to reduce binary string to '1' using (if odd: +1, if even: /2)!",
        description="Given a binary string `s` representing an integer, return the number of steps to reduce it to 1 under rules: If current number is even, divide by 2. If odd, add 1.",
        examples=[{"input": "s = \"1101\"", "output": "6"}, {"input": "s = \"10\"", "output": "1"}, {"input": "s = \"1\"", "output": "0"}],
        constraints=["1 <= s.length <= 500"],
        function_name="numSteps",
        starter_code="def numSteps(s: str) -> int:\n    pass\n",
        solution_code="def numSteps(s: str) -> int:\n    carry = 0\n    steps = 0\n    for i in range(len(s) - 1, 0, -1):\n        digit = int(s[i]) + carry\n        if digit % 2 == 1:\n            steps += 2\n            carry = 1\n        else:\n            steps += 1\n    return steps + carry\n",
        test_cases=[{"input": ["1101"], "expected": 6}, {"input": ["10"], "expected": 1}, {"input": ["1"], "expected": 0}],
        hints=["Simulate backwards tracking carry: if current digit + carry is odd, +1 then /2 takes 2 steps and produces carry = 1."],
        leetcode_id=1404
    ))

    # 25. Minimum Bit Flips to Convert Number
    problems.append(make_problem(
        pid="bit-m-min-bit-flips-convert", title="Min Bit Flips to Convert Number",
        wing_id="bit-manipulation", floor=525, difficulty="medium", visualizer_type="array",
        monster_name="Transformation Wraith", monster_title="Morpher of Integer States",
        monster_sprite="wraith", monster_color="#10b981", monster_attack="Bit Morph",
        monster_quote="Minimum bit flips to transform start into goal!",
        description="A bit flip of a number `x` is choosing a bit in the binary representation of `x` and flipping it. Given two integers `start` and `goal`, return the minimum number of bit flips to convert `start` to `goal`.",
        examples=[{"input": "start = 10, goal = 7", "output": "3"}, {"input": "start = 3, goal = 4", "output": "3"}],
        constraints=["0 <= start, goal <= 10^9"],
        function_name="minBitFlips",
        starter_code="def minBitFlips(start: int, goal: int) -> int:\n    pass\n",
        solution_code="def minBitFlips(start: int, goal: int) -> int:\n    diff = start ^ goal\n    count = 0\n    while diff > 0:\n        diff &= (diff - 1)\n        count += 1\n    return count\n",
        test_cases=[{"input": [10, 7], "expected": 3}, {"input": [3, 4], "expected": 3}],
        hints=["The answer is the Hamming weight of (start ^ goal)."],
        leetcode_id=2220
    ))

    return problems
