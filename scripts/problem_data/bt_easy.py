"""
Backtracking Easy Problems (10 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_bt_easy():
    problems = []

    # 1. Binary Watch
    problems.append(make_problem(
        pid="bt-e-binary-watch", title="Binary Watch Illuminations",
        wing_id="backtracking", floor=201, difficulty="easy", visualizer_type="bits",
        monster_name="Chronos Imp", monster_title="Tinkerer of LED Dials",
        monster_sprite="goblin", monster_color="#eab308", monster_attack="LED Spark",
        monster_quote="My binary dials illuminated all matching timestamps!",
        description="A binary watch has 4 LEDs on the top to represent hours (0-11), and 6 LEDs on the bottom to represent minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right. Given an integer `turnedOn` which represents the number of LEDs that are currently on, return all possible times the watch could represent in sorted order.",
        examples=[{"input": "turnedOn = 1", "output": "[\"0:01\",\"0:02\",\"0:04\",\"0:08\",\"0:16\",\"0:32\",\"1:00\",\"2:00\",\"4:00\",\"8:00\"]"}, {"input": "turnedOn = 9", "output": "[]"}],
        constraints=["0 <= turnedOn <= 10"],
        function_name="readBinaryWatch",
        starter_code="def readBinaryWatch(turnedOn: int) -> list[str]:\n    pass\n",
        solution_code="def readBinaryWatch(turnedOn: int) -> list[str]:\n    res = []\n    for h in range(12):\n        for m in range(60):\n            if (bin(h).count('1') + bin(m).count('1')) == turnedOn:\n                res.append(f\"{h}:{m:02d}\")\n    return sorted(res)\n",
        test_cases=[{"input": [1], "expected": ["0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00", "4:00", "8:00"]}, {"input": [9], "expected": []}, {"input": [0], "expected": ["0:00"]}],
        hints=["Iterate over all valid hours (0-11) and minutes (0-59), checking if total set bits equals turnedOn."],
        leetcode_id=401
    ))

    # 2. Letter Case Permutation
    problems.append(make_problem(
        pid="bt-e-letter-case-permutation", title="Letter Case Permutation",
        wing_id="backtracking", floor=202, difficulty="easy", visualizer_type="array",
        monster_name="Case Shifter", monster_title="Twister of Capital Runes",
        monster_sprite="slime", monster_color="#06b6d4", monster_attack="Case Shift",
        monster_quote="Every branching casing path was explored recursively!",
        description="Given a string `s`, you can transform every letter individually to be lowercase or uppercase to create another string. Return a list of all possible strings we could create in lexicographical order.",
        examples=[{"input": "s = \"a1b2\"", "output": "[\"a1b2\",\"a1B2\",\"A1b2\",\"A1B2\"]"}, {"input": "s = \"3z4\"", "output": "[\"3z4\",\"3Z4\"]"}],
        constraints=["1 <= len(s) <= 12", "s consists of lowercase English letters, uppercase English letters, and digits"],
        function_name="letterCasePermutation",
        starter_code="def letterCasePermutation(s: str) -> list[str]:\n    pass\n",
        solution_code="def letterCasePermutation(s: str) -> list[str]:\n    res = []\n    def backtrack(idx, path):\n        if idx == len(s):\n            res.append(''.join(path))\n            return\n        if s[idx].isalpha():\n            backtrack(idx + 1, path + [s[idx].lower()])\n            backtrack(idx + 1, path + [s[idx].upper()])\n        else:\n            backtrack(idx + 1, path + [s[idx]])\n    backtrack(0, [])\n    return sorted(res)\n",
        test_cases=[{"input": ["a1b2"], "expected": ["A1B2", "A1b2", "a1B2", "a1b2"]}, {"input": ["3z4"], "expected": ["3Z4", "3z4"]}, {"input": ["123"], "expected": ["123"]}],
        hints=["Branch on letters with lower and upper cases; leave digits unchanged."],
        leetcode_id=784
    ))

    # 3. Sum of All Subset XOR Totals
    problems.append(make_problem(
        pid="bt-e-subset-xor-sum", title="Sum of All Subset XOR Totals",
        wing_id="backtracking", floor=203, difficulty="easy", visualizer_type="bits",
        monster_name="XOR Sprite", monster_title="Accumulator of Subsequence Bit Totals",
        monster_sprite="slime", monster_color="#8b5cf6", monster_attack="XOR Spark",
        monster_quote="Every subset's cumulative XOR sum was tallied!",
        description="The XOR total of an array is defined as the bitwise XOR of all its elements, or `0` if the array is empty. Given an array `nums`, return the sum of all XOR totals for every subset of `nums`.",
        examples=[{"input": "nums = [1,3]", "output": "6"}, {"input": "nums = [5,1,6]", "output": "28"}, {"input": "nums = [3,4,5,6,7,8]", "output": "480"}],
        constraints=["1 <= len(nums) <= 12", "1 <= nums[i] <= 20"],
        function_name="subsetXORSum",
        starter_code="def subsetXORSum(nums: list[int]) -> int:\n    pass\n",
        solution_code="def subsetXORSum(nums: list[int]) -> int:\n    total = 0\n    def dfs(idx, curr_xor):\n        nonlocal total\n        if idx == len(nums):\n            total += curr_xor\n            return\n        dfs(idx + 1, curr_xor ^ nums[idx])\n        dfs(idx + 1, curr_xor)\n    dfs(0, 0)\n    return total\n",
        test_cases=[{"input": [[1, 3]], "expected": 6}, {"input": [[5, 1, 6]], "expected": 28}, {"input": [[3, 4, 5, 6, 7, 8]], "expected": 480}, {"input": [[10]], "expected": 10}],
        hints=["At each element, choose whether to include it in the current subset XOR or exclude it."],
        leetcode_id=1863
    ))

    # 4. Generate All Binary Strings of Length N
    problems.append(make_problem(
        pid="bt-e-generate-binary-strings", title="Binary String Permutations",
        wing_id="backtracking", floor=204, difficulty="easy", visualizer_type="bits",
        monster_name="Binary Golem", monster_title="Mason of Fixed-Length Words",
        monster_sprite="golem", monster_color="#64748b", monster_attack="Bit Compression",
        monster_quote="All 2^n binary permutations were generated in order!",
        description="Given an integer `n`, return all binary strings of length `n` in lexicographical order.",
        examples=[{"input": "n = 2", "output": "[\"00\",\"01\",\"10\",\"11\"]"}, {"input": "n = 1", "output": "[\"0\",\"1\"]"}],
        constraints=["1 <= n <= 8"],
        function_name="generateBinaryStrings",
        starter_code="def generateBinaryStrings(n: int) -> list[str]:\n    pass\n",
        solution_code="def generateBinaryStrings(n: int) -> list[str]:\n    res = []\n    def dfs(path):\n        if len(path) == n:\n            res.append(path)\n            return\n        dfs(path + '0')\n        dfs(path + '1')\n    dfs('')\n    return res\n",
        test_cases=[{"input": [2], "expected": ["00", "01", "10", "11"]}, {"input": [1], "expected": ["0", "1"]}, {"input": [3], "expected": ["000", "001", "010", "011", "100", "101", "110", "111"]}],
        hints=["Recursively append '0' then '1' until the path reaches length n."],
        leetcode_id=None
    ))

    # 5. Permutations of Elements
    problems.append(make_problem(
        pid="bt-e-permute-three", title="Fixed Element Permutations",
        wing_id="backtracking", floor=205, difficulty="easy", visualizer_type="array",
        monster_name="Shuffle Imp", monster_title="Scrambler of Tiny Arrays",
        monster_sprite="goblin", monster_color="#f97316", monster_attack="Shuffle Toss",
        monster_quote="Every permutation of the small set was generated!",
        description="Given an array `nums` of distinct integers, return all the possible permutations in lexicographical order.",
        examples=[{"input": "nums = [1,2,3]", "output": "[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]"}],
        constraints=["1 <= len(nums) <= 4"],
        function_name="permuteThree",
        starter_code="def permuteThree(nums: list[int]) -> list[list[int]]:\n    pass\n",
        solution_code="def permuteThree(nums: list[int]) -> list[list[int]]:\n    res = []\n    def backtrack(curr, used):\n        if len(curr) == len(nums):\n            res.append(list(curr))\n            return\n        for i, val in enumerate(nums):\n            if not used[i]:\n                used[i] = True\n                curr.append(val)\n                backtrack(curr, used)\n                curr.pop()\n                used[i] = False\n    backtrack([], [False] * len(nums))\n    return sorted(res)\n",
        test_cases=[{"input": [[1, 2, 3]], "expected": [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]}, {"input": [[1, 2]], "expected": [[1, 2], [2, 1]]}, {"input": [[1]], "expected": [[1]]}],
        hints=["Use a boolean used array to track which elements are already in the current permutation."],
        leetcode_id=46
    ))

    # 6. Target Sum with Dice Combinations
    problems.append(make_problem(
        pid="bt-e-dice-combinations", title="Dice Combinations Target Sum",
        wing_id="backtracking", floor=206, difficulty="easy", visualizer_type="array",
        monster_name="Dice Drake", monster_title="Roller of Polyhedral Destinies",
        monster_sprite="dragon", monster_color="#ec4899", monster_attack="Dice Breath",
        monster_quote="All dice roll combinations summing to target were found!",
        description="Given an integer `d` (number of standard 6-sided dice) and an integer `target`, return all combinations of rolls (each 1-6) that sum to `target`, sorted lexicographically.",
        examples=[{"input": "d = 2, target = 7", "output": "[[1,6],[2,5],[3,4],[4,3],[5,2],[6,1]]"}],
        constraints=["1 <= d <= 3", "d <= target <= 6 * d"],
        function_name="diceCombinations",
        starter_code="def diceCombinations(d: int, target: int) -> list[list[int]]:\n    pass\n",
        solution_code="def diceCombinations(d: int, target: int) -> list[list[int]]:\n    res = []\n    def backtrack(dice_left, curr_sum, path):\n        if dice_left == 0:\n            if curr_sum == target:\n                res.append(list(path))\n            return\n        for face in range(1, 7):\n            if curr_sum + face + (dice_left - 1) * 1 <= target <= curr_sum + face + (dice_left - 1) * 6:\n                backtrack(dice_left - 1, curr_sum + face, path + [face])\n    backtrack(d, 0, [])\n    return res\n",
        test_cases=[{"input": [2, 7], "expected": [[1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1]]}, {"input": [1, 5], "expected": [[5]]}, {"input": [2, 12], "expected": [[6, 6]]}],
        hints=["Prune whenever the target is impossible to reach with remaining dice."],
        leetcode_id=1155
    ))

    # 7. Word Pattern Simple
    problems.append(make_problem(
        pid="bt-e-word-pattern-simple", title="Word Pattern Bijection",
        wing_id="backtracking", floor=207, difficulty="easy", visualizer_type="array",
        monster_name="Grammar Banshee", monster_title="Watcher of Structural Bijections",
        monster_sprite="wraith", monster_color="#a855f7", monster_attack="Grammar Wail",
        monster_quote="One-to-one character-to-word bijection verified!",
        description="Given a `pattern` and a string `s`, find if `s` follows the same pattern. Follow means a full match, such that there is a bijection between a letter in `pattern` and a non-empty word in `s`.",
        examples=[{"input": "pattern = \"abba\", s = \"dog cat cat dog\"", "output": "True"}, {"input": "pattern = \"abba\", s = \"dog cat cat fish\"", "output": "False"}],
        constraints=["1 <= len(pattern) <= 300", "1 <= len(s) <= 3000"],
        function_name="wordPatternSimple",
        starter_code="def wordPatternSimple(pattern: str, s: str) -> bool:\n    pass\n",
        solution_code="def wordPatternSimple(pattern: str, s: str) -> bool:\n    words = s.split()\n    if len(pattern) != len(words): return False\n    p2w, w2p = {}, {}\n    for p, w in zip(pattern, words):\n        if p in p2w and p2w[p] != w: return False\n        if w in w2p and w2p[w] != p: return False\n        p2w[p] = w\n        w2p[w] = p\n    return True\n",
        test_cases=[{"input": ["abba", "dog cat cat dog"], "expected": True}, {"input": ["abba", "dog cat cat fish"], "expected": False}, {"input": ["aaaa", "dog cat cat dog"], "expected": False}],
        hints=["Use two hash maps to establish a two-way bijection between pattern letters and words."],
        leetcode_id=290
    ))

    # 8. Subsets with Sum at Least K
    problems.append(make_problem(
        pid="bt-e-filtered-subsets", title="Subsets With Sum >= K",
        wing_id="backtracking", floor=208, difficulty="easy", visualizer_type="array",
        monster_name="Sum Sentry", monster_title="Gatekeeper of the Minimum Threshold",
        monster_sprite="golem", monster_color="#10b981", monster_attack="Threshold Bash",
        monster_quote="Filtered subsets met the target constraint exactly!",
        description="Given an array of distinct integers `nums` and a threshold integer `k`, return the count of non-empty subsets whose sum is greater than or equal to `k`.",
        examples=[{"input": "nums = [1,2,3], k = 3", "output": "5"}],
        constraints=["1 <= len(nums) <= 10", "1 <= nums[i] <= 100", "1 <= k <= 1000"],
        function_name="filteredSubsets",
        starter_code="def filteredSubsets(nums: list[int], k: int) -> int:\n    pass\n",
        solution_code="def filteredSubsets(nums: list[int], k: int) -> int:\n    count = 0\n    def dfs(idx, curr_sum, count_items):\n        nonlocal count\n        if idx == len(nums):\n            if count_items > 0 and curr_sum >= k:\n                count += 1\n            return\n        dfs(idx + 1, curr_sum + nums[idx], count_items + 1)\n        dfs(idx + 1, curr_sum, count_items)\n    dfs(0, 0, 0)\n    return count\n",
        test_cases=[{"input": [[1, 2, 3], 3], "expected": 5}, {"input": [[5], 5], "expected": 1}, {"input": [[1, 1], 10], "expected": 0}],
        hints=["Explore pick/skip at each index, verifying sum >= k at the leaves."],
        leetcode_id=None
    ))

    # 9. Count Paths to Leaf
    problems.append(make_problem(
        pid="bt-e-count-paths-leaf", title="Count Root-to-Leaf Paths",
        wing_id="backtracking", floor=209, difficulty="easy", visualizer_type="tree",
        monster_name="Canopy Shade", monster_title="Dweller of Binary Termini",
        monster_sprite="wraith", monster_color="#38bdf8", monster_attack="Root Hex",
        monster_quote="All paths from root to leaves counted successfully!",
        description="Given a complete binary tree array where node `i` has children `2*i + 1` and `2*i + 2`, return the number of distinct root-to-leaf paths.",
        examples=[{"input": "tree = [1,2,3,None,5]", "output": "2"}],
        constraints=["0 <= len(tree) <= 100"],
        function_name="countPathsToLeaf",
        starter_code="def countPathsToLeaf(tree: list) -> int:\n    pass\n",
        solution_code="def countPathsToLeaf(tree: list) -> int:\n    if not tree or tree[0] is None: return 0\n    def dfs(idx):\n        if idx >= len(tree) or tree[idx] is None: return 0\n        left, right = 2 * idx + 1, 2 * idx + 2\n        has_left = left < len(tree) and tree[left] is not None\n        has_right = right < len(tree) and tree[right] is not None\n        if not has_left and not has_right: return 1\n        return dfs(left) + dfs(right)\n    return dfs(0)\n",
        test_cases=[{"input": [[1, 2, 3, None, 5]], "expected": 2}, {"input": [[1]], "expected": 1}, {"input": [[]], "expected": 0}],
        hints=["A leaf has neither a valid left nor right child."],
        leetcode_id=257
    ))

    # 10. Generate Base-3 Combinations
    problems.append(make_problem(
        pid="bt-e-generate-base3", title="Base-3 Combinations Generator",
        wing_id="backtracking", floor=210, difficulty="easy", visualizer_type="array",
        monster_name="Ternary Imp", monster_title="Weaver of Tri-State Strings",
        monster_sprite="goblin", monster_color="#ec4899", monster_attack="Tri-Spark",
        monster_quote="All 3^n ternary branches accounted for!",
        description="Given an integer `n`, return all strings of length `n` containing characters `'0'`, `'1'`, and `'2'` in lexicographical order.",
        examples=[{"input": "n = 1", "output": "[\"0\",\"1\",\"2\"]"}, {"input": "n = 2", "output": "[\"00\",\"01\",\"02\",\"10\",\"11\",\"12\",\"20\",\"21\",\"22\"]"}],
        constraints=["1 <= n <= 4"],
        function_name="generateBase3",
        starter_code="def generateBase3(n: int) -> list[str]:\n    pass\n",
        solution_code="def generateBase3(n: int) -> list[str]:\n    res = []\n    def dfs(path):\n        if len(path) == n:\n            res.append(path)\n            return\n        for ch in '012':\n            dfs(path + ch)\n    dfs('')\n    return res\n",
        test_cases=[{"input": [1], "expected": ["0", "1", "2"]}, {"input": [2], "expected": ["00", "01", "02", "10", "11", "12", "20", "21", "22"]}],
        hints=["Recursively loop through '0', '1', '2' for each position."],
        leetcode_id=None
    ))

    return problems
