"""
Data Structures Medium Problems Part 4 (Problems 41 to 60).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_data_structures_medium_part4():
    problems = []

    # 41. Maximum Width Ramp
    problems.append(make_problem(
        pid="ds-m-max-width-ramp", title="Maximum Width Ramp",
        wing_id="data-structures", floor=151, difficulty="medium", visualizer_type="stack",
        monster_name="Incline Behemoth", monster_title="Ascender of Stagnant Slopes",
        monster_sprite="golem", monster_color="#6366f1", monster_attack="Slope Bash",
        monster_quote="A decreasing index stack tracked the widest possible ramp!",
        description="A ramp in an integer array `nums` is a pair `(i, j)` for which `i < j` and `nums[i] <= nums[j]`. The width of such a ramp is `j - i`. Given an integer array `nums`, return the maximum width of a ramp in `nums`. If there is no ramp, return `0`.",
        examples=[{"input": "nums = [6,0,8,2,1,5]", "output": "4"}, {"input": "nums = [9,8,1,0,1,9,4,0,4,1]", "output": "7"}],
        constraints=["2 <= len(nums) <= 5 * 10^4", "0 <= nums[i] <= 5 * 10^4"],
        function_name="maxWidthRamp",
        starter_code="def maxWidthRamp(nums: list[int]) -> int:\n    pass\n",
        solution_code="def maxWidthRamp(nums: list[int]) -> int:\n    stack = []\n    for i, n in enumerate(nums):\n        if not stack or nums[stack[-1]] > n:\n            stack.append(i)\n    res = 0\n    for j in range(len(nums) - 1, -1, -1):\n        while stack and nums[stack[-1]] <= nums[j]:\n            res = max(res, j - stack.pop())\n    return res\n",
        test_cases=[{"input": [[6, 0, 8, 2, 1, 5]], "expected": 4}, {"input": [[9, 8, 1, 0, 1, 9, 4, 0, 4, 1]], "expected": 7}, {"input": [[5, 4, 3, 2, 1]], "expected": 0}, {"input": [[1, 2]], "expected": 1}],
        hints=["Push decreasing indices onto a stack. Iterate from right to left popping when condition holds."],
        leetcode_id=962
    ))

    # 42. Car Pooling
    problems.append(make_problem(
        pid="ds-m-car-pooling", title="Car Pooling Capacity",
        wing_id="data-structures", floor=152, difficulty="medium", visualizer_type="array",
        monster_name="Chariot Wyvern", monster_title="Weigher of Passenger Manifests",
        monster_sprite="dragon", monster_color="#eab308", monster_attack="Overload Dive",
        monster_quote="The sweep-line difference array caught all capacity overshoots!",
        description="There is a car with `capacity` empty seats. The vehicle only drives east. You are given the integer `capacity` and an array `trips` where `trips[i] = [numPassengers, from, to]` indicates that the `i-th` trip has `numPassengers` passengers and the locations are `from` and `to`. Return `True` if it is possible to pick up and drop off all passengers for all the given trips, or `False` otherwise.",
        examples=[{"input": "trips = [[2,1,5],[3,3,7]], capacity = 4", "output": "False"}, {"input": "trips = [[2,1,5],[3,3,7]], capacity = 5", "output": "True"}, {"input": "trips = [[2,1,5],[3,5,7]], capacity = 3", "output": "True"}],
        constraints=["1 <= len(trips) <= 1000", "trips[i].length == 3", "1 <= capacity <= 10^5"],
        function_name="carPooling",
        starter_code="def carPooling(trips: list[list[int]], capacity: int) -> bool:\n    pass\n",
        solution_code="def carPooling(trips: list[list[int]], capacity: int) -> bool:\n    diff = [0] * 1001\n    for num, start, end in trips:\n        diff[start] += num\n        diff[end] -= num\n    curr = 0\n    for passengers in diff:\n        curr += passengers\n        if curr > capacity:\n            return False\n    return True\n",
        test_cases=[{"input": [[[2, 1, 5], [3, 3, 7]], 4], "expected": False}, {"input": [[[2, 1, 5], [3, 3, 7]], 5], "expected": True}, {"input": [[[2, 1, 5], [3, 5, 7]], 3], "expected": True}],
        hints=["Use a difference array / timeline array to track passenger deltas at pickup and dropoff points."],
        leetcode_id=1094
    ))

    # 43. Corporate Flight Bookings
    problems.append(make_problem(
        pid="ds-m-corp-flight-bookings", title="Flight Booking Differential",
        wing_id="data-structures", floor=153, difficulty="medium", visualizer_type="array",
        monster_name="Aero Drake", monster_title="Auditor of Continuous Seat Reservations",
        monster_sprite="dragon", monster_color="#38bdf8", monster_attack="Turbulence Gust",
        monster_quote="Prefix sum prefix reconstruction totaled seat counts in O(n)!",
        description="There are `n` flights that are labeled from `1` to `n`. You are given an array of flight bookings `bookings`, where `bookings[i] = [first, last, seats]` represents a booking for flights `first` through `last` of `seats` seats reserved for each flight in the range. Return an array `answer` of length `n`, where `answer[i]` is the total number of seats reserved for flight `i + 1`.",
        examples=[{"input": "bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5", "output": "[10,55,45,25,25]"}, {"input": "bookings = [[1,2,10],[2,2,15]], n = 2", "output": "[10,25]"}],
        constraints=["1 <= n <= 2 * 10^4", "1 <= len(bookings) <= 2 * 10^4"],
        function_name="corpFlightBookings",
        starter_code="def corpFlightBookings(bookings: list[list[int]], n: int) -> list[int]:\n    pass\n",
        solution_code="def corpFlightBookings(bookings: list[list[int]], n: int) -> list[int]:\n    diff = [0] * (n + 1)\n    for first, last, seats in bookings:\n        diff[first - 1] += seats\n        diff[last] -= seats\n    res = [0] * n\n    curr = 0\n    for i in range(n):\n        curr += diff[i]\n        res[i] = curr\n    return res\n",
        test_cases=[{"input": [[[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5], "expected": [10, 55, 45, 25, 25]}, {"input": [[[1, 2, 10], [2, 2, 15]], 2], "expected": [10, 25]}],
        hints=["Apply range update O(1) by marking +seats at start and -seats at end + 1."],
        leetcode_id=1109
    ))

    # 44. My Calendar I
    problems.append(make_problem(
        pid="ds-m-book-calendar", title="My Calendar I Single Booking",
        wing_id="data-structures", floor=154, difficulty="medium", visualizer_type="array",
        monster_name="Temporal Archon", monster_title="Gatekeeper of Non-Overlapping Epochs",
        monster_sprite="lich", monster_color="#8b5cf6", monster_attack="Time Paradox",
        monster_quote="Your interval intersection test prevented double booking!",
        description="You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking. Given a list of booking intervals `[start, end)`, return a list of booleans indicating whether each booking was successfully scheduled.",
        examples=[{"input": "intervals = [[10,20],[15,25],[20,30]]", "output": "[True,False,True]"}],
        constraints=["1 <= len(intervals) <= 1000", "0 <= start < end <= 10^9"],
        function_name="bookCalendar",
        starter_code="def bookCalendar(intervals: list[list[int]]) -> list[bool]:\n    pass\n",
        solution_code="def bookCalendar(intervals: list[list[int]]) -> list[bool]:\n    booked = []\n    res = []\n    for s, e in intervals:\n        conflict = False\n        for bs, be in booked:\n            if max(s, bs) < min(e, be):\n                conflict = True\n                break\n        if not conflict:\n            booked.append((s, e))\n            res.append(True)\n        else:\n            res.append(False)\n    return res\n",
        test_cases=[{"input": [[[10, 20], [15, 25], [20, 30]]], "expected": [True, False, True]}, {"input": [[[47, 50], [33, 41], [39, 45], [33, 42], [25, 32], [26, 35]]], "expected": [True, True, False, False, True, False]}],
        hints=["Two intervals [s1, e1) and [s2, e2) overlap if and only if max(s1, s2) < min(e1, e2)."],
        leetcode_id=729
    ))

    # 45. Find Peak Element
    problems.append(make_problem(
        pid="ds-m-find-peak-element", title="Find Peak Element",
        wing_id="data-structures", floor=155, difficulty="medium", visualizer_type="array",
        monster_name="Mountain Basilisk", monster_title="Dweller of Isolated Summits",
        monster_sprite="slime", monster_color="#10b981", monster_attack="Apex Venom",
        monster_quote="Binary search ascended directly to an apex peak in O(log n)!",
        description="A peak element is an element that is strictly greater than its neighbors. Given a 0-indexed integer array `nums`, find a peak element, and return its index. You may imagine that `nums[-1] = nums[n] = -∞`.",
        examples=[{"input": "nums = [1,2,3,1]", "output": "2"}, {"input": "nums = [1,2,1,3,5,6,4]", "output": "5"}],
        constraints=["1 <= len(nums) <= 1000", "-2^31 <= nums[i] <= 2^31 - 1"],
        function_name="findPeakElement",
        starter_code="def findPeakElement(nums: list[int]) -> int:\n    pass\n",
        solution_code="def findPeakElement(nums: list[int]) -> int:\n    left, right = 0, len(nums) - 1\n    while left < right:\n        mid = (left + right) // 2\n        if nums[mid] > nums[mid + 1]:\n            right = mid\n        else:\n            left = mid + 1\n    return left\n",
        test_cases=[{"input": [[1, 2, 3, 1]], "expected": 2}, {"input": [[1]], "expected": 0}, {"input": [[1, 2]], "expected": 1}],
        hints=["If nums[mid] < nums[mid + 1], a peak must exist to the right."],
        leetcode_id=162
    ))

    # 46. Kth Largest Element in an Array
    problems.append(make_problem(
        pid="ds-m-find-kth-largest", title="Kth Largest Element",
        wing_id="data-structures", floor=156, difficulty="medium", visualizer_type="array",
        monster_name="Colossus of Ranks", monster_title="Keeper of the Kth Highest Tier",
        monster_sprite="golem", monster_color="#f59e0b", monster_attack="Rank Stomp",
        monster_quote="A min-heap of size k held the exact threshold!",
        description="Given an integer array `nums` and an integer `k`, return the `k-th` largest element in the array.",
        examples=[{"input": "nums = [3,2,1,5,6,4], k = 2", "output": "5"}, {"input": "nums = [3,2,3,1,2,4,5,5,6], k = 4", "output": "4"}],
        constraints=["1 <= k <= len(nums) <= 10^5", "-10^4 <= nums[i] <= 10^4"],
        function_name="findKthLargest",
        starter_code="def findKthLargest(nums: list[int], k: int) -> int:\n    pass\n",
        solution_code="def findKthLargest(nums: list[int], k: int) -> int:\n    import heapq\n    min_heap = []\n    for n in nums:\n        heapq.heappush(min_heap, n)\n        if len(min_heap) > k:\n            heapq.heappop(min_heap)\n    return min_heap[0]\n",
        test_cases=[{"input": [[3, 2, 1, 5, 6, 4], 2], "expected": 5}, {"input": [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4], "expected": 4}, {"input": [[1], 1], "expected": 1}],
        hints=["Maintain a min-heap of size k, pushing every element and evicting when size > k."],
        leetcode_id=215
    ))

    # 47. Top K Frequent Words
    problems.append(make_problem(
        pid="ds-m-top-k-frequent-words", title="Top K Frequent Words",
        wing_id="data-structures", floor=157, difficulty="medium", visualizer_type="array",
        monster_name="Lexicon Shade", monster_title="Sorter of Lexical Frequencies",
        monster_sprite="wraith", monster_color="#a855f7", monster_attack="Lexical Curse",
        monster_quote="Ties were broken alphabetically with custom comparator sorting!",
        description="Given an array of strings `words` and an integer `k`, return the `k` most frequent strings sorted by frequency from highest to lowest, breaking ties by lower alphabetical order.",
        examples=[{"input": "words = [\"i\",\"love\",\"leetcode\",\"i\",\"love\",\"coding\"], k = 2", "output": "[\"i\",\"love\"]"}, {"input": "words = [\"the\",\"day\",\"is\",\"sunny\",\"the\",\"the\",\"the\",\"sunny\",\"is\",\"is\"], k = 4", "output": "[\"the\",\"is\",\"sunny\",\"day\"]"}],
        constraints=["1 <= len(words) <= 500", "1 <= k <= unique words"],
        function_name="topKFrequentWords",
        starter_code="def topKFrequentWords(words: list[str], k: int) -> list[str]:\n    pass\n",
        solution_code="def topKFrequentWords(words: list[str], k: int) -> list[str]:\n    from collections import Counter\n    counts = Counter(words)\n    sorted_words = sorted(counts.keys(), key=lambda w: (-counts[w], w))\n    return sorted_words[:k]\n",
        test_cases=[{"input": [["i", "love", "leetcode", "i", "love", "coding"], 2], "expected": ["i", "love"]}, {"input": [["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4], "expected": ["the", "is", "sunny", "day"]}],
        hints=["Count words with Counter, then sort by key (-count, word)."],
        leetcode_id=692
    ))

    # 48. Sort Colors (Dutch National Flag)
    problems.append(make_problem(
        pid="ds-m-sort-colors", title="Sort Colors (Dutch National Flag)",
        wing_id="data-structures", floor=158, difficulty="medium", visualizer_type="array",
        monster_name="Tricolor Sentinel", monster_title="Partition Master of Three Hues",
        monster_sprite="golem", monster_color="#ef4444", monster_attack="Tricolor Beam",
        monster_quote="Three pointers partitioned 0s, 1s, and 2s in one pass!",
        description="Given an array `nums` with `n` objects colored red, white, or blue (represented as 0, 1, and 2), sort them in-place so that objects of the same color are adjacent in the order 0, 1, and 2. Return the sorted array.",
        examples=[{"input": "nums = [2,0,2,1,1,0]", "output": "[0,0,1,1,2,2]"}, {"input": "nums = [2,0,1]", "output": "[0,1,2]"}],
        constraints=["n == len(nums)", "1 <= n <= 300", "nums[i] is 0, 1, or 2"],
        function_name="sortColors",
        starter_code="def sortColors(nums: list[int]) -> list[int]:\n    pass\n",
        solution_code="def sortColors(nums: list[int]) -> list[int]:\n    low, mid, high = 0, 0, len(nums) - 1\n    while mid <= high:\n        if nums[mid] == 0:\n            nums[low], nums[mid] = nums[mid], nums[low]\n            low += 1\n            mid += 1\n        elif nums[mid] == 1:\n            mid += 1\n        else:\n            nums[mid], nums[high] = nums[high], nums[mid]\n            high -= 1\n    return nums\n",
        test_cases=[{"input": [[2, 0, 2, 1, 1, 0]], "expected": [0, 0, 1, 1, 2, 2]}, {"input": [[2, 0, 1]], "expected": [0, 1, 2]}, {"input": [[0]], "expected": [0]}],
        hints=["Use Dijkstra's 3-way partition: low tracks 0s, mid scans, high tracks 2s."],
        leetcode_id=75
    ))

    # 49. Wiggle Sort Sequence
    problems.append(make_problem(
        pid="ds-m-wiggle-sort", title="Wiggle Sort Sequence",
        wing_id="data-structures", floor=159, difficulty="medium", visualizer_type="array",
        monster_name="Wave Serpent", monster_title="Oscillator of Alternating Amplitudes",
        monster_sprite="slime", monster_color="#06b6d4", monster_attack="Wave Ripple",
        monster_quote="Every odd index was guaranteed greater than adjacent evens!",
        description="Given an integer array `nums`, reorder it in-place such that `nums[0] <= nums[1] >= nums[2] <= nums[3]...`. Return the reordered array.",
        examples=[{"input": "nums = [3,5,2,1,6,4]", "output": "[3,5,1,6,2,4]"}],
        constraints=["1 <= len(nums) <= 5 * 10^4", "0 <= nums[i] <= 10^4"],
        function_name="wiggleSort",
        starter_code="def wiggleSort(nums: list[int]) -> list[int]:\n    pass\n",
        solution_code="def wiggleSort(nums: list[int]) -> list[int]:\n    for i in range(len(nums) - 1):\n        if (i % 2 == 0 and nums[i] > nums[i + 1]) or (i % 2 == 1 and nums[i] < nums[i + 1]):\n            nums[i], nums[i + 1] = nums[i + 1], nums[i]\n    return nums\n",
        test_cases=[{"input": [[3, 5, 2, 1, 6, 4]], "expected": [3, 5, 1, 6, 2, 4]}, {"input": [[1, 2, 3]], "expected": [1, 3, 2]}, {"input": [[1]], "expected": [1]}],
        hints=["Single pass: swap adjacent elements if condition nums[i] <= nums[i+1] is violated."],
        leetcode_id=280
    ))

    # 50. Custom Sort String
    problems.append(make_problem(
        pid="ds-m-custom-sort-string", title="Custom Sort String",
        wing_id="data-structures", floor=160, difficulty="medium", visualizer_type="array",
        monster_name="Alphabet Demon", monster_title="Dictator of Arbitrary Alphabets",
        monster_sprite="demon", monster_color="#ec4899", monster_attack="Alphabet Whip",
        monster_quote="Characters conformed precisely to the custom permutation order!",
        description="You are given two strings `order` and `s`. All the characters of `order` are unique and were sorted in some custom order previously. Permute the characters of `s` so that they match the order that `order` was sorted.",
        examples=[{"input": "order = \"cba\", s = \"abcd\"", "output": "\"cbad\""}, {"input": "order = \"cbafg\", s = \"abcd\"", "output": "\"cbad\""}],
        constraints=["1 <= len(order) <= 26", "1 <= len(s) <= 200"],
        function_name="customSortString",
        starter_code="def customSortString(order: str, s: str) -> str:\n    pass\n",
        solution_code="def customSortString(order: str, s: str) -> str:\n    rank = {ch: i for i, ch in enumerate(order)}\n    return ''.join(sorted(s, key=lambda ch: rank.get(ch, 100)))\n",
        test_cases=[{"input": ["cba", "abcd"], "expected": "cbad"}, {"input": ["cbafg", "abcd"], "expected": "cbad"}, {"input": ["kqep", "pekeq"], "expected": "kqeep"}],
        hints=["Sort characters using their index in the order string as the key."],
        leetcode_id=791
    ))

    # 51. Reorder List (Fold In Half)
    problems.append(make_problem(
        pid="ds-m-reorder-list", title="Fold Reordered List",
        wing_id="data-structures", floor=161, difficulty="medium", visualizer_type="array",
        monster_name="Interleaving Phantom", monster_title="Weaver of Folded Head-Tails",
        monster_sprite="wraith", monster_color="#14b8a6", monster_attack="Fold Bind",
        monster_quote="Interleaving the first half and reversed second half succeeded!",
        description="You are given an array of node values representing a singly linked-list: `L0 → L1 → … → Ln - 1 → Ln`. Reorder the list to be: `L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …`. Return the reordered array of values.",
        examples=[{"input": "head = [1,2,3,4]", "output": "[1,4,2,3]"}, {"input": "head = [1,2,3,4,5]", "output": "[1,5,2,4,3]"}],
        constraints=["1 <= len(head) <= 5 * 10^4"],
        function_name="reorderList",
        starter_code="def reorderList(head: list[int]) -> list[int]:\n    pass\n",
        solution_code="def reorderList(head: list[int]) -> list[int]:\n    if len(head) <= 2: return head\n    left, right = 0, len(head) - 1\n    res = []\n    while left <= right:\n        if left == right:\n            res.append(head[left])\n            break\n        res.append(head[left])\n        res.append(head[right])\n        left += 1\n        right -= 1\n    return res\n",
        test_cases=[{"input": [[1, 2, 3, 4]], "expected": [1, 4, 2, 3]}, {"input": [[1, 2, 3, 4, 5]], "expected": [1, 5, 2, 4, 3]}, {"input": [[1]], "expected": [1]}],
        hints=["Find middle, reverse the second half, and interleave nodes."],
        leetcode_id=143
    ))

    # 52. Swap Nodes in Pairs
    problems.append(make_problem(
        pid="ds-m-swap-pairs", title="Swap List Elements in Pairs",
        wing_id="data-structures", floor=162, difficulty="medium", visualizer_type="array",
        monster_name="Pair Twister", monster_title="Inverter of Adjacent Duos",
        monster_sprite="slime", monster_color="#84cc16", monster_attack="Pair Vortex",
        monster_quote="Every adjacent pair was exchanged without disturbing the chain!",
        description="Given an array `head` representing values of a linked list, swap every two adjacent nodes and return its values.",
        examples=[{"input": "head = [1,2,3,4]", "output": "[2,1,4,3]"}, {"input": "head = []", "output": "[]"}, {"input": "head = [1]", "output": "[1]"}],
        constraints=["0 <= len(head) <= 100"],
        function_name="swapPairs",
        starter_code="def swapPairs(head: list[int]) -> list[int]:\n    pass\n",
        solution_code="def swapPairs(head: list[int]) -> list[int]:\n    res = list(head)\n    for i in range(0, len(res) - 1, 2):\n        res[i], res[i + 1] = res[i + 1], res[i]\n    return res\n",
        test_cases=[{"input": [[1, 2, 3, 4]], "expected": [2, 1, 4, 3]}, {"input": [[]], "expected": []}, {"input": [[1]], "expected": [1]}, {"input": [[1, 2, 3]], "expected": [2, 1, 3]}],
        hints=["Step by 2 and swap elements at indices i and i + 1."],
        leetcode_id=24
    ))

    # 53. Remove Nth Node From End of List
    problems.append(make_problem(
        pid="ds-m-remove-nth-from-end", title="Remove Nth Node From End of List",
        wing_id="data-structures", floor=163, difficulty="medium", visualizer_type="array",
        monster_name="End-Gap Stalker", monster_title="Severer of Tail Offsets",
        monster_sprite="wraith", monster_color="#e11d48", monster_attack="Gap Snip",
        monster_quote="Two pointers separated by gap n severed the exact target node!",
        description="Given the head values of a linked list as an array, remove the `n-th` node from the end of the list and return its values.",
        examples=[{"input": "head = [1,2,3,4,5], n = 2", "output": "[1,2,3,5]"}, {"input": "head = [1], n = 1", "output": "[]"}, {"input": "head = [1,2], n = 1", "output": "[1]"}],
        constraints=["1 <= len(head) <= 30", "1 <= n <= len(head)"],
        function_name="removeNthFromEnd",
        starter_code="def removeNthFromEnd(head: list[int], n: int) -> list[int]:\n    pass\n",
        solution_code="def removeNthFromEnd(head: list[int], n: int) -> list[int]:\n    idx = len(head) - n\n    return head[:idx] + head[idx + 1:]\n",
        test_cases=[{"input": [[1, 2, 3, 4, 5], 2], "expected": [1, 2, 3, 5]}, {"input": [[1], 1], "expected": []}, {"input": [[1, 2], 1], "expected": [1]}],
        hints=["Target index is len(head) - n."],
        leetcode_id=19
    ))

    # 54. Delete Node in a BST
    problems.append(make_problem(
        pid="ds-m-delete-node-bst", title="Delete Node in a BST (Inorder Successor)",
        wing_id="data-structures", floor=164, difficulty="medium", visualizer_type="tree",
        monster_name="BST Pruning Wight", monster_title="Rebalancer of Severed Branches",
        monster_sprite="lich", monster_color="#8b5cf6", monster_attack="Prune Scythe",
        monster_quote="Replacing with the inorder successor preserved the BST property!",
        description="Given an array of integers representing a BST in sorted order (inorder traversal), simulate deleting the node with value `key` and return the remaining BST inorder array.",
        examples=[{"input": "inorder = [2,3,4,5,6,7], key = 3", "output": "[2,4,5,6,7]"}],
        constraints=["1 <= len(inorder) <= 10^4", "inorder is strictly ascending"],
        function_name="deleteNodeBST",
        starter_code="def deleteNodeBST(inorder: list[int], key: int) -> list[int]:\n    pass\n",
        solution_code="def deleteNodeBST(inorder: list[int], key: int) -> list[int]:\n    return [x for x in inorder if x != key]\n",
        test_cases=[{"input": [[2, 3, 4, 5, 6, 7], 3], "expected": [2, 4, 5, 6, 7]}, {"input": [[5], 5], "expected": []}, {"input": [[1, 2, 3], 4], "expected": [1, 2, 3]}],
        hints=["In a BST, deletion replaces a node with 2 children with its inorder successor."],
        leetcode_id=450
    ))

    # 55. Insert into a Binary Search Tree
    problems.append(make_problem(
        pid="ds-m-insert-into-bst", title="Insert Value into BST",
        wing_id="data-structures", floor=165, difficulty="medium", visualizer_type="tree",
        monster_name="Root Scribe", monster_title="Placer of Binary Runes",
        monster_sprite="golem", monster_color="#f59e0b", monster_attack="Rune Press",
        monster_quote="The new element slotted into its sorted BST position!",
        description="Given the sorted values of a BST, insert a new integer `val` into the BST such that the resulting inorder traversal remains strictly sorted.",
        examples=[{"input": "inorder = [1,2,3,5,7], val = 4", "output": "[1,2,3,4,5,7]"}],
        constraints=["0 <= len(inorder) <= 10^4", "all values are unique"],
        function_name="insertIntoBST",
        starter_code="def insertIntoBST(inorder: list[int], val: int) -> list[int]:\n    pass\n",
        solution_code="def insertIntoBST(inorder: list[int], val: int) -> list[int]:\n    import bisect\n    res = list(inorder)\n    bisect.insort(res, val)\n    return res\n",
        test_cases=[{"input": [[1, 2, 3, 5, 7], 4], "expected": [1, 2, 3, 4, 5, 7]}, {"input": [[], 5], "expected": [5]}, {"input": [[10, 20], 5], "expected": [5, 10, 20]}],
        hints=["BST inorder traversal is strictly ascending, so insertion maintains sorted order."],
        leetcode_id=701
    ))

    # 56. Validate Binary Search Tree
    problems.append(make_problem(
        pid="ds-m-is-valid-bst", title="Validate Binary Search Tree Inorder",
        wing_id="data-structures", floor=166, difficulty="medium", visualizer_type="tree",
        monster_name="BST Inquisitor", monster_title="Detector of Illicit Branch Inversions",
        monster_sprite="beholder", monster_color="#ec4899", monster_attack="Ascending Glare",
        monster_quote="Strictly ascending verification proved the tree's BST validity!",
        description="Given an array `values` representing the inorder traversal of a binary tree, return `True` if it represents a valid BST (strictly increasing), or `False` otherwise.",
        examples=[{"input": "values = [1,2,3,4,5]", "output": "True"}, {"input": "values = [5,1,4,None,None,3,6]", "output": "False"}],
        constraints=["1 <= len(values) <= 10^4"],
        function_name="isValidBST",
        starter_code="def isValidBST(values: list[int]) -> bool:\n    pass\n",
        solution_code="def isValidBST(values: list[int]) -> bool:\n    for i in range(1, len(values)):\n        if values[i] <= values[i - 1]:\n            return False\n    return True\n",
        test_cases=[{"input": [[1, 2, 3, 4, 5]], "expected": True}, {"input": [[5, 1, 4]], "expected": False}, {"input": [[1, 1]], "expected": False}, {"input": [[10]], "expected": True}],
        hints=["An inorder traversal of a valid BST must be strictly increasing without duplicates."],
        leetcode_id=98
    ))

    # 57. Binary Tree Level Order Traversal
    problems.append(make_problem(
        pid="ds-m-level-order", title="Binary Tree Level Order Traversal",
        wing_id="data-structures", floor=167, difficulty="medium", visualizer_type="tree",
        monster_name="Stratum Wraith", monster_title="Tiered Collector of Tree Strata",
        monster_sprite="wraith", monster_color="#38bdf8", monster_attack="Stratum Pulse",
        monster_quote="Queue BFS collected every depth layer in order!",
        description="Given a binary tree as a 0-indexed complete binary tree array where node `i` has children `2*i + 1` and `2*i + 2`, return the level order traversal of its nodes' values as a list of lists.",
        examples=[{"input": "tree = [3,9,20,None,None,15,7]", "output": "[[3],[9,20],[15,7]]"}],
        constraints=["0 <= len(tree) <= 2000"],
        function_name="levelOrder",
        starter_code="def levelOrder(tree: list) -> list[list[int]]:\n    pass\n",
        solution_code="def levelOrder(tree: list) -> list[list[int]]:\n    if not tree or tree[0] is None: return []\n    from collections import deque\n    res = []\n    queue = deque([0])\n    while queue:\n        level = []\n        for _ in range(len(queue)):\n            idx = queue.popleft()\n            if idx < len(tree) and tree[idx] is not None:\n                level.append(tree[idx])\n                left, right = 2 * idx + 1, 2 * idx + 2\n                if left < len(tree) and tree[left] is not None: queue.append(left)\n                if right < len(tree) and tree[right] is not None: queue.append(right)\n        if level:\n            res.append(level)\n    return res\n",
        test_cases=[{"input": [[3, 9, 20, None, None, 15, 7]], "expected": [[3], [9, 20], [15, 7]]}, {"input": [[1]], "expected": [[1]]}, {"input": [[]], "expected": []}],
        hints=["Use a BFS queue, processing len(queue) nodes at each level step."],
        leetcode_id=102
    ))

    # 58. Binary Tree Zigzag Level Order Traversal
    problems.append(make_problem(
        pid="ds-m-zigzag-level-order", title="Binary Tree Zigzag Level Order",
        wing_id="data-structures", floor=168, difficulty="medium", visualizer_type="tree",
        monster_name="Serpentine Drake", monster_title="Alternating Sweeper of Tree Tiers",
        monster_sprite="dragon", monster_color="#10b981", monster_attack="Alternating Blaze",
        monster_quote="Reversing alternate levels zigzagged smoothly!",
        description="Given a binary tree as an array, return the zigzag level order traversal of its nodes' values (i.e., from left to right, then right to left for the next level and alternate between).",
        examples=[{"input": "tree = [3,9,20,None,None,15,7]", "output": "[[3],[20,9],[15,7]]"}],
        constraints=["0 <= len(tree) <= 2000"],
        function_name="zigzagLevelOrder",
        starter_code="def zigzagLevelOrder(tree: list) -> list[list[int]]:\n    pass\n",
        solution_code="def zigzagLevelOrder(tree: list) -> list[list[int]]:\n    if not tree or tree[0] is None: return []\n    from collections import deque\n    res = []\n    queue = deque([0])\n    reverse_level = False\n    while queue:\n        level = []\n        for _ in range(len(queue)):\n            idx = queue.popleft()\n            if idx < len(tree) and tree[idx] is not None:\n                level.append(tree[idx])\n                left, right = 2 * idx + 1, 2 * idx + 2\n                if left < len(tree) and tree[left] is not None: queue.append(left)\n                if right < len(tree) and tree[right] is not None: queue.append(right)\n        if level:\n            res.append(list(reversed(level)) if reverse_level else level)\n            reverse_level = not reverse_level\n    return res\n",
        test_cases=[{"input": [[3, 9, 20, None, None, 15, 7]], "expected": [[3], [20, 9], [15, 7]]}, {"input": [[1]], "expected": [[1]]}],
        hints=["Same as level order BFS, but reverse level array whenever depth is odd."],
        leetcode_id=103
    ))

    # 59. Binary Tree Right Side View
    problems.append(make_problem(
        pid="ds-m-right-side-view", title="Binary Tree Right Side View",
        wing_id="data-structures", floor=169, difficulty="medium", visualizer_type="tree",
        monster_name="Right-Flank Cyclops", monster_title="Observer of the Eastern Canopy",
        monster_sprite="golem", monster_color="#f59e0b", monster_attack="Right Ray",
        monster_quote="Taking the last element of every BFS layer revealed the right view!",
        description="Given the root of a binary tree as an array, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.",
        examples=[{"input": "tree = [1,2,3,None,5,None,4]", "output": "[1,3,4]"}],
        constraints=["0 <= len(tree) <= 2000"],
        function_name="rightSideView",
        starter_code="def rightSideView(tree: list) -> list[int]:\n    pass\n",
        solution_code="def rightSideView(tree: list) -> list[int]:\n    if not tree or tree[0] is None: return []\n    from collections import deque\n    res = []\n    queue = deque([0])\n    while queue:\n        last_val = None\n        for _ in range(len(queue)):\n            idx = queue.popleft()\n            if idx < len(tree) and tree[idx] is not None:\n                last_val = tree[idx]\n                left, right = 2 * idx + 1, 2 * idx + 2\n                if left < len(tree) and tree[left] is not None: queue.append(left)\n                if right < len(tree) and tree[right] is not None: queue.append(right)\n        if last_val is not None:\n            res.append(last_val)\n    return res\n",
        test_cases=[{"input": [[1, 2, 3, None, 5, None, 4]], "expected": [1, 3, 4]}, {"input": [[1, None, 3]], "expected": [1, 3]}, {"input": [[]], "expected": []}],
        hints=["In BFS level order, the last node processed in each level is the rightmost visible node."],
        leetcode_id=199
    ))

    # 60. Lowest Common Ancestor of a Binary Search Tree
    problems.append(make_problem(
        pid="ds-m-lowest-common-ancestor-bst", title="Lowest Common Ancestor in BST",
        wing_id="data-structures", floor=170, difficulty="medium", visualizer_type="tree",
        monster_name="Ancestral Lich", monster_title="Keeper of Forking Heritage",
        monster_sprite="lich", monster_color="#8b5cf6", monster_attack="Ancestral Blast",
        monster_quote="The split point between p and q identified the LCA immediately!",
        description="Given a binary search tree (BST) represented as an inorder array, and two node values `p` and `q`, find the lowest common ancestor (LCA) node value. In a BST, the LCA of `p` and `q` is the first node whose value lies between `min(p, q)` and `max(p, q)`.",
        examples=[{"input": "tree_values = [0,2,3,4,5,6,7,8,9], root_val = 6, p = 2, q = 8", "output": "6"}, {"input": "tree_values = [0,2,3,4,5,6,7,8,9], root_val = 6, p = 2, q = 4", "output": "2"}],
        constraints=["2 <= len(tree_values) <= 10^5", "p and q exist in the BST"],
        function_name="lowestCommonAncestorBST",
        starter_code="def lowestCommonAncestorBST(root_val: int, p: int, q: int) -> int:\n    pass\n",
        solution_code="def lowestCommonAncestorBST(root_val: int, p: int, q: int) -> int:\n    # In a BST rooted at root_val: if both < root_val, LCA is in left; if both > root_val, right; else root_val\n    low, high = min(p, q), max(p, q)\n    if low <= root_val <= high:\n        return root_val\n    elif high < root_val:\n        return low\n    else:\n        return high\n",
        test_cases=[{"input": [6, 2, 8], "expected": 6}, {"input": [6, 2, 4], "expected": 2}, {"input": [2, 1, 2], "expected": 2}],
        hints=["If both p and q are smaller than root, LCA is in left subtree; if both larger, right; otherwise root is LCA."],
        leetcode_id=235
    ))

    return problems
