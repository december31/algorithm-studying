import { Problem } from '../../types/problem';
import { BitFrame } from '../../types/visualizer';

export const bitManipulationProblems: Problem[] = [
  // 🟢 EASY (8 Problems)
  {
    id: 'single-number',
    wingId: 'bit-manipulation',
    floor: 1,
    title: 'Single Number (XOR Cancellation Property: x ^ x = 0)',
    difficulty: 'easy',
    visualizerType: 'bits',
    monster: {
      id: 'xor-imp',
      name: 'Null-Imp the Binary Canceller',
      title: 'Scavenger of Paired Bits',
      maxHp: 3,
      hp: 3,
      sprite: 'slime',
      color: '#10b981',
      attackName: 'Bitwise Inversion Slash',
      attackPower: 1,
      defeatQuote: 'All paired numbers annihilated to zero, leaving my true identity...',
    },
    description: `Given a non-empty array of integers \`nums\`, every element appears twice except for one. Find that single one. You must implement a solution with a linear runtime complexity and use only constant extra space (O(1) memory).`,
    examples: [
      { input: 'nums = [2,2,1]', output: '1' },
      { input: 'nums = [4,1,2,1,2]', output: '4' },
      { input: 'nums = [1]', output: '1' },
    ],
    constraints: ['1 <= nums.length <= 3 * 10^4', '-3 * 10^4 <= nums[i] <= 3 * 10^4'],
    starterCode: `function singleNumber(nums) {
  return 0;
}`,
    solutionCode: `function singleNumber(nums) {
  let res = 0;
  for (const n of nums) res ^= n;
  return res;
}`,
    functionName: 'singleNumber',
    testCases: [
      { id: 1, input: [[2, 2, 1]], expected: 1, inputDisplay: 'nums = [2, 2, 1]', expectedDisplay: '1' },
      { id: 2, input: [[4, 1, 2, 1, 2]], expected: 4, inputDisplay: 'nums = [4, 1, 2, 1, 2]', expectedDisplay: '4' },
      { id: 3, input: [[1]], expected: 1, inputDisplay: 'nums = [1]', expectedDisplay: '1' },
    ],
    hints: ['XORing a number with itself yields 0: a ^ a = 0. XORing with 0 preserves value: a ^ 0 = a.'],
    generateDefaultFrames: (tc) => [{
      type: 'bits',
      binaryString: (tc.input[0][0] || 0).toString(2),
      decimalValue: tc.input[0][0] || 0,
      operation: 'XOR ACCUMULATION',
      message: 'XORing all elements eliminates pairs leaving the single number',
    }],
  },
  {
    id: 'number-of-1-bits',
    wingId: 'bit-manipulation',
    floor: 2,
    title: 'Number of 1 Bits (Brian Kernighan\'s Algorithm: n & (n - 1))',
    difficulty: 'easy',
    visualizerType: 'bits',
    monster: {
      id: 'popcount-skeleton',
      name: 'Tally the Bit Skeleton',
      title: 'Counter of Radiant High Pins',
      maxHp: 3,
      hp: 3,
      sprite: 'skeleton',
      color: '#38bdf8',
      attackName: 'Hamming Weight Shock',
      attackPower: 1,
      defeatQuote: 'My lowest set bits were cleared one by one...',
    },
    description: `Given a positive integer \`n\`, write a function that returns the number of set bits it has (also known as the Hamming weight).`,
    examples: [
      { input: 'n = 11 (binary 1011)', output: '3' },
      { input: 'n = 128 (binary 10000000)', output: '1' },
      { input: 'n = 2147483645', output: '30' },
    ],
    constraints: ['1 <= n <= 2^31 - 1'],
    starterCode: `function hammingWeight(n) {
  return 0;
}`,
    solutionCode: `function hammingWeight(n) {
  let count = 0;
  while (n > 0) {
    n = n & (n - 1);
    count++;
  }
  return count;
}`,
    functionName: 'hammingWeight',
    testCases: [
      { id: 1, input: [11], expected: 3, inputDisplay: 'n = 11 (0b1011)', expectedDisplay: '3' },
      { id: 2, input: [128], expected: 1, inputDisplay: 'n = 128 (0b10000000)', expectedDisplay: '1' },
      { id: 3, input: [7], expected: 3, inputDisplay: 'n = 7 (0b111)', expectedDisplay: '3' },
    ],
    hints: ['n & (n - 1) clears the lowest set bit in O(1) operations.'],
    generateDefaultFrames: (tc) => [{
      type: 'bits',
      binaryString: tc.input[0].toString(2),
      decimalValue: tc.input[0],
      operation: 'n & (n - 1)',
      message: `Counting set bits in 0b${tc.input[0].toString(2)}`,
    }],
  },
  {
    id: 'counting-bits',
    wingId: 'bit-manipulation',
    floor: 3,
    title: 'Counting Bits (Bit Shift Dynamic Progression)',
    difficulty: 'easy',
    visualizerType: 'bits',
    monster: {
      id: 'binary-shade',
      name: 'Shiftus the Progression Shade',
      title: 'Master of i >> 1 Recurrence',
      maxHp: 3,
      hp: 3,
      sprite: 'wraith',
      color: '#a855f7',
      attackName: 'Bit Shift Drain',
      attackPower: 1,
      defeatQuote: 'The DP recurrence dp[i] = dp[i >> 1] + (i & 1) outpaced me...',
    },
    description: `Given an integer \`n\`, return an array \`ans\` of length \`n + 1\` such that for each \`i\` (0 <= i <= n), \`ans[i]\` is the number of 1's in the binary representation of \`i\`.`,
    examples: [
      { input: 'n = 2', output: '[0,1,1]' },
      { input: 'n = 5', output: '[0,1,1,2,1,2]' },
    ],
    constraints: ['0 <= n <= 10^5'],
    starterCode: `function countBits(n) {
  return [];
}`,
    solutionCode: `function countBits(n) {
  const ans = new Array(n + 1).fill(0);
  for (let i = 1; i <= n; i++) {
    ans[i] = ans[i >> 1] + (i & 1);
  }
  return ans;
}`,
    functionName: 'countBits',
    testCases: [
      { id: 1, input: [2], expected: [0, 1, 1], inputDisplay: 'n = 2', expectedDisplay: '[0, 1, 1]' },
      { id: 2, input: [5], expected: [0, 1, 1, 2, 1, 2], inputDisplay: 'n = 5', expectedDisplay: '[0, 1, 1, 2, 1, 2]' },
      { id: 3, input: [0], expected: [0], inputDisplay: 'n = 0', expectedDisplay: '[0]' },
    ],
    hints: ['The number of set bits in i is equal to set bits in (i >> 1) plus (i & 1).'],
    generateDefaultFrames: (tc) => [{
      type: 'bits',
      binaryString: tc.input[0].toString(2),
      decimalValue: tc.input[0],
      operation: 'i >> 1 + (i & 1)',
      message: `Calculating bit popcounts up to n = ${tc.input[0]}`,
    }],
  },
  {
    id: 'reverse-bits',
    wingId: 'bit-manipulation',
    floor: 4,
    title: 'Reverse Bits (32-Bit Inversion Shift)',
    difficulty: 'easy',
    visualizerType: 'bits',
    monster: {
      id: 'mirror-gargoyle',
      name: 'Reflector the Inverted Gargoyle',
      title: 'Rotator of 32 Register Cells',
      maxHp: 3,
      hp: 3,
      sprite: 'gargoyle',
      color: '#64748b',
      attackName: 'Reversed Bit Burst',
      attackPower: 1,
      defeatQuote: 'My 32-bit register was inverted end-to-end...',
    },
    description: `Reverse bits of a given 32 bits unsigned integer.`,
    examples: [
      { input: 'n = 43261596 (0b00000010100101000001111010011100)', output: '964176192 (0b00111001011110000010100101000000)' },
    ],
    constraints: ['The input must be a binary string or 32-bit integer.'],
    starterCode: `function reverseBits(n) {
  return 0;
}`,
    solutionCode: `function reverseBits(n) {
  let result = 0;
  for (let i = 0; i < 32; i++) {
    result = (result << 1) | (n & 1);
    n >>>= 1;
  }
  return result >>> 0;
}`,
    functionName: 'reverseBits',
    testCases: [
      { id: 1, input: [43261596], expected: 964176192, inputDisplay: 'n = 43261596', expectedDisplay: '964176192' },
      { id: 2, input: [1], expected: 2147483648, inputDisplay: 'n = 1 (bit 0 -> bit 31)', expectedDisplay: '2147483648' },
      { id: 3, input: [0], expected: 0, inputDisplay: 'n = 0', expectedDisplay: '0' },
    ],
    hints: ['Shift result left by 1 and OR with (n & 1), then shift n right by 1 for 32 iterations.'],
    generateDefaultFrames: (tc) => [{
      type: 'bits',
      binaryString: (tc.input[0] >>> 0).toString(2).padStart(32, '0').slice(-8),
      decimalValue: tc.input[0],
      operation: 'REVERSE 32-BIT',
      message: 'Inverting bit positions from LSB to MSB',
    }],
  },
  {
    id: 'power-of-two',
    wingId: 'bit-manipulation',
    floor: 5,
    title: 'Power of Two (Single Set Bit Mask Validation)',
    difficulty: 'easy',
    visualizerType: 'bits',
    monster: {
      id: 'binary-dragon',
      name: 'Duplicus the Power Drake',
      title: 'Emperor of Binary Radix',
      maxHp: 3,
      hp: 3,
      sprite: 'dragon',
      color: '#eab308',
      attackName: 'Radix Flame',
      attackPower: 1,
      defeatQuote: 'Only a single 1-bit resides in a true power of two...',
    },
    description: `Given an integer \`n\`, return \`true\` if it is a power of two. Otherwise, return \`false\`. An integer \`n\` is a power of two if there exists an integer \`x\` such that \`n == 2^x\`.`,
    examples: [
      { input: 'n = 1', output: 'true' },
      { input: 'n = 16', output: 'true' },
      { input: 'n = 3', output: 'false' },
    ],
    constraints: ['-2^31 <= n <= 2^31 - 1'],
    starterCode: `function isPowerOfTwo(n) {
  return false;
}`,
    solutionCode: `function isPowerOfTwo(n) {
  return n > 0 && (n & (n - 1)) === 0;
}`,
    functionName: 'isPowerOfTwo',
    testCases: [
      { id: 1, input: [1], expected: true, inputDisplay: 'n = 1 (2^0)', expectedDisplay: 'true' },
      { id: 2, input: [16], expected: true, inputDisplay: 'n = 16 (2^4)', expectedDisplay: 'true' },
      { id: 3, input: [3], expected: false, inputDisplay: 'n = 3', expectedDisplay: 'false' },
    ],
    hints: ['A power of two in binary has exactly one set bit. Thus n > 0 && (n & (n - 1)) === 0.'],
    generateDefaultFrames: (tc) => [{
      type: 'bits',
      binaryString: (Math.max(0, tc.input[0])).toString(2),
      decimalValue: tc.input[0],
      operation: 'n & (n - 1) === 0',
      message: `Validating single set bit in ${tc.input[0]}`,
    }],
  },
  {
    id: 'hamming-distance',
    wingId: 'bit-manipulation',
    floor: 6,
    title: 'Hamming Distance (XOR Difference Counting)',
    difficulty: 'easy',
    visualizerType: 'bits',
    monster: {
      id: 'diff-specter',
      name: 'Divergo the Discrepancy Specter',
      title: 'Tallyman of Discordant Bits',
      maxHp: 3,
      hp: 3,
      sprite: 'wraith',
      color: '#ec4899',
      attackName: 'Discordant Pulse',
      attackPower: 1,
      defeatQuote: 'All divergent bit positions were tallied...',
    },
    description: `The Hamming distance between two integers is the number of positions at which the corresponding bits are different. Given two integers \`x\` and \`y\`, return the Hamming distance between them.`,
    examples: [
      { input: 'x = 1, y = 4', output: '2' },
      { input: 'x = 3, y = 1', output: '1' },
    ],
    constraints: ['0 <= x, y <= 2^31 - 1'],
    starterCode: `function hammingDistance(x, y) {
  return 0;
}`,
    solutionCode: `function hammingDistance(x, y) {
  let xor = x ^ y;
  let dist = 0;
  while (xor > 0) {
    xor &= (xor - 1);
    dist++;
  }
  return dist;
}`,
    functionName: 'hammingDistance',
    testCases: [
      { id: 1, input: [1, 4], expected: 2, inputDisplay: 'x = 1 (0001), y = 4 (0100)', expectedDisplay: '2' },
      { id: 2, input: [3, 1], expected: 1, inputDisplay: 'x = 3 (0011), y = 1 (0001)', expectedDisplay: '1' },
      { id: 3, input: [0, 0], expected: 0, inputDisplay: 'x = 0, y = 0', expectedDisplay: '0' },
    ],
    hints: ['Compute x ^ y, then count the number of 1-bits in the result.'],
    generateDefaultFrames: (tc) => [{
      type: 'bits',
      binaryString: tc.input[0].toString(2),
      secondaryBinary: tc.input[1].toString(2),
      decimalValue: tc.input[0] ^ tc.input[1],
      operation: 'x ^ y (DIFF BITS)',
      message: `Calculating bit differences between ${tc.input[0]} and ${tc.input[1]}`,
    }],
  },
  {
    id: 'number-complement',
    wingId: 'bit-manipulation',
    floor: 7,
    title: 'Number Complement (Full-Width Mask Flip)',
    difficulty: 'easy',
    visualizerType: 'bits',
    monster: {
      id: 'complement-imp',
      name: 'Inverto the Bit-Flip Imp',
      title: 'Inverter of Bit Width Masks',
      maxHp: 3,
      hp: 3,
      sprite: 'slime',
      color: '#f59e0b',
      attackName: 'Complementary Flash',
      attackPower: 1,
      defeatQuote: 'My mask flipped each 1 to 0 and 0 to 1...',
    },
    description: `The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation. Given an integer \`num\`, return its complement.`,
    examples: [
      { input: 'num = 5 (0b101)', output: '2 (0b010)' },
      { input: 'num = 1 (0b1)', output: '0 (0b0)' },
    ],
    constraints: ['1 <= num < 2^31'],
    starterCode: `function findComplement(num) {
  return 0;
}`,
    solutionCode: `function findComplement(num) {
  let mask = 1;
  while (mask < num) {
    mask = (mask << 1) | 1;
  }
  return num ^ mask;
}`,
    functionName: 'findComplement',
    testCases: [
      { id: 1, input: [5], expected: 2, inputDisplay: 'num = 5 (101 -> 010)', expectedDisplay: '2' },
      { id: 2, input: [1], expected: 0, inputDisplay: 'num = 1 (1 -> 0)', expectedDisplay: '0' },
      { id: 3, input: [2], expected: 1, inputDisplay: 'num = 2 (10 -> 01)', expectedDisplay: '1' },
    ],
    hints: ['Create an all-1s mask of the same bit length, then XOR num with mask.'],
    generateDefaultFrames: (tc) => [{
      type: 'bits',
      binaryString: tc.input[0].toString(2),
      decimalValue: tc.input[0],
      operation: 'num ^ mask',
      message: `Flipping binary bits of ${tc.input[0]}`,
    }],
  },
  {
    id: 'missing-number-bit',
    wingId: 'bit-manipulation',
    floor: 8,
    title: 'Missing Number (XOR Bit Balance: i ^ nums[i])',
    difficulty: 'easy',
    visualizerType: 'bits',
    monster: {
      id: 'balance-skeleton',
      name: 'Nullus the XOR Boneguard',
      title: 'Keeper of Index-Value Balance',
      maxHp: 3,
      hp: 3,
      sprite: 'skeleton',
      color: '#475569',
      attackName: 'XOR Void Blade',
      attackPower: 1,
      defeatQuote: 'The XOR balance isolated the missing number...',
    },
    description: `Given an array \`nums\` containing \`n\` distinct numbers in the range \`[0, n]\`, return the only number in the range that is missing from the array using bitwise XOR.`,
    examples: [
      { input: 'nums = [3,0,1]', output: '2' },
      { input: 'nums = [0,1]', output: '2' },
    ],
    constraints: ['n == nums.length', '1 <= n <= 10^4', '0 <= nums[i] <= n'],
    starterCode: `function missingNumberBit(nums) {
  return 0;
}`,
    solutionCode: `function missingNumberBit(nums) {
  let xor = nums.length;
  for (let i = 0; i < nums.length; i++) {
    xor ^= i ^ nums[i];
  }
  return xor;
}`,
    functionName: 'missingNumberBit',
    testCases: [
      { id: 1, input: [[3, 0, 1]], expected: 2, inputDisplay: 'nums = [3, 0, 1]', expectedDisplay: '2' },
      { id: 2, input: [[0, 1]], expected: 2, inputDisplay: 'nums = [0, 1]', expectedDisplay: '2' },
      { id: 3, input: [[9,6,4,2,3,5,7,0,1]], expected: 8, inputDisplay: 'nums = 9 elements missing 8', expectedDisplay: '8' },
    ],
    hints: ['XOR all indices 0..n and all array values. Paired values cancel out, leaving the missing number.'],
    generateDefaultFrames: (tc) => [{
      type: 'bits',
      binaryString: tc.input[0].length.toString(2),
      decimalValue: tc.input[0].length,
      operation: 'XOR INDEX BALANCE',
      message: 'XORing indices and values to isolate the missing integer',
    }],
  },

  // 🟡 MEDIUM (6 Problems)
  {
    id: 'single-number-iii',
    wingId: 'bit-manipulation',
    floor: 9,
    title: 'Single Number III (Isolating Lowest Set Bit Differentials)',
    difficulty: 'medium',
    visualizerType: 'bits',
    monster: {
      id: 'dual-wraith',
      name: 'Twin-Void the Bifurcated Wraith',
      title: 'Splitter of Mixed XOR Pools',
      maxHp: 3,
      hp: 3,
      sprite: 'wraith',
      color: '#8b5cf6',
      attackName: 'Bitmask Bifurcation',
      attackPower: 2,
      defeatQuote: 'The lowest differential bit partitioned our dual identities...',
    },
    description: `Given an integer array \`nums\`, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order. O(1) space.`,
    examples: [
      { input: 'nums = [1,2,1,3,2,5]', output: '[3,5]' },
      { input: 'nums = [-1,0]', output: '[-1,0]' },
    ],
    constraints: ['2 <= nums.length <= 3 * 10^4', 'Each value fits in 32-bit integer.'],
    starterCode: `function singleNumberIII(nums) {
  return [];
}`,
    solutionCode: `function singleNumberIII(nums) {
  let diff = 0;
  for (const n of nums) diff ^= n;
  // Isolate lowest set bit
  const diffBit = diff & (-diff);
  let a = 0, b = 0;
  for (const n of nums) {
    if ((n & diffBit) !== 0) a ^= n;
    else b ^= n;
  }
  return a < b ? [a, b] : [b, a];
}`,
    functionName: 'singleNumberIII',
    testCases: [
      { id: 1, input: [[1, 2, 1, 3, 2, 5]], expected: [3, 5], inputDisplay: 'nums = [1,2,1,3,2,5]', expectedDisplay: '[3, 5]' },
      { id: 2, input: [[-1, 0]], expected: [-1, 0], inputDisplay: 'nums = [-1, 0]', expectedDisplay: '[-1, 0]' },
      { id: 3, input: [[0, 1]], expected: [0, 1], inputDisplay: 'nums = [0, 1]', expectedDisplay: '[0, 1]' },
    ],
    hints: ['XOR all elements to get a ^ b. Find diff & (-diff) to identify a bit where a and b differ, then partition into two groups.'],
    generateDefaultFrames: (tc) => [{
      type: 'bits',
      binaryString: '101',
      decimalValue: 5,
      operation: 'diff & (-diff)',
      message: 'Isolating differing bit to split into two independent XOR groups',
    }],
  },
  {
    id: 'single-number-ii',
    wingId: 'bit-manipulation',
    floor: 10,
    title: 'Single Number II (Modulo 3 Bit Counting)',
    difficulty: 'medium',
    visualizerType: 'bits',
    monster: {
      id: 'triad-golem',
      name: 'Triad the Modulo Golem',
      title: 'Guardian of Thrice-Repeated Runes',
      maxHp: 3,
      hp: 3,
      sprite: 'golem',
      color: '#eab308',
      attackName: 'Ternary Stun Pulse',
      attackPower: 2,
      defeatQuote: 'Bit modulo 3 revealed the single remainder...',
    },
    description: `Given an integer array \`nums\` where every element appears three times except for one, which appears exactly once. Find the single element and return it. Must be O(1) space.`,
    examples: [
      { input: 'nums = [2,2,3,2]', output: '3' },
      { input: 'nums = [0,1,0,1,0,1,99]', output: '99' },
    ],
    constraints: ['1 <= nums.length <= 3 * 10^4', '-2^31 <= nums[i] <= 2^31 - 1'],
    starterCode: `function singleNumberII(nums) {
  return 0;
}`,
    solutionCode: `function singleNumberII(nums) {
  let ones = 0, twos = 0;
  for (const n of nums) {
    ones = (ones ^ n) & ~twos;
    twos = (twos ^ n) & ~ones;
  }
  return ones;
}`,
    functionName: 'singleNumberII',
    testCases: [
      { id: 1, input: [[2, 2, 3, 2]], expected: 3, inputDisplay: 'nums = [2, 2, 3, 2]', expectedDisplay: '3' },
      { id: 2, input: [[0, 1, 0, 1, 0, 1, 99]], expected: 99, inputDisplay: 'nums = [0,1,0,1,0,1,99]', expectedDisplay: '99' },
      { id: 3, input: [[5]], expected: 5, inputDisplay: 'nums = [5]', expectedDisplay: '5' },
    ],
    hints: ['Track bits appearing 1 time and 2 times using bitwise gates: ones = (ones ^ n) & ~twos.'],
    generateDefaultFrames: (tc) => [{
      type: 'bits',
      binaryString: (tc.input[0][0] || 0).toString(2),
      decimalValue: tc.input[0][0] || 0,
      operation: 'MOD 3 ACCUMULATOR',
      message: 'Counting bit populations modulo 3',
    }],
  },
  {
    id: 'bitwise-and-of-numbers-range',
    wingId: 'bit-manipulation',
    floor: 11,
    title: 'Bitwise AND of Numbers Range (Common Prefix Shift)',
    difficulty: 'medium',
    visualizerType: 'bits',
    monster: {
      id: 'prefix-lich',
      name: 'Prefixo the Common Prefix Lich',
      title: 'Stripper of Divergent Bit Tails',
      maxHp: 3,
      hp: 3,
      sprite: 'lich',
      color: '#06b6d4',
      attackName: 'Bitwise Prefix Ray',
      attackPower: 2,
      defeatQuote: 'Only the highest matching bit prefix survived the range AND...',
    },
    description: `Given two integers \`left\` and \`right\` that represent the range \`[left, right]\`, return the bitwise AND of all numbers in this range, inclusive.`,
    examples: [
      { input: 'left = 5, right = 7', output: '4' },
      { input: 'left = 0, right = 0', output: '0' },
      { input: 'left = 1, right = 2147483647', output: '0' },
    ],
    constraints: ['0 <= left <= right <= 2^31 - 1'],
    starterCode: `function rangeBitwiseAnd(left, right) {
  return 0;
}`,
    solutionCode: `function rangeBitwiseAnd(left, right) {
  let shift = 0;
  while (left < right) {
    left >>= 1;
    right >>= 1;
    shift++;
  }
  return left << shift;
}`,
    functionName: 'rangeBitwiseAnd',
    testCases: [
      { id: 1, input: [5, 7], expected: 4, inputDisplay: 'left = 5, right = 7', expectedDisplay: '4' },
      { id: 2, input: [0, 0], expected: 0, inputDisplay: 'left = 0, right = 0', expectedDisplay: '0' },
      { id: 3, input: [1, 2147483647], expected: 0, inputDisplay: 'left = 1, right = max', expectedDisplay: '0' },
    ],
    hints: ['The bitwise AND of a range is simply the common binary prefix of left and right, with all differing lower bits becoming 0.'],
    generateDefaultFrames: (tc) => [{
      type: 'bits',
      binaryString: tc.input[0].toString(2),
      secondaryBinary: tc.input[1].toString(2),
      decimalValue: tc.input[0],
      operation: 'COMMON PREFIX SHIFT',
      message: `Finding common bit prefix of range [${tc.input[0]}, ${tc.input[1]}]`,
    }],
  },
  {
    id: 'sum-of-two-integers',
    wingId: 'bit-manipulation',
    floor: 12,
    title: 'Sum of Two Integers (Carry & Half-Adder Logic)',
    difficulty: 'medium',
    visualizerType: 'bits',
    monster: {
      id: 'adder-orc',
      name: 'Krag the Bit-Adder Orc',
      title: 'Simulator of Hardware Adders',
      maxHp: 3,
      hp: 3,
      sprite: 'orc',
      color: '#f97316',
      attackName: 'Carry Propagate Smash',
      attackPower: 2,
      defeatQuote: 'You summed two integers using pure XOR sum and AND carry...',
    },
    description: `Given two integers \`a\` and \`b\`, return the sum of the two integers without using the operators \`+\` and \`-\`.`,
    examples: [
      { input: 'a = 1, b = 2', output: '3' },
      { input: 'a = 2, b = 3', output: '5' },
    ],
    constraints: ['-1000 <= a, b <= 1000'],
    starterCode: `function getSum(a, b) {
  return 0;
}`,
    solutionCode: `function getSum(a, b) {
  while (b !== 0) {
    const carry = (a & b) << 1;
    a = a ^ b;
    b = carry;
  }
  return a;
}`,
    functionName: 'getSum',
    testCases: [
      { id: 1, input: [1, 2], expected: 3, inputDisplay: 'a = 1, b = 2', expectedDisplay: '3' },
      { id: 2, input: [2, 3], expected: 5, inputDisplay: 'a = 2, b = 3', expectedDisplay: '5' },
      { id: 3, input: [20, 30], expected: 50, inputDisplay: 'a = 20, b = 30', expectedDisplay: '50' },
    ],
    hints: ['XOR computes the sum without carry (a ^ b). AND shifted left computes carry ((a & b) << 1).'],
    generateDefaultFrames: (tc) => [{
      type: 'bits',
      binaryString: tc.input[0].toString(2),
      secondaryBinary: tc.input[1].toString(2),
      decimalValue: tc.input[0] + tc.input[1],
      operation: 'XOR SUM / AND CARRY',
      message: `Adding ${tc.input[0]} + ${tc.input[1]} without arithmetic operators`,
    }],
  },
  {
    id: 'xor-queries-of-a-subarray',
    wingId: 'bit-manipulation',
    floor: 13,
    title: 'XOR Queries of a Subarray (Prefix XOR Array)',
    difficulty: 'medium',
    visualizerType: 'bits',
    monster: {
      id: 'query-golem',
      name: 'Runic-Sentry the Prefix Golem',
      title: 'Keeper of Cumulative XOR Tables',
      maxHp: 3,
      hp: 3,
      sprite: 'golem',
      color: '#10b981',
      attackName: 'Range Inversion Blast',
      attackPower: 2,
      defeatQuote: 'The prefix XOR array answered range queries in O(1)...',
    },
    description: `You are given an array \`arr\` of positive integers and an array \`queries\` where \`queries[i] = [left_i, right_i]\`. For each query, compute the XOR of elements from \`left_i\` to \`right_i\` (that is, \`arr[left_i] ^ ... ^ arr[right_i]\`). Return an array containing the results.`,
    examples: [
      { input: 'arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]', output: '[2,7,14,8]' },
      { input: 'arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]', output: '[8,0,4,4]' },
    ],
    constraints: ['1 <= arr.length, queries.length <= 3 * 10^4', 'queries[i].length == 2'],
    starterCode: `function xorQueries(arr, queries) {
  return [];
}`,
    solutionCode: `function xorQueries(arr, queries) {
  const prefix = new Array(arr.length + 1).fill(0);
  for (let i = 0; i < arr.length; i++) {
    prefix[i + 1] = prefix[i] ^ arr[i];
  }
  const result = [];
  for (const [L, R] of queries) {
    result.push(prefix[R + 1] ^ prefix[L]);
  }
  return result;
}`,
    functionName: 'xorQueries',
    testCases: [
      { id: 1, input: [[1, 3, 4, 8], [[0, 1], [1, 2], [0, 3], [3, 3]]], expected: [2, 7, 14, 8], inputDisplay: 'arr = [1,3,4,8], 4 queries', expectedDisplay: '[2, 7, 14, 8]' },
      { id: 2, input: [[4, 8, 2, 10], [[2, 3], [1, 3], [0, 0], [0, 3]]], expected: [8, 0, 4, 4], inputDisplay: 'arr = [4,8,2,10], 4 queries', expectedDisplay: '[8, 0, 4, 4]' },
      { id: 3, input: [[5], [[0, 0]]], expected: [5], inputDisplay: 'arr = [5], 1 query', expectedDisplay: '[5]' },
    ],
    hints: ['Compute prefix XOR: prefix[i] = prefix[i-1] ^ arr[i]. Then range XOR(L..R) = prefix[R+1] ^ prefix[L].'],
    generateDefaultFrames: (tc) => [{
      type: 'bits',
      binaryString: (tc.input[0][0] || 0).toString(2),
      decimalValue: tc.input[0][0] || 0,
      operation: 'PREFIX XOR LOOKUP',
      message: 'Answering range XOR queries with cumulative prefix XOR array',
    }],
  },
  {
    id: 'longest-subarray-with-maximum-bitwise-and',
    wingId: 'bit-manipulation',
    floor: 14,
    title: 'Longest Subarray With Maximum Bitwise AND (Property Deduction)',
    difficulty: 'medium',
    visualizerType: 'bits',
    monster: {
      id: 'and-dragon',
      name: 'Nadir the Bitwise Dragon',
      title: 'Monarch of Invariant Bitwise Maxima',
      maxHp: 3,
      hp: 3,
      sprite: 'dragon',
      color: '#dc2626',
      attackName: 'Invariant High Bit Flare',
      attackPower: 2,
      defeatQuote: 'You realized that x & y <= min(x, y)...',
    },
    description: `You are given an integer array \`nums\`. The bitwise AND of an array cannot be greater than any element in the array. Return the length of the longest subarray which has the maximum possible bitwise AND.`,
    examples: [
      { input: 'nums = [1,2,3,3,2,2]', output: '2' },
      { input: 'nums = [1,2,3,4]', output: '1' },
    ],
    constraints: ['1 <= nums.length <= 10^5', '1 <= nums[i] <= 10^6'],
    starterCode: `function longestSubarray(nums) {
  return 0;
}`,
    solutionCode: `function longestSubarray(nums) {
  const maxVal = Math.max(...nums);
  let maxLen = 0;
  let currentLen = 0;
  for (const n of nums) {
    if (n === maxVal) {
      currentLen++;
      maxLen = Math.max(maxLen, currentLen);
    } else {
      currentLen = 0;
    }
  }
  return maxLen;
}`,
    functionName: 'longestSubarray',
    testCases: [
      { id: 1, input: [[1, 2, 3, 3, 2, 2]], expected: 2, inputDisplay: 'nums = [1,2,3,3,2,2]', expectedDisplay: '2' },
      { id: 2, input: [[1, 2, 3, 4]], expected: 1, inputDisplay: 'nums = [1,2,3,4]', expectedDisplay: '1' },
      { id: 3, input: [[5, 5, 5]], expected: 3, inputDisplay: 'nums = [5, 5, 5]', expectedDisplay: '3' },
    ],
    hints: ['Bitwise AND cannot increase value: a & b <= min(a, b). The maximum AND must be equal to max(nums). Find longest contiguous run of max(nums).'],
    generateDefaultFrames: (tc) => [{
      type: 'bits',
      binaryString: Math.max(...tc.input[0]).toString(2),
      decimalValue: Math.max(...tc.input[0]),
      operation: 'MAXIMUM VALUE RUN',
      message: 'Scanning longest contiguous run of max element',
    }],
  },

  // 🔴 HARD (3 Problems - Boss Candidates)
  {
    id: 'shortest-path-visiting-all-nodes',
    wingId: 'bit-manipulation',
    floor: 15,
    title: 'Boss Chamber: Shortest Path Visiting All Nodes (Bitmask BFS)',
    difficulty: 'hard',
    visualizerType: 'bits',
    monster: {
      id: 'hamiltonian-titan',
      name: 'Omnis the Bitmask Sovereign',
      title: 'Emperor of 2^N Visited States',
      maxHp: 4,
      hp: 4,
      sprite: 'golem',
      color: '#eab308',
      attackName: 'Bitmask Singularity Quake',
      attackPower: 3,
      defeatQuote: 'All 2^N visited states converged into the shortest Hamiltonian route...',
    },
    description: `You have an undirected, connected graph of \`n\` nodes labeled from 0 to \`n - 1\`. You are given an array \`graph\` where \`graph[i]\` is a list of all the nodes connected with node \`i\` by an edge. Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.`,
    examples: [
      { input: 'graph = [[1,2,3],[0],[0],[0]]', output: '4' },
      { input: 'graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]', output: '4' },
    ],
    constraints: ['n == graph.length', '1 <= n <= 12'],
    starterCode: `function shortestPathLength(graph) {
  return 0;
}`,
    solutionCode: `function shortestPathLength(graph) {
  const n = graph.length;
  if (n <= 1) return 0;
  const targetMask = (1 << n) - 1;
  const queue = [];
  const visited = new Set();

  for (let i = 0; i < n; i++) {
    const mask = 1 << i;
    queue.push([i, mask, 0]);
    visited.add(i + '-' + mask);
  }

  while (queue.length > 0) {
    const [node, mask, dist] = queue.shift();
    if (mask === targetMask) return dist;
    for (const next of graph[node]) {
      const nextMask = mask | (1 << next);
      const key = next + '-' + nextMask;
      if (!visited.has(key)) {
        visited.add(key);
        queue.push([next, nextMask, dist + 1]);
      }
    }
  }
  return 0;
}`,
    functionName: 'shortestPathLength',
    testCases: [
      { id: 1, input: [[[1, 2, 3], [0], [0], [0]]], expected: 4, inputDisplay: 'graph = star graph with 4 nodes', expectedDisplay: '4' },
      { id: 2, input: [[[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]], expected: 4, inputDisplay: 'graph = 5 nodes connected', expectedDisplay: '4' },
      { id: 3, input: [[[]]], expected: 0, inputDisplay: 'single node', expectedDisplay: '0' },
    ],
    hints: ['Represent the set of visited nodes as a bitmask (1 << i). Run BFS over state space (node, visited_bitmask).'],
    generateDefaultFrames: (tc) => [{
      type: 'bits',
      binaryString: ((1 << tc.input[0].length) - 1).toString(2),
      decimalValue: (1 << tc.input[0].length) - 1,
      operation: 'BFS STATE: (u, mask)',
      message: `Bitmask BFS over 2^${tc.input[0].length} visited state configurations`,
    }],
  },
  {
    id: 'triplets-with-bitwise-and-equal-to-zero',
    wingId: 'bit-manipulation',
    floor: 16,
    title: 'Boss Chamber: Triplets with Bitwise AND Equal To Zero (Frequency Map)',
    difficulty: 'hard',
    visualizerType: 'bits',
    monster: {
      id: 'zero-lich',
      name: 'Nullus-Rex the Zero Arch-Lich',
      title: 'Devourer of Non-Zero Configurations',
      maxHp: 4,
      hp: 4,
      sprite: 'lich',
      color: '#9333ea',
      attackName: 'Cataclysmic Nullification',
      attackPower: 3,
      defeatQuote: 'All triplets (i, j, k) annihilated to zero bitwise...',
    },
    description: `Given an integer array nums, return the number of AND triplets. An AND triplet is a tuple of indices (i, j, k) such that nums[i] & nums[j] & nums[k] == 0.`,
    examples: [
      { input: 'nums = [2,1,3]', output: '12' },
      { input: 'nums = [0,0,0]', output: '27' },
    ],
    constraints: ['1 <= nums.length <= 1000', '0 <= nums[i] < 2^16'],
    starterCode: `function countTriplets(nums) {
  return 0;
}`,
    solutionCode: `function countTriplets(nums) {
  const pairCount = new Array(1 << 16).fill(0);
  for (const a of nums) {
    for (const b of nums) {
      pairCount[a & b]++;
    }
  }
  let ans = 0;
  for (const c of nums) {
    for (let pair = 0; pair < (1 << 16); pair++) {
      if ((c & pair) === 0) {
        ans += pairCount[pair];
      }
    }
  }
  return ans;
}`,
    functionName: 'countTriplets',
    testCases: [
      { id: 1, input: [[2, 1, 3]], expected: 12, inputDisplay: 'nums = [2, 1, 3]', expectedDisplay: '12' },
      { id: 2, input: [[0, 0, 0]], expected: 27, inputDisplay: 'nums = [0, 0, 0]', expectedDisplay: '27' },
      { id: 3, input: [[1]], expected: 0, inputDisplay: 'nums = [1]', expectedDisplay: '0' },
    ],
    hints: ['Precompute counts of (nums[i] & nums[j]) in a table of size 2^16, reducing O(n^3) to O(n^2 + 2^16 * n).'],
    generateDefaultFrames: (tc) => [{
      type: 'bits',
      binaryString: '00000000',
      decimalValue: 0,
      operation: 'a & b & c === 0',
      message: 'Counting triplets yielding 0 with precomputed pair table',
    }],
  },
  {
    id: 'minimum-one-bit-operations',
    wingId: 'bit-manipulation',
    floor: 17,
    title: 'Boss Chamber: Minimum One Bit Operations to Make Integers Zero (Gray Code Decoding)',
    difficulty: 'hard',
    visualizerType: 'bits',
    monster: {
      id: 'gray-dragon',
      name: 'Grayus the Runic Dragon',
      title: 'Grand Sovereign of Reflected Binary Codes',
      maxHp: 4,
      hp: 4,
      sprite: 'dragon',
      color: '#dc2626',
      attackName: 'Reflected Binary Annihilation',
      attackPower: 3,
      defeatQuote: 'You decoded the Gray Code transformation in logarithmic operations...',
    },
    description: `Given an integer \`n\`, you must transform it to 0 using minimum operations: 1. Change the 0th bit of n. 2. Change the \`i\`th bit if (i-1)th bit is 1 and all lower bits (i-2..0) are 0. Return the minimum number of operations.`,
    examples: [
      { input: 'n = 3', output: '2' },
      { input: 'n = 6', output: '4' },
    ],
    constraints: ['0 <= n <= 10^9'],
    starterCode: `function minimumOneBitOperations(n) {
  return 0;
}`,
    solutionCode: `function minimumOneBitOperations(n) {
  let ans = 0;
  while (n > 0) {
    ans ^= n;
    n >>= 1;
  }
  return ans;
}`,
    functionName: 'minimumOneBitOperations',
    testCases: [
      { id: 1, input: [3], expected: 2, inputDisplay: 'n = 3', expectedDisplay: '2' },
      { id: 2, input: [6], expected: 4, inputDisplay: 'n = 6', expectedDisplay: '4' },
      { id: 3, input: [0], expected: 0, inputDisplay: 'n = 0', expectedDisplay: '0' },
    ],
    hints: ['The operation transitions correspond precisely to Gray code. The inverse Gray code formula is: ans ^= n while shifting right.'],
    generateDefaultFrames: (tc) => [{
      type: 'bits',
      binaryString: tc.input[0].toString(2),
      decimalValue: tc.input[0],
      operation: 'GRAY CODE INVERSE (ans ^= n)',
      message: `Decoding Gray code steps to reduce ${tc.input[0]} to 0`,
    }],
  },
];
