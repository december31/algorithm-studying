"""
Bit Manipulation Medium Problems - Part 3 (Floors 541 to 555 - 15 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_bit_medium_part3():
    problems = []

    # 41. Maximum Compatibility Score Sum
    problems.append(make_problem(
        pid="bit-m-max-compatibility-score", title="Maximum Compatibility Score (Bitmask Assignment)",
        wing_id="bit-manipulation", floor=541, difficulty="medium", visualizer_type="array",
        monster_name="Affinity Spectre", monster_title="Harmonizer of Binary Profiles",
        monster_sprite="spectre", monster_color="#38bdf8", monster_attack="Affinity Pulse",
        monster_quote="Max total compatibility score across paired student-mentor masks!",
        description="There is a survey with `m` binary questions. Given `students` and `mentors` (both `m x n`). The score of a pair is the number of matching answers. Return the maximum compatibility score sum assigning each student to one mentor.",
        examples=[{"input": "students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]]", "output": "8"}],
        constraints=["m == students.length == mentors.length <= 8", "1 <= n <= 8"],
        function_name="maxCompatibilityMatch",
        starter_code="def maxCompatibilityMatch(students: list[list[int]], mentors: list[list[int]]) -> int:\n    pass\n",
        solution_code="def maxCompatibilityMatch(students: list[list[int]], mentors: list[list[int]]) -> int:\n    m, n = len(students), len(students[0])\n    scores = [[sum(students[i][k] == mentors[j][k] for k in range(n)) for j in range(m)] for i in range(m)]\n    memo = {}\n    def dfs(s_idx, mask):\n        if s_idx == m: return 0\n        if mask in memo: return memo[mask]\n        res = 0\n        for j in range(m):\n            if not (mask & (1 << j)):\n                res = max(res, scores[s_idx][j] + dfs(s_idx + 1, mask | (1 << j)))\n        memo[mask] = res\n        return res\n    return dfs(0, 0)\n",
        test_cases=[{"input": [[[1, 1, 0], [1, 0, 1], [0, 0, 1]], [[1, 0, 0], [0, 0, 1], [1, 1, 0]]], "expected": 8}, {"input": [[[0, 0], [0, 0], [0, 0]], [[1, 1], [1, 1], [1, 1]]], "expected": 0}],
        hints=["Bitmask memoization over assigned mentors mask with current student index."],
        leetcode_id=1947
    ))

    # 42. Special Permutations
    problems.append(make_problem(
        pid="bit-m-special-permutations-dp", title="Special Permutations (Bitmask Hamiltonian DP)",
        wing_id="bit-manipulation", floor=542, difficulty="medium", visualizer_type="array",
        monster_name="Divisibility Lich", monster_title="Weaver of Permutational Divisibility",
        monster_sprite="lich", monster_color="#8b5cf6", monster_attack="Divisibility Beam",
        monster_quote="Count of special permutations where every adjacent pair divides modulo 10^9+7!",
        description="Given an array `nums` of `n` distinct positive integers. A permutation is special if for all adjacent indices `i`: `nums[i] % nums[i+1] == 0` or `nums[i+1] % nums[i] == 0`. Return the total number of special permutations modulo `10^9 + 7`.",
        examples=[{"input": "nums = [2,3,6]", "output": "2"}, {"input": "nums = [1,4,3]", "output": "2"}],
        constraints=["2 <= nums.length <= 14"],
        function_name="specialPerm",
        starter_code="def specialPerm(nums: list[int]) -> int:\n    pass\n",
        solution_code="def specialPerm(nums: list[int]) -> int:\n    n = len(nums)\n    MOD = 10**9 + 7\n    memo = {}\n    def dfs(mask, last_idx):\n        if mask == (1 << n) - 1: return 1\n        state = (mask, last_idx)\n        if state in memo: return memo[state]\n        res = 0\n        for j in range(n):\n            if not (mask & (1 << j)):\n                if last_idx == -1 or nums[j] % nums[last_idx] == 0 or nums[last_idx] % nums[j] == 0:\n                    res = (res + dfs(mask | (1 << j), j)) % MOD\n        memo[state] = res\n        return res\n    return dfs(0, -1)\n",
        test_cases=[{"input": [[2, 3, 6]], "expected": 2}, {"input": [[1, 4, 3]], "expected": 2}],
        hints=["DP state is (visited_mask, last_index)."],
        leetcode_id=2741
    ))

    # 43. Can I Win
    problems.append(make_problem(
        pid="bit-m-can-i-win-minimax", title="Can I Win (Minimax Bitmask Memoization)",
        wing_id="bit-manipulation", floor=543, difficulty="medium", visualizer_type="array",
        monster_name="Game Theory Sphinx", monster_title="Oracle of Forced Win States",
        monster_sprite="sphinx", monster_color="#ef4444", monster_attack="Forced Checkmate",
        monster_quote="Can the first player force a win under optimal play?",
        description="In the \"100 game\", two players take turns adding, to a running total, any integer from `1` to `maxChoosableInteger`. Each integer can only be used once. The player who first causes the running total to reach or exceed `desiredTotal` wins. Return `True` if the first player can force a win, otherwise `False`.",
        examples=[{"input": "maxChoosableInteger = 10, desiredTotal = 11", "output": "False"}, {"input": "maxChoosableInteger = 10, desiredTotal = 0", "output": "True"}, {"input": "maxChoosableInteger = 10, desiredTotal = 1", "output": "True"}],
        constraints=["1 <= maxChoosableInteger <= 20", "0 <= desiredTotal <= 300"],
        function_name="canIWinGame",
        starter_code="def canIWinGame(maxChoosableInteger: int, desiredTotal: int) -> bool:\n    pass\n",
        solution_code="def canIWinGame(maxChoosableInteger: int, desiredTotal: int) -> bool:\n    if desiredTotal <= 0: return True\n    total_sum = (maxChoosableInteger * (maxChoosableInteger + 1)) // 2\n    if total_sum < desiredTotal: return False\n    memo = {}\n    def dfs(mask, rem):\n        if mask in memo: return memo[mask]\n        for i in range(1, maxChoosableInteger + 1):\n            if not (mask & (1 << i)):\n                if i >= rem or not dfs(mask | (1 << i), rem - i):\n                    memo[mask] = True\n                    return True\n        memo[mask] = False\n        return False\n    return dfs(0, desiredTotal)\n",
        test_cases=[{"input": [10, 11], "expected": False}, {"input": [10, 0], "expected": True}, {"input": [10, 1], "expected": True}],
        hints=["Bitmask memoization: if choosing integer i forces opponent into a losing state (!dfs), current player wins."],
        leetcode_id=464
    ))

    # 44. Find the Longest Substring Containing Vowels in Even Counts
    problems.append(make_problem(
        pid="bit-m-longest-substring-even-vowels", title="Longest Substring with Even Vowel Counts",
        wing_id="bit-manipulation", floor=544, difficulty="medium", visualizer_type="array",
        monster_name="Vocalic Siren", monster_title="Mistress of Parity Harmonics",
        monster_sprite="wraith", monster_color="#ec4899", monster_attack="Siren Song",
        monster_quote="Longest substring where each of 'a, e, i, o, u' appears an even number of times!",
        description="Given the string `s`, return the size of the longest substring containing each vowel ('a', 'e', 'i', 'o', 'u') an even number of times.",
        examples=[{"input": "s = \"eleetminicoworoep\"", "output": "13"}, {"input": "s = \"leetcodeisgreat\"", "output": "5"}, {"input": "s = \"bcbcbc\"", "output": "6"}],
        constraints=["1 <= s.length <= 500000"],
        function_name="findTheLongestSubstring",
        starter_code="def findTheLongestSubstring(s: str) -> int:\n    pass\n",
        solution_code="def findTheLongestSubstring(s: str) -> int:\n    vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}\n    first_seen = {0: -1}\n    mask = 0\n    max_len = 0\n    for i, ch in enumerate(s):\n        if ch in vowels:\n            mask ^= (1 << vowels[ch])\n        if mask in first_seen:\n            max_len = max(max_len, i - first_seen[mask])\n        else:\n            first_seen[mask] = i\n    return max_len\n",
        test_cases=[{"input": ["eleetminicoworoep"], "expected": 13}, {"input": ["leetcodeisgreat"], "expected": 5}, {"input": ["bcbcbc"], "expected": 6}],
        hints=["Maintain a 5-bit parity mask for the vowels. Whenever the same mask reappears at j, substring (first_seen[mask], j] has all even vowel counts."],
        leetcode_id=1371
    ))

    # 45. Beautiful Arrangement
    problems.append(make_problem(
        pid="bit-m-beautiful-arrangement-bitmask", title="Beautiful Arrangement (Bitmask DP)",
        wing_id="bit-manipulation", floor=545, difficulty="medium", visualizer_type="array",
        monster_name="Permutational Golem", monster_title="Builder of Divisible Alignments",
        monster_sprite="golem", monster_color="#10b981", monster_attack="Divisibility Lock",
        monster_quote="Number of beautiful 1..n arrangements satisfying index divisibility!",
        description="Suppose you have `n` integers labeled 1 through `n`. A permutation of those `n` integers `perm` is considered a beautiful arrangement if for every `i` (1 <= i <= n): `perm[i] % i == 0` or `i % perm[i] == 0`. Given `n`, return the number of the beautiful arrangements.",
        examples=[{"input": "n = 2", "output": "2"}, {"input": "n = 1", "output": "1"}],
        constraints=["1 <= n <= 15"],
        function_name="countArrangementBitmask",
        starter_code="def countArrangementBitmask(n: int) -> int:\n    pass\n",
        solution_code="def countArrangementBitmask(n: int) -> int:\n    memo = {}\n    def dfs(mask):\n        if mask == (1 << n) - 1: return 1\n        if mask in memo: return memo[mask]\n        pos = bin(mask).count('1') + 1\n        ans = 0\n        for num in range(1, n + 1):\n            if not (mask & (1 << (num - 1))):\n                if num % pos == 0 or pos % num == 0:\n                    ans += dfs(mask | (1 << (num - 1)))\n        memo[mask] = ans\n        return ans\n    return dfs(0)\n",
        test_cases=[{"input": [2], "expected": 2}, {"input": [1], "expected": 1}, {"input": [3], "expected": 3}],
        hints=["Bitmask DP: current placement position is bit_count(mask) + 1."],
        leetcode_id=526
    ))

    # 46. Number of Wonderful Substrings
    problems.append(make_problem(
        pid="bit-m-number-wonderful-substrings", title="Number of Wonderful Substrings (At Most 1 Odd)",
        wing_id="bit-manipulation", floor=546, difficulty="medium", visualizer_type="array",
        monster_name="Parity Chimera", monster_title="Seeker of At-Most-One Odd Letter Frequencies",
        monster_sprite="manticore", monster_color="#f59e0b", monster_attack="Parity Claws",
        monster_quote="Substrings where at most one letter appears an odd number of times counted!",
        description="A wonderful string is a string where at most one letter appears an odd number of times. Given a string `word` that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in `word`.",
        examples=[{"input": "word = \"aba\"", "output": "4"}, {"input": "word = \"aabb\"", "output": "9"}, {"input": "word = \"he\"", "output": "2"}],
        constraints=["1 <= word.length <= 100000", "word consists only of letters 'a' to 'j'"],
        function_name="wonderfulSubstrings",
        starter_code="def wonderfulSubstrings(word: str) -> int:\n    pass\n",
        solution_code="def wonderfulSubstrings(word: str) -> int:\n    from collections import defaultdict\n    count = [0] * 1024\n    count[0] = 1\n    mask = 0\n    ans = 0\n    for ch in word:\n        mask ^= (1 << (ord(ch) - ord('a')))\n        ans += count[mask]\n        for i in range(10):\n            ans += count[mask ^ (1 << i)]\n        count[mask] += 1\n    return ans\n",
        test_cases=[{"input": ["aba"], "expected": 4}, {"input": ["aabb"], "expected": 9}],
        hints=["10-bit prefix parity mask: check matching prefix (0 odd) and masks differing by 1 bit (1 odd)."],
        leetcode_id=1915
    ))

    # 47. Maximum Score Words Formed by Letters
    problems.append(make_problem(
        pid="bit-m-max-score-words", title="Max Score Words Formed by Letters",
        wing_id="bit-manipulation", floor=547, difficulty="medium", visualizer_type="array",
        monster_name="Lexicon Dragon", monster_title="Hoarder of Letter Tiles",
        monster_sprite="dragon", monster_color="#06b6d4", monster_attack="Scrabble Fire",
        monster_quote="Maximum letter score achieved using available inventory!",
        description="Given a list of `words`, list of single `letters` (might be repeating) and `score` of every character from 'a' to 'z'. Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used multiple times).",
        examples=[{"input": "words = [\"dog\",\"cat\",\"dad\",\"good\"], letters = [\"a\",\"a\",\"c\",\"d\",\"d\",\"d\",\"g\",\"o\",\"o\"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]", "output": "23"}],
        constraints=["1 <= words.length <= 14"],
        function_name="maxScoreWords",
        starter_code="def maxScoreWords(words: list[str], letters: list[str], score: list[int]) -> int:\n    pass\n",
        solution_code="def maxScoreWords(words: list[str], letters: list[str], score: list[int]) -> int:\n    from collections import Counter\n    avail = Counter(letters)\n    n = len(words)\n    max_val = 0\n    for mask in range(1 << n):\n        needed = Counter()\n        word_score = 0\n        for i in range(n):\n            if (mask & (1 << i)):\n                for ch in words[i]:\n                    needed[ch] += 1\n                    word_score += score[ord(ch) - ord('a')]\n        if all(needed[ch] <= avail[ch] for ch in needed):\n            max_val = max(max_val, word_score)\n    return max_val\n",
        test_cases=[{"input": [["dog", "cat", "dad", "good"], ["a", "a", "c", "d", "d", "d", "g", "o", "o"], [1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], "expected": 23}],
        hints=["Since words.length <= 14, iterate all 2^14 subsets using bitmasks and check letter budget."],
        leetcode_id=1255
    ))

    # 48. Maximum OR with K Doublings
    problems.append(make_problem(
        pid="bit-m-maximum-or-k-doublings", title="Maximum OR of Array with K Shifts",
        wing_id="bit-manipulation", floor=548, difficulty="medium", visualizer_type="array",
        monster_name="Bit Shift Titan", monster_title="Multiplier of Binary Values",
        monster_sprite="titan", monster_color="#ef4444", monster_attack="Bit Shift Surge",
        monster_quote="Maximum bitwise OR achieved by shifting one element left by k bits!",
        description="You are given a 0-indexed integer array `nums` of length `n` and an integer `k`. In an operation, you can multiply any `nums[i]` by 2. Return the maximum possible value of `nums[0] | nums[1] | ... | nums[n - 1]` that can be obtained after applying the operation at most `k` times.",
        examples=[{"input": "nums = [12,9], k = 1", "output": "30"}, {"input": "nums = [8,1,2], k = 2", "output": "35"}],
        constraints=["1 <= nums.length <= 100000", "1 <= k <= 15"],
        function_name="maximumOr",
        starter_code="def maximumOr(nums: list[int], k: int) -> int:\n    pass\n",
        solution_code="def maximumOr(nums: list[int], k: int) -> int:\n    n = len(nums)\n    pref = [0] * (n + 1)\n    suff = [0] * (n + 1)\n    for i in range(n): pref[i + 1] = pref[i] | nums[i]\n    for i in range(n - 1, -1, -1): suff[i] = suff[i + 1] | nums[i]\n    ans = 0\n    for i in range(n):\n        ans = max(ans, pref[i] | (nums[i] << k) | suff[i + 1])\n    return ans\n",
        test_cases=[{"input": [[12, 9], 1], "expected": 30}, {"input": [[8, 1, 2], 2], "expected": 35}],
        hints=["Greedy property: all k multiplications by 2 (left shifts) should be applied to the same single number."],
        leetcode_id=2680
    ))

    # 49. Maximum Number of Achievable Transfer Requests
    problems.append(make_problem(
        pid="bit-m-max-achievable-transfers", title="Max Achievable Transfer Requests",
        wing_id="bit-manipulation", floor=549, difficulty="medium", visualizer_type="array",
        monster_name="Relocation Specter", monster_title="Balancer of Net Building Capacities",
        monster_sprite="spectre", monster_color="#38bdf8", monster_attack="Relocation Loop",
        monster_quote="Maximum subset of transfer requests maintaining zero net building changes!",
        description="We have `n` buildings numbered from 0 to `n - 1`. Each building has a number of employees. Given `requests` where `requests[i] = [fromi, toi]`. Return the maximum number of achievable requests where every building ends up with the same net number of employees.",
        examples=[{"input": "n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]", "output": "5"}, {"input": "n = 3, requests = [[0,0],[1,2],[2,1]]", "output": "3"}],
        constraints=["1 <= n <= 20", "1 <= requests.length <= 16"],
        function_name="maximumRequests",
        starter_code="def maximumRequests(n: int, requests: list[list[int]]) -> int:\n    pass\n",
        solution_code="def maximumRequests(n: int, requests: list[list[int]]) -> int:\n    m = len(requests)\n    ans = 0\n    for mask in range(1 << m):\n        net = [0] * n\n        count = 0\n        for i in range(m):\n            if (mask & (1 << i)):\n                count += 1\n                net[requests[i][0]] -= 1\n                net[requests[i][1]] += 1\n        if all(x == 0 for x in net):\n            ans = max(ans, count)\n    return ans\n",
        test_cases=[{"input": [5, [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]], "expected": 5}, {"input": [3, [[0, 0], [1, 2], [2, 1]]], "expected": 3}],
        hints=["Since requests.length <= 16, iterate all 2^16 subsets of requests and verify all building net changes are 0."],
        leetcode_id=1601
    ))

    # 50. Smallest Sufficient Team
    problems.append(make_problem(
        pid="bit-m-smallest-sufficient-team", title="Smallest Sufficient Team (Set Cover Bitmask DP)",
        wing_id="bit-manipulation", floor=550, difficulty="medium", visualizer_type="array",
        monster_name="Synergy Sovereign", monster_title="Recruiter of Minimal Cover Teams",
        monster_sprite="boss", monster_color="#8b5cf6", monster_attack="Synergy Alignment",
        monster_quote="Smallest team of people covering all required skills assembled!",
        description="In a project, you have a list of `req_skills`, and a list of `people`. The `i`-th person `people[i]` contains a list of skills that the person has. A sufficient team is a set of people such that for every required skill, there is at least one person with that skill. Return any sufficient team of the smallest possible size.",
        examples=[{"input": "req_skills = [\"java\",\"nodejs\",\"reactjs\"], people = [[\"java\"],[\"nodejs\"],[\"nodejs\",\"reactjs\"]]", "output": "[0,2]"}],
        constraints=["1 <= req_skills.length <= 16", "1 <= people.length <= 60"],
        function_name="smallestSufficientTeam",
        starter_code="def smallestSufficientTeam(req_skills: list[str], people: list[list[str]]) -> list[int]:\n    pass\n",
        solution_code="def smallestSufficientTeam(req_skills: list[str], people: list[list[str]]) -> list[int]:\n    skill_map = {s: i for i, s in enumerate(req_skills)}\n    target = (1 << len(req_skills)) - 1\n    dp = {0: []}\n    for person_idx, skills in enumerate(people):\n        p_mask = 0\n        for s in skills:\n            if s in skill_map: p_mask |= (1 << skill_map[s])\n        if p_mask == 0: continue\n        curr_items = list(dp.items())\n        for mask, team in curr_items:\n            comb = mask | p_mask\n            if comb not in dp or len(team) + 1 < len(dp[comb]):\n                dp[comb] = team + [person_idx]\n    return sorted(dp[target])\n",
        test_cases=[{"input": [["java", "nodejs", "reactjs"], [["java"], ["nodejs"], [["nodejs", "reactjs"]][0]]], "expected": [0, 2]}],
        hints=["Bitmask DP: dp[skill_mask] = minimum list of people covering skill_mask."],
        leetcode_id=1125
    ))

    # 51. Minimum Cost to Connect Two Groups of Points
    problems.append(make_problem(
        pid="bit-m-connect-two-groups-cost", title="Minimum Cost to Connect Two Groups of Points",
        wing_id="bit-manipulation", floor=551, difficulty="medium", visualizer_type="array",
        monster_name="Bipartite Weaver", monster_title="Coupler of Two Finite Point Sets",
        monster_sprite="gargoyle", monster_color="#10b981", monster_attack="Tether Quake",
        monster_quote="Minimum connection cost ensuring every point in both groups is connected!",
        description="You are given two groups of points: group 1 has `sz1` points, and group 2 has `sz2` points. `cost[i][j]` is the cost of connecting point `i` of group 1 and point `j` of group 2. Return the minimum cost to connect the two groups so every point has at least one connected edge.",
        examples=[{"input": "cost = [[15,96],[36,2]]", "output": "17"}, {"input": "cost = [[1,3,5],[4,1,1],[1,5,3]]", "output": "4"}],
        constraints=["sz1 <= 12", "sz2 <= 12"],
        function_name="connectTwoGroups",
        starter_code="def connectTwoGroups(cost: list[list[int]]) -> int:\n    pass\n",
        solution_code="def connectTwoGroups(cost: list[list[int]]) -> int:\n    sz1, sz2 = len(cost), len(cost[0])\n    min_col_cost = [min(cost[i][j] for i in range(sz1)) for j in range(sz2)]\n    memo = {}\n    def dfs(i, mask):\n        if (i, mask) in memo: return memo[(i, mask)]\n        if i == sz1:\n            # Connect any remaining unconnected nodes in group 2 to their cheapest group 1 node\n            ans = sum(min_col_cost[j] for j in range(sz2) if not (mask & (1 << j)))\n            return ans\n        res = float('inf')\n        for j in range(sz2):\n            res = min(res, cost[i][j] + dfs(i + 1, mask | (1 << j)))\n        memo[(i, mask)] = res\n        return res\n    return dfs(0, 0)\n",
        test_cases=[{"input": [[[15, 96], [36, 2]]], "expected": 17}, {"input": [[[1, 3, 5], [4, 1, 1], [1, 5, 3]]], "expected": 4}],
        hints=["DP state: (current_node_in_group_1, visited_mask_of_group_2). For unconnected group 2 nodes, pick cheapest edge."],
        leetcode_id=1595
    ))

    # 52. Distribute Repeating Integers
    problems.append(make_problem(
        pid="bit-m-distribute-repeating-integers", title="Distribute Repeating Integers (Subset Sum DP)",
        wing_id="bit-manipulation", floor=552, difficulty="medium", visualizer_type="array",
        monster_name="Quota Golem", monster_title="Fulfiller of Customer Demands",
        monster_sprite="golem", monster_color="#f59e0b", monster_attack="Quota Slam",
        monster_quote="Can all customer quantity demands be satisfied by integer frequencies?",
        description="You are given an array of `n` integers `nums` and an array of `m` customer orders `quantity` where the `i`-th customer requires `quantity[i]` copies of any single value. Return `True` if it is possible to distribute `nums` such that the `i`-th customer is satisfied.",
        examples=[{"input": "nums = [1,2,3,4], quantity = [2]", "output": "False"}, {"input": "nums = [1,2,3,3], quantity = [2]", "output": "True"}],
        constraints=["1 <= quantity.length <= 10"],
        function_name="canDistribute",
        starter_code="def canDistribute(nums: list[int], quantity: list[int]) -> bool:\n    pass\n",
        solution_code="def canDistribute(nums: list[int], quantity: list[int]) -> bool:\n    from collections import Counter\n    counts = sorted(Counter(nums).values(), reverse=True)\n    m = len(quantity)\n    quantity.sort(reverse=True)\n    def backtrack(cust_idx):\n        if cust_idx == m: return True\n        q = quantity[cust_idx]\n        for i in range(len(counts)):\n            if counts[i] >= q:\n                counts[i] -= q\n                if backtrack(cust_idx + 1): return True\n                counts[i] += q\n            if counts[i] == 0: break\n        return False\n    return backtrack(0)\n",
        test_cases=[{"input": [[1, 2, 3, 4], [2]], "expected": False}, {"input": [[1, 2, 3, 3], [2]], "expected": True}],
        hints=["Sort customer demands descending and backtrack over frequency buckets with pruning."],
        leetcode_id=1655
    ))

    # 53. Longest Subarray With Equal 0 and 1
    problems.append(make_problem(
        pid="bit-m-contiguous-equal-zeros-ones", title="Contiguous Array with Equal 0s and 1s",
        wing_id="bit-manipulation", floor=553, difficulty="medium", visualizer_type="array",
        monster_name="Equilibrium Sphinx", monster_title="Measurer of Balanced Binary Segments",
        monster_sprite="sphinx", monster_color="#06b6d4", monster_attack="Binary Equilibrium",
        monster_quote="Longest contiguous subarray with equal number of 0s and 1s measured!",
        description="Given a binary array `nums`, return the maximum length of a contiguous subarray with an equal number of `0` and `1`.",
        examples=[{"input": "nums = [0,1]", "output": "2"}, {"input": "nums = [0,1,0]", "output": "2"}],
        constraints=["1 <= nums.length <= 100000"],
        function_name="findMaxLength",
        starter_code="def findMaxLength(nums: list[int]) -> int:\n    pass\n",
        solution_code="def findMaxLength(nums: list[int]) -> int:\n    seen = {0: -1}\n    curr = 0\n    max_len = 0\n    for i, x in enumerate(nums):\n        curr += (1 if x == 1 else -1)\n        if curr in seen:\n            max_len = max(max_len, i - seen[curr])\n        else:\n            seen[curr] = i\n    return max_len\n",
        test_cases=[{"input": [[0, 1]], "expected": 2}, {"input": [[0, 1, 0]], "expected": 2}],
        hints=["Treat 0 as -1 and 1 as +1. Problem reduces to finding longest subarray with sum 0."],
        leetcode_id=525
    ))

    # 54. Minimum Subarray Length with Bitwise OR at Least K
    problems.append(make_problem(
        pid="bit-m-min-subarray-or-k", title="Shortest Subarray with OR at Least K",
        wing_id="bit-manipulation", floor=554, difficulty="medium", visualizer_type="array",
        monster_name="Threshold Drake", monster_title="Accumulator of Bit Capacity Thresholds",
        monster_sprite="dragon", monster_color="#ec4899", monster_attack="Threshold Flare",
        monster_quote="Shortest subarray whose bitwise OR meets or exceeds k!",
        description="You are given an array `nums` of non-negative integers and an integer `k`. A subarray is called special if the bitwise OR of all its elements is at least `k`. Return the minimum length of a special non-empty subarray, or `-1` if none exists.",
        examples=[{"input": "nums = [1,2,3], k = 2", "output": "1"}, {"input": "nums = [2,1,8], k = 10", "output": "3"}, {"input": "nums = [1,2], k = 0", "output": "1"}],
        constraints=["1 <= nums.length <= 50", "0 <= nums[i] <= 50", "0 <= k <= 64"],
        function_name="minimumSubarrayLength",
        starter_code="def minimumSubarrayLength(nums: list[int], k: int) -> int:\n    pass\n",
        solution_code="def minimumSubarrayLength(nums: list[int], k: int) -> int:\n    n = len(nums)\n    ans = float('inf')\n    for i in range(n):\n        curr_or = 0\n        for j in range(i, n):\n            curr_or |= nums[j]\n            if curr_or >= k:\n                ans = min(ans, j - i + 1)\n                break\n    return ans if ans != float('inf') else -1\n",
        test_cases=[{"input": [[1, 2, 3], 2], "expected": 1}, {"input": [[2, 1, 8], 10], "expected": 3}, {"input": [[1, 2], 0], "expected": 1}],
        hints=["Slide window tracking 32-bit count array to maintain bitwise OR dynamically."],
        leetcode_id=3097
    ))

    # 55. Single Number (Find Unique in 4-Tuples)
    problems.append(make_problem(
        pid="bit-m-single-number-quad", title="Single Number Among Quadruplicates (Mod 4)",
        wing_id="bit-manipulation", floor=555, difficulty="medium", visualizer_type="array",
        monster_name="Quadruple Warden", monster_title="Canceler of 4-Fold Bit Repetitions",
        monster_sprite="boss", monster_color="#ef4444", monster_attack="Quad Cleave",
        monster_quote="Single unique element located among values appearing 4 times!",
        description="Given an integer array `nums` where every element appears four times except for one which appears exactly once. Find and return the single element.",
        examples=[{"input": "nums = [1,1,1,1,5]", "output": "5"}, {"input": "nums = [7,2,2,2,2]", "output": "7"}],
        constraints=["1 <= nums.length <= 50000"],
        function_name="singleNumberQuad",
        starter_code="def singleNumberQuad(nums: list[int]) -> int:\n    pass\n",
        solution_code="def singleNumberQuad(nums: list[int]) -> int:\n    ans = 0\n    for bit in range(32):\n        cnt = sum((x >> bit) & 1 for x in nums)\n        if cnt % 4 != 0:\n            ans |= (1 << bit)\n    return ans\n",
        test_cases=[{"input": [[1, 1, 1, 1, 5]], "expected": 5}, {"input": [[7, 2, 2, 2, 2]], "expected": 7}],
        hints=["Accumulate set bit counts modulo 4 across each bit position."],
        leetcode_id=0
    ))

    return problems
