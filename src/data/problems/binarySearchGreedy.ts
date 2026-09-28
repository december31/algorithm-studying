import { Problem } from '../../types/problem';
import { ArrayFrame } from '../../types/visualizer';

export const binarySearchGreedyProblems: Problem[] = [
  // 🟢 EASY (7 Problems)
  {
    id: 'binary-search',
    wingId: 'binary-search-greedy',
    floor: 1,
    title: 'Binary Search (Logarithmic Division)',
    difficulty: 'easy',
    visualizerType: 'array',
    monster: {
      id: 'binary-goblin',
      name: 'Halfo the Slicing Goblin',
      title: 'Dissector of Sorted Arrays',
      maxHp: 3,
      hp: 3,
      sprite: 'goblin',
      color: '#06b6d4',
      attackName: 'Halving Dagger',
      attackPower: 1,
      defeatQuote: 'You halved my hiding spots in O(log n) time...',
    },
    description: `Given an array of integers \`nums\` which is sorted in ascending order, and an integer \`target\`, write a function to search \`target\` in \`nums\`. If \`target\` exists, then return its index. Otherwise, return -1.`,
    examples: [
      { input: 'nums = [-1,0,3,5,9,12], target = 9', output: '4' },
      { input: 'nums = [-1,0,3,5,9,12], target = 2', output: '-1' },
    ],
    constraints: ['1 <= nums.length <= 10^4', '-10^4 < nums[i], target < 10^4', 'All elements in nums are unique and sorted.'],
    starterCode: `function search(nums, target) {
  return -1;
}`,
    solutionCode: `function search(nums, target) {
  let left = 0, right = nums.length - 1;
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (nums[mid] === target) return mid;
    if (nums[mid] < target) left = mid + 1;
    else right = mid - 1;
  }
  return -1;
}`,
    functionName: 'search',
    testCases: [
      { id: 1, input: [[-1, 0, 3, 5, 9, 12], 9], expected: 4, inputDisplay: 'nums = [-1,0,3,5,9,12], target = 9', expectedDisplay: '4' },
      { id: 2, input: [[-1, 0, 3, 5, 9, 12], 2], expected: -1, inputDisplay: 'nums = [-1,0,3,5,9,12], target = 2', expectedDisplay: '-1' },
      { id: 3, input: [[5], 5], expected: 0, inputDisplay: 'nums = [5], target = 5', expectedDisplay: '0' },
    ],
    hints: ['Compute mid = floor((left + right) / 2). If nums[mid] < target, search right half; else search left.'],
    generateDefaultFrames: (tc) => {
      const arr = tc.input[0];
      return [{
        type: 'array',
        array: arr,
        pointers: [
          { name: 'L', index: 0, color: '#38bdf8' },
          { name: 'mid', index: Math.floor(arr.length / 2), color: '#f59e0b' },
          { name: 'R', index: arr.length - 1, color: '#ec4899' },
        ],
        message: `Binary search for target ${tc.input[1]}`,
      }];
    },
  },
  {
    id: 'best-time-to-buy-and-sell-stock',
    wingId: 'binary-search-greedy',
    floor: 2,
    title: 'Best Time to Buy and Sell Stock (Greedy Minimum Tracking)',
    difficulty: 'easy',
    visualizerType: 'array',
    monster: {
      id: 'merchant-imp',
      name: 'Greedo the Market Imp',
      title: 'Manipulator of Volatile Prices',
      maxHp: 3,
      hp: 3,
      sprite: 'slime',
      color: '#f59e0b',
      attackName: 'Short-Sell Sting',
      attackPower: 1,
      defeatQuote: 'You timed the dip and sold at peak profit...',
    },
    description: `You are given an array \`prices\` where \`prices[i]\` is the price of a given stock on the \`i\`th day. You want to maximize your profit by choosing a single day to buy and a different day in the future to sell. Return the maximum profit you can achieve. If you cannot achieve any profit, return 0.`,
    examples: [
      { input: 'prices = [7,1,5,3,6,4]', output: '5' },
      { input: 'prices = [7,6,4,3,1]', output: '0' },
    ],
    constraints: ['1 <= prices.length <= 10^5', '0 <= prices[i] <= 10^4'],
    starterCode: `function maxProfit(prices) {
  return 0;
}`,
    solutionCode: `function maxProfit(prices) {
  let minPrice = Infinity;
  let maxProfit = 0;
  for (const p of prices) {
    if (p < minPrice) minPrice = p;
    else if (p - minPrice > maxProfit) maxProfit = p - minPrice;
  }
  return maxProfit;
}`,
    functionName: 'maxProfit',
    testCases: [
      { id: 1, input: [[7, 1, 5, 3, 6, 4]], expected: 5, inputDisplay: 'prices = [7,1,5,3,6,4]', expectedDisplay: '5' },
      { id: 2, input: [[7, 6, 4, 3, 1]], expected: 0, inputDisplay: 'prices = [7,6,4,3,1]', expectedDisplay: '0' },
      { id: 3, input: [[2, 4, 1]], expected: 2, inputDisplay: 'prices = [2, 4, 1]', expectedDisplay: '2' },
    ],
    hints: ['Track the lowest price seen so far in a single pass, updating max profit at each day.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], message: 'Tracking minimum purchase price seen so far' }],
  },
  {
    id: 'search-insert-position',
    wingId: 'binary-search-greedy',
    floor: 3,
    title: 'Search Insert Position (Boundary Point Discovery)',
    difficulty: 'easy',
    visualizerType: 'array',
    monster: {
      id: 'boundary-gargoyle',
      name: 'Petra the Boundary Gargoyle',
      title: 'Keeper of Sorted Slots',
      maxHp: 3,
      hp: 3,
      sprite: 'gargoyle',
      color: '#64748b',
      attackName: 'Stonewall Wedge',
      attackPower: 1,
      defeatQuote: 'You inserted your blade into the exact boundary...',
    },
    description: `Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. Must be O(log n).`,
    examples: [
      { input: 'nums = [1,3,5,6], target = 5', output: '2' },
      { input: 'nums = [1,3,5,6], target = 2', output: '1' },
      { input: 'nums = [1,3,5,6], target = 7', output: '4' },
    ],
    constraints: ['1 <= nums.length <= 10^4', '-10^4 <= nums[i], target <= 10^4'],
    starterCode: `function searchInsert(nums, target) {
  return 0;
}`,
    solutionCode: `function searchInsert(nums, target) {
  let left = 0, right = nums.length - 1;
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (nums[mid] === target) return mid;
    if (nums[mid] < target) left = mid + 1;
    else right = mid - 1;
  }
  return left;
}`,
    functionName: 'searchInsert',
    testCases: [
      { id: 1, input: [[1, 3, 5, 6], 5], expected: 2, inputDisplay: 'nums = [1,3,5,6], target = 5', expectedDisplay: '2' },
      { id: 2, input: [[1, 3, 5, 6], 2], expected: 1, inputDisplay: 'nums = [1,3,5,6], target = 2', expectedDisplay: '1' },
      { id: 3, input: [[1, 3, 5, 6], 7], expected: 4, inputDisplay: 'nums = [1,3,5,6], target = 7', expectedDisplay: '4' },
    ],
    hints: ['When binary search terminates with left > right, left is the exact insertion point.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], message: `Finding insertion index for target ${tc.input[1]}` }],
  },
  {
    id: 'sqrt-x',
    wingId: 'binary-search-greedy',
    floor: 4,
    title: 'Sqrt(x) (Mathematical Integer Binary Search)',
    difficulty: 'easy',
    visualizerType: 'array',
    monster: {
      id: 'root-golem',
      name: 'Radix the Square Root Golem',
      title: 'Architect of Quadratic Domains',
      maxHp: 3,
      hp: 3,
      sprite: 'golem',
      color: '#eab308',
      attackName: 'Quadratic Shockwave',
      attackPower: 1,
      defeatQuote: 'The integer square root bound my power...',
    },
    description: `Given a non-negative integer \`x\`, return the square root of \`x\` rounded down to the nearest integer. The returned integer should be non-negative as well. Do not use built-in exponent functions.`,
    examples: [
      { input: 'x = 4', output: '2' },
      { input: 'x = 8', output: '2' },
    ],
    constraints: ['0 <= x <= 2^31 - 1'],
    starterCode: `function mySqrt(x) {
  return 0;
}`,
    solutionCode: `function mySqrt(x) {
  if (x < 2) return x;
  let left = 1, right = Math.floor(x / 2);
  let ans = 1;
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (mid * mid === x) return mid;
    if (mid * mid < x) {
      ans = mid;
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return ans;
}`,
    functionName: 'mySqrt',
    testCases: [
      { id: 1, input: [4], expected: 2, inputDisplay: 'x = 4', expectedDisplay: '2' },
      { id: 2, input: [8], expected: 2, inputDisplay: 'x = 8', expectedDisplay: '2' },
      { id: 3, input: [0], expected: 0, inputDisplay: 'x = 0', expectedDisplay: '0' },
    ],
    hints: ['Binary search the range [1, floor(x/2)]. Check if mid * mid <= x.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: [0, 1, 2, tc.input[0]], message: `Binary search for integer sqrt of ${tc.input[0]}` }],
  },
  {
    id: 'assign-cookies',
    wingId: 'binary-search-greedy',
    floor: 5,
    title: 'Assign Cookies (Two Pointer Greedy Matching)',
    difficulty: 'easy',
    visualizerType: 'array',
    monster: {
      id: 'glutton-orc',
      name: 'Gromm the Cookie Glutton',
      title: 'Devourer of Sized Treats',
      maxHp: 3,
      hp: 3,
      sprite: 'orc',
      color: '#15803d',
      attackName: 'Gluttonous Roar',
      attackPower: 1,
      defeatQuote: 'All the children received their satisfied treats...',
    },
    description: `Assume you are an awesome parent and want to give your children some cookies. Each child \`i\` has a greed factor \`g[i]\`, and each cookie \`j\` has a size \`s[j]\`. If \`s[j] >= g[i]\`, we can assign cookie \`j\` to child \`i\`. Maximize the number of content children.`,
    examples: [
      { input: 'g = [1,2,3], s = [1,1]', output: '1' },
      { input: 'g = [1,2], s = [1,2,3]', output: '2' },
    ],
    constraints: ['1 <= g.length <= 3 * 10^4', '0 <= s.length <= 3 * 10^4', '1 <= g[i], s[j] <= 2^31 - 1'],
    starterCode: `function findContentChildren(g, s) {
  return 0;
}`,
    solutionCode: `function findContentChildren(g, s) {
  g.sort((a, b) => a - b);
  s.sort((a, b) => a - b);
  let child = 0, cookie = 0;
  while (child < g.length && cookie < s.length) {
    if (s[cookie] >= g[child]) {
      child++;
    }
    cookie++;
  }
  return child;
}`,
    functionName: 'findContentChildren',
    testCases: [
      { id: 1, input: [[1, 2, 3], [1, 1]], expected: 1, inputDisplay: 'g = [1,2,3], s = [1,1]', expectedDisplay: '1' },
      { id: 2, input: [[1, 2], [1, 2, 3]], expected: 2, inputDisplay: 'g = [1,2], s = [1,2,3]', expectedDisplay: '2' },
      { id: 3, input: [[3, 4], [1, 2]], expected: 0, inputDisplay: 'g = [3,4], s = [1,2]', expectedDisplay: '0' },
    ],
    hints: ['Sort both arrays. Satisfy the child with the smallest greed factor using the smallest viable cookie.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], secondaryArray: tc.input[1], message: 'Greedily matching smallest cookies to lowest greeds' }],
  },
  {
    id: 'lemonade-change',
    wingId: 'binary-search-greedy',
    floor: 6,
    title: 'Lemonade Change (Greedy Bill Consumption)',
    difficulty: 'easy',
    visualizerType: 'array',
    monster: {
      id: 'cashier-wraith',
      name: 'Tithe the Bill Collector',
      title: 'Exactor of Exact Currency',
      maxHp: 3,
      hp: 3,
      sprite: 'wraith',
      color: '#10b981',
      attackName: 'Counterfeit Curse',
      attackPower: 1,
      defeatQuote: 'You provided exact change down to the last dollar...',
    },
    description: `At a lemonade stand, each lemonade costs $5. Customers stand in a queue and order one at a time. Each customer pays with a $5, $10, or $20 bill. Return \`true\` if you can provide every customer with correct change.`,
    examples: [
      { input: 'bills = [5,5,5,10,20]', output: 'true' },
      { input: 'bills = [5,5,10,10,20]', output: 'false' },
    ],
    constraints: ['1 <= bills.length <= 10^5', 'bills[i] is either 5, 10, or 20.'],
    starterCode: `function lemonadeChange(bills) {
  return true;
}`,
    solutionCode: `function lemonadeChange(bills) {
  let five = 0, ten = 0;
  for (const b of bills) {
    if (b === 5) {
      five++;
    } else if (b === 10) {
      if (five === 0) return false;
      five--;
      ten++;
    } else {
      // $20 bill: prefer giving $10 + $5 over 3x $5
      if (ten > 0 && five > 0) {
        ten--;
        five--;
      } else if (five >= 3) {
        five -= 3;
      } else {
        return false;
      }
    }
  }
  return true;
}`,
    functionName: 'lemonadeChange',
    testCases: [
      { id: 1, input: [[5, 5, 5, 10, 20]], expected: true, inputDisplay: 'bills = [5,5,5,10,20]', expectedDisplay: 'true' },
      { id: 2, input: [[5, 5, 10, 10, 20]], expected: false, inputDisplay: 'bills = [5,5,10,10,20]', expectedDisplay: 'false' },
      { id: 3, input: [[5, 5, 10]], expected: true, inputDisplay: 'bills = [5, 5, 10]', expectedDisplay: 'true' },
    ],
    hints: ['Always prioritize giving a $10 bill as change for a $20 bill, preserving flexible $5 bills.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], message: 'Tracking 5s and 10s bill counts greedily' }],
  },
  {
    id: 'find-the-highest-altitude',
    wingId: 'binary-search-greedy',
    floor: 7,
    title: 'Find the Highest Altitude (Prefix Peak Scan)',
    difficulty: 'easy',
    visualizerType: 'array',
    monster: {
      id: 'cliff-specter',
      name: 'Zephyr the Summit Specter',
      title: 'Lord of the Highest Elevation',
      maxHp: 3,
      hp: 3,
      sprite: 'wraith',
      color: '#38bdf8',
      attackName: 'Hypobaric Gust',
      attackPower: 1,
      defeatQuote: 'You reached the supreme altitude above my clouds...',
    },
    description: `There is a biker going on a road trip. The road trip consists of \`n + 1\` points at different altitudes. You are given an integer array \`gain\` of length \`n\` where \`gain[i]\` is the net gain in altitude between points \`i\` and \`i + 1\`. Return the highest altitude of a point. Start altitude is 0.`,
    examples: [
      { input: 'gain = [-5,1,5,0,-7]', output: '1' },
      { input: 'gain = [-4,-3,-2,-1,4,3,2]', output: '0' },
    ],
    constraints: ['n == gain.length', '1 <= n <= 100', '-100 <= gain[i] <= 100'],
    starterCode: `function largestAltitude(gain) {
  return 0;
}`,
    solutionCode: `function largestAltitude(gain) {
  let maxAlt = 0;
  let curr = 0;
  for (const g of gain) {
    curr += g;
    maxAlt = Math.max(maxAlt, curr);
  }
  return maxAlt;
}`,
    functionName: 'largestAltitude',
    testCases: [
      { id: 1, input: [[-5, 1, 5, 0, -7]], expected: 1, inputDisplay: 'gain = [-5,1,5,0,-7]', expectedDisplay: '1' },
      { id: 2, input: [[-4, -3, -2, -1, 4, 3, 2]], expected: 0, inputDisplay: 'gain = [-4,-3,-2,-1,4,3,2]', expectedDisplay: '0' },
      { id: 3, input: [[1, 2, 3]], expected: 6, inputDisplay: 'gain = [1, 2, 3]', expectedDisplay: '6' },
    ],
    hints: ['Accumulate the running prefix sum starting from 0 and maintain the max value.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], message: 'Tracking running altitude prefix sum' }],
  },

  // 🟡 MEDIUM (7 Problems)
  {
    id: 'search-in-rotated-sorted-array',
    wingId: 'binary-search-greedy',
    floor: 8,
    title: 'Search in Rotated Sorted Array (Inflection Boundary Logic)',
    difficulty: 'medium',
    visualizerType: 'array',
    monster: {
      id: 'rotated-lich',
      name: 'Invertor the Rotated Lich',
      title: 'Twister of Monotonic Sequences',
      maxHp: 3,
      hp: 3,
      sprite: 'lich',
      color: '#8b5cf6',
      attackName: 'Discontinuous Rift',
      attackPower: 2,
      defeatQuote: 'You identified the sorted half despite my spatial rotation...',
    },
    description: `Given the array \`nums\` after the possible rotation and an integer \`target\`, return the index of \`target\` if it is in \`nums\`, or -1 if it is not in \`nums\`. Must be O(log n).`,
    examples: [
      { input: 'nums = [4,5,6,7,0,1,2], target = 0', output: '4' },
      { input: 'nums = [4,5,6,7,0,1,2], target = 3', output: '-1' },
      { input: 'nums = [1], target = 0', output: '-1' },
    ],
    constraints: ['1 <= nums.length <= 5000', '-10^4 <= nums[i], target <= 10^4', 'All values of nums are unique.'],
    starterCode: `function searchRotated(nums, target) {
  return -1;
}`,
    solutionCode: `function searchRotated(nums, target) {
  let left = 0, right = nums.length - 1;
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (nums[mid] === target) return mid;
    // Check which half is sorted
    if (nums[left] <= nums[mid]) {
      // Left half is sorted
      if (nums[left] <= target && target < nums[mid]) right = mid - 1;
      else left = mid + 1;
    } else {
      // Right half is sorted
      if (nums[mid] < target && target <= nums[right]) left = mid + 1;
      else right = mid - 1;
    }
  }
  return -1;
}`,
    functionName: 'searchRotated',
    testCases: [
      { id: 1, input: [[4, 5, 6, 7, 0, 1, 2], 0], expected: 4, inputDisplay: 'nums = [4,5,6,7,0,1,2], target = 0', expectedDisplay: '4' },
      { id: 2, input: [[4, 5, 6, 7, 0, 1, 2], 3], expected: -1, inputDisplay: 'nums = [4,5,6,7,0,1,2], target = 3', expectedDisplay: '-1' },
      { id: 3, input: [[1], 0], expected: -1, inputDisplay: 'nums = [1], target = 0', expectedDisplay: '-1' },
    ],
    hints: ['One half of the array will always remain normally sorted. Determine if target lies inside it.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], message: `Binary search over rotated sorted array for target ${tc.input[1]}` }],
  },
  {
    id: 'find-first-and-last-position',
    wingId: 'binary-search-greedy',
    floor: 9,
    title: 'Find First and Last Position in Sorted Array (Bound Binary Search)',
    difficulty: 'medium',
    visualizerType: 'array',
    monster: {
      id: 'span-gargoyle',
      name: 'Vorg the Bound Gargoyle',
      title: 'Keeper of Left & Right Horizons',
      maxHp: 3,
      hp: 3,
      sprite: 'gargoyle',
      color: '#3b82f6',
      attackName: 'Horizonal Shockwave',
      attackPower: 2,
      defeatQuote: 'Both boundaries were pinned down in O(log n)...',
    },
    description: `Given an array of integers \`nums\` sorted in non-decreasing order, find the starting and ending position of a given \`target\` value. If target is not found, return [-1, -1]. Must be O(log n).`,
    examples: [
      { input: 'nums = [5,7,7,8,8,10], target = 8', output: '[3,4]' },
      { input: 'nums = [5,7,7,8,8,10], target = 6', output: '[-1,-1]' },
    ],
    constraints: ['0 <= nums.length <= 10^5', '-10^9 <= nums[i], target <= 10^9'],
    starterCode: `function searchRange(nums, target) {
  return [-1, -1];
}`,
    solutionCode: `function searchRange(nums, target) {
  function findBound(isFirst) {
    let left = 0, right = nums.length - 1;
    let bound = -1;
    while (left <= right) {
      const mid = Math.floor((left + right) / 2);
      if (nums[mid] === target) {
        bound = mid;
        if (isFirst) right = mid - 1;
        else left = mid + 1;
      } else if (nums[mid] < target) {
        left = mid + 1;
      } else {
        right = mid - 1;
      }
    }
    return bound;
  }
  return [findBound(true), findBound(false)];
}`,
    functionName: 'searchRange',
    testCases: [
      { id: 1, input: [[5, 7, 7, 8, 8, 10], 8], expected: [3, 4], inputDisplay: 'nums = [5,7,7,8,8,10], target = 8', expectedDisplay: '[3, 4]' },
      { id: 2, input: [[5, 7, 7, 8, 8, 10], 6], expected: [-1, -1], inputDisplay: 'nums = [5,7,7,8,8,10], target = 6', expectedDisplay: '[-1, -1]' },
      { id: 3, input: [[], 0], expected: [-1, -1], inputDisplay: 'nums = [], target = 0', expectedDisplay: '[-1, -1]' },
    ],
    hints: ['Run two binary searches: one searching leftwards when match is found, one searching rightwards.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], message: `Finding lower and upper boundaries for target ${tc.input[1]}` }],
  },
  {
    id: 'jump-game',
    wingId: 'binary-search-greedy',
    floor: 10,
    title: 'Jump Game (Dynamic Reachability Greedy Tracking)',
    difficulty: 'medium',
    visualizerType: 'array',
    monster: {
      id: 'spring-goblin',
      name: 'Springo the Leap Goblin',
      title: 'Surveyor of Chasm Reachabilities',
      maxHp: 3,
      hp: 3,
      sprite: 'goblin',
      color: '#f59e0b',
      attackName: 'Spring-Loaded Leap Slash',
      attackPower: 2,
      defeatQuote: 'Your maximum reach bridged the final abyss...',
    },
    description: `You are given an integer array \`nums\`. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position. Return \`true\` if you can reach the last index, or \`false\` otherwise.`,
    examples: [
      { input: 'nums = [2,3,1,1,4]', output: 'true' },
      { input: 'nums = [3,2,1,0,4]', output: 'false' },
    ],
    constraints: ['1 <= nums.length <= 10^4', '0 <= nums[i] <= 10^5'],
    starterCode: `function canJump(nums) {
  return false;
}`,
    solutionCode: `function canJump(nums) {
  let maxReach = 0;
  for (let i = 0; i < nums.length; i++) {
    if (i > maxReach) return false;
    maxReach = Math.max(maxReach, i + nums[i]);
    if (maxReach >= nums.length - 1) return true;
  }
  return true;
}`,
    functionName: 'canJump',
    testCases: [
      { id: 1, input: [[2, 3, 1, 1, 4]], expected: true, inputDisplay: 'nums = [2,3,1,1,4]', expectedDisplay: 'true' },
      { id: 2, input: [[3, 2, 1, 0, 4]], expected: false, inputDisplay: 'nums = [3,2,1,0,4]', expectedDisplay: 'false' },
      { id: 3, input: [[0]], expected: true, inputDisplay: 'nums = [0]', expectedDisplay: 'true' },
    ],
    hints: ['Maintain maxReach = max(maxReach, i + nums[i]). If i > maxReach, you are stuck.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], message: 'Tracking maximum jump reach index greedily' }],
  },
  {
    id: 'merge-intervals',
    wingId: 'binary-search-greedy',
    floor: 11,
    title: 'Merge Intervals (Sort + Sequence Consolidation)',
    difficulty: 'medium',
    visualizerType: 'array',
    monster: {
      id: 'interval-titan',
      name: 'Consolidus the Interval Titan',
      title: 'Fuser of Overlapping Chrono-Spans',
      maxHp: 3,
      hp: 3,
      sprite: 'golem',
      color: '#eab308',
      attackName: 'Temporal Compression',
      attackPower: 2,
      defeatQuote: 'All overlapping time spans were unified...',
    },
    description: `Given an array of \`intervals\` where \`intervals[i] = [start_i, end_i]\`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.`,
    examples: [
      { input: 'intervals = [[1,3],[2,6],[8,10],[15,18]]', output: '[[1,6],[8,10],[15,18]]' },
      { input: 'intervals = [[1,4],[4,5]]', output: '[[1,5]]' },
    ],
    constraints: ['1 <= intervals.length <= 10^4', 'intervals[i].length == 2', '0 <= start_i <= end_i <= 10^4'],
    starterCode: `function mergeIntervals(intervals) {
  return [];
}`,
    solutionCode: `function mergeIntervals(intervals) {
  if (intervals.length <= 1) return intervals;
  intervals.sort((a, b) => a[0] - b[0]);
  const result = [intervals[0]];
  for (let i = 1; i < intervals.length; i++) {
    const prev = result[result.length - 1];
    const curr = intervals[i];
    if (curr[0] <= prev[1]) {
      prev[1] = Math.max(prev[1], curr[1]);
    } else {
      result.push(curr);
    }
  }
  return result;
}`,
    functionName: 'mergeIntervals',
    testCases: [
      { id: 1, input: [[[1, 3], [2, 6], [8, 10], [15, 18]]], expected: [[1, 6], [8, 10], [15, 18]], inputDisplay: '[[1,3],[2,6],[8,10],[15,18]]', expectedDisplay: '[[1,6],[8,10],[15,18]]' },
      { id: 2, input: [[[1, 4], [4, 5]]], expected: [[1, 5]], inputDisplay: '[[1,4],[4,5]]', expectedDisplay: '[[1,5]]' },
      { id: 3, input: [[[1, 4], [2, 3]]], expected: [[1, 4]], inputDisplay: '[[1,4],[2,3]]', expectedDisplay: '[[1,4]]' },
    ],
    hints: ['Sort intervals by start time. Merge with previous if current.start <= prev.end.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0].map((int: any) => `${int[0]}-${int[1]}`), message: 'Merging overlapping interval segments' }],
  },
  {
    id: 'non-overlapping-intervals',
    wingId: 'binary-search-greedy',
    floor: 12,
    title: 'Non-overlapping Intervals (Finish-Time Greedy Sort)',
    difficulty: 'medium',
    visualizerType: 'array',
    monster: {
      id: 'schedule-wraith',
      name: 'Horolog the Schedule Wraith',
      title: 'Optimizer of Minimal Deletions',
      maxHp: 3,
      hp: 3,
      sprite: 'wraith',
      color: '#a855f7',
      attackName: 'Temporal Clash Surge',
      attackPower: 2,
      defeatQuote: 'You minimized interval overlap with surgical finish-time sorting...',
    },
    description: `Given an array of intervals \`intervals\` where \`intervals[i] = [start_i, end_i]\`, return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.`,
    examples: [
      { input: 'intervals = [[1,2],[2,3],[3,4],[1,3]]', output: '1' },
      { input: 'intervals = [[1,2],[1,2],[1,2]]', output: '2' },
    ],
    constraints: ['1 <= intervals.length <= 10^5', 'intervals[i].length == 2'],
    starterCode: `function eraseOverlapIntervals(intervals) {
  return 0;
}`,
    solutionCode: `function eraseOverlapIntervals(intervals) {
  if (intervals.length <= 1) return 0;
  // Greedy interval scheduling: sort by end time
  intervals.sort((a, b) => a[1] - b[1]);
  let removed = 0;
  let prevEnd = intervals[0][1];
  for (let i = 1; i < intervals.length; i++) {
    if (intervals[i][0] < prevEnd) {
      removed++;
    } else {
      prevEnd = intervals[i][1];
    }
  }
  return removed;
}`,
    functionName: 'eraseOverlapIntervals',
    testCases: [
      { id: 1, input: [[[1, 2], [2, 3], [3, 4], [1, 3]]], expected: 1, inputDisplay: '[[1,2],[2,3],[3,4],[1,3]]', expectedDisplay: '1' },
      { id: 2, input: [[[1, 2], [1, 2], [1, 2]]], expected: 2, inputDisplay: '[[1,2],[1,2],[1,2]]', expectedDisplay: '2' },
      { id: 3, input: [[[1, 2], [2, 3]]], expected: 0, inputDisplay: '[[1,2],[2,3]]', expectedDisplay: '0' },
    ],
    hints: ['Sort by end time. Always keep the interval that finishes earliest to leave maximum room for future intervals.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0].map((int: any) => `${int[0]}-${int[1]}`), message: 'Greedily selecting earliest finish times' }],
  },
  {
    id: 'find-peak-element',
    wingId: 'binary-search-greedy',
    floor: 13,
    title: 'Find Peak Element (Slope Direction Binary Search)',
    difficulty: 'medium',
    visualizerType: 'array',
    monster: {
      id: 'summit-dragon',
      name: 'Apex the Summit Dragon',
      title: 'Monarch of Local Maximums',
      maxHp: 3,
      hp: 3,
      sprite: 'dragon',
      color: '#dc2626',
      attackName: 'Altitude Flare',
      attackPower: 2,
      defeatQuote: 'You followed the upward slope straight to my crest...',
    },
    description: `A peak element is an element that is strictly greater than its neighbors. Given an integer array \`nums\`, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks. Must run in O(log n).`,
    examples: [
      { input: 'nums = [1,2,3,1]', output: '2' },
      { input: 'nums = [1,2,1,3,5,6,4]', output: '5' },
    ],
    constraints: ['1 <= nums.length <= 1000', '-2^31 <= nums[i] <= 2^31 - 1'],
    starterCode: `function findPeakElement(nums) {
  return 0;
}`,
    solutionCode: `function findPeakElement(nums) {
  let left = 0, right = nums.length - 1;
  while (left < right) {
    const mid = Math.floor((left + right) / 2);
    if (nums[mid] < nums[mid + 1]) {
      left = mid + 1; // rising slope: peak must exist to the right
    } else {
      right = mid; // falling slope: peak is at mid or to the left
    }
  }
  return left;
}`,
    functionName: 'findPeakElement',
    testCases: [
      { id: 1, input: [[1, 2, 3, 1]], expected: 2, inputDisplay: 'nums = [1,2,3,1]', expectedDisplay: '2' },
      { id: 2, input: [[1, 2, 1, 3, 5, 6, 4]], expected: 5, inputDisplay: 'nums = [1,2,1,3,5,6,4]', expectedDisplay: '5' },
      { id: 3, input: [[1]], expected: 0, inputDisplay: 'nums = [1]', expectedDisplay: '0' },
    ],
    hints: ['If nums[mid] < nums[mid+1], you are on an upward slope and a peak is guaranteed to the right.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], message: 'Binary search following upward gradient slope' }],
  },
  {
    id: 'find-minimum-in-rotated-sorted-array',
    wingId: 'binary-search-greedy',
    floor: 14,
    title: 'Find Minimum in Rotated Sorted Array (Inflection Point)',
    difficulty: 'medium',
    visualizerType: 'array',
    monster: {
      id: 'inflection-treant',
      name: 'Nadir the Root Weaver',
      title: 'Guardian of the Valley Low',
      maxHp: 3,
      hp: 3,
      sprite: 'treant',
      color: '#15803d',
      attackName: 'Tectonic Dip Crack',
      attackPower: 2,
      defeatQuote: 'The valley inflection was discovered in logarithmic time...',
    },
    description: `Given the sorted rotated array \`nums\` of unique elements, return the minimum element of this array. Must run in O(log n) time.`,
    examples: [
      { input: 'nums = [3,4,5,1,2]', output: '1' },
      { input: 'nums = [4,5,6,7,0,1,2]', output: '0' },
      { input: 'nums = [11,13,15,17]', output: '11' },
    ],
    constraints: ['n == nums.length', '1 <= n <= 5000', '-5000 <= nums[i] <= 5000'],
    starterCode: `function findMin(nums) {
  return 0;
}`,
    solutionCode: `function findMin(nums) {
  let left = 0, right = nums.length - 1;
  while (left < right) {
    const mid = Math.floor((left + right) / 2);
    if (nums[mid] > nums[right]) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }
  return nums[left];
}`,
    functionName: 'findMin',
    testCases: [
      { id: 1, input: [[3, 4, 5, 1, 2]], expected: 1, inputDisplay: 'nums = [3,4,5,1,2]', expectedDisplay: '1' },
      { id: 2, input: [[4, 5, 6, 7, 0, 1, 2]], expected: 0, inputDisplay: 'nums = [4,5,6,7,0,1,2]', expectedDisplay: '0' },
      { id: 3, input: [[11, 13, 15, 17]], expected: 11, inputDisplay: 'nums = [11,13,15,17]', expectedDisplay: '11' },
    ],
    hints: ['Compare nums[mid] with nums[right]. If mid is greater, the inflection drop is in the right half.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], message: 'Locating minimum inflection point via binary search' }],
  },

  // 🔴 HARD (3 Problems - Boss Candidates)
  {
    id: 'split-array-largest-sum',
    wingId: 'binary-search-greedy',
    floor: 15,
    title: 'Boss Chamber: Split Array Largest Sum (Binary Search on Answer)',
    difficulty: 'hard',
    visualizerType: 'array',
    monster: {
      id: 'partition-titan',
      name: 'Divido the Subarray Colossus',
      title: 'Architect of Minimized Maxima',
      maxHp: 4,
      hp: 4,
      sprite: 'golem',
      color: '#eab308',
      attackName: 'Subarray Partition Blast',
      attackPower: 3,
      defeatQuote: 'Your binary search pinned the exact minimized maximum sum...',
    },
    description: `Given an integer array \`nums\` and an integer \`k\`, split \`nums\` into \`k\` non-empty subarrays such that the largest sum of any subarray is minimized. Return the minimized largest sum of the split.`,
    examples: [
      { input: 'nums = [7,2,5,10,8], k = 2', output: '18' },
      { input: 'nums = [1,2,3,4,5], k = 2', output: '9' },
    ],
    constraints: ['1 <= nums.length <= 1000', '0 <= nums[i] <= 10^6', '1 <= k <= min(50, nums.length)'],
    starterCode: `function splitArray(nums, k) {
  return 0;
}`,
    solutionCode: `function splitArray(nums, k) {
  let left = Math.max(...nums);
  let right = nums.reduce((a, b) => a + b, 0);

  function canSplit(maxSum) {
    let pieces = 1;
    let curr = 0;
    for (const num of nums) {
      if (curr + num > maxSum) {
        pieces++;
        curr = num;
      } else {
        curr += num;
      }
    }
    return pieces <= k;
  }

  let ans = right;
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (canSplit(mid)) {
      ans = mid;
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }
  return ans;
}`,
    functionName: 'splitArray',
    testCases: [
      { id: 1, input: [[7, 2, 5, 10, 8], 2], expected: 18, inputDisplay: 'nums = [7,2,5,10,8], k = 2', expectedDisplay: '18' },
      { id: 2, input: [[1, 2, 3, 4, 5], 2], expected: 9, inputDisplay: 'nums = [1,2,3,4,5], k = 2', expectedDisplay: '9' },
      { id: 3, input: [[1, 4, 4], 3], expected: 4, inputDisplay: 'nums = [1,4,4], k = 3', expectedDisplay: '4' },
    ],
    hints: ['Binary search the answer range: [max(nums), sum(nums)]. Use greedy check to count required splits.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], message: `Binary searching answer space for k = ${tc.input[1]} partitions` }],
  },
  {
    id: 'candy',
    wingId: 'binary-search-greedy',
    floor: 16,
    title: 'Boss Chamber: Candy (Two-Pass Greedy Condition Scan)',
    difficulty: 'hard',
    visualizerType: 'array',
    monster: {
      id: 'sugar-lich',
      name: 'Dulcis the Confection Lich',
      title: 'Exactor of Strict Rating Rations',
      maxHp: 4,
      hp: 4,
      sprite: 'lich',
      color: '#ec4899',
      attackName: 'Crystalline Sugar Nova',
      attackPower: 3,
      defeatQuote: 'Both left and right condition sweeps matched minimum distribution...',
    },
    description: `There are \`n\` children standing in a line. Each child is assigned a rating value given in the integer array \`ratings\`. Each child must have at least one candy. Children with a higher rating get more candies than their neighbors. Return the minimum number of candies you need to distribute.`,
    examples: [
      { input: 'ratings = [1,0,2]', output: '5' },
      { input: 'ratings = [1,2,2]', output: '4' },
    ],
    constraints: ['n == ratings.length', '1 <= n <= 2 * 10^4', '0 <= ratings[i] <= 2 * 10^4'],
    starterCode: `function candy(ratings) {
  return 0;
}`,
    solutionCode: `function candy(ratings) {
  const n = ratings.length;
  const candies = new Array(n).fill(1);
  // Left-to-right pass
  for (let i = 1; i < n; i++) {
    if (ratings[i] > ratings[i - 1]) candies[i] = candies[i - 1] + 1;
  }
  // Right-to-left pass
  for (let i = n - 2; i >= 0; i--) {
    if (ratings[i] > ratings[i + 1]) candies[i] = Math.max(candies[i], candies[i + 1] + 1);
  }
  return candies.reduce((a, b) => a + b, 0);
}`,
    functionName: 'candy',
    testCases: [
      { id: 1, input: [[1, 0, 2]], expected: 5, inputDisplay: 'ratings = [1,0,2]', expectedDisplay: '5' },
      { id: 2, input: [[1, 2, 2]], expected: 4, inputDisplay: 'ratings = [1,2,2]', expectedDisplay: '4' },
      { id: 3, input: [[1, 3, 2, 2, 1]], expected: 7, inputDisplay: 'ratings = [1,3,2,2,1]', expectedDisplay: '7' },
    ],
    hints: ['Make two passes: first left-to-right, then right-to-left taking max(candies[i], candies[i+1] + 1).'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], message: 'Two-pass bidirectional greedy candy distribution' }],
  },
  {
    id: 'median-of-two-sorted-arrays',
    wingId: 'binary-search-greedy',
    floor: 17,
    title: 'Boss Chamber: Median of Two Sorted Arrays (Dual Partition Binary Split)',
    difficulty: 'hard',
    visualizerType: 'array',
    monster: {
      id: 'median-dragon',
      name: 'Bifrost the Dual Partition Dragon',
      title: 'Emperor of Balanced Halves',
      maxHp: 4,
      hp: 4,
      sprite: 'dragon',
      color: '#dc2626',
      attackName: 'Dual Horizon Disintegration',
      attackPower: 3,
      defeatQuote: 'The dual array partition balanced with O(log(min(m,n))) perfection...',
    },
    description: `Given two sorted arrays \`nums1\` and \`nums2\` of size \`m\` and \`n\` respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).`,
    examples: [
      { input: 'nums1 = [1,3], nums2 = [2]', output: '2.0' },
      { input: 'nums1 = [1,2], nums2 = [3,4]', output: '2.5' },
    ],
    constraints: ['nums1.length == m, nums2.length == n', '0 <= m, n <= 1000', '1 <= m + n <= 2000'],
    starterCode: `function findMedianSortedArrays(nums1, nums2) {
  return 0.0;
}`,
    solutionCode: `function findMedianSortedArrays(nums1, nums2) {
  if (nums1.length > nums2.length) return findMedianSortedArrays(nums2, nums1);
  const m = nums1.length, n = nums2.length;
  let left = 0, right = m;
  while (left <= right) {
    const p1 = Math.floor((left + right) / 2);
    const p2 = Math.floor((m + n + 1) / 2) - p1;

    const maxLeft1 = p1 === 0 ? -Infinity : nums1[p1 - 1];
    const minRight1 = p1 === m ? Infinity : nums1[p1];

    const maxLeft2 = p2 === 0 ? -Infinity : nums2[p2 - 1];
    const minRight2 = p2 === n ? Infinity : nums2[p2];

    if (maxLeft1 <= minRight2 && maxLeft2 <= minRight1) {
      if ((m + n) % 2 === 0) {
        return (Math.max(maxLeft1, maxLeft2) + Math.min(minRight1, minRight2)) / 2;
      } else {
        return Math.max(maxLeft1, maxLeft2);
      }
    } else if (maxLeft1 > minRight2) {
      right = p1 - 1;
    } else {
      left = p1 + 1;
    }
  }
  return 0.0;
}`,
    functionName: 'findMedianSortedArrays',
    testCases: [
      { id: 1, input: [[1, 3], [2]], expected: 2, inputDisplay: 'nums1 = [1,3], nums2 = [2]', expectedDisplay: '2.0' },
      { id: 2, input: [[1, 2], [3, 4]], expected: 2.5, inputDisplay: 'nums1 = [1,2], nums2 = [3,4]', expectedDisplay: '2.5' },
      { id: 3, input: [[0, 0], [0, 0]], expected: 0, inputDisplay: 'nums1 = [0,0], nums2 = [0,0]', expectedDisplay: '0.0' },
    ],
    hints: ['Binary search the smaller array for a cut point such that left elements <= right elements.'],
    generateDefaultFrames: (tc) => [{ type: 'array', array: tc.input[0], secondaryArray: tc.input[1], message: 'Dual array binary search partition balance' }],
  },
];
