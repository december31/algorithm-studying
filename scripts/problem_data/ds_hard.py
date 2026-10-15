"""
Data Structures Hard Problems (30 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_data_structures_hard():
    problems = []

    # 1. Trapping Rain Water
    problems.append(make_problem(
        pid="ds-h-trap-rain-water", title="Trapping Rain Water",
        wing_id="data-structures", floor=171, difficulty="hard", visualizer_type="array",
        monster_name="Aquatic Colossus", monster_title="Lord of Valley Reservoirs",
        monster_sprite="golem", monster_color="#06b6d4", monster_attack="Tsunami Crash",
        monster_quote="Two pointers bounded the maximum trapped moisture!",
        description="Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.",
        examples=[{"input": "height = [0,1,0,2,1,0,1,3,2,1,2,1]", "output": "6"}, {"input": "height = [4,2,0,3,2,5]", "output": "9"}],
        constraints=["n == len(height)", "1 <= n <= 2 * 10^4", "0 <= height[i] <= 10^5"],
        function_name="trapRainWater",
        starter_code="def trapRainWater(height: list[int]) -> int:\n    pass\n",
        solution_code="def trapRainWater(height: list[int]) -> int:\n    if not height: return 0\n    left, right = 0, len(height) - 1\n    left_max, right_max = height[left], height[right]\n    water = 0\n    while left < right:\n        if left_max < right_max:\n            left += 1\n            left_max = max(left_max, height[left])\n            water += left_max - height[left]\n        else:\n            right -= 1\n            right_max = max(right_max, height[right])\n            water += right_max - height[right]\n    return water\n",
        test_cases=[{"input": [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]], "expected": 6}, {"input": [[4, 2, 0, 3, 2, 5]], "expected": 9}, {"input": [[1, 2, 3]], "expected": 0}, {"input": [[3, 0, 3]], "expected": 3}],
        hints=["Two pointers with left_max and right_max gives O(n) time and O(1) space."],
        leetcode_id=42
    ))

    # 2. Largest Rectangle in Histogram
    problems.append(make_problem(
        pid="ds-h-largest-rectangle-histogram", title="Largest Rectangle in Histogram",
        wing_id="data-structures", floor=172, difficulty="hard", visualizer_type="stack",
        monster_name="Pillar Demon", monster_title="Crusher of Spanning Heights",
        monster_sprite="demon", monster_color="#ef4444", monster_attack="Pillar Crush",
        monster_quote="The monotonic stack discovered the maximum spanning rectangle!",
        description="Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return the area of the largest rectangle in the histogram.",
        examples=[{"input": "heights = [2,1,5,6,2,3]", "output": "10"}, {"input": "heights = [2,4]", "output": "4"}],
        constraints=["1 <= len(heights) <= 10^5", "0 <= heights[i] <= 10^4"],
        function_name="largestRectangleArea",
        starter_code="def largestRectangleArea(heights: list[int]) -> int:\n    pass\n",
        solution_code="def largestRectangleArea(heights: list[int]) -> int:\n    stack = []\n    max_area = 0\n    h = heights + [0]\n    for i, val in enumerate(h):\n        while stack and h[stack[-1]] > val:\n            height = h[stack.pop()]\n            width = i if not stack else i - stack[-1] - 1\n            max_area = max(max_area, height * width)\n        stack.append(i)\n    return max_area\n",
        test_cases=[{"input": [[2, 1, 5, 6, 2, 3]], "expected": 10}, {"input": [[2, 4]], "expected": 4}, {"input": [[1]], "expected": 1}, {"input": [[2, 1, 2]], "expected": 3}],
        hints=["Monotonic increasing stack; pop when encountering smaller bar and compute width = i - stack[-1] - 1."],
        leetcode_id=84
    ))

    # 3. Maximal Rectangle in 2D Binary Matrix
    problems.append(make_problem(
        pid="ds-h-maximal-rectangle", title="Maximal Rectangle in 2D Matrix",
        wing_id="data-structures", floor=173, difficulty="hard", visualizer_type="stack",
        monster_name="Tessellation Sphinx", monster_title="Examiner of Continuous Ones",
        monster_sprite="beholder", monster_color="#a855f7", monster_attack="Area Gaze",
        monster_quote="Histogram DP on each row yielded the largest solid rectangle!",
        description="Given a `rows x cols` binary `matrix` filled with `0`'s and `1`'s, find the largest rectangle containing only `1`'s and return its area.",
        examples=[{"input": "matrix = [[\"1\",\"0\",\"1\",\"0\",\"0\"],[\"1\",\"0\",\"1\",\"1\",\"1\"],[\"1\",\"1\",\"1\",\"1\",\"1\"],[\"1\",\"0\",\"0\",\"1\",\"0\"]]", "output": "6"}],
        constraints=["1 <= len(matrix), len(matrix[0]) <= 200"],
        function_name="maximalRectangle",
        starter_code="def maximalRectangle(matrix: list[list[str]]) -> int:\n    pass\n",
        solution_code="def maximalRectangle(matrix: list[list[str]]) -> int:\n    if not matrix or not matrix[0]: return 0\n    cols = len(matrix[0])\n    heights = [0] * cols\n    max_area = 0\n    def get_max_hist(h):\n        st = []\n        area = 0\n        arr = h + [0]\n        for i, v in enumerate(arr):\n            while st and arr[st[-1]] > v:\n                height = arr[st.pop()]\n                w = i if not st else i - st[-1] - 1\n                area = max(area, height * w)\n            st.append(i)\n        return area\n    for row in matrix:\n        for j in range(cols):\n            heights[j] = heights[j] + 1 if row[j] == '1' else 0\n        max_area = max(max_area, get_max_hist(heights))\n    return max_area\n",
        test_cases=[{"input": [[["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]], "expected": 6}, {"input": [[["0"]]], "expected": 0}, {"input": [[["1"]]], "expected": 1}],
        hints=["Accumulate continuous 1s vertically into a histogram per row, then apply Largest Rectangle in Histogram."],
        leetcode_id=85
    ))

    # 4. Sliding Window Maximum
    problems.append(make_problem(
        pid="ds-h-max-sliding-window", title="Sliding Window Maximum",
        wing_id="data-structures", floor=174, difficulty="hard", visualizer_type="array",
        monster_name="Apex Wyrm", monster_title="Culler of Non-Maximal Nodes",
        monster_sprite="dragon", monster_color="#f59e0b", monster_attack="Apex Flare",
        monster_quote="Monotonic deque maintained the rolling maximum in O(n)!",
        description="You are given an array of integers `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Return the max sliding window.",
        examples=[{"input": "nums = [1,3,-1,-3,5,3,6,7], k = 3", "output": "[3,3,5,5,6,7]"}, {"input": "nums = [1], k = 1", "output": "[1]"}],
        constraints=["1 <= len(nums) <= 10^5", "-10^4 <= nums[i] <= 10^4", "1 <= k <= len(nums)"],
        function_name="maxSlidingWindow",
        starter_code="def maxSlidingWindow(nums: list[int], k: int) -> list[int]:\n    pass\n",
        solution_code="def maxSlidingWindow(nums: list[int], k: int) -> list[int]:\n    from collections import deque\n    q = deque()\n    res = []\n    for i, n in enumerate(nums):\n        while q and nums[q[-1]] <= n:\n            q.pop()\n        q.append(i)\n        if q[0] <= i - k:\n            q.popleft()\n        if i >= k - 1:\n            res.append(nums[q[0]])\n    return res\n",
        test_cases=[{"input": [[1, 3, -1, -3, 5, 3, 6, 7], 3], "expected": [3, 3, 5, 5, 6, 7]}, {"input": [[1], 1], "expected": [1]}, {"input": [[1, -1], 1], "expected": [1, -1]}, {"input": [[9, 11], 2], "expected": [11]}],
        hints=["Use a monotonic decreasing deque storing indices. The front always holds the maximum."],
        leetcode_id=239
    ))

    # 5. Minimum Window Substring
    problems.append(make_problem(
        pid="ds-h-min-window-substring", title="Minimum Window Substring",
        wing_id="data-structures", floor=175, difficulty="hard", visualizer_type="array",
        monster_name="Substring Lich", monster_title="Extractor of the Leanest Cover",
        monster_sprite="lich", monster_color="#ec4899", monster_attack="Constrict Hex",
        monster_quote="Character requirement count matched and shrunk to minimal span!",
        description="Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string `\"\"`.",
        examples=[{"input": "s = \"ADOBECODEBANC\", t = \"ABC\"", "output": "\"BANC\""}, {"input": "s = \"a\", t = \"a\"", "output": "\"a\""}, {"input": "s = \"a\", t = \"aa\"", "output": "\"\""}],
        constraints=["m == len(s), n == len(t)", "1 <= m, n <= 10^5"],
        function_name="minWindow",
        starter_code="def minWindow(s: str, t: str) -> str:\n    pass\n",
        solution_code="def minWindow(s: str, t: str) -> str:\n    from collections import Counter\n    target = Counter(t)\n    window = {}\n    have, need = 0, len(target)\n    res, min_len = (-1, -1), float('inf')\n    left = 0\n    for right, ch in enumerate(s):\n        window[ch] = window.get(ch, 0) + 1\n        if ch in target and window[ch] == target[ch]:\n            have += 1\n        while have == need:\n            if (right - left + 1) < min_len:\n                min_len = right - left + 1\n                res = (left, right)\n            window[s[left]] -= 1\n            if s[left] in target and window[s[left]] < target[s[left]]:\n                have -= 1\n            left += 1\n    l, r = res\n    return s[l:r + 1] if min_len != float('inf') else \"\"\n",
        test_cases=[{"input": ["ADOBECODEBANC", "ABC"], "expected": "BANC"}, {"input": ["a", "a"], "expected": "a"}, {"input": ["a", "aa"], "expected": ""}, {"input": ["ab", "b"], "expected": "b"}],
        hints=["Two pointers with have/need counter variables to track full character satisfaction."],
        leetcode_id=76
    ))

    # 6. First Missing Positive
    problems.append(make_problem(
        pid="ds-h-first-missing-positive", title="First Missing Positive (O(n) In-place)",
        wing_id="data-structures", floor=176, difficulty="hard", visualizer_type="array",
        monster_name="Cyclic Inversion Wraith", monster_title="Hider of the Smallest Omitted Positive",
        monster_sprite="wraith", monster_color="#8b5cf6", monster_attack="Omission Curse",
        monster_quote="Cyclic indexing placed every positive integer at index val - 1!",
        description="Given an unsorted integer array `nums`, return the smallest positive integer that is not present in `nums`. You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.",
        examples=[{"input": "nums = [1,2,0]", "output": "3"}, {"input": "nums = [3,4,-1,1]", "output": "2"}, {"input": "nums = [7,8,9,11,12]", "output": "1"}],
        constraints=["1 <= len(nums) <= 10^5", "-2^31 <= nums[i] <= 2^31 - 1"],
        function_name="firstMissingPositive",
        starter_code="def firstMissingPositive(nums: list[int]) -> int:\n    pass\n",
        solution_code="def firstMissingPositive(nums: list[int]) -> int:\n    n = len(nums)\n    for i in range(n):\n        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:\n            target = nums[i] - 1\n            nums[i], nums[target] = nums[target], nums[i]\n    for i in range(n):\n        if nums[i] != i + 1:\n            return i + 1\n    return n + 1\n",
        test_cases=[{"input": [[1, 2, 0]], "expected": 3}, {"input": [[3, 4, -1, 1]], "expected": 2}, {"input": [[7, 8, 9, 11, 12]], "expected": 1}, {"input": [[1]], "expected": 2}],
        hints=["Cyclic sort: put each number x into nums[x - 1] if 1 <= x <= n."],
        leetcode_id=41
    ))

    # 7. Longest Valid Parentheses
    problems.append(make_problem(
        pid="ds-h-longest-valid-parentheses", title="Longest Valid Parentheses",
        wing_id="data-structures", floor=177, difficulty="hard", visualizer_type="stack",
        monster_name="Parenthesis Titan", monster_title="Keeper of Unbroken Nestings",
        monster_sprite="golem", monster_color="#38bdf8", monster_attack="Bracket Slam",
        monster_quote="Stack index tracking calculated the longest unbroken well-formed span!",
        description="Given a string containing just the characters `'('` and `')'`, return the length of the longest valid (well-formed) parentheses substring.",
        examples=[{"input": "s = \"(()\"", "output": "2"}, {"input": "s = \")()())\"", "output": "4"}, {"input": "s = \"\"", "output": "0"}],
        constraints=["0 <= len(s) <= 3 * 10^4", "s[i] is '(' or ')'"],
        function_name="longestValidParentheses",
        starter_code="def longestValidParentheses(s: str) -> int:\n    pass\n",
        solution_code="def longestValidParentheses(s: str) -> int:\n    stack = [-1]\n    max_len = 0\n    for i, ch in enumerate(s):\n        if ch == '(':\n            stack.append(i)\n        else:\n            stack.pop()\n            if not stack:\n                stack.append(i)\n            else:\n                max_len = max(max_len, i - stack[-1])\n    return max_len\n",
        test_cases=[{"input": ["(()"], "expected": 2}, {"input": [")()())"], "expected": 4}, {"input": [""], "expected": 0}, {"input": ["()(()()"], "expected": 4}],
        hints=["Initialize stack with -1 as boundary. Pop on ')'; if stack empty push current index, else compute i - stack[-1]."],
        leetcode_id=32
    ))

    # 8. Basic Calculator (Parentheses and Signs)
    problems.append(make_problem(
        pid="ds-h-calculate-basic", title="Basic Calculator",
        wing_id="data-structures", floor=178, difficulty="hard", visualizer_type="stack",
        monster_name="Math Drake", monster_title="Solver of Nested Signed Expressions",
        monster_sprite="dragon", monster_color="#10b981", monster_attack="Parenthesis Flare",
        monster_quote="Stack saved intermediate signs across nested parentheses!",
        description="Given a string `s` representing a valid expression with `+`, `-`, non-negative integers, and parentheses `(`, `)`, implement a basic calculator to evaluate it.",
        examples=[{"input": "s = \"1 + 1\"", "output": "2"}, {"input": "s = \" 2-1 + 2 \"", "output": "3"}, {"input": "s = \"(1+(4+5+2)-3)+(6+8)\"", "output": "23"}],
        constraints=["1 <= len(s) <= 3 * 10^4"],
        function_name="calculateExpression",
        starter_code="def calculateExpression(s: str) -> int:\n    pass\n",
        solution_code="def calculateExpression(s: str) -> int:\n    stack = []\n    res = 0\n    num = 0\n    sign = 1\n    for ch in s:\n        if ch.isdigit():\n            num = num * 10 + int(ch)\n        elif ch in '+-':\n            res += sign * num\n            num = 0\n            sign = 1 if ch == '+' else -1\n        elif ch == '(':\n            stack.append(res)\n            stack.append(sign)\n            res = 0\n            sign = 1\n        elif ch == ')':\n            res += sign * num\n            num = 0\n            res *= stack.pop()\n            res += stack.pop()\n    res += sign * num\n    return res\n",
        test_cases=[{"input": ["1 + 1"], "expected": 2}, {"input": [" 2-1 + 2 "], "expected": 3}, {"input": ["(1+(4+5+2)-3)+(6+8)"], "expected": 23}, {"input": ["- (3 + (4 + 5))"], "expected": -12}],
        hints=["Maintain running result and current sign. On '(', push result and sign; on ')', pop and combine."],
        leetcode_id=224
    ))

    # 9. Basic Calculator II (Multiplication and Division)
    problems.append(make_problem(
        pid="ds-h-calculate-ii", title="Basic Calculator II",
        wing_id="data-structures", floor=179, difficulty="hard", visualizer_type="stack",
        monster_name="Precedence Hydra", monster_title="Master of Multiplicative Priority",
        monster_sprite="hydra", monster_color="#e11d48", monster_attack="Precedence Strike",
        monster_quote="Multiplication and division were resolved immediately on the stack!",
        description="Given a string `s` which represents an expression, evaluate this expression. Integer division should truncate toward zero. Operators are `+`, `-`, `*`, `/` without parentheses.",
        examples=[{"input": "s = \"3+2*2\"", "output": "7"}, {"input": "s = \" 3/2 \"", "output": "1"}, {"input": "s = \" 3+5 / 2 \"", "output": "5"}],
        constraints=["1 <= len(s) <= 3 * 10^5"],
        function_name="calculateWithMultDiv",
        starter_code="def calculateWithMultDiv(s: str) -> int:\n    pass\n",
        solution_code="def calculateWithMultDiv(s: str) -> int:\n    stack = []\n    num = 0\n    sign = '+'\n    for i, ch in enumerate(s):\n        if ch.isdigit():\n            num = num * 10 + int(ch)\n        if ch in '+-*/' or i == len(s) - 1:\n            if not ch.isdigit() and ch == ' ' and i == len(s) - 1:\n                pass\n            if sign == '+': stack.append(num)\n            elif sign == '-': stack.append(-num)\n            elif sign == '*': stack.append(stack.pop() * num)\n            elif sign == '/': stack.append(int(stack.pop() / num))\n            sign = ch\n            num = 0\n    return sum(stack)\n",
        test_cases=[{"input": ["3+2*2"], "expected": 7}, {"input": [" 3/2 "], "expected": 1}, {"input": [" 3+5 / 2 "], "expected": 5}, {"input": ["14-3/2"], "expected": 13}],
        hints=["Resolve * and / directly on stack top; delay + and - for the final sum."],
        leetcode_id=227
    ))

    # 10. Merge K Sorted Arrays
    problems.append(make_problem(
        pid="ds-h-merge-k-lists", title="Merge K Sorted Lists / Arrays",
        wing_id="data-structures", floor=180, difficulty="hard", visualizer_type="array",
        monster_name="Multi-Stream Hydra", monster_title="Consolidator of K Riverbeds",
        monster_sprite="hydra", monster_color="#06b6d4", monster_attack="River Surge",
        monster_quote="A min-heap merged k streams in O(N log k) time!",
        description="You are given an array of `k` linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted list and return it.",
        examples=[{"input": "lists = [[1,4,5],[1,3,4],[2,6]]", "output": "[1,1,2,3,4,4,5,6]"}, {"input": "lists = []", "output": "[]"}],
        constraints=["k == len(lists)", "0 <= k <= 10^4", "0 <= sum(len(l)) <= 10^5"],
        function_name="mergeKArrays",
        starter_code="def mergeKArrays(lists: list[list[int]]) -> list[int]:\n    pass\n",
        solution_code="def mergeKArrays(lists: list[list[int]]) -> list[int]:\n    import heapq\n    heap = []\n    for i, lst in enumerate(lists):\n        if lst:\n            heapq.heappush(heap, (lst[0], i, 0))\n    res = []\n    while heap:\n        val, list_idx, elem_idx = heapq.heappop(heap)\n        res.append(val)\n        if elem_idx + 1 < len(lists[list_idx]):\n            next_val = lists[list_idx][elem_idx + 1]\n            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))\n    return res\n",
        test_cases=[{"input": [[[1, 4, 5], [1, 3, 4], [2, 6]]], "expected": [1, 1, 2, 3, 4, 4, 5, 6]}, {"input": [[]], "expected": []}, {"input": [[[], [1]]], "expected": [1]}],
        hints=["Use a min-heap storing (val, list_idx, elem_idx). Pull smallest and push its successor."],
        leetcode_id=23
    ))

    # 11. Smallest Range Covering Elements from K Lists
    problems.append(make_problem(
        pid="ds-h-smallest-range-k-lists", title="Smallest Range from K Lists",
        wing_id="data-structures", floor=181, difficulty="hard", visualizer_type="array",
        monster_name="Span Strangler", monster_title="Compressor of Multi-Stream Intervals",
        monster_sprite="wraith", monster_color="#ec4899", monster_attack="Tight Span",
        monster_quote="Min-heap sliding window found the minimal spanning interval!",
        description="You have `k` lists of sorted integers in non-decreasing order. Find the smallest range `[a, b]` that includes at least one number from each of the `k` lists.",
        examples=[{"input": "nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]", "output": "[20,24]"}, {"input": "nums = [[1,2,3],[1,2,3],[1,2,3]]", "output": "[1,1]"}],
        constraints=["nums.length == k", "1 <= k <= 3500", "1 <= len(nums[i]) <= 50"],
        function_name="smallestRangeKLists",
        starter_code="def smallestRangeKLists(nums: list[list[int]]) -> list[int]:\n    pass\n",
        solution_code="def smallestRangeKLists(nums: list[list[int]]) -> list[int]:\n    import heapq\n    heap = []\n    curr_max = float('-inf')\n    for i, lst in enumerate(nums):\n        heapq.heappush(heap, (lst[0], i, 0))\n        curr_max = max(curr_max, lst[0])\n    best_range = [heap[0][0], curr_max]\n    while True:\n        val, list_idx, elem_idx = heapq.heappop(heap)\n        if curr_max - val < best_range[1] - best_range[0]:\n            best_range = [val, curr_max]\n        if elem_idx + 1 == len(nums[list_idx]):\n            break\n        next_val = nums[list_idx][elem_idx + 1]\n        heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))\n        curr_max = max(curr_max, next_val)\n    return best_range\n",
        test_cases=[{"input": [[[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]], "expected": [20, 24]}, {"input": [[[1, 2, 3], [1, 2, 3], [1, 2, 3]]], "expected": [1, 1]}],
        hints=["Min-heap tracks current minimum among current pointers while a variable tracks current maximum."],
        leetcode_id=632
    ))

    # 12. Substring with Concatenation of All Words
    problems.append(make_problem(
        pid="ds-h-find-substring-words", title="Substring Concatenation of All Words",
        wing_id="data-structures", floor=182, difficulty="hard", visualizer_type="array",
        monster_name="Lexicon Behemoth", monster_title="Devourer of Word Tiles",
        monster_sprite="beholder", monster_color="#8b5cf6", monster_attack="Lexicon Gaze",
        monster_quote="Fixed-word-length chunking mapped all concatenated indices!",
        description="You are given a string `s` and an array of strings `words` of the same length. Return an array of all the starting indices of substring(s) in `s` that is a concatenation of each word in `words` exactly once and without any intervening characters.",
        examples=[{"input": "s = \"barfoothefoobarman\", words = [\"foo\",\"bar\"]", "output": "[0,9]"}, {"input": "s = \"wordgoodgoodgoodbestword\", words = [\"word\",\"good\",\"best\",\"word\"]", "output": "[]"}],
        constraints=["1 <= len(s) <= 10^4", "1 <= len(words) <= 5000", "all words[i] have same length"],
        function_name="findSubstringWords",
        starter_code="def findSubstringWords(s: str, words: list[str]) -> list[int]:\n    pass\n",
        solution_code="def findSubstringWords(s: str, words: list[str]) -> list[int]:\n    if not s or not words: return []\n    from collections import Counter\n    w_len = len(words[0])\n    total_len = len(words) * w_len\n    word_count = Counter(words)\n    res = []\n    for i in range(len(s) - total_len + 1):\n        sub = s[i:i + total_len]\n        chunks = [sub[j:j + w_len] for j in range(0, total_len, w_len)]\n        if Counter(chunks) == word_count:\n            res.append(i)\n    return res\n",
        test_cases=[{"input": ["barfoothefoobarman", ["foo", "bar"]], "expected": [0, 9]}, {"input": ["wordgoodgoodgoodbestword", ["word", "good", "best", "word"]], "expected": []}, {"input": ["barfoofoobarthefoobarman", ["bar", "foo", "the"]], "expected": [6, 9, 12]}],
        hints=["Since all words have the same length L, split every window of size len(words)*L into chunks of size L."],
        leetcode_id=30
    ))

    # 13. Shortest Subarray with Sum at Least K
    problems.append(make_problem(
        pid="ds-h-shortest-subarray-k", title="Shortest Subarray with Sum >= K",
        wing_id="data-structures", floor=183, difficulty="hard", visualizer_type="array",
        monster_name="Sum Constrictor", monster_title="Crusher of Cumulative Thresholds",
        monster_sprite="golem", monster_color="#ef4444", monster_attack="Threshold Slam",
        monster_quote="Monotonic deque on prefix sums handled negative elements in O(n)!",
        description="Given an integer array `nums` and an integer `k`, return the length of the shortest non-empty subarray of `nums` with a sum of at least `k`. If there is no such subarray, return `-1`.",
        examples=[{"input": "nums = [1], k = 1", "output": "1"}, {"input": "nums = [1,2], k = 4", "output": "-1"}, {"input": "nums = [2,-1,2], k = 3", "output": "3"}],
        constraints=["1 <= len(nums) <= 10^5", "-10^5 <= nums[i] <= 10^5", "1 <= k <= 10^9"],
        function_name="shortestSubarraySumK",
        starter_code="def shortestSubarraySumK(nums: list[int], k: int) -> int:\n    pass\n",
        solution_code="def shortestSubarraySumK(nums: list[int], k: int) -> int:\n    from collections import deque\n    P = [0]\n    for x in nums: P.append(P[-1] + x)\n    ans = float('inf')\n    monoq = deque()\n    for y, Py in enumerate(P):\n        while monoq and Py <= P[monoq[-1]]:\n            monoq.pop()\n        while monoq and Py - P[monoq[0]] >= k:\n            ans = min(ans, y - monoq.popleft())\n        monoq.append(y)\n    return ans if ans != float('inf') else -1\n",
        test_cases=[{"input": [[1], 1], "expected": 1}, {"input": [[1, 2], 4], "expected": -1}, {"input": [[2, -1, 2], 3], "expected": 3}, {"input": [[84, -37, 32, 40, 95], 167], "expected": 3}],
        hints=["Compute prefix sums and maintain a monotonic increasing deque of prefix sum indices."],
        leetcode_id=862
    ))

    # 14. Constrained Subsequence Sum
    problems.append(make_problem(
        pid="ds-h-constrained-subset-sum", title="Constrained Subsequence Sum",
        wing_id="data-structures", floor=184, difficulty="hard", visualizer_type="array",
        monster_name="Leaping Chimera", monster_title="Pouncer across Limited Gaps",
        monster_sprite="demon", monster_color="#f59e0b", monster_attack="Leap Claw",
        monster_quote="Monotonic deque DP optimized the k-step sliding maximum!",
        description="Given an integer array `nums` and an integer `k`, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, their indices differ by at most `k`.",
        examples=[{"input": "nums = [10,2,-10,5,20], k = 2", "output": "37"}, {"input": "nums = [-1,-2,-3], k = 1", "output": "-1"}],
        constraints=["1 <= k <= len(nums) <= 10^5", "-10^4 <= nums[i] <= 10^4"],
        function_name="constrainedSubsetSum",
        starter_code="def constrainedSubsetSum(nums: list[int], k: int) -> int:\n    pass\n",
        solution_code="def constrainedSubsetSum(nums: list[int], k: int) -> int:\n    from collections import deque\n    dp = list(nums)\n    q = deque()\n    for i in range(len(nums)):\n        if q and q[0] < i - k:\n            q.popleft()\n        if q:\n            dp[i] = max(dp[i], dp[i] + dp[q[0]])\n        while q and dp[q[-1]] <= dp[i]:\n            q.pop()\n        q.append(i)\n    return max(dp)\n",
        test_cases=[{"input": [[10, 2, -10, 5, 20], 2], "expected": 37}, {"input": [[-1, -2, -3], 1], "expected": -1}, {"input": [[10, -2, -10, -5, 20], 2], "expected": 23}],
        hints=["dp[i] = nums[i] + max(0, max(dp[i-k ... i-1])). Use monotonic deque to get window max in O(1)."],
        leetcode_id=1425
    ))

    # 15. Jump Game VI
    problems.append(make_problem(
        pid="ds-h-jump-game-vi", title="Jump Game VI (Max Score)",
        wing_id="data-structures", floor=185, difficulty="hard", visualizer_type="array",
        monster_name="Vault Drake", monster_title="Glider of K-Step Chasms",
        monster_sprite="dragon", monster_color="#10b981", monster_attack="Vault Strike",
        monster_quote="Reaching the final step with maximal score achieved!",
        description="You are given a 0-indexed integer array `nums` and an integer `k`. You are initially standing at index `0`. In one move, you can jump at most `k` steps forward without going outside the boundaries of the array. Your score is the sum of all `nums[j]` for each index `j` you visited. Return the maximum score you can get.",
        examples=[{"input": "nums = [1,-1,-2,4,-7,3], k = 2", "output": "7"}, {"input": "nums = [10,-5,-2,4,0,3], k = 3", "output": "17"}],
        constraints=["1 <= len(nums), k <= 10^5"],
        function_name="maxResultJumpGame",
        starter_code="def maxResultJumpGame(nums: list[int], k: int) -> int:\n    pass\n",
        solution_code="def maxResultJumpGame(nums: list[int], k: int) -> int:\n    from collections import deque\n    n = len(nums)\n    dp = [0] * n\n    dp[0] = nums[0]\n    q = deque([0])\n    for i in range(1, n):\n        if q and q[0] < i - k:\n            q.popleft()\n        dp[i] = nums[i] + dp[q[0]]\n        while q and dp[q[-1]] <= dp[i]:\n            q.pop()\n        q.append(i)\n    return dp[-1]\n",
        test_cases=[{"input": [[1, -1, -2, 4, -7, 3], 2], "expected": 7}, {"input": [[10, -5, -2, 4, 0, 3], 3], "expected": 17}, {"input": [[1, -5, -20, 4, -1, 3, -6, -3], 2], "expected": 0}],
        hints=["dp[i] = nums[i] + max(dp[i-k ... i-1]). Monotonic deque maintains max in window."],
        leetcode_id=1696
    ))

    # 16. Sliding Window Median
    problems.append(make_problem(
        pid="ds-h-median-sliding-window", title="Sliding Window Median",
        wing_id="data-structures", floor=186, difficulty="hard", visualizer_type="array",
        monster_name="Equilibrium Wyrm", monster_title="Balancer of Rolling Medians",
        monster_sprite="slime", monster_color="#ec4899", monster_attack="Median Pulse",
        monster_quote="Bisect window maintenance produced exact floating-point medians!",
        description="Given an array `nums` and an integer `k`, there is a sliding window of size `k` moving from left to right. Return the median array for each window in the original array.",
        examples=[{"input": "nums = [1,3,-1,-3,5,3,6,7], k = 3", "output": "[1.0,-1.0,-1.0,3.0,5.0,6.0]"}],
        constraints=["1 <= k <= len(nums) <= 10^5"],
        function_name="medianSlidingWindow",
        starter_code="def medianSlidingWindow(nums: list[int], k: int) -> list[float]:\n    pass\n",
        solution_code="def medianSlidingWindow(nums: list[int], k: int) -> list[float]:\n    import bisect\n    window = sorted(nums[:k])\n    res = []\n    for i in range(k, len(nums) + 1):\n        if k % 2 == 1:\n            res.append(float(window[k // 2]))\n        else:\n            res.append((window[k // 2 - 1] + window[k // 2]) / 2.0)\n        if i < len(nums):\n            del window[bisect.bisect_left(window, nums[i - k])]\n            bisect.insort(window, nums[i])\n    return res\n",
        test_cases=[{"input": [[1, 3, -1, -3, 5, 3, 6, 7], 3], "expected": [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]}, {"input": [[1, 2, 3, 4], 2], "expected": [1.5, 2.5, 3.5]}, {"input": [[5], 1], "expected": [5.0]}],
        hints=["Maintain a sorted window with bisect insertion and deletion, reading median at k//2."],
        leetcode_id=480
    ))

    # 17. Max Chunks To Make Sorted II
    problems.append(make_problem(
        pid="ds-h-max-chunks-to-sorted", title="Max Chunks To Make Sorted II",
        wing_id="data-structures", floor=187, difficulty="hard", visualizer_type="array",
        monster_name="Partition Lich", monster_title="Divider of Independent Chunks",
        monster_sprite="lich", monster_color="#8b5cf6", monster_attack="Severing Beam",
        monster_quote="Prefix max and suffix min revealed all valid chunk cuts!",
        description="Given an array of integers `arr` (not necessarily distinct), we split the array into some number of chunks (partitions), and individually sort each chunk. After concatenating them, the result equals the sorted array. Return the largest number of chunks we can make.",
        examples=[{"input": "arr = [5,4,3,2,1]", "output": "1"}, {"input": "arr = [2,1,3,4,4]", "output": "4"}],
        constraints=["1 <= len(arr) <= 2000", "0 <= arr[i] <= 10^8"],
        function_name="maxChunksToSortedHard",
        starter_code="def maxChunksToSortedHard(arr: list[int]) -> int:\n    pass\n",
        solution_code="def maxChunksToSortedHard(arr: list[int]) -> int:\n    n = len(arr)\n    min_right = [0] * n\n    min_right[-1] = arr[-1]\n    for i in range(n - 2, -1, -1):\n        min_right[i] = min(min_right[i + 1], arr[i])\n    chunks = 0\n    max_left = 0\n    for i in range(n - 1):\n        max_left = max(max_left, arr[i])\n        if max_left <= min_right[i + 1]:\n            chunks += 1\n    return chunks + 1\n",
        test_cases=[{"input": [[5, 4, 3, 2, 1]], "expected": 1}, {"input": [[2, 1, 3, 4, 4]], "expected": 4}, {"input": [[1, 1, 1]], "expected": 3}],
        hints=["A chunk can be cut after index i if max(arr[0...i]) <= min(arr[i+1...n-1])."],
        leetcode_id=768
    ))

    # 18. Number of Visible People in a Queue
    problems.append(make_problem(
        pid="ds-h-can-see-persons-count", title="Visible People in a Queue",
        wing_id="data-structures", floor=188, difficulty="hard", visualizer_type="stack",
        monster_name="Sightline Specter", monster_title="Obscurer of Line-of-Sight Rays",
        monster_sprite="wraith", monster_color="#6366f1", monster_attack="Blind Veil",
        monster_quote="Monotonic stack counted all direct line-of-sight people!",
        description="There are `n` people standing in a queue numbered from `0` to `n - 1` from left to right. You are given an array `heights` of distinct integers where `heights[i]` represents the height of the `i-th` person. A person can see another person to their right in the queue if everyone in between is shorter than both of them. Return an array `answer` of length `n` where `answer[i]` is the number of people the `i-th` person can see.",
        examples=[{"input": "heights = [10,6,8,5,11,9]", "output": "[3,1,2,1,1,0]"}, {"input": "heights = [5,1,2,3,10]", "output": "[4,1,1,1,0]"}],
        constraints=["n == len(heights)", "1 <= n <= 10^5", "1 <= heights[i] <= 10^9"],
        function_name="canSeePersonsCount",
        starter_code="def canSeePersonsCount(heights: list[int]) -> list[int]:\n    pass\n",
        solution_code="def canSeePersonsCount(heights: list[int]) -> list[int]:\n    n = len(heights)\n    res = [0] * n\n    stack = []\n    for i in range(n - 1, -1, -1):\n        count = 0\n        while stack and stack[-1] < heights[i]:\n            stack.pop()\n            count += 1\n        if stack:\n            count += 1\n        res[i] = count\n        stack.append(heights[i])\n    return res\n",
        test_cases=[{"input": [[10, 6, 8, 5, 11, 9]], "expected": [3, 1, 2, 1, 1, 0]}, {"input": [[5, 1, 2, 3, 10]], "expected": [4, 1, 1, 1, 0]}, {"input": [[1]], "expected": [0]}],
        hints=["Iterate backwards using a monotonic decreasing stack; each person can see popped shorter people plus one taller person at stack top."],
        leetcode_id=1944
    ))

    # 19. Max Value of Equation
    problems.append(make_problem(
        pid="ds-h-find-max-value-equation", title="Max Value of Equation",
        wing_id="data-structures", floor=189, difficulty="hard", visualizer_type="array",
        monster_name="Coordinate Golem", monster_title="Optimizer of Chebyshev Manhattan Sums",
        monster_sprite="golem", monster_color="#06b6d4", monster_attack="Vector Smash",
        monster_quote="Rewriting equation as (yi - xi) + (yj + xj) maximized the deque!",
        description="You are given an array `points` containing the coordinates of points on a 2D plane, sorted by the x-values, where `points[i] = [xi, yi]` such that `xi < xj` for all `1 <= i < j <= points.length`. You are also given an integer `k`. Return the maximum value of the equation `yi + yj + |xi - xj|` where `|xi - xj| <= k` and `1 <= i < j <= points.length`.",
        examples=[{"input": "points = [[1,3],[2,0],[5,10],[6,-10]], k = 1", "output": "4"}, {"input": "points = [[0,0],[3,0],[9,2]], k = 3", "output": "3"}],
        constraints=["2 <= len(points) <= 10^5", "points[i].length == 2", "-10^8 <= xi, yi <= 10^8", "1 <= k <= 2 * 10^8"],
        function_name="findMaxValueOfEquation",
        starter_code="def findMaxValueOfEquation(points: list[list[int]], k: int) -> int:\n    pass\n",
        solution_code="def findMaxValueOfEquation(points: list[list[int]], k: int) -> int:\n    from collections import deque\n    q = deque()\n    ans = float('-inf')\n    for x, y in points:\n        while q and x - q[0][1] > k:\n            q.popleft()\n        if q:\n            ans = max(ans, x + y + q[0][0])\n        while q and q[-1][0] <= y - x:\n            q.pop()\n        q.append((y - x, x))\n    return ans\n",
        test_cases=[{"input": [[[1, 3], [2, 0], [5, 10], [6, -10]], 1], "expected": 4}, {"input": [[[0, 0], [3, 0], [9, 2]], 3], "expected": 3}],
        hints=["Since xj > xi, yi + yj + |xi - xj| = (yi - xi) + (yj + xj). Maximize (yi - xi) in sliding window."],
        leetcode_id=1499
    ))

    # 20. The Skyline Problem
    problems.append(make_problem(
        pid="ds-h-the-skyline-problem", title="The Skyline Problem",
        wing_id="data-structures", floor=190, difficulty="hard", visualizer_type="array",
        monster_name="Silhouette Titan", monster_title="Architect of Urban Contours",
        monster_sprite="golem", monster_color="#10b981", monster_attack="Rooftop Collapse",
        monster_quote="Sweep-line heap mapped all critical silhouette turning points!",
        description="A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings `[left, right, height]`, return the key points that outline the skyline.",
        examples=[{"input": "buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]", "output": "[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]"}],
        constraints=["1 <= len(buildings) <= 10^4", "0 <= left < right <= 2^31 - 1", "1 <= height <= 2^31 - 1"],
        function_name="getSkyline",
        starter_code="def getSkyline(buildings: list[list[int]]) -> list[list[int]]:\n    pass\n",
        solution_code="def getSkyline(buildings: list[list[int]]) -> list[list[int]]:\n    import heapq\n    events = []\n    for L, R, H in buildings:\n        events.append((L, -H, R))\n        events.append((R, 0, 0))\n    events.sort()\n    res = [[0, 0]]\n    live = [(0, float('inf'))]\n    for pos, negH, R in events:\n        while live[0][1] <= pos:\n            heapq.heappop(live)\n        if negH != 0:\n            heapq.heappush(live, (negH, R))\n        curr_h = -live[0][0]\n        if res[-1][1] != curr_h:\n            res.append([pos, curr_h])\n    return res[1:]\n",
        test_cases=[{"input": [[[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]], "expected": [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]}, {"input": [[[0, 2, 3], [2, 5, 3]]], "expected": [[0, 3], [5, 0]]}],
        hints=["Use event points sorted by x. Maintain max heap of active building heights."],
        leetcode_id=218
    ))

    # 21. Subarray With Elements Greater Than Varying Threshold
    problems.append(make_problem(
        pid="ds-h-valid-subarray-size", title="Subarray Elements > Threshold / Length",
        wing_id="data-structures", floor=191, difficulty="hard", visualizer_type="stack",
        monster_name="Threshold Drake", monster_title="Weigher of Scaled Minimums",
        monster_sprite="dragon", monster_color="#f59e0b", monster_attack="Threshold Blast",
        monster_quote="Monotonic stack span check found the valid threshold length k!",
        description="You are given an integer array `nums` and an integer `threshold`. Find any valid subarray of size `k` such that every element in the subarray is greater than `threshold / k`. Return the size of any such valid subarray, or return `-1` if no such subarray exists.",
        examples=[{"input": "nums = [1,3,4,3,1], threshold = 6", "output": "3"}, {"input": "nums = [6,5,6,5,8], threshold = 7", "output": "1"}],
        constraints=["1 <= len(nums) <= 10^5", "1 <= nums[i], threshold <= 10^9"],
        function_name="validSubarraySize",
        starter_code="def validSubarraySize(nums: list[int], threshold: int) -> int:\n    pass\n",
        solution_code="def validSubarraySize(nums: list[int], threshold: int) -> int:\n    nums = [0] + nums + [0]\n    stack = [0]\n    for i in range(1, len(nums)):\n        while nums[stack[-1]] > nums[i]:\n            val = nums[stack.pop()]\n            k = i - stack[-1] - 1\n            if val > threshold // k:\n                return k\n        stack.append(i)\n    return -1\n",
        test_cases=[{"input": [[1, 3, 4, 3, 1], 6], "expected": 3}, {"input": [[6, 5, 6, 5, 8], 7], "expected": 1}, {"input": [[1, 1], 10], "expected": -1}],
        hints=["Every element can be treated as the minimum of a maximal subarray of width k using monotonic stack."],
        leetcode_id=2334
    ))

    # 22. Count Subarrays With More Than K Elements
    problems.append(make_problem(
        pid="ds-h-count-subarrays-k", title="Count Subarrays Where Max Element Appears >= K Times",
        wing_id="data-structures", floor=192, difficulty="hard", visualizer_type="array",
        monster_name="Max-Frequency Daemon", monster_title="Lord of the Peak Frequencies",
        monster_sprite="demon", monster_color="#ef4444", monster_attack="Frequency Flare",
        monster_quote="Sliding window counted all right-extended subarrays!",
        description="You are given an integer array `nums` and a positive integer `k`. Return the number of subarrays where the maximum element of `nums` appears at least `k` times in that subarray.",
        examples=[{"input": "nums = [1,3,2,3,3], k = 2", "output": "6"}, {"input": "nums = [1,4,2,1], k = 3", "output": "0"}],
        constraints=["1 <= len(nums) <= 10^5", "1 <= nums[i] <= 10^6", "1 <= k <= 10^5"],
        function_name="countSubarraysK",
        starter_code="def countSubarraysK(nums: list[int], k: int) -> int:\n    pass\n",
        solution_code="def countSubarraysK(nums: list[int], k: int) -> int:\n    max_val = max(nums)\n    ans = left = count = 0\n    for right, x in enumerate(nums):\n        if x == max_val: count += 1\n        while count >= k:\n            if nums[left] == max_val: count -= 1\n            left += 1\n        ans += left\n    return ans\n",
        test_cases=[{"input": [[1, 3, 2, 3, 3], 2], "expected": 6}, {"input": [[1, 4, 2, 1], 3], "expected": 0}, {"input": [[5, 5, 5], 1], "expected": 6}],
        hints=["Find max_val, then use sliding window to count valid subarrays ending at right."],
        leetcode_id=2962
    ))

    # 23. Falling Squares Simulation
    problems.append(make_problem(
        pid="ds-h-falling-squares", title="Falling Squares Simulation",
        wing_id="data-structures", floor=193, difficulty="hard", visualizer_type="array",
        monster_name="Tetris Golem", monster_title="Stacker of Heavy Cubes",
        monster_sprite="golem", monster_color="#a855f7", monster_attack="Square Drop",
        monster_quote="Interval coordinate height compression tracked max elevation!",
        description="There are several squares being dropped onto an X-axis. You are given a 2D integer array `positions` where `positions[i] = [left_i, sideLength_i]`. Return an array of the maximum height of the stack of squares after each square is dropped.",
        examples=[{"input": "positions = [[1,2],[2,3],[6,1]]", "output": "[2,5,5]"}, {"input": "positions = [[100,100],[200,100]]", "output": "[100,100]"}],
        constraints=["1 <= len(positions) <= 1000", "1 <= left <= 10^8", "1 <= sideLength <= 10^6"],
        function_name="fallingSquaresSimulator",
        starter_code="def fallingSquaresSimulator(positions: list[list[int]]) -> list[int]:\n    pass\n",
        solution_code="def fallingSquaresSimulator(positions: list[list[int]]) -> list[int]:\n    intervals = []\n    res = []\n    max_h = 0\n    for left, size in positions:\n        right = left + size\n        h = size\n        for l, r, prev_h in intervals:\n            if not (right <= l or left >= r):\n                h = max(h, prev_h + size)\n        intervals.append((left, right, h))\n        max_h = max(max_h, h)\n        res.append(max_h)\n    return res\n",
        test_cases=[{"input": [[[1, 2], [2, 3], [6, 1]]], "expected": [2, 5, 5]}, {"input": [[[100, 100], [200, 100]]], "expected": [100, 100]}],
        hints=["Track interval heights. When dropping [left, right], base height is max overlapping interval height."],
        leetcode_id=699
    ))

    # 24. Maximum Frequency Stack
    problems.append(make_problem(
        pid="ds-h-freq-stack", title="Maximum Frequency Stack Simulator",
        wing_id="data-structures", floor=194, difficulty="hard", visualizer_type="stack",
        monster_name="Resonance Lich", monster_title="Drainer of Most Frequent Echoes",
        monster_sprite="lich", monster_color="#ec4899", monster_attack="Frequency Drain",
        monster_quote="Map of stacks by frequency returned highest-frequency elements first!",
        description="Design a stack-like data structure to push elements, and pop the most frequent element from the stack. If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned. Given a list of operations `[\"push\", x]` or `[\"pop\"]`, return the outputs of `pop`.",
        examples=[{"input": "commands = [[\"push\",5],[\"push\",7],[\"push\",5],[\"push\",7],[\"push\",4],[\"push\",5],[\"pop\"],[\"pop\"],[\"pop\"],[\"pop\"]]", "output": "[5,7,5,4]"}],
        constraints=["1 <= len(commands) <= 10^4"],
        function_name="freqStackSimulator",
        starter_code="def freqStackSimulator(commands: list) -> list[int]:\n    pass\n",
        solution_code="def freqStackSimulator(commands: list) -> list[int]:\n    from collections import defaultdict\n    freq = defaultdict(int)\n    group = defaultdict(list)\n    max_f = 0\n    res = []\n    for cmd in commands:\n        if cmd[0] == 'push':\n            val = cmd[1]\n            f = freq[val] + 1\n            freq[val] = f\n            if f > max_f: max_f = f\n            group[f].append(val)\n        elif cmd[0] == 'pop':\n            x = group[max_f].pop()\n            freq[x] -= 1\n            if not group[max_f]:\n                max_f -= 1\n            res.append(x)\n    return res\n",
        test_cases=[{"input": [[["push", 5], ["push", 7], ["push", 5], ["push", 7], ["push", 4], ["push", 5], ["pop"], ["pop"], ["pop"], ["pop"]]], "expected": [5, 7, 5, 4]}],
        hints=["Maintain a map from frequency to a stack of elements having that frequency."],
        leetcode_id=895
    ))

    # 25. Sum of Subsequence Widths
    problems.append(make_problem(
        pid="ds-h-sum-subseq-widths", title="Sum of Subsequence Widths",
        wing_id="data-structures", floor=195, difficulty="hard", visualizer_type="array",
        monster_name="Combinatorial Archon", monster_title="Multiplier of Subsequence Extremes",
        monster_sprite="beholder", monster_color="#e11d48", monster_attack="Extreme Beam",
        monster_quote="Powers of 2 sorted contribution summed in O(n log n)!",
        description="The width of a sequence is the difference between the maximum and minimum elements in the sequence. Given an array of integers `nums`, return the sum of the widths of all non-empty subsequences of `nums` modulo `10^9 + 7`.",
        examples=[{"input": "nums = [2,1,3]", "output": "6"}, {"input": "nums = [1]", "output": "0"}],
        constraints=["1 <= len(nums) <= 20000", "1 <= nums[i] <= 20000"],
        function_name="sumSubseqWidths",
        starter_code="def sumSubseqWidths(nums: list[int]) -> int:\n    pass\n",
        solution_code="def sumSubseqWidths(nums: list[int]) -> int:\n    MOD = 10**9 + 7\n    nums.sort()\n    n = len(nums)\n    pow2 = [1] * n\n    for i in range(1, n): pow2[i] = (pow2[i - 1] * 2) % MOD\n    ans = 0\n    for i in range(n):\n        ans = (ans + (pow2[i] - pow2[n - 1 - i]) * nums[i]) % MOD\n    return ans\n",
        test_cases=[{"input": [[2, 1, 3]], "expected": 6}, {"input": [[1]], "expected": 0}, {"input": [[1, 2]], "expected": 1}],
        hints=["Sort nums. nums[i] is the max in 2^i subsequences and the min in 2^(n-1-i) subsequences."],
        leetcode_id=891
    ))

    # 26. Minimum Cost to Hire K Workers
    problems.append(make_problem(
        pid="ds-h-mincost-hire-workers", title="Minimum Cost to Hire K Workers",
        wing_id="data-structures", floor=196, difficulty="hard", visualizer_type="array",
        monster_name="Wage Overseer", monster_title="Gauger of Wage-to-Quality Ratios",
        monster_sprite="orc", monster_color="#f59e0b", monster_attack="Wage Strike",
        monster_quote="Sorting by wage/quality ratio and max-heap of qualities gave min cost!",
        description="There are `n` workers. You are given two integer arrays `quality` and `wage` where `quality[i]` is the quality of the `i-th` worker and `wage[i]` is the minimum wage expectation. We want to hire exactly `k` workers such that every worker is paid proportional to their quality compared to others, and at least their minimum wage. Return the least amount of money needed to form a paid group.",
        examples=[{"input": "quality = [10,20,5], wage = [70,50,30], k = 2", "output": "105.0"}, {"input": "quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3", "output": "30.66667"}],
        constraints=["1 <= k <= len(quality) == len(wage) <= 10^4"],
        function_name="mincostToHireWorkers",
        starter_code="def mincostToHireWorkers(quality: list[int], wage: list[int], k: int) -> float:\n    pass\n",
        solution_code="def mincostToHireWorkers(quality: list[int], wage: list[int], k: int) -> float:\n    import heapq\n    workers = sorted([(w / q, q) for w, q in zip(wage, quality)])\n    max_heap = []\n    q_sum = 0\n    min_cost = float('inf')\n    for ratio, q in workers:\n        heapq.heappush(max_heap, -q)\n        q_sum += q\n        if len(max_heap) > k:\n            q_sum += heapq.heappop(max_heap)\n        if len(max_heap) == k:\n            min_cost = min(min_cost, ratio * q_sum)\n    return round(min_cost, 5)\n",
        test_cases=[{"input": [[10, 20, 5], [70, 50, 30], 2], "expected": 105.0}, {"input": [[3, 1, 10, 10, 1], [4, 8, 2, 2, 7], 3], "expected": 30.66667}],
        hints=["Sort by wage/quality ratio. Maintain max heap of qualities of size k."],
        leetcode_id=857
    ))

    # 27. Maximum Performance of a Team
    problems.append(make_problem(
        pid="ds-h-max-performance-team", title="Maximum Performance of a Team",
        wing_id="data-structures", floor=197, difficulty="hard", visualizer_type="array",
        monster_name="Synergy Colossus", monster_title="Multiplier of Team Efficiencies",
        monster_sprite="golem", monster_color="#38bdf8", monster_attack="Synergy Slam",
        monster_quote="Sorting by decreasing efficiency and min-heap of speeds maximized score!",
        description="You are given two integers `n` and `k` and two integer arrays `speed` and `efficiency` both of length `n`. There are `n` engineers. The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers. Return the maximum performance of this team at most `k` engineers modulo `10^9 + 7`.",
        examples=[{"input": "n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2", "output": "60"}, {"input": "n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3", "output": "68"}],
        constraints=["1 <= k <= n <= 10^5"],
        function_name="maxPerformance",
        starter_code="def maxPerformance(n: int, speed: list[int], efficiency: list[int], k: int) -> int:\n    pass\n",
        solution_code="def maxPerformance(n: int, speed: list[int], efficiency: list[int], k: int) -> int:\n    import heapq\n    MOD = 10**9 + 7\n    engineers = sorted(zip(efficiency, speed), reverse=True)\n    speed_heap = []\n    speed_sum = 0\n    max_perf = 0\n    for eff, spd in engineers:\n        heapq.heappush(speed_heap, spd)\n        speed_sum += spd\n        if len(speed_heap) > k:\n            speed_sum -= heapq.heappop(speed_heap)\n        max_perf = max(max_perf, speed_sum * eff)\n    return max_perf % MOD\n",
        test_cases=[{"input": [6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2], "expected": 60}, {"input": [6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3], "expected": 68}],
        hints=["Sort by decreasing efficiency. Use min-heap of size at most k for speeds."],
        leetcode_id=1383
    ))

    # 28. IPO (Maximize Capital)
    problems.append(make_problem(
        pid="ds-h-ipo-capital", title="IPO (Maximize Capital)",
        wing_id="data-structures", floor=198, difficulty="hard", visualizer_type="array",
        monster_name="Venture Arch-Fiend", monster_title="Harvester of Maximal Returns",
        monster_sprite="demon", monster_color="#10b981", monster_attack="Capital Shock",
        monster_quote="Greedy max-heap on available projects multiplied initial capital!",
        description="You are given `n` projects where the `i-th` project has a pure profit `profits[i]` and a minimum capital `capital[i]` needed to start it. Initially, you have `w` capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital. Pick a list of at most `k` distinct projects from given projects to maximize your final capital.",
        examples=[{"input": "k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]", "output": "4"}, {"input": "k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]", "output": "6"}],
        constraints=["1 <= k <= 10^5", "0 <= w <= 10^9", "1 <= len(profits) == len(capital) <= 10^5"],
        function_name="findMaximizedCapital",
        starter_code="def findMaximizedCapital(k: int, w: int, profits: list[int], capital: list[int]) -> int:\n    pass\n",
        solution_code="def findMaximizedCapital(k: int, w: int, profits: list[int], capital: list[int]) -> int:\n    import heapq\n    projects = sorted(zip(capital, profits))\n    max_heap = []\n    idx = 0\n    n = len(projects)\n    for _ in range(k):\n        while idx < n and projects[idx][0] <= w:\n            heapq.heappush(max_heap, -projects[idx][1])\n            idx += 1\n        if not max_heap:\n            break\n        w += -heapq.heappop(max_heap)\n    return w\n",
        test_cases=[{"input": [2, 0, [1, 2, 3], [0, 1, 1]], "expected": 4}, {"input": [3, 0, [1, 2, 3], [0, 1, 2]], "expected": 6}],
        hints=["Sort by required capital. Push available projects to max-heap of profits and pick top."],
        leetcode_id=502
    ))

    # 29. Median of Two Sorted Arrays
    problems.append(make_problem(
        pid="ds-h-median-sorted-arrays", title="Median of Two Sorted Arrays",
        wing_id="data-structures", floor=199, difficulty="hard", visualizer_type="array",
        monster_name="Dual-Stream Sphinx", monster_title="Gatekeeper of the Halfway Partition",
        monster_sprite="beholder", monster_color="#8b5cf6", monster_attack="Binary Partition Gaze",
        monster_quote="Binary searching the partition of the shorter array solved in O(log(min(m, n)))!",
        description="Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays. The overall run time complexity should be `O(log (m+n))`.",
        examples=[{"input": "nums1 = [1,3], nums2 = [2]", "output": "2.0"}, {"input": "nums1 = [1,2], nums2 = [3,4]", "output": "2.5"}],
        constraints=["0 <= len(nums1), len(nums2) <= 1000", "1 <= len(nums1) + len(nums2) <= 2000"],
        function_name="findMedianSortedArrays",
        starter_code="def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:\n    pass\n",
        solution_code="def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:\n    A, B = nums1, nums2\n    total = len(nums1) + len(nums2)\n    half = total // 2\n    if len(B) < len(A): A, B = B, A\n    l, r = 0, len(A) - 1\n    while True:\n        i = (l + r) // 2\n        j = half - i - 2\n        Aleft = A[i] if i >= 0 else float('-inf')\n        Aright = A[i + 1] if (i + 1) < len(A) else float('inf')\n        Bleft = B[j] if j >= 0 else float('-inf')\n        Bright = B[j + 1] if (j + 1) < len(B) else float('inf')\n        if Aleft <= Bright and Bleft <= Aright:\n            if total % 2:\n                return float(min(Aright, Bright))\n            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0\n        elif Aleft > Bright:\n            r = i - 1\n        else:\n            l = i + 1\n",
        test_cases=[{"input": [[1, 3], [2]], "expected": 2.0}, {"input": [[1, 2], [3, 4]], "expected": 2.5}, {"input": [[0, 0], [0, 0]], "expected": 0.0}],
        hints=["Binary search partition in the smaller array such that max(left) <= min(right)."],
        leetcode_id=4
    ))

    # 30. Reverse Nodes in k-Group
    problems.append(make_problem(
        pid="ds-h-reverse-k-group", title="Reverse Nodes in k-Group",
        wing_id="data-structures", floor=200, difficulty="hard", visualizer_type="array",
        monster_name="K-Group Arch-Demon", monster_title="Grand Boss of the Structure Vault",
        monster_sprite="demon", monster_color="#e11d48", monster_attack="K-Group Annihilation",
        monster_quote="Every complete cluster of k nodes was inverted without breaking the tail!",
        description="Given the head values of a linked list as an array, reverse the nodes of the list `k` at a time, and return the modified list. If the number of nodes is not a multiple of `k` then left-out nodes, in the end, should remain as it is.",
        examples=[{"input": "head = [1,2,3,4,5], k = 2", "output": "[2,1,4,3,5]"}, {"input": "head = [1,2,3,4,5], k = 3", "output": "[3,2,1,4,5]"}],
        constraints=["1 <= k <= len(head) <= 5000", "0 <= head[i] <= 1000"],
        function_name="reverseKGroup",
        starter_code="def reverseKGroup(head: list[int], k: int) -> list[int]:\n    pass\n",
        solution_code="def reverseKGroup(head: list[int], k: int) -> list[int]:\n    res = []\n    n = len(head)\n    for i in range(0, n, k):\n        chunk = head[i:i + k]\n        if len(chunk) == k:\n            res.extend(reversed(chunk))\n        else:\n            res.extend(chunk)\n    return res\n",
        test_cases=[{"input": [[1, 2, 3, 4, 5], 2], "expected": [2, 1, 4, 3, 5]}, {"input": [[1, 2, 3, 4, 5], 3], "expected": [3, 2, 1, 4, 5]}, {"input": [[1], 1], "expected": [1]}],
        hints=["Reverse chunks of size k. If remaining chunk size < k, preserve original order."],
        leetcode_id=25
    ))

    return problems
