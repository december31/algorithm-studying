"""
Data Structures Medium Problems Part 2 (Problems 11 to 35).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_data_structures_medium_part2():
    problems = []

    # 11. Decode String
    problems.append(make_problem(
        pid="ds-m-decode-string",
        title="Decode String",
        wing_id="data-structures",
        floor=121,
        difficulty="medium",
        visualizerType="stack",
        monster_name="Cipher Banshee",
        monster_title="Shrieker of Compressed Runs",
        monster_sprite="wraith",
        monster_color="#8b5cf6",
        monster_attack="Frequency Wail",
        monster_quote="My nested brackets have unfolded completely!",
        description="Given an encoded string `s`, return its decoded string. The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times.",
        examples=[
            {"input": "s = \"3[a]2[bc]\"", "output": "\"aaabcbc\""},
            {"input": "s = \"3[a2[c]]\"", "output": "\"accaccacc\""},
            {"input": "s = \"2[abc]3[cd]ef\"", "output": "\"abcabccdcdcdef\""}
        ],
        constraints=["1 <= len(s) <= 30", "s consists of lowercase English letters, digits, and square brackets"],
        function_name="decodeString",
        starter_code="def decodeString(s: str) -> str:\n    pass\n",
        solution_code="def decodeString(s: str) -> str:\n    stack = []\n    curr_str = ''\n    curr_num = 0\n    for ch in s:\n        if ch.isdigit():\n            curr_num = curr_num * 10 + int(ch)\n        elif ch == '[':\n            stack.append((curr_str, curr_num))\n            curr_str = ''\n            curr_num = 0\n        elif ch == ']':\n            prev_str, repeat = stack.pop()\n            curr_str = prev_str + curr_str * repeat\n        else:\n            curr_str += ch\n    return curr_str\n",
        test_cases=[
            {"input": ["3[a]2[bc]"], "expected": "aaabcbc"},
            {"input": ["3[a2[c]]"], "expected": "accaccacc"},
            {"input": ["2[abc]3[cd]ef"], "expected": "abcabccdcdcdef"},
            {"input": ["abc"], "expected": "abc"},
        ],
        hints=["Use a stack to remember previous string states and multipliers when entering brackets."],
        leetcode_id=394,
    ))

    # 12. Remove K Digits
    problems.append(make_problem(
        pid="ds-m-remove-k-digits",
        title="Remove K Digits",
        wing_id="data-structures",
        floor=122,
        difficulty="medium",
        visualizerType="stack",
        monster_name="Greedy Numeral Lich",
        monster_title="Easer of Leading Magnitudes",
        monster_sprite="lich",
        monster_color="#06b6d4",
        monster_attack="Peak Scythe",
        monster_quote="My larger high-order digits were culled by your greedy stack!",
        description="Given string `num` representing a non-negative integer and an integer `k`, return the smallest possible integer after removing `k` digits from `num` as a string without leading zeros (or \"0\" if empty).",
        examples=[
            {"input": "num = \"1432219\", k = 3", "output": "\"1219\""},
            {"input": "num = \"10200\", k = 1", "output": "\"200\""},
            {"input": "num = \"10\", k = 2", "output": "\"0\""}
        ],
        constraints=["1 <= k <= len(num) <= 10^5", "num consists of only digits"],
        function_name="removeKdigits",
        starter_code="def removeKdigits(num: str, k: int) -> str:\n    pass\n",
        solution_code="def removeKdigits(num: str, k: int) -> str:\n    stack = []\n    for d in num:\n        while k > 0 and stack and stack[-1] > d:\n            stack.pop()\n            k -= 1\n        stack.append(d)\n    while k > 0 and stack:\n        stack.pop()\n        k -= 1\n    res = ''.join(stack).lstrip('0')\n    return res if res else '0'\n",
        test_cases=[
            {"input": ["1432219", 3], "expected": "1219"},
            {"input": ["10200", 1], "expected": "200"},
            {"input": ["10", 2], "expected": "0"},
            {"input": ["9", 1], "expected": "0"},
        ],
        hints=["Monotonic increasing stack; pop larger elements when encountering smaller ones."],
        leetcode_id=402,
    ))

    # 13. Online Stock Span
    problems.append(make_problem(
        pid="ds-m-online-stock-span",
        title="Online Stock Span",
        wing_id="data-structures",
        floor=123,
        difficulty="medium",
        visualizerType="stack",
        monster_name="Market Bull-Demon",
        monster_title="Charger of Consecutive Bull Runs",
        monster_sprite="demon",
        monster_color="#10b981",
        monster_attack="Trend Spike",
        monster_quote="You tracked every continuous price span with a monotonic stack!",
        description="Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day. The span is the maximum number of consecutive days (starting today and going backwards) for which the price was less than or equal to today's price. Given a list of daily quotes `prices`, return the array of spans.",
        examples=[
            {"input": "prices = [100,80,60,70,60,75,85]", "output": "[1,1,1,2,1,4,6]"}
        ],
        constraints=["1 <= len(prices) <= 10^5", "1 <= prices[i] <= 10^5"],
        function_name="stockSpans",
        starter_code="def stockSpans(prices: list[int]) -> list[int]:\n    pass\n",
        solution_code="def stockSpans(prices: list[int]) -> list[int]:\n    stack = []\n    spans = []\n    for p in prices:\n        span = 1\n        while stack and stack[-1][0] <= p:\n            span += stack.pop()[1]\n        stack.append((p, span))\n        spans.append(span)\n    return spans\n",
        test_cases=[
            {"input": [[100, 80, 60, 70, 60, 75, 85]], "expected": [1, 1, 1, 2, 1, 4, 6]},
            {"input": [[10, 20, 30, 40]], "expected": [1, 2, 3, 4]},
            {"input": [[50, 40, 30]], "expected": [1, 1, 1]},
            {"input": [[50]], "expected": [1]},
        ],
        hints=["Maintain a stack of pairs (price, span). Pop smaller or equal elements and add their spans."],
        leetcode_id=901,
    ))

    # 14. Validate Stack Sequences
    problems.append(make_problem(
        pid="ds-m-validate-stack-sequences",
        title="Validate Stack Sequences",
        wing_id="data-structures",
        floor=124,
        difficulty="medium",
        visualizerType="stack",
        monster_name="LIFO Warden",
        monster_title="Inspector of Push-Pop Alignments",
        monster_sprite="golem",
        monster_color="#eab308",
        monster_attack="LIFO Hammer",
        monster_quote="Your simulated stack verified the sequence perfectly!",
        description="Given two integer arrays `pushed` and `popped` each with distinct values, return `True` if this could have been the result of a sequence of push and pop operations on an initially empty stack, or `False` otherwise.",
        examples=[
            {"input": "pushed = [1,2,3,4,5], popped = [4,5,3,2,1]", "output": "True"},
            {"input": "pushed = [1,2,3,4,5], popped = [4,3,5,1,2]", "output": "False"}
        ],
        constraints=["1 <= len(pushed) <= 1000", "0 <= pushed[i] <= 1000", "pushed and popped are permutations of each other"],
        function_name="validateStackSequences",
        starter_code="def validateStackSequences(pushed: list[int], popped: list[int]) -> bool:\n    pass\n",
        solution_code="def validateStackSequences(pushed: list[int], popped: list[int]) -> bool:\n    stack = []\n    pop_idx = 0\n    for val in pushed:\n        stack.append(val)\n        while stack and pop_idx < len(popped) and stack[-1] == popped[pop_idx]:\n            stack.pop()\n            pop_idx += 1\n    return pop_idx == len(popped)\n",
        test_cases=[
            {"input": [[1, 2, 3, 4, 5], [4, 5, 3, 2, 1]], "expected": True},
            {"input": [[1, 2, 3, 4, 5], [4, 3, 5, 1, 2]], "expected": False},
            {"input": [[1], [1]], "expected": True},
            {"input": [[2, 1, 0], [1, 2, 0]], "expected": True},
        ],
        hints=["Simulate push operations, and greedily pop while stack top matches current popped element."],
        leetcode_id=946,
    ))

    # 15. Sum of Subarray Minimums
    problems.append(make_problem(
        pid="ds-m-sum-subarray-mins",
        title="Sum of Subarray Minimums",
        wing_id="data-structures",
        floor=125,
        difficulty="medium",
        visualizerType="stack",
        monster_name="Subarray Trough Fiend",
        monster_title="Accumulator of Valley Boundaries",
        monster_sprite="slime",
        monster_color="#f97316",
        monster_attack="Valley Compression",
        monster_quote="Contribution of every minimum calculated modulo 10^9 + 7!",
        description="Given an array of integers `arr`, find the sum of `min(b)`, where `b` ranges over every (contiguous) subarray of `arr`. Since the answer may be large, return the answer modulo `10^9 + 7`.",
        examples=[
            {"input": "arr = [3,1,2,4]", "output": "17"},
            {"input": "arr = [11,81,94,43,3]", "output": "444"}
        ],
        constraints=["1 <= len(arr) <= 3 * 10^4", "1 <= arr[i] <= 3 * 10^4"],
        function_name="sumSubarrayMins",
        starter_code="def sumSubarrayMins(arr: list[int]) -> int:\n    pass\n",
        solution_code="def sumSubarrayMins(arr: list[int]) -> int:\n    MOD = 10**9 + 7\n    n = len(arr)\n    left = [0] * n\n    right = [0] * n\n    s1 = []\n    for i in range(n):\n        count = 1\n        while s1 and s1[-1][0] > arr[i]:\n            count += s1.pop()[1]\n        s1.append((arr[i], count))\n        left[i] = count\n    s2 = []\n    for i in range(n - 1, -1, -1):\n        count = 1\n        while s2 and s2[-1][0] >= arr[i]:\n            count += s2.pop()[1]\n        s2.append((arr[i], count))\n        right[i] = count\n    ans = sum(arr[i] * left[i] * right[i] for i in range(n)) % MOD\n    return ans\n",
        test_cases=[
            {"input": [[3, 1, 2, 4]], "expected": 17},
            {"input": [[11, 81, 94, 43, 3]], "expected": 444},
            {"input": [[5]], "expected": 5},
            {"input": [[7, 7]], "expected": 21},
        ],
        hints=["Calculate number of subarrays where arr[i] is the minimum using monotonic stacks for left and right spans."],
        leetcode_id=907,
    ))

    # 16. Score of Parentheses
    problems.append(make_problem(
        pid="ds-m-score-of-parentheses",
        title="Score of Parentheses",
        wing_id="data-structures",
        floor=126,
        difficulty="medium",
        visualizerType="stack",
        monster_name="Nesting Sprite",
        monster_title="Multiplier of Balanced Depths",
        monster_sprite="slime",
        monster_color="#ec4899",
        monster_attack="Depth Shock",
        monster_quote="Balanced parentheses evaluated to their correct score!",
        description="Given a balanced parentheses string `s`, return the score of the string. `()` has score 1, `AB` has score `A + B`, and `(A)` has score `2 * A`.",
        examples=[
            {"input": "s = \"()\"", "output": "1"},
            {"input": "s = \"(())\"", "output": "2"},
            {"input": "s = \"()()\"", "output": "2"},
            {"input": "s = \"(()(()))\"", "output": "6"}
        ],
        constraints=["2 <= len(s) <= 50", "s is a balanced parentheses string"],
        function_name="scoreOfParentheses",
        starter_code="def scoreOfParentheses(s: str) -> int:\n    pass\n",
        solution_code="def scoreOfParentheses(s: str) -> int:\n    stack = [0]\n    for ch in s:\n        if ch == '(':\n            stack.append(0)\n        else:\n            v = stack.pop()\n            stack[-1] += max(2 * v, 1)\n    return stack[0]\n",
        test_cases=[
            {"input": ["()"], "expected": 1},
            {"input": ["(())"], "expected": 2},
            {"input": ["()()"], "expected": 2},
            {"input": ["(()(()))"], "expected": 6},
        ],
        hints=["Use a stack to accumulate scores at each parenthesis nesting depth."],
        leetcode_id=856,
    ))

    # 17. Next Greater Element II (Circular)
    problems.append(make_problem(
        pid="ds-m-next-greater-element-ii",
        title="Next Greater Element II (Circular Array)",
        wing_id="data-structures",
        floor=127,
        difficulty="medium",
        visualizerType="stack",
        monster_name="Ouroboros Specter",
        monster_title="Guardian of the Looping Index",
        monster_sprite="dragon",
        monster_color="#38bdf8",
        monster_attack="Tail Whip Cycle",
        monster_quote="Even looping twice around the ring could not evade your stack!",
        description="Given a circular integer array `nums`, return the next greater number for every element in `nums`. If it doesn't exist, return -1 for this number.",
        examples=[
            {"input": "nums = [1,2,1]", "output": "[2,-1,2]"},
            {"input": "nums = [1,2,3,4,3]", "output": "[2,3,4,-1,4]"}
        ],
        constraints=["1 <= len(nums) <= 10^4", "-10^9 <= nums[i] <= 10^9"],
        function_name="nextGreaterElements",
        starter_code="def nextGreaterElements(nums: list[int]) -> list[int]:\n    pass\n",
        solution_code="def nextGreaterElements(nums: list[int]) -> list[int]:\n    n = len(nums)\n    res = [-1] * n\n    stack = []\n    for i in range(2 * n):\n        num = nums[i % n]\n        while stack and nums[stack[-1]] < num:\n            idx = stack.pop()\n            res[idx] = num\n        if i < n:\n            stack.append(i)\n    return res\n",
        test_cases=[
            {"input": [[1, 2, 1]], "expected": [2, -1, 2]},
            {"input": [[1, 2, 3, 4, 3]], "expected": [2, 3, 4, -1, 4]},
            {"input": [[5, 4, 3, 2, 1]], "expected": [-1, 5, 5, 5, 5]},
            {"input": [[1]], "expected": [-1]},
        ],
        hints=["Simulate circular array by iterating 2 * n times using modulo n with a monotonic stack."],
        leetcode_id=503,
    ))

    # 18. Next Greater Node in Linked List
    problems.append(make_problem(
        pid="ds-m-next-larger-nodes",
        title="Next Greater Value in Sequence",
        wing_id="data-structures",
        floor=128,
        difficulty="medium",
        visualizerType="stack",
        monster_name="Chain Phantom",
        monster_title="Lookahead Wraith of Linked Links",
        monster_sprite="wraith",
        monster_color="#a855f7",
        monster_attack="Chain Drain",
        monster_quote="The next strictly greater value was spotted down the line!",
        description="You are given an integer array `values` representing node values in a singly linked list. Return an array of integers `answer` where `answer[i]` is the value of the next greater node for the `i-th` node. If no greater node exists, `answer[i] = 0`.",
        examples=[
            {"input": "values = [2,1,5]", "output": "[5,5,0]"},
            {"input": "values = [2,7,4,3,5]", "output": "[7,0,5,5,0]"}
        ],
        constraints=["1 <= len(values) <= 10^4", "1 <= values[i] <= 10^9"],
        function_name="nextLargerNodes",
        starter_code="def nextLargerNodes(values: list[int]) -> list[int]:\n    pass\n",
        solution_code="def nextLargerNodes(values: list[int]) -> list[int]:\n    res = [0] * len(values)\n    stack = []\n    for i, v in enumerate(values):\n        while stack and values[stack[-1]] < v:\n            idx = stack.pop()\n            res[idx] = v\n        stack.append(i)\n    return res\n",
        test_cases=[
            {"input": [[2, 1, 5]], "expected": [5, 5, 0]},
            {"input": [[2, 7, 4, 3, 5]], "expected": [7, 0, 5, 5, 0]},
            {"input": [[1, 7, 5, 1, 9, 2, 5, 1]], "expected": [7, 9, 9, 9, 0, 5, 0, 0]},
            {"input": [[3]], "expected": [0]},
        ],
        hints=["Store indices in a decreasing monotonic stack."],
        leetcode_id=1019,
    ))

    # 19. Reorganize String
    problems.append(make_problem(
        pid="ds-m-reorganize-string",
        title="Reorganize String (No Adjacent Equal)",
        wing_id="data-structures",
        floor=129,
        difficulty="medium",
        visualizerType="array",
        monster_name="Alternating Drake",
        monster_title="Enforcer of Non-Repeating Breaths",
        monster_sprite="dragon",
        monster_color="#14b8a6",
        monster_attack="Alternating Fire",
        monster_quote="Your max-heap interleaved my characters without repetition!",
        description="Given a string `s`, rearrange the characters of `s` so that any two adjacent characters are not the same. Return any possible rearrangement of `s` or return `\"\"` if not possible.",
        examples=[
            {"input": "s = \"aab\"", "output": "\"aba\""},
            {"input": "s = \"aaab\"", "output": "\"\""}
        ],
        constraints=["1 <= len(s) <= 500", "s consists of lowercase English letters"],
        function_name="reorganizeString",
        starter_code="def reorganizeString(s: str) -> str:\n    pass\n",
        solution_code="def reorganizeString(s: str) -> str:\n    import heapq\n    from collections import Counter\n    counts = Counter(s)\n    max_freq = max(counts.values())\n    if max_freq > (len(s) + 1) // 2:\n        return \"\"\n    heap = [(-count, ch) for ch, count in counts.items()]\n    heapq.heapify(heap)\n    res = []\n    prev_cnt, prev_ch = 0, ''\n    while heap:\n        cnt, ch = heapq.heappop(heap)\n        res.append(ch)\n        if prev_cnt < 0:\n            heapq.heappush(heap, (prev_cnt, prev_ch))\n        prev_cnt = cnt + 1\n        prev_ch = ch\n    return ''.join(res)\n",
        test_cases=[
            {"input": ["aab"], "expected": "aba"},
            {"input": ["aaab"], "expected": ""},
            {"input": ["vvvlo"], "expected": "vlvov"},
            {"input": ["a"], "expected": "a"},
        ],
        hints=["Use a max-heap of character frequencies, pulling the top two alternating."],
        leetcode_id=767,
    ))

    # 20. Task Scheduler Cooldown
    problems.append(make_problem(
        pid="ds-m-least-interval",
        title="Task Scheduler Minimum Time",
        wing_id="data-structures",
        floor=130,
        difficulty="medium",
        visualizerType="array",
        monster_name="Chrono Taskmaster",
        monster_title="Overlord of Idle CPU Slots",
        monster_sprite="lich",
        monster_color="#e11d48",
        monster_attack="Idle Stasis",
        monster_quote="The mathematical idle calculation minimized CPU downtime!",
        description="Given a characters array `tasks`, representing the tasks a CPU needs to do, where each letter represents a different task. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle. However, there is a non-negative integer `n` that represents the cooldown period between two same tasks. Return the least number of units of times that the CPU will take to finish all the given tasks.",
        examples=[
            {"input": "tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 2", "output": "8"},
            {"input": "tasks = [\"A\",\"A\",\"A\",\"B\",\"B\",\"B\"], n = 0", "output": "6"},
            {"input": "tasks = [\"A\",\"A\",\"A\",\"A\",\"A\",\"A\",\"B\",\"C\",\"D\",\"E\",\"F\",\"G\"], n = 2", "output": "16"}
        ],
        constraints=["1 <= len(tasks) <= 10^4", "0 <= n <= 100", "tasks[i] is uppercase English letter"],
        function_name="leastInterval",
        starter_code="def leastInterval(tasks: list[str], n: int) -> int:\n    pass\n",
        solution_code="def leastInterval(tasks: list[str], n: int) -> int:\n    from collections import Counter\n    counts = Counter(tasks)\n    max_f = max(counts.values())\n    count_max_f = sum(1 for v in counts.values() if v == max_f)\n    empty_slots = (max_f - 1) * (n + 1) + count_max_f\n    return max(len(tasks), empty_slots)\n",
        test_cases=[
            {"input": [["A", "A", "A", "B", "B", "B"], 2], "expected": 8},
            {"input": [["A", "A", "A", "B", "B", "B"], 0], "expected": 6},
            {"input": [["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2], "expected": 16},
            {"input": [["A"], 2], "expected": 1},
        ],
        hints=["Calculate based on the most frequent task: (max_f - 1) * (n + 1) + count_of_max_f."],
        leetcode_id=621,
    ))

    return problems
