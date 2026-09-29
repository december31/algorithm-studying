import * as fs from 'fs';
import * as path from 'path';
import { allProblems } from '../src/data/problems';
import { pythonCurriculum } from '../src/data/pythonCurriculum';
import { getEnrichedTestCases } from '../src/data/edgeCases';
import { leetcodeMapping } from '../src/data/leetcodeMapping';
import { Problem } from '../src/types/problem';

// Interface for serialized problem JSON
export interface SerializedProblem {
  id: string;
  wingId: string;
  floor: number;
  title: string;
  difficulty: 'easy' | 'medium' | 'hard';
  visualizerType: string;
  monster: {
    id: string;
    name: string;
    title: string;
    maxHp: number;
    hp: number;
    sprite: string;
    color: string;
    attackName: string;
    attackPower: number;
    defeatQuote: string;
  };
  description: string;
  examples: {
    input: string;
    output: string;
    explanation?: string;
  }[];
  constraints: string[];
  starterCode: string;
  solutionCode: string;
  functionName: string;
  testCases: {
    id: number;
    input: any[];
    expected: any;
    inputDisplay: string;
    expectedDisplay: string;
    isHidden?: boolean;
  }[];
  hints: string[];
  python: {
    starterCode: string;
    solutionCode: string;
  };
  leetcodeId?: number;
  leetcodeTitle?: string;
  leetcodeUrl?: string;
}

export interface CatalogEntry {
  id: string;
  wingId: string;
  floor: number;
  title: string;
  difficulty: 'easy' | 'medium' | 'hard';
  visualizerType: string;
  leetcodeId?: number;
  leetcodeTitle?: string;
  leetcodeUrl?: string;
  monster: {
    id: string;
    name: string;
    title: string;
    maxHp: number;
    hp: number;
    sprite: string;
    color: string;
    attackName: string;
    attackPower: number;
    defeatQuote: string;
  };
}

