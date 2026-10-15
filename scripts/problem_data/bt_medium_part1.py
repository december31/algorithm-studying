"""
Backtracking Medium Problems Part 1 (Problems 11 to 40 - 30 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_bt_medium_part1():
    problems = []

    # 11. Subsets
    problems.append(make_problem(
        pid="bt-m-subsets", title="Subsets (Power Set)",
        wing_id="backtracking", floor=211, difficulty="medium", visualizer_type="array",
        monster_name="Power-Set Spectre", monster_title="Multiplier of Binary Choices",
        monster_sprite="wraith", monster_color="#8b5cf6", monster_attack="Combinatorial Flare",
        monster_quote="All 2^n subsets of the power set materialized!",
        description="Given an integer array `nums` of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution sorted by subset length, then lexicographically.",
        examples=[{"input": "nums = [1,2,3]", "output": "[[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]"}],
        constraints=["1 <= len(nums) <= 10", "-10 <= nums[i] <= 10", "All the numbers of nums are unique"],
        function_name="subsets",
        starter_code="def subsets(nums: list[int]) -> list[list[int]]:\n    pass\n",
        solution_code="def subsets(nums: list[int]) -> list[list[int]]:\n    res = []\n    def backtrack(idx, path):\n        res.append(list(path))\n        for i in range(idx, len(nums)):\n            path.append(nums[i])\n            backtrack(i + 1, path)\n            path.pop()\n    backtrack(0, [])\n    res.sort(key=lambda s: (len(s), s))\n    return res\n",
        test_cases=[{"input": [[1, 2, 3]], "expected": [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]}, {"input": [[0]], "expected": [[], [0]]}],
        hints=["At each step, push the current path into result, then iterate remaining elements."],
        leetcode_id=78
    ))

    # 12. Subsets II (With Duplicates)
    problems.append(make_problem(
        pid="bt-m-subsets-ii", title="Subsets II (Unique Subsets with Duplicates)",
        wing_id="backtracking", floor=212, difficulty="medium", visualizer_type="array",
        monster_name="Duplicate Fiend", monster_title="Purifier of Redundant Sets",
        monster_sprite="demon", monster_color="#ef4444", monster_attack="Duplicate Pierce",
        monster_quote="Duplicate branches pruned whenever nums[i] == nums[i-1]!",
        description="Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets. Return the solution sorted by length and then elements.",
        examples=[{"input": "nums = [1,2,2]", "output": "[[],[1],[2],[1,2],[2,2],[1,2,2]"}],
        constraints=["1 <= len(nums) <= 10"],
        function_name="subsetsWithDup",
        starter_code="def subsetsWithDup(nums: list[int]) -> list[list[int]]:\n    pass\n",
        solution_code="def subsetsWithDup(nums: list[int]) -> list[list[int]]:\n    nums.sort()\n    res = []\n    def backtrack(idx, path):\n        res.append(list(path))\n        for i in range(idx, len(nums)):\n            if i > idx and nums[i] == nums[i - 1]:\n                continue\n            path.append(nums[i])\n            backtrack(i + 1, path)\n            path.pop()\n    backtrack(0, [])\n    res.sort(key=lambda s: (len(s), s))\n    return res\n",
        test_cases=[{"input": [[1, 2, 2]], "expected": [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]}, {"input": [[0]], "expected": [[], [0]]}],
        hints=["Sort first, and skip duplicate elements at the same recursion depth: if i > idx and nums[i] == nums[i-1]."],
        leetcode_id=90
    ))

    # 13. Permutations
    problems.append(make_problem(
        pid="bt-m-permutations", title="Permutations (All Distinct)",
        wing_id="backtracking", floor=213, difficulty="medium", visualizer_type="array",
        monster_name="Permuto Behemoth", monster_title="Lord of the Factorial Matrix",
        monster_sprite="golem", monster_color="#f59e0b", monster_attack="Factorial Stomp",
        monster_quote="All N! full permutations verified in order!",
        description="Given an array `nums` of distinct integers, return all the possible permutations sorted lexicographically.",
        examples=[{"input": "nums = [1,2,3]", "output": "[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]"}],
        constraints=["1 <= len(nums) <= 6"],
        function_name="permute",
        starter_code="def permute(nums: list[int]) -> list[list[int]]:\n    pass\n",
        solution_code="def permute(nums: list[int]) -> list[list[int]]:\n    res = []\n    used = [False] * len(nums)\n    def backtrack(curr):\n        if len(curr) == len(nums):\n            res.append(list(curr))\n            return\n        for i in range(len(nums)):\n            if not used[i]:\n                used[i] = True\n                curr.append(nums[i])\n                backtrack(curr)\n                curr.pop()\n                used[i] = False\n    backtrack([])\n    return sorted(res)\n",
        test_cases=[{"input": [[1, 2, 3]], "expected": [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]}, {"input": [[0, 1]], "expected": [[0, 1], [1, 0]]}],
        hints=["Track elements placed with a used boolean array."],
        leetcode_id=46
    ))

    # 14. Permutations II (Unique Duplicates)
    problems.append(make_problem(
        pid="bt-m-permutations-ii", title="Permutations II (With Duplicates)",
        wing_id="backtracking", floor=214, difficulty="medium", visualizer_type="array",
        monster_name="Twin Gargoyle", monster_title="Protector of Duplicate Keys",
        monster_sprite="golem", monster_color="#10b981", monster_attack="Twin Blast",
        monster_quote="Identical consecutive candidates skipped if previous sibling was unused!",
        description="Given a collection of numbers, `nums`, that might contain duplicates, return all possible unique permutations in sorted order.",
        examples=[{"input": "nums = [1,1,2]", "output": "[[1,1,2],[1,2,1],[2,1,1]]"}],
        constraints=["1 <= len(nums) <= 8"],
        function_name="permuteUnique",
        starter_code="def permuteUnique(nums: list[int]) -> list[list[int]]:\n    pass\n",
        solution_code="def permuteUnique(nums: list[int]) -> list[list[int]]:\n    nums.sort()\n    res = []\n    used = [False] * len(nums)\n    def backtrack(curr):\n        if len(curr) == len(nums):\n            res.append(list(curr))\n            return\n        for i in range(len(nums)):\n            if used[i]: continue\n            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]: continue\n            used[i] = True\n            curr.append(nums[i])\n            backtrack(curr)\n            curr.pop()\n            used[i] = False\n    backtrack([])\n    return res\n",
        test_cases=[{"input": [[1, 1, 2]], "expected": [[1, 1, 2], [1, 2, 1], [2, 1, 1]]}, {"input": [[1, 2, 3]], "expected": [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]}],
        hints=["Sort nums. Skip duplicate if nums[i] == nums[i-1] and not used[i-1]."],
        leetcode_id=47
    ))

    # 15. Combinations
    problems.append(make_problem(
        pid="bt-m-combinations", title="Combinations (N Choose K)",
        wing_id="backtracking", floor=215, difficulty="medium", visualizer_type="array",
        monster_name="Binomial Wyvern", monster_title="Keeper of Pascal's Exponents",
        monster_sprite="dragon", monster_color="#38bdf8", monster_attack="Binomial Flame",
        monster_quote="All n choose k combinations extracted in sorted order!",
        description="Given two integers `n` and `k`, return all possible combinations of `k` numbers chosen from the range `[1, n]` in lexicographical order.",
        examples=[{"input": "n = 4, k = 2", "output": "[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]"}],
        constraints=["1 <= n <= 20", "1 <= k <= n"],
        function_name="combine",
        starter_code="def combine(n: int, k: int) -> list[list[int]]:\n    pass\n",
        solution_code="def combine(n: int, k: int) -> list[list[int]]:\n    res = []\n    def backtrack(start, curr):\n        if len(curr) == k:\n            res.append(list(curr))\n            return\n        need = k - len(curr)\n        for i in range(start, n - need + 2):\n            curr.append(i)\n            backtrack(i + 1, curr)\n            curr.pop()\n    backtrack(1, [])\n    return res\n",
        test_cases=[{"input": [4, 2], "expected": [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]}, {"input": [1, 1], "expected": [[1]]}],
        hints=["Prune the loop bound: i only needs to go up to n - (k - len(curr)) + 1."],
        leetcode_id=77
    ))

    # 16. Combination Sum
    problems.append(make_problem(
        pid="bt-m-combination-sum", title="Combination Sum (Unlimited Reuse)",
        wing_id="backtracking", floor=216, difficulty="medium", visualizer_type="array",
        monster_name="Sum Titan", monster_title="Pounder of Target Coin Allocations",
        monster_sprite="golem", monster_color="#f59e0b", monster_attack="Coin Stomp",
        monster_quote="Unbounded candidate reuse achieved the target sum!",
        description="Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. The same number may be chosen unlimited times.",
        examples=[{"input": "candidates = [2,3,6,7], target = 7", "output": "[[2,2,3],[7]]"}, {"input": "candidates = [2,3,5], target = 8", "output": "[[2,2,2,2],[2,3,3],[3,5]]"}],
        constraints=["1 <= len(candidates) <= 30", "2 <= candidates[i] <= 40", "1 <= target <= 40"],
        function_name="combinationSum",
        starter_code="def combinationSum(candidates: list[int], target: int) -> list[list[int]]:\n    pass\n",
        solution_code="def combinationSum(candidates: list[int], target: int) -> list[list[int]]:\n    candidates.sort()\n    res = []\n    def backtrack(idx, rem, path):\n        if rem == 0:\n            res.append(list(path))\n            return\n        for i in range(idx, len(candidates)):\n            if candidates[i] > rem: break\n            path.append(candidates[i])\n            backtrack(i, rem - candidates[i], path)\n            path.pop()\n    backtrack(0, target, [])\n    return res\n",
        test_cases=[{"input": [[2, 3, 6, 7], 7], "expected": [[2, 2, 3], [7]]}, {"input": [[2, 3, 5], 8], "expected": [[2, 2, 2, 2], [2, 3, 3], [3, 5]]}, {"input": [[2], 1], "expected": []}],
        hints=["Since candidates can be reused, recursive call passes i instead of i + 1."],
        leetcode_id=39
    ))

    # 17. Combination Sum II
    problems.append(make_problem(
        pid="bt-m-combination-sum-ii", title="Combination Sum II (Single Use)",
        wing_id="backtracking", floor=217, difficulty="medium", visualizer_type="array",
        monster_name="Coin Specter", monster_title="Auditor of Single-Use Shards",
        monster_sprite="wraith", monster_color="#ec4899", monster_attack="Coin Drain",
        monster_quote="Single-use candidates with duplicate skips matched target!",
        description="Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sum to `target`. Each number in `candidates` may only be used once in the combination.",
        examples=[{"input": "candidates = [10,1,2,7,6,1,5], target = 8", "output": "[[1,1,6],[1,2,5],[1,7],[2,6]]"}],
        constraints=["1 <= len(candidates) <= 100", "1 <= target <= 30"],
        function_name="combinationSum2",
        starter_code="def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:\n    pass\n",
        solution_code="def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:\n    candidates.sort()\n    res = []\n    def backtrack(idx, rem, path):\n        if rem == 0:\n            res.append(list(path))\n            return\n        for i in range(idx, len(candidates)):\n            if candidates[i] > rem: break\n            if i > idx and candidates[i] == candidates[i - 1]: continue\n            path.append(candidates[i])\n            backtrack(i + 1, rem - candidates[i], path)\n            path.pop()\n    backtrack(0, target, [])\n    return res\n",
        test_cases=[{"input": [[10, 1, 2, 7, 6, 1, 5], 8], "expected": [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]}, {"input": [[2, 5, 2, 1, 2], 5], "expected": [[1, 2, 2], [5]]}],
        hints=["Sort, pass i + 1 for single use, and skip duplicates when i > idx and candidates[i] == candidates[i-1]."],
        leetcode_id=40
    ))

    # 18. Combination Sum III
    problems.append(make_problem(
        pid="bt-m-combination-sum-iii", title="Combination Sum III (K Numbers 1-9)",
        wing_id="backtracking", floor=218, difficulty="medium", visualizer_type="array",
        monster_name="Nine-Digit Sphinx", monster_title="Keeper of Single-Digit Constellations",
        monster_sprite="beholder", monster_color="#8b5cf6", monster_attack="Digit Glare",
        monster_quote="K distinct digits from 1 to 9 summed to n!",
        description="Find all valid combinations of `k` numbers that sum up to `n` such that only numbers 1 through 9 are used, and each number is used at most once. Return a list of all possible valid combinations.",
        examples=[{"input": "k = 3, n = 7", "output": "[[1,2,4]]"}, {"input": "k = 3, n = 9", "output": "[[1,2,6],[1,3,5],[2,3,4]]"}],
        constraints=["2 <= k <= 9", "1 <= n <= 60"],
        function_name="combinationSum3",
        starter_code="def combinationSum3(k: int, n: int) -> list[list[int]]:\n    pass\n",
        solution_code="def combinationSum3(k: int, n: int) -> list[list[int]]:\n    res = []\n    def backtrack(start, rem, curr):\n        if len(curr) == k:\n            if rem == 0: res.append(list(curr))\n            return\n        for d in range(start, 10):\n            if d > rem: break\n            curr.append(d)\n            backtrack(d + 1, rem - d, curr)\n            curr.pop()\n    backtrack(1, n, [])\n    return res\n",
        test_cases=[{"input": [3, 7], "expected": [[1, 2, 4]]}, {"input": [3, 9], "expected": [[1, 2, 6], [1, 3, 5], [2, 3, 4]]}, {"input": [4, 1], "expected": []}],
        hints=["Digits from 1 to 9. Enforce len(curr) == k and rem == 0."],
        leetcode_id=216
    ))

    # 19. Letter Combinations of a Phone Number
    problems.append(make_problem(
        pid="bt-m-letter-combinations-phone", title="Phone Number Mnemonics",
        wing_id="backtracking", floor=219, difficulty="medium", visualizer_type="array",
        monster_name="Keypad Demon", monster_title="Transcriber of DTMF Tones",
        monster_sprite="demon", monster_color="#06b6d4", monster_attack="Tone Blast",
        monster_quote="All phone mnemonic permutations matched the digits!",
        description="Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in lexicographical order.",
        examples=[{"input": "digits = \"23\"", "output": "[\"ad\",\"ae\",\"af\",\"bd\",\"be\",\"bf\",\"cd\",\"ce\",\"cf\"]"}, {"input": "digits = \"\"", "output": "[]"}],
        constraints=["0 <= len(digits) <= 4", "digits[i] is between '2' and '9'"],
        function_name="letterCombinations",
        starter_code="def letterCombinations(digits: str) -> list[str]:\n    pass\n",
        solution_code="def letterCombinations(digits: str) -> list[str]:\n    if not digits: return []\n    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}\n    res = []\n    def backtrack(idx, path):\n        if idx == len(digits):\n            res.append(''.join(path))\n            return\n        for ch in mapping[digits[idx]]:\n            path.append(ch)\n            backtrack(idx + 1, path)\n            path.pop()\n    backtrack(0, [])\n    return sorted(res)\n",
        test_cases=[{"input": ["23"], "expected": ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]}, {"input": [""], "expected": []}, {"input": ["2"], "expected": ["a", "b", "c"]}],
        hints=["Map each digit to letters and branch on each letter at index idx."],
        leetcode_id=17
    ))

    # 20. Generate Parentheses
    problems.append(make_problem(
        pid="bt-m-generate-parentheses", title="Generate Parentheses",
        wing_id="backtracking", floor=220, difficulty="medium", visualizer_type="stack",
        monster_name="Catalan Golem", monster_title="Architect of Well-Formed Dyck Paths",
        monster_sprite="golem", monster_color="#10b981", monster_attack="Catalan Quake",
        monster_quote="All C_n well-formed parenthetical strings produced!",
        description="Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses in lexicographical order.",
        examples=[{"input": "n = 3", "output": "[\"((()))\",\"(()())\",\"(())()\",\"()(())\",\"()()()\"]"}, {"input": "n = 1", "output": "[\"()\"]"}],
        constraints=["1 <= n <= 8"],
        function_name="generateParenthesis",
        starter_code="def generateParenthesis(n: int) -> list[str]:\n    pass\n",
        solution_code="def generateParenthesis(n: int) -> list[str]:\n    res = []\n    def backtrack(open_c, close_c, path):\n        if len(path) == 2 * n:\n            res.append(path)\n            return\n        if open_c < n:\n            backtrack(open_c + 1, close_c, path + '(')\n        if close_c < open_c:\n            backtrack(open_c, close_c + 1, path + ')')\n    backtrack(0, 0, '')\n    return sorted(res)\n",
        test_cases=[{"input": [3], "expected": ["((()))", "(()())", "(())()", "()(())", "()()()"]}, {"input": [1], "expected": ["()"]}, {"input": [2], "expected": ["(())", "()()"]}],
        hints=["Only add '(' if open < n; only add ')' if close < open."],
        leetcode_id=22
    ))

    # 21. Palindrome Partitioning
    problems.append(make_problem(
        pid="bt-m-palindrome-partitioning", title="Palindrome Partitioning",
        wing_id="backtracking", floor=221, difficulty="medium", visualizer_type="array",
        monster_name="Mirror Hydra", monster_title="Splitter of Palindromic Segments",
        monster_sprite="hydra", monster_color="#ec4899", monster_attack="Mirror Sever",
        monster_quote="All substrings checked for palindromes at every partition point!",
        description="Given a string `s`, partition `s` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of `s`.",
        examples=[{"input": "s = \"aab\"", "output": "[[\"a\",\"a\",\"b\"],[\"aa\",\"b\"]]"}, {"input": "s = \"a\"", "output": "[[\"a\"]]"}],
        constraints=["1 <= len(s) <= 16", "s contains only lowercase English letters"],
        function_name="partitionPalindromes",
        starter_code="def partitionPalindromes(s: str) -> list[list[str]]:\n    pass\n",
        solution_code="def partitionPalindromes(s: str) -> list[list[str]]:\n    res = []\n    def is_pal(sub): return sub == sub[::-1]\n    def backtrack(start, path):\n        if start == len(s):\n            res.append(list(path))\n            return\n        for end in range(start + 1, len(s) + 1):\n            sub = s[start:end]\n            if is_pal(sub):\n                path.append(sub)\n                backtrack(end, path)\n                path.pop()\n    backtrack(0, [])\n    return res\n",
        test_cases=[{"input": ["aab"], "expected": [["a", "a", "b"], ["aa", "b"]]}, {"input": ["a"], "expected": [["a"]]}],
        hints=["Backtrack over prefix lengths. If prefix is palindrome, recursively partition remaining string."],
        leetcode_id=131
    ))

    # 22. Restore IP Addresses
    problems.append(make_problem(
        pid="bt-m-restore-ip-addresses", title="Restore IP Addresses",
        wing_id="backtracking", floor=222, difficulty="medium", visualizer_type="array",
        monster_name="IPv4 Warden", monster_title="Validator of Octet Ranges",
        monster_sprite="lich", monster_color="#38bdf8", monster_attack="Packet Drop",
        monster_quote="Every 4-octet valid IP address reconstructed without leading zeroes!",
        description="A valid IP address consists of exactly four integers separated by single dots. Each integer is between `0` and `255` (inclusive) and cannot have leading zeros. Given a string `s` containing only digits, return all possible valid IP addresses in sorted order.",
        examples=[{"input": "s = \"25525511135\"", "output": "[\"255.255.11.135\",\"255.255.111.35\"]"}, {"input": "s = \"0000\"", "output": "[\"0.0.0.0\"]"}],
        constraints=["1 <= len(s) <= 20", "s consists of digits only"],
        function_name="restoreIpAddresses",
        starter_code="def restoreIpAddresses(s: str) -> list[str]:\n    pass\n",
        solution_code="def restoreIpAddresses(s: str) -> list[str]:\n    res = []\n    def backtrack(start, parts):\n        if len(parts) == 4:\n            if start == len(s): res.append('.'.join(parts))\n            return\n        for length in range(1, 4):\n            if start + length > len(s): break\n            part = s[start:start + length]\n            if (len(part) > 1 and part[0] == '0') or int(part) > 255: continue\n            parts.append(part)\n            backtrack(start + length, parts)\n            parts.pop()\n    backtrack(0, [])\n    return sorted(res)\n",
        test_cases=[{"input": ["25525511135"], "expected": ["255.255.11.135", "255.255.111.35"]}, {"input": ["0000"], "expected": ["0.0.0.0"]}, {"input": ["101023"], "expected": ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]}],
        hints=["4 segments. Each segment has length 1 to 3, must not have leading zero, and value <= 255."],
        leetcode_id=93
    ))

    # 23. Word Search in Grid
    problems.append(make_problem(
        pid="bt-m-word-search", title="Word Search in Grid",
        wing_id="backtracking", floor=223, difficulty="medium", visualizer_type="graph",
        monster_name="Grid Basilisk", monster_title="Stalker of 4-Directional Word Trails",
        monster_sprite="dragon", monster_color="#10b981", monster_attack="Grid Venom",
        monster_quote="DFS backtracking traversed the word without reusing cells!",
        description="Given an `m x n` grid of characters `board` and a string `word`, return `True` if `word` exists in the grid. The word can be constructed from letters of sequentially adjacent cells (horizontally or vertically). The same letter cell may not be used more than once.",
        examples=[{"input": "board = [[\"A\",\"B\",\"C\",\"E\"],[\"S\",\"F\",\"C\",\"S\"],[\"A\",\"D\",\"E\",\"E\"]], word = \"ABCCED\"", "output": "True"}, {"input": "board = [[\"A\",\"B\",\"C\",\"E\"],[\"S\",\"F\",\"C\",\"S\"],[\"A\",\"D\",\"E\",\"E\"]], word = \"SEE\"", "output": "True"}, {"input": "board = [[\"A\",\"B\",\"C\",\"E\"],[\"S\",\"F\",\"C\",\"S\"],[\"A\",\"D\",\"E\",\"E\"]], word = \"ABCB\"", "output": "False"}],
        constraints=["m == len(board)", "n == len(board[0])", "1 <= m, n <= 6", "1 <= len(word) <= 15"],
        function_name="existWord",
        starter_code="def existWord(board: list[list[str]], word: str) -> bool:\n    pass\n",
        solution_code="def existWord(board: list[list[str]], word: str) -> bool:\n    m, n = len(board), len(board[0])\n    def dfs(r, c, idx):\n        if idx == len(word): return True\n        if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[idx]: return False\n        temp = board[r][c]\n        board[r][c] = '#'\n        found = dfs(r+1, c, idx+1) or dfs(r-1, c, idx+1) or dfs(r, c+1, idx+1) or dfs(r, c-1, idx+1)\n        board[r][c] = temp\n        return found\n    for i in range(m):\n        for j in range(n):\n            if dfs(i, j, 0): return True\n    return False\n",
        test_cases=[{"input": [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"], "expected": True}, {"input": [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"], "expected": True}, {"input": [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"], "expected": False}],
        hints=["Mark visited cells with '#' during recursion and restore back upon return."],
        leetcode_id=79
    ))

    # 24. Target Sum
    problems.append(make_problem(
        pid="bt-m-target-sum", title="Target Sum Expressions",
        wing_id="backtracking", floor=224, difficulty="medium", visualizer_type="array",
        monster_name="Binary Sign Wraith", monster_title="Assigner of Plus and Minus Glyphs",
        monster_sprite="wraith", monster_color="#eab308", monster_attack="Sign Hex",
        monster_quote="Every + and - configuration checked with memoization!",
        description="You are given an integer array `nums` and an integer `target`. You want to build an expression out of nums by adding one of the symbols `'+'` and `'-'` before each integer. Return the number of different expressions that evaluate to `target`.",
        examples=[{"input": "nums = [1,1,1,1,1], target = 3", "output": "5"}, {"input": "nums = [1], target = 1", "output": "1"}],
        constraints=["1 <= len(nums) <= 20", "0 <= nums[i] <= 1000", "-1000 <= target <= 1000"],
        function_name="findTargetSumWays",
        starter_code="def findTargetSumWays(nums: list[int], target: int) -> int:\n    pass\n",
        solution_code="def findTargetSumWays(nums: list[int], target: int) -> int:\n    memo = {}\n    def dfs(idx, curr):\n        if idx == len(nums):\n            return 1 if curr == target else 0\n        state = (idx, curr)\n        if state in memo: return memo[state]\n        ans = dfs(idx + 1, curr + nums[idx]) + dfs(idx + 1, curr - nums[idx])\n        memo[state] = ans\n        return ans\n    return dfs(0, 0)\n",
        test_cases=[{"input": [[1, 1, 1, 1, 1], 3], "expected": 5}, {"input": [[1], 1], "expected": 1}, {"input": [[1], 2], "expected": 0}],
        hints=["Memoize state (index, current_sum). Branch on +num and -num."],
        leetcode_id=494
    ))

    # 25. Path with Maximum Gold
    problems.append(make_problem(
        pid="bt-m-path-max-gold", title="Path with Maximum Gold",
        wing_id="backtracking", floor=225, difficulty="medium", visualizer_type="graph",
        monster_name="Gold Vein Golem", monster_title="Hoarder of Subterranean Nuggets",
        monster_sprite="golem", monster_color="#eab308", monster_attack="Gold Shock",
        monster_quote="Backtracking visited non-zero cells and gathered maximum gold!",
        description="In a gold mine grid of size `m x n`, each cell has an integer representing the amount of gold in that cell (0 if empty). From a cell with gold, you can walk 4 directions to other gold cells without visiting any cell more than once. Return the maximum amount of gold you can collect starting from any position.",
        examples=[{"input": "grid = [[0,6,0],[5,8,7],[0,9,0]]", "output": "24"}, {"input": "grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]", "output": "28"}],
        constraints=["m == len(grid)", "n == len(grid[i])", "1 <= m, n <= 15", "0 <= grid[i][j] <= 100"],
        function_name="getMaximumGold",
        starter_code="def getMaximumGold(grid: list[list[int]]) -> int:\n    pass\n",
        solution_code="def getMaximumGold(grid: list[list[int]]) -> int:\n    m, n = len(grid), len(grid[0])\n    def dfs(r, c):\n        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0: return 0\n        gold = grid[r][c]\n        grid[r][c] = 0\n        best = max(dfs(r+1, c), dfs(r-1, c), dfs(r, c+1), dfs(r, c-1))\n        grid[r][c] = gold\n        return gold + best\n    ans = 0\n    for i in range(m):\n        for j in range(n):\n            if grid[i][j] > 0: ans = max(ans, dfs(i, j))\n    return ans\n",
        test_cases=[{"input": [[[0, 6, 0], [5, 8, 7], [0, 9, 0]]], "expected": 24}, {"input": [[[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]], "expected": 28}],
        hints=["Temporarily zero out grid[r][c] to prevent cycle, restore on backtracking."],
        leetcode_id=1219
    ))

    # 26. Non-decreasing Subsequences
    problems.append(make_problem(
        pid="bt-m-non-decreasing-subsequences", title="Non-decreasing Subsequences",
        wing_id="backtracking", floor=226, difficulty="medium", visualizer_type="array",
        monster_name="Ascending Wyrm", monster_title="Climber of Monotonic Stairs",
        monster_sprite="dragon", monster_color="#10b981", monster_attack="Ascent Breath",
        monster_quote="Level-set hashing prevented duplicate non-decreasing sequences!",
        description="Given an integer array `nums`, return all the different possible non-decreasing subsequences of the given array with at least two elements in sorted order.",
        examples=[{"input": "nums = [4,6,7,7]", "output": "[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]"}, {"input": "nums = [4,4,3,2,1]", "output": "[[4,4]]"}],
        constraints=["1 <= len(nums) <= 15", "-100 <= nums[i] <= 100"],
        function_name="findSubsequences",
        starter_code="def findSubsequences(nums: list[int]) -> list[list[int]]:\n    pass\n",
        solution_code="def findSubsequences(nums: list[int]) -> list[list[int]]:\n    res = []\n    def backtrack(idx, path):\n        if len(path) >= 2:\n            res.append(list(path))\n        used = set()\n        for i in range(idx, len(nums)):\n            if nums[i] in used: continue\n            if not path or nums[i] >= path[-1]:\n                used.add(nums[i])\n                path.append(nums[i])\n                backtrack(i + 1, path)\n                path.pop()\n    backtrack(0, [])\n    res.sort(key=lambda s: (len(s), s))\n    return res\n",
        test_cases=[{"input": [[4, 6, 7, 7]], "expected": [[4, 6], [4, 7], [6, 7], [7, 7], [4, 6, 7], [4, 7, 7], [6, 7, 7], [4, 6, 7, 7]]}, {"input": [[4, 4, 3, 2, 1]], "expected": [[4, 4]]}],
        hints=["Use a local set at each recursion level to prevent reusing duplicate values at the same depth."],
        leetcode_id=491
    ))

    # 27. Beautiful Arrangement
    problems.append(make_problem(
        pid="bt-m-beautiful-arrangement", title="Beautiful Arrangement",
        wing_id="backtracking", floor=227, difficulty="medium", visualizer_type="array",
        monster_name="Divisibility Sphinx", monster_title="Keeper of Divisible Alignments",
        monster_sprite="beholder", monster_color="#ec4899", monster_attack="Divisibility Gaze",
        monster_quote="Every index i satisfies (val % i == 0 or i % val == 0)!",
        description="Suppose you have `n` integers labeled `1` through `n`. A permutation of these `n` integers is called a beautiful arrangement if for every `i` (1 <= i <= n): `perm[i] % i == 0` or `i % perm[i] == 0`. Return the number of the beautiful arrangements that you can construct.",
        examples=[{"input": "n = 2", "output": "2"}, {"input": "n = 1", "output": "1"}],
        constraints=["1 <= n <= 15"],
        function_name="countArrangement",
        starter_code="def countArrangement(n: int) -> int:\n    pass\n",
        solution_code="def countArrangement(n: int) -> int:\n    count = 0\n    used = [False] * (n + 1)\n    def backtrack(pos):\n        nonlocal count\n        if pos > n:\n            count += 1\n            return\n        for num in range(1, n + 1):\n            if not used[num] and (num % pos == 0 or pos % num == 0):\n                used[num] = True\n                backtrack(pos + 1)\n                used[num] = False\n    backtrack(1)\n    return count\n",
        test_cases=[{"input": [2], "expected": 2}, {"input": [1], "expected": 1}, {"input": [3], "expected": 3}],
        hints=["Place numbers at position 1..n. Prune when neither num % pos == 0 nor pos % num == 0."],
        leetcode_id=526
    ))

    # 28. Matchsticks to Square
    problems.append(make_problem(
        pid="bt-m-matchsticks-to-square", title="Matchsticks to Square",
        wing_id="backtracking", floor=228, difficulty="medium", visualizer_type="array",
        monster_name="Pyromancer Golem", monster_title="Builder of 4-Sided Perimeters",
        monster_sprite="golem", monster_color="#f97316", monster_attack="Flame Perimeter",
        monster_quote="The 4 perimeter sides summed to perimeter / 4 exactly!",
        description="You are given an integer array `matchsticks` where `matchsticks[i]` is the length of the `i-th` matchstick. You want to use all the matchsticks to make one square without breaking any stick. Return `True` if you can make this square and `False` otherwise.",
        examples=[{"input": "matchsticks = [1,1,2,2,2]", "output": "True"}, {"input": "matchsticks = [3,3,3,3,4]", "output": "False"}],
        constraints=["1 <= len(matchsticks) <= 15", "1 <= matchsticks[i] <= 10^8"],
        function_name="makesquare",
        starter_code="def makesquare(matchsticks: list[int]) -> bool:\n    pass\n",
        solution_code="def makesquare(matchsticks: list[int]) -> bool:\n    total = sum(matchsticks)\n    if total % 4 != 0: return False\n    target = total // 4\n    matchsticks.sort(reverse=True)\n    sides = [0] * 4\n    def backtrack(idx):\n        if idx == len(matchsticks):\n            return sides[0] == sides[1] == sides[2] == target\n        for i in range(4):\n            if sides[i] + matchsticks[idx] <= target:\n                sides[i] += matchsticks[idx]\n                if backtrack(idx + 1): return True\n                sides[i] -= matchsticks[idx]\n            if sides[i] == 0: break\n        return False\n    return backtrack(0)\n",
        test_cases=[{"input": [[1, 1, 2, 2, 2]], "expected": True}, {"input": [[3, 3, 3, 3, 4]], "expected": False}, {"input": [[5, 5, 5, 5]], "expected": True}],
        hints=["Sort descending to prune early. Maintain 4 side sums up to total // 4."],
        leetcode_id=473
    ))

    # 29. Partition to K Equal Sum Subsets
    problems.append(make_problem(
        pid="bt-m-partition-k-equal-sum", title="Partition to K Equal Sum Subsets",
        wing_id="backtracking", floor=229, difficulty="medium", visualizer_type="array",
        monster_name="Bucket Chimera", monster_title="Distributor of K Equal Troughs",
        monster_sprite="demon", monster_color="#ef4444", monster_attack="Partition Claw",
        monster_quote="Elements partitioned into k equal subsets seamlessly!",
        description="Given an integer array `nums` and an integer `k`, return `True` if it is possible to divide this array into `k` non-empty subsets whose sums are all equal.",
        examples=[{"input": "nums = [4,3,2,3,5,2,1], k = 4", "output": "True"}, {"input": "nums = [1,2,3,4], k = 3", "output": "False"}],
        constraints=["1 <= k <= len(nums) <= 16", "1 <= nums[i] <= 10^4"],
        function_name="canPartitionKSubsets",
        starter_code="def canPartitionKSubsets(nums: list[int], k: int) -> bool:\n    pass\n",
        solution_code="def canPartitionKSubsets(nums: list[int], k: int) -> bool:\n    total = sum(nums)\n    if total % k != 0: return False\n    target = total // k\n    nums.sort(reverse=True)\n    buckets = [0] * k\n    def backtrack(idx):\n        if idx == len(nums): return True\n        for i in range(k):\n            if buckets[i] + nums[idx] <= target:\n                buckets[i] += nums[idx]\n                if backtrack(idx + 1): return True\n                buckets[i] -= nums[idx]\n            if buckets[i] == 0: break\n        return False\n    return backtrack(0)\n",
        test_cases=[{"input": [[4, 3, 2, 3, 5, 2, 1], 4], "expected": True}, {"input": [[1, 2, 3, 4], 3], "expected": False}],
        hints=["Sort descending and break when buckets[i] == 0 to eliminate duplicate symmetric bucket assignments."],
        leetcode_id=698
    ))

    # 30. Split Array into Fibonacci Sequence
    problems.append(make_problem(
        pid="bt-m-split-fibonacci", title="Split Array into Fibonacci Sequence",
        wing_id="backtracking", floor=230, difficulty="medium", visualizer_type="array",
        monster_name="Fibonacci Lich", monster_title="Conjurer of Additive Sequences",
        monster_sprite="lich", monster_color="#8b5cf6", monster_attack="Fibonacci Hex",
        monster_quote="Consecutive sum condition F[n-2] + F[n-1] == F[n] satisfied!",
        description="Given a string of digits `num`, split `num` into a Fibonacci-like sequence where each piece fits in a 32-bit signed integer and has at least 3 numbers. Return any valid sequence or `[]` if none exists.",
        examples=[{"input": "num = \"1101111\"", "output": "[11,0,11,11]"}, {"input": "num = \"112358130\"", "output": "[]"}],
        constraints=["1 <= len(num) <= 200"],
        function_name="splitIntoFibonacci",
        starter_code="def splitIntoFibonacci(num: str) -> list[int]:\n    pass\n",
        solution_code="def splitIntoFibonacci(num: str) -> list[int]:\n    res = []\n    MAX_INT = 2**31 - 1\n    def backtrack(idx):\n        if idx == len(num) and len(res) >= 3:\n            return True\n        for length in range(1, len(num) - idx + 1):\n            if length > 1 and num[idx] == '0': break\n            val = int(num[idx:idx + length])\n            if val > MAX_INT: break\n            if len(res) >= 2:\n                expected = res[-1] + res[-2]\n                if val < expected: continue\n                elif val > expected: break\n            res.append(val)\n            if backtrack(idx + length): return True\n            res.pop()\n        return False\n    if backtrack(0): return res\n    return []\n",
        test_cases=[{"input": ["1101111"], "expected": [11, 0, 11, 11]}, {"input": ["112358130"], "expected": []}, {"input": ["0123"], "expected": []}],
        hints=["After two numbers are picked, the third is strictly determined by their sum."],
        leetcode_id=842
    ))

    return problems
