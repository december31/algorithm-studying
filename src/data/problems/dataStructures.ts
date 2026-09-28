import { Problem } from '../../types/problem';
import { ArrayFrame, StackFrame } from '../../types/visualizer';

export const dataStructureProblems: Problem[] = [
  // 🟢 EASY (8 Problems)
  {
    id: 'two-sum',
    wingId: 'data-structures',
    floor: 1,
    title: 'Two Sum (Hash Map)',
    difficulty: 'easy',
    visualizerType: 'array',
    monster: {
      id: 'goblin-scout',
      name: 'Grom the Key Goblin',
      title: 'Scavenger of Key-Value Shards',
      maxHp: 3,
      hp: 3,
      sprite: 'goblin',
      color: '#eab308',
      attackName: 'Rusty Dagger Shank',
      attackPower: 1,
      defeatQuote: 'Grom could not find complement in time...',
    },
    description: `Given an array of integers \`nums\` and an integer \`target\`, return the indices of the two numbers such that they add up to \`target\`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.`,
    examples: [
      { input: 'nums = [2, 7, 11, 15], target = 9', output: '[0, 1]' },
      { input: 'nums = [3, 2, 4], target = 6', output: '[1, 2]' },
      { input: 'nums = [3, 3], target = 6', output: '[0, 1]' },
    ],
    constraints: ['2 <= nums.length <= 10^4', '-10^9 <= nums[i] <= 10^9', 'Exactly one valid answer exists.'],
    starterCode: `function twoSum(nums, target) {
  return [];
}`,
    solutionCode: `function twoSum(nums, target) {
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (map.has(complement)) {
      return [map.get(complement), i];
    }
    map.set(nums[i], i);
  }
  return [];
}`,
    functionName: 'twoSum',
    testCases: [
      { id: 1, input: [[2, 7, 11, 15], 9], expected: [0, 1], inputDisplay: 'nums = [2, 7, 11, 15], target = 9', expectedDisplay: '[0, 1]' },
      { id: 2, input: [[3, 2, 4], 6], expected: [1, 2], inputDisplay: 'nums = [3, 2, 4], target = 6', expectedDisplay: '[1, 2]' },
      { id: 3, input: [[3, 3], 6], expected: [0, 1], inputDisplay: 'nums = [3, 3], target = 6', expectedDisplay: '[0, 1]' },
    ],
    hints: ['Store previously seen values in a Hash Map to look up complements in O(1) time.'],
    generateDefaultFrames: (tc) => {
      const nums = tc.input[0];
      const target = tc.input[1];
      const frames: ArrayFrame[] = [];
      frames.push({ type: 'array', array: [...nums], pointers: [{ name: 'target', index: 0, color: '#f59e0b' }], message: `Scan elements checking if (target - num) exists in Map` });
      return frames;
    },
  },
  {
    id: 'valid-parentheses',
    wingId: 'data-structures',
    floor: 2,
    title: 'Valid Parentheses (Stack)',
    difficulty: 'easy',
    visualizerType: 'stack',
    monster: {
      id: 'bracket-imp',
      name: 'Klack the Bracket Imp',
      title: 'Weaver of Nested Enclosures',
      maxHp: 3,
      hp: 3,
      sprite: 'slime',
      color: '#38bdf8',
      attackName: 'Unbalanced Clatter',
      attackPower: 1,
      defeatQuote: 'All my brackets were popped cleanly...',
    },
    description: `Given a string \`s\` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

Open brackets must be closed by the same type of brackets in the correct LIFO order.`,
    examples: [
      { input: 's = "()"', output: 'true' },
      { input: 's = "()[]{}"', output: 'true' },
      { input: 's = "(]"', output: 'false' },
    ],
    constraints: ['1 <= s.length <= 10^4', 's consists of parentheses only \'()[]{}\'.'],
    starterCode: `function isValid(s) {
  return true;
}`,
    solutionCode: `function isValid(s) {
  const stack = [];
  const map = { ')': '(', '}': '{', ']': '[' };
  for (const c of s) {
    if (c === '(' || c === '{' || c === '[') {
      stack.push(c);
    } else {
      if (stack.length === 0 || stack.pop() !== map[c]) return false;
    }
  }
  return stack.length === 0;
}`,
    functionName: 'isValid',
    testCases: [
      { id: 1, input: ['()'], expected: true, inputDisplay: 's = "()"', expectedDisplay: 'true' },
      { id: 2, input: ['()[]{}'], expected: true, inputDisplay: 's = "()[]{}"', expectedDisplay: 'true' },
      { id: 3, input: ['(]'], expected: false, inputDisplay: 's = "(]"', expectedDisplay: 'false' },
    ],
    hints: ['Push opening brackets to stack; on closing bracket, pop and ensure matching pair.'],
    generateDefaultFrames: (tc) => {
      const s = tc.input[0];
      const frames: StackFrame[] = [];
      frames.push({ type: 'stack', stack: [], message: `Processing string "${s}" with LIFO stack` });
      return frames;
    },
  },
  {
    id: 'contains-duplicate',
    wingId: 'data-structures',
    floor: 3,
    title: 'Contains Duplicate (Set)',
    difficulty: 'easy',
    visualizerType: 'array',
    monster: {
      id: 'mirror-slime',
      name: 'Doppel the Cloned Slime',
      title: 'Divider of Identical Souls',
      maxHp: 3,
      hp: 3,
      sprite: 'slime',
      color: '#10b981',
      attackName: 'Mitotic Splash',
      attackPower: 1,
      defeatQuote: 'No duplicates found in my essence...',
    },
    description: `Given an integer array \`nums\`, return \`true\` if any value appears at least twice in the array, and return \`false\` if every element is distinct.`,
    examples: [
      { input: 'nums = [1, 2, 3, 1]', output: 'true' },
      { input: 'nums = [1, 2, 3, 4]', output: 'false' },
      { input: 'nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]', output: 'true' },
    ],
    constraints: ['1 <= nums.length <= 10^5', '-10^9 <= nums[i] <= 10^9'],
    starterCode: `function containsDuplicate(nums) {
  return false;
}`,
    solutionCode: `function containsDuplicate(nums) {
  return new Set(nums).size !== nums.length;
}`,
    functionName: 'containsDuplicate',
    testCases: [
      { id: 1, input: [[1, 2, 3, 1]], expected: true, inputDisplay: 'nums = [1, 2, 3, 1]', expectedDisplay: 'true' },
      { id: 2, input: [[1, 2, 3, 4]], expected: false, inputDisplay: 'nums = [1, 2, 3, 4]', expectedDisplay: 'false' },
      { id: 3, input: [[1, 1, 1, 3, 3, 4, 3, 2, 4, 2]], expected: true, inputDisplay: 'nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]', expectedDisplay: 'true' },
    ],
    hints: ['A Hash Set stores only unique values. Compare set size with array length.'],
    generateDefaultFrames: (tc) => {
      const arr = tc.input[0];
      return [{ type: 'array', array: arr, message: `Insert elements into Set to detect duplicate values` }];
    },
  },
  {
    id: 'valid-anagram',
    wingId: 'data-structures',
    floor: 4,
    title: 'Valid Anagram (Frequency Map)',
    difficulty: 'easy',
    visualizerType: 'array',
    monster: {
      id: 'anagram-shade',
      name: 'Lexis the Scrambled Shade',
      title: 'Distorter of Wordcraft',
      maxHp: 3,
      hp: 3,
      sprite: 'wraith',
      color: '#a855f7',
      attackName: 'Permuted Curse',
      attackPower: 1,
      defeatQuote: 'You balanced every single character tally...',
    },
    description: `Given two strings \`s\` and \`t\`, return \`true\` if \`t\` is an anagram of \`s\`, and \`false\` otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase.`,
    examples: [
      { input: 's = "anagram", t = "nagaram"', output: 'true' },
      { input: 's = "rat", t = "car"', output: 'false' },
    ],
    constraints: ['1 <= s.length, t.length <= 5 * 10^4', 's and t consist of lowercase English letters.'],
    starterCode: `function isAnagram(s, t) {
  return false;
}`,
    solutionCode: `function isAnagram(s, t) {
  if (s.length !== t.length) return false;
  const count = {};
  for (const c of s) count[c] = (count[c] || 0) + 1;
  for (const c of t) {
    if (!count[c]) return false;
    count[c]--;
  }
  return true;
}`,
    functionName: 'isAnagram',
    testCases: [
      { id: 1, input: ['anagram', 'nagaram'], expected: true, inputDisplay: 's = "anagram", t = "nagaram"', expectedDisplay: 'true' },
      { id: 2, input: ['rat', 'car'], expected: false, inputDisplay: 's = "rat", t = "car"', expectedDisplay: 'false' },
      { id: 3, input: ['listen', 'silent'], expected: true, inputDisplay: 's = "listen", t = "silent"', expectedDisplay: 'true' },
    ],
    hints: ['Count character frequencies of s in a hash map, then decrement with t.'],
    generateDefaultFrames: (tc) => {
      return [{ type: 'array', array: tc.input[0].split(''), message: `Comparing frequencies of "${tc.input[0]}" vs "${tc.input[1]}"` }];
    },
  },
  {
    id: 'first-unique-character',
    wingId: 'data-structures',
    floor: 5,
    title: 'First Unique Character in a String (Map)',
    difficulty: 'easy',
    visualizerType: 'array',
    monster: {
      id: 'unique-gargoyle',
      name: 'Singulus the Solitary Sentry',
      title: 'Guardian of Non-Repeating Glyphs',
      maxHp: 3,
      hp: 3,
      sprite: 'gargoyle',
      color: '#06b6d4',
      attackName: 'Echo Stun',
      attackPower: 1,
      defeatQuote: 'The lone glyph has pierced my stony facade...',
    },
    description: `Given a string \`s\`, find the first non-repeating character in it and return its index. If it does not exist, return -1.`,
    examples: [
      { input: 's = "leetcode"', output: '0' },
      { input: 's = "loveleetcode"', output: '2' },
      { input: 's = "aabb"', output: '-1' },
    ],
    constraints: ['1 <= s.length <= 10^5', 's consists of only lowercase English letters.'],
    starterCode: `function firstUniqChar(s) {
  return -1;
}`,
    solutionCode: `function firstUniqChar(s) {
  const count = {};
  for (const c of s) count[c] = (count[c] || 0) + 1;
  for (let i = 0; i < s.length; i++) {
    if (count[s[i]] === 1) return i;
  }
  return -1;
}`,
    functionName: 'firstUniqChar',
    testCases: [
      { id: 1, input: ['leetcode'], expected: 0, inputDisplay: 's = "leetcode"', expectedDisplay: '0' },
      { id: 2, input: ['loveleetcode'], expected: 2, inputDisplay: 's = "loveleetcode"', expectedDisplay: '2' },
      { id: 3, input: ['aabb'], expected: -1, inputDisplay: 's = "aabb"', expectedDisplay: '-1' },
    ],
    hints: ['Two passes: first count all frequencies, then return index of first char with count 1.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0].split(''), message: `Scanning for first frequency === 1 in "${tc.input[0]}"` }],
  },
  {
    id: 'intersection-of-two-arrays',
    wingId: 'data-structures',
    floor: 6,
    title: 'Intersection of Two Arrays (Set)',
    difficulty: 'easy',
    visualizerType: 'array',
    monster: {
      id: 'cross-skeleton',
      name: 'Intersecto the Bone Sifter',
      title: 'Keeper of Common Remnants',
      maxHp: 3,
      hp: 3,
      sprite: 'skeleton',
      color: '#f97316',
      attackName: 'Dual Scythe Cross',
      attackPower: 1,
      defeatQuote: 'Our common ground was shattered...',
    },
    description: `Given two integer arrays \`nums1\` and \`nums2\`, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.`,
    examples: [
      { input: 'nums1 = [1, 2, 2, 1], nums2 = [2, 2]', output: '[2]' },
      { input: 'nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]', output: '[4, 9]' },
    ],
    constraints: ['1 <= nums1.length, nums2.length <= 1000', '0 <= nums1[i], nums2[i] <= 1000'],
    starterCode: `function intersection(nums1, nums2) {
  return [];
}`,
    solutionCode: `function intersection(nums1, nums2) {
  const set1 = new Set(nums1);
  const result = new Set();
  for (const n of nums2) {
    if (set1.has(n)) result.add(n);
  }
  return Array.from(result);
}`,
    functionName: 'intersection',
    testCases: [
      { id: 1, input: [[1, 2, 2, 1], [2, 2]], expected: [2], inputDisplay: 'nums1 = [1,2,2,1], nums2 = [2,2]', expectedDisplay: '[2]' },
      { id: 2, input: [[4, 9, 5], [9, 4, 9, 8, 4]], expected: [9, 4], inputDisplay: 'nums1 = [4,9,5], nums2 = [9,4,9,8,4]', expectedDisplay: '[9, 4]' },
      { id: 3, input: [[1, 2, 3], [4, 5, 6]], expected: [], inputDisplay: 'nums1 = [1,2,3], nums2 = [4,5,6]', expectedDisplay: '[]' },
    ],
    hints: ['Convert the first array into a Set, then filter the second array and deduplicate with another Set.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], secondaryArray: tc.input[1], message: 'Finding common unique elements between sets' }],
  },
  {
    id: 'remove-all-adjacent-duplicates',
    wingId: 'data-structures',
    floor: 7,
    title: 'Remove All Adjacent Duplicates In String (Stack)',
    difficulty: 'easy',
    visualizerType: 'stack',
    monster: {
      id: 'repeater-slime',
      name: 'Echo-Gel the Recursive Slime',
      title: 'Absorber of Adjacent Pairs',
      maxHp: 3,
      hp: 3,
      sprite: 'slime',
      color: '#ec4899',
      attackName: 'Twin Ooze Compression',
      attackPower: 1,
      defeatQuote: 'All my adjacent layers collapsed into void...',
    },
    description: `You are given a string \`s\` consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on \`s\` until we no longer can. Return the final string after all such duplicate removals have been made.`,
    examples: [
      { input: 's = "abbaca"', output: '"ca"' },
      { input: 's = "azxxzy"', output: '"ay"' },
    ],
    constraints: ['1 <= s.length <= 10^5', 's consists of lowercase English letters.'],
    starterCode: `function removeDuplicates(s) {
  return "";
}`,
    solutionCode: `function removeDuplicates(s) {
  const stack = [];
  for (const c of s) {
    if (stack.length > 0 && stack[stack.length - 1] === c) {
      stack.pop();
    } else {
      stack.push(c);
    }
  }
  return stack.join('');
}`,
    functionName: 'removeDuplicates',
    testCases: [
      { id: 1, input: ['abbaca'], expected: 'ca', inputDisplay: 's = "abbaca"', expectedDisplay: '"ca"' },
      { id: 2, input: ['azxxzy'], expected: 'ay', inputDisplay: 's = "azxxzy"', expectedDisplay: '"ay"' },
      { id: 3, input: ['a'], expected: 'a', inputDisplay: 's = "a"', expectedDisplay: '"a"' },
    ],
    hints: ['Use a stack. If the incoming character matches the top of the stack, pop it; otherwise push.'],
    generateDefaultFrames: (tc) => [{ type: 'stack', stack: [], message: `Processing string "${tc.input[0]}" with elimination stack` }],
  },
  {
    id: 'missing-number',
    wingId: 'data-structures',
    floor: 8,
    title: 'Missing Number (Set / Hash)',
    difficulty: 'easy',
    visualizerType: 'array',
    monster: {
      id: 'void-skeleton',
      name: 'Nullus the Void Skeleton',
      title: 'Stealer of the Missing Index',
      maxHp: 3,
      hp: 3,
      sprite: 'skeleton',
      color: '#64748b',
      attackName: 'Arithmetic Void',
      attackPower: 1,
      defeatQuote: 'The gap was found and healed...',
    },
    description: `Given an array \`nums\` containing \`n\` distinct numbers in the range \`[0, n]\`, return the only number in the range that is missing from the array.`,
    examples: [
      { input: 'nums = [3, 0, 1]', output: '2' },
      { input: 'nums = [0, 1]', output: '2' },
      { input: 'nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]', output: '8' },
    ],
    constraints: ['n == nums.length', '1 <= n <= 10^4', '0 <= nums[i] <= n', 'All numbers in nums are unique.'],
    starterCode: `function missingNumber(nums) {
  return 0;
}`,
    solutionCode: `function missingNumber(nums) {
  const n = nums.length;
  const expectedSum = (n * (n + 1)) / 2;
  const actualSum = nums.reduce((a, b) => a + b, 0);
  return expectedSum - actualSum;
}`,
    functionName: 'missingNumber',
    testCases: [
      { id: 1, input: [[3, 0, 1]], expected: 2, inputDisplay: 'nums = [3, 0, 1]', expectedDisplay: '2' },
      { id: 2, input: [[0, 1]], expected: 2, inputDisplay: 'nums = [0, 1]', expectedDisplay: '2' },
      { id: 3, input: [[9, 6, 4, 2, 3, 5, 7, 0, 1]], expected: 8, inputDisplay: 'nums = [9,6,4,2,3,5,7,0,1]', expectedDisplay: '8' },
    ],
    hints: ['The sum of 0..n is n*(n+1)/2. Subtract actual array sum to find missing element.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], message: 'Summing elements to compare with expected arithmetic progression' }],
  },

  // 🟡 MEDIUM (6 Problems)
  {
    id: 'daily-temperatures',
    wingId: 'data-structures',
    floor: 9,
    title: 'Daily Temperatures (Monotonic Stack)',
    difficulty: 'medium',
    visualizerType: 'stack',
    monster: {
      id: 'frost-orc',
      name: 'Brog the Frost Orc',
      title: 'Warden of the Thermal Peak',
      maxHp: 3,
      hp: 3,
      sprite: 'orc',
      color: '#38bdf8',
      attackName: 'Permafrost Cleave',
      attackPower: 2,
      defeatQuote: 'The temperature soared beyond my freezing grasp...',
    },
    description: `Given an array of integers \`temperatures\` represents daily temperatures, return an array \`answer\` such that \`answer[i]\` is the number of days you have to wait after the \`i\`th day to get a warmer temperature. If there is no future day for which this is possible, keep \`answer[i] == 0\` instead.`,
    examples: [
      { input: 'temperatures = [73, 74, 75, 71, 69, 72, 76, 73]', output: '[1, 1, 4, 2, 1, 1, 0, 0]' },
      { input: 'temperatures = [30, 40, 50, 60]', output: '[1, 1, 1, 0]' },
    ],
    constraints: ['1 <= temperatures.length <= 10^5', '30 <= temperatures[i] <= 100'],
    starterCode: `function dailyTemperatures(temperatures) {
  return new Array(temperatures.length).fill(0);
}`,
    solutionCode: `function dailyTemperatures(temperatures) {
  const n = temperatures.length;
  const res = new Array(n).fill(0);
  const stack = [];
  for (let i = 0; i < n; i++) {
    while (stack.length > 0 && temperatures[i] > temperatures[stack[stack.length - 1]]) {
      const prev = stack.pop();
      res[prev] = i - prev;
    }
    stack.push(i);
  }
  return res;
}`,
    functionName: 'dailyTemperatures',
    testCases: [
      { id: 1, input: [[73, 74, 75, 71, 69, 72, 76, 73]], expected: [1, 1, 4, 2, 1, 1, 0, 0], inputDisplay: 'temperatures = [73,74,75,71,69,72,76,73]', expectedDisplay: '[1,1,4,2,1,1,0,0]' },
      { id: 2, input: [[30, 40, 50, 60]], expected: [1, 1, 1, 0], inputDisplay: 'temperatures = [30,40,50,60]', expectedDisplay: '[1,1,1,0]' },
      { id: 3, input: [[30, 60, 90]], expected: [1, 1, 0], inputDisplay: 'temperatures = [30,60,90]', expectedDisplay: '[1,1,0]' },
    ],
    hints: ['Maintain a monotonic decreasing stack of indices. Pop when encountering a warmer day.'],
    generateDefaultFrames: (tc) => [{ type: 'stack', stack: [], message: 'Scanning temperatures with monotonic index stack' }],
  },
  {
    id: 'group-anagrams',
    wingId: 'data-structures',
    floor: 10,
    title: 'Group Anagrams (Map + Sorting)',
    difficulty: 'medium',
    visualizerType: 'array',
    monster: {
      id: 'cipher-wraith',
      name: 'Vesper the Cipher Wraith',
      title: 'Sorcerer of Sorted Canonical Keys',
      maxHp: 3,
      hp: 3,
      sprite: 'wraith',
      color: '#8b5cf6',
      attackName: 'Permutational Drain',
      attackPower: 2,
      defeatQuote: 'My anagram clusters were canonicalized and banished...',
    },
    description: `Given an array of strings \`strs\`, group the anagrams together. You can return the answer in any order.`,
    examples: [
      { input: 'strs = ["eat","tea","tan","ate","nat","bat"]', output: '[["bat"],["nat","tan"],["ate","eat","tea"]]' },
      { input: 'strs = [""]', output: '[[""]]' },
      { input: 'strs = ["a"]', output: '[["a"]]' },
    ],
    constraints: ['1 <= strs.length <= 10^4', '0 <= strs[i].length <= 100', 'strs[i] consists of lowercase English letters.'],
    starterCode: `function groupAnagrams(strs) {
  return [];
}`,
    solutionCode: `function groupAnagrams(strs) {
  const map = {};
  for (const s of strs) {
    const key = s.split('').sort().join('');
    if (!map[key]) map[key] = [];
    map[key].push(s);
  }
  return Object.values(map);
}`,
    functionName: 'groupAnagrams',
    testCases: [
      { id: 1, input: [["eat","tea","tan","ate","nat","bat"]], expected: [["eat","tea","ate"],["tan","nat"],["bat"]], inputDisplay: 'strs = ["eat","tea","tan","ate","nat","bat"]', expectedDisplay: '[["eat","tea","ate"],["tan","nat"],["bat"]]' },
      { id: 2, input: [[""]], expected: [[""]], inputDisplay: 'strs = [""]', expectedDisplay: '[[""]]' },
      { id: 3, input: [["a"]], expected: [["a"]], inputDisplay: 'strs = ["a"]', expectedDisplay: '[["a"]]' },
    ],
    hints: ['Sort each word alphabetically to use as the hash map key.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], message: 'Sorting words to group by canonical anagram keys' }],
  },
  {
    id: 'top-k-frequent-elements',
    wingId: 'data-structures',
    floor: 11,
    title: 'Top K Frequent Elements (Map + Bucket Sort)',
    difficulty: 'medium',
    visualizerType: 'array',
    monster: {
      id: 'frequency-golem',
      name: 'Ferrum the Frequency Golem',
      title: 'Titan of Tallied Occurrences',
      maxHp: 3,
      hp: 3,
      sprite: 'golem',
      color: '#f59e0b',
      attackName: 'Resonant Quake',
      attackPower: 2,
      defeatQuote: 'The top frequencies outweighed my stony mass...',
    },
    description: `Given an integer array \`nums\` and an integer \`k\`, return the \`k\` most frequent elements. You may return the answer in any order.`,
    examples: [
      { input: 'nums = [1, 1, 1, 2, 2, 3], k = 2', output: '[1, 2]' },
      { input: 'nums = [1], k = 1', output: '[1]' },
    ],
    constraints: ['1 <= nums.length <= 10^5', '-10^4 <= nums[i] <= 10^4', 'k is in the range [1, the number of unique elements in the array].'],
    starterCode: `function topKFrequent(nums, k) {
  return [];
}`,
    solutionCode: `function topKFrequent(nums, k) {
  const count = new Map();
  for (const n of nums) count.set(n, (count.get(n) || 0) + 1);
  const bucket = Array.from({ length: nums.length + 1 }, () => []);
  for (const [n, freq] of count.entries()) {
    bucket[freq].push(n);
  }
  const result = [];
  for (let i = bucket.length - 1; i >= 0 && result.length < k; i--) {
    for (const n of bucket[i]) {
      result.push(n);
      if (result.length === k) break;
    }
  }
  return result;
}`,
    functionName: 'topKFrequent',
    testCases: [
      { id: 1, input: [[1, 1, 1, 2, 2, 3], 2], expected: [1, 2], inputDisplay: 'nums = [1,1,1,2,2,3], k = 2', expectedDisplay: '[1, 2]' },
      { id: 2, input: [[1], 1], expected: [1], inputDisplay: 'nums = [1], k = 1', expectedDisplay: '[1]' },
      { id: 3, input: [[4, 1, -1, 2, -1, 2, 3], 2], expected: [-1, 2], inputDisplay: 'nums = [4,1,-1,2,-1,2,3], k = 2', expectedDisplay: '[-1, 2]' },
    ],
    hints: ['Count occurrences with a Map, then use bucket sort where index = frequency.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], message: `Counting frequencies and grouping into buckets for top ${tc.input[1]}` }],
  },
  {
    id: 'evaluate-reverse-polish-notation',
    wingId: 'data-structures',
    floor: 12,
    title: 'Evaluate Reverse Polish Notation (Stack)',
    difficulty: 'medium',
    visualizerType: 'stack',
    monster: {
      id: 'postfix-lich',
      name: 'Calcus the Postfix Necromancer',
      title: 'Master of Operand Chains',
      maxHp: 3,
      hp: 3,
      sprite: 'lich',
      color: '#e11d48',
      attackName: 'Arithmetic Curse',
      attackPower: 2,
      defeatQuote: 'The stack evaluated directly to zero...',
    },
    description: `You are given an array of strings \`tokens\` that represents an arithmetic expression in a Reverse Polish Notation (postfix). Evaluate the expression and return an integer that represents the value.

Valid operators are '+', '-', '*', and '/'. Division truncates toward zero.`,
    examples: [
      { input: 'tokens = ["2","1","+","3","*"]', output: '9' },
      { input: 'tokens = ["4","13","5","/","+"]', output: '6' },
    ],
    constraints: ['1 <= tokens.length <= 10^4', 'tokens[i] is either an operator or an integer in the range [-200, 200].'],
    starterCode: `function evalRPN(tokens) {
  return 0;
}`,
    solutionCode: `function evalRPN(tokens) {
  const stack = [];
  for (const t of tokens) {
    if (t === '+' || t === '-' || t === '*' || t === '/') {
      const b = stack.pop();
      const a = stack.pop();
      if (t === '+') stack.push(a + b);
      else if (t === '-') stack.push(a - b);
      else if (t === '*') stack.push(a * b);
      else if (t === '/') stack.push(Math.trunc(a / b));
    } else {
      stack.push(Number(t));
    }
  }
  return stack[0];
}`,
    functionName: 'evalRPN',
    testCases: [
      { id: 1, input: [["2", "1", "+", "3", "*"]], expected: 9, inputDisplay: 'tokens = ["2","1","+","3","*"]', expectedDisplay: '9' },
      { id: 2, input: [["4", "13", "5", "/", "+"]], expected: 6, inputDisplay: 'tokens = ["4","13","5","/","+"]', expectedDisplay: '6' },
      { id: 3, input: [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]], expected: 22, inputDisplay: 'tokens = ["10","6","9","3","+","-11","*","/",...]', expectedDisplay: '22' },
    ],
    hints: ['Push numbers to stack. When hitting an operator, pop two operands, compute, and push result.'],
    generateDefaultFrames: (tc) => [{ type: 'stack', stack: [], message: 'Evaluating RPN expression with operand stack' }],
  },
  {
    id: 'validate-stack-sequences',
    wingId: 'data-structures',
    floor: 13,
    title: 'Validate Stack Sequences (Stack Simulation)',
    difficulty: 'medium',
    visualizerType: 'stack',
    monster: {
      id: 'sequence-treant',
      name: 'Kallor the Knot-Bender',
      title: 'Entangler of Push/Pop Orders',
      maxHp: 3,
      hp: 3,
      sprite: 'treant',
      color: '#15803d',
      attackName: 'Twisted Root Lash',
      attackPower: 2,
      defeatQuote: 'The sequence was untangled smoothly...',
    },
    description: `Given two integer arrays \`pushed\` and \`popped\` each with distinct values, return \`true\` if this could have been the result of a sequence of push and pop operations on an initially empty stack, or \`false\` otherwise.`,
    examples: [
      { input: 'pushed = [1, 2, 3, 4, 5], popped = [4, 5, 3, 2, 1]', output: 'true' },
      { input: 'pushed = [1, 2, 3, 4, 5], popped = [4, 3, 5, 1, 2]', output: 'false' },
    ],
    constraints: ['1 <= pushed.length <= 1000', '0 <= pushed[i] <= 1000', 'pushed.length == popped.length'],
    starterCode: `function validateStackSequences(pushed, popped) {
  return false;
}`,
    solutionCode: `function validateStackSequences(pushed, popped) {
  const stack = [];
  let j = 0;
  for (const x of pushed) {
    stack.push(x);
    while (stack.length > 0 && j < popped.length && stack[stack.length - 1] === popped[j]) {
      stack.pop();
      j++;
    }
  }
  return j === popped.length;
}`,
    functionName: 'validateStackSequences',
    testCases: [
      { id: 1, input: [[1, 2, 3, 4, 5], [4, 5, 3, 2, 1]], expected: true, inputDisplay: 'pushed = [1,2,3,4,5], popped = [4,5,3,2,1]', expectedDisplay: 'true' },
      { id: 2, input: [[1, 2, 3, 4, 5], [4, 3, 5, 1, 2]], expected: false, inputDisplay: 'pushed = [1,2,3,4,5], popped = [4,3,5,1,2]', expectedDisplay: 'false' },
      { id: 3, input: [[1, 0], [1, 0]], expected: true, inputDisplay: 'pushed = [1,0], popped = [1,0]', expectedDisplay: 'true' },
    ],
    hints: ['Simulate the stack push sequence. While the top matches popped[j], pop and increment j.'],
    generateDefaultFrames: (tc) => [{ type: 'stack', stack: [], message: 'Simulating push/pop sequence with real stack' }],
  },
  {
    id: 'lru-cache-simulation',
    wingId: 'data-structures',
    floor: 14,
    title: 'LRU Cache Access Verification (Map)',
    difficulty: 'medium',
    visualizerType: 'array',
    monster: {
      id: 'cache-dragon',
      name: 'Chronos the Eviction Drake',
      title: 'Devourer of Stale Memories',
      maxHp: 3,
      hp: 3,
      sprite: 'dragon',
      color: '#eab308',
      attackName: 'Temporal Expulsion',
      attackPower: 2,
      defeatQuote: 'My cache hit ratio could not hold back your power...',
    },
    description: `Given a sequence of cache operations \`ops\` and a maximum capacity \`cap\`, return the list of items remaining in the LRU cache ordered from most recently used to least recently used.`,
    examples: [
      { input: 'ops = ["A", "B", "C", "A", "D"], cap = 3', output: '["D", "A", "C"]' },
    ],
    constraints: ['1 <= cap <= 1000', '1 <= ops.length <= 10^4'],
    starterCode: `function getLruOrder(ops, cap) {
  return [];
}`,
    solutionCode: `function getLruOrder(ops, cap) {
  const map = new Map();
  for (const item of ops) {
    if (map.has(item)) {
      map.delete(item);
    } else if (map.size >= cap) {
      const oldest = map.keys().next().value;
      map.delete(oldest);
    }
    map.set(item, true);
  }
  return Array.from(map.keys()).reverse();
}`,
    functionName: 'getLruOrder',
    testCases: [
      { id: 1, input: [["A", "B", "C", "A", "D"], 3], expected: ["D", "A", "C"], inputDisplay: 'ops = ["A","B","C","A","D"], cap = 3', expectedDisplay: '["D","A","C"]' },
      { id: 2, input: [["X", "Y", "Z"], 2], expected: ["Z", "Y"], inputDisplay: 'ops = ["X","Y","Z"], cap = 2', expectedDisplay: '["Z","Y"]' },
      { id: 3, input: [["1", "2", "1", "3", "4"], 3], expected: ["4", "3", "1"], inputDisplay: 'ops = ["1","2","1","3","4"], cap = 3', expectedDisplay: '["4","3","1"]' },
    ],
    hints: ['JavaScript Map preserves insertion order. Deleting and re-setting an entry moves it to the most-recent end.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], message: `Simulating LRU cache with capacity ${tc.input[1]}` }],
  },

  // 🔴 HARD (3 Problems - Boss Candidates)
  {
    id: 'largest-rectangle-in-histogram',
    wingId: 'data-structures',
    floor: 15,
    title: 'Boss Chamber: Largest Rectangle in Histogram (Monotonic Stack)',
    difficulty: 'hard',
    visualizerType: 'array',
    monster: {
      id: 'histogram-titan',
      name: 'Malakor the Monotonic Sovereign',
      title: 'Grand Tyrant of Histogram Boundaries',
      maxHp: 4,
      hp: 4,
      sprite: 'gargoyle',
      color: '#ef4444',
      attackName: 'Tectonic Pillar Collapse',
      attackPower: 3,
      defeatQuote: 'You calculated the exact maximal boundary across my stone pillars...',
    },
    description: `Given an array of integers \`heights\` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.`,
    examples: [
      { input: 'heights = [2, 1, 5, 6, 2, 3]', output: '10' },
      { input: 'heights = [2, 4]', output: '4' },
    ],
    constraints: ['1 <= heights.length <= 10^5', '0 <= heights[i] <= 10^4'],
    starterCode: `function largestRectangleArea(heights) {
  return 0;
}`,
    solutionCode: `function largestRectangleArea(heights) {
  const stack = [];
  let maxArea = 0;
  const ext = [...heights, 0];
  for (let i = 0; i < ext.length; i++) {
    while (stack.length > 0 && ext[i] < ext[stack[stack.length - 1]]) {
      const h = ext[stack.pop()];
      const w = stack.length === 0 ? i : i - stack[stack.length - 1] - 1;
      maxArea = Math.max(maxArea, h * w);
    }
    stack.push(i);
  }
  return maxArea;
}`,
    functionName: 'largestRectangleArea',
    testCases: [
      { id: 1, input: [[2, 1, 5, 6, 2, 3]], expected: 10, inputDisplay: 'heights = [2, 1, 5, 6, 2, 3]', expectedDisplay: '10' },
      { id: 2, input: [[2, 4]], expected: 4, inputDisplay: 'heights = [2, 4]', expectedDisplay: '4' },
      { id: 3, input: [[1, 1, 1, 1]], expected: 4, inputDisplay: 'heights = [1, 1, 1, 1]', expectedDisplay: '4' },
    ],
    hints: ['Maintain an increasing monotonic stack of indices. When a shorter bar appears, pop and compute area with height of popped bar.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], message: 'Tracking histogram area bounds with monotonic stack' }],
  },
  {
    id: 'sliding-window-maximum',
    wingId: 'data-structures',
    floor: 16,
    title: 'Boss Chamber: Sliding Window Maximum (Monotonic Deque)',
    difficulty: 'hard',
    visualizerType: 'array',
    monster: {
      id: 'window-leviathan',
      name: 'Ouroboros the Monotonic Deque',
      title: 'Apex Sovereign of Sliding Windows',
      maxHp: 4,
      hp: 4,
      sprite: 'dragon',
      color: '#dc2626',
      attackName: 'Glacial Deque Squeeze',
      attackPower: 3,
      defeatQuote: 'My monotonic window shattered under your O(n) precision...',
    },
    description: `You are given an array of integers \`nums\`, there is a sliding window of size \`k\` which is moving from the very left of the array to the very right. You can only see the \`k\` numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.`,
    examples: [
      { input: 'nums = [1,3,-1,-3,5,3,6,7], k = 3', output: '[3,3,5,5,6,7]' },
      { input: 'nums = [1], k = 1', output: '[1]' },
    ],
    constraints: ['1 <= nums.length <= 10^5', '-10^4 <= nums[i] <= 10^4', '1 <= k <= nums.length'],
    starterCode: `function maxSlidingWindow(nums, k) {
  return [];
}`,
    solutionCode: `function maxSlidingWindow(nums, k) {
  const q = []; // monotonic deque storing indices
  const res = [];
  for (let i = 0; i < nums.length; i++) {
    // Remove indices outside current window
    while (q.length > 0 && q[0] <= i - k) q.shift();
    // Maintain decreasing order in deque
    while (q.length > 0 && nums[q[q.length - 1]] <= nums[i]) q.pop();
    q.push(i);
    if (i >= k - 1) res.push(nums[q[0]]);
  }
  return res;
}`,
    functionName: 'maxSlidingWindow',
    testCases: [
      { id: 1, input: [[1, 3, -1, -3, 5, 3, 6, 7], 3], expected: [3, 3, 5, 5, 6, 7], inputDisplay: 'nums = [1,3,-1,-3,5,3,6,7], k = 3', expectedDisplay: '[3, 3, 5, 5, 6, 7]' },
      { id: 2, input: [[1], 1], expected: [1], inputDisplay: 'nums = [1], k = 1', expectedDisplay: '[1]' },
      { id: 3, input: [[1, -1], 1], expected: [1, -1], inputDisplay: 'nums = [1, -1], k = 1', expectedDisplay: '[1, -1]' },
    ],
    hints: ['Store indices in a double-ended queue. Maintain decreasing element values so the front always holds the current window maximum.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], message: `Tracking sliding window max of size ${tc.input[1]}` }],
  },
  {
    id: 'longest-valid-parentheses',
    wingId: 'data-structures',
    floor: 17,
    title: 'Boss Chamber: Longest Valid Parentheses (Stack)',
    difficulty: 'hard',
    visualizerType: 'stack',
    monster: {
      id: 'arch-archon',
      name: 'Aethelgard the Infinite Boundary',
      title: 'Emperor of Balanced Dimensions',
      maxHp: 4,
      hp: 4,
      sprite: 'lich',
      color: '#9333ea',
      attackName: 'Cataclysmic Void Split',
      attackPower: 3,
      defeatQuote: 'The balance of parentheses held against all odds...',
    },
    description: `Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.`,
    examples: [
      { input: 's = "(()"', output: '2' },
      { input: 's = ")()())"', output: '4' },
      { input: 's = ""', output: '0' },
    ],
    constraints: ['0 <= s.length <= 3 * 10^4', 's[i] is \'(\', or \')\'.'],
    starterCode: `function longestValidParentheses(s) {
  return 0;
}`,
    solutionCode: `function longestValidParentheses(s) {
  const stack = [-1];
  let maxLen = 0;
  for (let i = 0; i < s.length; i++) {
    if (s[i] === '(') {
      stack.push(i);
    } else {
      stack.pop();
      if (stack.length === 0) {
        stack.push(i);
      } else {
        maxLen = Math.max(maxLen, i - stack[stack.length - 1]);
      }
    }
  }
  return maxLen;
}`,
    functionName: 'longestValidParentheses',
    testCases: [
      { id: 1, input: ['(()'], expected: 2, inputDisplay: 's = "(()"', expectedDisplay: '2' },
      { id: 2, input: [')()())'], expected: 4, inputDisplay: 's = ")()())"', expectedDisplay: '4' },
      { id: 3, input: [''], expected: 0, inputDisplay: 's = ""', expectedDisplay: '0' },
    ],
    hints: ['Push -1 as a base index. On "(", push index. On ")", pop and calculate distance to new top.'],
    generateDefaultFrames: (tc) => [{ type: 'stack', stack: [-1], message: `Evaluating longest valid parentheses in "${tc.input[0]}"` }],
  },
];
