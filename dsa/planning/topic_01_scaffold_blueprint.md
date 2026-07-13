# Topic 01: Arrays & Strings — Problem Scaffolding Blueprint

## Instructions for AI Agent

This file contains the COMPLETE specification for scaffolding problem files 6-20 in
`dsa-2025/01-arrays-strings/solutions/`. Problems 1-5 are already created — use them
as reference for the format (look at any file like `03_two_sum.py`).

### File Naming Convention
`{number:02d}_{snake_case_name}.py` — e.g., `06_first_unique_char.py`

### Template Structure (MUST follow for every file)
```
1. Box header with problem name
2. Metadata block (Difficulty, Pattern, LeetCode, Key Insight, Time, Space)
3. Interview Tip (💡) and Pattern Recognition (🧠) notes
4. from typing import List (and other imports as needed)
5. Brute force function with hints (body = pass)
6. Optimized function with hints + walkthrough example (body = pass)
7. Test cases section with assert statements
8. Edge cases clearly labeled
9. print("✅ All tests passed!") at the end
```

> **CRITICAL: ALL function bodies must be `pass`. Do NOT write solutions. Only hints.**

---

## Problem 6: First Unique Character

- **File**: `06_first_unique_char.py`
- **Difficulty**: Easy
- **Pattern**: #️⃣ Hash Map (frequency counting)
- **LeetCode**: https://leetcode.com/problems/first-unique-character-in-a-string/
- **Key Insight**: Count frequencies first, then find the first char with count == 1.
- **Time**: O(n) → O(n) (two passes — one to count, one to find)
- **Space**: O(1) — at most 26 lowercase letters
- **💡 Interview Tip**: Two-pass is fine here. Don't try to do it in one pass — it's actually harder and not necessary.
- **🧠 Pattern Recognition**: "Find first/last element with specific frequency" = frequency map + second scan.

### Functions
```python
def first_unique_brute(s: str) -> int:
    """
    Approach: For each character, check if it appears elsewhere.
    Hints:
    - For each index i, scan rest of string for duplicates
    - Time: O(n²), Space: O(1)
    """
    pass

def first_unique_hashmap(s: str) -> int:
    """
    Approach: Count frequencies, then find first with count 1.
    Hints:
    - Pass 1: Build frequency map {char: count}
    - Pass 2: Iterate string again, return first index where count == 1
    - Return -1 if no unique character exists
    - You can use collections.Counter
    
    Walk through:
        "leetcode"
        freq: {'l':1, 'e':3, 't':1, 'c':1, 'o':1, 'd':1}
        Scan: s[0]='l', freq['l']=1 → return 0
    """
    pass
```

### Test Cases
```python
assert first_unique_hashmap("leetcode") == 0
assert first_unique_hashmap("loveleetcode") == 2
assert first_unique_hashmap("aabb") == -1            # no unique
assert first_unique_hashmap("") == -1                 # empty string
assert first_unique_hashmap("a") == 0                 # single char
assert first_unique_hashmap("aadadaad") == -1         # all repeated
```

---

## Problem 7: Move Zeros

- **File**: `07_move_zeros.py`
- **Difficulty**: Easy
- **Pattern**: 🔀 Two Pointers (fast-slow / read-write) + 🔧 In-Place
- **LeetCode**: https://leetcode.com/problems/move-zeroes/
- **Key Insight**: Use a write pointer to place non-zero elements at the front, then fill rest with zeros.
- **Time**: O(n)
- **Space**: O(1) — in-place
- **💡 Interview Tip**: This is the exact same pattern as Remove Duplicates (Problem 5). If you solved that, this is free. Interviewers look for you to recognize this.
- **🧠 Pattern Recognition**: "Move/remove elements in-place" = fast-slow two pointers. The write pointer always trails behind or stays with the read pointer.

### Functions
```python
def move_zeros(nums: List[int]) -> None:
    """
    Approach: Write pointer for non-zeros, then fill remaining with 0.
    Hints:
    - 'write' pointer starts at 0
    - Scan with 'read' pointer: if nums[read] != 0, copy to write position
    - After scan, fill positions from 'write' to end with 0
    - Modify array in-place, return None
    
    Walk through:
        [0, 1, 0, 3, 12]
        read=0: 0 → skip
        read=1: 1 → write to pos 0, write=1
        read=2: 0 → skip
        read=3: 3 → write to pos 1, write=2
        read=4: 12 → write to pos 2, write=3
        Fill [3:] with 0 → [1, 3, 12, 0, 0]
    """
    pass
```

