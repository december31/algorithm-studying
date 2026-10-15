"""
Binary Search & Greedy Easy Problems (Floors 401-410 - 10 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_bs_greedy_easy():
    problems = []

    # 1. Binary Search
    problems.append(make_problem(
        pid="bsg-e-binary-search", title="Standard Binary Search",
        wing_id="binary-search-greedy", floor=401, difficulty="easy", visualizer_type="array",
        monster_name="Bisection Imp", monster_title="Halver of Ordered Space",
        monster_sprite="imp", monster_color="#38bdf8", monster_attack="Half-Step Cleave",
        monster_quote="Target located in O(log n) logarithmic steps!",
        description="Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.",
        examples=[{"input": "nums = [-1,0,3,5,9,12], target = 9", "output": "4"}, {"input": "nums = [-1,0,3,5,9,12], target = 2", "output": "-1"}],
        constraints=["1 <= nums.length <= 10000", "-10000 < nums[i], target < 10000"],
        function_name="search",
        starter_code="def search(nums: list[int], target: int) -> int:\n    pass\n",
        solution_code="def search(nums: list[int], target: int) -> int:\n    lo, hi = 0, len(nums) - 1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        if nums[mid] == target: return mid\n        elif nums[mid] < target: lo = mid + 1\n        else: hi = mid - 1\n    return -1\n",
        test_cases=[{"input": [[-1, 0, 3, 5, 9, 12], 9], "expected": 4}, {"input": [[-1, 0, 3, 5, 9, 12], 2], "expected": -1}],
        hints=["Maintain [lo, hi] bounds, halving search space by comparing target to nums[mid]."],
        leetcode_id=704
    ))

    # 2. Search Insert Position
    problems.append(make_problem(
        pid="bsg-e-search-insert-position", title="Search Insert Position",
        wing_id="binary-search-greedy", floor=402, difficulty="easy", visualizer_type="array",
        monster_name="Slot Inserter", monster_title="Locator of Sorted Insertion Indices",
        monster_sprite="goblin", monster_color="#10b981", monster_attack="Index Wedge",
        monster_quote="Index where target belongs in sorted sequence found!",
        description="Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.",
        examples=[{"input": "nums = [1,3,5,6], target = 5", "output": "2"}, {"input": "nums = [1,3,5,6], target = 2", "output": "1"}, {"input": "nums = [1,3,5,6], target = 7", "output": "4"}],
        constraints=["1 <= nums.length <= 10000"],
        function_name="searchInsert",
        starter_code="def searchInsert(nums: list[int], target: int) -> int:\n    pass\n",
        solution_code="def searchInsert(nums: list[int], target: int) -> int:\n    lo, hi = 0, len(nums) - 1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        if nums[mid] == target: return mid\n        elif nums[mid] < target: lo = mid + 1\n        else: hi = mid - 1\n    return lo\n",
        test_cases=[{"input": [[1, 3, 5, 6], 5], "expected": 2}, {"input": [[1, 3, 5, 6], 2], "expected": 1}, {"input": [[1, 3, 5, 6], 7], "expected": 4}],
        hints=["Return `lo` after loop termination: `lo` points to the first element >= target."],
        leetcode_id=35
    ))

    # 3. Sqrt(x)
    problems.append(make_problem(
        pid="bsg-e-sqrt-x", title="Square Root via Binary Search",
        wing_id="binary-search-greedy", floor=403, difficulty="easy", visualizer_type="array",
        monster_name="Radical Fiend", monster_title="Truncator of Quadratic Roots",
        monster_sprite="slime", monster_color="#8b5cf6", monster_attack="Root Sever",
        monster_quote="Floor integer square root computed!",
        description="Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The returned integer should be non-negative as well. You must not use any built-in exponent function or operator.",
        examples=[{"input": "x = 4", "output": "2"}, {"input": "x = 8", "output": "2"}],
        constraints=["0 <= x <= 2^31 - 1"],
        function_name="mySqrt",
        starter_code="def mySqrt(x: int) -> int:\n    pass\n",
        solution_code="def mySqrt(x: int) -> int:\n    if x < 2: return x\n    lo, hi = 1, x // 2\n    ans = 1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        if mid * mid <= x:\n            ans = mid\n            lo = mid + 1\n        else:\n            hi = mid - 1\n    return ans\n",
        test_cases=[{"input": [4], "expected": 2}, {"input": [8], "expected": 2}, {"input": [0], "expected": 0}],
        hints=["Binary search over [1, x // 2]. Check if mid * mid <= x."],
        leetcode_id=69
    ))

    # 4. Peak Index in a Mountain Array
    problems.append(make_problem(
        pid="bsg-e-peak-index-mountain-array", title="Peak Index in Mountain Array",
        wing_id="binary-search-greedy", floor=404, difficulty="easy", visualizer_type="array",
        monster_name="Apex Drake", monster_title="Surveyor of Unimodal Peaks",
        monster_sprite="dragon", monster_color="#ec4899", monster_attack="Crest Gale",
        monster_quote="Summit index of unimodal mountain array located!",
        description="An array `arr` is a mountain if `arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`. Given a mountain array `arr`, return the index `i` such that `arr[0] < ... < arr[i] > ... > arr[arr.length - 1]`.",
        examples=[{"input": "arr = [0,1,0]", "output": "1"}, {"input": "arr = [0,2,1,0]", "output": "1"}, {"input": "arr = [0,10,5,2]", "output": "1"}],
        constraints=["3 <= arr.length <= 100000"],
        function_name="peakIndexInMountainArray",
        starter_code="def peakIndexInMountainArray(arr: list[int]) -> int:\n    pass\n",
        solution_code="def peakIndexInMountainArray(arr: list[int]) -> int:\n    lo, hi = 0, len(arr) - 1\n    while lo < hi:\n        mid = (lo + hi) // 2\n        if arr[mid] < arr[mid + 1]:\n            lo = mid + 1\n        else:\n            hi = mid\n    return lo\n",
        test_cases=[{"input": [[0, 1, 0]], "expected": 1}, {"input": [[0, 2, 1, 0]], "expected": 1}, {"input": [[0, 10, 5, 2]], "expected": 1}],
        hints=["Compare arr[mid] with arr[mid + 1] to decide whether to move up or down the slope."],
        leetcode_id=852
    ))

    # 5. Lemonade Change
    problems.append(make_problem(
        pid="bsg-e-lemonade-change", title="Lemonade Change (Greedy Cashier)",
        wing_id="binary-search-greedy", floor=405, difficulty="easy", visualizer_type="array",
        monster_name="Cashier Goblin", monster_title="Tender of Exact Change",
        monster_sprite="goblin", monster_color="#f59e0b", monster_attack="Coin Shower",
        monster_quote="Can change be provided for every customer in sequence?",
        description="At a lemonade stand, each lemonade costs $5. Customers stand in a queue and order one at a time, paying with a $5, $10, or $20 bill. You must provide the correct change to each customer, initially starting with no change. Return `True` if you can provide every customer with correct change, or `False` otherwise.",
        examples=[{"input": "bills = [5,5,5,10,20]", "output": "True"}, {"input": "bills = [5,5,10,10,20]", "output": "False"}],
        constraints=["1 <= bills.length <= 100000", "bills[i] is 5, 10, or 20"],
        function_name="lemonadeChange",
        starter_code="def lemonadeChange(bills: list[int]) -> bool:\n    pass\n",
        solution_code="def lemonadeChange(bills: list[int]) -> bool:\n    five = ten = 0\n    for b in bills:\n        if b == 5: five += 1\n        elif b == 10:\n            if five == 0: return False\n            five -= 1\n            ten += 1\n        else:\n            if ten > 0 and five > 0:\n                ten -= 1\n                five -= 1\n            elif five >= 3:\n                five -= 3\n            else:\n                return False\n    return True\n",
        test_cases=[{"input": [[5, 5, 5, 10, 20]], "expected": True}, {"input": [[5, 5, 10, 10, 20]], "expected": False}],
        hints=["Greedily use a $10 bill and a $5 bill to give change for $20 before falling back to three $5 bills."],
        leetcode_id=860
    ))

    # 6. Assign Cookies
    problems.append(make_problem(
        pid="bsg-e-assign-cookies", title="Assign Cookies (Greedy Contentment)",
        wing_id="binary-search-greedy", floor=406, difficulty="easy", visualizer_type="array",
        monster_name="Baker Imp", monster_title="Distributor of Sugary Morsels",
        monster_sprite="imp", monster_color="#f97316", monster_attack="Cookie Rain",
        monster_quote="Maximum number of children satisfied with cookie sizes!",
        description="Assume you are an awesome parent and want to give your children some cookies. Each child `i` has a greed factor `g[i]`, and each cookie `j` has a size `s[j]`. If `s[j] >= g[i]`, we can assign cookie `j` to child `i`. Your goal is to maximize the number of content children and return the count.",
        examples=[{"input": "g = [1,2,3], s = [1,1]", "output": "1"}, {"input": "g = [1,2], s = [1,2,3]", "output": "2"}],
        constraints=["1 <= g.length <= 30000", "0 <= s.length <= 30000"],
        function_name="findContentChildren",
        starter_code="def findContentChildren(g: list[int], s: list[int]) -> int:\n    pass\n",
        solution_code="def findContentChildren(g: list[int], s: list[int]) -> int:\n    g.sort()\n    s.sort()\n    i = j = 0\n    while i < len(g) and j < len(s):\n        if s[j] >= g[i]:\n            i += 1\n        j += 1\n    return i\n",
        test_cases=[{"input": [[1, 2, 3], [1, 1]], "expected": 1}, {"input": [[1, 2], [1, 2, 3]], "expected": 2}],
        hints=["Sort both arrays and greedily satisfy the least greedy child with the smallest sufficient cookie."],
        leetcode_id=455
    ))

    # 7. Can Place Flowers
    problems.append(make_problem(
        pid="bsg-e-can-place-flowers", title="Can Place Flowers (No-Adjacent Planting)",
        wing_id="binary-search-greedy", floor=407, difficulty="easy", visualizer_type="array",
        monster_name="Flora Sylph", monster_title="Planter in Non-Adjacent Soil",
        monster_sprite="spectre", monster_color="#22c55e", monster_attack="Thorn Sprout",
        monster_quote="Can n new flowers be planted without violating adjacency rules?",
        description="You have a long flowerbed in which some plots are planted (1) and some are not (0). Flowers cannot be planted in adjacent plots. Given an integer array `flowerbed` and an integer `n`, return `True` if `n` new flowers can be planted without violating the no-adjacent-flowers rule.",
        examples=[{"input": "flowerbed = [1,0,0,0,1], n = 1", "output": "True"}, {"input": "flowerbed = [1,0,0,0,1], n = 2", "output": "False"}],
        constraints=["1 <= flowerbed.length <= 20000", "0 <= n <= flowerbed.length"],
        function_name="canPlaceFlowers",
        starter_code="def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:\n    pass\n",
        solution_code="def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:\n    count = 0\n    for i in range(len(flowerbed)):\n        if flowerbed[i] == 0:\n            prev_empty = (i == 0 or flowerbed[i - 1] == 0)\n            next_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)\n            if prev_empty and next_empty:\n                flowerbed[i] = 1\n                count += 1\n    return count >= n\n",
        test_cases=[{"input": [[1, 0, 0, 0, 1], 1], "expected": True}, {"input": [[1, 0, 0, 0, 1], 2], "expected": False}],
        hints=["Greedily place a flower as early as possible whenever plot and both neighbors are 0."],
        leetcode_id=605
    ))

    # 8. Maximum Units on a Truck
    problems.append(make_problem(
        pid="bsg-e-max-units-truck", title="Maximum Units on a Truck (Fractional Knapsack)",
        wing_id="binary-search-greedy", floor=408, difficulty="easy", visualizer_type="array",
        monster_name="Freight Minotaur", monster_title="Loader of Denser Freight",
        monster_sprite="gargoyle", monster_color="#64748b", monster_attack="Cargo Crush",
        monster_quote="Total cargo units maximized within truck box capacity!",
        description="You are assigned to put some amount of boxes onto one truck. You are given a 2D array `boxTypes`, where `boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]`. You are also given `truckSize`, which is the maximum number of boxes that can be put on the truck. Return the maximum total number of units that can be put on the truck.",
        examples=[{"input": "boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4", "output": "8"}, {"input": "boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10", "output": "91"}],
        constraints=["1 <= boxTypes.length <= 1000", "1 <= truckSize <= 10^6"],
        function_name="maximumUnits",
        starter_code="def maximumUnits(boxTypes: list[list[int]], truckSize: int) -> int:\n    pass\n",
        solution_code="def maximumUnits(boxTypes: list[list[int]], truckSize: int) -> int:\n    boxTypes.sort(key=lambda x: x[1], reverse=True)\n    units = 0\n    for boxes, u in boxTypes:\n        take = min(boxes, truckSize)\n        units += take * u\n        truckSize -= take\n        if truckSize == 0: break\n    return units\n",
        test_cases=[{"input": [[[1, 3], [2, 2], [3, 1]], 4], "expected": 8}, {"input": [[[5, 10], [2, 5], [4, 7], [3, 9]], 10], "expected": 91}],
        hints=["Greedily pick boxes with the highest units per box first."],
        leetcode_id=1710
    ))

    # 9. Minimum Absolute Difference in Array
    problems.append(make_problem(
        pid="bsg-e-min-abs-diff-array", title="Minimum Absolute Difference Pairs",
        wing_id="binary-search-greedy", floor=409, difficulty="easy", visualizer_type="array",
        monster_name="Precision Wraith", monster_title="Seeker of Tightest Numeric Gaps",
        monster_sprite="wraith", monster_color="#38bdf8", monster_attack="Proximity Slice",
        monster_quote="All coordinate pairs with minimal absolute difference collected!",
        description="Given an array of distinct integers `arr`, find all pairs of elements with the minimum absolute difference of any two elements. Return a list of pairs in ascending order with respect to pairs.",
        examples=[{"input": "arr = [4,2,1,3]", "output": "[[1,2],[2,3],[3,4]]"}, {"input": "arr = [1,3,6,10,15]", "output": "[[1,3]]"}],
        constraints=["2 <= arr.length <= 100000"],
        function_name="minimumAbsDifference",
        starter_code="def minimumAbsDifference(arr: list[int]) -> list[list[int]]:\n    pass\n",
        solution_code="def minimumAbsDifference(arr: list[int]) -> list[list[int]]:\n    arr.sort()\n    min_diff = min(arr[i + 1] - arr[i] for i in range(len(arr) - 1))\n    return [[arr[i], arr[i + 1]] for i in range(len(arr) - 1) if arr[i + 1] - arr[i] == min_diff]\n",
        test_cases=[{"input": [[4, 2, 1, 3]], "expected": [[1, 2], [2, 3], [3, 4]]}, {"input": [[1, 3, 6, 10, 15]], "expected": [[1, 3]]}],
        hints=["Sort the array. The minimum difference must occur between two adjacent elements."],
        leetcode_id=1200
    ))

    # 10. Valid Perfect Square
    problems.append(make_problem(
        pid="bsg-e-valid-perfect-square", title="Valid Perfect Square",
        wing_id="binary-search-greedy", floor=410, difficulty="easy", visualizer_type="array",
        monster_name="Square Sentinel", monster_title="Guardian of Integer Quadrates",
        monster_sprite="boss", monster_color="#ef4444", monster_attack="Quadratic Ray",
        monster_quote="Is num a perfect square without using library functions?",
        description="Given a positive integer `num`, return `True` if `num` is a perfect square or `False` otherwise. You must not use any built-in library function, such as `sqrt`.",
        examples=[{"input": "num = 16", "output": "True"}, {"input": "num = 14", "output": "False"}],
        constraints=["1 <= num <= 2^31 - 1"],
        function_name="isPerfectSquare",
        starter_code="def isPerfectSquare(num: int) -> bool:\n    pass\n",
        solution_code="def isPerfectSquare(num: int) -> bool:\n    lo, hi = 1, num\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        sq = mid * mid\n        if sq == num: return True\n        elif sq < num: lo = mid + 1\n        else: hi = mid - 1\n    return False\n",
        test_cases=[{"input": [16], "expected": True}, {"input": [14], "expected": False}, {"input": [1], "expected": True}],
        hints=["Binary search for an integer k such that k * k == num."],
        leetcode_id=367
    ))

    return problems
