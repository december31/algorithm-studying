"""
Backtracking Medium Problems Part 2 (Problems 31 to 70 - 40 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_bt_medium_part2():
    problems = []

    # 31. All Paths From Source to Target
    problems.append(make_problem(
        pid="bt-m-all-paths-source-target", title="All Paths Source to Target",
        wing_id="backtracking", floor=231, difficulty="medium", visualizer_type="graph",
        monster_name="DAG Phantom", monster_title="Guider of Directed Acyclic Trails",
        monster_sprite="wraith", monster_color="#06b6d4", monster_attack="DAG Pierce",
        monster_quote="All topological paths from source to sink verified!",
        description="Given a directed acyclic graph (DAG) of `n` nodes labeled from `0` to `n - 1`, find all possible paths from node `0` to node `n - 1` and return them in sorted order.",
        examples=[{"input": "graph = [[1,2],[3],[3],[]]", "output": "[[0,1,3],[0,2,3]]"}],
        constraints=["n == len(graph)", "2 <= n <= 15"],
        function_name="allPathsSourceTarget",
        starter_code="def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:\n    pass\n",
        solution_code="def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:\n    target = len(graph) - 1\n    res = []\n    def dfs(curr, path):\n        if curr == target:\n            res.append(list(path))\n            return\n        for nxt in graph[curr]:\n            dfs(nxt, path + [nxt])\n    dfs(0, [0])\n    return sorted(res)\n",
        test_cases=[{"input": [[[1, 2], [3], [3], []]], "expected": [[0, 1, 3], [0, 2, 3]]}, {"input": [[[4, 3, 1], [3, 2, 4], [3], [4], []]], "expected": [[0, 1, 2, 3, 4], [0, 1, 3, 4], [0, 1, 4], [0, 3, 4], [0, 4]]}],
        hints=["DFS from node 0 to target on DAG. No visited set needed because DAG has no cycles."],
        leetcode_id=797
    ))

    # 32. Maximum Length of a Concatenated String with Unique Characters
    problems.append(make_problem(
        pid="bt-m-max-length-unique-concat", title="Max Length String with Unique Chars",
        wing_id="backtracking", floor=232, difficulty="medium", visualizer_type="array",
        monster_name="Alphabet Hydra", monster_title="Devourer of Disjoint Alphabets",
        monster_sprite="hydra", monster_color="#10b981", monster_attack="Disjoint Snap",
        monster_quote="Subsequence concatenation maintained 100% unique characters!",
        description="You are given an array of strings `arr`. A string `s` is formed by the concatenation of a subsequence of `arr` that has unique characters. Return the maximum possible length of `s`.",
        examples=[{"input": "arr = [\"un\",\"iq\",\"ue\"]", "output": "4"}, {"input": "arr = [\"cha\",\"r\",\"act\",\"ers\"]", "output": "6"}, {"input": "arr = [\"abcdefghijklmnopqrstuvwxyz\"]", "output": "26"}],
        constraints=["1 <= len(arr) <= 16", "1 <= len(arr[i]) <= 26"],
        function_name="maxLengthUnique",
        starter_code="def maxLengthUnique(arr: list[str]) -> int:\n    pass\n",
        solution_code="def maxLengthUnique(arr: list[str]) -> int:\n    valid = [s for s in arr if len(set(s)) == len(s)]\n    res = 0\n    def backtrack(idx, curr_set):\n        nonlocal res\n        res = max(res, len(curr_set))\n        for i in range(idx, len(valid)):\n            s_set = set(valid[i])\n            if not (curr_set & s_set):\n                backtrack(i + 1, curr_set | s_set)\n    backtrack(0, set())\n    return res\n",
        test_cases=[{"input": [["un", "iq", "ue"]], "expected": 4}, {"input": [["cha", "r", "act", "ers"]], "expected": 6}, {"input": [["abcdefghijklmnopqrstuvwxyz"]], "expected": 26}],
        hints=["Filter out strings with internal duplicates, then branch with set intersection."],
        leetcode_id=1239
    ))

    # 33. Splitting a String Into Descending Consecutive Values
    problems.append(make_problem(
        pid="bt-m-splitting-descending", title="Split String Descending Consecutive",
        wing_id="backtracking", floor=233, difficulty="medium", visualizer_type="array",
        monster_name="Countdown Golem", monster_title="Decrementer of Numeric Runs",
        monster_sprite="golem", monster_color="#f59e0b", monster_attack="Countdown Stomp",
        monster_quote="Every adjacent numerical token decremented by exactly 1!",
        description="You are given a string `s` that consists of only digits. Check if we can split `s` into two or more non-empty substrings such that the numerical values of the substrings are in descending order and the difference between numerical values of every two adjacent substrings is equal to `1`.",
        examples=[{"input": "s = \"050043\"", "output": "True"}, {"input": "s = \"9080701\"", "output": "False"}, {"input": "s = \"10009998\"", "output": "True"}],
        constraints=["1 <= len(s) <= 20", "s consists of only digits"],
        function_name="splitStringDescending",
        starter_code="def splitStringDescending(s: str) -> bool:\n    pass\n",
        solution_code="def splitStringDescending(s: str) -> bool:\n    def dfs(idx, prev):\n        if idx == len(s): return True\n        for j in range(idx + 1, len(s) + 1):\n            val = int(s[idx:j])\n            if val == prev - 1:\n                if dfs(j, val): return True\n        return False\n    for i in range(1, len(s)):\n        val = int(s[:i])\n        if dfs(i, val): return True\n    return False\n",
        test_cases=[{"input": ["050043"], "expected": True}, {"input": ["9080701"], "expected": False}, {"input": ["10009998"], "expected": True}, {"input": ["001"], "expected": False}],
        hints=["Pick the first number, then recursively search for value - 1."],
        leetcode_id=1849
    ))

    # 34. Factor Combinations
    problems.append(make_problem(
        pid="bt-m-factor-combinations", title="Factor Combinations",
        wing_id="backtracking", floor=234, difficulty="medium", visualizer_type="array",
        monster_name="Divisor Shade", monster_title="Factorizer of Composite Numbers",
        monster_sprite="wraith", monster_color="#8b5cf6", monster_attack="Prime Ray",
        monster_quote="All composite factorization trees evaluated!",
        description="Numbers can be regarded as product of its factors. Write a function that takes an integer `n` and returns all possible combinations of its factors greater than 1 and less than n in sorted order.",
        examples=[{"input": "n = 12", "output": "[[2,2,3],[2,6],[3,4]]"}, {"input": "n = 37", "output": "[]"}],
        constraints=["1 <= n <= 10^7"],
        function_name="getFactors",
        starter_code="def getFactors(n: int) -> list[list[int]]:\n    pass\n",
        solution_code="def getFactors(n: int) -> list[list[int]]:\n    res = []\n    def backtrack(rem, start, path):\n        if path:\n            res.append(path + [rem])\n        for f in range(start, int(rem**0.5) + 1):\n            if rem % f == 0:\n                backtrack(rem // f, f, path + [f])\n    backtrack(n, 2, [])\n    res.sort()\n    return res\n",
        test_cases=[{"input": [12], "expected": [[2, 2, 3], [2, 6], [3, 4]]}, {"input": [37], "expected": []}, {"input": [8], "expected": [[2, 2, 2], [2, 4]]}],
        hints=["Backtrack up to sqrt(rem), appending rem to path whenever path is non-empty."],
        leetcode_id=254
    ))

    # 35. Find Unique Binary String (Diagonalization)
    problems.append(make_problem(
        pid="bt-m-find-unique-binary-string", title="Find Unique Binary String",
        wing_id="backtracking", floor=235, difficulty="medium", visualizer_type="bits",
        monster_name="Cantor Lich", monster_title="Weaver of Diagonal Complements",
        monster_sprite="lich", monster_color="#38bdf8", monster_attack="Diagonal Hex",
        monster_quote="Cantor's diagonal argument generated the missing binary word!",
        description="Given an array of strings `nums` containing `n` unique binary strings each of length `n`, return a binary string of length `n` that does not appear in `nums`.",
        examples=[{"input": "nums = [\"01\",\"10\"]", "output": "\"11\""}, {"input": "nums = [\"00\",\"01\"]", "output": "\"10\""}, {"input": "nums = [\"111\",\"011\",\"001\"]", "output": "\"000\""}],
        constraints=["n == len(nums)", "1 <= n <= 16", "nums[i].length == n"],
        function_name="findDifferentBinaryString",
        starter_code="def findDifferentBinaryString(nums: list[str]) -> str:\n    pass\n",
        solution_code="def findDifferentBinaryString(nums: list[str]) -> str:\n    return ''.join('1' if nums[i][i] == '0' else '0' for i in range(len(nums)))\n",
        test_cases=[{"input": [["01", "10"]], "expected": "11"}, {"input": [["00", "01"]], "expected": "10"}, {"input": [["111", "011", "001"]], "expected": "000"}],
        hints=["Flip the i-th character of the i-th string (Cantor's diagonal argument)."],
        leetcode_id=1980
    ))

    # 36. Numbers With Same Consecutive Differences
    problems.append(make_problem(
        pid="bt-m-numbers-same-consec-diff", title="Same Consecutive Differences",
        wing_id="backtracking", floor=236, difficulty="medium", visualizer_type="array",
        monster_name="Difference Drake", monster_title="Maintainer of Delta Intervals",
        monster_sprite="dragon", monster_color="#ec4899", monster_attack="Delta Flame",
        monster_quote="Digits constructed with exact step difference k!",
        description="Given two integers `n` and `k`, return an array of all the integers of length `n` where the difference between every two consecutive digits is `k`. You may return the answer in any order.",
        examples=[{"input": "n = 3, k = 7", "output": "[181,292,707,818,929]"}, {"input": "n = 2, k = 1", "output": "[10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]"}],
        constraints=["2 <= n <= 9", "0 <= k <= 9"],
        function_name="numsSameConsecDiff",
        starter_code="def numsSameConsecDiff(n: int, k: int) -> list[int]:\n    pass\n",
        solution_code="def numsSameConsecDiff(n: int, k: int) -> list[int]:\n    res = []\n    def dfs(num, count):\n        if count == n:\n            res.append(num)\n            return\n        last = num % 10\n        next_digits = {last + k, last - k}\n        for d in next_digits:\n            if 0 <= d <= 9:\n                dfs(num * 10 + d, count + 1)\n    for start in range(1, 10):\n        dfs(start, 1)\n    return sorted(res)\n",
        test_cases=[{"input": [3, 7], "expected": [181, 292, 707, 818, 929]}, {"input": [2, 1], "expected": [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]}],
        hints=["Branch on last_digit + k and last_digit - k, avoiding duplicates when k == 0."],
        leetcode_id=967
    ))

    # 37. Letter Tile Possibilities
    problems.append(make_problem(
        pid="bt-m-letter-tile-possibilities", title="Letter Tile Possibilities",
        wing_id="backtracking", floor=237, difficulty="medium", visualizer_type="array",
        monster_name="Tile Fiend", monster_title="Scrabbler of Multi-Length Sequences",
        monster_sprite="demon", monster_color="#ef4444", monster_attack="Scrabble Strike",
        monster_quote="Every non-empty tile arrangement tallied without repetition!",
        description="You have `n` tiles, where each tile has one letter `tiles[i]` printed on it. Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.",
        examples=[{"input": "tiles = \"AAB\"", "output": "8"}, {"input": "tiles = \"AAABBC\"", "output": "188"}, {"input": "tiles = \"V\"", "output": "1"}],
        constraints=["1 <= len(tiles) <= 7"],
        function_name="numTilePossibilities",
        starter_code="def numTilePossibilities(tiles: str) -> int:\n    pass\n",
        solution_code="def numTilePossibilities(tiles: str) -> int:\n    from collections import Counter\n    counts = Counter(tiles)\n    def backtrack():\n        total = 0\n        for ch in counts:\n            if counts[ch] > 0:\n                counts[ch] -= 1\n                total += 1 + backtrack()\n                counts[ch] += 1\n        return total\n    return backtrack()\n",
        test_cases=[{"input": ["AAB"], "expected": 8}, {"input": ["AAABBC"], "expected": 188}, {"input": ["V"], "expected": 1}],
        hints=["Use frequency counter of tiles. At each step, decrement count, add 1, recurse, and restore."],
        leetcode_id=1079
    ))

    # 38. Combination Iterator
    problems.append(make_problem(
        pid="bt-m-iterator-combination", title="All Combinations of Length K",
        wing_id="backtracking", floor=238, difficulty="medium", visualizer_type="array",
        monster_name="Lexicon Golem", monster_title="Iterator of Ordered Combinations",
        monster_sprite="golem", monster_color="#64748b", monster_attack="Lexicon Strike",
        monster_quote="All k-length combinations listed in sorted order!",
        description="Given a string `characters` of sorted distinct lowercase English letters and a number `combinationLength`, return all combinations of characters of length `combinationLength` in lexicographical order.",
        examples=[{"input": "characters = \"abc\", combinationLength = 2", "output": "[\"ab\",\"ac\",\"bc\"]"}],
        constraints=["1 <= combinationLength <= len(characters) <= 15"],
        function_name="generateAllCombinations",
        starter_code="def generateAllCombinations(characters: str, combinationLength: int) -> list[str]:\n    pass\n",
        solution_code="def generateAllCombinations(characters: str, combinationLength: int) -> list[str]:\n    res = []\n    def backtrack(idx, path):\n        if len(path) == combinationLength:\n            res.append(''.join(path))\n            return\n        for i in range(idx, len(characters)):\n            path.append(characters[i])\n            backtrack(i + 1, path)\n            path.pop()\n    backtrack(0, [])\n    return res\n",
        test_cases=[{"input": ["abc", 2], "expected": ["ab", "ac", "bc"]}, {"input": ["abcd", 3], "expected": ["abc", "abd", "acd", "bcd"]}],
        hints=["Standard combination generation maintaining order of characters."],
        leetcode_id=1286
    ))

    # 39. Generalized Abbreviation
    problems.append(make_problem(
        pid="bt-m-generalized-abbreviation", title="Generalized Abbreviation",
        wing_id="backtracking", floor=239, difficulty="medium", visualizer_type="array",
        monster_name="Compressor Wraith", monster_title="Encoder of Substring Counts",
        monster_sprite="wraith", monster_color="#eab308", monster_attack="Count Hex",
        monster_quote="All 2^n character-or-count abbreviations generated!",
        description="A word can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. Given a string `word`, return a list of all the possible generalized abbreviations of `word` in sorted order.",
        examples=[{"input": "word = \"word\"", "output": "[\"1o1d\",\"1o2\",\"1or1\",\"1ord\",\"2r1\",\"2rd\",\"3d\",\"4\",\"w1r1\",\"w1rd\",\"w2d\",\"w3\",\"wo1d\",\"wo2\",\"wor1\",\"word\"]"}],
        constraints=["1 <= len(word) <= 10"],
        function_name="generateAbbreviations",
        starter_code="def generateAbbreviations(word: str) -> list[str]:\n    pass\n",
        solution_code="def generateAbbreviations(word: str) -> list[str]:\n    res = []\n    def backtrack(idx, curr, count):\n        if idx == len(word):\n            res.append(curr + (str(count) if count > 0 else ''))\n            return\n        # Option 1: abbreviate word[idx]\n        backtrack(idx + 1, curr, count + 1)\n        # Option 2: keep word[idx]\n        backtrack(idx + 1, curr + (str(count) if count > 0 else '') + word[idx], 0)\n    backtrack(0, '', 0)\n    return sorted(res)\n",
        test_cases=[{"input": ["word"], "expected": ["1o1d", "1o2", "1or1", "1ord", "2r1", "2rd", "3d", "4", "w1r1", "w1rd", "w2d", "w3", "wo1d", "wo2", "wor1", "word"]}, {"input": ["a"], "expected": ["1", "a"]}],
        hints=["At each position, choose to either increment the count of abbreviated letters or write the count and the letter."],
        leetcode_id=320
    ))

    # 40. Flip Game II (Game Theory Minimax)
    problems.append(make_problem(
        pid="bt-m-flip-game-ii", title="Flip Game II (Can Win)",
        wing_id="backtracking", floor=240, difficulty="medium", visualizer_type="array",
        monster_name="Plus-Minus Drake", monster_title="Strategist of Consecutive Inversions",
        monster_sprite="dragon", monster_color="#ec4899", monster_attack="Parity Breath",
        monster_quote="Minimax backtracking determined the winning initial state!",
        description="You are playing a Flip Game with your friend. You are given a string `currentState` that contains only `'+'` and `'-'`. You and your friend take turns to flip two consecutive `\"++\"` into `\"--\"`. The game ends when a person can no longer make a move, and therefore the other person will be the winner. Return `True` if the starting player can guarantee a win, and `False` otherwise.",
        examples=[{"input": "currentState = \"++++\"", "output": "True"}, {"input": "currentState = \"+\"", "output": "False"}],
        constraints=["1 <= len(currentState) <= 30"],
        function_name="canWinFlipGame",
        starter_code="def canWinFlipGame(currentState: str) -> bool:\n    pass\n",
        solution_code="def canWinFlipGame(currentState: str) -> bool:\n    memo = {}\n    def can_win(s):\n        if s in memo: return memo[s]\n        for i in range(len(s) - 1):\n            if s[i:i + 2] == '++':\n                next_s = s[:i] + '--' + s[i + 2:]\n                if not can_win(next_s):\n                    memo[s] = True\n                    return True\n        memo[s] = False\n        return False\n    return can_win(currentState)\n",
        test_cases=[{"input": ["++++"], "expected": True}, {"input": ["+"], "expected": False}, {"input": ["+++++"], "expected": False}],
        hints=["Player can guarantee win if there exists a valid move leading to a state where the opponent cannot win."],
        leetcode_id=294
    ))

    return problems
