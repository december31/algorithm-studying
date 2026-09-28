import sys

# Test all 18 Python reference solutions against test cases

tests_passed = 0
total_tests = 0

def test(name, actual, expected):
    global tests_passed, total_tests
    total_tests += 1
    if actual == expected:
        tests_passed += 1
        return True
    else:
        print(f"❌ FAIL {name}: expected {expected}, got {actual}")
        return False

# 1. Two Sum
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        comp = target - num
        if comp in seen:
            return [seen[comp], i]
        seen[num] = i
    return []

test("twoSum 1", twoSum([2, 7, 11, 15], 9), [0, 1])
test("twoSum 2", twoSum([3, 2, 4], 6), [1, 2])
test("twoSum 3", twoSum([3, 3], 6), [0, 1])

# 2. Container With Most Water
def maxArea(height):
    left, right = 0, len(height) - 1
    max_water = 0
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

test("maxArea 1", maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)
test("maxArea 2", maxArea([1, 1]), 1)
test("maxArea 3", maxArea([4, 3, 2, 1, 4]), 16)

# 3. Trapping Rain Water
def trap(height):
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water

test("trap 1", trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)
test("trap 2", trap([4, 2, 0, 3, 2, 5]), 9)
test("trap 3", trap([3, 0, 2, 0, 4]), 7)

# 4. Valid Parentheses
def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return len(stack) == 0

test("isValid 1", isValid("()[]{}"), True)
test("isValid 2", isValid("(]"), False)
test("isValid 3", isValid("{[]}"), True)

# 5. Daily Temperatures
def dailyTemperatures(temperatures):
    n = len(temperatures)
    res = [0] * n
    stack = []
    for i, temp in enumerate(temperatures):
        while stack and temp > temperatures[stack[-1]]:
            prev = stack.pop()
            res[prev] = i - prev
        stack.append(i)
    return res

test("dailyTemperatures 1", dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0])
test("dailyTemperatures 2", dailyTemperatures([30, 40, 50, 60]), [1, 1, 1, 0])
test("dailyTemperatures 3", dailyTemperatures([30, 60, 90]), [1, 1, 0])

# 6. Largest Rectangle in Histogram
def largestRectangleArea(heights):
    stack = []
    max_area = 0
    h_ext = heights + [0]
    for i, h in enumerate(h_ext):
        while stack and h < h_ext[stack[-1]]:
            height = h_ext[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area

test("largestRectangleArea 1", largestRectangleArea([2, 1, 5, 6, 2, 3]), 10)
test("largestRectangleArea 2", largestRectangleArea([2, 4]), 4)
test("largestRectangleArea 3", largestRectangleArea([1, 1, 1, 1]), 4)

# 7. Reverse Linked List
def reverseList(head):
    return head[::-1]

test("reverseList 1", reverseList([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
test("reverseList 2", reverseList([1, 2]), [2, 1])
test("reverseList 3", reverseList([]), [])

# 8. Linked List Cycle
def hasCycle(values, pos):
    if pos == -1 or len(values) == 0:
        return False
    return 0 <= pos < len(values)

test("hasCycle 1", hasCycle([3, 2, 0, -4], 1), True)
test("hasCycle 2", hasCycle([1, 2], 0), True)
test("hasCycle 3", hasCycle([1], -1), False)

# 9. Merge Two Sorted Lists
def mergeTwoLists(list1, list2):
    i, j = 0, 0
    merged = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

test("mergeTwoLists 1", mergeTwoLists([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4])
test("mergeTwoLists 2", mergeTwoLists([], []), [])
test("mergeTwoLists 3", mergeTwoLists([], [0]), [0])

# 10. Invert Binary Tree
def invertTree(root):
    if not root:
        return []
    res = []
    start, count = 0, 1
    while start < len(root):
        level = root[start:start + count]
        res.extend(level[::-1])
        start += count
        count *= 2
    return res

test("invertTree 1", invertTree([4, 2, 7, 1, 3, 6, 9]), [4, 7, 2, 9, 6, 3, 1])
test("invertTree 2", invertTree([2, 1, 3]), [2, 3, 1])
test("invertTree 3", invertTree([]), [])

# 11. Validate BST
def isValidBST(root):
    def validate(idx, low, high):
        if idx >= len(root) or root[idx] is None:
            return True
        val = root[idx]
        if low is not None and val <= low:
            return False
        if high is not None and val >= high:
            return False
        return validate(2 * idx + 1, low, val) and validate(2 * idx + 2, val, high)
    return validate(0, None, None)

test("isValidBST 1", isValidBST([2, 1, 3]), True)
test("isValidBST 2", isValidBST([5, 1, 4, None, None, 3, 6]), False)
test("isValidBST 3", isValidBST([10, 5, 15, None, None, 6, 20]), False)

# 12. Lowest Common Ancestor
def lowestCommonAncestor(root, p, q):
    curr = 0
    while curr < len(root) and root[curr] is not None:
        val = root[curr]
        if p < val and q < val:
            curr = 2 * curr + 1
        elif p > val and q > val:
            curr = 2 * curr + 2
        else:
            return val
    return root[0]

test("LCA 1", lowestCommonAncestor([6, 2, 8, 0, 4, 7, 9], 2, 8), 6)
test("LCA 2", lowestCommonAncestor([6, 2, 8, 0, 4, 7, 9], 2, 4), 2)
test("LCA 3", lowestCommonAncestor([2, 1, 3], 1, 3), 2)

# 13. Flood Fill
def floodFill(image, sr, sc, color):
    orig = image[sr][sc]
    if orig == color:
        return image
    m, n = len(image), len(image[0])
    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or image[r][c] != orig:
            return
        image[r][c] = color
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    dfs(sr, sc)
    return image

test("floodFill 1", floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2), [[2, 2, 2], [2, 2, 0], [2, 0, 1]])
test("floodFill 2", floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0), [[0, 0, 0], [0, 0, 0]])
test("floodFill 3", floodFill([[0, 0, 0], [0, 1, 1]], 1, 1, 1), [[0, 0, 0], [0, 1, 1]])

# 14. Number of Islands
def numIslands(grid):
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    count = 0
    def sink(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        sink(r + 1, c)
        sink(r - 1, c)
        sink(r, c + 1)
        sink(r, c - 1)
    for r in range(m):
        for c in range(n):
            if grid[r][c] == '1':
                count += 1
                sink(r, c)
    return count

test("numIslands 1", numIslands([["1","1","0"],["1","1","0"],["0","0","1"]]), 2)
test("numIslands 2", numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]), 1)
test("numIslands 3", numIslands([["0","0"],["0","0"]]), 0)

# 15. Shortest Path in Binary Matrix
from collections import deque

def shortestPathBinaryMatrix(grid):
    n = len(grid)
    if grid[0][0] != 0 or grid[n-1][n-1] != 0:
        return -1
    if n == 1:
        return 1
    queue = deque([(0, 0, 1)])
    grid[0][0] = 1
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    while queue:
        r, c, dist = queue.popleft()
        if r == n - 1 and c == n - 1:
            return dist
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                grid[nr][nc] = 1
                queue.append((nr, nc, dist + 1))
    return -1

test("shortestPath 1", shortestPathBinaryMatrix([[0, 1], [1, 0]]), 2)
test("shortestPath 2", shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]), 4)
test("shortestPath 3", shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]), -1)

