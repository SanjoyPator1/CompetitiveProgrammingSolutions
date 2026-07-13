# Sliding Window - Practice Problems

## Problem 1: Maximum Sum Subarray of Size K

**Difficulty**: Easy

**Description**: Find the maximum sum of any contiguous subarray of size k.

**Example**:

```
Input: arr = [2, 1, 5, 1, 3, 2], k = 3
Output: 9 (subarray [5, 1, 3])
```

**Hint**: Use fixed-size sliding window, maintain running sum.

---

## Problem 2: Average of Subarrays of Size K

**Difficulty**: Easy

**Description**: Find the average of all contiguous subarrays of size k.

**Example**:

```
Input: arr = [1, 3, 2, 6, -1, 4, 1, 8, 2], k = 5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]
```

**Hint**: Similar to maximum sum, but calculate average for each window.

---

## Problem 3: First Negative Number in Every Window

**Difficulty**: Easy

**Description**: Find the first negative number in every contiguous subarray of size k.

**Example**:

```
Input: arr = [12, -1, -7, 8, -15, 30, 16, 28], k = 3
Output: [-1, -1, -7, -15, -15, 0]
```

**Hint**: Use deque to store indices of negative numbers.

---

## Problem 4: Longest Substring Without Repeating Characters

**Difficulty**: Medium

**Description**: Find the length of the longest substring without repeating characters.

**Example**:

```
Input: "abcabcbb"
Output: 3 (substring "abc")
```

**Hint**: Use variable window with hash set to track characters.

---

## Problem 5: Minimum Size Subarray Sum

**Difficulty**: Medium

**Description**: Find the minimal length of contiguous subarray whose sum ≥ target.

**Example**:

```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2 (subarray [4,3])
```

**Hint**: Expand window until sum ≥ target, then contract to minimize length.

---

## Problem 6: Fruits Into Baskets

**Difficulty**: Medium

**Description**: Pick maximum fruits with at most 2 types (longest subarray with at most 2 distinct elements).

**Example**:

```
Input: fruits = [1,2,1,2,3,1,2]
Output: 5 (subarray [1,2,1,2,3] has 2 types)
```

**Hint**: Variable window with hash map tracking fruit types.

---

## Problem 7: Longest Substring with At Most K Distinct Characters

**Difficulty**: Medium

**Description**: Find the longest substring that contains at most k distinct characters.

**Example**:

```
Input: s = "eceba", k = 2
Output: 3 (substring "ece")
```

**Hint**: Use hash map to count characters, contract when > k distinct.

---

## Problem 8: Maximum Number of Vowels in Substring

**Difficulty**: Medium

**Description**: Find maximum number of vowels in any substring of length k.

**Example**:

```
Input: s = "abciiidef", k = 3
Output: 3 (substring "iii")
```

**Hint**: Fixed window, count vowels in current window.

---

## Problem 9: Contains Duplicate II

**Difficulty**: Easy

**Description**: Check if array contains duplicates within distance k.

**Example**:

```
Input: nums = [1,2,3,1], k = 3
Output: True (indices 0 and 3, distance = 3)
```

**Hint**: Use sliding window with hash set of size at most k.

---

## Problem 10: Find All Anagrams in String

**Difficulty**: Medium

**Description**: Find all start indices of anagrams of pattern in string.

**Example**:

```
Input: s = "abab", p = "ab"
Output: [0, 2] (substrings "ab" and "ab")
```

**Hint**: Fixed window of pattern length, compare character frequencies.

---

## Problem 11: Permutation in String

**Difficulty**: Medium

**Description**: Check if any permutation of s1 is a substring of s2.

**Example**:

```
Input: s1 = "ab", s2 = "eidbaooo"
Output: True (s2 contains "ba" which is permutation of "ab")
```

**Hint**: Similar to anagrams, fixed window with frequency matching.

---

## Problem 12: Longest Repeating Character Replacement

**Difficulty**: Medium

**Description**: Find longest substring with same character after replacing at most k characters.

**Example**:

```
Input: s = "ABAB", k = 2
Output: 4 (replace both B's with A's to get "AAAA")
```

**Hint**: Track max frequency character, window size - max_freq ≤ k.

---

## Problem 13: Max Consecutive Ones III

**Difficulty**: Medium

**Description**: Find maximum consecutive 1's after flipping at most k zeros.

**Example**:

```
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6 (flip zeros at indices 4,5 to get 6 consecutive 1's)
```

**Hint**: Count zeros in window, contract when zeros > k.

---

## Problem 14: Sliding Window Maximum

**Difficulty**: Medium

**Description**: Find maximum element in every sliding window of size k.

**Example**:

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
```

**Hint**: Use deque to maintain potential maximums in decreasing order.

---

## Problem 15: Minimum Window Substring

**Difficulty**: Medium

**Description**: Find minimum window in s that contains all characters of t.

**Example**:

```
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
```

**Hint**: Expand until all chars covered, then contract to minimize.

---

## Problem 16: Longest Substring with At Least K Repeating Characters

**Difficulty**: Medium

**Description**: Find longest substring where every character appears at least k times.

**Example**:

```
Input: s = "aaabb", k = 3
Output: 3 (substring "aaa")
```

**Hint**: Use divide and conquer or sliding window with frequency constraints.

---

## Problem 17: Grumpy Bookstore Owner

**Difficulty**: Medium

**Description**: Maximize satisfied customers using technique for k minutes.

**Example**:

```
Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], k = 3
Output: 16
```

**Hint**: Fixed window to find best k minutes to apply technique.

---

## Problem 18: Get Equal Substrings Within Budget

**Difficulty**: Medium

**Description**: Find longest substring you can get by changing at most maxCost.

**Example**:

```
Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
```

**Hint**: Variable window, track total cost of changes.

---

## Solving Strategy for Sliding Window Problems

### Step-by-Step Approach:

1. **Identify window type**: Fixed vs Variable size
2. **Determine what to track**: Sum, count, frequency, etc.
3. **Choose data structure**: Array, hash map, deque
4. **Implement expansion**: Add right element to window
5. **Implement contraction**: Remove left elements when needed
6. **Update result**: Track optimal window found so far

### Common Patterns:

- **Fixed size + optimization**: Maximum/minimum in window
- **Variable size + constraint**: At most k distinct, sum ≥ target
- **Frequency matching**: Anagrams, permutations
- **Character replacement**: At most k changes allowed

### Key Insights:

- Each element enters and leaves window at most once → O(n) time
- Use appropriate data structures for O(1) window operations
- Handle edge cases: empty input, k > length, no valid window

### Testing Tips:

1. **Empty/single element**: Edge cases
2. **k equals array length**: Entire array is window
3. **No valid solution**: Return appropriate default
4. **All elements same**: Verify logic works
5. **Optimal at boundaries**: First/last elements
