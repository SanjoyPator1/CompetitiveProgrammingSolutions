# Two Pointers - Practice Problems

## Problem 1: Valid Palindrome

**Difficulty**: Easy

**Description**: Check if a string is a palindrome, considering only alphanumeric characters and ignoring case.

**Example**:

```
Input: "A man, a plan, a canal: Panama"
Output: True

Input: "race a car"
Output: False
```

**Hint**: Use two pointers from start and end, skip non-alphanumeric characters.

---

## Problem 2: Two Sum II - Input Array is Sorted

**Difficulty**: Easy

**Description**: Find two numbers in a sorted array that add up to a target sum.

**Example**:

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2] (1-indexed)
```

**Hint**: Use left and right pointers, move based on sum comparison.

---

## Problem 3: Remove Duplicates from Sorted Array

**Difficulty**: Easy

**Description**: Remove duplicates from a sorted array in-place and return new length.

**Example**:

```
Input: [1,1,2,2,3]
Output: 3 (array becomes [1,2,3,_,_])
```

**Hint**: Use write pointer to track unique elements position.

---

## Problem 4: Move Zeroes

**Difficulty**: Easy

**Description**: Move all zeros to the end while maintaining relative order of non-zero elements.

**Example**:

```
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```

**Hint**: Use two pointers - one for reading, one for writing non-zero elements.

---

## Problem 5: Reverse String

**Difficulty**: Easy

**Description**: Reverse a string in-place.

**Example**:

```
Input: ['h','e','l','l','o']
Output: ['o','l','l','e','h']
```

**Hint**: Swap characters from both ends moving inward.

---

## Problem 6: Container With Most Water

**Difficulty**: Medium

**Description**: Find two lines that form a container holding the most water.

**Example**:

```
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```

**Hint**: Use two pointers at ends, move the pointer with smaller height.

---

## Problem 7: 3Sum

**Difficulty**: Medium

**Description**: Find all unique triplets that sum to zero.

**Example**:

```
Input: [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

**Hint**: Sort array, fix one element, use two pointers for remaining two.

---

## Problem 8: Remove Element

**Difficulty**: Easy

**Description**: Remove all instances of a value in-place and return new length.

**Example**:

```
Input: nums = [3,2,2,3], val = 3
Output: 2 (array becomes [2,2,_,_])
```

**Hint**: Use write pointer to overwrite elements that aren't equal to val.

---

## Problem 9: Squares of Sorted Array

**Difficulty**: Easy

**Description**: Return squares of a sorted array in sorted order.

**Example**:

```
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
```

**Hint**: Use two pointers from ends since largest squares are at extremes.

---

## Problem 10: Trapping Rain Water

**Difficulty**: Hard

**Description**: Calculate how much water can be trapped after raining.

**Example**:

```
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

**Hint**: Use two pointers with left_max and right_max tracking.

---

## Problem 11: Sort Colors

**Difficulty**: Medium

**Description**: Sort an array with only 0s, 1s, and 2s in-place.

**Example**:

```
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```

**Hint**: Use three pointers (Dutch National Flag algorithm).

---

## Problem 12: 4Sum

**Difficulty**: Medium

**Description**: Find all unique quadruplets that sum to target.

**Example**:

```
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

**Hint**: Extension of 3Sum with additional outer loop.

---

## Problem 13: Partition Labels

**Difficulty**: Medium

**Description**: Partition string into as many parts as possible so each letter appears in at most one part.

**Example**:

```
Input: "ababcbacadefegdehijhklij"
Output: [9,7,8]
```

**Hint**: Find last occurrence of each character, use two pointers to track partitions.

---

## Problem 14: Minimum Window Substring

**Difficulty**: Hard

**Description**: Find minimum window in string s that contains all characters of string t.

**Example**:

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
```

**Hint**: Use two pointers to maintain sliding window, expand right until valid, then contract left.

---

## Problem 15: 3Sum Closest

**Difficulty**: Medium

**Description**: Find three integers whose sum is closest to the target.

**Example**:

```
Input: nums = [-1,2,1,-4], target = 1
Output: 2 (sum of -1 + 2 + 1 = 2)
```

**Hint**: Similar to 3Sum but track minimum difference instead of exact match.

---

## Problem 16: Remove Duplicates from Sorted Array II

**Difficulty**: Medium

**Description**: Remove duplicates such that each element appears at most twice.

**Example**:

```
Input: [1,1,1,2,2,3]
Output: 5 (array becomes [1,1,2,2,3,_])
```

**Hint**: Use write pointer and count occurrences of current element.

---

## Problem 17: Backspace String Compare

**Difficulty**: Easy

**Description**: Compare two strings where '#' represents backspace operation.

**Example**:

```
Input: s = "ab#c", t = "ad#c"
Output: True (both become "ac")
```

**Hint**: Process strings from right to left using two pointers.

---

## Problem 18: Interval List Intersections

**Difficulty**: Medium

**Description**: Find intersections of two sorted interval lists.

**Example**:

```
Input: firstList = [[0,2],[5,10],[13,23],[24,25]]
       secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
```

**Hint**: Use two pointers to traverse both lists simultaneously.

---

## Problem 19: Sort Array By Parity

**Difficulty**: Easy

**Description**: Sort array so all even numbers come before odd numbers.

**Example**:

```
Input: [3,1,2,4]
Output: [2,4,3,1] (or any valid arrangement)
```

**Hint**: Use two pointers - one from start, one from end, swap when needed.

---

## Problem 20: Linked List Cycle II

**Difficulty**: Medium

**Description**: Find the node where cycle begins in a linked list.

**Example**:

```
Input: head = [3,2,0,-4], pos = 1 (cycle starts at node with value 2)
Output: Node with value 2
```

**Hint**: Use Floyd's algorithm to detect cycle, then find start position.

---

## Advanced Tips for Two Pointers Problems

### Problem-Solving Strategy:

1. **Identify the type**: Opposite direction vs Same direction
2. **Check if sorting helps**: Many problems become easier after sorting
3. **Handle edge cases**: Empty arrays, single elements, no valid answer
4. **Optimize pointer movement**: Skip duplicates when possible
5. **Consider multiple passes**: Sometimes need preprocessing

### Common Optimizations:

- **Skip duplicates**: `while left < right and arr[left] == arr[left+1]: left += 1`
- **Early termination**: Stop when impossible to find better solution
- **Boundary checks**: Always verify pointer validity before access

### Pattern Recognition:

- **Target sum problems** → Sort + two pointers
- **Palindrome problems** → Expand from center or opposite pointers
- **Array modification** → Read/write pointers
- **Cycle detection** → Fast/slow pointers
- **Merge operations** → Two pointers on different arrays

### Complexity Analysis:

- Most two-pointer solutions are **O(n) time**
- Space complexity usually **O(1)** unless storing results
- Sorting preprocessing adds **O(n log n)** time

### Testing Strategy:

1. **Empty input**: `[]` or `""`
2. **Single element**: `[1]` or `"a"`
3. **No solution exists**: Verify proper handling
4. **All elements same**: `[1,1,1,1]`
5. **Already optimal**: Pre-sorted or pre-arranged input
6. **Edge values**: Minimum/maximum constraints

### Common Mistakes:

1. **Forgetting to move pointers**: Causes infinite loops
2. **Wrong boundary conditions**: `<=` vs `<`
3. **Not handling duplicates**: Especially in sum problems
4. **Index out of bounds**: Always check validity
5. **Not considering sorted requirement**: Some patterns need sorting first

### Next Level Practice:

After mastering these problems, try:

- **Multi-pointer problems**: 4Sum and beyond
- **Linked list variations**: Cycle detection, intersection
- **String processing**: Advanced palindrome problems
- **Interval problems**: Merging and intersections
- **Geometric problems**: Closest pair of points