# 16. Climbing Stairs
def climbStairs(n):
    if n <= 2:
        return n
    p2, p1 = 1, 2
    for _ in range(3, n + 1):
        p2, p1 = p1, p1 + p2
    return p1

test("climbStairs 1", climbStairs(2), 2)
test("climbStairs 2", climbStairs(3), 3)
test("climbStairs 3", climbStairs(5), 8)

# 17. Coin Change
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

test("coinChange 1", coinChange([1, 2, 5], 11), 3)
test("coinChange 2", coinChange([2], 3), -1)
test("coinChange 3", coinChange([1], 0), 0)

# 18. Longest Increasing Subsequence
def lengthOfLIS(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

test("lengthOfLIS 1", lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)
test("lengthOfLIS 2", lengthOfLIS([0, 1, 0, 3, 2, 3]), 4)
test("lengthOfLIS 3", lengthOfLIS([7, 7, 7, 7, 7]), 1)

# 19. Ancient Temple (Lights Out Puzzle)
def solveAncientTemple(n, grid):
    min_touches = float('inf')
    for target in (0, 1):
        for mask in range(1 << n):
            touch = [[0] * n for _ in range(n)]
            for c in range(n):
                if (mask >> c) & 1:
                    touch[0][c] = 1
            for r in range(n - 1):
                for c in range(n):
                    val = grid[r][c] ^ touch[r][c]
                    if c > 0: val ^= touch[r][c - 1]
                    if c + 1 < n: val ^= touch[r][c + 1]
                    if r > 0: val ^= touch[r - 1][c]
                    touch[r + 1][c] = val ^ target
            valid = True
            for c in range(n):
                val = grid[n - 1][c] ^ touch[n - 1][c]
                if c > 0: val ^= touch[n - 1][c - 1]
                if c + 1 < n: val ^= touch[n - 1][c + 1]
                if n > 1: val ^= touch[n - 2][c]
                if val != target:
                    valid = False
                    break
            if valid:
                min_touches = min(min_touches, sum(sum(row) for row in touch))
    return min_touches if min_touches != float('inf') else -1

# Floor 1 tests
test("solveAncientTemple F1 T1", solveAncientTemple(2, [[0, 1], [1, 0]]), 2)
test("solveAncientTemple F1 T2", solveAncientTemple(2, [[0, 0], [0, 0]]), 0)
test("solveAncientTemple F1 T3", solveAncientTemple(3, [[0, 1, 0], [1, 0, 1], [0, 1, 0]]), 4)

# Floor 2 tests
test("solveAncientTemple F2 T1", solveAncientTemple(4, [[0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 1, 0]]), 4)
test("solveAncientTemple F2 T2", solveAncientTemple(4, [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]), 0)
test("solveAncientTemple F2 T3", solveAncientTemple(4, [[1, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 1]]), 4)

# Floor 3 tests (Guardian Boss)
test("solveAncientTemple F3 T1", solveAncientTemple(2, [[0, 1], [1, 0]]), 2)
test("solveAncientTemple F3 T2", solveAncientTemple(3, [[1, 1, 1], [1, 0, 1], [1, 1, 1]]), 5)
test("solveAncientTemple F3 T3", solveAncientTemple(5, [[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]), -1)
test("solveAncientTemple F3 T4", solveAncientTemple(6, [
    [0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0]
]), 22)

print(f"\n🐍 Python Curriculum Verification: {tests_passed}/{total_tests} test cases passed!")
if tests_passed != total_tests:
    sys.exit(1)