// 15 NEW MEDIUM & HARD PROBLEMS
const newProblems: SerializedProblem[] = [
  // ==========================================
  // TOPIC 1: DATA STRUCTURES (2 Medium, 1 Hard)
  // ==========================================
  {
    id: 'longest-substring-without-repeating-characters',
    wingId: 'data-structures',
    floor: 18,
    title: 'Longest Substring Without Repeating Characters (Sliding Window Map)',
    difficulty: 'medium',
    visualizerType: 'array',
    monster: {
      id: 'gorgon-substring',
      name: 'Medusith of the Unbroken String',
      title: 'Queen of Sliding Boundaries',
      maxHp: 4,
      hp: 4,
      sprite: 'slime',
      color: '#06b6d4',
      attackName: 'Duplicate Character Constriction',
      attackPower: 2,
      defeatQuote: 'Your window expanded without a single collision...',
    },
    description: `Given a string \`s\`, find the length of the longest substring without repeating characters.`,
    examples: [
      { input: 's = "abcabcbb"', output: '3', explanation: 'The answer is "abc", with the length of 3.' },
      { input: 's = "bbbbb"', output: '1', explanation: 'The answer is "b", with the length of 1.' },
      { input: 's = "pwwkew"', output: '3', explanation: 'The answer is "wke", with the length of 3.' },
    ],
    constraints: ['0 <= s.length <= 5 * 10^4', 's consists of English letters, digits, symbols and spaces.'],
    starterCode: `function lengthOfLongestSubstring(s) {
  return 0;
}`,
    solutionCode: `function lengthOfLongestSubstring(s) {
  const map = new Map();
  let maxLen = 0, left = 0;
  for (let right = 0; right < s.length; right++) {
    const c = s[right];
    if (map.has(c) && map.get(c) >= left) {
      left = map.get(c) + 1;
    }
    map.set(c, right);
    maxLen = Math.max(maxLen, right - left + 1);
  }
  return maxLen;
}`,
    functionName: 'lengthOfLongestSubstring',
    testCases: [
      { id: 1, input: ['abcabcbb'], expected: 3, inputDisplay: 's = "abcabcbb"', expectedDisplay: '3' },
      { id: 2, input: ['bbbbb'], expected: 1, inputDisplay: 's = "bbbbb"', expectedDisplay: '1' },
      { id: 3, input: ['pwwkew'], expected: 3, inputDisplay: 's = "pwwkew"', expectedDisplay: '3' },
      { id: 4, input: [''], expected: 0, inputDisplay: 's = ""', expectedDisplay: '0', isHidden: true },
      { id: 5, input: [' '], expected: 1, inputDisplay: 's = " "', expectedDisplay: '1', isHidden: true },
      { id: 6, input: ['au'], expected: 2, inputDisplay: 's = "au"', expectedDisplay: '2', isHidden: true },
      { id: 7, input: ['dvdf'], expected: 3, inputDisplay: 's = "dvdf"', expectedDisplay: '3', isHidden: true },
      { id: 8, input: ['abba'], expected: 2, inputDisplay: 's = "abba"', expectedDisplay: '2', isHidden: true },
      { id: 9, input: ['tmmzuxt'], expected: 5, inputDisplay: 's = "tmmzuxt"', expectedDisplay: '5', isHidden: true },
      { id: 10, input: ['abcdefghijklmnopqrstuvwxyz'], expected: 26, inputDisplay: 's = "a..z"', expectedDisplay: '26', isHidden: true },
    ],
    hints: ['Track the last seen index of each character in a Hash Map. When a duplicate appears inside the current window, shift the left pointer past it.'],
    python: {
      starterCode: `def lengthOfLongestSubstring(s):
    return 0
`,
      solutionCode: `def lengthOfLongestSubstring(s):
    seen = {}
    max_len = 0
    left = 0
    for right, c in enumerate(s):
        if c in seen and seen[c] >= left:
            left = seen[c] + 1
        seen[c] = right
        max_len = max(max_len, right - left + 1)
    return max_len
`,
    },
    leetcodeId: 3,
    leetcodeTitle: 'Longest Substring Without Repeating Characters',
    leetcodeUrl: 'https://leetcode.com/problems/longest-substring-without-repeating-characters/',
  },
  {
    id: 'three-sum',
    wingId: 'data-structures',
    floor: 19,
    title: '3Sum (Sort + Two Pointers)',
    difficulty: 'medium',
    visualizerType: 'array',
    monster: {
      id: 'triad-golem',
      name: 'Triad Golem of Equilibrium',
      title: 'Sentinel of Zero Sums',
      maxHp: 4,
      hp: 4,
      sprite: 'gargoyle',
      color: '#3b82f6',
      attackName: 'Tripartite Seismic Wave',
      attackPower: 2,
      defeatQuote: 'Three pointers converged and neutralized my core...',
    },
    description: `Given an integer array \`nums\`, return all the triplets \`[nums[i], nums[j], nums[k]]\` such that \`i != j\`, \`i != k\`, and \`j != k\`, and \`nums[i] + nums[j] + nums[k] == 0\`.

Notice that the solution set must not contain duplicate triplets.`,
    examples: [
      { input: 'nums = [-1,0,1,2,-1,-4]', output: '[[-1,-1,2],[-1,0,1]]' },
      { input: 'nums = [0,1,1]', output: '[]' },
      { input: 'nums = [0,0,0]', output: '[[0,0,0]]' },
    ],
    constraints: ['3 <= nums.length <= 3000', '-10^5 <= nums[i] <= 10^5'],
    starterCode: `function threeSum(nums) {
  return [];
}`,
    solutionCode: `function threeSum(nums) {
  nums.sort((a, b) => a - b);
  const res = [];
  for (let i = 0; i < nums.length - 2; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue;
    let l = i + 1, r = nums.length - 1;
    while (l < r) {
      const sum = nums[i] + nums[l] + nums[r];
      if (sum === 0) {
        res.push([nums[i], nums[l], nums[r]]);
        while (l < r && nums[l] === nums[l + 1]) l++;
        while (l < r && nums[r] === nums[r - 1]) r--;
        l++;
        r--;
      } else if (sum < 0) {
        l++;
      } else {
        r--;
      }
    }
  }
  return res;
}`,
    functionName: 'threeSum',
    testCases: [
      { id: 1, input: [[-1, 0, 1, 2, -1, -4]], expected: [[-1, -1, 2], [-1, 0, 1]], inputDisplay: 'nums = [-1,0,1,2,-1,-4]', expectedDisplay: '[[-1,-1,2],[-1,0,1]]' },
      { id: 2, input: [[0, 1, 1]], expected: [], inputDisplay: 'nums = [0,1,1]', expectedDisplay: '[]' },
      { id: 3, input: [[0, 0, 0]], expected: [[0, 0, 0]], inputDisplay: 'nums = [0,0,0]', expectedDisplay: '[[0,0,0]]' },
      { id: 4, input: [[-2, 0, 1, 1, 2]], expected: [[-2, 0, 2], [-2, 1, 1]], inputDisplay: 'nums = [-2,0,1,1,2]', expectedDisplay: '[[-2,0,2],[-2,1,1]]', isHidden: true },
      { id: 5, input: [[0, 0, 0, 0]], expected: [[0, 0, 0]], inputDisplay: 'nums = [0,0,0,0]', expectedDisplay: '[[0,0,0]]', isHidden: true },
      { id: 6, input: [[-1, 0, 1]], expected: [[-1, 0, 1]], inputDisplay: 'nums = [-1,0,1]', expectedDisplay: '[[-1,0,1]]', isHidden: true },
      { id: 7, input: [[1, 2, -2, -1]], expected: [], inputDisplay: 'nums = [1,2,-2,-1]', expectedDisplay: '[]', isHidden: true },
      { id: 8, input: [[-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]], expected: [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]], inputDisplay: 'nums = [-4,-2,-2...]', expectedDisplay: '6 triplets', isHidden: true },
      { id: 9, input: [[3, 0, -2, -1, 1, 2]], expected: [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]], inputDisplay: 'nums = [3,0,-2,-1,1,2]', expectedDisplay: '3 triplets', isHidden: true },
      { id: 10, input: [[-1, -1, -1, 2, 2]], expected: [[-1, -1, 2]], inputDisplay: 'nums = [-1,-1,-1,2,2]', expectedDisplay: '[[-1,-1,2]]', isHidden: true },
    ],
    hints: ['Sort the array first. Fix nums[i], then use two pointers (left and right) to find pairs summing to -nums[i]. Skip duplicates!'],
    python: {
      starterCode: `def threeSum(nums):
    return []
`,
      solutionCode: `def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return res
`,
    },
    leetcodeId: 15,
    leetcodeTitle: '3Sum',
    leetcodeUrl: 'https://leetcode.com/problems/3sum/',
  },
  {
    id: 'merge-k-sorted-lists',
    wingId: 'data-structures',
    floor: 20,
    title: 'Boss Chamber: Merge k Sorted Arrays (Min-Heap / Divide & Conquer)',
    difficulty: 'hard',
    visualizerType: 'array',
    monster: {
      id: 'hydra-k-lists',
      name: 'Hydra of Ten Thousand Heads',
      title: 'Grand Sovereign of Multi-List Merging',
      maxHp: 4,
      hp: 4,
      sprite: 'dragon',
      color: '#ef4444',
      attackName: 'Multi-Stream Tectonic Torrent',
      attackPower: 3,
      defeatQuote: 'My k heads severed one by one into a single sorted destiny...',
    },
    description: `You are given an array of \`k\` sorted integer arrays \`lists\`. Merge all the sorted arrays into one sorted array and return it.`,
    examples: [
      { input: 'lists = [[1,4,5],[1,3,4],[2,6]]', output: '[1,1,2,3,4,4,5,6]' },
      { input: 'lists = []', output: '[]' },
      { input: 'lists = [[]]', output: '[]' },
    ],
    constraints: ['k == lists.length', '0 <= k <= 10^4', '0 <= lists[i].length <= 500', '-10^4 <= lists[i][j] <= 10^4'],
    starterCode: `function mergeKLists(lists) {
  return [];
}`,
    solutionCode: `function mergeKLists(lists) {
  if (!lists || lists.length === 0) return [];
  const mergeTwo = (a, b) => {
    const res = [];
    let i = 0, j = 0;
    while (i < a.length && j < b.length) {
      if (a[i] <= b[j]) res.push(a[i++]);
      else res.push(b[j++]);
    }
    while (i < a.length) res.push(a[i++]);
    while (j < b.length) res.push(b[j++]);
    return res;
  };
  while (lists.length > 1) {
    const merged = [];
    for (let i = 0; i < lists.length; i += 2) {
      if (i + 1 < lists.length) merged.push(mergeTwo(lists[i], lists[i + 1]));
      else merged.push(lists[i]);
    }
    lists = merged;
  }
  return lists[0] || [];
}`,
    functionName: 'mergeKLists',
    testCases: [
      { id: 1, input: [[[1, 4, 5], [1, 3, 4], [2, 6]]], expected: [1, 1, 2, 3, 4, 4, 5, 6], inputDisplay: 'lists = [[1,4,5],[1,3,4],[2,6]]', expectedDisplay: '[1,1,2,3,4,4,5,6]' },
      { id: 2, input: [[]], expected: [], inputDisplay: 'lists = []', expectedDisplay: '[]' },
      { id: 3, input: [[[]]], expected: [], inputDisplay: 'lists = [[]]', expectedDisplay: '[]' },
      { id: 4, input: [[[1], [0]]], expected: [0, 1], inputDisplay: 'lists = [[1],[0]]', expectedDisplay: '[0,1]', isHidden: true },
      { id: 5, input: [[[2], [], [-1]]], expected: [-1, 2], inputDisplay: 'lists = [[2],[],[-1]]', expectedDisplay: '[-1,2]', isHidden: true },
      { id: 6, input: [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]], expected: [1, 2, 3, 4, 5, 6, 7, 8, 9], inputDisplay: 'lists = 3 contiguous ranges', expectedDisplay: '[1..9]', isHidden: true },
      { id: 7, input: [[[-10, -5], [-8, 0], [1, 5]]], expected: [-10, -8, -5, 0, 1, 5], inputDisplay: 'lists with negatives', expectedDisplay: '[-10,-8,-5,0,1,5]', isHidden: true },
      { id: 8, input: [[[], [], []]], expected: [], inputDisplay: 'lists = [[],[],[]]', expectedDisplay: '[]', isHidden: true },
      { id: 9, input: [[[5], [4], [3], [2], [1]]], expected: [1, 2, 3, 4, 5], inputDisplay: '5 singleton lists', expectedDisplay: '[1,2,3,4,5]', isHidden: true },
      { id: 10, input: [[[1, 1, 1], [1, 1, 1]]], expected: [1, 1, 1, 1, 1, 1], inputDisplay: 'duplicate identical values', expectedDisplay: '[1,1,1,1,1,1]', isHidden: true },
    ],
    hints: ['Pairwise merge the lists in O(N log k) using divide and conquer, or maintain a min-heap of the leading element from each list.'],
    python: {
      starterCode: `def mergeKLists(lists):
    return []
`,
      solutionCode: `def mergeKLists(lists):
    if not lists:
        return []
    import heapq
    heap = []
    res = []
    for i, arr in enumerate(lists):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))
    while heap:
        val, arr_idx, elem_idx = heapq.heappop(heap)
        res.append(val)
        if elem_idx + 1 < len(lists[arr_idx]):
            heapq.heappush(heap, (lists[arr_idx][elem_idx + 1], arr_idx, elem_idx + 1))
    return res
`,
    },
    leetcodeId: 23,
    leetcodeTitle: 'Merge k Sorted Lists',
    leetcodeUrl: 'https://leetcode.com/problems/merge-k-sorted-lists/',
  },

  // ==========================================
  // TOPIC 2: BACKTRACKING (2 Medium, 1 Hard)
  // ==========================================
  {
    id: 'letter-combinations-of-a-phone-number',
    wingId: 'backtracking',
    floor: 18,
    title: 'Letter Combinations of a Phone Number (Tree Branching)',
    difficulty: 'medium',
    visualizerType: 'tree',
    monster: {
      id: 'dialing-chimera',
      name: 'The Dialing Chimera',
      title: 'Keeper of Keypad Permutations',
      maxHp: 4,
      hp: 4,
      sprite: 'gargoyle',
      color: '#a855f7',
      attackName: 'Polyphonic Digit Scream',
      attackPower: 2,
      defeatQuote: 'Every branch of phone digits traversed to the leaf...',
    },
    description: `Given a string containing digits from \`2-9\` inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.`,
    examples: [
      { input: 'digits = "23"', output: '["ad","ae","af","bd","be","bf","cd","ce","cf"]' },
      { input: 'digits = ""', output: '[]' },
      { input: 'digits = "2"', output: '["a","b","c"]' },
    ],
    constraints: ['0 <= digits.length <= 4', 'digits[i] is a digit in the range [\'2\', \'9\'].'],
    starterCode: `function letterCombinations(digits) {
  return [];
}`,
    solutionCode: `function letterCombinations(digits) {
  if (!digits) return [];
  const map = {
    '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
    '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
  };
  const res = [];
  function backtrack(idx, path) {
    if (idx === digits.length) {
      res.push(path);
      return;
    }
    const letters = map[digits[idx]] || '';
    for (let i = 0; i < letters.length; i++) {
      backtrack(idx + 1, path + letters[i]);
    }
  }
  backtrack(0, '');
  return res;
}`,
    functionName: 'letterCombinations',
    testCases: [
      { id: 1, input: ['23'], expected: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'], inputDisplay: 'digits = "23"', expectedDisplay: '["ad","ae","af","bd","be","bf","cd","ce","cf"]' },
      { id: 2, input: [''], expected: [], inputDisplay: 'digits = ""', expectedDisplay: '[]' },
      { id: 3, input: ['2'], expected: ['a', 'b', 'c'], inputDisplay: 'digits = "2"', expectedDisplay: '["a","b","c"]' },
      { id: 4, input: ['9'], expected: ['w', 'x', 'y', 'z'], inputDisplay: 'digits = "9"', expectedDisplay: '["w","x","y","z"]', isHidden: true },
      { id: 5, input: ['79'], expected: ['pw', 'px', 'py', 'pz', 'qw', 'qx', 'qy', 'qz', 'rw', 'rx', 'ry', 'rz', 'sw', 'sx', 'sy', 'sz'], inputDisplay: 'digits = "79"', expectedDisplay: '16 combinations', isHidden: true },
      { id: 6, input: ['4'], expected: ['g', 'h', 'i'], inputDisplay: 'digits = "4"', expectedDisplay: '["g","h","i"]', isHidden: true },
      { id: 7, input: ['22'], expected: ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc'], inputDisplay: 'digits = "22"', expectedDisplay: '9 combinations', isHidden: true },
      { id: 8, input: ['345'], expected: ['dgj','dgk','dgl','dhj','dhk','dhl','dij','dik','dil','egj','egk','egl','ehj','ehk','ehl','eij','eik','eil','fgj','fgk','fgl','fhj','fhk','fhl','fij','fik','fil'], inputDisplay: 'digits = "345"', expectedDisplay: '27 combinations', isHidden: true },
      { id: 9, input: ['7'], expected: ['p', 'q', 'r', 's'], inputDisplay: 'digits = "7"', expectedDisplay: '["p","q","r","s"]', isHidden: true },
      { id: 10, input: ['8'], expected: ['t', 'u', 'v'], inputDisplay: 'digits = "8"', expectedDisplay: '["t","u","v"]', isHidden: true },
    ],
    hints: ['Map each digit to its respective letters. Recurse depth-first, passing the accumulated string down to the base case at digits.length.'],
    python: {
      starterCode: `def letterCombinations(digits):
    return []
`,
      solutionCode: `def letterCombinations(digits):
    if not digits:
        return []
    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    res = []
    def backtrack(idx, path):
        if idx == len(digits):
            res.append(path)
            return
        for char in mapping.get(digits[idx], ''):
            backtrack(idx + 1, path + char)
    backtrack(0, '')
    return res
`,
    },
    leetcodeId: 17,
    leetcodeTitle: 'Letter Combinations of a Phone Number',
    leetcodeUrl: 'https://leetcode.com/problems/letter-combinations-of-a-phone-number/',
  },
  {
    id: 'palindrome-partitioning',
    wingId: 'backtracking',
    floor: 19,
    title: 'Palindrome Partitioning (Substring Backtracking)',
    difficulty: 'medium',
    visualizerType: 'tree',
    monster: {
      id: 'mirror-shade',
      name: 'Mirror Shade of Symmetrical Cuts',
      title: 'Arbiter of Palindromic Partitions',
      maxHp: 4,
      hp: 4,
      sprite: 'lich',
      color: '#c084fc',
      attackName: 'Shattered Mirror Slices',
      attackPower: 2,
      defeatQuote: 'Every partition reflected true symmetry...',
    },
    description: `Given a string \`s\`, partition \`s\` such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of \`s\`.`,
    examples: [
      { input: 's = "aab"', output: '[["a","a","b"],["aa","b"]]' },
      { input: 's = "a"', output: '[["a"]]' },
    ],
    constraints: ['1 <= s.length <= 16', 's contains only lowercase English letters.'],
    starterCode: `function partition(s) {
  return [];
}`,
    solutionCode: `function partition(s) {
  const res = [];
  function isPal(sub) {
    let l = 0, r = sub.length - 1;
    while (l < r) {
      if (sub[l++] !== sub[r--]) return false;
    }
    return true;
  }
  function backtrack(start, current) {
    if (start === s.length) {
      res.push([...current]);
      return;
    }
    for (let end = start + 1; end <= s.length; end++) {
      const sub = s.slice(start, end);
      if (isPal(sub)) {
        current.push(sub);
        backtrack(end, current);
        current.pop();
      }
    }
  }
  backtrack(0, []);
  return res;
}`,
    functionName: 'partition',
    testCases: [
      { id: 1, input: ['aab'], expected: [['a', 'a', 'b'], ['aa', 'b']], inputDisplay: 's = "aab"', expectedDisplay: '[["a","a","b"],["aa","b"]]' },
      { id: 2, input: ['a'], expected: [['a']], inputDisplay: 's = "a"', expectedDisplay: '[["a"]]' },
      { id: 3, input: ['ab'], expected: [['a', 'b']], inputDisplay: 's = "ab"', expectedDisplay: '[["a","b"]]' },
      { id: 4, input: ['aba'], expected: [['a', 'b', 'a'], ['aba']], inputDisplay: 's = "aba"', expectedDisplay: '[["a","b","a"],["aba"]]', isHidden: true },
      { id: 5, input: ['aaa'], expected: [['a', 'a', 'a'], ['a', 'aa'], ['aa', 'a'], ['aaa']], inputDisplay: 's = "aaa"', expectedDisplay: '4 partitions', isHidden: true },
      { id: 6, input: ['bb'], expected: [['b', 'b'], ['bb']], inputDisplay: 's = "bb"', expectedDisplay: '[["b","b"],["bb"]]', isHidden: true },
      { id: 7, input: ['racecar'], expected: [['r','a','c','e','c','a','r'], ['r','a','cec','a','r'], ['r','aceca','r'], ['racecar']], inputDisplay: 's = "racecar"', expectedDisplay: '4 partitions', isHidden: true },
      { id: 8, input: ['abc'], expected: [['a', 'b', 'c']], inputDisplay: 's = "abc"', expectedDisplay: '[["a","b","c"]]', isHidden: true },
      { id: 9, input: ['abba'], expected: [['a', 'b', 'b', 'a'], ['a', 'bb', 'a'], ['abba']], inputDisplay: 's = "abba"', expectedDisplay: '3 partitions', isHidden: true },
      { id: 10, input: ['cdd'], expected: [['c', 'd', 'd'], ['c', 'dd']], inputDisplay: 's = "cdd"', expectedDisplay: '[["c","d","d"],["c","dd"]]', isHidden: true },
    ],
    hints: ['Try all possible first prefix substrings. If the prefix is a palindrome, recurse on the remainder of the string.'],
    python: {
      starterCode: `def partition(s):
    return []
`,
      solutionCode: `def partition(s):
    res = []
    def backtrack(start, curr):
        if start == len(s):
            res.append(list(curr))
            return
        for end in range(start + 1, len(s) + 1):
            sub = s[start:end]
            if sub == sub[::-1]:
                curr.append(sub)
                backtrack(end, curr)
                curr.pop()
    backtrack(0, [])
    return res
`,
    },
    leetcodeId: 131,
    leetcodeTitle: 'Palindrome Partitioning',
    leetcodeUrl: 'https://leetcode.com/problems/palindrome-partitioning/',
  },
  {
    id: 'word-break-ii',
    wingId: 'backtracking',
    floor: 20,
    title: 'Boss Chamber: Word Break II (DFS + Memoization)',
    difficulty: 'hard',
    visualizerType: 'tree',
    monster: {
      id: 'lexicon-overlord',
      name: 'Lexicon Overlord of Endless Parse Trees',
      title: 'Grand Tyrant of Dictionary Decompositions',
      maxHp: 4,
      hp: 4,
      sprite: 'lich',
      color: '#e11d48',
      attackName: 'Recursive Lexicon Fracture',
      attackPower: 3,
      defeatQuote: 'Every word token found its rightful whitespace boundary...',
    },
    description: `Given a string \`s\` and a dictionary of strings \`wordDict\`, add spaces in \`s\` to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.`,
    examples: [
      { input: 's = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]', output: '["cats and dog","cat sand dog"]' },
      { input: 's = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]', output: '["pine apple pen apple","pineapple pen apple","pine applepen apple"]' },
      { input: 's = "catsandog", wordDict = ["cats","dog","sand","and","cat"]', output: '[]' },
    ],
    constraints: ['1 <= s.length <= 20', '1 <= wordDict.length <= 1000', '1 <= wordDict[i].length <= 10'],
    starterCode: `function wordBreak(s, wordDict) {
  return [];
}`,
    solutionCode: `function wordBreak(s, wordDict) {
  const dict = new Set(wordDict);
  const memo = new Map();
  function dfs(str) {
    if (memo.has(str)) return memo.get(str);
    if (str.length === 0) return [''];
    const res = [];
    for (const word of dict) {
      if (str.startsWith(word)) {
        const subList = dfs(str.slice(word.length));
        for (const sub of subList) {
          res.push(sub.length === 0 ? word : word + ' ' + sub);
        }
      }
    }
    memo.set(str, res);
    return res;
  }
  return dfs(s);
}`,
    functionName: 'wordBreak',
    testCases: [
      { id: 1, input: ['catsanddog', ['cat', 'cats', 'and', 'sand', 'dog']], expected: ['cat sand dog', 'cats and dog'], inputDisplay: 's = "catsanddog", wordDict = 5 words', expectedDisplay: '["cat sand dog","cats and dog"]' },
      { id: 2, input: ['pineapplepenapple', ['apple', 'pen', 'applepen', 'pine', 'pineapple']], expected: ['pine apple pen apple', 'pine applepen apple', 'pineapple pen apple'], inputDisplay: 's = "pineapplepenapple"', expectedDisplay: '3 sentences' },
      { id: 3, input: ['catsandog', ['cats', 'dog', 'sand', 'and', 'cat']], expected: [], inputDisplay: 's = "catsandog"', expectedDisplay: '[]' },
      { id: 4, input: ['a', ['a']], expected: ['a'], inputDisplay: 's = "a", wordDict = ["a"]', expectedDisplay: '["a"]', isHidden: true },
      { id: 5, input: ['ab', ['a', 'b']], expected: ['a b'], inputDisplay: 's = "ab"', expectedDisplay: '["a b"]', isHidden: true },
      { id: 6, input: ['aaaa', ['a', 'aa', 'aaa']], expected: ['a a a a', 'a a aa', 'a aa a', 'a aaa', 'aa a a', 'aa aa', 'aaa a'], inputDisplay: 's = "aaaa"', expectedDisplay: '7 sentences', isHidden: true },
      { id: 7, input: ['bb', ['a', 'b', 'bbb']], expected: ['b b'], inputDisplay: 's = "bb"', expectedDisplay: '["b b"]', isHidden: true },
      { id: 8, input: ['sanddog', ['sand', 'dog']], expected: ['sand dog'], inputDisplay: 's = "sanddog"', expectedDisplay: '["sand dog"]', isHidden: true },
      { id: 9, input: ['cat', ['cat']], expected: ['cat'], inputDisplay: 's = "cat"', expectedDisplay: '["cat"]', isHidden: true },
      { id: 10, input: ['dogcat', ['cat', 'dog']], expected: ['dog cat'], inputDisplay: 's = "dogcat"', expectedDisplay: '["dog cat"]', isHidden: true },
    ],
    hints: ['DFS from the start of the string, matching any prefix that exists in the dictionary. Memoize results for each suffix string to avoid repeated work.'],
    python: {
      starterCode: `def wordBreak(s, wordDict):
    return []
`,
      solutionCode: `def wordBreak(s, wordDict):
    d = set(wordDict)
    memo = {}
    def dfs(rem):
        if rem in memo:
            return memo[rem]
        if not rem:
            return [""]
        res = []
        for word in wordDict:
            if rem.startswith(word):
                sub_res = dfs(rem[len(word):])
                for sub in sub_res:
                    res.append(word if not sub else word + " " + sub)
        memo[rem] = res
        return res
    return dfs(s)
`,
    },
    leetcodeId: 140,
    leetcodeTitle: 'Word Break II',
    leetcodeUrl: 'https://leetcode.com/problems/word-break-ii/',
  },

  // ==========================================
  // TOPIC 3: GRAPHS (2 Medium, 1 Hard)
  // ==========================================
  {
    id: 'course-schedule-ii',
    wingId: 'graphs',
    floor: 16,
    title: 'Course Schedule II (Topological Sort / Kahn\'s BFS)',
    difficulty: 'medium',
    visualizerType: 'graph',
    monster: {
      id: 'topological-archon',
      name: 'Topological Archon of Dependencies',
      title: 'Master of In-Degree Sequencing',
      maxHp: 4,
      hp: 4,
      sprite: 'lich',
      color: '#38bdf8',
      attackName: 'Circular Prerequisite Binding',
      attackPower: 2,
      defeatQuote: 'Zero in-degree ordering resolved every dependency...',
    },
    description: `There are a total of \`numCourses\` courses you have to take, labeled from \`0\` to \`numCourses - 1\`. You are given an array \`prerequisites\` where \`prerequisites[i] = [ai, bi]\` indicates that you must take course \`bi\` first if you want to take course \`ai\`.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.`,
    examples: [
      { input: 'numCourses = 2, prerequisites = [[1,0]]', output: '[0,1]' },
      { input: 'numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]', output: '[0,2,1,3]' },
      { input: 'numCourses = 1, prerequisites = []', output: '[0]' },
    ],
    constraints: ['1 <= numCourses <= 2000', '0 <= prerequisites.length <= numCourses * (numCourses - 1)'],
    starterCode: `function findOrder(numCourses, prerequisites) {
  return [];
}`,
    solutionCode: `function findOrder(numCourses, prerequisites) {
  const inDegree = new Array(numCourses).fill(0);
  const adj = Array.from({ length: numCourses }, () => []);
  for (const [dest, src] of prerequisites) {
    adj[src].push(dest);
    inDegree[dest]++;
  }
  const queue = [];
  for (let i = 0; i < numCourses; i++) {
    if (inDegree[i] === 0) queue.push(i);
  }
  const order = [];
  while (queue.length > 0) {
    const u = queue.shift();
    order.push(u);
    for (const v of adj[u]) {
      inDegree[v]--;
      if (inDegree[v] === 0) queue.push(v);
    }
  }
  return order.length === numCourses ? order : [];
}`,
    functionName: 'findOrder',
    testCases: [
      { id: 1, input: [2, [[1, 0]]], expected: [0, 1], inputDisplay: 'numCourses = 2, prerequisites = [[1,0]]', expectedDisplay: '[0,1]' },
      { id: 2, input: [4, [[1, 0], [2, 0], [3, 1], [3, 2]]], expected: [0, 1, 2, 3], inputDisplay: 'numCourses = 4, prereqs = 4 pairs', expectedDisplay: '[0,1,2,3]' },
      { id: 3, input: [1, []], expected: [0], inputDisplay: 'numCourses = 1, prerequisites = []', expectedDisplay: '[0]' },
      { id: 4, input: [2, [[0, 1], [1, 0]]], expected: [], inputDisplay: 'numCourses = 2, cycle [[0,1],[1,0]]', expectedDisplay: '[]', isHidden: true },
      { id: 5, input: [3, [[1, 0], [2, 1]]], expected: [0, 1, 2], inputDisplay: 'numCourses = 3, chain', expectedDisplay: '[0,1,2]', isHidden: true },
      { id: 6, input: [3, []], expected: [0, 1, 2], inputDisplay: 'numCourses = 3, independent', expectedDisplay: '[0,1,2]', isHidden: true },
      { id: 7, input: [3, [[0, 1], [0, 2], [1, 2]]], expected: [2, 1, 0], inputDisplay: 'numCourses = 3, reverse dependencies', expectedDisplay: '[2,1,0]', isHidden: true },
      { id: 8, input: [3, [[1, 0], [0, 2], [2, 1]]], expected: [], inputDisplay: 'numCourses = 3, 3-node cycle', expectedDisplay: '[]', isHidden: true },
      { id: 9, input: [2, []], expected: [0, 1], inputDisplay: 'numCourses = 2, empty prereqs', expectedDisplay: '[0,1]', isHidden: true },
      { id: 10, input: [5, [[1, 0], [2, 0], [3, 1], [4, 2]]], expected: [0, 1, 2, 3, 4], inputDisplay: 'numCourses = 5, branching tree', expectedDisplay: '[0,1,2,3,4]', isHidden: true },
    ],
    hints: ['Compute in-degrees of all nodes. Enqueue courses with in-degree 0. As courses are taken, decrement neighbor in-degrees.'],
    python: {
      starterCode: `def findOrder(numCourses, prerequisites):
    return []
`,
      solutionCode: `def findOrder(numCourses, prerequisites):
    from collections import deque
    in_degree = [0] * numCourses
    adj = [[] for _ in range(numCourses)]
    for dest, src in prerequisites:
        adj[src].append(dest)
        in_degree[dest] += 1
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    return order if len(order) == numCourses else []
`,
    },
    leetcodeId: 210,
    leetcodeTitle: 'Course Schedule II',
    leetcodeUrl: 'https://leetcode.com/problems/course-schedule-ii/',
  },
  {
    id: 'pacific-atlantic-water-flow',
    wingId: 'graphs',
    floor: 17,
    title: 'Pacific Atlantic Water Flow (Multi-Source BFS / DFS)',
    difficulty: 'medium',
    visualizerType: 'graph',
    monster: {
      id: 'dual-leviathan',
      name: 'Dual-Current Leviathan',
      title: 'Lord of Continental Divides',
      maxHp: 4,
      hp: 4,
      sprite: 'dragon',
      color: '#0284c7',
      attackName: 'Tidal Convergence Deluge',
      attackPower: 2,
      defeatQuote: 'Both oceans met at your precise continental coordinates...',
    },
    description: `There is an \`m x n\` rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific borders the top and left, and the Atlantic borders the bottom and right.

Return a 2D list of grid coordinates \`result\` where \`result[i] = [ri, ci]\` denotes that rain water can flow from cell \`(ri, ci)\` to both the Pacific and Atlantic oceans.`,
    examples: [
      { input: 'heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]', output: '[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]' },
      { input: 'heights = [[1]]', output: '[[0,0]]' },
    ],
    constraints: ['m == heights.length', 'n == heights[r].length', '1 <= m, n <= 200', '0 <= heights[r][c] <= 10^5'],
    starterCode: `function pacificAtlantic(heights) {
  return [];
}`,
    solutionCode: `function pacificAtlantic(heights) {
  if (!heights || heights.length === 0) return [];
  const m = heights.length, n = heights[0].length;
  const pac = Array.from({ length: m }, () => new Array(n).fill(false));
  const atl = Array.from({ length: m }, () => new Array(n).fill(false));
  const dfs = (r, c, visited, prevHeight) => {
    if (r < 0 || r >= m || c < 0 || c >= n || visited[r][c] || heights[r][c] < prevHeight) return;
    visited[r][c] = true;
    dfs(r + 1, c, visited, heights[r][c]);
    dfs(r - 1, c, visited, heights[r][c]);
    dfs(r, c + 1, visited, heights[r][c]);
    dfs(r, c - 1, visited, heights[r][c]);
  };
  for (let i = 0; i < m; i++) {
    dfs(i, 0, pac, heights[i][0]);
    dfs(i, n - 1, atl, heights[i][n - 1]);
  }
  for (let j = 0; j < n; j++) {
    dfs(0, j, pac, heights[0][j]);
    dfs(m - 1, j, atl, heights[m - 1][j]);
  }
  const res = [];
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (pac[i][j] && atl[i][j]) res.push([i, j]);
    }
  }
  return res;
}`,
    functionName: 'pacificAtlantic',
    testCases: [
      { id: 1, input: [[[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]], expected: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]], inputDisplay: 'heights = 5x5 grid', expectedDisplay: '7 cells' },
      { id: 2, input: [[[1]]], expected: [[0, 0]], inputDisplay: 'heights = [[1]]', expectedDisplay: '[[0,0]]' },
      { id: 3, input: [[[2, 1], [1, 2]]], expected: [[0, 0], [0, 1], [1, 0], [1, 1]], inputDisplay: 'heights = 2x2 grid', expectedDisplay: 'all 4 cells' },
      { id: 4, input: [[[10, 10, 10], [10, 1, 10], [10, 10, 10]]], expected: [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]], inputDisplay: 'heights = outer ring', expectedDisplay: '8 boundary cells', isHidden: true },
      { id: 5, input: [[[1, 2, 3], [8, 9, 4], [7, 6, 5]]], expected: [[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]], inputDisplay: 'spiral heights', expectedDisplay: '7 cells', isHidden: true },
      { id: 6, input: [[[1, 1], [1, 1]]], expected: [[0, 0], [0, 1], [1, 0], [1, 1]], inputDisplay: 'flat 2x2 grid', expectedDisplay: '[[0,0],[0,1],[1,0],[1,1]]', isHidden: true },
      { id: 7, input: [[[3, 3, 3, 3, 3, 3]]], expected: [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5]], inputDisplay: 'single row 1x6', expectedDisplay: 'all 6 cells', isHidden: true },
      { id: 8, input: [[[1], [2], [3], [4]]], expected: [[0, 0], [1, 0], [2, 0], [3, 0]], inputDisplay: 'single column 4x1', expectedDisplay: 'all 4 cells', isHidden: true },
      { id: 9, input: [[[1, 2], [4, 3]]], expected: [[0, 1], [1, 0], [1, 1]], inputDisplay: '2x2 increasing heights', expectedDisplay: '3 cells', isHidden: true },
      { id: 10, input: [[[5, 4, 3], [6, 1, 2], [7, 8, 9]]], expected: [[0, 0], [0, 1], [0, 2], [1, 0], [2, 0], [2, 1], [2, 2]], inputDisplay: 'complex basin', expectedDisplay: '7 cells', isHidden: true },
    ],
    hints: ['Reverse the flow: Start DFS from the Pacific borders flowing uphill, and separately from the Atlantic borders flowing uphill. Find the intersection.'],
    python: {
      starterCode: `def pacificAtlantic(heights):
    return []
`,
      solutionCode: `def pacificAtlantic(heights):
    if not heights:
        return []
    m, n = len(heights), len(heights[0])
    pac = [[False] * n for _ in range(m)]
    atl = [[False] * n for _ in range(m)]
    def dfs(r, c, vis, prev_h):
        if r < 0 or r >= m or c < 0 or c >= n or vis[r][c] or heights[r][c] < prev_h:
            return
        vis[r][c] = True
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dfs(r + dr, c + dc, vis, heights[r][c])
    for i in range(m):
        dfs(i, 0, pac, heights[i][0])
        dfs(i, n - 1, atl, heights[i][n - 1])
    for j in range(n):
        dfs(0, j, pac, heights[0][j])
        dfs(m - 1, j, atl, heights[m - 1][j])
    return [[i, j] for i in range(m) for j in range(n) if pac[i][j] and atl[i][j]]
`,
    },
    leetcodeId: 417,
    leetcodeTitle: 'Pacific Atlantic Water Flow',
    leetcodeUrl: 'https://leetcode.com/problems/pacific-atlantic-water-flow/',
  },
  {
    id: 'longest-increasing-path-in-a-matrix',
    wingId: 'graphs',
    floor: 18,
    title: 'Boss Chamber: Longest Increasing Path in a Matrix (DAG DFS + Memo)',
    difficulty: 'hard',
    visualizerType: 'graph',
    monster: {
      id: 'ascendant-titan',
      name: 'Ascendant Titan of Mountain Crests',
      title: 'Emperor of Strict Ascent Paths',
      maxHp: 4,
      hp: 4,
      sprite: 'gargoyle',
      color: '#dc2626',
      attackName: 'Steep Avalanche Cascade',
      attackPower: 3,
      defeatQuote: 'You climbed the maximal DAG path straight to my throne...',
    },
    description: `Given an \`m x n\` integers \`matrix\`, return the length of the longest increasing path in \`matrix\`. From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary.`,
    examples: [
      { input: 'matrix = [[9,9,4],[6,6,8],[2,1,1]]', output: '4', explanation: 'The longest increasing path is [1, 2, 6, 9].' },
      { input: 'matrix = [[3,4,5],[3,2,6],[2,2,1]]', output: '4', explanation: 'The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.' },
      { input: 'matrix = [[1]]', output: '1' },
    ],
    constraints: ['m == matrix.length', 'n == matrix[i].length', '1 <= m, n <= 200', '0 <= matrix[i][j] <= 2^31 - 1'],
    starterCode: `function longestIncreasingPath(matrix) {
  return 0;
}`,
    solutionCode: `function longestIncreasingPath(matrix) {
  if (!matrix || matrix.length === 0) return 0;
  const m = matrix.length, n = matrix[0].length;
  const memo = Array.from({ length: m }, () => new Array(n).fill(0));
  const dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]];
  let maxPath = 0;
  function dfs(r, c) {
    if (memo[r][c] !== 0) return memo[r][c];
    let len = 1;
    for (const [dr, dc] of dirs) {
      const nr = r + dr, nc = c + dc;
      if (nr >= 0 && nr < m && nc >= 0 && nc < n && matrix[nr][nc] > matrix[r][c]) {
        len = Math.max(len, 1 + dfs(nr, nc));
      }
    }
    memo[r][c] = len;
    return len;
  }
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      maxPath = Math.max(maxPath, dfs(i, j));
    }
  }
  return maxPath;
}`,
    functionName: 'longestIncreasingPath',
    testCases: [
      { id: 1, input: [[[9, 9, 4], [6, 6, 8], [2, 1, 1]]], expected: 4, inputDisplay: 'matrix = [[9,9,4],[6,6,8],[2,1,1]]', expectedDisplay: '4' },
      { id: 2, input: [[[3, 4, 5], [3, 2, 6], [2, 2, 1]]], expected: 4, inputDisplay: 'matrix = [[3,4,5],[3,2,6],[2,2,1]]', expectedDisplay: '4' },
      { id: 3, input: [[[1]]], expected: 1, inputDisplay: 'matrix = [[1]]', expectedDisplay: '1' },
      { id: 4, input: [[[1, 2], [3, 4]]], expected: 3, inputDisplay: 'matrix = 2x2 grid', expectedDisplay: '3', isHidden: true },
      { id: 5, input: [[[7, 8, 9], [9, 7, 6], [7, 2, 3]]], expected: 6, inputDisplay: 'matrix = serpentine path', expectedDisplay: '6', isHidden: true },
      { id: 6, input: [[[1, 2, 3, 4, 5]]], expected: 5, inputDisplay: 'single row increasing 1..5', expectedDisplay: '5', isHidden: true },
      { id: 7, input: [[[5], [4], [3], [2], [1]]], expected: 5, inputDisplay: 'single column decreasing 5..1', expectedDisplay: '5', isHidden: true },
      { id: 8, input: [[[2, 2, 2], [2, 2, 2]]], expected: 1, inputDisplay: 'all identical cells', expectedDisplay: '1', isHidden: true },
      { id: 9, input: [[[1, 2], [2, 3]]], expected: 3, inputDisplay: 'matrix with equal adjacents', expectedDisplay: '3', isHidden: true },
      { id: 10, input: [[[0, 1, 2, 3], [7, 6, 5, 4]]], expected: 8, inputDisplay: '2x4 continuous snake', expectedDisplay: '8', isHidden: true },
    ],
    hints: ['Model the matrix as a Directed Acyclic Graph (DAG) with edges from smaller to strictly larger neighbors. Use DFS with memoization.'],
    python: {
      starterCode: `def longestIncreasingPath(matrix):
    return 0
`,
      solutionCode: `def longestIncreasingPath(matrix):
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    memo = [[0] * n for _ in range(m)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def dfs(r, c):
        if memo[r][c] != 0:
            return memo[r][c]
        length = 1
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] > matrix[r][c]:
                length = max(length, 1 + dfs(nr, nc))
        memo[r][c] = length
        return length
    return max(dfs(r, c) for r in range(m) for c in range(n))
`,
    },
    leetcodeId: 329,
    leetcodeTitle: 'Longest Increasing Path in a Matrix',
    leetcodeUrl: 'https://leetcode.com/problems/longest-increasing-path-in-a-matrix/',
  },

  // ==========================================
  // TOPIC 4: BINARY SEARCH & GREEDY (2 Medium, 1 Hard)
  // ==========================================
  {
    id: 'koko-eating-bananas',
    wingId: 'binary-search-greedy',
    floor: 18,
    title: 'Koko Eating Bananas (Binary Search on Answer)',
    difficulty: 'medium',
    visualizerType: 'array',
    monster: {
      id: 'voracious-kong',
      name: 'Voracious Kong of the Logarithmic Horizon',
      title: 'Beast of Rate Optimization',
      maxHp: 4,
      hp: 4,
      sprite: 'gargoyle',
      color: '#f59e0b',
      attackName: 'Pancake Banana Barrel Barrage',
      attackPower: 2,
      defeatQuote: 'You found the exact integer rate speed to outrun the guard...',
    },
    description: `Koko loves to eat bananas. There are \`n\` piles of bananas, the \`i-th\` pile has \`piles[i]\` bananas. The guards will return in \`h\` hours.

Koko can decide her bananas-per-hour eating speed of \`k\`. Each hour, she chooses some pile of bananas and eats \`k\` bananas from that pile. If the pile has less than \`k\` bananas, she eats all of them and will not eat any more bananas during this hour.

Return the minimum integer \`k\` such that she can eat all the bananas within \`h\` hours.`,
    examples: [
      { input: 'piles = [3,6,7,11], h = 8', output: '4' },
      { input: 'piles = [30,11,23,4,20], h = 5', output: '30' },
      { input: 'piles = [30,11,23,4,20], h = 6', output: '23' },
    ],
    constraints: ['1 <= piles.length <= 10^4', 'piles.length <= h <= 10^9', '1 <= piles[i] <= 10^9'],
    starterCode: `function minEatingSpeed(piles, h) {
  return 1;
}`,
    solutionCode: `function minEatingSpeed(piles, h) {
  let low = 1, high = Math.max(...piles);
  let ans = high;
  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    let hours = 0;
    for (const p of piles) {
      hours += Math.ceil(p / mid);
    }
    if (hours <= h) {
      ans = mid;
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }
  return ans;
}`,
    functionName: 'minEatingSpeed',
    testCases: [
      { id: 1, input: [[3, 6, 7, 11], 8], expected: 4, inputDisplay: 'piles = [3,6,7,11], h = 8', expectedDisplay: '4' },
      { id: 2, input: [[30, 11, 23, 4, 20], 5], expected: 30, inputDisplay: 'piles = [30,11,23,4,20], h = 5', expectedDisplay: '30' },
      { id: 3, input: [[30, 11, 23, 4, 20], 6], expected: 23, inputDisplay: 'piles = [30,11,23,4,20], h = 6', expectedDisplay: '23' },
      { id: 4, input: [[312884470], 312884469], expected: 2, inputDisplay: 'large single pile', expectedDisplay: '2', isHidden: true },
      { id: 5, input: [[1000000000], 2], expected: 500000000, inputDisplay: '10^9 bananas in 2h', expectedDisplay: '500000000', isHidden: true },
      { id: 6, input: [[1, 1, 1, 1], 4], expected: 1, inputDisplay: 'all 1s matching h', expectedDisplay: '1', isHidden: true },
      { id: 7, input: [[5, 5, 5], 6], expected: 3, inputDisplay: 'piles = [5,5,5], h = 6', expectedDisplay: '3', isHidden: true },
      { id: 8, input: [[2, 2], 2], expected: 2, inputDisplay: 'piles = [2,2], h = 2', expectedDisplay: '2', isHidden: true },
      { id: 9, input: [[10, 20, 30], 100], expected: 1, inputDisplay: 'large hour budget', expectedDisplay: '1', isHidden: true },
      { id: 10, input: [[15, 20, 25, 30], 10], expected: 10, inputDisplay: 'piles = [15,20,25,30], h = 10', expectedDisplay: '10', isHidden: true },
    ],
    hints: ['Binary search the candidate speed k in [1, max(piles)]. For each speed, compute the total ceiling hours needed.'],
    python: {
      starterCode: `def minEatingSpeed(piles, h):
    return 1
`,
      solutionCode: `def minEatingSpeed(piles, h):
    import math
    low, high = 1, max(piles)
    ans = high
    while low <= high:
        mid = (low + high) // 2
        hours = sum(math.ceil(p / mid) for p in piles)
        if hours <= h:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
`,
    },
    leetcodeId: 875,
    leetcodeTitle: 'Koko Eating Bananas',
    leetcodeUrl: 'https://leetcode.com/problems/koko-eating-bananas/',
  },
  {
    id: 'jump-game-ii',
    wingId: 'binary-search-greedy',
    floor: 19,
    title: 'Jump Game II (Greedy Window Extension)',
    difficulty: 'medium',
    visualizerType: 'array',
    monster: {
      id: 'leaping-behemoth',
      name: 'Leaping Behemoth of Minimum Strides',
      title: 'Titan of Optimal Interval Strides',
      maxHp: 4,
      hp: 4,
      sprite: 'slime',
      color: '#eab308',
      attackName: 'Spring-Loaded Leap Smash',
      attackPower: 2,
      defeatQuote: 'You crossed my chasm in the exact theoretical minimum jumps...',
    },
    description: `You are given a 0-indexed array of integers \`nums\` of length \`n\`. You are initially positioned at \`nums[0]\`. Each element \`nums[i]\` represents the maximum length of a forward jump from index \`i\`.

Return the minimum number of jumps to reach \`nums[n - 1]\`. You can assume that you can always reach the last index.`,
    examples: [
      { input: 'nums = [2,3,1,1,4]', output: '2', explanation: 'Jump 1 step from index 0 to 1, then 3 steps to the last index.' },
      { input: 'nums = [2,3,0,1,4]', output: '2' },
    ],
    constraints: ['1 <= nums.length <= 10^4', '0 <= nums[i] <= 1000'],
    starterCode: `function jump(nums) {
  return 0;
}`,
    solutionCode: `function jump(nums) {
  let jumps = 0, currentEnd = 0, farthest = 0;
  for (let i = 0; i < nums.length - 1; i++) {
    farthest = Math.max(farthest, i + nums[i]);
    if (i === currentEnd) {
      jumps++;
      currentEnd = farthest;
    }
  }
  return jumps;
}`,
    functionName: 'jump',
    testCases: [
      { id: 1, input: [[2, 3, 1, 1, 4]], expected: 2, inputDisplay: 'nums = [2,3,1,1,4]', expectedDisplay: '2' },
      { id: 2, input: [[2, 3, 0, 1, 4]], expected: 2, inputDisplay: 'nums = [2,3,0,1,4]', expectedDisplay: '2' },
      { id: 3, input: [[0]], expected: 0, inputDisplay: 'nums = [0]', expectedDisplay: '0' },
      { id: 4, input: [[1, 2]], expected: 1, inputDisplay: 'nums = [1,2]', expectedDisplay: '1', isHidden: true },
      { id: 5, input: [[1, 1, 1, 1]], expected: 3, inputDisplay: 'nums = [1,1,1,1]', expectedDisplay: '3', isHidden: true },
      { id: 6, input: [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1, 0]], expected: 2, inputDisplay: 'huge initial jump', expectedDisplay: '2', isHidden: true },
      { id: 7, input: [[2, 1]], expected: 1, inputDisplay: 'nums = [2,1]', expectedDisplay: '1', isHidden: true },
      { id: 8, input: [[3, 2, 1, 1, 1]], expected: 2, inputDisplay: 'nums = [3,2,1,1,1]', expectedDisplay: '2', isHidden: true },
      { id: 9, input: [[1, 2, 3]], expected: 2, inputDisplay: 'nums = [1,2,3]', expectedDisplay: '2', isHidden: true },
      { id: 10, input: [[7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]], expected: 2, inputDisplay: 'scattered big steps', expectedDisplay: '2', isHidden: true },
    ],
    hints: ['Greedily record the farthest reachable index. When you reach the boundary of the current jump, increment jumps and update the boundary to the farthest point.'],
    python: {
      starterCode: `def jump(nums):
    return 0
`,
      solutionCode: `def jump(nums):
    jumps, curr_end, farthest = 0, 0, 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == curr_end:
            jumps += 1
            curr_end = farthest
    return jumps
`,
    },
    leetcodeId: 45,
    leetcodeTitle: 'Jump Game II',
    leetcodeUrl: 'https://leetcode.com/problems/jump-game-ii/',
  },
  {
    id: 'trapping-rain-water',
    wingId: 'binary-search-greedy',
    floor: 20,
    title: 'Boss Chamber: Trapping Rain Water (Two-Pointer Monotonic Boundary)',
    difficulty: 'hard',
    visualizerType: 'array',
    monster: {
      id: 'abyssal-aquifer',
      name: 'Cataclysmic Abyssal Aquifer',
      title: 'Leviathan of Inundated Ravines',
      maxHp: 4,
      hp: 4,
      sprite: 'dragon',
      color: '#2563eb',
      attackName: 'Tidal Monotonic Deluge',
      attackPower: 3,
      defeatQuote: 'You trapped all the volume across my elevation bars...',
    },
    description: `Given \`n\` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.`,
    examples: [
      { input: 'height = [0,1,0,2,1,0,1,3,2,1,2,1]', output: '6' },
      { input: 'height = [4,2,0,3,2,5]', output: '9' },
    ],
    constraints: ['n == height.length', '1 <= n <= 2 * 10^4', '0 <= height[i] <= 10^5'],
    starterCode: `function trap(height) {
  return 0;
}`,
    solutionCode: `function trap(height) {
  if (!height || height.length === 0) return 0;
  let left = 0, right = height.length - 1;
  let leftMax = 0, rightMax = 0;
  let totalWater = 0;
  while (left < right) {
    if (height[left] < height[right]) {
      if (height[left] >= leftMax) leftMax = height[left];
      else totalWater += leftMax - height[left];
      left++;
    } else {
      if (height[right] >= rightMax) rightMax = height[right];
      else totalWater += rightMax - height[right];
      right--;
    }
  }
  return totalWater;
}`,
    functionName: 'trap',
    testCases: [
      { id: 1, input: [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]], expected: 6, inputDisplay: 'height = [0,1,0,2,1,0,1,3,2,1,2,1]', expectedDisplay: '6' },
      { id: 2, input: [[4, 2, 0, 3, 2, 5]], expected: 9, inputDisplay: 'height = [4,2,0,3,2,5]', expectedDisplay: '9' },
      { id: 3, input: [[0]], expected: 0, inputDisplay: 'height = [0]', expectedDisplay: '0' },
      { id: 4, input: [[3, 0, 3]], expected: 3, inputDisplay: 'height = [3,0,3]', expectedDisplay: '3', isHidden: true },
      { id: 5, input: [[5, 4, 1, 2]], expected: 1, inputDisplay: 'height = [5,4,1,2]', expectedDisplay: '1', isHidden: true },
      { id: 6, input: [[0, 2, 0]], expected: 0, inputDisplay: 'height = [0,2,0]', expectedDisplay: '0', isHidden: true },
      { id: 7, input: [[2, 0, 2]], expected: 2, inputDisplay: 'height = [2,0,2]', expectedDisplay: '2', isHidden: true },
      { id: 8, input: [[5, 2, 1, 2, 1, 5]], expected: 14, inputDisplay: 'height = deep valley', expectedDisplay: '14', isHidden: true },
      { id: 9, input: [[1, 2, 3, 4, 5]], expected: 0, inputDisplay: 'strictly ascending', expectedDisplay: '0', isHidden: true },
      { id: 10, input: [[5, 4, 3, 2, 1]], expected: 0, inputDisplay: 'strictly descending', expectedDisplay: '0', isHidden: true },
    ],
    hints: ['Use two pointers moving inward. Maintain leftMax and rightMax; the water trapped at any position is bounded by min(leftMax, rightMax) - height.'],
    python: {
      starterCode: `def trap(height):
    return 0
`,
      solutionCode: `def trap(height):
    if not height:
        return 0
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
`,
    },
    leetcodeId: 42,
    leetcodeTitle: 'Trapping Rain Water',
    leetcodeUrl: 'https://leetcode.com/problems/trapping-rain-water/',
  },

  // ==========================================
  // TOPIC 5: BIT MANIPULATION (2 Medium, 1 Hard)
  // ==========================================
  {
    id: 'divide-two-integers',
    wingId: 'bit-manipulation',
    floor: 18,
    title: 'Divide Two Integers (Bit Shift Subtraction)',
    difficulty: 'medium',
    visualizerType: 'bits',
    monster: {
      id: 'quotient-wraith',
      name: 'Quotient Wraith of Binary Halving',
      title: 'Phantom of Integer Division without Operators',
      maxHp: 4,
      hp: 4,
      sprite: 'lich',
      color: '#a855f7',
      attackName: 'Bitwise Long Division Beam',
      attackPower: 2,
      defeatQuote: 'Shifted and subtracted my essence until the remainder perished...',
    },
    description: `Given two integers \`dividend\` and \`divisor\`, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero. Return the quotient after dividing dividend by divisor. Clamp within the 32-bit signed integer range \`[-2^31, 2^31 - 1]\`.`,
    examples: [
      { input: 'dividend = 10, divisor = 3', output: '3', explanation: '10/3 = 3.33333.. which is truncated to 3.' },
      { input: 'dividend = 7, divisor = -3', output: '-2', explanation: '7/-3 = -2.33333.. which is truncated to -2.' },
    ],
    constraints: ['-2^31 <= dividend, divisor <= 2^31 - 1', 'divisor != 0'],
    starterCode: `function divide(dividend, divisor) {
  return 0;
}`,
    solutionCode: `function divide(dividend, divisor) {
  const MAX = 2147483647;
  const MIN = -2147483648;
  if (dividend === MIN && divisor === -1) return MAX;
  const negative = (dividend < 0) !== (divisor < 0);
  let a = Math.abs(dividend);
  let b = Math.abs(divisor);
  let quotient = 0;
  while (a >= b) {
    let temp = b, multiple = 1;
    while (a >= temp * 2 && temp * 2 > 0) {
      temp *= 2;
      multiple *= 2;
    }
    a -= temp;
    quotient += multiple;
  }
  return negative ? -quotient : quotient;
}`,
    functionName: 'divide',
    testCases: [
      { id: 1, input: [10, 3], expected: 3, inputDisplay: 'dividend = 10, divisor = 3', expectedDisplay: '3' },
      { id: 2, input: [7, -3], expected: -2, inputDisplay: 'dividend = 7, divisor = -3', expectedDisplay: '-2' },
      { id: 3, input: [0, 1], expected: 0, inputDisplay: 'dividend = 0, divisor = 1', expectedDisplay: '0' },
      { id: 4, input: [-2147483648, -1], expected: 2147483647, inputDisplay: 'overflow clamp case', expectedDisplay: '2147483647', isHidden: true },
      { id: 5, input: [1, 1], expected: 1, inputDisplay: 'dividend = 1, divisor = 1', expectedDisplay: '1', isHidden: true },
      { id: 6, input: [-1, 1], expected: -1, inputDisplay: 'dividend = -1, divisor = 1', expectedDisplay: '-1', isHidden: true },
      { id: 7, input: [2147483647, 2], expected: 1073741823, inputDisplay: 'large dividend halving', expectedDisplay: '1073741823', isHidden: true },
      { id: 8, input: [-2147483648, 1], expected: -2147483648, inputDisplay: 'min 32-bit int / 1', expectedDisplay: '-2147483648', isHidden: true },
      { id: 9, input: [100, 10], expected: 10, inputDisplay: 'dividend = 100, divisor = 10', expectedDisplay: '10', isHidden: true },
      { id: 10, input: [-100, -25], expected: 4, inputDisplay: 'dividend = -100, divisor = -25', expectedDisplay: '4', isHidden: true },
    ],
    hints: ['Double the divisor using bit shifts (divisor << 1) repeatedly until it exceeds the remaining dividend, then subtract and add the power of two to quotient.'],
    python: {
      starterCode: `def divide(dividend, divisor):
    return 0
`,
      solutionCode: `def divide(dividend, divisor):
    MAX = 2147483647
    MIN = -2147483648
    if dividend == MIN and divisor == -1:
        return MAX
    negative = (dividend < 0) ^ (divisor < 0)
    a, b = abs(dividend), abs(divisor)
    quotient = 0
    while a >= b:
        temp, mult = b, 1
        while a >= (temp << 1):
            temp <<= 1
            mult <<= 1
        a -= temp
        quotient += mult
    return -quotient if negative else quotient
`,
    },
    leetcodeId: 29,
    leetcodeTitle: 'Divide Two Integers',
    leetcodeUrl: 'https://leetcode.com/problems/divide-two-integers/',
  },
  {
    id: 'find-the-duplicate-number',
    wingId: 'bit-manipulation',
    floor: 19,
    title: 'Find the Duplicate Number (Bit Count Parity)',
    difficulty: 'medium',
    visualizerType: 'bits',
    monster: {
      id: 'doppelganger-spectre',
      name: 'Doppelganger Spectre of Pigeonhole Parity',
      title: 'Phantom of the Extra Value',
      maxHp: 4,
      hp: 4,
      sprite: 'lich',
      color: '#6366f1',
      attackName: 'Pigeonhole Phase Siphon',
      attackPower: 2,
      defeatQuote: 'Cycle detected: the duplicate identity stood revealed...',
    },
    description: `Given an array of integers \`nums\` containing \`n + 1\` integers where each integer is in the range \`[1, n]\` inclusive. There is only one repeated number in \`nums\`, return this repeated number.

You must solve the problem without modifying the array and uses only constant extra space.`,
    examples: [
      { input: 'nums = [1,3,4,2,2]', output: '2' },
      { input: 'nums = [3,1,3,4,2]', output: '3' },
      { input: 'nums = [3,3,3,3,3]', output: '3' },
    ],
    constraints: ['1 <= n <= 10^5', 'nums.length == n + 1', '1 <= nums[i] <= n'],
    starterCode: `function findDuplicate(nums) {
  return 0;
}`,
    solutionCode: `function findDuplicate(nums) {
  let slow = nums[0], fast = nums[0];
  do {
    slow = nums[slow];
    fast = nums[nums[fast]];
  } while (slow !== fast);
  slow = nums[0];
  while (slow !== fast) {
    slow = nums[slow];
    fast = nums[fast];
  }
  return slow;
}`,
    functionName: 'findDuplicate',
    testCases: [
      { id: 1, input: [[1, 3, 4, 2, 2]], expected: 2, inputDisplay: 'nums = [1,3,4,2,2]', expectedDisplay: '2' },
      { id: 2, input: [[3, 1, 3, 4, 2]], expected: 3, inputDisplay: 'nums = [3,1,3,4,2]', expectedDisplay: '3' },
      { id: 3, input: [[3, 3, 3, 3, 3]], expected: 3, inputDisplay: 'nums = [3,3,3,3,3]', expectedDisplay: '3' },
      { id: 4, input: [[2, 2, 2, 2, 2]], expected: 2, inputDisplay: 'nums = [2,2,2,2,2]', expectedDisplay: '2', isHidden: true },
      { id: 5, input: [[1, 2, 2]], expected: 2, inputDisplay: 'nums = [1,2,2]', expectedDisplay: '2', isHidden: true },
      { id: 6, input: [[2, 1, 2]], expected: 2, inputDisplay: 'nums = [2,1,2]', expectedDisplay: '2', isHidden: true },
      { id: 7, input: [[1, 4, 4, 2, 3]], expected: 4, inputDisplay: 'nums = [1,4,4,2,3]', expectedDisplay: '4', isHidden: true },
      { id: 8, input: [[4, 3, 1, 4, 2]], expected: 4, inputDisplay: 'nums = [4,3,1,4,2]', expectedDisplay: '4', isHidden: true },
      { id: 9, input: [[1, 1]], expected: 1, inputDisplay: 'nums = [1,1]', expectedDisplay: '1', isHidden: true },
      { id: 10, input: [[1, 2, 3, 4, 5, 6, 7, 8, 9, 5]], expected: 5, inputDisplay: 'nums = [1..9, 5]', expectedDisplay: '5', isHidden: true },
    ],
    hints: ['Treat the array indices and values as a linked list (i -> nums[i]). Since a number is duplicated, a cycle exists. Use Floyd\'s Tortoise and Hare.'],
    python: {
      starterCode: `def findDuplicate(nums):
    return 0
`,
      solutionCode: `def findDuplicate(nums):
    slow, fast = nums[0], nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
`,
    },
    leetcodeId: 287,
    leetcodeTitle: 'Find the Duplicate Number',
    leetcodeUrl: 'https://leetcode.com/problems/find-the-duplicate-number/',
  },
  {
    id: 'number-of-valid-words-for-each-puzzle',
    wingId: 'bit-manipulation',
    floor: 20,
    title: 'Boss Chamber: Number of Valid Words for Each Puzzle (Bitmask Submask Enumeration)',
    difficulty: 'hard',
    visualizerType: 'bits',
    monster: {
      id: 'cryptarch-sphinx',
      name: 'Cryptarch Sphinx of 26 Bit Masks',
      title: 'Emperor of Alphabet Submasks',
      maxHp: 4,
      hp: 4,
      sprite: 'lich',
      color: '#e11d48',
      attackName: 'Submask Enumeration Blast',
      attackPower: 3,
      defeatQuote: 'All submasks collapsed before your bitwise deduction...',
    },
    description: `With respect to a given \`puzzle\` string, a \`word\` is valid if:
- \`word\` contains the first letter of \`puzzle\`.
- For each letter in \`word\`, that letter is in \`puzzle\`.

Return an array \`answer\`, where \`answer[i]\` is the number of words in the given word list \`words\` that are valid with respect to the puzzle \`puzzles[i]\`.`,
    examples: [
      { input: 'words = ["aaaa","asas","able","ability","actt","actor","access"], puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]', output: '[1,1,3,2,4,0]' },
      { input: 'words = ["apple","plea","please"], puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]', output: '[0,1,3,2,0]' },
    ],
    constraints: ['1 <= words.length <= 10^5', '4 <= words[i].length <= 50', '1 <= puzzles.length <= 10^4', 'puzzles[i].length == 7', 'words[i] and puzzles[i] consist of lowercase English letters.'],
    starterCode: `function findNumOfValidWords(words, puzzles) {
  return [];
}`,
    solutionCode: `function findNumOfValidWords(words, puzzles) {
  const wordCount = new Map();
  for (const w of words) {
    let mask = 0;
    for (let i = 0; i < w.length; i++) {
      mask |= (1 << (w.charCodeAt(i) - 97));
    }
    wordCount.set(mask, (wordCount.get(mask) || 0) + 1);
  }
  const res = [];
  for (const p of puzzles) {
    const firstBit = 1 << (p.charCodeAt(0) - 97);
    let mask = 0;
    for (let i = 0; i < p.length; i++) {
      mask |= (1 << (p.charCodeAt(i) - 97));
    }
    let count = 0;
    let submask = mask;
    while (submask > 0) {
      if ((submask & firstBit) !== 0) {
        count += wordCount.get(submask) || 0;
      }
      submask = (submask - 1) & mask;
    }
    res.push(count);
  }
  return res;
}`,
    functionName: 'findNumOfValidWords',
    testCases: [
      { id: 1, input: [['aaaa', 'asas', 'able', 'ability', 'actt', 'actor', 'access'], ['aboveyz', 'abrodyz', 'abslute', 'absoryz', 'actresz', 'gaswxyz']], expected: [1, 1, 3, 2, 4, 0], inputDisplay: '7 words, 6 puzzles', expectedDisplay: '[1,1,3,2,4,0]' },
      { id: 2, input: [['apple', 'plea', 'please'], ['aelwxyz', 'aelpxyz', 'aelpsxy', 'saelpxy', 'xaelpsy']], expected: [0, 2, 3, 1, 0], inputDisplay: '3 words, 5 puzzles', expectedDisplay: '[0,2,3,1,0]' },
      { id: 3, input: [['abc', 'ab', 'a'], ['abcdefg']], expected: [3], inputDisplay: 'words with common subsets', expectedDisplay: '[3]' },
      { id: 4, input: [['abcd'], ['abcdefg', 'bcdefga']], expected: [1, 1], inputDisplay: 'first character required constraint', expectedDisplay: '[1,1]', isHidden: true },
      { id: 5, input: [['cat', 'dog', 'bird'], ['actwxyz', 'dogwxyz']], expected: [1, 1], inputDisplay: '2 puzzles matching exactly 1 word', expectedDisplay: '[1,1]', isHidden: true },
      { id: 6, input: [['zzzz'], ['zabcdef']], expected: [1], inputDisplay: 'single letter mask', expectedDisplay: '[1]', isHidden: true },
      { id: 7, input: [['abcdefg'], ['abcdefg']], expected: [1], inputDisplay: 'exact 7-letter match', expectedDisplay: '[1]', isHidden: true },
      { id: 8, input: [['hijk'], ['abcdefg']], expected: [0], inputDisplay: 'disjoint character sets', expectedDisplay: '[0]', isHidden: true },
      { id: 9, input: [['a', 'b', 'c'], ['abcdefg', 'bacdefg']], expected: [1, 1], inputDisplay: 'first letter exclusivity', expectedDisplay: '[1,1]', isHidden: true },
      { id: 10, input: [['hello', 'world'], ['helowxy', 'wordlxy']], expected: [1, 1], inputDisplay: 'common english words', expectedDisplay: '[1,1]', isHidden: true },
    ],
    hints: ['Represent each word as a 26-bit bitmask. Each puzzle has length 7, so iterate over all 2^7 = 128 submasks using submask = (submask - 1) & mask.'],
    python: {
      starterCode: `def findNumOfValidWords(words, puzzles):
    return []
`,
      solutionCode: `def findNumOfValidWords(words, puzzles):
    from collections import Counter
    word_count = Counter()
    for w in words:
        mask = 0
        for ch in w:
            mask |= 1 << (ord(ch) - 97)
        word_count[mask] += 1
    res = []
    for p in puzzles:
        first_bit = 1 << (ord(p[0]) - 97)
        mask = 0
        for ch in p:
            mask |= 1 << (ord(ch) - 97)
        count = 0
        submask = mask
        while submask > 0:
            if submask & first_bit:
                count += word_count[submask]
            submask = (submask - 1) & mask
        res.append(count)
    return res
`,
    },
    leetcodeId: 1178,
    leetcodeTitle: 'Number of Valid Words for Each Puzzle',
    leetcodeUrl: 'https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/',
  },
];

