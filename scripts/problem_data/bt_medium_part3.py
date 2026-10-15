"""
Backtracking Medium Problems Part 3 (Problems 41 to 70 - 30 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_bt_medium_part3():
    problems = []

    # 41. Word Pattern II
    problems.append(make_problem(
        pid="bt-m-word-pattern-ii", title="Word Pattern II (Bijection Search)",
        wing_id="backtracking", floor=241, difficulty="medium", visualizer_type="array",
        monster_name="Bijection Gorgon", monster_title="Seeker of Arbitrary Word Mappings",
        monster_sprite="slime", monster_color="#8b5cf6", monster_attack="Mapping Petrification",
        monster_quote="One-to-one word mapping backtrack discovered the bijection!",
        description="Given a `pattern` and a string `s`, return `True` if `s` matches the `pattern`. A string `s` matches a pattern if there is some bijective mapping of single characters to non-empty strings such that if each character in `pattern` is replaced with the string it maps to, then the resulting string is `s`.",
        examples=[{"input": "pattern = \"abab\", s = \"redblueredblue\"", "output": "True"}, {"input": "pattern = \"aaaa\", s = \"asdasdasdasd\"", "output": "True"}, {"input": "pattern = \"aabb\", s = \"xyzabcxzyabc\"", "output": "False"}],
        constraints=["1 <= len(pattern), len(s) <= 20"],
        function_name="wordPatternMatch",
        starter_code="def wordPatternMatch(pattern: str, s: str) -> bool:\n    pass\n",
        solution_code="def wordPatternMatch(pattern: str, s: str) -> bool:\n    p2s = {}\n    s2p = set()\n    def backtrack(p_idx, s_idx):\n        if p_idx == len(pattern) and s_idx == len(s): return True\n        if p_idx == len(pattern) or s_idx == len(s): return False\n        ch = pattern[p_idx]\n        if ch in p2s:\n            word = p2s[ch]\n            if not s.startswith(word, s_idx): return False\n            return backtrack(p_idx + 1, s_idx + len(word))\n        for k in range(s_idx + 1, len(s) + 1):\n            sub = s[s_idx:k]\n            if sub in s2p: continue\n            p2s[ch] = sub\n            s2p.add(sub)\n            if backtrack(p_idx + 1, k): return True\n            del p2s[ch]\n            s2p.remove(sub)\n        return False\n    return backtrack(0, 0)\n",
        test_cases=[{"input": ["abab", "redblueredblue"], "expected": True}, {"input": ["aaaa", "asdasdasdasd"], "expected": True}, {"input": ["aabb", "xyzabcxzyabc"], "expected": False}],
        hints=["Use backtracking to match pattern characters to candidate substrings with bijective hash sets."],
        leetcode_id=291
    ))

    # 42. Brace Expansion
    problems.append(make_problem(
        pid="bt-m-brace-expansion", title="Brace Expansion",
        wing_id="backtracking", floor=242, difficulty="medium", visualizer_type="array",
        monster_name="Expansion Gargoyle", monster_title="Expander of Grouped Options",
        monster_sprite="golem", monster_color="#10b981", monster_attack="Expansion Pulse",
        monster_quote="Cartesian product of brace groups generated in alphabetical order!",
        description="You are given a string `s` representing a list of words. Each letter in the word has one or more options. If there are multiple options, the options are given in braces like `\"{a,b,c}\"`. Return all words that can be formed, in lexicographical order.",
        examples=[{"input": "s = \"{a,b}c{d,e}f\"", "output": "[\"acdf\",\"acef\",\"bcdf\",\"bcef\"]"}, {"input": "s = \"abcd\"", "output": "[\"abcd\"]"}],
        constraints=["1 <= len(s) <= 50"],
        function_name="expandBraces",
        starter_code="def expandBraces(s: str) -> list[str]:\n    pass\n",
        solution_code="def expandBraces(s: str) -> list[str]:\n    groups = []\n    i = 0\n    while i < len(s):\n        if s[i] == '{':\n            j = s.index('}', i)\n            groups.append(sorted(s[i + 1:j].split(',')))\n            i = j + 1\n        else:\n            groups.append([s[i]])\n            i += 1\n    res = []\n    def backtrack(idx, path):\n        if idx == len(groups):\n            res.append(''.join(path))\n            return\n        for opt in groups[idx]:\n            backtrack(idx + 1, path + [opt])\n    backtrack(0, [])\n    return res\n",
        test_cases=[{"input": ["{a,b}c{d,e}f"], "expected": ["acdf", "acef", "bcdf", "bcef"]}, {"input": ["abcd"], "expected": ["abcd"]}],
        hints=["Parse string into groups of choices and compute their Cartesian product."],
        leetcode_id=1087
    ))

    # 43. Increasing Subsequences of Length K
    problems.append(make_problem(
        pid="bt-m-increasing-subsequences-k", title="Increasing Subsequences of Length K",
        wing_id="backtracking", floor=243, difficulty="medium", visualizer_type="array",
        monster_name="Strict Order Drake", monster_title="Watcher of Length-K Ascents",
        monster_sprite="dragon", monster_color="#38bdf8", monster_attack="Ascent Claw",
        monster_quote="All length-k strictly ascending subsequences gathered!",
        description="Given an integer array `nums` and an integer `k`, return all strictly increasing subsequences of length `k` in lexicographical order.",
        examples=[{"input": "nums = [1,2,3,4], k = 2", "output": "[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]"}],
        constraints=["1 <= k <= len(nums) <= 12"],
        function_name="increasingSubsequencesK",
        starter_code="def increasingSubsequencesK(nums: list[int], k: int) -> list[list[int]]:\n    pass\n",
        solution_code="def increasingSubsequencesK(nums: list[int], k: int) -> list[list[int]]:\n    res = []\n    def backtrack(idx, path):\n        if len(path) == k:\n            res.append(list(path))\n            return\n        for i in range(idx, len(nums)):\n            if not path or nums[i] > path[-1]:\n                backtrack(i + 1, path + [nums[i]])\n    backtrack(0, [])\n    return res\n",
        test_cases=[{"input": [[1, 2, 3, 4], 2], "expected": [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]}, {"input": [[4, 3, 2, 1], 2], "expected": []}],
        hints=["Backtrack maintaining strictly greater than previous element until length equals k."],
        leetcode_id=None
    ))

    # 44. Strobogrammatic Number II
    problems.append(make_problem(
        pid="bt-m-strobogrammatic-number-ii", title="Strobogrammatic Numbers",
        wing_id="backtracking", floor=244, difficulty="medium", visualizer_type="array",
        monster_name="Rotation Spectre", monster_title="Reflector of 180-Degree Digits",
        monster_sprite="wraith", monster_color="#f59e0b", monster_attack="180-Degree Inversion",
        monster_quote="Numbers that look the same rotated 180 degrees generated!",
        description="Given an integer `n`, return all the strobogrammatic numbers that are of length `n` in sorted order. A strobogrammatic number is a number that looks the same when rotated 180 degrees (upside down: 0, 1, 8 map to self; 6 and 9 swap).",
        examples=[{"input": "n = 2", "output": "[\"11\",\"69\",\"88\",\"96\"]"}, {"input": "n = 1", "output": "[\"0\",\"1\",\"8\"]"}],
        constraints=["1 <= n <= 6"],
        function_name="findStrobogrammatic",
        starter_code="def findStrobogrammatic(n: int) -> list[str]:\n    pass\n",
        solution_code="def findStrobogrammatic(n: int) -> list[str]:\n    pairs = [('0', '0'), ('1', '1'), ('8', '8'), ('6', '9'), ('9', '6')]\n    def helper(m):\n        if m == 0: return [\"\"]\n        if m == 1: return [\"0\", \"1\", \"8\"]\n        prev = helper(m - 2)\n        curr = []\n        for p in prev:\n            for l, r in pairs:\n                if m != n or l != '0':\n                    curr.append(l + p + r)\n        return curr\n    return sorted(helper(n))\n",
        test_cases=[{"input": [2], "expected": ["11", "69", "88", "96"]}, {"input": [1], "expected": ["0", "1", "8"]}],
        hints=["Build from center outwards, avoiding leading zero on the outer layer."],
        leetcode_id=247
    ))

    # 45. Additive Number
    problems.append(make_problem(
        pid="bt-m-additive-number", title="Additive Number",
        wing_id="backtracking", floor=245, difficulty="medium", visualizer_type="array",
        monster_name="Additive Sphinx", monster_title="Verifier of Consecutive Sums",
        monster_sprite="beholder", monster_color="#ec4899", monster_attack="Additive Gaze",
        monster_quote="A valid additive sequence was verified across the string!",
        description="An additive number is a string whose digits can form an additive sequence: num1 + num2 = num3. Given a string containing only digits, return `True` if it is an additive number or `False` otherwise.",
        examples=[{"input": "num = \"112358\"", "output": "True"}, {"input": "num = \"199100199\"", "output": "True"}],
        constraints=["1 <= len(num) <= 35"],
        function_name="isAdditiveNumber",
        starter_code="def isAdditiveNumber(num: str) -> bool:\n    pass\n",
        solution_code="def isAdditiveNumber(num: str) -> bool:\n    n = len(num)\n    for i in range(1, n):\n        for j in range(i + 1, n):\n            s1, s2 = num[:i], num[i:j]\n            if (len(s1) > 1 and s1[0] == '0') or (len(s2) > 1 and s2[0] == '0'): continue\n            n1, n2 = int(s1), int(s2)\n            k = j\n            valid = True\n            while k < n:\n                n3 = n1 + n2\n                s3 = str(n3)\n                if not num.startswith(s3, k):\n                    valid = False\n                    break\n                k += len(s3)\n                n1, n2 = n2, n3\n            if valid and k == n: return True\n    return False\n",
        test_cases=[{"input": ["112358"], "expected": True}, {"input": ["199100199"], "expected": True}, {"input": ["1023"], "expected": False}],
        hints=["Fix the first two numbers; all subsequent numbers are determined by their sum."],
        leetcode_id=306
    ))

    # 46. Lexicographical Numbers
    problems.append(make_problem(
        pid="bt-m-lexicographical-numbers", title="Lexicographical Numbers (1 to N)",
        wing_id="backtracking", floor=246, difficulty="medium", visualizer_type="array",
        monster_name="Alphabetical Golem", monster_title="Traverser of Decimal Tries",
        monster_sprite="golem", monster_color="#64748b", monster_attack="Lexical Stomp",
        monster_quote="Preorder traversal of the base-10 trie produced order in O(n)!",
        description="Given an integer `n`, return all the numbers in the range `[1, n]` sorted in lexicographical order in O(n) time.",
        examples=[{"input": "n = 13", "output": "[1,10,11,12,13,2,3,4,5,6,7,8,9]"}, {"input": "n = 2", "output": "[1,2]"}],
        constraints=["1 <= n <= 5 * 10^4"],
        function_name="lexicalOrder",
        starter_code="def lexicalOrder(n: int) -> list[int]:\n    pass\n",
        solution_code="def lexicalOrder(n: int) -> list[int]:\n    res = []\n    def dfs(curr):\n        if curr > n: return\n        res.append(curr)\n        for d in range(10):\n            if curr * 10 + d <= n:\n                dfs(curr * 10 + d)\n            else:\n                break\n    for start in range(1, 10):\n        dfs(start)\n    return res\n",
        test_cases=[{"input": [13], "expected": [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]}, {"input": [2], "expected": [1, 2]}],
        hints=["Treat numbers 1..n as a 10-ary tree and do preorder DFS starting from 1..9."],
        leetcode_id=386
    ))

    # 47. Partition Equal Subset Sum
    problems.append(make_problem(
        pid="bt-m-partition-equal-subset-sum", title="Partition Equal Subset Sum",
        wing_id="backtracking", floor=247, difficulty="medium", visualizer_type="array",
        monster_name="Bisection Drake", monster_title="Balancer of Two Equal Halves",
        monster_sprite="dragon", monster_color="#10b981", monster_attack="Bisection Flare",
        monster_quote="Subset sum equal to sum // 2 found!",
        description="Given an integer array `nums`, return `True` if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or `False` otherwise.",
        examples=[{"input": "nums = [1,5,11,5]", "output": "True"}, {"input": "nums = [1,2,3,5]", "output": "False"}],
        constraints=["1 <= len(nums) <= 200", "1 <= nums[i] <= 100"],
        function_name="canPartition",
        starter_code="def canPartition(nums: list[int]) -> bool:\n    pass\n",
        solution_code="def canPartition(nums: list[int]) -> bool:\n    total = sum(nums)\n    if total % 2 != 0: return False\n    target = total // 2\n    dp = {0}\n    for n in nums:\n        dp |= {x + n for x in dp if x + n <= target}\n        if target in dp: return True\n    return target in dp\n",
        test_cases=[{"input": [[1, 5, 11, 5]], "expected": True}, {"input": [[1, 2, 3, 5]], "expected": False}, {"input": [[2, 2]], "expected": True}],
        hints=["Find if there is a subset summing to total // 2 using bitwise DP / reachable set."],
        leetcode_id=416
    ))

    # 48. Shopping Offers
    problems.append(make_problem(
        pid="bt-m-shopping-offers", title="Shopping Offers Minimum Cost",
        wing_id="backtracking", floor=248, difficulty="medium", visualizer_type="array",
        monster_name="Bargain Fiend", monster_title="Vendor of Discount Bundles",
        monster_sprite="demon", monster_color="#f59e0b", monster_attack="Discount Slash",
        monster_quote="Special bundles and regular pricing optimized to lowest cost!",
        description="In a store, there are some items for sale. You are given an array `price` where `price[i]` is the price of the `i-th` item, `special` offers with bundle counts and bundle price, and an array `needs` representing your target item counts. Return the lowest price you have to pay for exactly certain items as specified.",
        examples=[{"input": "price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]", "output": "14"}, {"input": "price = [2,3,4], special = [[1,1,0,4],[2,2,1,9]], needs = [1,2,1]", "output": "11"}],
        constraints=["price.length == needs.length", "1 <= len(price) <= 6"],
        function_name="shoppingOffers",
        starter_code="def shoppingOffers(price: list[int], special: list[list[int]], needs: list[int]) -> int:\n    pass\n",
        solution_code="def shoppingOffers(price: list[int], special: list[list[int]], needs: list[int]) -> int:\n    memo = {}\n    def dfs(cur_needs):\n        key = tuple(cur_needs)\n        if key in memo: return memo[key]\n        cost = sum(p * n for p, n in zip(price, cur_needs))\n        for sp in special:\n            new_needs = [cur_needs[i] - sp[i] for i in range(len(price))]\n            if all(x >= 0 for x in new_needs):\n                cost = min(cost, sp[-1] + dfs(new_needs))\n        memo[key] = cost\n        return cost\n    return dfs(needs)\n",
        test_cases=[{"input": [[2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2]], "expected": 14}, {"input": [[2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1]], "expected": 11}],
        hints=["Memoized DFS on remaining needs tuple, testing each applicable special bundle."],
        leetcode_id=638
    ))

    # 49. Word Break II Subset
    problems.append(make_problem(
        pid="bt-m-word-break-ii-subset", title="Word Break Reconstruction",
        wing_id="backtracking", floor=249, difficulty="medium", visualizer_type="array",
        monster_name="Token Carver", monster_title="Dissector of Continuous Strings",
        monster_sprite="wraith", monster_color="#8b5cf6", monster_attack="Token Sever",
        monster_quote="All space-separated word combinations reconstructed!",
        description="Given a string `s` and a dictionary of strings `wordDict`, add spaces in `s` to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in sorted order.",
        examples=[{"input": "s = \"catsanddog\", wordDict = [\"cat\",\"cats\",\"and\",\"sand\",\"dog\"]", "output": "[\"cat sand dog\",\"cats and dog\"]"}],
        constraints=["1 <= len(s) <= 20", "1 <= len(wordDict) <= 1000"],
        function_name="wordBreakList",
        starter_code="def wordBreakList(s: str, wordDict: list[str]) -> list[str]:\n    pass\n",
        solution_code="def wordBreakList(s: str, wordDict: list[str]) -> list[str]:\n    words = set(wordDict)\n    memo = {}\n    def dfs(sub):\n        if sub in memo: return memo[sub]\n        if not sub: return [\"\"]\n        res = []\n        for w in words:\n            if sub.startswith(w):\n                sub_res = dfs(sub[len(w):])\n                for rest in sub_res:\n                    res.append(w + (\" \" + rest if rest else \"\"))\n        memo[sub] = res\n        return res\n    return sorted(dfs(s))\n",
        test_cases=[{"input": ["catsanddog", ["cat", "cats", "and", "sand", "dog"]], "expected": ["cat sand dog", "cats and dog"]}, {"input": ["pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]], "expected": ["pine apple pen apple", "pine applepen apple", "pineapple pen apple"]}],
        hints=["Memoized recursion: partition prefix that is in wordDict and combine with suffix partitions."],
        leetcode_id=140
    ))

    # 50. Subsets with GCD Equals One
    problems.append(make_problem(
        pid="bt-m-find-subsets-gcd", title="Subsets with GCD Equals One",
        wing_id="backtracking", floor=250, difficulty="medium", visualizer_type="array",
        monster_name="Euclidean Lich", monster_title="Tester of Coprime Combinations",
        monster_sprite="lich", monster_color="#06b6d4", monster_attack="Euclidean Hex",
        monster_quote="Coprime subsets evaluated with greatest common divisor math!",
        description="Given an array of integers `nums`, return the number of non-empty subsets whose greatest common divisor (GCD) is equal to 1.",
        examples=[{"input": "nums = [2,3,6]", "output": "2"}, {"input": "nums = [2,4]", "output": "0"}],
        constraints=["1 <= len(nums) <= 12", "1 <= nums[i] <= 100"],
        function_name="subsetsGcdOne",
        starter_code="def subsetsGcdOne(nums: list[int]) -> int:\n    pass\n",
        solution_code="def subsetsGcdOne(nums: list[int]) -> int:\n    import math\n    count = 0\n    def dfs(idx, curr_gcd):\n        nonlocal count\n        if idx == len(nums):\n            if curr_gcd == 1: count += 1\n            return\n        dfs(idx + 1, curr_gcd)\n        next_gcd = nums[idx] if curr_gcd is None else math.gcd(curr_gcd, nums[idx])\n        dfs(idx + 1, next_gcd)\n    dfs(0, None)\n    return count\n",
        test_cases=[{"input": [[2, 3, 6]], "expected": 2}, {"input": [[2, 4]], "expected": 0}, {"input": [[1]], "expected": 1}],
        hints=["Explore pick/skip. Update running math.gcd(curr_gcd, nums[idx])."],
        leetcode_id=None
    ))

    return problems
