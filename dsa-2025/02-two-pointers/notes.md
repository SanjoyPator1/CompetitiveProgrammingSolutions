# Two Pointers - Study Notes

## Core Concept

Two pointers is a technique where we use two pointers (indices) to traverse data structures, typically arrays or strings. This approach often reduces time complexity from O(n²) to O(n).

## Types of Two Pointers

### 1. Opposite Direction (Left-Right Pointers)

- **Start**: One pointer at beginning, one at end
- **Movement**: Move pointers toward each other
- **Use Cases**: Palindromes, pair finding, reversing

```python
def two_pointers_opposite(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # Process arr[left] and arr[right]
        left += 1
        right -= 1
```

### 2. Same Direction (Fast-Slow Pointers)

- **Start**: Both pointers at beginning (or specific positions)
- **Movement**: One moves faster than the other
- **Use Cases**: Cycle detection, finding middle, removing elements

```python
def two_pointers_same_direction(arr):
    slow = fast = 0
    while fast < len(arr):
        # Process logic
        slow += 1
        fast += 2  # or some other increment
```

### 3. Sliding Window Variation

- **Start**: Both pointers at beginning
- **Movement**: Expand/contract window based on conditions
- **Use Cases**: Subarray problems, variable window sizes

## Common Patterns

### Pattern 1: Target Sum Problems

Finding pairs that sum to a target value in sorted arrays.

```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
```

### Pattern 2: Palindrome Verification

```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

### Pattern 3: Remove/Replace Elements

```python
def remove_element(arr, val):
    write_index = 0
    for read_index in range(len(arr)):
        if arr[read_index] != val:
            arr[write_index] = arr[read_index]
            write_index += 1
    return write_index
```

### Pattern 4: Cycle Detection (Floyd's Algorithm)

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

## When to Use Two Pointers

### Indicators:

1. **Sorted array/string** - Often a hint for opposite direction pointers
2. **Finding pairs/triplets** - Classic two pointer scenario
3. **Palindrome checking** - Natural fit for opposite direction
4. **In-place modifications** - Use read/write pointers
5. **Cycle detection** - Fast-slow pointer technique
6. **Reversing** - Swap elements from ends

### Problem Types:

- Target sum problems
- Palindrome problems
- Array reversal
- Removing duplicates
- Container problems
- Linked list cycles
- Merge operations

## Advantages

1. **Time Efficiency**: Often reduces O(n²) to O(n)
2. **Space Efficiency**: Usually O(1) extra space
3. **Intuitive**: Easy to understand and implement
4. **Versatile**: Works on arrays, strings, linked lists

## Common Mistakes to Avoid

1. **Incorrect boundary conditions**: Always check `left < right`
2. **Infinite loops**: Ensure pointers move in each iteration
3. **Off-by-one errors**: Be careful with indices
4. **Unsorted data**: Many techniques require sorted data
5. **Not handling duplicates**: Consider how duplicates affect logic

## Template Code

### Basic Opposite Direction Template

```python
def solve_opposite_direction(arr):
    left, right = 0, len(arr) - 1
    result = []

    while left < right:
        # Calculate or compare current elements
        if condition_met:
            # Record result
            result.append([arr[left], arr[right]])
            left += 1
            right -= 1
        elif need_larger_sum:
            left += 1
        else:
            right -= 1

    return result
```

### Basic Same Direction Template

```python
def solve_same_direction(arr):
    slow = 0

    for fast in range(len(arr)):
        if condition_met:
            arr[slow] = arr[fast]
            slow += 1

    return slow  # or arr[:slow]
```

## Time and Space Complexity

- **Time**: Usually O(n) where n is the length of input
- **Space**: Usually O(1) as we only use constant extra space
- **Exception**: If we need to store results, space becomes O(k) where k is result size

## Practice Strategy

1. **Start with sorted arrays**: Easier to visualize
2. **Master the basic patterns**: Target sum, palindrome, removal
3. **Practice boundary conditions**: Empty arrays, single elements
4. **Expand to unsorted data**: When sorting is beneficial
5. **Apply to linked lists**: Different but similar concepts

## Common Variations

1. **Three pointers**: For problems like 3Sum
2. **Multiple passes**: Sometimes need more than one two-pointer pass
3. **Modified conditions**: Custom logic for pointer movement
4. **Preprocessing**: Sort first, then apply two pointers