async function main() {
  console.log('🚀 BUILDING ALGODUNGEON PROBLEMS DATABASE (PHASE 1 ON-DEMAND JSON ARCHITECTURE)...');

  const outputDir = path.join(process.cwd(), 'public', 'problems', 'data');
  const catalogPath = path.join(process.cwd(), 'public', 'problems', 'catalog.json');
  fs.mkdirSync(outputDir, { recursive: true });

  const allList: SerializedProblem[] = [];

  // 1. Process 83 existing problems
  for (const [topic, problems] of Object.entries(allProblems)) {
    for (const prob of problems) {
      const enrichedTests = getEnrichedTestCases(prob);
      const py = pythonCurriculum[prob.id] || { starterCode: prob.starterCode, solutionCode: prob.solutionCode };
      const lc = leetcodeMapping[prob.id];

      const serialized: SerializedProblem = {
        id: prob.id,
        wingId: prob.wingId,
        floor: prob.floor,
        title: prob.title,
        difficulty: prob.difficulty,
        visualizerType: prob.visualizerType,
        monster: { ...prob.monster, maxHp: enrichedTests.length, hp: enrichedTests.length },
        description: prob.description,
        examples: prob.examples,
        constraints: prob.constraints,
        starterCode: prob.starterCode,
        solutionCode: prob.solutionCode,
        functionName: prob.functionName,
        testCases: enrichedTests,
        hints: prob.hints,
        python: py,
        leetcodeId: lc?.id,
        leetcodeTitle: lc?.title,
        leetcodeUrl: lc?.url,
      };

      allList.push(serialized);
    }
  }

  // 2. Add 15 new Medium and Hard problems
  allList.push(...newProblems);

  // Clean problem titles: remove all guide/technique hints (e.g. "(Hash Map)", "(Stack)")
  for (const p of allList) {
    const lc = leetcodeMapping[p.id];
    if (lc?.title) {
      p.title = lc.title;
    } else {
      p.title = p.title
        .replace(/^Boss Chamber:\s*/i, '')
        .replace(/\s*\([^)]*\)$/, '')
        .trim();
    }
  }

  console.log(`📦 Total problems assembled: ${allList.length}`);

  // 3. Write individual JSON files
  const catalog: CatalogEntry[] = [];

  for (const p of allList) {
    const filePath = path.join(outputDir, `${p.id}.json`);
    fs.writeFileSync(filePath, JSON.stringify(p, null, 2), 'utf-8');

    catalog.push({
      id: p.id,
      wingId: p.wingId,
      floor: p.floor,
      title: p.title,
      difficulty: p.difficulty,
      visualizerType: p.visualizerType,
      leetcodeId: p.leetcodeId,
      leetcodeTitle: p.leetcodeTitle,
      leetcodeUrl: p.leetcodeUrl,
      monster: p.monster,
    });
  }

  // 4. Write catalog.json and src/data/problems/catalog.ts
  fs.writeFileSync(catalogPath, JSON.stringify(catalog, null, 2), 'utf-8');
  console.log(`✅ Saved catalog.json with ${catalog.length} entries (${(fs.statSync(catalogPath).size / 1024).toFixed(1)} KB)`);

  const tsCatalogPath = path.join(process.cwd(), 'src', 'data', 'problems', 'catalog.ts');
  const tsContent = `// Auto-generated by scripts/buildProblemsDatabase.ts - DO NOT EDIT MANUALLY
import { DungeonTopic, Difficulty } from '../../types/game';

export interface CatalogEntry {
  id: string;
  wingId: DungeonTopic;
  floor: number;
  title: string;
  difficulty: Difficulty;
  visualizerType: string;
  leetcodeId?: number;
  leetcodeTitle?: string;
  leetcodeUrl?: string;
  monster: {
    id: string;
    name: string;
    title: string;
    maxHp: number;
    hp: number;
    sprite: string;
    color: string;
    attackName: string;
    attackPower: number;
    defeatQuote: string;
  };
}

export const problemCatalog: CatalogEntry[] = ${JSON.stringify(catalog, null, 2)};
`;
  fs.writeFileSync(tsCatalogPath, tsContent, 'utf-8');
  console.log(`✅ Emitted src/data/problems/catalog.ts`);
  console.log(`✅ Emitted ${allList.length} problem JSON files to public/problems/data/`);
}

main().catch(console.error);
