export interface PythonProblemCode {
  starterCode: string;
  solutionCode: string;
}

export const pythonCurriculum: Record<string, PythonProblemCode> = {
  // ==========================================
  // TOPIC 1: DATA STRUCTURES
  // ==========================================
  'two-sum': {
    starterCode: `def twoSum(nums, target):
    return []
`,
    solutionCode: `def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        comp = target - num
        if comp in seen:
            return [seen[comp], i]
        seen[num] = i
    return []
`,
  },
  'valid-parentheses': {
    starterCode: `def isValid(s):
    return True
`,
    solutionCode: `def isValid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack
`,
  },
  'contains-duplicate': {
    starterCode: `def containsDuplicate(nums):
    return False
`,
    solutionCode: `def containsDuplicate(nums):
    return len(set(nums)) != len(nums)
`,
  },
  'valid-anagram': {
    starterCode: `def isAnagram(s, t):
    return False
`,
    solutionCode: `def isAnagram(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in t:
        if c not in count or count[c] == 0:
            return False
        count[c] -= 1
    return True
`,
  },
  'first-unique-character': {
    starterCode: `def firstUniqChar(s):
    return -1
`,
    solutionCode: `def firstUniqChar(s):
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1
`,
  },
  'intersection-of-two-arrays': {
    starterCode: `def intersection(nums1, nums2):
    return []
`,
    solutionCode: `def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
`,
  },
  'remove-all-adjacent-duplicates': {
    starterCode: `def removeDuplicates(s):
    return ""
`,
    solutionCode: `def removeDuplicates(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)
`,
  },
  'missing-number': {
    starterCode: `def missingNumber(nums):
    return 0
`,
    solutionCode: `def missingNumber(nums):
    n = len(nums)
    return (n * (n + 1)) // 2 - sum(nums)
`,
  },
  'daily-temperatures': {
    starterCode: `def dailyTemperatures(temperatures):
    return [0] * len(temperatures)
`,
    solutionCode: `def dailyTemperatures(temperatures):
    n = len(temperatures)
    res = [0] * n
    stack = []
    for i, t in enumerate(temperatures):
        while stack and t > temperatures[stack[-1]]:
            prev = stack.pop()
            res[prev] = i - prev
        stack.append(i)
    return res
`,
  },
  'group-anagrams': {
    starterCode: `def groupAnagrams(strs):
    return []
`,
    solutionCode: `def groupAnagrams(strs):
    groups = {}
    for s in strs:
        key = "".join(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())
`,
  },
  'top-k-frequent-elements': {
    starterCode: `def topKFrequent(nums, k):
    return []
`,
    solutionCode: `def topKFrequent(nums, k):
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1
    buckets = [[] for _ in range(len(nums) + 1)]
    for n, freq in count.items():
        buckets[freq].append(n)
    res = []
    for i in range(len(buckets) - 1, 0, -1):
        for n in buckets[i]:
            res.append(n)
            if len(res) == k:
                return res
    return res
`,
  },
  'evaluate-reverse-polish-notation': {
    starterCode: `def evalRPN(tokens):
    return 0
`,
    solutionCode: `def evalRPN(tokens):
    stack = []
    for t in tokens:
        if t in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if t == "+": stack.append(a + b)
            elif t == "-": stack.append(a - b)
            elif t == "*": stack.append(a * b)
            elif t == "/": stack.append(int(a / b))
        else:
            stack.append(int(t))
    return stack[0]
`,
  },
  'validate-stack-sequences': {
    starterCode: `def validateStackSequences(pushed, popped):
    return False
`,
    solutionCode: `def validateStackSequences(pushed, popped):
    stack = []
    j = 0
    for x in pushed:
        stack.append(x)
        while stack and j < len(popped) and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    return j == len(popped)
`,
  },
  'lru-cache-simulation': {
    starterCode: `def getLruOrder(ops, cap):
    return []
`,
    solutionCode: `def getLruOrder(ops, cap):
    cache = {}
    for item in ops:
        if item in cache:
            del cache[item]
        elif len(cache) >= cap:
            oldest = next(iter(cache))
            del cache[oldest]
        cache[item] = True
    return list(reversed(list(cache.keys())))
`,
  },
  'largest-rectangle-in-histogram': {
    starterCode: `def largestRectangleArea(heights):
    return 0
`,
    solutionCode: `def largestRectangleArea(heights):
    stack = []
    max_area = 0
    ext = heights + [0]
    for i, h in enumerate(ext):
        while stack and h < ext[stack[-1]]:
            top_h = ext[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, top_h * w)
        stack.append(i)
    return max_area
`,
  },
  'sliding-window-maximum': {
    starterCode: `def maxSlidingWindow(nums, k):
    return []
`,
    solutionCode: `from collections import deque
def maxSlidingWindow(nums, k):
    q = deque()
    res = []
    for i, n in enumerate(nums):
        while q and q[0] <= i - k:
            q.popleft()
        while q and nums[q[-1]] <= n:
            q.pop()
        q.append(i)
        if i >= k - 1:
            res.append(nums[q[0]])
    return res
`,
  },
  'longest-valid-parentheses': {
    starterCode: `def longestValidParentheses(s):
    return 0
`,
    solutionCode: `def longestValidParentheses(s):
    stack = [-1]
    max_len = 0
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len
`,
  },

  // ==========================================
  // TOPIC 2: EXHAUSTIVE SEARCH & BACKTRACKING
  // ==========================================
  'binary-tree-paths': {
    starterCode: `def binaryTreePaths(root):
    return []
`,
    solutionCode: `def binaryTreePaths(root):
    if not root or root[0] is None:
        return []
    paths = []
    def dfs(idx, curr):
        if idx >= len(root) or root[idx] is None:
            return
        nxt = str(root[idx]) if not curr else curr + "->" + str(root[idx])
        left = 2 * idx + 1
        right = 2 * idx + 2
        is_leaf = (left >= len(root) or root[left] is None) and (right >= len(root) or root[right] is None)
        if is_leaf:
            paths.append(nxt)
            return
        dfs(left, nxt)
        dfs(right, nxt)
    dfs(0, "")
    return paths
`,
  },
  'sum-of-all-subset-xor-totals': {
    starterCode: `def subsetXORSum(nums):
    return 0
`,
    solutionCode: `def subsetXORSum(nums):
    total = 0
    def backtrack(idx, curr):
        nonlocal total
        if idx == len(nums):
            total += curr
            return
        backtrack(idx + 1, curr ^ nums[idx])
        backtrack(idx + 1, curr)
    backtrack(0, 0)
    return total
`,
  },
  'invert-binary-tree': {
    starterCode: `def invertTree(root):
    return []
`,
    solutionCode: `def invertTree(root):
    if not root:
        return []
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
    root_node = Node(root[0])
    q = [root_node]
    i = 1
    while q and i < len(root):
        curr = q.pop(0)
        if i < len(root) and root[i] is not None:
            curr.left = Node(root[i])
            q.append(curr.left)
        i += 1
        if i < len(root) and root[i] is not None:
            curr.right = Node(root[i])
            q.append(curr.right)
        i += 1
    def invert(node):
        if not node:
            return None
        node.left, node.right = invert(node.right), invert(node.left)
        return node
    invert(root_node)
    res = []
    q = [root_node]
    while q:
        curr = q.pop(0)
        if curr:
            res.append(curr.val)
            q.append(curr.left)
            q.append(curr.right)
    return res
`,
  },
  'path-sum': {
    starterCode: `def hasPathSum(root, targetSum):
    return False
`,
    solutionCode: `def hasPathSum(root, targetSum):
    if not root or root[0] is None:
        return False
    def dfs(idx, remain):
        if idx >= len(root) or root[idx] is None:
            return False
        curr = remain - root[idx]
        left = 2 * idx + 1
        right = 2 * idx + 2
        is_leaf = (left >= len(root) or root[left] is None) and (right >= len(root) or root[right] is None)
        if is_leaf:
            return curr == 0
        return dfs(left, curr) or dfs(right, curr)
    return dfs(0, targetSum)
`,
  },
  'maximum-depth-of-binary-tree': {
    starterCode: `def maxDepth(root):
    return 0
`,
    solutionCode: `def maxDepth(root):
    if not root or root[0] is None:
        return 0
    def get_depth(idx):
        if idx >= len(root) or root[idx] is None:
            return 0
        return 1 + max(get_depth(2 * idx + 1), get_depth(2 * idx + 2))
    return get_depth(0)
`,
  },
  'same-tree': {
    starterCode: `def isSameTree(p, q):
    return True
`,
    solutionCode: `def isSameTree(p, q):
    return p == q
`,
  },
  'binary-tree-inorder-traversal': {
    starterCode: `def inorderTraversal(root):
    return []
`,
    solutionCode: `def inorderTraversal(root):
    if not root or root[0] is None:
        return []
    res = []
    def traverse(idx):
        if idx >= len(root) or root[idx] is None:
            return
        traverse(2 * idx + 1)
        res.append(root[idx])
        traverse(2 * idx + 2)
    traverse(0)
    return res
`,
  },
  'subsets': {
    starterCode: `def subsets(nums):
    return []
`,
    solutionCode: `def subsets(nums):
    res = []
    def backtrack(start, curr):
        res.append(list(curr))
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
    backtrack(0, [])
    return res
`,
  },
  'permutations': {
    starterCode: `def permute(nums):
    return []
`,
    solutionCode: `def permute(nums):
    res = []
    used = [False] * len(nums)
    def backtrack(curr):
        if len(curr) == len(nums):
            res.append(list(curr))
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                curr.append(nums[i])
                backtrack(curr)
                curr.pop()
                used[i] = False
    backtrack([])
    return res
`,
  },
  'combination-sum': {
    starterCode: `def combinationSum(candidates, target):
    return []
`,
    solutionCode: `def combinationSum(candidates, target):
    candidates.sort()
    res = []
    def backtrack(start, remain, curr):
        if remain == 0:
            res.append(list(curr))
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remain:
                break
            curr.append(candidates[i])
            backtrack(i, remain - candidates[i], curr)
            curr.pop()
    backtrack(0, target, [])
    return res
`,
  },
  'combinations': {
    starterCode: `def combine(n, k):
    return []
`,
    solutionCode: `def combine(n, k):
    res = []
    def backtrack(start, curr):
        if len(curr) == k:
            res.append(list(curr))
            return
        for i in range(start, n + 1):
            curr.append(i)
            backtrack(i + 1, curr)
            curr.pop()
    backtrack(1, [])
    return res
`,
  },
  'generate-parentheses': {
    starterCode: `def generateParenthesis(n):
    return []
`,
    solutionCode: `def generateParenthesis(n):
    res = []
    def backtrack(open_c, close_c, curr):
        if len(curr) == 2 * n:
            res.append(curr)
            return
        if open_c < n:
            backtrack(open_c + 1, close_c, curr + "(")
        if close_c < open_c:
            backtrack(open_c, close_c + 1, curr + ")")
    backtrack(0, 0, "")
    return res
`,
  },
  'subsets-ii': {
    starterCode: `def subsetsWithDup(nums):
    return []
`,
    solutionCode: `def subsetsWithDup(nums):
    nums.sort()
    res = []
    def backtrack(start, curr):
        res.append(list(curr))
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
    backtrack(0, [])
    return res
`,
  },
  'word-search': {
    starterCode: `def exist(board, word):
    return False
`,
    solutionCode: `def exist(board, word):
    m, n = len(board), len(board[0])
    def dfs(r, c, idx):
        if idx == len(word):
            return True
        if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[idx]:
            return False
        temp = board[r][c]
        board[r][c] = "#"
        found = (dfs(r + 1, c, idx + 1) or
                 dfs(r - 1, c, idx + 1) or
                 dfs(r, c + 1, idx + 1) or
                 dfs(r, c - 1, idx + 1))
        board[r][c] = temp
        return found
    for r in range(m):
        for c in range(n):
            if dfs(r, c, 0):
                return True
    return False
`,
  },
  'n-queens': {
    starterCode: `def solveNQueens(n):
    return []
`,
    solutionCode: `def solveNQueens(n):
    res = []
    cols, diag1, diag2 = set(), set(), set()
    board = [["."] * n for _ in range(n)]
    def backtrack(r):
        if r == n:
            res.append(["".join(row) for row in board])
            return
        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)
            board[r][c] = "Q"
            backtrack(r + 1)
            board[r][c] = "."
            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)
    backtrack(0)
    return res
`,
  },
  'n-queens-ii': {
    starterCode: `def totalNQueens(n):
    return 0
`,
    solutionCode: `def totalNQueens(n):
    count = 0
    cols, diag1, diag2 = set(), set(), set()
    def backtrack(r):
        nonlocal count
        if r == n:
            count += 1
            return
        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)
            backtrack(r + 1)
            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)
    backtrack(0)
    return count
`,
  },
  'sudoku-solver': {
    starterCode: `def solveSudoku(board):
    return board
`,
    solutionCode: `def solveSudoku(board):
    def is_valid(r, c, ch):
        for i in range(9):
            if board[r][i] == ch or board[i][c] == ch:
                return False
            br, bc = 3 * (r // 3) + i // 3, 3 * (c // 3) + i % 3
            if board[br][bc] == ch:
                return False
        return True
    def solve():
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for d in "123456789":
                        if is_valid(r, c, d):
                            board[r][c] = d
                            if solve():
                                return True
                            board[r][c] = "."
                    return False
        return True
    solve()
    return board
`,
  },

  // ==========================================
  // TOPIC 3: GRAPHS (BFS, DFS & FLOOD FILL)
  // ==========================================
  'flood-fill': {
    starterCode: `def floodFill(image, sr, sc, color):
    return image
`,
    solutionCode: `def floodFill(image, sr, sc, color):
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
`,
  },
  'island-perimeter': {
    starterCode: `def islandPerimeter(grid):
    return 0
`,
    solutionCode: `def islandPerimeter(grid):
    m, n = len(grid), len(grid[0])
    perimeter = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                perimeter += 4
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2
    return perimeter
`,
  },
  'find-if-path-exists-in-graph': {
    starterCode: `def validPath(n, edges, source, destination):
    return False
`,
    solutionCode: `from collections import deque
def validPath(n, edges, source, destination):
    if source == destination:
        return True
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    visited = {source}
    q = deque([source])
    while q:
        curr = q.popleft()
        if curr == destination:
            return True
        for nxt in adj[curr]:
            if nxt not in visited:
                visited.add(nxt)
                q.append(nxt)
    return False
`,
  },
  'average-of-levels-in-binary-tree': {
    starterCode: `def averageOfLevels(root):
    return []
`,
    solutionCode: `from collections import deque
def averageOfLevels(root):
    if not root or root[0] is None:
        return []
    res = []
    q = deque([0])
    while q:
        size = len(q)
        total = 0
        for _ in range(size):
            idx = q.popleft()
            total += root[idx]
            left, right = 2 * idx + 1, 2 * idx + 2
            if left < len(root) and root[left] is not None:
                q.append(left)
            if right < len(root) and root[right] is not None:
                q.append(right)
        res.append(round(total / size, 5))
    return res
`,
  },
  'univalued-binary-tree': {
    starterCode: `def isUnivalTree(root):
    return True
`,
    solutionCode: `def isUnivalTree(root):
    if not root or root[0] is None:
        return True
    val = root[0]
    return all(x is None or x == val for x in root)
`,
  },
  'cousins-in-binary-tree': {
    starterCode: `def isCousins(root, x, y):
    return False
`,
    solutionCode: `def isCousins(root, x, y):
    x_info, y_info = None, None
    def dfs(idx, depth, parent):
        nonlocal x_info, y_info
        if idx >= len(root) or root[idx] is None:
            return
        v = root[idx]
        if v == x: x_info = (depth, parent)
        if v == y: y_info = (depth, parent)
        dfs(2 * idx + 1, depth + 1, v)
        dfs(2 * idx + 2, depth + 1, v)
    dfs(0, 0, None)
    return x_info and y_info and x_info[0] == y_info[0] and x_info[1] != y_info[1]
`,
  },
  'number-of-islands': {
    starterCode: `def numIslands(grid):
    return 0
`,
    solutionCode: `def numIslands(grid):
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])
    count = 0
    def sink(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        sink(r + 1, c)
        sink(r - 1, c)
        sink(r, c + 1)
        sink(r, c - 1)
    for r in range(m):
        for c in range(n):
            if grid[r][c] == "1":
                count += 1
                sink(r, c)
    return count
`,
  },
  'rotting-oranges': {
    starterCode: `def orangesRotting(grid):
    return 0
`,
    solutionCode: `from collections import deque
def orangesRotting(grid):
    m, n = len(grid), len(grid[0])
    fresh = 0
    q = deque()
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 2:
                q.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1
    minutes = 0
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while q:
        r, c, t = q.popleft()
        minutes = max(minutes, t)
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                q.append((nr, nc, t + 1))
    return minutes if fresh == 0 else -1
`,
  },
  'max-area-of-island': {
    starterCode: `def maxAreaOfIsland(grid):
    return 0
`,
    solutionCode: `def maxAreaOfIsland(grid):
    m, n = len(grid), len(grid[0])
    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
            return 0
        grid[r][c] = 0
        return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
    max_area = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                max_area = max(max_area, dfs(r, c))
    return max_area
`,
  },
  'shortest-path-in-binary-matrix': {
    starterCode: `def shortestPathBinaryMatrix(grid):
    return -1
`,
    solutionCode: `from collections import deque
def shortestPathBinaryMatrix(grid):
    n = len(grid)
    if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
        return -1
    if n == 1:
        return 1
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    q = deque([(0, 0, 1)])
    grid[0][0] = 1
    while q:
        r, c, dist = q.popleft()
        if r == n - 1 and c == n - 1:
            return dist
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                grid[nr][nc] = 1
                q.append((nr, nc, dist + 1))
    return -1
`,
  },
  'course-schedule': {
    starterCode: `def canFinish(numCourses, prerequisites):
    return True
`,
    solutionCode: `from collections import deque
def canFinish(numCourses, prerequisites):
    in_degree = [0] * numCourses
    adj = [[] for _ in range(numCourses)]
    for course, pre in prerequisites:
        adj[pre].append(course)
        in_degree[course] += 1
    q = deque([i for i in range(numCourses) if in_degree[i] == 0])
    count = 0
    while q:
        curr = q.popleft()
        count += 1
        for nxt in adj[curr]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                q.append(nxt)
    return count == numCourses
`,
  },
  'clone-graph': {
    starterCode: `def cloneGraph(adjList):
    return adjList
`,
    solutionCode: `def cloneGraph(adjList):
    if not adjList:
        return []
    return [list(neighbors) for neighbors in adjList]
`,
  },
  'word-ladder': {
    starterCode: `def ladderLength(beginWord, endWord, wordList):
    return 0
`,
    solutionCode: `from collections import deque
def ladderLength(beginWord, endWord, wordList):
    words = set(wordList)
    if endWord not in words:
        return 0
    q = deque([(beginWord, 1)])
    visited = {beginWord}
    while q:
        curr, level = q.popleft()
        if curr == endWord:
            return level
        for i in range(len(curr)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                nxt = curr[:i] + c + curr[i+1:]
                if nxt in words and nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, level + 1))
    return 0
`,
  },
  'making-a-large-island': {
    starterCode: `def largestIsland(grid):
    return 0
`,
    solutionCode: `def largestIsland(grid):
    n = len(grid)
    island_id = 2
    area_map = {}
    def dfs(r, c, i_id):
        if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
            return 0
        grid[r][c] = i_id
        return 1 + dfs(r + 1, c, i_id) + dfs(r - 1, c, i_id) + dfs(r, c + 1, i_id) + dfs(r, c - 1, i_id)
    max_area = 0
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                area_map[island_id] = dfs(r, c, island_id)
                max_area = max(max_area, area_map[island_id])
                island_id += 1
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0:
                neighbors = set()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                        neighbors.add(grid[nr][nc])
                total = 1 + sum(area_map[nid] for nid in neighbors)
                max_area = max(max_area, total)
    return max_area
`,
  },
  'sliding-puzzle': {
    starterCode: `def slidingPuzzle(board):
    return -1
`,
    solutionCode: `from collections import deque
def slidingPuzzle(board):
    target = "123450"
    start = "".join(str(n) for row in board for n in row)
    if start == target:
        return 0
    neighbors = {
        0: [1, 3],
        1: [0, 2, 4],
        2: [1, 5],
        3: [0, 4],
        4: [1, 3, 5],
        5: [2, 4]
    }
    q = deque([(start, 0)])
    visited = {start}
    while q:
        state, moves = q.popleft()
        if state == target:
            return moves
        z = state.index("0")
        for nxt in neighbors[z]:
            arr = list(state)
            arr[z], arr[nxt] = arr[nxt], arr[z]
            n_state = "".join(arr)
            if n_state not in visited:
                visited.add(n_state)
                q.append((n_state, moves + 1))
    return -1
`,
  },

  // ==========================================
  // TOPIC 4: BINARY SEARCH & GREEDY
  // ==========================================
  'binary-search': {
    starterCode: `def search(nums, target):
    return -1
`,
    solutionCode: `def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
`,
  },
  'best-time-to-buy-and-sell-stock': {
    starterCode: `def maxProfit(prices):
    return 0
`,
    solutionCode: `def maxProfit(prices):
    min_price = float("inf")
    max_p = 0
    for p in prices:
        if p < min_price:
            min_price = p
        elif p - min_price > max_p:
            max_p = p - min_price
    return max_p
`,
  },
  'search-insert-position': {
    starterCode: `def searchInsert(nums, target):
    return 0
`,
    solutionCode: `def searchInsert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left
`,
  },
  'sqrt-x': {
    starterCode: `def mySqrt(x):
    return 0
`,
    solutionCode: `def mySqrt(x):
    if x < 2:
        return x
    left, right = 1, x // 2
    ans = 1
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans
`,
  },
  'assign-cookies': {
    starterCode: `def findContentChildren(g, s):
    return 0
`,
    solutionCode: `def findContentChildren(g, s):
    g.sort()
    s.sort()
    child, cookie = 0, 0
    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:
            child += 1
        cookie += 1
    return child
`,
  },
  'lemonade-change': {
    starterCode: `def lemonadeChange(bills):
    return True
`,
    solutionCode: `def lemonadeChange(bills):
    five, ten = 0, 0
    for b in bills:
        if b == 5:
            five += 1
        elif b == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1
        else:
            if ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True
`,
  },
  'find-the-highest-altitude': {
    starterCode: `def largestAltitude(gain):
    return 0
`,
    solutionCode: `def largestAltitude(gain):
    max_alt = 0
    curr = 0
    for g in gain:
        curr += g
        max_alt = max(max_alt, curr)
    return max_alt
`,
  },
  'search-in-rotated-sorted-array': {
    starterCode: `def searchRotated(nums, target):
    return -1
`,
    solutionCode: `def searchRotated(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
`,
  },
  'find-first-and-last-position': {
    starterCode: `def searchRange(nums, target):
    return [-1, -1]
`,
    solutionCode: `def searchRange(nums, target):
    def find_bound(first):
        left, right = 0, len(nums) - 1
        bound = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                bound = mid
                if first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return bound
    return [find_bound(True), find_bound(False)]
`,
  },
  'jump-game': {
    starterCode: `def canJump(nums):
    return False
`,
    solutionCode: `def canJump(nums):
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
        if max_reach >= len(nums) - 1:
            return True
    return True
`,
  },
  'merge-intervals': {
    starterCode: `def mergeIntervals(intervals):
    return []
`,
    solutionCode: `def mergeIntervals(intervals):
    if len(intervals) <= 1:
        return intervals
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]
    for curr in intervals[1:]:
        if curr[0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1], curr[1])
        else:
            res.append(curr)
    return res
`,
  },
  'non-overlapping-intervals': {
    starterCode: `def eraseOverlapIntervals(intervals):
    return 0
`,
    solutionCode: `def eraseOverlapIntervals(intervals):
    if len(intervals) <= 1:
        return 0
    intervals.sort(key=lambda x: x[1])
    removed = 0
    prev_end = intervals[0][1]
    for curr in intervals[1:]:
        if curr[0] < prev_end:
            removed += 1
        else:
            prev_end = curr[1]
    return removed
`,
  },
  'find-peak-element': {
    starterCode: `def findPeakElement(nums):
    return 0
`,
    solutionCode: `def findPeakElement(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left
`,
  },
  'find-minimum-in-rotated-sorted-array': {
    starterCode: `def findMin(nums):
    return 0
`,
    solutionCode: `def findMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]
`,
  },
  'split-array-largest-sum': {
    starterCode: `def splitArray(nums, k):
    return 0
`,
    solutionCode: `def splitArray(nums, k):
    left = max(nums)
    right = sum(nums)
    def can_split(max_s):
        pieces, curr = 1, 0
        for n in nums:
            if curr + n > max_s:
                pieces += 1
                curr = n
            else:
                curr += n
        return pieces <= k
    ans = right
    while left <= right:
        mid = (left + right) // 2
        if can_split(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans
`,
  },
  'candy': {
    starterCode: `def candy(ratings):
    return 0
`,
    solutionCode: `def candy(ratings):
    n = len(ratings)
    candies = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    return sum(candies)
`,
  },
  'median-of-two-sorted-arrays': {
    starterCode: `def findMedianSortedArrays(nums1, nums2):
    return 0.0
`,
    solutionCode: `def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        return findMedianSortedArrays(nums2, nums1)
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    while left <= right:
        p1 = (left + right) // 2
        p2 = (m + n + 1) // 2 - p1
        max_left1 = float("-inf") if p1 == 0 else nums1[p1 - 1]
        min_right1 = float("inf") if p1 == m else nums1[p1]
        max_left2 = float("-inf") if p2 == 0 else nums2[p2 - 1]
        min_right2 = float("inf") if p2 == n else nums2[p2]
        if max_left1 <= min_right2 and max_left2 <= min_right1:
            if (m + n) % 2 == 0:
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
            else:
                return float(max(max_left1, max_left2))
        elif max_left1 > min_right2:
            right = p1 - 1
        else:
            left = p1 + 1
    return 0.0
`,
  },

  // ==========================================
  // TOPIC 5: BIT MANIPULATION
  // ==========================================
  'single-number': {
    starterCode: `def singleNumber(nums):
    return 0
`,
    solutionCode: `def singleNumber(nums):
    res = 0
    for n in nums:
        res ^= n
    return res
`,
  },
  'number-of-1-bits': {
    starterCode: `def hammingWeight(n):
    return 0
`,
    solutionCode: `def hammingWeight(n):
    count = 0
    while n:
        n &= (n - 1)
        count += 1
    return count
`,
  },
  'counting-bits': {
    starterCode: `def countBits(n):
    return []
`,
    solutionCode: `def countBits(n):
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans
`,
  },
  'reverse-bits': {
    starterCode: `def reverseBits(n):
    return 0
`,
    solutionCode: `def reverseBits(n):
    res = 0
    for _ in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1
    return res
`,
  },
  'power-of-two': {
    starterCode: `def isPowerOfTwo(n):
    return False
`,
    solutionCode: `def isPowerOfTwo(n):
    return n > 0 and (n & (n - 1)) == 0
`,
  },
  'hamming-distance': {
    starterCode: `def hammingDistance(x, y):
    return 0
`,
    solutionCode: `def hammingDistance(x, y):
    xor = x ^ y
    count = 0
    while xor:
        xor &= (xor - 1)
        count += 1
    return count
`,
  },
  'number-complement': {
    starterCode: `def findComplement(num):
    return 0
`,
    solutionCode: `def findComplement(num):
    mask = 1
    while mask < num:
        mask = (mask << 1) | 1
    return num ^ mask
`,
  },
  'missing-number-bit': {
    starterCode: `def missingNumberBit(nums):
    return 0
`,
    solutionCode: `def missingNumberBit(nums):
    xor = len(nums)
    for i, n in enumerate(nums):
        xor ^= i ^ n
    return xor
`,
  },
  'single-number-iii': {
    starterCode: `def singleNumberIII(nums):
    return []
`,
    solutionCode: `def singleNumberIII(nums):
    diff = 0
    for n in nums:
        diff ^= n
    diff_bit = diff & (-diff)
    a, b = 0, 0
    for n in nums:
        if n & diff_bit:
            a ^= n
        else:
            b ^= n
    return [a, b] if a < b else [b, a]
`,
  },
  'single-number-ii': {
    starterCode: `def singleNumberII(nums):
    return 0
`,
    solutionCode: `def singleNumberII(nums):
    ones, twos = 0, 0
    for n in nums:
        ones = (ones ^ n) & ~twos
        twos = (twos ^ n) & ~ones
    return ones
`,
  },
  'bitwise-and-of-numbers-range': {
    starterCode: `def rangeBitwiseAnd(left, right):
    return 0
`,
    solutionCode: `def rangeBitwiseAnd(left, right):
    shift = 0
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    return left << shift
`,
  },
  'sum-of-two-integers': {
    starterCode: `def getSum(a, b):
    return 0
`,
    solutionCode: `def getSum(a, b):
    mask = 0xFFFFFFFF
    while (b & mask) > 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    return (a & mask) if b > 0 else a
`,
  },
  'xor-queries-of-a-subarray': {
    starterCode: `def xorQueries(arr, queries):
    return []
`,
    solutionCode: `def xorQueries(arr, queries):
    prefix = [0] * (len(arr) + 1)
    for i, n in enumerate(arr):
        prefix[i + 1] = prefix[i] ^ n
    return [prefix[r + 1] ^ prefix[l] for l, r in queries]
`,
  },
  'longest-subarray-with-maximum-bitwise-and': {
    starterCode: `def longestSubarray(nums):
    return 0
`,
    solutionCode: `def longestSubarray(nums):
    max_val = max(nums)
    max_len = 0
    curr_len = 0
    for n in nums:
        if n == max_val:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 0
    return max_len
`,
  },
  'shortest-path-visiting-all-nodes': {
    starterCode: `def shortestPathLength(graph):
    return 0
`,
    solutionCode: `from collections import deque
def shortestPathLength(graph):
    n = len(graph)
    if n <= 1:
        return 0
    target = (1 << n) - 1
    q = deque()
    visited = set()
    for i in range(n):
        mask = 1 << i
        q.append((i, mask, 0))
        visited.add((i, mask))
    while q:
        u, mask, dist = q.popleft()
        if mask == target:
            return dist
        for v in graph[u]:
            next_mask = mask | (1 << v)
            if (v, next_mask) not in visited:
                visited.add((v, next_mask))
                q.append((v, next_mask, dist + 1))
    return 0
`,
  },
  'triplets-with-bitwise-and-equal-to-zero': {
    starterCode: `def countTriplets(nums):
    return 0
`,
    solutionCode: `def countTriplets(nums):
    pair_count = [0] * (1 << 16)
    for a in nums:
        for b in nums:
            pair_count[a & b] += 1
    ans = 0
    for c in nums:
        for pair in range(1 << 16):
            if (c & pair) == 0:
                ans += pair_count[pair]
    return ans
`,
  },
  'minimum-one-bit-operations': {
    starterCode: `def minimumOneBitOperations(n):
    return 0
`,
    solutionCode: `def minimumOneBitOperations(n):
    ans = 0
    while n > 0:
        ans ^= n
        n >>= 1
    return ans
`,
  },
};
