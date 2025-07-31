# Hash Tables - Study Notes

## Core Concept

Hash Tables (Hash Maps/Hash Sets) provide O(1) average-case lookup, insertion, and deletion by using a hash function to map keys to array indices. They're essential for solving problems that require fast lookups or frequency counting.

## Types of Hash Tables

### 1. Hash Map (Dictionary)

- **Key-Value pairs**: Store associations between keys and values
- **Python**: `dict` or `collections.defaultdict`
- **Use Cases**: Frequency counting, caching, lookups

```python
# Basic Hash Map operations
hash_map = {}
hash_map[key] = value    # Insert/Update - O(1)
value = hash_map[key]    # Access - O(1)
del hash_map[key]        # Delete - O(1)
key in hash_map          # Check existence - O(1)
```

### 2. Hash Set

- **Unique elements only**: No duplicates allowed
- **Python**: `set`
- **Use Cases**: Membership testing, removing duplicates

```python
# Basic Hash Set operations
hash_set = set()
hash_set.add(element)       # Insert - O(1)
hash_set.remove(element)    # Delete - O(1)
element in hash_set         # Check existence - O(1)
```

## Common Patterns

### Pattern 1: Frequency Counting

```python
from collections import Counter, defaultdict

# Method 1: Using Counter
freq = Counter(arr)

# Method 2: Using defaultdict
freq = defaultdict(int)
for element in arr:
    freq[element] += 1

# Method 3: Manual counting
freq = {}
for element in arr:
    freq[element] = freq.get(element, 0) + 1
```

### Pattern 2: Two Sum Pattern

```python
def two_sum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### Pattern 3: Grouping/Categorizing

```python
def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        # Use sorted string as key
        key = ''.join(sorted(s))
        groups[key].append(s)
    return list(groups.values())
```

### Pattern 4: Caching/Memoization

```python
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]
```

### Pattern 5: Set Operations

```python
def intersection(arr1, arr2):
    set1 = set(arr1)
    return [x for x in arr2 if x in set1]

def union(arr1, arr2):
    return list(set(arr1) | set(arr2))

def difference(arr1, arr2):
    return list(set(arr1) - set(arr2))
```

## When to Use Hash Tables

### Problem Indicators:

1. **"Find pairs/triplets that sum to X"**
2. **"Count frequency/occurrences"**
3. **"Check if X exists"**
4. **"Group similar elements"**
5. **"Remove duplicates"**
6. **"Anagram problems"**
7. **"Cache results"**

### Time Complexity Benefits:

- **Lookup**: O(n) → O(1)
- **Two Sum**: O(n²) → O(n)
- **Frequency Count**: Always O(n)
- **Duplicate Detection**: O(n log n) → O(n)

## Hash Functions and Keys

### Good Hash Keys:

```python
# Immutable types work as keys
string_key = "hello"
tuple_key = (1, 2, 3)
frozenset_key = frozenset([1, 2, 3])

# For custom objects
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
```

### Creative Key Strategies:

```python
# Sorted string for anagrams
key = ''.join(sorted(word))

# Tuple for coordinates
key = (row, col)

# Bitmask for subsets
key = sum(2**i for i in subset)

# String concatenation with delimiter
key = f"{val1}#{val2}"
```

## Advanced Techniques

### 1. Rolling Hash

```python
def rolling_hash(s, base=256, mod=10**9 + 7):
    hash_val = 0
    power = 1

    for char in s:
        hash_val = (hash_val + ord(char) * power) % mod
        power = (power * base) % mod

    return hash_val
```

### 2. Prefix Hash for Substrings

```python
def build_prefix_hash(s):
    n = len(s)
    prefix_hash = [0] * (n + 1)
    base, mod = 31, 10**9 + 7

    for i in range(n):
        prefix_hash[i + 1] = (prefix_hash[i] * base + ord(s[i])) % mod

    return prefix_hash
```

### 3. Multi-level Hashing

```python
# For 2D problems
hash_map = defaultdict(lambda: defaultdict(int))
hash_map[row][col] = value

# For nested grouping
groups = defaultdict(lambda: defaultdict(list))
groups[category][subcategory].append(item)
```

## Common Hash Table Problems

### 1. Array Problems:

- Two Sum, Three Sum
- Contains Duplicate
- Intersection of Arrays
- Majority Element

### 2. String Problems:

- Valid Anagram
- Group Anagrams
- Longest Substring Without Repeating Characters
- First Unique Character

### 3. Design Problems:

- LRU Cache
- Design HashMap
- Design HashSet

## Performance Considerations

### Time Complexity:

- **Average Case**: O(1) for all operations
- **Worst Case**: O(n) when many collisions occur
- **Amortized**: O(1) with good hash function

### Space Complexity:

- **Storage**: O(n) where n is number of elements
- **Load Factor**: Keep below 0.75 for good performance

### Hash Collisions:

```python
# Python handles collisions automatically
# But be aware of worst-case scenarios

# Bad: All elements hash to same value
# Good: Well-distributed hash values
```

## Best Practices

### 1. Choose Right Data Structure:

```python
# Counting → defaultdict(int) or Counter
# Grouping → defaultdict(list)
# Membership → set
# Key-Value → dict
```

### 2. Handle Missing Keys:

```python
# Method 1: get() with default
value = hash_map.get(key, default_value)

# Method 2: defaultdict
from collections import defaultdict
hash_map = defaultdict(int)  # Returns 0 for missing keys

# Method 3: setdefault
hash_map.setdefault(key, []).append(value)
```

### 3. Efficient Iteration:

```python
# Iterate over items (most common)
for key, value in hash_map.items():
    process(key, value)

# Iterate over keys only
for key in hash_map:
    process(key)

# Iterate over values only
for value in hash_map.values():
    process(value)
```

## Common Mistakes to Avoid

1. **Using mutable objects as keys**: Lists, sets can't be keys
2. **Not handling missing keys**: Use .get() or defaultdict
3. **Modifying dict while iterating**: Create copy first
4. **Forgetting about hash collisions**: Rare but possible
5. **Not considering memory usage**: Hash tables use extra space

## Templates

### Basic Frequency Count Template:

```python
def solve_with_frequency(arr):
    freq = defaultdict(int)
    for element in arr:
        freq[element] += 1

    # Process frequencies
    for element, count in freq.items():
        if condition_met(count):
            return element
```

### Two Sum Template:

```python
def two_sum_pattern(arr, target):
    seen = {}
    for i, val in enumerate(arr):
        complement = target - val
        if complement in seen:
            return [seen[complement], i]
        seen[val] = i
    return []
```

### Grouping Template:

```python
def group_by_property(items):
    groups = defaultdict(list)
    for item in items:
        key = extract_property(item)
        groups[key].append(item)
    return dict(groups)
```
