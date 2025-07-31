# Arrays and Strings - Study Notes

## Core Concepts

### Arrays

- **Definition**: Contiguous memory locations storing elements of the same data type
- **Time Complexity**:
  - Access: O(1)
  - Search: O(n)
  - Insertion: O(n) worst case, O(1) at end
  - Deletion: O(n) worst case, O(1) at end

### Strings

- **Definition**: Sequence of characters (array of characters)
- **Immutability**: In Python, strings are immutable
- **Common Operations**: Concatenation, substring, comparison

## Key Patterns and Techniques

### 1. Index Manipulation

```python
# Reverse iteration
for i in range(len(arr) - 1, -1, -1):
    print(arr[i])

# Skip elements
for i in range(0, len(arr), 2):  # Every 2nd element
    print(arr[i])
```

### 2. In-place Modifications

- Minimize space complexity by modifying the original array
- Use two pointers for swapping elements

### 3. Frequency Counting

```python
from collections import Counter
freq = Counter(arr)  # Quick frequency count
```

### 4. Prefix and Suffix Arrays

- Build cumulative information for range queries
- Useful for sum, product, or other associative operations

## String-Specific Techniques

### 1. Character Mapping

```python
# ASCII values
ord('a')  # 97
chr(97)   # 'a'

# Case conversion
s.lower(), s.upper(), s.title()
```

### 2. String Building

```python
# Efficient string building
result = []
result.append(char)
return ''.join(result)  # O(n) vs O(n²) concatenation
```

### 3. Palindrome Checking

```python
def is_palindrome(s):
    return s == s[::-1]  # Simple approach

# Optimized with two pointers
def is_palindrome_optimized(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

## Common Edge Cases to Consider

1. **Empty arrays/strings**: `[]` or `""`
2. **Single element**: `[1]` or `"a"`
3. **All same elements**: `[1,1,1,1]`
4. **Already sorted/reverse sorted**: `[1,2,3,4]` or `[4,3,2,1]`
5. **Negative numbers**: `[-1, -2, 0, 1]`
6. **Special characters in strings**: Spaces, punctuation, Unicode

## Time and Space Complexity Guidelines

- **Linear Scan**: O(n) time, O(1) space
- **Nested Loops**: O(n²) time - try to optimize
- **Sorting**: O(n log n) time
- **Hash Map Usage**: O(n) space for O(1) lookups

## Problem-Solving Framework

1. **Understand**: Read problem twice, identify input/output
2. **Plan**: Choose appropriate technique (brute force → optimize)
3. **Implement**: Write clean, readable code
4. **Test**: Check edge cases and examples
5. **Optimize**: Analyze time/space complexity

## Quick Reference - Python String Methods

```python
s.strip()           # Remove whitespace
s.split()           # Split by whitespace
s.replace(old, new) # Replace substring
s.find(substring)   # Find index (-1 if not found)
s.count(char)       # Count occurrences
s.isalnum()         # Check alphanumeric
s.isdigit()         # Check if all digits
```

## Quick Reference - Python List Methods

```python
arr.append(x)       # Add to end
arr.insert(i, x)    # Insert at index
arr.pop()           # Remove last element
arr.remove(x)       # Remove first occurrence
arr.reverse()       # Reverse in-place
arr.sort()          # Sort in-place
```

## Mental Models

- **Array as a window**: Use for sliding window problems
- **String as a sequence**: Think character by character
- **Frequency as a histogram**: Visualize character/element counts
- **Palindrome as a mirror**: Center expansion or two pointers
