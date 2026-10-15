"""
Builder for Data Structures problems (10 Easy, 60 Medium, 30 Hard).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem
from scripts.problem_data.ds_easy import get_data_structures_problems as get_ds_easy


def get_data_structures_medium():
    problems = []

    # 1. Subarray Sum Equals K
    problems.append(make_problem(
        pid="ds-m-subarray-sum-k",
        title="Subarray Sum Equals K",
        wing_id="data-structures",
        floor=111,
        difficulty="medium",
        visualizerType="array",
        monster_name="Sum Wraith",
        monster_title="Harvester of Prefix Differences",
        monster_sprite="wraith",
        monster_color="#8b5cf6",
        monster_attack="Prefix Drain",
        monster_quote="The prefix sum hash revealed all my hidden intervals!",
        description="Given an array of integers `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals to `k`.",
        examples=[
            {"input": "nums = [1,1,1], k = 2", "output": "2"},
            {"input": "nums = [1,2,3], k = 3", "output": "2"}
        ],
        constraints=["1 <= len(nums) <= 2 * 10^4", "-1000 <= nums[i] <= 1000", "-10^7 <= k <= 10^7"],
        function_name="subarraySum",
        starter_code="def subarraySum(nums: list[int], k: int) -> int:\n    pass\n",
        solution_code="def subarraySum(nums: list[int], k: int) -> int:\n    count = 0\n    curr_sum = 0\n    prefix_map = {0: 1}\n    for num in nums:\n        curr_sum += num\n        if curr_sum - k in prefix_map:\n            count += prefix_map[curr_sum - k]\n        prefix_map[curr_sum] = prefix_map.get(curr_sum, 0) + 1\n    return count\n",
        test_cases=[
            {"input": [[1, 1, 1], 2], "expected": 2},
            {"input": [[1, 2, 3], 3], "expected": 2},
            {"input": [[1, -1, 0], 0], "expected": 3},
            {"input": [[3], 3], "expected": 1},
            {"input": [[1], 0], "expected": 0},
        ],
        hints=["Use a prefix sum hash map to store frequencies of prefix sums."],
        leetcode_id=560,
    ))

    # 2. Daily Temperatures
    problems.append(make_problem(
        pid="ds-m-daily-temperatures",
        title="Daily Temperatures",
        wing_id="data-structures",
        floor=112,
        difficulty="medium",
        visualizerType="stack",
        monster_name="Thermal Drake",
        monster_title="Lord of Rising Heat Waves",
        monster_sprite="dragon",
        monster_color="#ef4444",
        monster_attack="Inferno Blast",
        monster_quote="A monotonic stack pierced right through my temperature anomalies!",
        description="Given an array of integers `temperatures` representing daily temperatures, return an array `answer` such that `answer[i]` is the number of days you have to wait after the `i-th` day to get a warmer temperature. If there is no future day for which this is possible, keep `answer[i] == 0`.",
        examples=[
            {"input": "temperatures = [73,74,75,71,69,72,76,73]", "output": "[1,1,4,2,1,1,0,0]"},
            {"input": "temperatures = [30,40,50,60]", "output": "[1,1,1,0]"}
        ],
        constraints=["1 <= len(temperatures) <= 10^5", "30 <= temperatures[i] <= 100"],
        function_name="dailyTemperatures",
        starter_code="def dailyTemperatures(temperatures: list[int]) -> list[int]:\n    pass\n",
        solution_code="def dailyTemperatures(temperatures: list[int]) -> list[int]:\n    res = [0] * len(temperatures)\n    stack = []\n    for i, t in enumerate(temperatures):\n        while stack and temperatures[stack[-1]] < t:\n            prev = stack.pop()\n            res[prev] = i - prev\n        stack.append(i)\n    return res\n",
        test_cases=[
            {"input": [[73, 74, 75, 71, 69, 72, 76, 73]], "expected": [1, 1, 4, 2, 1, 1, 0, 0]},
            {"input": [[30, 40, 50, 60]], "expected": [1, 1, 1, 0]},
            {"input": [[30, 60, 90]], "expected": [1, 1, 0]},
            {"input": [[80, 70, 60]], "expected": [0, 0, 0]},
        ],
        hints=["Maintain a decreasing monotonic stack of indices."],
        leetcode_id=739,
    ))

    # 3. Evaluate Reverse Polish Notation
    problems.append(make_problem(
        pid="ds-m-eval-rpn",
        title="Evaluate Reverse Polish Notation",
        wing_id="data-structures",
        floor=113,
        difficulty="medium",
        visualizerType="stack",
        monster_name="Postfix Daemon",
        monster_title="Parser of Inverted Formulas",
        monster_sprite="demon",
        monster_color="#ec4899",
        monster_attack="Postfix Slam",
        monster_quote="You parsed my operands and operators without error!",
        description="Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are `+`, `-`, `*`, and `/`. Each operand may be an integer or another expression. Division between two integers should truncate toward zero.",
        examples=[
            {"input": "tokens = [\"2\",\"1\",\"+\",\"3\",\"*\"]", "output": "9"},
            {"input": "tokens = [\"4\",\"13\",\"5\",\"/\",\"+\"]", "output": "6"},
            {"input": "tokens = [\"10\",\"6\",\"9\",\"3\",\"+\",\"-11\",\"*\",\"/\",\"*\",\"17\",\"+\",\"5\",\"+\"]", "output": "22"}
        ],
        constraints=["1 <= len(tokens) <= 10^4", "Tokens are valid RPN tokens"],
        function_name="evalRPN",
        starter_code="def evalRPN(tokens: list[str]) -> int:\n    pass\n",
        solution_code="def evalRPN(tokens: list[str]) -> int:\n    stack = []\n    for t in tokens:\n        if t not in '+-*/':\n            stack.append(int(t))\n        else:\n            b = stack.pop()\n            a = stack.pop()\n            if t == '+': stack.append(a + b)\n            elif t == '-': stack.append(a - b)\n            elif t == '*': stack.append(a * b)\n            elif t == '/': stack.append(int(a / b))\n    return stack[0]\n",
        test_cases=[
            {"input": [["2", "1", "+", "3", "*"]], "expected": 9},
            {"input": [["4", "13", "5", "/", "+"]], "expected": 6},
            {"input": [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]], "expected": 22},
            {"input": [["3", "-4", "+"]], "expected": -1},
        ],
        hints=["Push numbers to a stack; upon an operator, pop two operands, apply the operator, and push back."],
        leetcode_id=150,
    ))

    # 4. Simplify Path
    problems.append(make_problem(
        pid="ds-m-simplify-path",
        title="Simplify Unix Path",
        wing_id="data-structures",
        floor=114,
        difficulty="medium",
        visualizerType="stack",
        monster_name="Directory Golem",
        monster_title="Warden of Nested Folders",
        monster_sprite="golem",
        monster_color="#6366f1",
        monster_attack="Path Truncation",
        monster_quote="Canonical paths leave no room for directory recursion!",
        description="Given a string `path`, which is an absolute path to a file or directory in a Unix-style file system, convert it to the simplified canonical path.",
        examples=[
            {"input": "path = \"/home/\"", "output": "\"/home\""},
            {"input": "path = \"/../\"", "output": "\"/\""},
            {"input": "path = \"/home//foo/\"", "output": "\"/home/foo\""},
            {"input": "path = \"/a/./b/../../c/\"", "output": "\"/c\""}
        ],
        constraints=["1 <= len(path) <= 3000", "path consists of English letters, digits, '.', '/', or '_'"],
        function_name="simplifyPath",
        starter_code="def simplifyPath(path: str) -> str:\n    pass\n",
        solution_code="def simplifyPath(path: str) -> str:\n    parts = path.split('/')\n    stack = []\n    for p in parts:\n        if p == '' or p == '.':\n            continue\n        if p == '..':\n            if stack:\n                stack.pop()\n        else:\n            stack.append(p)\n    return '/' + '/'.join(stack)\n",
        test_cases=[
            {"input": ["/home/"], "expected": "/home"},
            {"input": ["/../"], "expected": "/"},
            {"input": ["/home//foo/"], "expected": "/home/foo"},
            {"input": ["/a/./b/../../c/"], "expected": "/c"},
            {"input": ["/a/../../b/../c//.//"], "expected": "/c"},
        ],
        hints=["Split by '/' and use a stack to push directories or pop on '..'."],
        leetcode_id=71,
    ))

    # 5. Longest Consecutive Sequence
    problems.append(make_problem(
        pid="ds-m-longest-consecutive",
        title="Longest Consecutive Sequence",
        wing_id="data-structures",
        floor=115,
        difficulty="medium",
        visualizerType="array",
        monster_name="Continuum Hydra",
        monster_title="Beast of Broken Sequences",
        monster_sprite="hydra",
        monster_color="#14b8a6",
        monster_attack="Sequence Constriction",
        monster_quote="You tracked consecutive intervals in O(n) without sorting!",
        description="Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence. You must write an algorithm that runs in O(n) time.",
        examples=[
            {"input": "nums = [100,4,200,1,3,2]", "output": "4"},
            {"input": "nums = [0,3,7,2,5,8,4,6,0,1]", "output": "9"}
        ],
        constraints=["0 <= len(nums) <= 10^5", "-10^9 <= nums[i] <= 10^9"],
        function_name="longestConsecutive",
        starter_code="def longestConsecutive(nums: list[int]) -> int:\n    pass\n",
        solution_code="def longestConsecutive(nums: list[int]) -> int:\n    num_set = set(nums)\n    longest = 0\n    for n in num_set:\n        if n - 1 not in num_set:\n            curr = n\n            streak = 1\n            while curr + 1 in num_set:\n                curr += 1\n                streak += 1\n            longest = max(longest, streak)\n    return longest\n",
        test_cases=[
            {"input": [[100, 4, 200, 1, 3, 2]], "expected": 4},
            {"input": [[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]], "expected": 9},
            {"input": [[]], "expected": 0},
            {"input": [[10]], "expected": 1},
            {"input": [[1, 2, 0, 1]], "expected": 3},
        ],
        hints=["Store elements in a set. Only begin counting when `num - 1` is not in the set."],
        leetcode_id=128,
    ))

    # 6. Group Anagrams
    problems.append(make_problem(
        pid="ds-m-group-anagrams",
        title="Group Anagram Signatures",
        wing_id="data-structures",
        floor=116,
        difficulty="medium",
        visualizerType="array",
        monster_name="Permutation Gorgon",
        monster_title="Weaver of Shuffled Syllables",
        monster_sprite="slime",
        monster_color="#f59e0b",
        monster_attack="Scramble Stare",
        monster_quote="My scrambled letters were indexed by their canonical sorts!",
        description="Given an array of strings `strs`, group the anagrams together. Return the groups sorted by group size, and lexicographically within each group.",
        examples=[
            {"input": "strs = [\"eat\",\"tea\",\"tan\",\"ate\",\"nat\",\"bat\"]", "output": "[[\"bat\"], [\"nat\", \"tan\"], [\"ate\", \"eat\", \"tea\"]]"}
        ],
        constraints=["1 <= len(strs) <= 10^4", "0 <= len(strs[i]) <= 100", "strs[i] consists of lowercase English letters"],
        function_name="groupAnagramsCanonical",
        starter_code="def groupAnagramsCanonical(strs: list[str]) -> list[list[str]]:\n    pass\n",
        solution_code="def groupAnagramsCanonical(strs: list[str]) -> list[list[str]]:\n    from collections import defaultdict\n    groups = defaultdict(list)\n    for s in strs:\n        key = ''.join(sorted(s))\n        groups[key].append(s)\n    res = [sorted(g) for g in groups.values()]\n    res.sort(key=lambda x: (len(x), x[0] if x else ''))\n    return res\n",
        test_cases=[
            {"input": [["eat", "tea", "tan", "ate", "nat", "bat"]], "expected": [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]},
            {"input": [[""]], "expected": [[""]]},
            {"input": [["a"]], "expected": [["a"]]},
            {"input": [["ab", "ba", "abc", "cba"]], "expected": [["ab", "ba"], ["abc", "cba"]]},
        ],
        hints=["Use tuple of char counts or sorted string as dictionary key."],
        leetcode_id=49,
    ))

    # 7. Top K Frequent Elements
    problems.append(make_problem(
        pid="ds-m-top-k-frequent",
        title="Top K Frequent Elements",
        wing_id="data-structures",
        floor=117,
        difficulty="medium",
        visualizerType="array",
        monster_name="Frequency Behemoth",
        monster_title="Counter of Occurrences",
        monster_sprite="golem",
        monster_color="#10b981",
        monster_attack="Quake Resonance",
        monster_quote="Bucket sort and heaps exposed the top k frequencies!",
        description="Given an integer array `nums` and an integer `k`, return the `k` most frequent elements in descending order of frequency.",
        examples=[
            {"input": "nums = [1,1,1,2,2,3], k = 2", "output": "[1,2]"},
            {"input": "nums = [1], k = 1", "output": "[1]"}
        ],
        constraints=["1 <= len(nums) <= 10^5", "-10^4 <= nums[i] <= 10^4", "k is in range [1, unique elements]"],
        function_name="topKFrequent",
        starter_code="def topKFrequent(nums: list[int], k: int) -> list[int]:\n    pass\n",
        solution_code="def topKFrequent(nums: list[int], k: int) -> list[int]:\n    from collections import Counter\n    counts = Counter(nums)\n    sorted_items = sorted(counts.keys(), key=lambda x: -counts[x])\n    return sorted_items[:k]\n",
        test_cases=[
            {"input": [[1, 1, 1, 2, 2, 3], 2], "expected": [1, 2]},
            {"input": [[1], 1], "expected": [1]},
            {"input": [[4, 4, 4, 6, 6, 8, 8, 8, 8], 2], "expected": [8, 4]},
            {"input": [[5, 2, 5, 3, 5, 3, 1], 2], "expected": [5, 3]},
        ],
        hints=["Count frequencies, then use a heap or bucket sort to extract top k."],
        leetcode_id=347,
    ))

    # 8. Sort Characters By Frequency
    problems.append(make_problem(
        pid="ds-m-sort-characters-frequency",
        title="Sort Characters By Frequency",
        wing_id="data-structures",
        floor=118,
        difficulty="medium",
        visualizerType="array",
        monster_name="Resonance Harpy",
        monster_title="Singer of Repetitive Chants",
        monster_sprite="wraith",
        monster_color="#ec4899",
        monster_attack="Harmonic Shriek",
        monster_quote="My highest frequency screams were gathered first!",
        description="Given a string `s`, sort it in decreasing order based on the frequency of the characters. If two characters have the same frequency, sort them alphabetically.",
        examples=[
            {"input": "s = \"tree\"", "output": "\"eert\""},
            {"input": "s = \"cccaaa\"", "output": "\"aaaccc\""},
            {"input": "s = \"Aabb\"", "output": "\"bbAa\""}
        ],
        constraints=["1 <= len(s) <= 5 * 10^5", "s consists of uppercase and lowercase English letters and digits"],
        function_name="frequencySort",
        starter_code="def frequencySort(s: str) -> str:\n    pass\n",
        solution_code="def frequencySort(s: str) -> str:\n    from collections import Counter\n    counts = Counter(s)\n    sorted_chars = sorted(counts.keys(), key=lambda ch: (-counts[ch], ch))\n    return ''.join(ch * counts[ch] for ch in sorted_chars)\n",
        test_cases=[
            {"input": ["tree"], "expected": "eert"},
            {"input": ["cccaaa"], "expected": "aaaccc"},
            {"input": ["Aabb"], "expected": "bbAa"},
            {"input": ["z"], "expected": "z"},
        ],
        hints=["Count character frequencies and sort using frequency and character."],
        leetcode_id=451,
    ))

    # 9. 132 Pattern
    problems.append(make_problem(
        pid="ds-m-132-pattern",
        title="132 Pattern Hunter",
        wing_id="data-structures",
        floor=119,
        difficulty="medium",
        visualizerType="stack",
        monster_name="Valley Stalker",
        monster_title="Seeker of the Hidden Peak-Valley",
        monster_sprite="lich",
        monster_color="#38bdf8",
        monster_attack="Triple Valley Pierce",
        monster_quote="The monotonic stack caught the 1-3-2 inversion!",
        description="Given an array of `n` integers `nums`, a 132 pattern is a subsequence of three integers `nums[i]`, `nums[j]` and `nums[k]` such that `i < j < k` and `nums[i] < nums[k] < nums[j]`. Return `True` if there is a 132 pattern in `nums`, otherwise return `False`.",
        examples=[
            {"input": "nums = [1,2,3,4]", "output": "False"},
            {"input": "nums = [3,1,4,2]", "output": "True"},
            {"input": "nums = [-1,3,2,0]", "output": "True"}
        ],
        constraints=["1 <= len(nums) <= 2 * 10^5", "-10^9 <= nums[i] <= 10^9"],
        function_name="find132pattern",
        starter_code="def find132pattern(nums: list[int]) -> bool:\n    pass\n",
        solution_code="def find132pattern(nums: list[int]) -> bool:\n    stack = []\n    s3 = float('-inf')\n    for num in reversed(nums):\n        if num < s3:\n            return True\n        while stack and stack[-1] < num:\n            s3 = stack.pop()\n        stack.append(num)\n    return False\n",
        test_cases=[
            {"input": [[1, 2, 3, 4]], "expected": False},
            {"input": [[3, 1, 4, 2]], "expected": True},
            {"input": [[-1, 3, 2, 0]], "expected": True},
            {"input": [[1, 0, 1, -4, -3]], "expected": False},
        ],
        hints=["Traverse backwards with a monotonic decreasing stack, maintaining candidate for '2'."],
        leetcode_id=456,
    ))

    # 10. Asteroid Collision
    problems.append(make_problem(
        pid="ds-m-asteroid-collision",
        title="Asteroid Collision Simulation",
        wing_id="data-structures",
        floor=120,
        difficulty="medium",
        visualizerType="stack",
        monster_name="Cosmic Crusher",
        monster_title="Smasher of Orbiting Debris",
        monster_sprite="golem",
        monster_color="#e11d48",
        monster_attack="Meteor Crash",
        monster_quote="My colliding rocks pulverized themselves on your stack!",
        description="We are given an array `asteroids` of integers representing asteroids in a row. The absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). If two asteroids meet, the smaller one explodes. If both are the same size, both explode. Two asteroids moving in the same direction will never meet. Return the state of the asteroids after all collisions.",
        examples=[
            {"input": "asteroids = [5,10,-5]", "output": "[5,10]"},
            {"input": "asteroids = [8,-8]", "output": "[]"},
            {"input": "asteroids = [10,2,-5]", "output": "[10]"}
        ],
        constraints=["2 <= len(asteroids) <= 10^4", "-1000 <= asteroids[i] <= 1000", "asteroids[i] != 0"],
        function_name="asteroidCollision",
        starter_code="def asteroidCollision(asteroids: list[int]) -> list[int]:\n    pass\n",
        solution_code="def asteroidCollision(asteroids: list[int]) -> list[int]:\n    stack = []\n    for ast in asteroids:\n        alive = True\n        while alive and ast < 0 and stack and stack[-1] > 0:\n            if stack[-1] < -ast:\n                stack.pop()\n            elif stack[-1] == -ast:\n                stack.pop()\n                alive = False\n            else:\n                alive = False\n        if alive:\n            stack.append(ast)\n    return stack\n",
        test_cases=[
            {"input": [[5, 10, -5]], "expected": [5, 10]},
            {"input": [[8, -8]], "expected": []},
            {"input": [[10, 2, -5]], "expected": [10]},
            {"input": [[-2, -1, 1, 2]], "expected": [-2, -1, 1, 2]},
        ],
        hints=["Use a stack to simulate collisions between right-moving and left-moving asteroids."],
        leetcode_id=735,
    ))

    return problems
