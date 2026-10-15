"""
Binary Search & Greedy Medium Problems - Part 3 (Floors 441 to 455 - 15 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_bs_greedy_medium_part3():
    problems = []

    # 41. Minimum Speed to Arrive on Time
    problems.append(make_problem(
        pid="bsg-m-min-speed-arrive-on-time", title="Minimum Speed to Arrive on Time",
        wing_id="binary-search-greedy", floor=441, difficulty="medium", visualizer_type="array",
        monster_name="Locomotive Wyrm", monster_title="Throttle Master of Timed Commutes",
        monster_sprite="dragon", monster_color="#ef4444", monster_attack="Steam Blast",
        monster_quote="Minimum integer train speed to reach destination within hour limit!",
        description="You are given a floating point number `hour`, representing the amount of time you have to reach the office. To commute to the office, you must take `n` trains in sequential order. Given `dist` of length `n`, each train departs at integer hours except the last. Return the minimum positive integer speed required to arrive on time, or -1 if impossible.",
        examples=[{"input": "dist = [1,3,2], hour = 6", "output": "1"}, {"input": "dist = [1,3,2], hour = 2.7", "output": "3"}, {"input": "dist = [1,3,2], hour = 1.9", "output": "-1"}],
        constraints=["1 <= dist.length <= 100000", "1 <= hour <= 10^9"],
        function_name="minSpeedOnTime",
        starter_code="def minSpeedOnTime(dist: list[int], hour: float) -> int:\n    pass\n",
        solution_code="def minSpeedOnTime(dist: list[int], hour: float) -> int:\n    import math\n    if hour <= len(dist) - 1: return -1\n    lo, hi = 1, 10**7\n    ans = -1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        t = sum(math.ceil(d / mid) for d in dist[:-1]) + dist[-1] / mid\n        if t <= hour:\n            ans = mid\n            hi = mid - 1\n        else:\n            lo = mid + 1\n    return ans\n",
        test_cases=[{"input": [[1, 3, 2], 6], "expected": 1}, {"input": [[1, 3, 2], 2.7], "expected": 3}, {"input": [[1, 3, 2], 1.9], "expected": -1}],
        hints=["Binary search speed in [1, 10^7]. Remember earlier trains wait for the next integer hour."],
        leetcode_id=1870
    ))

    # 42. Maximum Number of Removable Characters
    problems.append(make_problem(
        pid="bsg-m-max-removable-characters", title="Maximum Number of Removable Characters",
        wing_id="binary-search-greedy", floor=442, difficulty="medium", visualizer_type="array",
        monster_name="Redaction Specter", monster_title="Eraser of Substring Glyphs",
        monster_sprite="spectre", monster_color="#8b5cf6", monster_attack="Glyph Erasure",
        monster_quote="Maximum k removals from s such that p remains a subsequence!",
        description="You are given two strings `s` and `p` where `p` is a subsequence of `s`. You are also given a distinct 0-indexed integer array `removable` containing a subset of indices of `s`. You want to choose an integer `k` (`0 <= k <= removable.length`) such that, after removing characters at `removable[0], ..., removable[k - 1]`, `p` is still a subsequence of `s`. Return the maximum `k`.",
        examples=[{"input": "s = \"abcacb\", p = \"ab\", removable = [3,1,0]", "output": "2"}, {"input": "s = \"abcbddddd\", p = \"abcd\", removable = [3,2,1,4,5,6]", "output": "1"}],
        constraints=["1 <= p.length <= s.length <= 100000"],
        function_name="maximumRemovals",
        starter_code="def maximumRemovals(s: str, p: str, removable: list[int]) -> int:\n    pass\n",
        solution_code="def maximumRemovals(s: str, p: str, removable: list[int]) -> int:\n    def is_subseq(k):\n        removed = set(removable[:k])\n        j = 0\n        for i, ch in enumerate(s):\n            if i not in removed and ch == p[j]:\n                j += 1\n                if j == len(p): return True\n        return False\n    lo, hi = 0, len(removable)\n    ans = 0\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        if is_subseq(mid):\n            ans = mid\n            lo = mid + 1\n        else:\n            hi = mid - 1\n    return ans\n",
        test_cases=[{"input": ["abcacb", "ab", [3, 1, 0]], "expected": 2}, {"input": ["abcbddddd", "abcd", [3, 2, 1, 4, 5, 6]], "expected": 1}],
        hints=["Binary search on k in [0, len(removable)]. Test subsequence validity in O(len(s))."],
        leetcode_id=1898
    ))

    # 43. Kth Missing Positive Number
    problems.append(make_problem(
        pid="bsg-m-kth-missing-positive", title="Kth Missing Positive Number",
        wing_id="binary-search-greedy", floor=443, difficulty="medium", visualizer_type="array",
        monster_name="Gap Golem", monster_title="Overseer of Absent Integers",
        monster_sprite="golem", monster_color="#f59e0b", monster_attack="Omission Void",
        monster_quote="The k-th positive integer missing from sorted array found!",
        description="Given an array `arr` of positive integers sorted in a strictly increasing order, and an integer `k`. Return the `k`-th positive integer that is missing from this array.",
        examples=[{"input": "arr = [2,3,4,7,11], k = 5", "output": "9"}, {"input": "arr = [1,2,3,4], k = 2", "output": "6"}],
        constraints=["1 <= arr.length <= 1000", "1 <= arr[i] <= 1000", "1 <= k <= 1000"],
        function_name="findKthPositive",
        starter_code="def findKthPositive(arr: list[int], k: int) -> int:\n    pass\n",
        solution_code="def findKthPositive(arr: list[int], k: int) -> int:\n    lo, hi = 0, len(arr) - 1\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        missing = arr[mid] - (mid + 1)\n        if missing < k:\n            lo = mid + 1\n        else:\n            hi = mid - 1\n    return lo + k\n",
        test_cases=[{"input": [[2, 3, 4, 7, 11], 5], "expected": 9}, {"input": [[1, 2, 3, 4], 2], "expected": 6}],
        hints=["Missing numbers before index mid is arr[mid] - (mid + 1). Binary search for the first index where missing >= k."],
        leetcode_id=1539
    ))

    # 44. Minimum Limit of Balls in a Bag
    problems.append(make_problem(
        pid="bsg-m-min-limit-balls-bag", title="Minimum Limit of Balls in a Bag (Max Penalty)",
        wing_id="binary-search-greedy", floor=444, difficulty="medium", visualizer_type="array",
        monster_name="Fission Drake", monster_title="Cleaver of Oversized Satchels",
        monster_sprite="dragon", monster_color="#06b6d4", monster_attack="Bag Rupture",
        monster_quote="Max bag size minimized using at most maxOperations splits!",
        description="You are given an integer array `nums` where the `i`-th bag contains `nums[i]` balls. You can divide any bag into two new bags. You can perform at most `maxOperations` operations. Your penalty is the maximum number of balls in a bag. Return the minimum possible penalty.",
        examples=[{"input": "nums = [9], maxOperations = 2", "output": "3"}, {"input": "nums = [2,4,8,2], maxOperations = 4", "output": "2"}],
        constraints=["1 <= nums.length <= 100000", "1 <= maxOperations, nums[i] <= 10^9"],
        function_name="minimumSize",
        starter_code="def minimumSize(nums: list[int], maxOperations: int) -> int:\n    pass\n",
        solution_code="def minimumSize(nums: list[int], maxOperations: int) -> int:\n    lo, hi = 1, max(nums)\n    ans = hi\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        ops = sum((x - 1) // mid for x in nums)\n        if ops <= maxOperations:\n            ans = mid\n            hi = mid - 1\n        else:\n            lo = mid + 1\n    return ans\n",
        test_cases=[{"input": [[9], 2], "expected": 3}, {"input": [[2, 4, 8, 2], 4], "expected": 2}, {"input": [[7, 17], 2], "expected": 7}],
        hints=["Binary search target maximum penalty mid. Number of operations to split bag x into parts <= mid is (x - 1) // mid."],
        leetcode_id=1760
    ))

    # 45. Maximum Candies Allocated to K Children
    problems.append(make_problem(
        pid="bsg-m-max-candies-k-children", title="Maximum Candies Allocated to K Children",
        wing_id="binary-search-greedy", floor=445, difficulty="medium", visualizer_type="array",
        monster_name="Confection Colossus", monster_title="Distributor of Equal Sugar Heaps",
        monster_sprite="golem", monster_color="#ec4899", monster_attack="Caramel Deluge",
        monster_quote="Maximum equal candy pile size that can be given to all k children!",
        description="You are given a 0-indexed integer array `candies`. Each element in the array denotes a pile of candies of size `candies[i]`. You can divide each pile into any number of sub piles. You have `k` children. You want to allocate to each child an equal number of candies from a sub pile. Return the maximum number of candies each child can get.",
        examples=[{"input": "candies = [5,8,6], k = 3", "output": "5"}, {"input": "candies = [2,5], k = 11", "output": "0"}],
        constraints=["1 <= candies.length <= 100000", "1 <= k <= 10^12"],
        function_name="maximumCandies",
        starter_code="def maximumCandies(candies: list[int], k: int) -> int:\n    pass\n",
        solution_code="def maximumCandies(candies: list[int], k: int) -> int:\n    lo, hi = 1, max(candies)\n    ans = 0\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        piles = sum(c // mid for c in candies)\n        if piles >= k:\n            ans = mid\n            lo = mid + 1\n        else:\n            hi = mid - 1\n    return ans\n",
        test_cases=[{"input": [[5, 8, 6], 3], "expected": 5}, {"input": [[2, 5], 11], "expected": 0}],
        hints=["Binary search on answer pile size mid in [1, max(candies)]. Count sum(c // mid)."],
        leetcode_id=2226
    ))

    # 46. Most Profit Assigning Work
    problems.append(make_problem(
        pid="bsg-m-most-profit-assigning-work", title="Most Profit Assigning Work",
        wing_id="binary-search-greedy", floor=446, difficulty="medium", visualizer_type="array",
        monster_name="Guildmaster Fiend", monster_title="Contractor of Skilled Labor",
        monster_sprite="boss", monster_color="#38bdf8", monster_attack="Bounty Slash",
        monster_quote="Max total profit collected across all worker abilities!",
        description="You have `n` jobs and `m` workers. Given `difficulty` and `profit` of jobs, and `worker` abilities. Each worker can be assigned at most one job that has difficulty at most their ability. Return the maximum profit we can achieve.",
        examples=[{"input": "difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]", "output": "100"}],
        constraints=["1 <= difficulty.length == profit.length <= 10000", "1 <= worker.length <= 10000"],
        function_name="maxProfitAssignment",
        starter_code="def maxProfitAssignment(difficulty: list[int], profit: list[int], worker: list[int]) -> int:\n    pass\n",
        solution_code="def maxProfitAssignment(difficulty: list[int], profit: list[int], worker: list[int]) -> int:\n    jobs = sorted(zip(difficulty, profit))\n    worker.sort()\n    total = best = j = 0\n    for ability in worker:\n        while j < len(jobs) and jobs[j][0] <= ability:\n            best = max(best, jobs[j][1])\n            j += 1\n        total += best\n    return total\n",
        test_cases=[{"input": [[2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]], "expected": 100}, {"input": [[85, 47, 57], [24, 66, 99], [40, 25, 25]], "expected": 0}],
        hints=["Sort jobs by difficulty and workers by ability. Two-pointer sweep maintaining running maximum profit."],
        leetcode_id=826
    ))

    # 47. Maximum Number of Events That Can Be Attended
    problems.append(make_problem(
        pid="bsg-m-max-events-attended", title="Max Events That Can Be Attended",
        wing_id="binary-search-greedy", floor=447, difficulty="medium", visualizer_type="array",
        monster_name="Calendar Wraith", monster_title="Scheduler of Fleeting Days",
        monster_sprite="wraith", monster_color="#10b981", monster_attack="Schedule Lock",
        monster_quote="Maximum distinct events attended on distinct days!",
        description="You are given an array of `events` where `events[i] = [startDayi, endDayi]`. You can attend event `i` at any day where `startDayi <= d <= endDayi`. You can only attend one event at any given day. Return the maximum number of events you can attend.",
        examples=[{"input": "events = [[1,2],[2,3],[3,4]]", "output": "3"}, {"input": "events = [[1,2],[2,3],[3,4],[1,2]]", "output": "4"}],
        constraints=["1 <= events.length <= 100000"],
        function_name="maxEvents",
        starter_code="def maxEvents(events: list[list[int]]) -> int:\n    pass\n",
        solution_code="def maxEvents(events: list[list[int]]) -> int:\n    import heapq\n    events.sort(key=lambda x: x[0])\n    pq = []\n    attended = 0\n    day = 0\n    i = 0\n    n = len(events)\n    while i < n or pq:\n        if not pq:\n            day = events[i][0]\n        while i < n and events[i][0] <= day:\n            heapq.heappush(pq, events[i][1])\n            i += 1\n        while pq and pq[0] < day:\n            heapq.heappop(pq)\n        if pq:\n            heapq.heappop(pq)\n            attended += 1\n            day += 1\n    return attended\n",
        test_cases=[{"input": [[[1, 2], [2, 3], [3, 4]]], "expected": 3}, {"input": [[[1, 2], [2, 3], [3, 4], [1, 2]]], "expected": 4}],
        hints=["Simulate day by day. On each day, greedily attend the open event that finishes earliest (min-heap)."],
        leetcode_id=1353
    ))

    # 48. Reduce Array Size to The Half
    problems.append(make_problem(
        pid="bsg-m-reduce-array-size-half", title="Reduce Array Size to The Half",
        wing_id="binary-search-greedy", floor=448, difficulty="medium", visualizer_type="array",
        monster_name="Decimation Imp", monster_title="Pruner of Dominant Elements",
        monster_sprite="imp", monster_color="#ef4444", monster_attack="Halving Cleave",
        monster_quote="Minimum unique values removed to eliminate at least half the array!",
        description="You are given an integer array `arr`. You can choose a set of integers and remove all the occurrences of these integers in the array. Return the minimum size of the set so that at least half of the integers of the array are removed.",
        examples=[{"input": "arr = [3,3,3,3,5,5,5,2,2,7]", "output": "2"}, {"input": "arr = [7,7,7,7,7,7]", "output": "1"}],
        constraints=["2 <= arr.length <= 100000", "arr.length is even"],
        function_name="minSetSize",
        starter_code="def minSetSize(arr: list[int]) -> int:\n    pass\n",
        solution_code="def minSetSize(arr: list[int]) -> int:\n    from collections import Counter\n    counts = Counter(arr)\n    freqs = sorted(counts.values(), reverse=True)\n    removed = 0\n    ans = 0\n    half = len(arr) // 2\n    for f in freqs:\n        removed += f\n        ans += 1\n        if removed >= half: return ans\n    return ans\n",
        test_cases=[{"input": [[3, 3, 3, 3, 5, 5, 5, 2, 2, 7]], "expected": 2}, {"input": [[7, 7, 7, 7, 7, 7]], "expected": 1}],
        hints=["Sort value frequencies in descending order and greedily take the most frequent numbers."],
        leetcode_id=1338
    ))

    # 49. Minimum Deletions to Make Character Frequencies Unique
    problems.append(make_problem(
        pid="bsg-m-min-deletions-unique-frequencies", title="Min Deletions for Unique Frequencies",
        wing_id="binary-search-greedy", floor=449, difficulty="medium", visualizer_type="array",
        monster_name="Frequency Archon", monster_title="Enforcer of Non-Colliding Multiplicities",
        monster_sprite="spectre", monster_color="#8b5cf6", monster_attack="Collision Erasure",
        monster_quote="Minimum characters deleted so all letter frequencies are distinct!",
        description="A string `s` is called good if there are no two different characters in `s` that have the same frequency. Given a string `s`, return the minimum number of characters you need to delete to make `s` good.",
        examples=[{"input": "s = \"aab\"", "output": "0"}, {"input": "s = \"aaabbbcc\"", "output": "2"}, {"input": "s = \"ceabaacb\"", "output": "2"}],
        constraints=["1 <= s.length <= 100000"],
        function_name="minDeletions",
        starter_code="def minDeletions(s: str) -> int:\n    pass\n",
        solution_code="def minDeletions(s: str) -> int:\n    from collections import Counter\n    counts = Counter(s)\n    seen = set()\n    deletions = 0\n    for freq in counts.values():\n        while freq > 0 and freq in seen:\n            freq -= 1\n            deletions += 1\n        if freq > 0:\n            seen.add(freq)\n    return deletions\n",
        test_cases=[{"input": ["aab"], "expected": 0}, {"input": ["aaabbbcc"], "expected": 2}, {"input": ["ceabaacb"], "expected": 2}],
        hints=["Track occupied frequencies in a set. Greedily decrement duplicate frequencies until reaching an unused number or 0."],
        leetcode_id=1647
    ))

    # 50. Eliminate Maximum Number of Monsters
    problems.append(make_problem(
        pid="bsg-m-eliminate-max-monsters", title="Eliminate Maximum Number of Monsters",
        wing_id="binary-search-greedy", floor=450, difficulty="medium", visualizer_type="array",
        monster_name="Siege Gorgon", monster_title="Charger Against the City Gates",
        monster_sprite="boss", monster_color="#ef4444", monster_attack="Stampede Rush",
        monster_quote="Monsters eliminated before any creature reaches city gates!",
        description="You are playing a video game where monsters advance towards your city. Monster `i` starts at `dist[i]` and moves at `speed[i]`. Your weapon can vaporize one monster per minute. Return the maximum number of monsters that you can eliminate before you lose.",
        examples=[{"input": "dist = [1,3,4], speed = [1,1,1]", "output": "3"}, {"input": "dist = [1,1,2,3], speed = [1,1,1,1]", "output": "1"}],
        constraints=["n == dist.length == speed.length", "1 <= n <= 100000"],
        function_name="eliminateMaximum",
        starter_code="def eliminateMaximum(dist: list[int], speed: list[int]) -> int:\n    pass\n",
        solution_code="def eliminateMaximum(dist: list[int], speed: list[int]) -> int:\n    import math\n    arrival = sorted(d / s for d, s in zip(dist, speed))\n    for minute, arr_time in enumerate(arrival):\n        if arr_time <= minute:\n            return minute\n    return len(dist)\n",
        test_cases=[{"input": [[1, 3, 4], [1, 1, 1]], "expected": 3}, {"input": [[1, 1, 2, 3], [1, 1, 1, 1]], "expected": 1}, {"input": [[3, 2, 4], [5, 3, 2]], "expected": 1}],
        hints=["Calculate arrival times dist / speed, sort ascending, and check if arrival_time <= minute."],
        leetcode_id=1921
    ))

    # 51. Maximum Ice Cream Bars
    problems.append(make_problem(
        pid="bsg-m-max-ice-cream-bars", title="Maximum Ice Cream Bars (Greedy Purchase)",
        wing_id="binary-search-greedy", floor=451, difficulty="medium", visualizer_type="array",
        monster_name="Frost Merchant", monster_title="Vendor of Subzero Delicacies",
        monster_sprite="goblin", monster_color="#06b6d4", monster_attack="Frostbite Bargain",
        monster_quote="Maximum number of ice cream bars acquired within budget coins!",
        description="A boy wants to buy ice cream bars. You are given an array `costs` of length `n` and integer `coins`. Return the maximum number of ice cream bars the boy can buy with `coins` coins.",
        examples=[{"input": "costs = [1,3,2,4,1], coins = 7", "output": "4"}, {"input": "costs = [10,6,8,7,7,8], coins = 5", "output": "0"}],
        constraints=["1 <= costs.length <= 100000", "1 <= coins <= 10^8"],
        function_name="maxIceCream",
        starter_code="def maxIceCream(costs: list[int], coins: int) -> int:\n    pass\n",
        solution_code="def maxIceCream(costs: list[int], coins: int) -> int:\n    costs.sort()\n    count = 0\n    for c in costs:\n        if coins >= c:\n            coins -= c\n            count += 1\n        else: break\n    return count\n",
        test_cases=[{"input": [[1, 3, 2, 4, 1], 7], "expected": 4}, {"input": [[10, 6, 8, 7, 7, 8], 5], "expected": 0}],
        hints=["Greedily buy cheapest ice cream bars first after sorting costs."],
        leetcode_id=1833
    ))

    # 52. Minimum Time to Complete Trips
    problems.append(make_problem(
        pid="bsg-m-min-time-complete-trips", title="Minimum Time to Complete Trips",
        wing_id="binary-search-greedy", floor=452, difficulty="medium", visualizer_type="array",
        monster_name="Conveyance Titan", monster_title="Orchestrator of Concurrent Bus Lines",
        monster_sprite="titan", monster_color="#f59e0b", monster_attack="Transit Convergence",
        monster_quote="Minimum time elapsed until totalTrips completed across bus fleet!",
        description="You are given an array `time` where `time[i]` denotes the time taken by the `i`-th bus to complete one trip. Each bus can make multiple trips successively. Return the minimum time required for all buses to complete at least `totalTrips` trips in total.",
        examples=[{"input": "time = [1,2,3], totalTrips = 5", "output": "3"}, {"input": "time = [2], totalTrips = 1", "output": "2"}],
        constraints=["1 <= time.length <= 100000", "1 <= totalTrips <= 10^7"],
        function_name="minimumTime",
        starter_code="def minimumTime(time: list[int], totalTrips: int) -> int:\n    pass\n",
        solution_code="def minimumTime(time: list[int], totalTrips: int) -> int:\n    lo, hi = 1, min(time) * totalTrips\n    ans = hi\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        trips = sum(mid // t for t in time)\n        if trips >= totalTrips:\n            ans = mid\n            hi = mid - 1\n        else:\n            lo = mid + 1\n    return ans\n",
        test_cases=[{"input": [[1, 2, 3], 5], "expected": 3}, {"input": [[2], 1], "expected": 2}],
        hints=["Binary search on time T in [1, min(time) * totalTrips]. Total trips completed at time T is sum(T // t)."],
        leetcode_id=2187
    ))

    # 53. Maximum Running Time of N Computers
    problems.append(make_problem(
        pid="bsg-m-max-run-time-n-computers", title="Maximum Running Time of N Computers",
        wing_id="binary-search-greedy", floor=453, difficulty="medium", visualizer_type="array",
        monster_name="Galvanic Colossus", monster_title="Drainer of Parallel Power Cells",
        monster_sprite="golem", monster_color="#38bdf8", monster_attack="Battery Drain",
        monster_quote="Max simultaneous running minutes for n machines found!",
        description="You have `n` computers. You are given the integer array `batteries` where `batteries[i]` is the minutes the `i`-th battery can run. Batteries can be swapped instantaneously. Return the maximum number of minutes you can run all `n` computers simultaneously.",
        examples=[{"input": "n = 2, batteries = [3,3,3]", "output": "4"}, {"input": "n = 2, batteries = [1,1,1,1]", "output": "2"}],
        constraints=["1 <= n <= batteries.length <= 100000"],
        function_name="maxRunTime",
        starter_code="def maxRunTime(n: int, batteries: list[int]) -> int:\n    pass\n",
        solution_code="def maxRunTime(n: int, batteries: list[int]) -> int:\n    lo, hi = 1, sum(batteries) // n\n    ans = 0\n    while lo <= hi:\n        target = (lo + hi) // 2\n        total = sum(min(b, target) for b in batteries)\n        if total >= target * n:\n            ans = target\n            lo = target + 1\n        else:\n            hi = target - 1\n    return ans\n",
        test_cases=[{"input": [2, [3, 3, 3]], "expected": 4}, {"input": [2, [1, 1, 1, 1]], "expected": 2}],
        hints=["Binary search target time T. Each battery can contribute at most min(b, T). Check sum >= T * n."],
        leetcode_id=2141
    ))

    # 54. Find the Smallest Divisor Given a Threshold
    problems.append(make_problem(
        pid="bsg-m-smallest-divisor-threshold", title="Smallest Divisor Given a Threshold",
        wing_id="binary-search-greedy", floor=454, difficulty="medium", visualizer_type="array",
        monster_name="Quotient Specter", monster_title="Minimizer of Clamped Divisors",
        monster_sprite="spectre", monster_color="#10b981", monster_attack="Divisor Snap",
        monster_quote="Smallest integer divisor ensuring sum of division results <= threshold!",
        description="Given an array of integers `nums` and an integer `threshold`, find the smallest divisor such that the result of dividing each element by the divisor (rounded up) sums to at most `threshold`.",
        examples=[{"input": "nums = [1,2,5,9], threshold = 6", "output": "5"}, {"input": "nums = [44,22,33,11,1], threshold = 5", "output": "44"}],
        constraints=["1 <= nums.length <= 50000", "nums.length <= threshold <= 10^6"],
        function_name="smallestDivisor",
        starter_code="def smallestDivisor(nums: list[int], threshold: int) -> int:\n    pass\n",
        solution_code="def smallestDivisor(nums: list[int], threshold: int) -> int:\n    import math\n    lo, hi = 1, max(nums)\n    ans = hi\n    while lo <= hi:\n        mid = (lo + hi) // 2\n        total = sum(math.ceil(x / mid) for x in nums)\n        if total <= threshold:\n            ans = mid\n            hi = mid - 1\n        else:\n            lo = mid + 1\n    return ans\n",
        test_cases=[{"input": [[1, 2, 5, 9], 6], "expected": 5}, {"input": [[44, 22, 33, 11, 1], 5], "expected": 44}],
        hints=["Binary search divisor in [1, max(nums)]. Check sum(ceil(x / mid)) <= threshold."],
        leetcode_id=1283
    ))

    # 55. Kth Smallest Element in a Sorted Matrix
    problems.append(make_problem(
        pid="bsg-m-kth-smallest-sorted-matrix", title="Kth Smallest Element in Sorted Matrix",
        wing_id="binary-search-greedy", floor=455, difficulty="medium", visualizer_type="grid",
        monster_name="Matrix Behemoth", monster_title="Keeper of Row-Col Monotonicity",
        monster_sprite="boss", monster_color="#ec4899", monster_attack="Matrix Stampede",
        monster_quote="K-th smallest value in 2D sorted matrix found in logarithmic range time!",
        description="Given an `n x n` matrix where each row and column is sorted in ascending order, return the `k`-th smallest element in the matrix.",
        examples=[{"input": "matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8", "output": "13"}, {"input": "matrix = [[-5]], k = 1", "output": "-5"}],
        constraints=["n == matrix.length", "1 <= n <= 300", "1 <= k <= n^2"],
        function_name="kthSmallest",
        starter_code="def kthSmallest(matrix: list[list[int]], k: int) -> int:\n    pass\n",
        solution_code="def kthSmallest(matrix: list[list[int]], k: int) -> int:\n    n = len(matrix)\n    lo, hi = matrix[0][0], matrix[n - 1][n - 1]\n    def count_less_equal(mid):\n        count = 0\n        c = n - 1\n        for r in range(n):\n            while c >= 0 and matrix[r][c] > mid: c -= 1\n            count += (c + 1)\n        return count\n    while lo < hi:\n        mid = (lo + hi) // 2\n        if count_less_equal(mid) < k:\n            lo = mid + 1\n        else:\n            hi = mid\n    return lo\n",
        test_cases=[{"input": [[[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8], "expected": 13}, {"input": [[[-5]], 1], "expected": -5}],
        hints=["Binary search on value range [matrix[0][0], matrix[n-1][n-1]]. Count elements <= mid in O(n)."],
        leetcode_id=378
    ))

    return problems
