# Sliding Window - Study Notes

## Core Concept

Sliding Window is a technique used to solve array/string problems by maintaining a "window" of elements and sliding it across the data structure. This reduces time complexity from O(n²) to O(n) for many subarray/substring problems.

## Types of Sliding Window

### 1. Fixed Size Window

- **Window size remains constant**
- **Movement**: Slide one position at a time
- **Use Cases**: Maximum sum of k elements, average of subarrays

```python
def fixed_window(arr, k):
    if len(arr) < k:
        return []

    # Calculate first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

### 2. Variable Size Window

- **Window size changes based on conditions**
- **Movement**: Expand right, contract left as needed
- **Use Cases**: Longest substring with k distinct chars, minimum window substring

```python
def variable_window(arr, condition):
    left = 0
    result = 0

    for right in range(len(arr)):
        # Expand window by including arr[right]

        # Contract window while condition is violated
        while condition_violated:
            # Remove arr[left] from window
            left += 1

        # Update result with current valid window
        result = max(result, right - left + 1)

    return result
```

## Common Patterns

### Pattern 1: Maximum/Minimum in Fixed Window

```python
def max_sum_subarray(arr, k):
    max_sum = float('-inf')
    window_sum = 0

    for i in range(len(arr)):
        window_sum += arr[i]

        if i >= k - 1:  # Window is of size k
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[i - k + 1]  # Remove leftmost element

    return max_sum
```

### Pattern 2: Longest Substring with Condition

```python
def longest_substring_k_distinct(s, k):
    if k == 0:
        return 0

    char_count = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Expand window
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        # Contract window if condition violated
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length
```

### Pattern 3: Minimum Window with Condition

```python
def minimum_window_substring(s, t):
    if not s or not t:
        return ""

    dict_t = {}
    for char in t:
        dict_t[char] = dict_t.get(char, 0) + 1

    required = len(dict_t)
    left = right = 0
    formed = 0
    window_counts = {}
    ans = float("inf"), None, None

    while right < len(s):
        # Expand window
        character = s[right]
        window_counts[character] = window_counts.get(character, 0) + 1

        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        # Contract window
        while left <= right and formed == required:
            character = s[left]

            # Update answer if current window is smaller
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)

            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

            left += 1

        right += 1

    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
```

## When to Use Sliding Window

### Problem Indicators:

1. **Subarray/substring problems**
2. **"Contiguous" mentioned in problem**
3. **Fixed or variable size requirements**
4. **Optimization problems** (max/min/longest/shortest)
5. **"All subarrays of size k"**

### Common Problem Types:

- Maximum sum of k elements
- Longest substring with k distinct characters
- Minimum window containing all characters
- Average of all subarrays of size k
- Count of subarrays with given condition

## Key Techniques

### 1. Two Pointers for Window Boundaries

```python
left = 0
for right in range(len(arr)):
    # Process arr[right] (expand window)

    while window_invalid:
        # Process arr[left] (contract window)
        left += 1

    # Current window: [left, right]
```

### 2. Hash Map for Character/Element Counting

```python
from collections import defaultdict

char_count = defaultdict(int)
for char in window:
    char_count[char] += 1
```

### 3. Deque for Min/Max in Window

```python
from collections import deque

def sliding_window_maximum(nums, k):
    dq = deque()  # Store indices
    result = []

    for i in range(len(nums)):
        # Remove elements outside window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove smaller elements (not useful)
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
```

## Common Mistakes to Avoid

1. **Not updating window state correctly**: Remember to add/remove elements
2. **Off-by-one errors**: Be careful with window size calculations
3. **Forgetting edge cases**: Empty arrays, k > array length
4. **Inefficient window updates**: Use proper data structures
5. **Not handling duplicates**: Consider how duplicates affect counting

## Templates

### Fixed Size Window Template

```python
def fixed_size_window(arr, k):
    if len(arr) < k:
        return None

    # Initialize first window
    window_property = calculate_initial_window(arr[:k])
    result = window_property

    # Slide the window
    for i in range(k, len(arr)):
        # Remove leftmost element
        remove_element(arr[i-k])
        # Add rightmost element
        add_element(arr[i])
        # Update result
        result = update_result(window_property)

    return result
```

### Variable Size Window Template

```python
def variable_size_window(arr):
    left = 0
    result = 0
    window_state = initialize_state()

    for right in range(len(arr)):
        # Expand window
        add_to_window(arr[right])

        # Contract window while invalid
        while is_window_invalid():
            remove_from_window(arr[left])
            left += 1

        # Update result
        result = max(result, right - left + 1)

    return result
```

## Time and Space Complexity

- **Time**: O(n) where n is the length of input
- **Space**: O(k) where k is window size or number of distinct elements
- **Key insight**: Each element is added and removed at most once

## Optimization Tips

1. **Use appropriate data structures**: Hash maps for counting, deques for min/max
2. **Early termination**: Stop when no better solution possible
3. **Preprocessing**: Sometimes sorting or other preprocessing helps
4. **Multiple passes**: Rare, but sometimes needed for complex conditions

## Practice Strategy

1. **Start with fixed-size problems**: Easier to visualize
2. **Master the expansion-contraction pattern**: Core of variable windows
3. **Practice with different data types**: Strings, integers, etc.
4. **Focus on state management**: What to track in the window
5. **Handle edge cases**: Empty input, single elements