### Test Cases
```python
nums1 = [0, 1, 0, 3, 12]
move_zeros(nums1)
assert nums1 == [1, 3, 12, 0, 0]

nums2 = [0]
move_zeros(nums2)
assert nums2 == [0]                    # single zero

nums3 = [1, 2, 3]
move_zeros(nums3)
assert nums3 == [1, 2, 3]             # no zeros

nums4 = [0, 0, 0, 0]
move_zeros(nums4)
assert nums4 == [0, 0, 0, 0]          # all zeros

nums5 = [1]
move_zeros(nums5)
assert nums5 == [1]                    # single non-zero

nums6 = [0, 0, 1]
move_zeros(nums6)
assert nums6 == [1, 0, 0]             # zeros at start
```

---

## Problem 8: Valid Palindrome

- **File**: `08_valid_palindrome.py`
- **Difficulty**: Easy
- **Pattern**: 🔀 Two Pointers (converging from both ends)
- **LeetCode**: https://leetcode.com/problems/valid-palindrome/
- **Key Insight**: Use two pointers from both ends, skip non-alphanumeric chars, compare case-insensitively.
- **Time**: O(n)
- **Space**: O(1) — just two pointers
- **💡 Interview Tip**: The tricky part is handling non-alphanumeric characters. Use `char.isalnum()` and `char.lower()`. Don't create a cleaned string — that's O(n) space.
- **🧠 Pattern Recognition**: "Check symmetry" or "compare from both ends" = converging two pointers.

### Functions
```python
def is_palindrome_clean(s: str) -> bool:
    """
    Approach: Clean string first, then check.
    Hints:
    - Filter out non-alphanumeric, convert to lowercase
    - Compare cleaned string with its reverse
    - Time: O(n), Space: O(n) — not optimal
    """
    pass

def is_palindrome_two_pointers(s: str) -> bool:
    """
    Approach: Two pointers from both ends, skip non-alphanumeric.
    Hints:
    - left starts at 0, right starts at len-1
    - Skip non-alphanumeric: while not s[left].isalnum(): left += 1
    - Compare s[left].lower() == s[right].lower()
    - If mismatch → return False
    - If pointers meet → return True
    - Be careful with bounds checking!
    
    Walk through:
        "A man, a plan, a canal: Panama"
        left→'A' right→'a' → match (case insensitive)
        left→'m' right→'m' → match
        ...all match → True
    """
    pass
```

### Test Cases
```python
assert is_palindrome_two_pointers("A man, a plan, a canal: Panama") == True
assert is_palindrome_two_pointers("race a car") == False
assert is_palindrome_two_pointers("") == True               # empty is palindrome
assert is_palindrome_two_pointers(" ") == True               # spaces only
assert is_palindrome_two_pointers("a") == True               # single char
assert is_palindrome_two_pointers(".,") == True              # only non-alnum
assert is_palindrome_two_pointers("0P") == False             # mixed types
```

---

## Problem 9: Merge Sorted Arrays

