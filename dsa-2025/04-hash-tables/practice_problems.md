# Hash Tables - Practice Problems

## Problem 1: Two Sum

**Difficulty**: Easy

**Description**: Find two numbers in array that add up to target sum.

**Example**:

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
```

**Hint**: Use hash map to store value->index mapping, check for complement.

---

## Problem 2: Contains Duplicate

**Difficulty**: Easy

**Description**: Check if array contains any duplicate values.

**Example**:

```
Input: [1,2,3,1]
Output: True
```

**Hint**: Use hash set to track seen elements.

---

## Problem 3: Valid Anagram

**Difficulty**: Easy

**Description**: Check if two strings are anagrams of each other.

**Example**:

```
Input: s = "anagram", t = "nagaram"
Output: True
```

**Hint**: Count character frequencies in both strings.

---

## Problem 4: First Unique Character

**Difficulty**: Easy

**Description**: Find first non-repeating character in string.

**Example**:

```
Input: "leetcode"
Output: 0 (character 'l')
```

**Hint**: Two-pass solution - count frequencies, then find first with count 1.

---

## Problem 5: Majority Element

**Difficulty**: Easy

**Description**: Find element that appears more than n/2 times.

**Example**:

```
Input: [3,2,3]
Output: 3
```

**Hint**: Count frequencies and check which exceeds n/2.

---

## Problem 6: Group Anagrams

**Difficulty**: Medium

**Description**: Group strings that are anagrams of each other.

**Example**:

```
Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Hint**: Use sorted string as key to group anagrams.

---

## Problem 7: Top K Frequent Elements

**Difficulty**: Medium

**Description**: Find k most frequent elements in array.

**Example**:

```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```

**Hint**: Count frequencies, then use heap or bucket sort.

---

## Problem 8: Intersection of Two Arrays

**Difficulty**: Easy

**Description**: Find intersection of two arrays (unique elements).

**Example**:

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
```

**Hint**: Convert one array to set, check membership for other.

---

## Problem 9: Happy Number

**Difficulty**: Easy

**Description**: Check if number eventually becomes 1 by repeatedly replacing with sum of squares of digits.

**Example**:

```
Input: 19 → 1²+9² = 82 → 8²+2² = 68 → ... → 1
Output: True
```

**Hint**: Use set to detect cycles in the process.

---

## Problem 10: Isomorphic Strings

**Difficulty**: Easy

**Description**: Check if two strings are isomorphic (bijective character mapping).

**Example**:

```
Input: s = "egg", t = "add"
Output: True (e->a, g->d)
```

**Hint**: Use two hash maps to ensure bijective mapping.

---

## Problem 11: Word Pattern

**Difficulty**: Easy

**Description**: Check if string follows the same pattern as given pattern.

**Example**:

```
Input: pattern = "abba", s = "dog cat cat dog"
Output: True
```

**Hint**: Map pattern characters to words, ensure consistent mapping.

---

## Problem 12: Find All Anagrams in String

**Difficulty**: Medium

**Description**: Find all anagrams of pattern in string.

**Example**:

```
Input: s = "abab", p = "ab"
Output: [0,2]
```

**Hint**: Sliding window with frequency comparison.

---

## Problem 13: Longest Substring Without Repeating Characters

**Difficulty**: Medium

**Description**: Find length of longest substring without repeating characters.

**Example**:

```
Input: "abcabcbb"
Output: 3 (substring "abc")
```

**Hint**: Sliding window with hash set to track characters.

---

## Problem 14: 4Sum II

**Difficulty**: Medium

**Description**: Count tuples (i,j,k,l) where nums1[i] + nums2[j] + nums3[k] + nums4[l] = 0.

**Example**:

```
Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
```

**Hint**: Hash map to store sums of first two arrays, check complements in last two.

---

## Problem 15: Subarray Sum Equals K

**Difficulty**: Medium

**Description**: Count number of continuous subarrays whose sum equals k.

**Example**:

```
Input: nums = [1,1,1], k = 2
Output: 2
```

**Hint**: Use prefix sum and hash map to count occurrences.

---

## Problem 16: Valid Sudoku

**Difficulty**: Medium

**Description**: Check if 9×9 Sudoku board is valid.

**Example**:

```
Input: Valid sudoku board
Output: True
```

**Hint**: Use hash sets to track seen numbers in rows, columns, and boxes.

---

## Problem 17: Longest Consecutive Sequence

**Difficulty**: Medium

**Description**: Find length of longest consecutive elements sequence.

**Example**:

```
Input: [100,4,200,1,3,2]
Output: 4 (sequence [1,2,3,4])
```

**Hint**: Use hash set, for each number check if it's start of sequence.

---

## Problem 18: Design HashMap

**Difficulty**: Easy

**Description**: Implement basic hash map with put, get, remove operations.

**Example**:

```
Input: ["MyHashMap","put","put","get","get","put","get","remove","get"]
       [[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]
Output: [null,null,null,1,-1,null,1,null,-1]
```

**Hint**: Use array of buckets with linked lists for collision handling.

---

## Problem 19: Jewels and Stones

**Difficulty**: Easy

**Description**: Count how many stones are also jewels.

**Example**:

```
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
```

**Hint**: Convert jewels to set, count stones that are in set.

---

## Problem 20: Number of Good Pairs

**Difficulty**: Easy

**Description**: Count pairs (i,j) where nums[i] == nums[j] and i < j.

**Example**:

```
Input: nums = [1,2,3,1,1,3]
Output: 4
```

**Hint**: Count frequency of each number, calculate pairs using n\*(n-1)/2.
