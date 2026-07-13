# Arrays and Strings - Practice Problems

## Problem 1: Find Maximum Element

**Difficulty**: Easy

**Description**: Find the maximum element in an array of integers.

**Example**:

```
Input: [3, 1, 4, 1, 5, 9, 2, 6]
Output: 9
```

**Constraints**:

- 1 ≤ array length ≤ 1000
- -10^6 ≤ elements ≤ 10^6

---

## Problem 2: Reverse String

**Difficulty**: Easy

**Description**: Reverse a string in-place (if using a mutable array) or return a new reversed string.

**Example**:

```
Input: "hello"
Output: "olleh"
```

**Constraints**:

- 0 ≤ string length ≤ 1000

---

## Problem 3: Two Sum

**Difficulty**: Easy

**Description**: Given an array of integers and a target sum, return indices of two numbers that add up to the target.

**Example**:

```
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1] (because nums[0] + nums[1] = 2 + 7 = 9)
```

**Constraints**:

- Each input has exactly one solution
- Cannot use the same element twice

---

## Problem 4: Valid Anagram

**Difficulty**: Easy

**Description**: Check if two strings are anagrams of each other.

**Example**:

```
Input: s = "listen", t = "silent"
Output: True

Input: s = "rat", t = "car"
Output: False
```

**Constraints**:

- Strings contain only lowercase letters

---

## Problem 5: Remove Duplicates from Sorted Array

**Difficulty**: Easy

**Description**: Remove duplicates from a sorted array in-place and return the new length.

**Example**:

```
Input: [1, 1, 2, 2, 3, 4, 4, 5]
Output: 5 (array becomes [1, 2, 3, 4, 5, _, _, _])
```

**Constraints**:

- Array is sorted in ascending order

---

## Problem 6: First Unique Character

**Difficulty**: Easy

**Description**: Find the first non-repeating character in a string and return its index.

**Example**:

```
Input: "leetcode"
Output: 0 (character 'l' at index 0)

Input: "loveleetcode"
Output: 2 (character 'v' at index 2)
```

**Constraints**:

- String contains only lowercase letters

---

## Problem 7: Move Zeros

**Difficulty**: Easy

**Description**: Move all zeros in an array to the end while maintaining the relative order of non-zero elements.

**Example**:

```
Input: [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]
```

**Constraints**:

- Modify the array in-place

---

## Problem 8: Valid Palindrome

**Difficulty**: Easy

**Description**: Check if a string is a palindrome, considering only alphanumeric characters and ignoring case.

**Example**:

```
Input: "A man, a plan, a canal: Panama"
Output: True

Input: "race a car"
Output: False
```

**Constraints**:

- Consider only alphanumeric characters

---

## Problem 9: Merge Sorted Arrays

**Difficulty**: Easy

**Description**: Merge two sorted arrays into the first array in-place.

**Example**:

```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
```

**Constraints**:

- nums1 has enough space to hold elements from nums2

---

## Problem 10: Contains Duplicate

**Difficulty**: Easy

**Description**: Check if an array contains any duplicate values.

**Example**:

```
Input: [1,2,3,1]
Output: True

Input: [1,2,3,4]
Output: False
```

**Constraints**:

- 1 ≤ array length ≤ 10^5

---

## Problem 11: Roman to Integer

**Difficulty**: Medium

**Description**: Convert a Roman numeral string to an integer.

**Example**:

```
Input: "III"
Output: 3

Input: "MCMXC"
Output: 1990
```

**Constraints**:

- Valid Roman numeral (I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

---

## Problem 12: Longest Common Prefix

**Difficulty**: Medium

**Description**: Find the longest common prefix among an array of strings.

**Example**:

```
Input: ["flower","flow","flight"]
Output: "fl"

Input: ["dog","racecar","car"]
Output: ""
```

**Constraints**:

- All strings contain only lowercase letters

---

## Problem 13: Product of Array Except Self

**Difficulty**: Medium

**Description**: Return an array where each element is the product of all elements except itself.

**Example**:

```
Input: [1,2,3,4]
Output: [24,12,8,6]
```

**Constraints**:

- Cannot use division operator
- O(n) time complexity

---

## Problem 14: Group Anagrams

**Difficulty**: Medium

**Description**: Group strings that are anagrams of each other.

**Example**:

```
Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Constraints**:

- Strings contain only lowercase letters

---

## Problem 15: Longest Substring Without Repeating Characters

**Difficulty**: Medium

**Description**: Find the length of the longest substring without repeating characters.

**Example**:

```
Input: "abcabcbb"
Output: 3 (substring "abc")

Input: "pwwkew"
Output: 3 (substring "wke")
```

**Constraints**:

- String contains ASCII characters

---

## Problem 16: Valid Parentheses

**Difficulty**: Medium

**Description**: Check if a string of parentheses is valid (properly opened and closed).

**Example**:

```
Input: "()[]{}"
Output: True

Input: "([)]"
Output: False
```

**Constraints**:

- String contains only '(', ')', '{', '}', '[', ']'

---

## Problem 17: Three Sum

**Difficulty**: Medium

**Description**: Find all unique triplets that sum to zero.

**Example**:

```
Input: [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
```

**Constraints**:

- Solution must not contain duplicate triplets

---

## Problem 18: String to Integer (atoi)

**Difficulty**: Medium

**Description**: Implement string to integer conversion with proper handling of edge cases.

**Example**:

```
Input: "42"
Output: 42

Input: "   -42"
Output: -42

Input: "4193 with words"
Output: 4193
```

**Constraints**:

- Handle whitespace, signs, overflow

---

## Problem 19: Container With Most Water

**Difficulty**: Medium

**Description**: Find two lines that together with the x-axis form a container that holds the most water.

**Example**:

```
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```

**Constraints**:

- Array represents heights of vertical lines

---

## Problem 20: Rotate Array

**Difficulty**: Medium

**Description**: Rotate an array to the right by k steps.

**Example**:

```
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
```

**Constraints**:

- Try to solve in O(1) extra space

---

## Tips for Solving These Problems

### Easy Problems (1-10):

- Focus on basic array/string operations
- Practice edge case handling
- Implement brute force first, then optimize

### Medium Problems (11-20):

- Look for patterns (two pointers, hash maps)
- Consider multiple approaches
- Pay attention to time/space complexity

### General Approach:

1. Read the problem carefully
2. Work through examples manually
3. Identify the pattern or technique needed
4. Implement step by step
5. Test with edge cases
6. Optimize if needed

### Common Techniques Used:

- Two pointers
- Hash maps for O(1) lookup
- Sorting for easier processing
- In-place modifications
- Prefix/suffix arrays
- Stack for parentheses matching