- **File**: `09_merge_sorted_arrays.py`
- **Difficulty**: Easy
- **Pattern**: 🔀 Two Pointers (three pointers, merge from the end)
- **LeetCode**: https://leetcode.com/problems/merge-sorted-array/
- **Key Insight**: Start merging from the END of nums1 (where there's empty space). Compare largest elements first.
- **Time**: O(m + n)
- **Space**: O(1) — in-place
- **💡 Interview Tip**: The key trick is merging BACKWARDS. If you merge forward, you'll overwrite elements you haven't processed yet. This is a classic insight.
- **🧠 Pattern Recognition**: "Merge two sorted sequences in-place" = three pointers from the end.

### Functions
```python
def merge_brute(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Approach: Copy nums2 into nums1, then sort.
    Hints:
    - Place nums2 elements at positions m, m+1, ... m+n-1
    - Sort the entire array
    - Time: O((m+n) log(m+n)), Space: O(1)
    """
    pass

def merge_optimized(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Approach: Three pointers, merge from the end.
    Hints:
    - p1 = m - 1 (last real element in nums1)
    - p2 = n - 1 (last element in nums2)
    - write = m + n - 1 (last position in nums1)
    - Compare nums1[p1] vs nums2[p2], place larger at write position
    - Move the used pointer and write pointer backward
    - If p1 runs out, copy remaining nums2 elements
    - (If p2 runs out, nums1 elements are already in place!)
    
    Walk through:
        nums1 = [1,2,3,0,0,0], m=3, nums2 = [2,5,6], n=3
        write=5: compare 3 vs 6 → place 6 at [5]
        write=4: compare 3 vs 5 → place 5 at [4]
        write=3: compare 3 vs 2 → place 3 at [3]
        write=2: compare 2 vs 2 → place 2 at [2]
        write=1: p1=0, compare 1 vs 2 → place 2 at [1]
        p2 done → result [1,2,2,3,5,6]
    """
    pass
```

### Test Cases
```python
nums1 = [1,2,3,0,0,0]
merge_optimized(nums1, 3, [2,5,6], 3)
assert nums1 == [1,2,2,3,5,6]

nums2 = [1]
merge_optimized(nums2, 1, [], 0)
assert nums2 == [1]                         # nothing to merge

nums3 = [0]
merge_optimized(nums3, 0, [1], 1)
assert nums3 == [1]                         # nums1 is empty

nums4 = [4,5,6,0,0,0]
merge_optimized(nums4, 3, [1,2,3], 3)
assert nums4 == [1,2,3,4,5,6]              # nums2 all smaller

nums5 = [1,2,3,0,0,0]
merge_optimized(nums5, 3, [4,5,6], 3)
assert nums5 == [1,2,3,4,5,6]              # nums2 all larger
```

---

## Problem 10: Contains Duplicate

- **File**: `10_contains_duplicate.py`
- **Difficulty**: Easy
- **Pattern**: #️⃣ Hash Set (existence check)
- **LeetCode**: https://leetcode.com/problems/contains-duplicate/
- **Key Insight**: A set gives O(1) lookup — add elements, if already in set → duplicate found.
- **Time**: O(n² or n log n) → O(n) (brute/sort → hash set)
- **Space**: O(1) → O(n) (brute → hash set)
- **💡 Interview Tip**: Three approaches exist. Know trade-offs: brute O(n²)/O(1), sort O(n log n)/O(1), hash set O(n)/O(n).
- **🧠 Pattern Recognition**: "Does X exist in collection?" = Hash Set. Fastest existence check.

### Functions
```python
def contains_duplicate_brute(nums: List[int]) -> bool:
    """
    Approach: Check every pair.
    Hints:
    - Two nested loops, compare all pairs
    - Time: O(n²), Space: O(1)
    """
    pass

def contains_duplicate_sort(nums: List[int]) -> bool:
    """
    Approach: Sort, then check adjacent elements.
    Hints:
    - Sort the array
    - If any nums[i] == nums[i+1] → duplicate
    - Time: O(n log n), Space: O(1) if in-place sort
    """
    pass

def contains_duplicate_set(nums: List[int]) -> bool:
    """
    Approach: Use a hash set.
    Hints:
    - Iterate through array
    - If num already in set → return True
    - Otherwise add to set
    - Time: O(n), Space: O(n)
    
    Alternative one-liner (know this but explain the above in interview):
        return len(nums) != len(set(nums))
    """
    pass
```

### Test Cases
```python
assert contains_duplicate_set([1,2,3,1]) == True
assert contains_duplicate_set([1,2,3,4]) == False
assert contains_duplicate_set([1,1,1,3,3,4,3,2,4,2]) == True
assert contains_duplicate_set([]) == False               # empty
assert contains_duplicate_set([1]) == False              # single element
assert contains_duplicate_set([1,1]) == True             # two same
assert contains_duplicate_set([1,2]) == False            # two different
```

---

## Problem 11: Roman to Integer

- **File**: `11_roman_to_integer.py`
- **Difficulty**: Medium
- **Pattern**: #️⃣ Hash Map (lookup table) + Linear Scan
- **LeetCode**: https://leetcode.com/problems/roman-to-integer/
- **Key Insight**: If a smaller value appears BEFORE a larger value, subtract it (e.g., IV = 4). Otherwise, add it.
- **Time**: O(n)
- **Space**: O(1) — fixed-size lookup map (7 entries)
- **💡 Interview Tip**: The subtraction rule is the only tricky part. Compare current char value with NEXT char value.
- **🧠 Pattern Recognition**: "Convert using rules with context" = scan with lookahead.

### Functions
```python
def roman_to_int(s: str) -> int:
    """
    Approach: Map + linear scan with lookahead.
    Hints:
    - Create map: {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    - Iterate through string
    - If current value < next value → SUBTRACT current (e.g., I before V = 4)
    - Otherwise → ADD current
    - Handle last character separately (no next to compare)
    
    Walk through:
        "MCMXCIV" = 1994
        M=1000 (M>C → add) → 1000
        C=100  (C<M → subtract) → 900
        M=1000 (M>X → add) → 1900
        X=10   (X<C → subtract) → 1890
        C=100  (C>I → add) → 1990
        I=1    (I<V → subtract) → 1989... wait
        V=5    (last → add) → 1994 ✓
    """
    pass
```

### Test Cases
```python
assert roman_to_int("III") == 3
assert roman_to_int("LVIII") == 58
assert roman_to_int("MCMXCIV") == 1994
assert roman_to_int("IV") == 4                  # subtraction case
assert roman_to_int("IX") == 9                  # subtraction case
assert roman_to_int("XL") == 40                 # subtraction case
assert roman_to_int("XC") == 90                 # subtraction case
assert roman_to_int("CD") == 400                # subtraction case
assert roman_to_int("CM") == 900                # subtraction case
assert roman_to_int("I") == 1                   # single char
assert roman_to_int("MMMCMXCIX") == 3999        # max valid roman
```

---

## Problem 12: Longest Common Prefix

- **File**: `12_longest_common_prefix.py`
- **Difficulty**: Medium
- **Pattern**: 🔧 Vertical Scanning (character-by-character comparison)
- **LeetCode**: https://leetcode.com/problems/longest-common-prefix/
- **Key Insight**: Compare characters at the same position across all strings. Stop at first mismatch.
- **Time**: O(S) where S = sum of all characters in all strings
- **Space**: O(1)
- **💡 Interview Tip**: Multiple approaches exist (vertical scan, horizontal scan, divide & conquer, binary search). Vertical scan is simplest and sufficient.
- **🧠 Pattern Recognition**: "Compare multiple sequences" = iterate position by position.

### Functions
```python
def longest_common_prefix_brute(strs: List[str]) -> str:
    """
    Approach: Horizontal scan — compare first two, then result with third, etc.
    Hints:
    - Start with prefix = strs[0]
    - For each next string, shorten prefix until it matches
    - Time: O(S), Space: O(1)
    """
    pass

def longest_common_prefix(strs: List[str]) -> str:
    """
    Approach: Vertical scan — check one character position at a time.
    Hints:
    - For each position i (0, 1, 2, ...):
      - Get char at position i from first string
      - Check if ALL other strings have the same char at position i
      - If any string is too short or has different char → return prefix so far
    - Edge case: empty list → return ""
    
    Walk through:
        ["flower", "flow", "flight"]
        pos 0: f,f,f → match
        pos 1: l,l,l → match
        pos 2: o,o,i → MISMATCH → return "fl"
    """
    pass
```

### Test Cases
```python
assert longest_common_prefix(["flower","flow","flight"]) == "fl"
assert longest_common_prefix(["dog","racecar","car"]) == ""
assert longest_common_prefix(["interspecies","interstellar","interstate"]) == "inters"
assert longest_common_prefix([""]) == ""                    # single empty
assert longest_common_prefix(["a"]) == "a"                  # single string
assert longest_common_prefix(["","b"]) == ""                # one empty
assert longest_common_prefix(["abc","abc","abc"]) == "abc"  # all same
assert longest_common_prefix([]) == ""                      # empty list
```

---

## Problem 13: Product of Array Except Self

- **File**: `13_product_except_self.py`
- **Difficulty**: Medium
- **Pattern**: 📊 Prefix/Suffix (left-right product passes)
- **LeetCode**: https://leetcode.com/problems/product-of-array-except-self/
- **Key Insight**: For each position, result = product of everything LEFT × product of everything RIGHT. Build both in two passes.
- **Time**: O(n)
- **Space**: O(1) extra (output array doesn't count)
- **💡 Interview Tip**: The constraint "no division" is key. With division you'd just do total_product / nums[i], but that fails with zeros. The prefix/suffix approach handles zeros naturally.
- **🧠 Pattern Recognition**: "Need aggregate of everything except current" = prefix + suffix passes.

### Functions
```python
def product_except_self_brute(nums: List[int]) -> List[int]:
    """
    Approach: For each element, multiply all others.
    Hints:
    - For each i, loop through all j != i and multiply
    - Time: O(n²), Space: O(n)
    """
    pass

def product_except_self(nums: List[int]) -> List[int]:
    """
    Approach: Two passes — left products then right products.
    Hints:
    - Create result array of 1s
    - LEFT PASS: result[i] = running product of all elements to the left
      - Maintain left_product, start at 1
      - result[i] = left_product, then left_product *= nums[i]
    - RIGHT PASS: multiply result[i] by running product from the right
      - Maintain right_product, start at 1
      - result[i] *= right_product, then right_product *= nums[i]
    
    Walk through:
        nums = [1, 2, 3, 4]
        
        Left pass (left_product):
          result = [1, 1, 2, 6]    (each = product of everything before it)
        
        Right pass (right_product):
          result[3] *= 1 = 6       right_product = 4
          result[2] *= 4 = 8       right_product = 12
          result[1] *= 12 = 12     right_product = 24
          result[0] *= 24 = 24     right_product = 24
        
        result = [24, 12, 8, 6] ✓
    """
    pass
```

### Test Cases
```python
assert product_except_self([1,2,3,4]) == [24,12,8,6]
assert product_except_self([-1,1,0,-3,3]) == [0,0,9,0,0]  # with zero
assert product_except_self([1,1]) == [1,1]                  # two elements
assert product_except_self([2,3]) == [3,2]                  # two elements
assert product_except_self([0,0]) == [0,0]                  # two zeros
assert product_except_self([5]) == [1]                       # single element (debatable)
```

---

## Problem 14: Group Anagrams

- **File**: `14_group_anagrams.py`
- **Difficulty**: Medium
- **Pattern**: #️⃣ Hash Map (grouping by key)
- **LeetCode**: https://leetcode.com/problems/group-anagrams/
- **Key Insight**: Anagrams produce the same string when sorted. Use sorted string as hash key.
- **Time**: O(n × k log k) where k = max string length
- **Space**: O(n × k)
- **💡 Interview Tip**: Two key approaches — (1) sorted string as key, (2) character count tuple as key. Know both. The count tuple approach is O(n × k) time (no sorting).
- **🧠 Pattern Recognition**: "Group items by shared property" = hash map where key = canonical form.

### Functions
```python
def group_anagrams_sort(strs: List[str]) -> List[List[str]]:
    """
    Approach: Use sorted string as hash key.
    Hints:
    - from collections import defaultdict
    - groups = defaultdict(list)
    - For each word: key = tuple(sorted(word))
    - groups[key].append(word)
    - Return list(groups.values())
    
    Walk through:
        ["eat","tea","tan","ate","nat","bat"]
        sorted("eat") = "aet" → groups["aet"] = ["eat", "tea", "ate"]
        sorted("tan") = "ant" → groups["ant"] = ["tan", "nat"]
        sorted("bat") = "abt" → groups["abt"] = ["bat"]
    """
    pass

def group_anagrams_count(strs: List[str]) -> List[List[str]]:
    """
    Approach: Use character count tuple as key (avoids sorting).
    Hints:
    - For each word, create a count array of 26 zeros
    - Count each character: count[ord(c) - ord('a')] += 1
    - Use tuple(count) as dictionary key
    - Time: O(n × k) — better than sorting approach!
    """
    pass
```

### Test Cases
```python
# Note: order within groups and order of groups doesn't matter
# So test by converting to sets of frozensets
result = group_anagrams_sort(["eat","tea","tan","ate","nat","bat"])
result_sets = set(frozenset(group) for group in result)
expected = {frozenset(["bat"]), frozenset(["nat","tan"]), frozenset(["ate","eat","tea"])}
assert result_sets == expected

assert group_anagrams_sort([""]) == [[""]]                    # empty string
assert group_anagrams_sort(["a"]) == [["a"]]                  # single char
```

---

## Problem 15: Longest Substring Without Repeating Characters

- **File**: `15_longest_substring.py`
- **Difficulty**: Medium
- **Pattern**: 🪟 Sliding Window (variable size) + #️⃣ Hash Set/Map
- **LeetCode**: https://leetcode.com/problems/longest-substring-without-repeating-characters/
- **Key Insight**: Expand window right, shrink from left when duplicate found. Track chars in window with a set or map.
- **Time**: O(n²) → O(n) (brute → sliding window)
- **Space**: O(min(n, alphabet_size))
- **💡 Interview Tip**: This is THE classic sliding window problem. You must know this cold. The hash map variant (storing last index) is more optimal than hash set.
- **🧠 Pattern Recognition**: "Longest/shortest substring with constraint" = Sliding Window. Always.

### Functions
```python
def length_of_longest_substring_brute(s: str) -> int:
    """
    Approach: Check every substring.
    Hints:
    - For each start position, expand right until duplicate
    - Track max length seen
    - Time: O(n²), Space: O(n)
    """
    pass

def length_of_longest_substring(s: str) -> int:
    """
    Approach: Sliding window with hash set.
    Hints:
    - Maintain a window [left, right]
    - Use a set to track characters in current window
    - Expand right: add s[right] to set
    - If s[right] already in set → shrink from left until it's removed
    - Track max window size
    
    ADVANCED variant (hash map storing last index):
    - Map each char to its last seen index
    - When duplicate found: left = max(left, last_index[char] + 1)
    - This avoids the inner while loop — true O(n)
    
    Walk through (set approach):
        "abcabcbb"
        [a]bcabcbb → window="a", len=1
        a[b]cabcbb → window="ab", len=2
        ab[c]abcbb → window="abc", len=3
        abc[a]bcbb → 'a' in set! remove from left until 'a' gone
                      → window="bca", len=3
        ...max = 3
    """
    pass
```

### Test Cases
```python
assert length_of_longest_substring("abcabcbb") == 3
assert length_of_longest_substring("bbbbb") == 1
assert length_of_longest_substring("pwwkew") == 3
assert length_of_longest_substring("") == 0              # empty
assert length_of_longest_substring(" ") == 1             # space
assert length_of_longest_substring("au") == 2            # two unique
assert length_of_longest_substring("dvdf") == 3          # tricky case
assert length_of_longest_substring("abcdefg") == 7       # all unique
assert length_of_longest_substring("aab") == 2           # dup at start
```

---

## Problem 16: Valid Parentheses

- **File**: `16_valid_parentheses.py`
- **Difficulty**: Medium
- **Pattern**: 📚 Stack (matching pairs)
- **LeetCode**: https://leetcode.com/problems/valid-parentheses/
- **Key Insight**: Push opening brackets onto stack, pop when matching closing bracket found. Stack must be empty at end.
- **Time**: O(n)
- **Space**: O(n)
- **💡 Interview Tip**: This is technically a Stack problem, not purely arrays. But it's in your problem set and is a MUST-KNOW. The hash map for matching pairs makes the code clean.
- **🧠 Pattern Recognition**: "Matching/nesting" = Stack. Any time you need to match opening/closing or handle nesting, think Stack.

### Functions
```python
def is_valid(s: str) -> bool:
    """
    Approach: Stack with hash map for matching.
    Hints:
    - Create matching map: {')':'(', '}':'{', ']':'['}
    - Iterate through string:
      - If opening bracket → push to stack
      - If closing bracket → check if top of stack matches
        - If matches → pop
        - If not → return False
    - At end, stack must be empty
    - Edge: empty string → True
    
    Walk through:
        "([{}])"
        '(' → push → stack: ['(']
        '[' → push → stack: ['(', '[']
        '{' → push → stack: ['(', '[', '{']
        '}' → matches '{' → pop → stack: ['(', '[']
        ']' → matches '[' → pop → stack: ['(']
        ')' → matches '(' → pop → stack: []
        Stack empty → True ✓
    """
    pass
```

### Test Cases
```python
assert is_valid("()") == True
assert is_valid("()[]{}") == True
assert is_valid("(]") == False
assert is_valid("([)]") == False
assert is_valid("{[]}") == True
assert is_valid("") == True                   # empty
assert is_valid("(") == False                 # unclosed
assert is_valid(")") == False                 # no opener
assert is_valid("(((())))") == True           # deeply nested
assert is_valid("({[)]}") == False            # interleaved wrong
```

---

## Problem 17: Three Sum

- **File**: `17_three_sum.py`
- **Difficulty**: Medium
- **Pattern**: 🔀 Two Pointers (sort + fix one + two-pointer scan)
- **LeetCode**: https://leetcode.com/problems/3sum/
- **Key Insight**: Sort array. Fix one element, then use Two Sum II (two pointers) on the remaining. Skip duplicates carefully.
- **Time**: O(n³) → O(n²) (brute → sort + two pointers)
- **Space**: O(1) extra (excluding output)
- **💡 Interview Tip**: The duplicate-skipping logic is where most people mess up. After finding a triplet, skip all duplicate values for both left and right pointers. Also skip duplicate values for the fixed element.
- **🧠 Pattern Recognition**: "K-Sum" problems reduce to "sort + fix one + Two Sum". 4Sum = fix one + 3Sum. It's recursive.

### Functions
```python
def three_sum_brute(nums: List[int]) -> List[List[int]]:
    """
    Approach: Check all triplets.
    Hints:
    - Three nested loops: i, j, k
    - Check if nums[i] + nums[j] + nums[k] == 0
    - Use a set to avoid duplicate triplets
    - Time: O(n³)
    """
    pass

def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Approach: Sort + Fix one + Two pointers.
    Hints:
    - Sort the array first
    - For each i (fixed element):
      - Skip if nums[i] == nums[i-1] (avoid duplicate triplets)
      - If nums[i] > 0: break (can't sum to 0 with all positives)
      - Set left = i+1, right = len-1
      - Two pointer: if sum < 0 → left++, if sum > 0 → right--
      - If sum == 0 → found! Add to result, skip duplicates for left AND right
    
    Walk through:
        [-1, 0, 1, 2, -1, -4]
        Sorted: [-4, -1, -1, 0, 1, 2]
        
        i=0, nums[0]=-4: left=1, right=5
          -4 + (-1) + 2 = -3 < 0 → left++
          -4 + (-1) + 2 = -3 < 0 → left++
          ... no triplet sums to 0
        
        i=1, nums[1]=-1: left=2, right=5
          -1 + (-1) + 2 = 0 → FOUND [-1,-1,2]
          -1 + 0 + 1 = 0 → FOUND [-1,0,1]
        
        i=2, nums[2]=-1: skip (duplicate of i=1)
    """
    pass
```

### Test Cases
```python
result = three_sum([-1,0,1,2,-1,-4])
# Sort inner lists and outer list for comparison
result_sorted = sorted([sorted(x) for x in result])
assert result_sorted == [[-1,-1,2],[-1,0,1]]

assert three_sum([0,1,1]) == []                          # no solution
assert three_sum([0,0,0]) == [[0,0,0]]                   # all zeros
assert three_sum([]) == []                                # empty
assert three_sum([0]) == []                               # too short
assert three_sum([-1,0,1,0]) == [[-1,0,1]]               # duplicates in result
assert sorted([sorted(x) for x in three_sum([-2,0,1,1,2])]) == [[-2,0,2],[-2,1,1]]
```

---

## Problem 18: String to Integer (atoi)

- **File**: `18_string_to_integer.py`
- **Difficulty**: Medium
- **Pattern**: 🔧 Linear Scan with state management
- **LeetCode**: https://leetcode.com/problems/string-to-integer-atoi/
- **Key Insight**: Handle edge cases systematically: whitespace → sign → digits → overflow. Process in order.
- **Time**: O(n)
- **Space**: O(1)
- **💡 Interview Tip**: This is an edge-case-heavy problem. The algorithm is simple, but handling ALL edge cases correctly is the challenge. Process step by step: strip whitespace, handle sign, read digits, clamp to INT range.
- **🧠 Pattern Recognition**: "Parse/convert with rules" = step-by-step state machine.

### Functions
```python
def my_atoi(s: str) -> int:
    """
    Approach: Step-by-step parsing.
    Hints:
    - Step 1: Skip leading whitespace
    - Step 2: Check for sign (+/-), default to positive
    - Step 3: Read digits until non-digit or end
      - Build number: result = result * 10 + digit
    - Step 4: Clamp to 32-bit int range [-2^31, 2^31 - 1]
    - Use index pointer, don't use strip/split
    
    INT_MIN = -2**31  = -2147483648
    INT_MAX = 2**31-1 = 2147483647
    """
    pass
```

### Test Cases
```python
assert my_atoi("42") == 42
assert my_atoi("   -42") == -42
assert my_atoi("4193 with words") == 4193
assert my_atoi("") == 0                              # empty
assert my_atoi("   ") == 0                           # only spaces
assert my_atoi("words and 987") == 0                 # no leading digits
assert my_atoi("+1") == 1                            # explicit plus
assert my_atoi("+-12") == 0                          # double sign
assert my_atoi("-91283472332") == -2147483648         # underflow → clamp
assert my_atoi("91283472332") == 2147483647           # overflow → clamp
assert my_atoi("   +0 123") == 0                     # zero with trailing
```

---

## Problem 19: Container With Most Water

- **File**: `19_container_with_most_water.py`
- **Difficulty**: Medium
- **Pattern**: 🔀 Two Pointers (greedy converging)
- **LeetCode**: https://leetcode.com/problems/container-with-most-water/
- **Key Insight**: Start with widest container (left=0, right=end). Move the pointer with the SHORTER line inward — you can only improve by finding a taller line.
- **Time**: O(n²) → O(n) (brute → two pointers)
- **Space**: O(1)
- **💡 Interview Tip**: The WHY behind moving the shorter pointer is the key insight. Moving the taller pointer can NEVER increase area (width decreases, height bounded by shorter side). This greedy argument is what interviewers want to hear.
- **🧠 Pattern Recognition**: "Maximize area/value between two boundaries" = converging two pointers with greedy choice.

### Functions
```python
def max_area_brute(height: List[int]) -> int:
    """
    Approach: Check every pair of lines.
    Hints:
    - For each pair (i, j): area = min(height[i], height[j]) * (j - i)
    - Track maximum
    - Time: O(n²)
    """
    pass

def max_area(height: List[int]) -> int:
    """
    Approach: Two pointers — start wide, move shorter side inward.
    Hints:
    - left = 0, right = len - 1
    - area = min(height[left], height[right]) * (right - left)
    - If height[left] < height[right] → move left++
    - Else → move right--
    - Track maximum area
    
    WHY this works:
    - Width always decreases by 1
    - Only way to increase area is to find taller height
    - Moving the taller pointer can't help (limited by shorter side)
    - So always move the shorter pointer — greedy optimal
    
    Walk through:
        [1,8,6,2,5,4,8,3,7]
        l=0,r=8: area=min(1,7)*8=8, move left (1<7)
        l=1,r=8: area=min(8,7)*7=49, move right (7<8)
        l=1,r=7: area=min(8,3)*6=18, move right (3<8)
        ... max=49
    """
    pass
```

### Test Cases
```python
assert max_area([1,8,6,2,5,4,8,3,7]) == 49
assert max_area([1,1]) == 1                        # minimum case
assert max_area([4,3,2,1,4]) == 16                 # first and last
assert max_area([1,2,1]) == 2                      # small array
assert max_area([1,8,6,2,5,4,8,3,7]) == 49
assert max_area([2,3,4,5,18,17,6]) == 17           # tall in middle
```

---

## Problem 20: Rotate Array

- **File**: `20_rotate_array.py`
- **Difficulty**: Medium
- **Pattern**: 🔧 In-Place (reversal trick)
- **LeetCode**: https://leetcode.com/problems/rotate-array/
- **Key Insight**: Three reversals — reverse all, reverse first k, reverse rest. This rotates in-place with O(1) space.
- **Time**: O(n)
- **Space**: O(n) → O(1) (extra array → reversal trick)
- **💡 Interview Tip**: Know all three approaches. The reversal trick is elegant and uses O(1) space. The interviewer will likely ask you to optimize from O(n) space to O(1).
- **🧠 Pattern Recognition**: "Rotate/shift in-place" = reversal trick. Works for both arrays and parts of linked lists.

### Functions
```python
def rotate_extra_space(nums: List[int], k: int) -> None:
    """
    Approach: Use extra array.
    Hints:
    - k = k % len(nums)  (handle k > length)
    - New position of nums[i] = (i + k) % n
    - Copy back to original array
    - Time: O(n), Space: O(n)
    """
    pass

def rotate(nums: List[int], k: int) -> None:
    """
    Approach: Three reversals — O(1) space!
    Hints:
    - k = k % len(nums)  (handle k > length)
    - Step 1: Reverse entire array
    - Step 2: Reverse first k elements
    - Step 3: Reverse remaining n-k elements
    - Write a helper: reverse(nums, start, end)
    
    Walk through:
        [1,2,3,4,5,6,7], k=3
        Step 1: reverse all →  [7,6,5,4,3,2,1]
        Step 2: reverse [0:3] → [5,6,7,4,3,2,1]
        Step 3: reverse [3:7] → [5,6,7,1,2,3,4] ✓
    
    WHY this works:
    - Original: [1,2,3,4 | 5,6,7]  (split at n-k)
    - Want:     [5,6,7 | 1,2,3,4]  (swap the two halves)
    - Reverse all: both halves get reversed AND swapped
    - Reverse each half: un-reverses the elements within each half
    """
    pass
```

### Test Cases
```python
nums1 = [1,2,3,4,5,6,7]
rotate(nums1, 3)
assert nums1 == [5,6,7,1,2,3,4]

nums2 = [-1,-100,3,99]
rotate(nums2, 2)
assert nums2 == [3,99,-1,-100]

nums3 = [1,2,3]
rotate(nums3, 4)                              # k > length
assert nums3 == [3,1,2]                       # same as k=1

nums4 = [1]
rotate(nums4, 0)                              # k = 0
assert nums4 == [1]

nums5 = [1]
rotate(nums5, 1)                              # single element
assert nums5 == [1]

nums6 = [1,2]
rotate(nums6, 1)
assert nums6 == [2,1]                         # two elements
```
