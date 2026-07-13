# 🏹 Arrays & Strings — Pattern Cheatsheet

> Quick reference while solving problems. Identify the pattern FIRST, then code.

---

## Pattern 1: 🔀 Two Pointers

### When to Use
- Array is **sorted** (or can be sorted)
- Finding **pairs/triplets** with a target sum
- **Palindrome** checks
- **Merging** two sorted arrays
- **Partitioning** (move elements around)

### Template
```python
# Left-Right pointers (converging)
left, right = 0, len(arr) - 1
while left < right:
    # Process arr[left] and arr[right]
    if condition:
        left += 1
    else:
        right -= 1

# Fast-Slow pointers (same direction)
slow = fast = 0
while fast < len(arr):
    if condition:
        arr[slow] = arr[fast]
        slow += 1
    fast += 1
```

### Problems Using This
- Two Sum (sorted), 3Sum, Container With Most Water
- Valid Palindrome, Reverse String
- Remove Duplicates, Move Zeros, Merge Sorted Arrays

---

## Pattern 2: 🪟 Sliding Window

### When to Use
- Find **substring/subarray** with certain property
- Keywords: "contiguous", "longest", "shortest", "at most K"
- Need to track a **window** of elements

### Template
```python
# Variable-size window
left = 0
window = {}  # or set, or counter
result = 0

for right in range(len(s)):
    # Expand: add s[right] to window
    window[s[right]] = window.get(s[right], 0) + 1
    
    # Shrink: while window is invalid
    while window_is_invalid():
        # Remove s[left] from window
        window[s[left]] -= 1
        left += 1
    
    # Update result
    result = max(result, right - left + 1)
```

### Problems Using This
- Longest Substring Without Repeating Characters
- (More in Topic 03: Sliding Window)

---

## Pattern 3: #️⃣ Hash Map / Hash Set

### When to Use
- Need **O(1) lookup** — "have we seen this before?"
- **Counting frequencies** of elements
- **Grouping** elements by property
- Finding **complements** (target - current)

### Template
```python
# Frequency counting
from collections import Counter
freq = Counter(arr)  # or manually: freq = {}

# Complement finding (Two Sum pattern)
seen = {}
for i, num in enumerate(arr):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i

# Grouping
from collections import defaultdict
groups = defaultdict(list)
for item in items:
    key = get_key(item)  # e.g., sorted(item) for anagrams
    groups[key].append(item)
```

### Problems Using This
- Two Sum, Valid Anagram, Group Anagrams
- Contains Duplicate, First Unique Character

---

## Pattern 4: 📊 Prefix / Suffix

### When to Use
- Need **running sum/product** across array
- **Range queries** (sum from index i to j)
- Product of array except self
- Keywords: "cumulative", "running total"

### Template
```python
# Prefix sum
prefix = [0] * (len(arr) + 1)
for i in range(len(arr)):
    prefix[i + 1] = prefix[i] + arr[i]
# Sum from i to j = prefix[j+1] - prefix[i]

# Prefix + Suffix product (no division)
n = len(nums)
result = [1] * n
# Left pass
left_product = 1
for i in range(n):
    result[i] = left_product
    left_product *= nums[i]
# Right pass
right_product = 1
for i in range(n - 1, -1, -1):
    result[i] *= right_product
    right_product *= nums[i]
```

### Problems Using This
- Product of Array Except Self
- Subarray Sum Equals K (prefix sum + hash map combo)

---

## Pattern 5: 🔧 In-Place Manipulation

### When to Use
- Problem says **"O(1) extra space"** or **"in-place"**
- **Partitioning** elements (0s and 1s, move zeros)
- **Removing** elements from sorted array
- Array **rotation**

### Template
```python
# Write pointer pattern (for removals/compaction)
write = 0
for read in range(len(arr)):
    if should_keep(arr[read]):
        arr[write] = arr[read]
        write += 1
# arr[0:write] contains the result

# Reversal trick (for rotation)
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
```

### Problems Using This
- Remove Duplicates from Sorted Array
- Move Zeros, Rotate Array
- Dutch National Flag (3-way partition)

---

## 🎯 Pattern Recognition Decision Tree

```
Is the array sorted (or should it be)?
├── YES → Try TWO POINTERS
│         (Two Sum II, 3Sum, Container With Most Water)
└── NO
    ├── Need O(1) lookup or counting?
    │   └── YES → Use HASH MAP/SET
    │             (Two Sum, Anagram, Group Anagrams)
    ├── Need contiguous subarray/substring?
    │   └── YES → Try SLIDING WINDOW
    │             (Longest Substring, Min Window)
    ├── Need running aggregate (sum/product)?
    │   └── YES → Try PREFIX/SUFFIX
    │             (Product Except Self, Range Sum)
    └── Must modify in-place with O(1) space?
        └── YES → Use IN-PLACE MANIPULATION
                  (Move Zeros, Remove Dupes, Rotate)
```

---

## ⏱️ Complexity Cheat Sheet

| Operation | Time | Space |
|-----------|------|-------|
| Two Pointers (sorted) | O(n) | O(1) |
| Hash Map lookup | O(1) avg | O(n) |
| Sliding Window | O(n) | O(k) window |
| Prefix Sum build | O(n) | O(n) |
| Sorting | O(n log n) | O(n) |
| Brute force pairs | O(n²) | O(1) |

---

*"Parth, pehle pattern pehchano, phir code likho"* 🏹
