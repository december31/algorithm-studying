from scripts.problem_data.common import make_problem

def get_bit_hard_part2():
    problems = []

    # 86. Split Array With Same Average (LC 805)
    problems.append(make_problem(
        pid="bit-h-split-array-same-avg", title="Split Array with Same Average",
        wing_id="bit-manipulation", floor=586, difficulty="hard", visualizer_type="array",
        monster_name="Equi-Average Chimera", monster_title="Harmonizer of Mean Values",
        monster_sprite="dragon", monster_color="#ef4444", monster_attack="Balanced Partition Surge",
        monster_quote="Divide the hoard in two non-empty tribes of identical average!",
        description="You are given an integer array `nums`. You want to split the array into two non-empty arrays `A` and `B` such that `average(A) == average(B)`. Return `True` if you can achieve that, or `False` otherwise.",
        examples=[
            {"input": "nums = [1,2,3,4,5,6,7,8]", "output": "True"},
            {"input": "nums = [3,1]", "output": "False"}
        ],
        constraints=["1 <= nums.length <= 30", "0 <= nums[i] <= 10^4"],
        function_name="splitArraySameAverage",
        starter_code="def splitArraySameAverage(nums: list[int]) -> bool:\n    pass\n",
        solution_code="def splitArraySameAverage(nums: list[int]) -> bool:\n    n = len(nums)\n    if n <= 1: return False\n    total = sum(nums)\n    mid = n // 2\n    left, right = nums[:mid], nums[mid:]\n    left_sums = [set() for _ in range(len(left) + 1)]\n    left_sums[0].add(0)\n    for x in left:\n        for sz in range(len(left_sums) - 1, 0, -1):\n            for s in left_sums[sz - 1]:\n                left_sums[sz].add(s + x)\n    right_sums = [set() for _ in range(len(right) + 1)]\n    right_sums[0].add(0)\n    for x in right:\n        for sz in range(len(right_sums) - 1, 0, -1):\n            for s in right_sums[sz - 1]:\n                right_sums[sz].add(s + x)\n    for k in range(1, mid + 1):\n        if (total * k) % n == 0:\n            target = (total * k) // n\n            for l_sz in range(min(k, len(left)) + 1):\n                r_sz = k - l_sz\n                if r_sz <= len(right):\n                    for s1 in left_sums[l_sz]:\n                        if (target - s1) in right_sums[r_sz]:\n                            return True\n    return False\n",
        test_cases=[
            {"input": [[1,2,3,4,5,6,7,8]], "expected": True},
            {"input": [[3,1]], "expected": False}
        ],
        hints=["Condition average(A) == total / n implies sum(A) = total * len(A) / n must be an integer. Check subset sums with meet-in-the-middle."],
        leetcode_id=805
    ))

    # 87. Triples with Bitwise AND Equal To Zero (LC 982)
    problems.append(make_problem(
        pid="bit-h-triples-and-zero", title="Triples with Bitwise AND Equal to Zero",
        wing_id="bit-manipulation", floor=587, difficulty="hard", visualizer_type="array",
        monster_name="Null-AND Cerberus", monster_title="Eater of Triple Bitwise Conjunctions",
        monster_sprite="boss", monster_color="#8b5cf6", monster_attack="Zero Bit Annihilation",
        monster_quote="Three numbers must share no common 1-bit when fused by bitwise AND!",
        description="Given an integer array `nums`, return the number of AND triples `(i, j, k)` such that `0 <= i < nums.length`, `0 <= j < nums.length`, `0 <= k < nums.length`, and `nums[i] & nums[j] & nums[k] == 0`.",
        examples=[
            {"input": "nums = [2,1,3]", "output": "12"},
            {"input": "nums = [0,0,0]", "output": "27"}
        ],
        constraints=["1 <= nums.length <= 1000", "0 <= nums[i] < 2^16"],
        function_name="countTriplets",
        starter_code="def countTriplets(nums: list[int]) -> int:\n    pass\n",
        solution_code="def countTriplets(nums: list[int]) -> int:\n    from collections import Counter\n    pair_counts = Counter()\n    for x in nums:\n        for y in nums:\n            pair_counts[x & y] += 1\n    ans = 0\n    for z in nums:\n        for xy, count in pair_counts.items():\n            if (xy & z) == 0:\n                ans += count\n    return ans\n",
        test_cases=[
            {"input": [[2, 1, 3]], "expected": 12},
            {"input": [[0, 0, 0]], "expected": 27}
        ],
        hints=["Precompute the frequencies of all pair-wise bitwise ANDs nums[i] & nums[j], then check each number nums[k] against distinct pair values."],
        leetcode_id=982
    ))

    # 88. Beautiful Subsets (LC 2597)
    problems.append(make_problem(
        pid="bit-h-beautiful-subsets", title="Beautiful Subsets",
        wing_id="bit-manipulation", floor=588, difficulty="hard", visualizer_type="array",
        monster_name="Concordance Sylph", monster_title="Purifier of Forbidden Differences",
        monster_sprite="fairy", monster_color="#ec4899", monster_attack="Harmony Pulse",
        monster_quote="No two items in a beautiful subset may differ by exactly k!",
        description="You are given an array `nums` of positive integers and a positive integer `k`. A subset of `nums` is beautiful if it does not contain two integers with an absolute difference of `k`. Return the number of non-empty beautiful subsets of the array `nums`.",
        examples=[
            {"input": "nums = [2,4,6], k = 2", "output": "4"},
            {"input": "nums = [1], k = 1", "output": "1"}
        ],
        constraints=["1 <= nums.length <= 20", "1 <= nums[i], k <= 1000"],
        function_name="beautifulSubsets",
        starter_code="def beautifulSubsets(nums: list[int], k: int) -> int:\n    pass\n",
        solution_code="def beautifulSubsets(nums: list[int], k: int) -> int:\n    nums.sort()\n    n = len(nums)\n    ans = 0\n    def backtrack(idx, current_set):\n        nonlocal ans\n        if idx == n:\n            if current_set:\n                ans += 1\n            return\n        backtrack(idx + 1, current_set)\n        if nums[idx] - k not in current_set:\n            current_set.add(nums[idx])\n            backtrack(idx + 1, current_set)\n            current_set.remove(nums[idx])\n    backtrack(0, set())\n    return ans\n",
        test_cases=[
            {"input": [[2, 4, 6], 2], "expected": 4},
            {"input": [[1], 1], "expected": 1}
        ],
        hints=["Since n <= 20, sort nums and backtrack: exclude or include nums[idx] only if nums[idx] - k is not already in the active subset."],
        leetcode_id=2597
    ))

    # 89. Can I Win (LC 464)
    problems.append(make_problem(
        pid="bit-h-can-i-win", title="Can I Win (Forced Minimax)",
        wing_id="bit-manipulation", floor=589, difficulty="hard", visualizer_type="array",
        monster_name="Minimax Archon", monster_title="Strategist of Game Trees",
        monster_sprite="boss", monster_color="#f59e0b", monster_attack="Deterministic Checkmate",
        monster_quote="Choose from 1 to maxChoosable without replacement; can you force the total?",
        description="In the '100 game', two players take turns adding to a running total any integer from `1` to `maxChoosableInteger`. Each integer can only be used once. The player who first causes the running total to reach or exceed `desiredTotal` wins. Given `maxChoosableInteger` and `desiredTotal`, return `True` if the first player to move can force a win, otherwise `False`.",
        examples=[
            {"input": "maxChoosableInteger = 10, desiredTotal = 11", "output": "False"},
            {"input": "maxChoosableInteger = 10, desiredTotal = 0", "output": "True"},
            {"input": "maxChoosableInteger = 10, desiredTotal = 1", "output": "True"}
        ],
        constraints=["1 <= maxChoosableInteger <= 20", "0 <= desiredTotal <= 300"],
        function_name="canIWin",
        starter_code="def canIWin(maxChoosableInteger: int, desiredTotal: int) -> bool:\n    pass\n",
        solution_code="def canIWin(maxChoosableInteger: int, desiredTotal: int) -> bool:\n    if desiredTotal <= 0: return True\n    total_sum = (maxChoosableInteger * (maxChoosableInteger + 1)) // 2\n    if total_sum < desiredTotal: return False\n    if total_sum == desiredTotal: return maxChoosableInteger % 2 == 1\n    memo = {}\n    def dp(mask, remaining):\n        if mask in memo: return memo[mask]\n        for i in range(1, maxChoosableInteger + 1):\n            bit = 1 << i\n            if not (mask & bit):\n                if i >= remaining or not dp(mask | bit, remaining - i):\n                    memo[mask] = True\n                    return True\n        memo[mask] = False\n        return False\n    return dp(0, desiredTotal)\n",
        test_cases=[
            {"input": [10, 11], "expected": False},
            {"input": [10, 0], "expected": True},
            {"input": [10, 1], "expected": True}
        ],
        hints=["Use a bitmask to record which numbers have already been chosen. Memoize dp(mask, remaining)."],
        leetcode_id=464
    ))

    # 90. Maximum Good People Based on Statements (LC 2151)
    problems.append(make_problem(
        pid="bit-h-max-good-people", title="Maximum Good People Based on Statements",
        wing_id="bit-manipulation", floor=590, difficulty="hard", visualizer_type="grid",
        monster_name="Veracity Arbiter", monster_title="Judge of Truth and Fabrication",
        monster_sprite="golem", monster_color="#10b981", monster_attack="Truth Matrix Ray",
        monster_quote="Good people never lie; bad people say whatever they desire!",
        description="There are `n` people. `statements[i][j]` is person `i`'s statement about person `j`: `0` means bad, `1` means good, and `2` means no statement. Good people always tell the truth; bad people may tell truth or lie. Return the maximum number of people that can be good in any valid scenario.",
        examples=[
            {"input": "statements = [[2,1,2],[1,2,2],[2,0,2]]", "output": "2"},
            {"input": "statements = [[2,0],[0,2]]", "output": "1"}
        ],
        constraints=["n == statements.length == statements[i].length <= 15"],
        function_name="maximumGood",
        starter_code="def maximumGood(statements: list[list[int]]) -> list[int]:\n    pass\n",
        solution_code="def maximumGood(statements: list[list[int]]) -> int:\n    n = len(statements)\n    ans = 0\n    for mask in range(1 << n):\n        valid = True\n        for i in range(n):\n            if mask & (1 << i):\n                for j in range(n):\n                    st = statements[i][j]\n                    if st == 0 and (mask & (1 << j)):\n                        valid = False\n                        break\n                    if st == 1 and not (mask & (1 << j)):\n                        valid = False\n                        break\n                if not valid: break\n        if valid:\n            ans = max(ans, bin(mask).count('1'))\n    return ans\n",
        test_cases=[
            {"input": [[[2,1,2],[1,2,2],[2,0,2]]], "expected": 2},
            {"input": [[[2,0],[0,2]]], "expected": 1}
        ],
        hints=["Since n <= 15, enumerate all 2^n configurations. For each configuration, verify that statements made by good people are 100% consistent with the mask."],
        leetcode_id=2151
    ))

    # 91. Count Pairs of Nodes with XOR in Range (LC 1803)
    problems.append(make_problem(
        pid="bit-h-count-pairs-xor-range", title="Count Pairs with XOR in Range",
        wing_id="bit-manipulation", floor=591, difficulty="hard", visualizer_type="array",
        monster_name="Trie Radix Sphinx", monster_title="Counter of Bounded Inversions",
        monster_sprite="wizard", monster_color="#3b82f6", monster_attack="0-1 Trie Sweep",
        monster_quote="Count all pairs whose bitwise XOR lies strictly within the holy interval!",
        description="Given an integer array `nums` and two integers `low` and `high`, return the number of nice pairs. A nice pair is a pair `(i, j)` where `0 <= i < j < nums.length` and `low <= (nums[i] ^ nums[j]) <= high`.",
        examples=[
            {"input": "nums = [1,4,2,7], low = 2, high = 6", "output": "6"},
            {"input": "nums = [9,8,4,2,1], low = 5, high = 14", "output": "8"}
        ],
        constraints=["1 <= nums.length <= 2 * 10^4", "1 <= nums[i] <= 2 * 10^4", "1 <= low <= high <= 2 * 10^4"],
        function_name="countPairs",
        starter_code="def countPairs(nums: list[int], low: int, high: int) -> int:\n    pass\n",
        solution_code="def countPairs(nums: list[int], low: int, high: int) -> int:\n    class TrieNode:\n        def __init__(self):\n            self.children = [None, None]\n            self.count = 0\n    def insert(root, val):\n        node = root\n        for b in range(16, -1, -1):\n            bit = (val >> b) & 1\n            if not node.children[bit]:\n                node.children[bit] = TrieNode()\n            node = node.children[bit]\n            node.count += 1\n    def count_less_than(root, val, k):\n        node = root\n        res = 0\n        for b in range(16, -1, -1):\n            if not node: break\n            v_bit = (val >> b) & 1\n            k_bit = (k >> b) & 1\n            if k_bit == 1:\n                if node.children[v_bit]:\n                    res += node.children[v_bit].count\n                node = node.children[1 - v_bit]\n            else:\n                node = node.children[v_bit]\n        return res\n    def count_k(k):\n        root = TrieNode()\n        total = 0\n        for x in nums:\n            total += count_less_than(root, x, k)\n            insert(root, x)\n        return total\n    return count_k(high + 1) - count_k(low)\n",
        test_cases=[
            {"input": [[1, 4, 2, 7], 2, 6], "expected": 6},
            {"input": [[9, 8, 4, 2, 1], 5, 14], "expected": 8}
        ],
        hints=["Use a 0-1 Trie with subtree counts. The number of pairs with XOR in [low, high] is countLessThan(high + 1) - countLessThan(low)."],
        leetcode_id=1803
    ))

    # 92. Partition Array Into Two Arrays to Minimize Sum Difference (LC 2035)
    problems.append(make_problem(
        pid="bit-h-partition-min-sum-diff", title="Partition Array to Minimize Sum Difference",
        wing_id="bit-manipulation", floor=592, difficulty="hard", visualizer_type="array",
        monster_name="Equipartition Leviathan", monster_title="Twin Sunderer of Arrays",
        monster_sprite="dragon", monster_color="#ca8a04", monster_attack="Bipartite Balance Cleave",
        monster_quote="Partition 2*n items into two arrays of n elements each, minimizing difference!",
        description="You are given an integer array `nums` of `2 * n` integers. You need to partition `nums` into two arrays of length `n` to minimize the absolute difference of their sums. Return the minimum possible absolute difference.",
        examples=[
            {"input": "nums = [3,9,7,3], n = 2", "output": "2"},
            {"input": "nums = [-36,36], n = 1", "output": "72"},
            {"input": "nums = [2,-1,0,4,-2,-9], n = 3", "output": "0"}
        ],
        constraints=["1 <= n <= 15", "nums.length == 2 * n"],
        function_name="minimumDifference",
        starter_code="def minimumDifference(nums: list[int], n: int) -> int:\n    pass\n",
        solution_code="def minimumDifference(nums: list[int], n: int) -> int:\n    from bisect import bisect_left\n    total = sum(nums)\n    left, right = nums[:n], nums[n:]\n    left_sums = [[] for _ in range(n + 1)]\n    right_sums = [[] for _ in range(n + 1)]\n    for mask in range(1 << n):\n        sz = bin(mask).count('1')\n        l_s = sum(left[i] for i in range(n) if (mask & (1 << i)))\n        r_s = sum(right[i] for i in range(n) if (mask & (1 << i)))\n        left_sums[sz].append(l_s)\n        right_sums[sz].append(r_s)\n    for sz in range(n + 1):\n        right_sums[sz].sort()\n    ans = float('inf')\n    for sz in range(n + 1):\n        r_sz = n - sz\n        r_list = right_sums[r_sz]\n        for l_s in left_sums[sz]:\n            target = total / 2 - l_s\n            idx = bisect_left(r_list, target)\n            if idx < len(r_list):\n                s = l_s + r_list[idx]\n                ans = min(ans, abs(total - 2 * s))\n            if idx > 0:\n                s = l_s + r_list[idx - 1]\n                ans = min(ans, abs(total - 2 * s))\n    return ans\n",
        test_cases=[
            {"input": [[3,9,7,3], 2], "expected": 2},
            {"input": [[-36,36], 1], "expected": 72},
            {"input": [[2,-1,0,4,-2,-9], 3], "expected": 0}
        ],
        hints=["Meet-in-the-middle: group subset sums of left and right halves by their size k. For each k, binary search for the best complement in right_sums[n - k]."],
        leetcode_id=2035
    ))

    # 93. Maximum Product of the Length of Two Palindromic Subsequences (LC 2002)
    problems.append(make_problem(
        pid="bit-h-max-product-palindromic-subseq", title="Product of Disjoint Palindromic Subsequences",
        wing_id="bit-manipulation", floor=593, difficulty="hard", visualizer_type="array",
        monster_name="Mirror Pair Hydra", monster_title="Twin Stalker of Disjoint Palindromes",
        monster_sprite="snake", monster_color="#06b6d4", monster_attack="Reflective Resonance",
        monster_quote="Two disjoint submasks, both reading identically forwards and backwards!",
        description="Given a string `s`, find two disjoint palindromic subsequences of `s` such that the product of their lengths is maximized. Return the maximum possible product.",
        examples=[
            {"input": "s = \"leetcodecom\"", "output": "9"},
            {"input": "s = \"bb\"", "output": "1"},
            {"input": "s = \"accbcaxxcxx\"", "output": "25"}
        ],
        constraints=["2 <= s.length <= 12"],
        function_name="maxProduct",
        starter_code="def maxProduct(s: str) -> int:\n    pass\n",
        solution_code="def maxProduct(s: str) -> int:\n    n = len(s)\n    palindromes = {}\n    for mask in range(1, 1 << n):\n        subseq = [s[i] for i in range(n) if (mask & (1 << i))]\n        if subseq == subseq[::-1]:\n            palindromes[mask] = len(subseq)\n    ans = 0\n    p_items = list(palindromes.items())\n    for i in range(len(p_items)):\n        m1, l1 = p_items[i]\n        for j in range(i + 1, len(p_items)):\n            m2, l2 = p_items[j]\n            if (m1 & m2) == 0:\n                prod = l1 * l2\n                if prod > ans:\n                    ans = prod\n    return ans\n",
        test_cases=[
            {"input": ["leetcodecom"], "expected": 9},
            {"input": ["bb"], "expected": 1},
            {"input": ["accbcaxxcxx"], "expected": 25}
        ],
        hints=["Since n <= 12, identify all bitmasks that form palindromes, then find pair of non-overlapping masks (mask1 & mask2 == 0) with max product of lengths."],
        leetcode_id=2002
    ))

    # 94. Minimum Number of Work Sessions to Finish the Tasks (LC 1986)
    problems.append(make_problem(
        pid="bit-h-min-work-sessions", title="Minimum Work Sessions for Tasks",
        wing_id="bit-manipulation", floor=594, difficulty="hard", visualizer_type="array",
        monster_name="Session Time Overlord", monster_title="Scheduler of Compact Intervals",
        monster_sprite="golem", monster_color="#475569", monster_attack="Time Box Compression",
        monster_quote="Pack tasks into sessions of length sessionTime; minimize the session count!",
        description="There are `n` tasks assigned to you. The task times are represented as an integer array `tasks` of length `n`, where the `i-th` task takes `tasks[i]` hours. You are also given an integer `sessionTime`. You can work on multiple tasks in a session as long as the total time does not exceed `sessionTime`. Return the minimum number of work sessions needed to finish all tasks.",
        examples=[
            {"input": "tasks = [1,2,3], sessionTime = 3", "output": "2"},
            {"input": "tasks = [3,1,3,1,1], sessionTime = 8", "output": "2"},
            {"input": "tasks = [1,2,3,4,5], sessionTime = 15", "output": "1"}
        ],
        constraints=["n == tasks.length <= 14", "1 <= tasks[i] <= 10", "max(tasks[i]) <= sessionTime <= 15"],
        function_name="minSessions",
        starter_code="def minSessions(tasks: list[int], sessionTime: int) -> int:\n    pass\n",
        solution_code="def minSessions(tasks: list[int], sessionTime: int) -> int:\n    n = len(tasks)\n    dp = [(float('inf'), float('inf'))] * (1 << n)\n    dp[0] = (1, 0)\n    for mask in range(1 << n):\n        sessions, rem = dp[mask]\n        if sessions == float('inf'): continue\n        for i in range(n):\n            if not (mask & (1 << i)):\n                nxt = mask | (1 << i)\n                if rem + tasks[i] <= sessionTime:\n                    cand = (sessions, rem + tasks[i])\n                else:\n                    cand = (sessions + 1, tasks[i])\n                if cand < dp[nxt]:\n                    dp[nxt] = cand\n    return dp[(1 << n) - 1][0]\n",
        test_cases=[
            {"input": [[1,2,3], 3], "expected": 2},
            {"input": [[3,1,3,1,1], 8], "expected": 2},
            {"input": [[1,2,3,4,5], 15], "expected": 1}
        ],
        hints=["DP state dp[mask] = (sessions_count, last_session_duration). Choose transitions that minimize (sessions_count, last_session_duration) lexicographically."],
        leetcode_id=1986
    ))

    # 95. Matchsticks to Square (LC 473)
    problems.append(make_problem(
        pid="bit-h-matchsticks-to-square", title="Matchsticks to Square",
        wing_id="bit-manipulation", floor=595, difficulty="hard", visualizer_type="array",
        monster_name="Quadrilateral Pyromancer", monster_title="Architect of Four Identical Edges",
        monster_sprite="boss", monster_color="#ef4444", monster_attack="Square Flame Wall",
        monster_quote="Every stick must be consumed to forge four sides of exact equal measure!",
        description="You are given an integer array `matchsticks` where `matchsticks[i]` is the length of the `i-th` matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly once. Return `True` if you can make this square and `False` otherwise.",
        examples=[
            {"input": "matchsticks = [1,1,2,2,2]", "output": "True"},
            {"input": "matchsticks = [3,3,3,3,4]", "output": "False"}
        ],
        constraints=["1 <= matchsticks.length <= 15", "1 <= matchsticks[i] <= 10^8"],
        function_name="makesquare",
        starter_code="def makesquare(matchsticks: list[int]) -> bool:\n    pass\n",
        solution_code="def makesquare(matchsticks: list[int]) -> bool:\n    total = sum(matchsticks)\n    if total % 4 != 0: return False\n    side = total // 4\n    matchsticks.sort(reverse=True)\n    if matchsticks[0] > side: return False\n    sides = [0] * 4\n    def backtrack(idx):\n        if idx == len(matchsticks):\n            return True\n        for i in range(4):\n            if sides[i] + matchsticks[idx] <= side:\n                sides[i] += matchsticks[idx]\n                if backtrack(idx + 1): return True\n                sides[i] -= matchsticks[idx]\n            if sides[i] == 0: break\n        return False\n    return backtrack(0)\n",
        test_cases=[
            {"input": [[1, 1, 2, 2, 2]], "expected": True},
            {"input": [[3, 3, 3, 3, 4]], "expected": False}
        ],
        hints=["Total sum must be divisible by 4. Sort matchsticks descending and use backtracking with early pruning on empty sides."],
        leetcode_id=473
    ))

    # 96. Fair Distribution of Cookies (LC 2305)
    problems.append(make_problem(
        pid="bit-h-fair-cookie-distribution", title="Fair Distribution of Cookies",
        wing_id="bit-manipulation", floor=596, difficulty="hard", visualizer_type="array",
        monster_name="Confectioner Goblin", monster_title="Distributor of Sugary Spoils",
        monster_sprite="goblin", monster_color="#ca8a04", monster_attack="Cookie Avalanche",
        monster_quote="Divide all cookie bags among k children to minimize the maximum burden!",
        description="You are given an integer array `cookies`, where `cookies[i]` denotes the number of cookies in the `i-th` bag. You are also given an integer `k` that denotes the number of children. All cookies must be distributed. The unfairness of a distribution is the maximum total cookies obtained by any child. Return the minimum unfairness of all distributions.",
        examples=[
            {"input": "cookies = [8,15,10,20,8], k = 2", "output": "31"},
            {"input": "cookies = [6,1,3,2,2,4,1,2], k = 3", "output": "7"}
        ],
        constraints=["2 <= cookies.length <= 8", "2 <= k <= cookies.length"],
        function_name="distributeCookies",
        starter_code="def distributeCookies(cookies: list[int], k: int) -> int:\n    pass\n",
        solution_code="def distributeCookies(cookies: list[int], k: int) -> int:\n    n = len(cookies)\n    submask_sum = [0] * (1 << n)\n    for mask in range(1 << n):\n        for i in range(n):\n            if mask & (1 << i):\n                submask_sum[mask] += cookies[i]\n    dp = submask_sum[:]\n    for child in range(2, k + 1):\n        nxt_dp = [float('inf')] * (1 << n)\n        for mask in range(1 << n):\n            submask = mask\n            while submask > 0:\n                val = max(dp[mask ^ submask], submask_sum[submask])\n                if val < nxt_dp[mask]: nxt_dp[mask] = val\n                submask = (submask - 1) & mask\n        dp = nxt_dp\n    return dp[(1 << n) - 1]\n",
        test_cases=[
            {"input": [[8,15,10,20,8], 2], "expected": 31},
            {"input": [[6,1,3,2,2,4,1,2], 3], "expected": 7}
        ],
        hints=["Submask enumeration DP: dp[child][mask] = min over submask of max(dp[child-1][mask ^ submask], sum(submask))."],
        leetcode_id=2305
    ))

    # 97. K-th Smallest XOR Coordinate Value (LC 1738)
    problems.append(make_problem(
        pid="bit-h-kth-xor-coordinate", title="K-th Largest XOR Coordinate Value",
        wing_id="bit-manipulation", floor=597, difficulty="hard", visualizer_type="grid",
        monster_name="Grid XOR Sovereign", monster_title="Master of 2D Bitwise Prefixes",
        monster_sprite="golem", monster_color="#8b5cf6", monster_attack="2D Bitwise Crossfire",
        monster_quote="Compute the 2D prefix XOR of all rectangular subgrids, find the k-th rank!",
        description="You are given a 2D integer matrix `matrix` of size `m x n` and an integer `k`. The value of coordinate `(a, b)` of the matrix is the XOR of all `matrix[i][j]` where `0 <= i <= a < m` and `0 <= j <= b < n` (0-indexed). Find the `k-th` largest value (1-indexed) of all the coordinates of `matrix`.",
        examples=[
            {"input": "matrix = [[5,2],[1,6]], k = 1", "output": "7"},
            {"input": "matrix = [[5,2],[1,6]], k = 2", "output": "5"},
            {"input": "matrix = [[5,2],[1,6]], k = 3", "output": "4"},
            {"input": "matrix = [[5,2],[1,6]], k = 4", "output": "0"}
        ],
        constraints=["m == matrix.length", "n == matrix[i].length", "1 <= m, n <= 1000", "1 <= k <= m * n"],
        function_name="kthLargestValue",
        starter_code="def kthLargestValue(matrix: list[list[int]], k: int) -> int:\n    pass\n",
        solution_code="def kthLargestValue(matrix: list[list[int]], k: int) -> int:\n    m, n = len(matrix), len(matrix[0])\n    xor_grid = [[0] * (n + 1) for _ in range(m + 1)]\n    values = []\n    for i in range(1, m + 1):\n        for j in range(1, n + 1):\n            val = matrix[i-1][j-1] ^ xor_grid[i-1][j] ^ xor_grid[i][j-1] ^ xor_grid[i-1][j-1]\n            xor_grid[i][j] = val\n            values.append(val)\n    values.sort(reverse=True)\n    return values[k - 1]\n",
        test_cases=[
            {"input": [[[5, 2], [1, 6]], 1], "expected": 7},
            {"input": [[[5, 2], [1, 6]], 2], "expected": 5},
            {"input": [[[5, 2], [1, 6]], 3], "expected": 4},
            {"input": [[[5, 2], [1, 6]], 4], "expected": 0}
        ],
        hints=["Use 2D prefix XOR: xor[i][j] = matrix[i-1][j-1] ^ xor[i-1][j] ^ xor[i][j-1] ^ xor[i-1][j-1]. Collect all coordinates and sort or quickselect."],
        leetcode_id=1738
    ))

    # 98. Maximum Subset XOR / Linear Basis
    problems.append(make_problem(
        pid="bit-h-max-subset-xor", title="Maximum Subset XOR (Linear Basis)",
        wing_id="bit-manipulation", floor=598, difficulty="hard", visualizer_type="array",
        monster_name="Basis Matrix Golem", monster_title="Keeper of the GF(2) Vector Space",
        monster_sprite="golem", monster_color="#06b6d4", monster_attack="Linear Elimination Pulse",
        monster_quote="Gaussian elimination over GF(2) extracts the absolute maximum XOR sum!",
        description="Given an array of integers `nums`, find the maximum possible bitwise XOR value of any subset of `nums`.",
        examples=[
            {"input": "nums = [2, 4, 5]", "output": "7"},
            {"input": "nums = [1, 2, 3]", "output": "3"},
            {"input": "nums = [9, 8, 5]", "output": "13"}
        ],
        constraints=["1 <= nums.length <= 10^5", "0 <= nums[i] <= 10^9"],
        function_name="maxSubsetXOR",
        starter_code="def maxSubsetXOR(nums: list[int]) -> int:\n    pass\n",
        solution_code="def maxSubsetXOR(nums: list[int]) -> int:\n    basis = [0] * 32\n    for x in nums:\n        for b in range(31, -1, -1):\n            if (x >> b) & 1:\n                if not basis[b]:\n                    basis[b] = x\n                    break\n                x ^= basis[b]\n    max_xor = 0\n    for b in range(31, -1, -1):\n        if (max_xor ^ basis[b]) > max_xor:\n            max_xor ^= basis[b]\n    return max_xor\n",
        test_cases=[
            {"input": [[2, 4, 5]], "expected": 7},
            {"input": [[1, 2, 3]], "expected": 3},
            {"input": [[9, 8, 5]], "expected": 13}
        ],
        hints=["Insert every element into a Linear Basis over GF(2). Greedily XOR each basis vector into the answer if it increases the result."],
        leetcode_id=0
    ))

    # 99. Total XOR Sum of All Pairs
    problems.append(make_problem(
        pid="bit-h-total-xor-sum-pairs", title="Total XOR Sum of All Pairs",
        wing_id="bit-manipulation", floor=599, difficulty="hard", visualizer_type="array",
        monster_name="Pairwise Parity Titan", monster_title="Accumulator of Bit Differences",
        monster_sprite="dragon", monster_color="#ef4444", monster_attack="Pairwise Bit Flare",
        monster_quote="Every bit position counts: ones multiplied by zeros yields the sum!",
        description="Given an integer array `nums`, compute the sum of `(nums[i] ^ nums[j])` over all pairs `0 <= i < j < len(nums)`. Return the total sum.",
        examples=[
            {"input": "nums = [1, 3, 5]", "output": "12"},
            {"input": "nums = [5, 9]", "output": "12"},
            {"input": "nums = [4, 14, 2]", "output": "28"}
        ],
        constraints=["1 <= nums.length <= 10^5", "0 <= nums[i] <= 10^9"],
        function_name="totalXORSum",
        starter_code="def totalXORSum(nums: list[int]) -> int:\n    pass\n",
        solution_code="def totalXORSum(nums: list[int]) -> int:\n    n = len(nums)\n    total = 0\n    for b in range(32):\n        ones = 0\n        for x in nums:\n            if (x >> b) & 1:\n                ones += 1\n        zeros = n - ones\n        total += ones * zeros * (1 << b)\n    return total\n",
        test_cases=[
            {"input": [[1, 3, 5]], "expected": 12},
            {"input": [[5, 9]], "expected": 12},
            {"input": [[4, 14, 2]], "expected": 28}
        ],
        hints=["Consider each bit independently. For bit b, if there are ones numbers with bit b set and zeros numbers without it, the bit contributes ones * zeros * (1 << b)."],
        leetcode_id=0
    ))

    # 100. Floor 600 Wing Boss: Universal Linear Basis Rank and Max XOR
    problems.append(make_problem(
        pid="bit-h-linear-basis-rank-max", title="Universal Linear Basis Sovereign",
        wing_id="bit-manipulation", floor=600, difficulty="hard", visualizer_type="array",
        monster_name="XOR Monarch of the 600th Abyss", monster_title="Omniscient Master of Bitwise Vector Spaces",
        monster_sprite="boss", monster_color="#7c3aed", monster_attack="Universal GF(2) Annihilation",
        monster_quote="I am the Sovereign of GF(2)! Behold the rank of your basis and the zenith of bitwise XOR!",
        description="Given an array of integers `nums`, construct the canonical Linear Basis over GF(2). Return a list `[rank, maxXor]` where `rank` is the number of linearly independent elements in the basis (the dimension of the vector space spanned by `nums`), and `maxXor` is the maximum XOR value obtainable from any subset of `nums`.",
        examples=[
            {"input": "nums = [2, 4, 5]", "output": "[3, 7]"},
            {"input": "nums = [1, 2, 3]", "output": "[2, 3]"},
            {"input": "nums = [10, 15, 20, 25]", "output": "[4, 30]"}
        ],
        constraints=["1 <= nums.length <= 10^5", "0 <= nums[i] <= 10^9"],
        function_name="linearBasisRankAndMax",
        starter_code="def linearBasisRankAndMax(nums: list[int]) -> list[int]:\n    pass\n",
        solution_code="def linearBasisRankAndMax(nums: list[int]) -> list[int]:\n    basis = [0] * 32\n    rank = 0\n    for x in nums:\n        for b in range(31, -1, -1):\n            if (x >> b) & 1:\n                if not basis[b]:\n                    basis[b] = x\n                    rank += 1\n                    break\n                x ^= basis[b]\n    max_xor = 0\n    for b in range(31, -1, -1):\n        if (max_xor ^ basis[b]) > max_xor:\n            max_xor ^= basis[b]\n    return [rank, max_xor]\n",
        test_cases=[
            {"input": [[2, 4, 5]], "expected": [3, 7]},
            {"input": [[1, 2, 3]], "expected": [2, 3]},
            {"input": [[10, 15, 20, 25]], "expected": [4, 30]}
        ],
        hints=["Insert elements into linear basis. Count number of successful insertions for rank. Greedily maximize XOR for maxXor."],
        leetcode_id=0
    ))

    return problems
