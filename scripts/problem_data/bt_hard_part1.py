"""
Backtracking Hard Problems (30 Problems).
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.problem_data.common import make_problem


def get_bt_hard():
    problems = []

    # 71. N-Queens
    problems.append(make_problem(
        pid="bt-h-n-queens", title="N-Queens Full Boards",
        wing_id="backtracking", floor=271, difficulty="hard", visualizer_type="array",
        monster_name="Regal Gorgon", monster_title="Empress of the Non-Attacking 8-Directions",
        monster_sprite="lich", monster_color="#ec4899", monster_attack="Royal Annihilation",
        monster_quote="All non-attacking queen configurations placed across rows and diagonals!",
        description="The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other. Return all distinct solutions to the n-queens puzzle. Each solution contains a distinct board configuration, where `'Q'` and `'.'` both indicate a queen and an empty space respectively.",
        examples=[{"input": "n = 4", "output": "[[\".Q..\",\"...Q\",\"Q...\",\"..Q.\"],[\"..Q.\",\"Q...\",\"...Q\",\".Q..\"]]"}],
        constraints=["1 <= n <= 9"],
        function_name="solveNQueens",
        starter_code="def solveNQueens(n: int) -> list[list[str]]:\n    pass\n",
        solution_code="def solveNQueens(n: int) -> list[list[str]]:\n    res = []\n    cols = set()\n    diag1 = set()\n    diag2 = set()\n    def backtrack(r, state):\n        if r == n:\n            board = []\n            for c in state:\n                board.append('.' * c + 'Q' + '.' * (n - c - 1))\n            res.append(board)\n            return\n        for c in range(n):\n            if c not in cols and (r - c) not in diag1 and (r + c) not in diag2:\n                cols.add(c)\n                diag1.add(r - c)\n                diag2.add(r + c)\n                backtrack(r + 1, state + [c])\n                cols.remove(c)\n                diag1.remove(r - c)\n                diag2.remove(r + c)\n    backtrack(0, [])\n    return res\n",
        test_cases=[{"input": [4], "expected": [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]}, {"input": [1], "expected": [["Q"]]}],
        hints=["Place row by row. Track occupied columns, main diagonals (r - c), and anti-diagonals (r + c)."],
        leetcode_id=51
    ))

    # 72. N-Queens II
    problems.append(make_problem(
        pid="bt-h-n-queens-ii", title="N-Queens II (Solution Count)",
        wing_id="backtracking", floor=272, difficulty="hard", visualizer_type="array",
        monster_name="Matriarch Spectre", monster_title="Counter of Peaceful Sovereign Formations",
        monster_sprite="wraith", monster_color="#8b5cf6", monster_attack="Sovereign Ray",
        monster_quote="The total count of valid N-Queens states was calculated!",
        description="The n-queens puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other. Given an integer `n`, return the number of distinct solutions to the n-queens puzzle.",
        examples=[{"input": "n = 4", "output": "2"}, {"input": "n = 1", "output": "1"}],
        constraints=["1 <= n <= 9"],
        function_name="totalNQueens",
        starter_code="def totalNQueens(n: int) -> int:\n    pass\n",
        solution_code="def totalNQueens(n: int) -> int:\n    count = 0\n    cols = set()\n    diag1 = set()\n    diag2 = set()\n    def backtrack(r):\n        nonlocal count\n        if r == n:\n            count += 1\n            return\n        for c in range(n):\n            if c not in cols and (r - c) not in diag1 and (r + c) not in diag2:\n                cols.add(c)\n                diag1.add(r - c)\n                diag2.add(r + c)\n                backtrack(r + 1)\n                cols.remove(c)\n                diag1.remove(r - c)\n                diag2.remove(r + c)\n    backtrack(0)\n    return count\n",
        test_cases=[{"input": [4], "expected": 2}, {"input": [1], "expected": 1}, {"input": [5], "expected": 10}],
        hints=["Exact same backtracking logic as N-Queens I, but incrementing count on terminal condition."],
        leetcode_id=52
    ))

    # 73. Sudoku Solver
    problems.append(make_problem(
        pid="bt-h-sudoku-solver", title="Sudoku Solver",
        wing_id="backtracking", floor=273, difficulty="hard", visualizer_type="array",
        monster_name="Arch-Sudoku Demon", monster_title="Grand Master of the 81 Tiles",
        monster_sprite="demon", monster_color="#ef4444", monster_attack="Matrix Annihilation",
        monster_quote="Every empty tile filled adhering strictly to row, column, and block uniqueness!",
        description="Write a program to solve a Sudoku puzzle by filling the empty cells. Empty cells are indicated by character `'.'`. Return the solved 9x9 board.",
        examples=[{"input": "board = [[\"5\",\"3\",\".\",\".\",\"7\",\".\",\".\",\".\",\".\"],[\"6\",\".\",\".\",\"1\",\"9\",\"5\",\".\",\".\",\".\"],[\".\",\"9\",\"8\",\".\",\".\",\".\",\".\",\"6\",\".\"],[\"8\",\".\",\".\",\".\",\"6\",\".\",\".\",\".\",\"3\"],[\"4\",\".\",\".\",\"8\",\".\",\"3\",\".\",\".\",\"1\"],[\"7\",\".\",\".\",\".\",\"2\",\".\",\".\",\".\",\"6\"],[\".\",\"6\",\".\",\".\",\".\",\".\",\"2\",\"8\",\".\"],[\".\",\".\",\".\",\"4\",\"1\",\"9\",\".\",\".\",\"5\"],[\".\",\".\",\".\",\".\",\"8\",\".\",\".\",\"7\",\"9\"]]", "output": "Solved 9x9 board"}],
        constraints=["board.length == 9", "board[i].length == 9"],
        function_name="solveSudoku",
        starter_code="def solveSudoku(board: list[list[str]]) -> list[list[str]]:\n    pass\n",
        solution_code="def solveSudoku(board: list[list[str]]) -> list[list[str]]:\n    def is_valid(r, c, ch):\n        for i in range(9):\n            if board[r][i] == ch or board[i][c] == ch: return False\n            if board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == ch: return False\n        return True\n    def solve():\n        for r in range(9):\n            for c in range(9):\n                if board[r][c] == '.':\n                    for d in '123456789':\n                        if is_valid(r, c, d):\n                            board[r][c] = d\n                            if solve(): return True\n                            board[r][c] = '.'\n                    return False\n        return True\n    solve()\n    return board\n",
        test_cases=[{"input": [[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."], [".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]], "expected": [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]}],
        hints=["Find first empty cell. Try '1'-'9' and backtrack on dead ends."],
        leetcode_id=37
    ))

    # 74. Word Search II (Trie Search)
    problems.append(make_problem(
        pid="bt-h-word-search-ii", title="Word Search II (Grid Trie Traversal)",
        wing_id="backtracking", floor=274, difficulty="hard", visualizer_type="graph",
        monster_name="Trie Gorgon", monster_title="Seeker of Multi-Word Vocabulary",
        monster_sprite="lich", monster_color="#06b6d4", monster_attack="Vocabulary Wave",
        monster_quote="Prefix Trie pruning found all matching dictionary words!",
        description="Given an `m x n` `board` of characters and a list of strings `words`, return all words on the board in sorted order.",
        examples=[{"input": "board = [[\"o\",\"a\",\"a\",\"n\"],[\"e\",\"t\",\"a\",\"e\"],[\"i\",\"h\",\"k\",\"r\"],[\"i\",\"f\",\"l\",\"v\"]], words = [\"oath\",\"pea\",\"eat\",\"rain\"]", "output": "[\"eat\",\"oath\"]"}],
        constraints=["1 <= len(board), len(board[0]) <= 12", "1 <= len(words) <= 300"],
        function_name="findWordsInGrid",
        starter_code="def findWordsInGrid(board: list[list[str]], words: list[str]) -> list[str]:\n    pass\n",
        solution_code="def findWordsInGrid(board: list[list[str]], words: list[str]) -> list[str]:\n    trie = {}\n    for w in words:\n        node = trie\n        for ch in w:\n            node = node.setdefault(ch, {})\n        node['#'] = w\n    m, n = len(board), len(board[0])\n    found = set()\n    def dfs(r, c, node):\n        ch = board[r][c]\n        if ch not in node: return\n        curr = node[ch]\n        if '#' in curr:\n            found.add(curr['#'])\n        board[r][c] = '*'\n        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:\n            nr, nc = r + dr, c + dc\n            if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != '*':\n                dfs(nr, nc, curr)\n        board[r][c] = ch\n    for i in range(m):\n        for j in range(n):\n            dfs(i, j, trie)\n    return sorted(list(found))\n",
        test_cases=[{"input": [[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]], ["oath", "pea", "eat", "rain"]], "expected": ["eat", "oath"]}, {"input": [[["a", "b"], ["c", "d"]], ["abcb"]], "expected": []}],
        hints=["Insert all words into a prefix trie, then DFS from each cell following trie branches."],
        leetcode_id=212
    ))

    # 75. Remove Invalid Parentheses
    problems.append(make_problem(
        pid="bt-h-remove-invalid-parentheses", title="Remove Invalid Parentheses",
        wing_id="backtracking", floor=275, difficulty="hard", visualizer_type="stack",
        monster_name="Balance Archon", monster_title="Pruner of Asymmetric Brackets",
        monster_sprite="beholder", monster_color="#10b981", monster_attack="Equilibrium Shock",
        monster_quote="Minimum removals to achieve valid parentheses generated!",
        description="Given a string `s` that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid. Return all unique possible results in sorted order.",
        examples=[{"input": "s = \"()())()\"", "output": "[\"(())\",\"()()()\"]"}, {"input": "s = \"(a)())()\"", "output": "[\"(a)()()\",\"(a())\"]"}],
        constraints=["1 <= len(s) <= 25"],
        function_name="removeInvalidParentheses",
        starter_code="def removeInvalidParentheses(s: str) -> list[str]:\n    pass\n",
        solution_code="def removeInvalidParentheses(s: str) -> list[str]:\n    def is_valid(sub):\n        cnt = 0\n        for ch in sub:\n            if ch == '(': cnt += 1\n            elif ch == ')':\n                cnt -= 1\n                if cnt < 0: return False\n        return cnt == 0\n    from collections import deque\n    queue = deque([s])\n    visited = {s}\n    found = False\n    res = []\n    while queue:\n        curr = queue.popleft()\n        if is_valid(curr):\n            res.append(curr)\n            found = True\n        if found: continue\n        for i in range(len(curr)):\n            if curr[i] not in '()': continue\n            nxt = curr[:i] + curr[i + 1:]\n            if nxt not in visited:\n                visited.add(nxt)\n                queue.append(nxt)\n    return sorted(res)\n",
        test_cases=[{"input": ["()())()"], "expected": ["(())()", "()()()"]}, {"input": ["(a)())()"], "expected": ["(a())()", "(a)()()"]}, {"input": [")("], "expected": [""]}],
        hints=["Breadth-First Search level by level guarantees minimum removals."],
        leetcode_id=301
    ))

    # 76. Wildcard Matching
    problems.append(make_problem(
        pid="bt-h-wildcard-matching", title="Wildcard Matching (* and ?)",
        wing_id="backtracking", floor=276, difficulty="hard", visualizer_type="array",
        monster_name="Wildcard Drake", monster_title="Morpher of Question Marks and Asterisks",
        monster_sprite="dragon", monster_color="#38bdf8", monster_attack="Wildcard Blast",
        monster_quote="Asterisk and question mark wildcard matches verified!",
        description="Given an input string (`s`) and a pattern (`p`), implement wildcard pattern matching with support for `'?'` (matches any single character) and `'*'` (matches any sequence of characters including empty).",
        examples=[{"input": "s = \"aa\", p = \"a\"", "output": "False"}, {"input": "s = \"aa\", p = \"*\"", "output": "True"}, {"input": "s = \"cb\", p = \"?a\"", "output": "False"}],
        constraints=["0 <= len(s), len(p) <= 2000"],
        function_name="isMatchWildcard",
        starter_code="def isMatchWildcard(s: str, p: str) -> bool:\n    pass\n",
        solution_code="def isMatchWildcard(s: str, p: str) -> bool:\n    s_ptr, p_ptr = 0, 0\n    star_idx = -1\n    match_idx = 0\n    while s_ptr < len(s):\n        if p_ptr < len(p) and (p[p_ptr] == '?' or p[p_ptr] == s[s_ptr]):\n            s_ptr += 1\n            p_ptr += 1\n        elif p_ptr < len(p) and p[p_ptr] == '*':\n            star_idx = p_ptr\n            match_idx = s_ptr\n            p_ptr += 1\n        elif star_idx != -1:\n            p_ptr = star_idx + 1\n            match_idx += 1\n            s_ptr = match_idx\n        else:\n            return False\n    while p_ptr < len(p) and p[p_ptr] == '*':\n        p_ptr += 1\n    return p_ptr == len(p)\n",
        test_cases=[{"input": ["aa", "a"], "expected": False}, {"input": ["aa", "*"], "expected": True}, {"input": ["cb", "?a"], "expected": False}, {"input": ["adceb", "*a*b"], "expected": True}],
        hints=["Two pointers with backtracking to the last seen '*' in O(n) average time."],
        leetcode_id=44
    ))

    # 77. Regular Expression Matching
    problems.append(make_problem(
        pid="bt-h-regular-expression-matching", title="Regular Expression Matching (. and *)",
        wing_id="backtracking", floor=277, difficulty="hard", visualizer_type="array",
        monster_name="Kleene Star Fiend", monster_title="Master of Zero-or-More Repeats",
        monster_sprite="demon", monster_color="#e11d48", monster_attack="Kleene Lash",
        monster_quote="Regex pattern matches validated with top-down memoization!",
        description="Given an input string `s` and a pattern `p`, implement regular expression matching with support for `'.'` (matches any single character) and `'*'` (matches zero or more of the preceding element).",
        examples=[{"input": "s = \"aa\", p = \"a*\"", "output": "True"}, {"input": "s = \"ab\", p = \".*\"", "output": "True"}, {"input": "s = \"aab\", p = \"c*a*b\"", "output": "True"}],
        constraints=["1 <= len(s), len(p) <= 30"],
        function_name="isMatchRegex",
        starter_code="def isMatchRegex(s: str, p: str) -> bool:\n    pass\n",
        solution_code="def isMatchRegex(s: str, p: str) -> bool:\n    memo = {}\n    def dp(i, j):\n        if (i, j) in memo: return memo[(i, j)]\n        if j == len(p): return i == len(s)\n        first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')\n        if j + 1 < len(p) and p[j + 1] == '*':\n            ans = dp(i, j + 2) or (first_match and dp(i + 1, j))\n        else:\n            ans = first_match and dp(i + 1, j + 1)\n        memo[(i, j)] = ans\n        return ans\n    return dp(0, 0)\n",
        test_cases=[{"input": ["aa", "a*"], "expected": True}, {"input": ["ab", ".*"], "expected": True}, {"input": ["aab", "c*a*b"], "expected": True}, {"input": ["mississippi", "mis*is*p*."], "expected": False}],
        hints=["Branch on '*': zero occurrences (skip 2 characters in pattern) or 1+ occurrences if first matches."],
        leetcode_id=10
    ))

    # 78. Unique Paths III
    problems.append(make_problem(
        pid="bt-h-unique-paths-iii", title="Unique Paths III (Visit Every Cell)",
        wing_id="backtracking", floor=278, difficulty="hard", visualizer_type="graph",
        monster_name="Hamiltonian Chimera", monster_title="Walker of Complete Grid Surfaces",
        monster_sprite="hydra", monster_color="#f59e0b", monster_attack="Hamiltonian Tail",
        monster_quote="Every empty square visited exactly once before the ending square!",
        description="You are given an `m x n` integer array `grid` where `1` represents starting square, `2` ending square, `0` empty squares, and `-1` obstacles. Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.",
        examples=[{"input": "grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]", "output": "2"}, {"input": "grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]", "output": "4"}],
        constraints=["1 <= len(grid), len(grid[0]) <= 20", "1 <= m * n <= 20"],
        function_name="uniquePathsIII",
        starter_code="def uniquePathsIII(grid: list[list[int]]) -> int:\n    pass\n",
        solution_code="def uniquePathsIII(grid: list[list[int]]) -> int:\n    m, n = len(grid), len(grid[0])\n    empty = 1\n    start = (0, 0)\n    for r in range(m):\n        for c in range(n):\n            if grid[r][c] == 0: empty += 1\n            elif grid[r][c] == 1: start = (r, c)\n    paths = 0\n    def dfs(r, c, remain):\n        nonlocal paths\n        if grid[r][c] == 2:\n            if remain == 0: paths += 1\n            return\n        temp = grid[r][c]\n        grid[r][c] = -1\n        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:\n            nr, nc = r + dr, c + dc\n            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != -1:\n                dfs(nr, nc, remain - 1)\n        grid[r][c] = temp\n    dfs(start[0], start[1], empty)\n    return paths\n",
        test_cases=[{"input": [[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]], "expected": 2}, {"input": [[[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]], "expected": 4}],
        hints=["Count empty squares upfront. Only increment path count when reaching '2' with remaining empty == 0."],
        leetcode_id=980
    ))

    # 79. Expression Add Operators
    problems.append(make_problem(
        pid="bt-h-expression-add-operators", title="Expression Add Operators",
        wing_id="backtracking", floor=279, difficulty="hard", visualizer_type="array",
        monster_name="Arithmetical Arch-Lich", monster_title="Injector of Precedence Glyphs",
        monster_sprite="lich", monster_color="#8b5cf6", monster_attack="Precedence Beam",
        monster_quote="Multiplication precedence tracking evaluated target expressions!",
        description="Given a string `num` that contains only digits and an integer `target`, return all possibilities to insert binary operators `'+'`, `'-'`, and/or `'*'` between the digits of `num` so that the resultant expression evaluates to the `target` value in sorted order.",
        examples=[{"input": "num = \"123\", target = 6", "output": "[\"1*2*3\",\"1+2+3\"]"}, {"input": "num = \"232\", target = 8", "output": "[\"2*3+2\",\"2+3*2\"]"}],
        constraints=["1 <= len(num) <= 10"],
        function_name="addOperators",
        starter_code="def addOperators(num: str, target: int) -> list[str]:\n    pass\n",
        solution_code="def addOperators(num: str, target: int) -> list[str]:\n    res = []\n    def backtrack(idx, prev_val, curr_val, path):\n        if idx == len(num):\n            if curr_val == target:\n                res.append(path)\n            return\n        for j in range(idx + 1, len(num) + 1):\n            if j > idx + 1 and num[idx] == '0': break\n            sub = num[idx:j]\n            val = int(sub)\n            if idx == 0:\n                backtrack(j, val, val, sub)\n            else:\n                backtrack(j, val, curr_val + val, path + '+' + sub)\n                backtrack(j, -val, curr_val - val, path + '-' + sub)\n                backtrack(j, prev_val * val, curr_val - prev_val + prev_val * val, path + '*' + sub)\n    backtrack(0, 0, 0, '')\n    return sorted(res)\n",
        test_cases=[{"input": ["123", 6], "expected": ["1*2*3", "1+2+3"]}, {"input": ["232", 8], "expected": ["2*3+2", "2+3*2"]}, {"input": ["105", 5], "expected": ["1*0+5", "10-5"]}],
        hints=["To handle multiplication precedence, pass prev_val and update curr_val - prev_val + prev_val * val."],
        leetcode_id=282
    ))

    # 80. 24 Game
    problems.append(make_problem(
        pid="bt-h-24-game", title="24 Game Solver",
        wing_id="backtracking", floor=280, difficulty="hard", visualizer_type="array",
        monster_name="Arithmancy Sphinx", monster_title="Enchanter of the Four Cards",
        monster_sprite="beholder", monster_color="#ec4899", monster_attack="24 Enigma",
        monster_quote="Parenthesization and 4 basic operations evaluated to 24!",
        description="You are given an integer array `cards` of length `4`. You have cards with values 1-9. You should arrange them such that using operators `+`, `-`, `*`, `/` and parentheses you get `24`. Division `/` is real division. Return `True` if you can get such an expression.",
        examples=[{"input": "cards = [4,1,8,7]", "output": "True"}, {"input": "cards = [1,2,1,2]", "output": "False"}],
        constraints=["len(cards) == 4", "1 <= cards[i] <= 9"],
        function_name="judgePoint24",
        starter_code="def judgePoint24(cards: list[int]) -> bool:\n    pass\n",
        solution_code="def judgePoint24(cards: list[int]) -> bool:\n    EPS = 1e-6\n    def dfs(nums):\n        if len(nums) == 1:\n            return abs(nums[0] - 24) < EPS\n        for i in range(len(nums)):\n            for j in range(len(nums)):\n                if i != j:\n                    next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]\n                    a, b = nums[i], nums[j]\n                    for res in [a + b, a - b, b - a, a * b]:\n                        if dfs(next_nums + [res]): return True\n                    if abs(b) > EPS and dfs(next_nums + [a / b]): return True\n                    if abs(a) > EPS and dfs(next_nums + [b / a]): return True\n        return False\n    return dfs([float(c) for c in cards])\n",
        test_cases=[{"input": [[4, 1, 8, 7]], "expected": True}, {"input": [[1, 2, 1, 2]], "expected": False}, {"input": [[3, 3, 8, 8]], "expected": True}],
        hints=["Pick any two numbers, replace them with one of their results, and recurse on the 3 remaining numbers."],
        leetcode_id=679
    ))

    # 81. Word Ladder II
    problems.append(make_problem(
        pid="bt-h-word-ladder-ii", title="Word Ladder II (All Shortest Chains)",
        wing_id="backtracking", floor=281, difficulty="hard", visualizer_type="graph",
        monster_name="Mutation Archon", monster_title="Lord of Minimum Transformation Sequences",
        monster_sprite="lich", monster_color="#06b6d4", monster_attack="Chain Mutation",
        monster_quote="BFS distance DAG followed by DFS backtracking found all shortest ladders!",
        description="A transformation sequence from `beginWord` to `endWord` using `wordList` is a sequence of words where each word differs by 1 character. Return all the shortest transformation sequences from `beginWord` to `endWord` in sorted order.",
        examples=[{"input": "beginWord = \"hit\", endWord = \"cog\", wordList = [\"hot\",\"dot\",\"dog\",\"lot\",\"log\",\"cog\"]", "output": "[[\"hit\",\"hot\",\"dot\",\"dog\",\"cog\"],[\"hit\",\"hot\",\"lot\",\"log\",\"cog\"]]"}],
        constraints=["1 <= len(beginWord) <= 5"],
        function_name="findLadders",
        starter_code="def findLadders(beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:\n    pass\n",
        solution_code="def findLadders(beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:\n    if endWord not in wordList: return []\n    from collections import defaultdict, deque\n    words = set(wordList)\n    level = {beginWord}\n    parents = defaultdict(set)\n    while level and endWord not in parents:\n        next_level = set()\n        words -= level\n        for word in level:\n            for i in range(len(word)):\n                for c in 'abcdefghijklmnopqrstuvwxyz':\n                    nxt = word[:i] + c + word[i+1:]\n                    if nxt in words:\n                        next_level.add(nxt)\n                        parents[nxt].add(word)\n        level = next_level\n    if endWord not in parents: return []\n    res = []\n    def dfs(curr, path):\n        if curr == beginWord:\n            res.append(path[::-1])\n            return\n        for p in parents[curr]:\n            dfs(p, path + [p])\n    dfs(endWord, [endWord])\n    res.sort()\n    return res\n",
        test_cases=[{"input": ["hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]], "expected": [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]}],
        hints=["Use BFS to record the parent DAG of shortest paths, then DFS backtrack from endWord to beginWord."],
        leetcode_id=126
    ))

    # 82. Number of Squareful Arrays
    problems.append(make_problem(
        pid="bt-h-number-of-squareful-arrays", title="Number of Squareful Arrays",
        wing_id="backtracking", floor=282, difficulty="hard", visualizer_type="array",
        monster_name="Perfect Square Wraith", monster_title="Harmonizer of Consecutive Quadratic Sums",
        monster_sprite="wraith", monster_color="#10b981", monster_attack="Square Shock",
        monster_quote="Adjacent sum square test passed for every permutation!",
        description="An array is squareful if the sum of every pair of adjacent elements is a perfect square. Given an integer array `nums`, return the number of unique permutations of `nums` that are squareful.",
        examples=[{"input": "nums = [1,17,8]", "output": "2"}, {"input": "nums = [2,2,2]", "output": "1"}],
        constraints=["1 <= len(nums) <= 12", "0 <= nums[i] <= 10^9"],
        function_name="numSquarefulPerms",
        starter_code="def numSquarefulPerms(nums: list[int]) -> int:\n    pass\n",
        solution_code="def numSquarefulPerms(nums: list[int]) -> int:\n    import math\n    def is_square(x):\n        s = int(math.isqrt(x))\n        return s * s == x\n    nums.sort()\n    used = [False] * len(nums)\n    count = 0\n    def backtrack(curr_val, length):\n        nonlocal count\n        if length == len(nums):\n            count += 1\n            return\n        for i in range(len(nums)):\n            if used[i]: continue\n            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]: continue\n            if curr_val is None or is_square(curr_val + nums[i]):\n                used[i] = True\n                backtrack(nums[i], length + 1)\n                used[i] = False\n    backtrack(None, 0)\n    return count\n",
        test_cases=[{"input": [[1, 17, 8]], "expected": 2}, {"input": [[2, 2, 2]], "expected": 1}],
        hints=["Sort nums to skip duplicates. Prune whenever curr + nums[i] is not a perfect square."],
        leetcode_id=996
    ))

    # 83. Can I Win (Minimax Game Theory)
    problems.append(make_problem(
        pid="bt-h-can-i-win", title="Can I Win (Minimax Backtracking)",
        wing_id="backtracking", floor=283, difficulty="hard", visualizer_type="bits",
        monster_name="Game-Tree Demon", monster_title="Grandmaster of Finite Sum Tournaments",
        monster_sprite="demon", monster_color="#e11d48", monster_attack="Minimax Stare",
        monster_quote="Minimax with bitmask memoization predicted the winning outcome!",
        description="In the '100 game', two players take turns choosing an integer from `1` to `maxChoosableInteger` without replacement, adding to a running total. The player who first causes the running total to reach or exceed `desiredTotal` wins. Return `True` if the first player can force a win.",
        examples=[{"input": "maxChoosableInteger = 10, desiredTotal = 11", "output": "False"}, {"input": "maxChoosableInteger = 10, desiredTotal = 0", "output": "True"}],
        constraints=["1 <= maxChoosableInteger <= 20", "0 <= desiredTotal <= 300"],
        function_name="canIWin",
        starter_code="def canIWin(maxChoosableInteger: int, desiredTotal: int) -> bool:\n    pass\n",
        solution_code="def canIWin(maxChoosableInteger: int, desiredTotal: int) -> bool:\n    if desiredTotal <= 0: return True\n    if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal: return False\n    memo = {}\n    def dfs(used_mask, rem):\n        if used_mask in memo: return memo[used_mask]\n        for i in range(1, maxChoosableInteger + 1):\n            mask = 1 << i\n            if not (used_mask & mask):\n                if i >= rem or not dfs(used_mask | mask, rem - i):\n                    memo[used_mask] = True\n                    return True\n        memo[used_mask] = False\n        return False\n    return dfs(0, desiredTotal)\n",
        test_cases=[{"input": [10, 11], "expected": False}, {"input": [10, 0], "expected": True}, {"input": [10, 1], "expected": True}],
        hints=["Use a bitmask to represent available integers and memoize (used_mask) state."],
        leetcode_id=292
    ))

    # 84. Palindrome Partitioning IV
    problems.append(make_problem(
        pid="bt-h-palindrome-partitioning-iv", title="Palindrome Partitioning IV (Exactly 3 Parts)",
        wing_id="backtracking", floor=284, difficulty="hard", visualizer_type="array",
        monster_name="Tri-Fold Sphinx", monster_title="Validator of 3 Palindromic Cuts",
        monster_sprite="beholder", monster_color="#ec4899", monster_attack="Tri-Fold Ray",
        monster_quote="String split into exactly 3 non-empty palindromic substrings!",
        description="Given a string `s`, return `True` if it is possible to split the string `s` into three non-empty palindromic substrings, or `False` otherwise.",
        examples=[{"input": "s = \"abcbdd\"", "output": "True"}, {"input": "s = \"bcbddxy\"", "output": "False"}],
        constraints=["3 <= len(s) <= 2000"],
        function_name="checkPartitioning",
        starter_code="def checkPartitioning(s: str) -> bool:\n    pass\n",
        solution_code="def checkPartitioning(s: str) -> bool:\n    n = len(s)\n    dp = [[False] * n for _ in range(n)]\n    for i in range(n - 1, -1, -1):\n        for j in range(i, n):\n            if s[i] == s[j]:\n                dp[i][j] = True if j - i <= 2 else dp[i + 1][j - 1]\n    for i in range(n - 2):\n        if dp[0][i]:\n            for j in range(i + 1, n - 1):\n                if dp[i + 1][j] and dp[j + 1][n - 1]:\n                    return True\n    return False\n",
        test_cases=[{"input": ["abcbdd"], "expected": True}, {"input": ["bcbddxy"], "expected": False}, {"input": ["aaa"], "expected": True}],
        hints=["Precompute 2D palindrome table in O(n^2), then iterate over the two cut indices i and j."],
        leetcode_id=1745
    ))

    # 85. Split Array With Same Average
    problems.append(make_problem(
        pid="bt-h-split-array-same-average", title="Split Array With Same Average",
        wing_id="backtracking", floor=285, difficulty="hard", visualizer_type="array",
        monster_name="Equi-Average Golem", monster_title="Balancer of Subset Means",
        monster_sprite="golem", monster_color="#f59e0b", monster_attack="Average Slam",
        monster_quote="Subsets A and B had identical averages!",
        description="You are given an integer array `nums`. You should move each element of `nums` into either the array `A` or the array `B` such that `A` and `B` are non-empty, and `average(A) == average(B)`. Return `True` if it is possible to achieve that and `False` otherwise.",
        examples=[{"input": "nums = [1,2,3,4,5,6,7,8]", "output": "True"}, {"input": "nums = [3,1]", "output": "False"}],
        constraints=["1 <= len(nums) <= 30", "0 <= nums[i] <= 10^4"],
        function_name="splitArraySameAverage",
        starter_code="def splitArraySameAverage(nums: list[int]) -> bool:\n    pass\n",
        solution_code="def splitArraySameAverage(nums: list[int]) -> bool:\n    n = len(nums)\n    total = sum(nums)\n    m = n // 2\n    # sum(A) / len(A) == total / n  => sum(A) = total * len(A) / n (must be integer)\n    possible = any((total * k) % n == 0 for k in range(1, m + 1))\n    if not possible: return False\n    dp = [set() for _ in range(m + 1)]\n    dp[0].add(0)\n    for num in nums:\n        for k in range(m, 0, -1):\n            for s in dp[k - 1]:\n                dp[k].add(s + num)\n    for k in range(1, m + 1):\n        if (total * k) % n == 0 and (total * k) // n in dp[k]:\n            return True\n    return False\n",
        test_cases=[{"input": [[1, 2, 3, 4, 5, 6, 7, 8]], "expected": True}, {"input": [[3, 1]], "expected": False}],
        hints=["sum(A) = (total * k) / n. Check if any subset of size k has this sum using set DP."],
        leetcode_id=805
    ))

    # 86. Minimum XOR Sum of Two Arrays
    problems.append(make_problem(
        pid="bt-h-minimum-xor-sum", title="Minimum XOR Sum of Two Arrays",
        wing_id="backtracking", floor=286, difficulty="hard", visualizer_type="bits",
        monster_name="XOR Pairing Archon", monster_title="Minimizer of Bitwise Mismatches",
        monster_sprite="demon", monster_color="#8b5cf6", monster_attack="Bitwise Pair Hex",
        monster_quote="Optimal bijection assignment minimized total XOR sum!",
        description="You are given two integer arrays `nums1` and `nums2` of length `n`. Rearrange the elements of `nums2` such that the sum of `(nums1[i] ^ nums2[i])` for all `0 <= i < n` is minimized. Return the minimum XOR sum.",
        examples=[{"input": "nums1 = [1,2], nums2 = [2,3]", "output": "2"}, {"input": "nums1 = [1,0,3], nums2 = [5,3,4]", "output": "8"}],
        constraints=["n == len(nums1) == len(nums2)", "1 <= n <= 14"],
        function_name="minimumXORSum",
        starter_code="def minimumXORSum(nums1: list[int], nums2: list[int]) -> int:\n    pass\n",
        solution_code="def minimumXORSum(nums1: list[int], nums2: list[int]) -> int:\n    n = len(nums1)\n    memo = {}\n    def dfs(i, mask):\n        if i == n: return 0\n        if mask in memo: return memo[mask]\n        ans = float('inf')\n        for j in range(n):\n            if not (mask & (1 << j)):\n                ans = min(ans, (nums1[i] ^ nums2[j]) + dfs(i + 1, mask | (1 << j)))\n        memo[mask] = ans\n        return ans\n    return dfs(0, 0)\n",
        test_cases=[{"input": [[1, 2], [2, 3]], "expected": 2}, {"input": [[1, 0, 3], [5, 3, 4]], "expected": 8}],
        hints=["Bitmask DP assigning elements of nums2 to positions of nums1."],
        leetcode_id=1879
    ))

    # 87. Distribute Repeating Integers
    problems.append(make_problem(
        pid="bt-h-distribute-repeating-integers", title="Distribute Repeating Integers",
        wing_id="backtracking", floor=287, difficulty="hard", visualizer_type="array",
        monster_name="Inventory Drake", monster_title="Fulfiller of Customer Batch Demands",
        monster_sprite="dragon", monster_color="#38bdf8", monster_attack="Batch Fire",
        monster_quote="Every customer requirement satisfied from single item frequency pools!",
        description="You are given an array of `n` integers, `nums`, where there are at most 50 unique values in the array. You are also given an array of `m` customer order quantities, `quantity`, where the `i-th` customer requires `quantity[i]` equal numbers. Return `True` if you can satisfy all customer orders.",
        examples=[{"input": "nums = [1,2,3,4], quantity = [2]", "output": "False"}, {"input": "nums = [1,2,3,3], quantity = [2]", "output": "True"}],
        constraints=["1 <= len(nums) <= 10^5", "1 <= len(quantity) <= 10"],
        function_name="canDistribute",
        starter_code="def canDistribute(nums: list[int], quantity: list[int]) -> bool:\n    pass\n",
        solution_code="def canDistribute(nums: list[int], quantity: list[int]) -> bool:\n    from collections import Counter\n    counts = sorted(Counter(nums).values(), reverse=True)\n    quantity.sort(reverse=True)\n    def backtrack(cust_idx):\n        if cust_idx == len(quantity): return True\n        for i in range(len(counts)):\n            if counts[i] >= quantity[cust_idx]:\n                counts[i] -= quantity[cust_idx]\n                if backtrack(cust_idx + 1): return True\n                counts[i] += quantity[cust_idx]\n            if counts[i] == 0: break\n        return False\n    return backtrack(0)\n",
        test_cases=[{"input": [[1, 2, 3, 4], [2]], "expected": False}, {"input": [[1, 2, 3, 3], [2]], "expected": True}],
        hints=["Sort both item counts and customer quantities in descending order to fail fast."],
        leetcode_id=1655
    ))

    # 88. Minimum Moves to Spread Stones Over Grid
    problems.append(make_problem(
        pid="bt-h-minimum-moves-stones-grid", title="Minimum Moves to Spread Stones",
        wing_id="backtracking", floor=288, difficulty="hard", visualizer_type="array",
        monster_name="Stone Golem", monster_title="Distributor of Overfilled Piles",
        monster_sprite="golem", monster_color="#64748b", monster_attack="Stone Stomp",
        monster_quote="Manhattan transfer distance minimized across the 3x3 grid!",
        description="You are given a `3 x 3` integer matrix `grid` containing 9 elements where each cell represents the number of stones. There are a total of 9 stones. In one move, you can move a stone from cell `(r1, c1)` to an adjacent cell `(r2, c2)`. Return the minimum number of moves to place one stone in each cell.",
        examples=[{"input": "grid = [[1,1,0],[1,1,1],[1,2,1]]", "output": "3"}, {"input": "grid = [[1,3,0],[1,0,0],[1,0,3]]", "output": "4"}],
        constraints=["grid.length == 3", "grid[0].length == 3"],
        function_name="minimumMovesStones",
        starter_code="def minimumMovesStones(grid: list[list[int]]) -> int:\n    pass\n",
        solution_code="def minimumMovesStones(grid: list[list[int]]) -> int:\n    zeros = []\n    extras = []\n    for r in range(3):\n        for c in range(3):\n            if grid[r][c] == 0: zeros.append((r, c))\n            elif grid[r][c] > 1: extras.extend([(r, c)] * (grid[r][c] - 1))\n    import itertools\n    min_moves = float('inf')\n    for p in set(itertools.permutations(extras)):\n        moves = sum(abs(z[0] - e[0]) + abs(z[1] - e[1]) for z, e in zip(zeros, p))\n        min_moves = min(min_moves, moves)\n    return min_moves if min_moves != float('inf') else 0\n",
        test_cases=[{"input": [[[1, 1, 0], [1, 1, 1], [1, 2, 1]]], "expected": 3}, {"input": [[[1, 3, 0], [1, 0, 0], [1, 0, 3]]], "expected": 4}],
        hints=["Collect cells with 0 stones and extra stones, then find minimum matching permutation."],
        leetcode_id=2850
    ))

    # 89. Cracking the Safe (De Bruijn Sequence)
    problems.append(make_problem(
        pid="bt-h-cracking-the-safe", title="Cracking the Safe (De Bruijn Sequence)",
        wing_id="backtracking", floor=289, difficulty="hard", visualizer_type="graph",
        monster_name="Vault Lock Hydra", monster_title="Guardian of De Bruijn Cycles",
        monster_sprite="hydra", monster_color="#10b981", monster_attack="Vault Squeeze",
        monster_quote="Eulerian circuit through de Bruijn graph unlocked the safe in k^n + n - 1 steps!",
        description="There is a safe protected by a password of `n` digits. Each digit can be one of the first `k` digits: `0, 1, ..., k-1`. The safe opens as soon as the last `n` digits of the entered sequence match the password. Return any sequence of minimum length that is guaranteed to open the safe.",
        examples=[{"input": "n = 1, k = 2", "output": "\"10\""}, {"input": "n = 2, k = 2", "output": "\"01100\""}],
        constraints=["1 <= n <= 4", "1 <= k <= 10", "k^n <= 4096"],
        function_name="crackSafe",
        starter_code="def crackSafe(n: int, k: int) -> str:\n    pass\n",
        solution_code="def crackSafe(n: int, k: int) -> str:\n    seen = set()\n    ans = []\n    def dfs(node):\n        for x in map(str, range(k)):\n            edge = node + x\n            if edge not in seen:\n                seen.add(edge)\n                dfs(edge[1:])\n                ans.append(x)\n    start = '0' * (n - 1)\n    dfs(start)\n    return start + ''.join(reversed(ans))\n",
        test_cases=[{"input": [1, 2], "expected": "01"}, {"input": [2, 2], "expected": "00110"}],
        hints=["Hierholzer's algorithm on the de Bruijn graph generates an Eulerian circuit."],
        leetcode_id=753
    ))

    # 90. Burst Balloons
    problems.append(make_problem(
        pid="bt-h-burst-balloons", title="Burst Balloons Maximal Coins",
        wing_id="backtracking", floor=290, difficulty="hard", visualizer_type="array",
        monster_name="Pneumatic Titan", monster_title="Grand Arch-Boss of Backtracking",
        monster_sprite="golem", monster_color="#ef4444", monster_attack="Pneumatic Shatter",
        monster_quote="Thinking in reverse—deciding which balloon to burst LAST—yielded the global maximum coins!",
        description="You are given `n` balloons, indexed from `0` to `n - 1`. Each balloon is painted with a number on it represented by an array `nums`. You are asked to burst all the balloons. If you burst balloon `i` you will get `nums[i - 1] * nums[i] * nums[i + 1]` coins. Return the maximum coins you can collect by bursting the balloons wisely.",
        examples=[{"input": "nums = [3,1,5,8]", "output": "167"}, {"input": "nums = [1,5]", "output": "10"}],
        constraints=["n == len(nums)", "1 <= n <= 300", "0 <= nums[i] <= 100"],
        function_name="maxCoins",
        starter_code="def maxCoins(nums: list[int]) -> int:\n    pass\n",
        solution_code="def maxCoins(nums: list[int]) -> int:\n    val = [1] + [x for x in nums if x > 0] + [1]\n    n = len(val)\n    dp = [[0] * n for _ in range(n)]\n    for length in range(2, n):\n        for i in range(n - length):\n            j = i + length\n            for k in range(i + 1, j):\n                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + val[i] * val[k] * val[j])\n    return dp[0][n - 1]\n",
        test_cases=[{"input": [[3, 1, 5, 8]], "expected": 167}, {"input": [[1, 5]], "expected": 10}, {"input": [[7]], "expected": 7}],
        hints=["Interval DP: choose which balloon k to burst LAST in the interval (i, j)."],
        leetcode_id=312
    ))

    return problems
