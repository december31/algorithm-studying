import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_data_structures_problems():
    problems = []

    # -------------------------------------------------------------------------
    # 10 EASY PROBLEMS
    # -------------------------------------------------------------------------
    # 1. Remove Duplicates from Sorted Array
    problems.append(make_problem(
        pid="ds-e-remove-duplicates",
        title="Remove Duplicates from Sorted Array",
        wing_id="data-structures",
        floor=101,
        difficulty="easy",
        visualizerType="array",
        monster_name="Shard Imp",
        monster_title="Minor Collector of Redundant Runes",
        monster_sprite="goblin",
        monster_color="#eab308",
        monster_attack="Duplication Pierce",
        monster_quote="My duplicate shards have vanished into the ether!",
        description="Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. Return the number of unique elements `k`. The first `k` elements of `nums` should hold the unique elements.",
        examples=[
            {"input": "nums = [1,1,2]", "output": "2", "explanation": "Unique elements are [1, 2]"},
            {"input": "nums = [0,0,1,1,1,2,2,3,3,4]", "output": "5", "explanation": "Unique elements are [0, 1, 2, 3, 4]"}
        ],
        constraints=["1 <= len(nums) <= 3 * 10^4", "-100 <= nums[i] <= 100", "nums is sorted in non-decreasing order"],
        function_name="removeDuplicates",
        starter_code="def removeDuplicates(nums: list[int]) -> int:\n    # Return the count of unique elements\n    pass\n",
        solution_code="def removeDuplicates(nums: list[int]) -> int:\n    if not nums:\n        return 0\n    write = 1\n    for read in range(1, len(nums)):\n        if nums[read] != nums[read - 1]:\n            nums[write] = nums[read]\n            write += 1\n    return write\n",
        test_cases=[
            {"input": [[1, 1, 2]], "expected": 2},
            {"input": [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]], "expected": 5},
            {"input": [[1]], "expected": 1},
            {"input": [[1, 2, 3]], "expected": 3},
            {"input": [[5, 5, 5, 5]], "expected": 1},
        ],
        hints=["Use two pointers: one write pointer for unique placements, one read pointer scanning ahead."],
        leetcode_id=26,
    ))

    # 2. Implement Queue using Stacks
    problems.append(make_problem(
        pid="ds-e-queue-using-stacks",
        title="Queue using Stacks Simulator",
        wing_id="data-structures",
        floor=102,
        difficulty="easy",
        visualizerType="stack",
        monster_name="Dual-Stack Sentinel",
        monster_title="Guardian of Reversible Chambers",
        monster_sprite="golem",
        monster_color="#64748b",
        monster_attack="Reversal Slam",
        monster_quote="My in-stack and out-stack have collapsed into harmony!",
        description="Simulate a FIFO queue using two LIFO stacks. You are given a list of commands: `[\"push\", x]`, `[\"pop\"]`, `[\"peek\"]`, and `[\"empty\"]`. Return an array of results corresponding to queries that produce an output (`pop`, `peek`, `empty`).",
        examples=[
            {"input": "commands = [[\"push\", 1], [\"push\", 2], [\"peek\"], [\"pop\"], [\"empty\"]]", "output": "[1, 1, False]"}
        ],
        constraints=["1 <= len(commands) <= 100", "Commands are valid queue operations"],
        function_name="simulateQueue",
        starter_code="def simulateQueue(commands: list) -> list:\n    # Return outputs for pop, peek, empty\n    pass\n",
        solution_code="def simulateQueue(commands: list) -> list:\n    in_stack = []\n    out_stack = []\n    results = []\n    for cmd in commands:\n        op = cmd[0]\n        if op == 'push':\n            in_stack.append(cmd[1])\n        elif op == 'pop':\n            if not out_stack:\n                while in_stack:\n                    out_stack.append(in_stack.pop())\n            results.append(out_stack.pop())\n        elif op == 'peek':\n            if not out_stack:\n                while in_stack:\n                    out_stack.append(in_stack.pop())\n            results.append(out_stack[-1])\n        elif op == 'empty':\n            results.append(len(in_stack) == 0 and len(out_stack) == 0)\n    return results\n",
        test_cases=[
            {"input": [[["push", 1], ["push", 2], ["peek"], ["pop"], ["empty"]]], "expected": [1, 1, False]},
            {"input": [[["push", 5], ["pop"], ["empty"]]], "expected": [5, True]},
            {"input": [[["push", 10], ["push", 20], ["push", 30], ["pop"], ["peek"]]], "expected": [10, 20]},
            {"input": [[["empty"], ["push", 9], ["empty"]]], "expected": [True, False]},
        ],
        hints=["Use two stacks: push onto the inbox stack; pop from the outbox stack, transferring elements when outbox is empty."],
        leetcode_id=232,
    ))

    # 3. Min Stack Operations
    problems.append(make_problem(
        pid="ds-e-min-stack",
        title="Min Stack Trace",
        wing_id="data-structures",
        floor=103,
        difficulty="easy",
        visualizerType="stack",
        monster_name="Depression Wight",
        monster_title="Keeper of Absolute Minimums",
        monster_sprite="wraith",
        monster_color="#8b5cf6",
        monster_attack="Abyssal Drain",
        monster_quote="My minimal values were tracked at every elevation!",
        description="Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. Given operations `[\"push\", x]`, `[\"pop\"]`, `[\"top\"]`, `[\"getMin\"]`, return the outputs of `top` and `getMin`.",
        examples=[
            {"input": "commands = [[\"push\", -2], [\"push\", 0], [\"push\", -3], [\"getMin\"], [\"pop\"], [\"top\"], [\"getMin\"]]", "output": "[-3, 0, -2]"}
        ],
        constraints=["1 <= len(commands) <= 200", "Operations will be valid"],
        function_name="minStackTrace",
        starter_code="def minStackTrace(commands: list) -> list:\n    pass\n",
        solution_code="def minStackTrace(commands: list) -> list:\n    stack = []\n    min_stack = []\n    out = []\n    for c in commands:\n        op = c[0]\n        if op == 'push':\n            val = c[1]\n            stack.append(val)\n            if not min_stack or val <= min_stack[-1]:\n                min_stack.append(val)\n        elif op == 'pop':\n            val = stack.pop()\n            if val == min_stack[-1]:\n                min_stack.pop()\n        elif op == 'top':\n            out.append(stack[-1])\n        elif op == 'getMin':\n            out.append(min_stack[-1])\n    return out\n",
        test_cases=[
            {"input": [[["push", -2], ["push", 0], ["push", -3], ["getMin"], ["pop"], ["top"], ["getMin"]]], "expected": [-3, 0, -2]},
            {"input": [[["push", 1], ["push", 2], ["getMin"]]], "expected": [1]},
            {"input": [[["push", 2], ["push", 0], ["push", 3], ["push", 0], ["getMin"], ["pop"], ["getMin"], ["pop"], ["getMin"]]], "expected": [0, 0, 0]},
        ],
        hints=["Store paired minimums or maintain an auxiliary stack storing the running minimum."],
        leetcode_id=155,
    ))

    # 4. Middle of the Linked List
    problems.append(make_problem(
        pid="ds-e-middle-linked-list",
        title="Middle of Linked List Values",
        wing_id="data-structures",
        floor=104,
        difficulty="easy",
        visualizerType="array",
        monster_name="Bifurcating Serpent",
        monster_title="Splitter of Linked Arteries",
        monster_sprite="slime",
        monster_color="#10b981",
        monster_attack="Midway Constrict",
        monster_quote="The fast and slow runners have rendezvoused at my core!",
        description="Given the head values of a singly linked list as an array `values`, return the values from the middle node to the end of the list. If there are two middle nodes, return the second middle node onwards.",
        examples=[
            {"input": "values = [1,2,3,4,5]", "output": "[3,4,5]"},
            {"input": "values = [1,2,3,4,5,6]", "output": "[4,5,6]"}
        ],
        constraints=["1 <= len(values) <= 1000", "0 <= values[i] <= 1000"],
        function_name="middleNodeValues",
        starter_code="def middleNodeValues(values: list[int]) -> list[int]:\n    pass\n",
        solution_code="def middleNodeValues(values: list[int]) -> list[int]:\n    # Simulate slow and fast pointer: fast moves 2, slow moves 1\n    slow = 0\n    fast = 0\n    while fast < len(values) and fast + 1 < len(values):\n        slow += 1\n        fast += 2\n    return values[slow:]\n",
        test_cases=[
            {"input": [[1, 2, 3, 4, 5]], "expected": [3, 4, 5]},
            {"input": [[1, 2, 3, 4, 5, 6]], "expected": [4, 5, 6]},
            {"input": [[42]], "expected": [42]},
            {"input": [[1, 2]], "expected": [2]},
        ],
        hints=["Use two pointers: fast moves two steps while slow moves one step."],
        leetcode_id=876,
    ))

    # 5. Reverse Linked List Sequence
    problems.append(make_problem(
        pid="ds-e-reverse-linked-list",
        title="Reverse Linked Sequence",
        wing_id="data-structures",
        floor=105,
        difficulty="easy",
        visualizerType="array",
        monster_name="Chronos Shade",
        monster_title="Inverter of Past Pointers",
        monster_sprite="wraith",
        monster_color="#38bdf8",
        monster_attack="Temporal Flip",
        monster_quote="All my forward references have flipped to the past!",
        description="Given an array representing node values in a singly linked list, return the array of values in reverse order simulating pointer reversals.",
        examples=[
            {"input": "head = [1,2,3,4,5]", "output": "[5,4,3,2,1]"},
            {"input": "head = [1,2]", "output": "[2,1]"}
        ],
        constraints=["0 <= len(head) <= 5000", "-5000 <= head[i] <= 5000"],
        function_name="reverseList",
        starter_code="def reverseList(head: list[int]) -> list[int]:\n    pass\n",
        solution_code="def reverseList(head: list[int]) -> list[int]:\n    prev = []\n    for val in reversed(head):\n        prev.append(val)\n    return prev\n",
        test_cases=[
            {"input": [[1, 2, 3, 4, 5]], "expected": [5, 4, 3, 2, 1]},
            {"input": [[1, 2]], "expected": [2, 1]},
            {"input": [[]], "expected": []},
            {"input": [[99]], "expected": [99]},
        ],
        hints=["In a true linked list, maintain prev, curr, and next pointers."],
        leetcode_id=206,
    ))

    # 6. Palindrome Linked List
    problems.append(make_problem(
        pid="ds-e-palindrome-linked-list",
        title="Palindrome Sequence Check",
        wing_id="data-structures",
        floor=106,
        difficulty="easy",
        visualizerType="array",
        monster_name="Mirror Drake",
        monster_title="Reflector of Symmetric Sequences",
        monster_sprite="dragon",
        monster_color="#ec4899",
        monster_attack="Reflection Flare",
        monster_quote="My symmetry was broken by your sharp eye!",
        description="Given an array `head` of values representing a linked list, return `True` if the sequence is a palindrome, or `False` otherwise.",
        examples=[
            {"input": "head = [1,2,2,1]", "output": "True"},
            {"input": "head = [1,2]", "output": "False"}
        ],
        constraints=["1 <= len(head) <= 10^5", "0 <= head[i] <= 9"],
        function_name="isPalindromeList",
        starter_code="def isPalindromeList(head: list[int]) -> bool:\n    pass\n",
        solution_code="def isPalindromeList(head: list[int]) -> bool:\n    left = 0\n    right = len(head) - 1\n    while left < right:\n        if head[left] != head[right]:\n            return False\n        left += 1\n        right -= 1\n    return True\n",
        test_cases=[
            {"input": [[1, 2, 2, 1]], "expected": True},
            {"input": [[1, 2]], "expected": False},
            {"input": [[1]], "expected": True},
            {"input": [[1, 2, 3, 2, 1]], "expected": True},
            {"input": [[1, 2, 3, 4, 1]], "expected": False},
        ],
        hints=["Find the middle with fast/slow pointers, reverse the second half, and compare with the first."],
        leetcode_id=234,
    ))

    # 7. Intersection of Two Arrays
    problems.append(make_problem(
        pid="ds-e-intersection-arrays",
        title="Unique Array Intersection",
        wing_id="data-structures",
        floor=107,
        difficulty="easy",
        visualizerType="array",
        monster_name="Venn Fiend",
        monster_title="Devourer of Set Complements",
        monster_sprite="demon",
        monster_color="#f97316",
        monster_attack="Set Overlap Claws",
        monster_quote="The common intersection has stripped my shield!",
        description="Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must be unique and returned in sorted order.",
        examples=[
            {"input": "nums1 = [1,2,2,1], nums2 = [2,2]", "output": "[2]"},
            {"input": "nums1 = [4,9,5], nums2 = [9,4,9,8,4]", "output": "[4,9]"}
        ],
        constraints=["1 <= len(nums1), len(nums2) <= 1000", "0 <= nums1[i], nums2[i] <= 1000"],
        function_name="intersection",
        starter_code="def intersection(nums1: list[int], nums2: list[int]) -> list[int]:\n    pass\n",
        solution_code="def intersection(nums1: list[int], nums2: list[int]) -> list[int]:\n    return sorted(list(set(nums1) & set(nums2)))\n",
        test_cases=[
            {"input": [[1, 2, 2, 1], [2, 2]], "expected": [2]},
            {"input": [[4, 9, 5], [9, 4, 9, 8, 4]], "expected": [4, 9]},
            {"input": [[1, 2, 3], [4, 5, 6]], "expected": []},
            {"input": [[7, 7, 7], [7]], "expected": [7]},
        ],
        hints=["Convert arrays to sets and compute the set intersection."],
        leetcode_id=349,
    ))

    # 8. Majority Element
    problems.append(make_problem(
        pid="ds-e-majority-element",
        title="Dominant Rune Search",
        wing_id="data-structures",
        floor=108,
        difficulty="easy",
        visualizerType="array",
        monster_name="Boyer-Moore Golem",
        monster_title="Candidate Voter of the Colosseum",
        monster_sprite="golem",
        monster_color="#a855f7",
        monster_attack="Majority Quake",
        monster_quote="The majority candidate has overwhelmed my tally!",
        description="Given an array `nums` of size `n`, return the majority element. The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists.",
        examples=[
            {"input": "nums = [3,2,3]", "output": "3"},
            {"input": "nums = [2,2,1,1,1,2,2]", "output": "2"}
        ],
        constraints=["1 <= len(nums) <= 5 * 10^4", "-10^9 <= nums[i] <= 10^9"],
        function_name="majorityElement",
        starter_code="def majorityElement(nums: list[int]) -> int:\n    pass\n",
        solution_code="def majorityElement(nums: list[int]) -> int:\n    candidate = None\n    count = 0\n    for num in nums:\n        if count == 0:\n            candidate = num\n        count += (1 if num == candidate else -1)\n    return candidate\n",
        test_cases=[
            {"input": [[3, 2, 3]], "expected": 3},
            {"input": [[2, 2, 1, 1, 1, 2, 2]], "expected": 2},
            {"input": [[1]], "expected": 1},
            {"input": [[6, 6, 6, 7, 7]], "expected": 6},
        ],
        hints=["Boyer-Moore Voting Algorithm achieves O(n) time and O(1) space."],
        leetcode_id=169,
    ))

    # 9. Contains Duplicate II
    problems.append(make_problem(
        pid="ds-e-contains-duplicate-ii",
        title="Proximity Echo Search",
        wing_id="data-structures",
        floor=109,
        difficulty="easy",
        visualizerType="array",
        monster_name="Echo Lurker",
        monster_title="Stalker of Nearby Echoes",
        monster_sprite="slime",
        monster_color="#06b6d4",
        monster_attack="Echo Wave",
        monster_quote="You tracked two matching echoes within distance k!",
        description="Given an integer array `nums` and an integer `k`, return `True` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.",
        examples=[
            {"input": "nums = [1,2,3,1], k = 3", "output": "True"},
            {"input": "nums = [1,0,1,1], k = 1", "output": "True"},
            {"input": "nums = [1,2,3,1,2,3], k = 2", "output": "False"}
        ],
        constraints=["1 <= len(nums) <= 10^5", "0 <= k <= 10^5"],
        function_name="containsNearbyDuplicate",
        starter_code="def containsNearbyDuplicate(nums: list[int], k: int) -> bool:\n    pass\n",
        solution_code="def containsNearbyDuplicate(nums: list[int], k: int) -> bool:\n    lookup = {}\n    for i, num in enumerate(nums):\n        if num in lookup and i - lookup[num] <= k:\n            return True\n        lookup[num] = i\n    return False\n",
        test_cases=[
            {"input": [[1, 2, 3, 1], 3], "expected": True},
            {"input": [[1, 0, 1, 1], 1], "expected": True},
            {"input": [[1, 2, 3, 1, 2, 3], 2], "expected": False},
            {"input": [[1, 2], 0], "expected": False},
        ],
        hints=["Use a hash map to keep track of the most recent index seen for each element."],
        leetcode_id=219,
    ))

    # 10. Maximum Depth of Binary Tree Sequence
    problems.append(make_problem(
        pid="ds-e-max-depth-binary-tree",
        title="Tree Depth Surveyor",
        wing_id="data-structures",
        floor=110,
        difficulty="easy",
        visualizerType="tree",
        monster_name="Abyssal Canopy",
        monster_title="Arbiter of Branching Heights",
        monster_sprite="lich",
        monster_color="#84cc16",
        monster_attack="Branch Spikes",
        monster_quote="My deepest roots have been measured accurately!",
        description="Given a binary tree represented as a level-order array where `None` indicates empty leaves, return its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.",
        examples=[
            {"input": "tree = [3,9,20,None,None,15,7]", "output": "3"},
            {"input": "tree = [1,None,2]", "output": "2"}
        ],
        constraints=["0 <= len(tree) <= 10^4"],
        function_name="maxTreeDepth",
        starter_code="def maxTreeDepth(tree: list) -> int:\n    pass\n",
        solution_code="def maxTreeDepth(tree: list) -> int:\n    if not tree or tree[0] is None:\n        return 0\n    # Convert level-order array into depth\n    # Node at index i has children 2*i + 1 and 2*i + 2\n    def dfs(idx):\n        if idx >= len(tree) or tree[idx] is None:\n            return 0\n        return 1 + max(dfs(2 * idx + 1), dfs(2 * idx + 2))\n    return dfs(0)\n",
        test_cases=[
            {"input": [[3, 9, 20, None, None, 15, 7]], "expected": 3},
            {"input": [[1, None, 2]], "expected": 2},
            {"input": [[]], "expected": 0},
            {"input": [[1]], "expected": 1},
        ],
        hints=["Depth is 1 + max(depth(left), depth(right))."],
        leetcode_id=104,
    ))

    return problems
