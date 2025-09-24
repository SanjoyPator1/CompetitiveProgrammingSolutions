# Hash Tables - Comprehensive Study Notes with Detailed Explanations

## Table of Contents

1. [Core Concept & Philosophy](#core-concept--philosophy)
2. [Types of Hash Table Problems](#types-of-hash-table-problems)
3. [Pattern Deep Dive](#pattern-deep-dive)
4. [Advanced Techniques](#advanced-techniques)
5. [Problem Recognition Guide](#problem-recognition-guide)
6. [Implementation Templates](#implementation-templates)
7. [Complexity Analysis](#complexity-analysis)
8. [Common Pitfalls & How to Avoid Them](#common-pitfalls--how-to-avoid-them)
9. [Practice Framework](#practice-framework)

## Core Concept & Philosophy

### What are Hash Tables?

Hash tables (also called hash maps, dictionaries, or associative arrays) are **data structures that provide extremely fast lookups, insertions, and deletions** by using a hash function to map keys to array indices. They're the backbone of many efficient algorithms and are essential for solving a wide variety of programming problems.

### The Big Idea

**Think of it like this**: Imagine a massive library where instead of browsing through thousands of books to find the one you want, you have a magical catalog system. You tell the system the book's title (key), and it instantly tells you the exact shelf location (index) where that book is stored. Hash tables work similarly - they use a mathematical function to convert keys into array positions for instant access.

### Core Principles

1. **Instant Access**: O(1) average-case lookup, insertion, and deletion
2. **Key-Value Mapping**: Store associations between keys and values
3. **Hash Function**: Convert keys to array indices deterministically
4. **Collision Handling**: Deal with different keys mapping to same index
5. **Memory-Time Tradeoff**: Use extra space to achieve faster operations

### When Hash Tables Shine

- **Fast Lookups**: When you need to check if something exists quickly
- **Counting/Frequency**: Tracking how often items appear
- **Caching/Memoization**: Storing computed results for reuse
- **Grouping**: Organizing data by categories or properties
- **Set Operations**: Union, intersection, difference of collections
- **Index Mapping**: Creating efficient mappings between different data representations

## Types of Hash Table Problems

### 1. Frequency Counting & Statistics

**Philosophy**: Use hash tables to count occurrences of elements, characters, or patterns.

**When to use**: Any time you see words like "count", "frequency", "most common", "least common", or "appears exactly k times".

**How it works**:

- Iterate through the data once
- For each element, increment its count in the hash table
- Use the final counts for analysis or comparison

**Real-world analogy**: Think of a cashier counting different types of items in a shopping cart. Each item type goes into a different mental bucket with a running tally.

```python
def frequency_counting_template(data):
    """
    Template for frequency counting problems.

    Example: Count character frequencies in a string
    """
    frequency = {}

    # Count frequencies
    for item in data:
        frequency[item] = frequency.get(item, 0) + 1

    # Use frequencies for analysis
    return process_frequencies(frequency)
```

**Use Cases**:

- Character frequency in strings
- Element frequency in arrays
- Word frequency in documents
- Pattern frequency in sequences

**Mental Model**: Think of it as **digital tallying** - each hash table entry is a tally counter.

### 2. Fast Lookups & Existence Checks

**Philosophy**: Use hash tables as ultra-fast "membership tests" to check if elements exist.

**When to use**: When you need to repeatedly check if elements exist in a collection, especially when the collection is large or the checks are frequent.

**How it works**:

- Store all elements you need to check against in a hash set
- For each query, check membership in O(1) time
- Much faster than linear search through lists

**Real-world analogy**: Think of a VIP list at an exclusive event. Instead of checking a long paper list every time someone arrives, the bouncer has all VIP names memorized for instant recognition.

```python
def fast_lookup_template(search_space, queries):
    """
    Template for fast existence checking.

    Example: Check which numbers exist in both arrays
    """
    # Create hash set for O(1) lookups
    lookup_set = set(search_space)

    results = []
    for query in queries:
        if query in lookup_set:
            results.append(query)

    return results
```

**Use Cases**:

- Two Sum problems
- Finding duplicates
- Set intersections
- Membership validation

**Mental Model**: Think of it as a **digital phonebook** - instant name-to-information lookup.

### 3. Grouping & Categorization

**Philosophy**: Use hash tables to organize data into categories or groups based on shared properties.

**When to use**: When you need to group elements that share common characteristics, patterns, or computed properties.

**How it works**:

- Define a grouping key (could be the element itself or a computed property)
- For each element, calculate its grouping key
- Add the element to the appropriate group in the hash table

**Real-world analogy**: Think of sorting mail by ZIP code. Each ZIP code is a key, and all mail with that ZIP code goes into the same group.

```python
def grouping_template(data, key_function):
    """
    Template for grouping problems.

    Example: Group words by their sorted characters (anagrams)
    """
    groups = {}

    for item in data:
        # Calculate grouping key
        key = key_function(item)

        # Add item to appropriate group
        if key not in groups:
            groups[key] = []
        groups[key].append(item)

    return groups
```

**Use Cases**:

- Group anagrams
- Group numbers by digit sum
- Group strings by length
- Group objects by properties

**Mental Model**: Think of it as **automatic filing system** - items automatically go to the right folder.

### 4. Caching & Memoization

**Philosophy**: Store computed results to avoid expensive recalculations.

**When to use**: When you have expensive computations that might be repeated with the same inputs, especially in recursive algorithms or repeated queries.

**How it works**:

- Before computing something, check if result is already cached
- If cached, return the stored result immediately
- If not cached, compute result and store it for future use

**Real-world analogy**: Think of a student keeping notes for different subjects. Instead of re-reading entire textbooks for each test, they refer to their organized notes for quick review.

```python
def memoization_template():
    """
    Template for caching/memoization problems.

    Example: Fibonacci with memoization
    """
    cache = {}

    def expensive_computation(n):
        # Check cache first
        if n in cache:
            return cache[n]

        # Compute result
        if n <= 1:
            result = n
        else:
            result = expensive_computation(n-1) + expensive_computation(n-2)

        # Store in cache
        cache[n] = result
        return result

    return expensive_computation
```

**Use Cases**:

- Dynamic programming optimization
- API response caching
- Complex calculation storage
- Recursive function optimization

**Mental Model**: Think of it as a **smart calculator** that remembers previous calculations.

## Pattern Deep Dive

### Pattern 1: Two Sum Family

This is the **most fundamental** hash table pattern and appears in countless variations.

#### Basic Two Sum

**Problem Setup**: Given an array of integers and a target sum, find two numbers that add up to the target.

**Key Insight**: Instead of checking every pair (O(n²)), we can use a hash table to store numbers we've seen and check if the "complement" (target - current_number) exists.

**Step-by-step breakdown**:

1. Create an empty hash table to store number → index mappings
2. For each number in the array:
   - Calculate complement = target - current_number
   - If complement exists in hash table, we found our pair!
   - Otherwise, store current_number → current_index in hash table
3. Continue until pair is found or array is exhausted

```python
def two_sum(nums, target):
    """
    Find two numbers that add up to target.

    Example walkthrough: nums = [2, 7, 11, 15], target = 9

    i=0, num=2: complement = 9-2 = 7
        7 not in seen_map, so seen_map[2] = 0
        seen_map = {2: 0}

    i=1, num=7: complement = 9-7 = 2
        2 IS in seen_map at index 0!
        Found pair: indices 0 and 1

    Result: [0, 1]
    Time: O(n), Space: O(n)
    """
    seen_map = {}  # number -> index

    for i, num in enumerate(nums):
        complement = target - num

        print(f"i={i}, num={num}, complement={complement}")
        print(f"seen_map before: {seen_map}")

        if complement in seen_map:
            print(f"Found pair! {complement} at index {seen_map[complement]}, {num} at index {i}")
            return [seen_map[complement], i]

        seen_map[num] = i
        print(f"seen_map after: {seen_map}")
        print()

    return []  # No solution found
```

**Why hash table is perfect here**: We need fast lookups to check if complement exists. Hash table gives us O(1) average lookup time, making the entire algorithm O(n) instead of O(n²).

#### Three Sum

**Problem Setup**: Find all unique triplets in an array that sum to zero.

**Key Strategy**: This combines hash tables with other techniques. We can fix one number and use Two Sum approach for the remaining two, or use hash tables differently for optimization.

**Hash table approach** (alternative to two pointers):

```python
def three_sum_hash(nums):
    """
    Find all unique triplets that sum to zero using hash tables.

    Strategy: For each pair (i,j), check if -(nums[i]+nums[j]) exists later in array
    """
    nums.sort()  # Sort for easier duplicate handling
    result = []
    n = len(nums)

    for i in range(n - 2):
        # Skip duplicates for first element
        if i > 0 and nums[i] == nums[i-1]:
            continue

        seen = set()
        for j in range(i + 1, n):
            complement = -(nums[i] + nums[j])

            if complement in seen:
                triplet = [nums[i], complement, nums[j]]
                result.append(triplet)

                # Skip duplicates for second element
                while j + 1 < n and nums[j] == nums[j + 1]:
                    j += 1

            seen.add(nums[j])

    return result
```

**Comparison with Two Pointers**: Hash table approach is conceptually simpler but uses O(n) extra space. Two pointers approach uses O(1) space but requires sorted array.

### Pattern 2: Character/String Analysis

#### Valid Anagram

**Problem Setup**: Check if two strings are anagrams (contain same characters with same frequencies).

**Key Insight**: Two strings are anagrams if and only if they have identical character frequency distributions.

**Strategy Options**:

1. **Count and Compare**: Count frequencies in both strings and compare
2. **Count and Decrement**: Count first string, then decrement with second string
3. **Sorting**: Sort both strings and compare (alternative approach)

```python
def is_anagram_detailed(s, t):
    """
    Check if two strings are anagrams using frequency counting.

    Example: s = "listen", t = "silent"

    s frequency: {'l':1, 'i':1, 's':1, 't':1, 'e':1, 'n':1}
    t frequency: {'s':1, 'i':1, 'l':1, 'e':1, 'n':1, 't':1}

    Frequencies match → True (anagram)

    Time: O(n), Space: O(1) for English alphabet
    """
    if len(s) != len(t):
        return False

    # Method 1: Count both and compare
    from collections import Counter
    return Counter(s) == Counter(t)

    # Method 2: Manual counting (more educational)
    char_count = {}

    # Count characters in s
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Decrement with characters in t
    for char in t:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]

    # If all counts cancelled out, it's an anagram
    return len(char_count) == 0
```

#### Group Anagrams

**Problem Setup**: Group strings that are anagrams of each other.

**Key Strategy**: Use a canonical representation of each string as the grouping key. Two anagrams will have the same canonical form.

**Canonical Forms**:

1. **Sorted string**: "eat" → "aet", "tea" → "aet", "ate" → "aet"
2. **Character frequency signature**: "eat" → "1a1e1t"
3. **Prime number encoding**: Each character maps to a prime, multiply them

```python
def group_anagrams(strs):
    """
    Group strings that are anagrams of each other.

    Example: ["eat","tea","tan","ate","nat","bat"]

    Groups formed:
    - "aet" (sorted): ["eat", "tea", "ate"]
    - "ant" (sorted): ["tan", "nat"]
    - "abt" (sorted): ["bat"]

    Result: [["eat","tea","ate"],["tan","nat"],["bat"]]
    Time: O(n*k*log(k)) where k is max string length
    Space: O(n*k)
    """
    from collections import defaultdict

    groups = defaultdict(list)

    for string in strs:
        # Use sorted string as canonical key
        canonical = ''.join(sorted(string))
        groups[canonical].append(string)

        print(f"'{string}' → canonical: '{canonical}'")
        print(f"Current groups: {dict(groups)}")
        print()

    return list(groups.values())

def group_anagrams_frequency(strs):
    """
    Alternative: Use frequency signature as key (more efficient for long strings)
    """
    from collections import defaultdict

    def get_signature(s):
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        return tuple(count)  # Tuple is hashable, list is not

    groups = defaultdict(list)
    for string in strs:
        signature = get_signature(string)
        groups[signature].append(string)

    return list(groups.values())
```

### Pattern 3: Array/Number Analysis

#### Contains Duplicate

**Problem Setup**: Check if an array contains any duplicate values.

**Key Insight**: Use a hash set to track seen elements. If we encounter an element we've already seen, we have a duplicate.

```python
def contains_duplicate(nums):
    """
    Check if array contains duplicates.

    Example: [1,2,3,1]

    i=0, num=1: seen = {}, 1 not in seen, add 1 → seen = {1}
    i=1, num=2: 2 not in seen, add 2 → seen = {1,2}
    i=2, num=3: 3 not in seen, add 3 → seen = {1,2,3}
    i=3, num=1: 1 IS in seen → duplicate found!

    Result: True
    Time: O(n), Space: O(n)
    """
    seen = set()

    for num in nums:
        print(f"Checking {num}, seen so far: {seen}")

        if num in seen:
            print(f"Duplicate found: {num}")
            return True

        seen.add(num)

    print("No duplicates found")
    return False

# Alternative: Use set length comparison
def contains_duplicate_concise(nums):
    """One-liner using set properties"""
    return len(nums) != len(set(nums))
```

#### Contains Duplicate II

**Problem Setup**: Check if array contains duplicates within k distance of each other.

**Key Enhancement**: We need to track not just if we've seen an element, but WHERE we've seen it (index).

```python
def contains_nearby_duplicate(nums, k):
    """
    Check if duplicates exist within k distance.

    Example: nums = [1,2,3,1], k = 3

    i=0, num=1: index_map = {}, store 1→0, index_map = {1:0}
    i=1, num=2: store 2→1, index_map = {1:0, 2:1}
    i=2, num=3: store 3→2, index_map = {1:0, 2:1, 3:2}
    i=3, num=1: 1 seen at index 0, distance = 3-0 = 3 ≤ k=3 → True!

    Time: O(n), Space: O(min(n,k))
    """
    index_map = {}  # number -> most recent index

    for i, num in enumerate(nums):
        print(f"i={i}, num={num}, index_map={index_map}")

        if num in index_map:
            distance = i - index_map[num]
            print(f"Found {num} at previous index {index_map[num]}, distance={distance}")

            if distance <= k:
                print(f"Distance {distance} ≤ k={k}, duplicate within range!")
                return True

        index_map[num] = i
        print(f"Updated index_map: {index_map}")
        print()

    return False
```

#### First Unique Character

**Problem Setup**: Find the first character that appears exactly once in a string.

**Key Strategy**: Two-pass approach - first pass counts frequencies, second pass finds first character with frequency 1.

```python
def first_unique_character(s):
    """
    Find index of first unique character.

    Example: s = "leetcode"

    Pass 1 - Count frequencies:
    'l':1, 'e':3, 't':1, 'c':1, 'o':1, 'd':1

    Pass 2 - Find first unique:
    s[0]='l': freq=1 → unique! Return index 0

    Time: O(n), Space: O(1) for English alphabet
    """
    from collections import Counter

    # Pass 1: Count character frequencies
    char_count = Counter(s)
    print(f"Character frequencies: {dict(char_count)}")

    # Pass 2: Find first character with frequency 1
    for i, char in enumerate(s):
        if char_count[char] == 1:
            print(f"First unique character: '{char}' at index {i}")
            return i

    print("No unique character found")
    return -1

# Alternative: Single pass with OrderedDict (maintains insertion order)
def first_unique_character_ordered(s):
    """Single pass using OrderedDict to maintain order"""
    from collections import OrderedDict

    char_count = OrderedDict()

    # Count frequencies while maintaining order
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find first character with count 1
    for char, count in char_count.items():
        if count == 1:
            return s.index(char)

    return -1
```

### Pattern 4: Intersection and Union

#### Intersection of Two Arrays

**Problem Setup**: Find common elements between two arrays.

**Strategy Comparison**:

1. **Hash Set**: Convert one array to set, check membership for other
2. **Two Hash Sets**: Convert both to sets, use set intersection
3. **Hash Map**: Count frequencies in one, decrement with other

```python
def intersection_two_arrays(nums1, nums2):
    """
    Find intersection of two arrays (unique elements).

    Example: nums1 = [1,2,2,1], nums2 = [2,2]

    Method 1: Hash set approach
    set1 = {1, 2}
    Check nums2: 2 in set1 ✓, 2 in set1 ✓
    Intersection = {2}

    Result: [2]
    Time: O(n+m), Space: O(min(n,m))
    """
    # Method 1: Convert smaller array to set for efficiency
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    set1 = set(nums1)
    intersection = set()

    for num in nums2:
        if num in set1:
            intersection.add(num)

    return list(intersection)

def intersection_with_duplicates(nums1, nums2):
    """
    Find intersection preserving duplicates (as many as appear in both).

    Example: nums1 = [1,2,2,1], nums2 = [2,2]

    Count nums1: {1:2, 2:2}
    Process nums2:
        - 2: min(count[2], freq in nums2) = min(2,2) = 2
    Result: [2,2]
    """
    from collections import Counter

    count1 = Counter(nums1)
    result = []

    for num in nums2:
        if count1[num] > 0:
            result.append(num)
            count1[num] -= 1

    return result
```

## Advanced Techniques

### 1. Rolling Hash for String Matching

**Problem**: Find all occurrences of pattern P in text T efficiently.

**Key Idea**: Use polynomial rolling hash to compute hash values for all substrings of length |P| in O(1) time each.

```python
def rolling_hash_search(text, pattern):
    """
    Find all occurrences of pattern in text using rolling hash.

    Rolling hash formula: hash = (c1*p^(n-1) + c2*p^(n-2) + ... + cn) mod m

    To roll: remove leftmost char, shift, add rightmost char
    new_hash = (old_hash - left_char*p^(n-1)) * p + right_char

    Time: O(n+m) average, O(nm) worst case
    Space: O(1)
    """
    if len(pattern) > len(text):
        return []

    # Hash parameters
    BASE = 256  # Number of characters in alphabet
    MOD = 10**9 + 7  # Large prime for modular arithmetic

    pattern_len = len(pattern)
    text_len = len(text)

    # Precompute BASE^(pattern_len-1) % MOD
    h = pow(BASE, pattern_len - 1, MOD)

    # Calculate hash of pattern and first window of text
    pattern_hash = 0
    text_hash = 0

    for i in range(pattern_len):
        pattern_hash = (pattern_hash * BASE + ord(pattern[i])) % MOD
        text_hash = (text_hash * BASE + ord(text[i])) % MOD

    result = []

    # Check all windows
    for i in range(text_len - pattern_len + 1):
        # If hashes match, verify with actual string comparison
        if pattern_hash == text_hash:
            if text[i:i+pattern_len] == pattern:
                result.append(i)

        # Calculate hash for next window (if not last window)
        if i < text_len - pattern_len:
            # Remove leftmost character and add rightmost character
            text_hash = (text_hash - ord(text[i]) * h) % MOD
            text_hash = (text_hash * BASE + ord(text[i + pattern_len])) % MOD
            text_hash = (text_hash + MOD) % MOD  # Ensure positive

    return result
```

### 2. Consistent Hashing for Distributed Systems

**Problem**: Distribute keys across multiple servers in a way that minimizes redistribution when servers are added/removed.

```python
import hashlib
import bisect

class ConsistentHashRing:
    """
    Implement consistent hashing for distributed key-value storage.

    Key benefits:
    - Adding/removing servers only affects ~1/n of keys
    - Load balancing through virtual nodes
    - Fault tolerance and scalability
    """

    def __init__(self, servers=None, virtual_nodes=150):
        self.virtual_nodes = virtual_nodes
        self.ring = {}  # hash -> server
        self.sorted_keys = []  # Sorted list of hash values

        if servers:
            for server in servers:
                self.add_server(server)

    def _hash(self, key):
        """Generate hash for a key"""
        return int(hashlib.md5(key.encode()).hexdigest(), 16)

    def add_server(self, server):
        """Add a server to the hash ring"""
        for i in range(self.virtual_nodes):
            virtual_key = f"{server}:{i}"
            hash_val = self._hash(virtual_key)

            self.ring[hash_val] = server
            bisect.insort(self.sorted_keys, hash_val)

    def remove_server(self, server):
        """Remove a server from the hash ring"""
        for i in range(self.virtual_nodes):
            virtual_key = f"{server}:{i}"
            hash_val = self._hash(virtual_key)

            del self.ring[hash_val]
            self.sorted_keys.remove(hash_val)

    def get_server(self, key):
        """Find which server should handle this key"""
        if not self.ring:
            return None

        hash_val = self._hash(key)

        # Find first server clockwise from hash position
        idx = bisect.bisect_right(self.sorted_keys, hash_val)
        if idx == len(self.sorted_keys):
            idx = 0

        return self.ring[self.sorted_keys[idx]]
```

### 3. Bloom Filters for Membership Testing

**Problem**: Test membership in a set with minimal memory usage, allowing false positives but no false negatives.

```python
import hashlib
from bitarray import bitarray

class BloomFilter:
    """
    Space-efficient probabilistic data structure for membership testing.

    Key properties:
    - No false negatives (if element not in filter, definitely not in set)
    - Possible false positives (if element in filter, might be in set)
    - Much more space-efficient than hash sets for large datasets
    """

    def __init__(self, capacity, error_rate=0.01):
        """
        Initialize bloom filter.

        Args:
            capacity: Expected number of elements
            error_rate: Desired false positive rate
        """
        # Calculate optimal bit array size and number of hash functions
        self.capacity = capacity
        self.error_rate = error_rate

        # m = -n*ln(p) / (ln(2)^2)
        import math
        self.bit_array_size = int(-capacity * math.log(error_rate) / (math.log(2) ** 2))

        # k = (m/n) * ln(2)
        self.hash_count = int((self.bit_array_size / capacity) * math.log(2))

        self.bit_array = bitarray(self.bit_array_size)
        self.bit_array.setall(0)

        self.items_count = 0

    def _hashes(self, item):
        """Generate multiple hash values for an item"""
        hashes = []
        for i in range(self.hash_count):
            # Create different hash functions using salt
            salted_item = f"{item}:{i}"
            hash_val = int(hashlib.md5(salted_item.encode()).hexdigest(), 16)
            hashes.append(hash_val % self.bit_array_size)
        return hashes

    def add(self, item):
        """Add item to the bloom filter"""
        for hash_val in self._hashes(item):
            self.bit_array[hash_val] = 1
        self.items_count += 1

    def contains(self, item):
        """Check if item might be in the set"""
        for hash_val in self._hashes(item):
            if not self.bit_array[hash_val]:
                return False  # Definitely not in set
        return True  # Might be in set

    def false_positive_rate(self):
        """Calculate current false positive rate"""
        import math
        # (1 - e^(-k*n/m))^k
        return (1 - math.exp(-self.hash_count * self.items_count / self.bit_array_size)) ** self.hash_count
```

### 4. LRU Cache Implementation

**Problem**: Implement a Least Recently Used cache with O(1) get and put operations.

```python
class LRUCache:
    """
    LRU Cache using hash map + doubly linked list.

    Hash map provides O(1) access to nodes
    Doubly linked list maintains LRU order with O(1) insertion/deletion

    Structure:
    head <-> node1 <-> node2 <-> ... <-> tail
    (most recent)                    (least recent)
    """

    class Node:
        def __init__(self, key=0, value=0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> node

        # Create dummy head and tail nodes
        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_head(self, node):
        """Add node right after head (most recent position)"""
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """Remove node from linked list"""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node):
        """Move existing node to head (mark as most recent)"""
        self._remove_node(node)
        self._add_to_head(node)

    def _remove_tail(self):
        """Remove least recently used node"""
        last_node = self.tail.prev
        self._remove_node(last_node)
        return last_node

    def get(self, key):
            """Get value and mark as most recently used"""
            if key in self.cache:
                node = self.cache[key]
                # Move to head (mark as most recent)
                self._move_to_head(node)
                return node.value
            return -1

    def put(self, key, value):
        """Put key-value pair, evict LRU if at capacity"""
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            # Add new key
            if len(self.cache) >= self.capacity:
                # Remove LRU node
                lru_node = self._remove_tail()
                del self.cache[lru_node.key]

            # Add new node
            new_node = self.Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
```

## Problem Recognition Guide

Learning to identify hash table problems is crucial for efficient problem-solving.

### Immediate Red Flags (Strong Indicators)

🚨 **"Count" or "Frequency"** → Almost always hash tables

- "Count occurrences", "Most frequent", "Character frequency"
- "How many times", "Number of appearances"

🚨 **"Duplicate" or "Unique"** → Hash sets for fast lookups

- "Contains duplicate", "First unique", "Remove duplicates"
- "Find duplicates", "All unique elements"

🚨 **"Two Sum" or "Target Sum"** → Hash map for complement lookup

- "Two numbers that add up to", "Pair with sum"
- "Find two elements", "Target value"

🚨 **"Group" or "Categorize"** → Hash map for grouping

- "Group anagrams", "Group by property"
- "Organize by", "Classify elements"

🚨 **"Fast lookup" or "O(1) access"** → Hash table optimization

- "Quick search", "Efficient retrieval"
- "Constant time", "Instant access"

### Decision-Making Framework

```
Do you need to track/count something?
├─ YES: Likely hash table
│   ├─ Count frequencies? → Hash map (element → count)
│   ├─ Check existence? → Hash set
│   ├─ Group elements? → Hash map (key → list)
│   └─ Cache results? → Hash map (input → output)
│
└─ Need fast lookups?
    ├─ Search for complements? → Hash map
    ├─ Membership testing? → Hash set
    └─ Key-value associations? → Hash map
```

## Implementation Templates

### Template 1: Frequency Counting

```python
def frequency_template(data):
    """Use when: counting occurrences, finding most/least common"""
    from collections import Counter

    # Method 1: Using Counter (most convenient)
    freq = Counter(data)

    # Method 2: Manual counting (more control)
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1

    # Method 3: Using defaultdict
    from collections import defaultdict
    freq = defaultdict(int)
    for item in data:
        freq[item] += 1

    return freq
```

### Template 2: Fast Lookups

```python
def lookup_template(search_space, queries):
    """Use when: checking membership, finding intersections"""
    # Convert to set for O(1) lookups
    lookup_set = set(search_space)

    results = []
    for query in queries:
        if query in lookup_set:
            results.append(query)

    return results
```

### Template 3: Grouping

```python
def grouping_template(data, key_func):
    """Use when: grouping by property, organizing data"""
    from collections import defaultdict

    groups = defaultdict(list)
    for item in data:
        key = key_func(item)
        groups[key].append(item)

    return dict(groups)
```

### Template 4: Complement Search

```python
def complement_template(arr, target):
    """Use when: two sum, pair finding problems"""
    seen = {}  # value → index

    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []
```

## Common Pitfalls & How to Avoid Them

### 1. Hash Map Key Errors

**❌ Wrong**:

```python
# Accessing non-existent key
count = freq_map[key]  # KeyError if key doesn't exist
```

**✅ Correct**:

```python
# Safe key access
count = freq_map.get(key, 0)  # Returns 0 if key missing
# OR
if key in freq_map:
    count = freq_map[key]
```

### 2. Mutable Keys in Hash Maps

**❌ Wrong**:

```python
# Using mutable objects as keys
my_dict = {}
key = [1, 2, 3]  # Lists are mutable, can't be keys
my_dict[key] = "value"  # TypeError!
```

**✅ Correct**:

```python
# Use immutable objects as keys
my_dict = {}
key = (1, 2, 3)  # Tuples are immutable
my_dict[key] = "value"  # Works fine
```

### 3. Set vs Dictionary Confusion

**❌ Wrong**:

```python
# Using dictionary when set is sufficient
seen = {}
for item in data:
    seen[item] = True  # Unnecessary value storage
```

**✅ Correct**:

```python
# Use set for membership testing only
seen = set()
for item in data:
    seen.add(item)  # More memory efficient
```

### 4. Zero Count Cleanup

**❌ Wrong**:

```python
# Not cleaning up zero counts
freq[char] -= 1  # freq[char] might become 0
# Zero entries remain in dictionary
```

**✅ Correct**:

```python
# Clean up zero counts
freq[char] -= 1
if freq[char] == 0:
    del freq[char]  # Remove zero entries
```

## Practice Framework

### Phase 1: Basic Hash Table Operations (Week 1)

**Goal**: Master fundamental hash table patterns and operations.

**Problems to Master**:

1. **Two Sum** - The foundation

   ```python
   # Key learnings:
   # - Complement calculation
   # - Hash map for O(1) lookups
   # - One-pass vs two-pass approaches
   ```

2. **Contains Duplicate** - Basic existence checking

   ```python
   # Key learnings:
   # - Set vs hash map choice
   # - Early termination optimization
   # - Memory vs time tradeoffs
   ```

3. **Valid Anagram** - Character frequency counting

   ```python
   # Key learnings:
   # - Frequency comparison techniques
   # - Counter vs manual counting
   # - Edge case handling
   ```

4. **Group Anagrams** - Grouping by computed keys
   ```python
   # Key learnings:
   # - Canonical key generation
   # - defaultdict usage
   # - Efficiency of different key methods
   ```

### Phase 2: Advanced Applications (Week 2)

**Goal**: Apply hash tables to more complex problems and optimizations.

**Problems to Master**:

1. **Longest Substring Without Repeating Characters** - Sliding window + hash set
2. **Top K Frequent Elements** - Frequency counting + sorting/heap
3. **Subarray Sum Equals K** - Prefix sums + hash map
4. **LRU Cache** - Hash map + doubly linked list

### Phase 3: System Design Applications (Week 3)

**Goal**: Understand hash tables in system design and advanced algorithms.

**Topics to Cover**:

1. **Consistent Hashing** - Distributed systems
2. **Bloom Filters** - Memory-efficient membership testing
3. **Hash-based Data Structures** - Hash sets, hash maps variations
4. **Collision Resolution** - Chaining vs open addressing

### Testing Strategy

**Essential Test Cases**:

1. **Empty Input**: `[]`, `""`, `{}`
2. **Single Element**: `[1]`, `"a"`
3. **All Same Elements**: `[1,1,1]`
4. **No Duplicates**: `[1,2,3,4]`
5. **All Duplicates**: `[1,1,1,1]`
6. **Large Input**: Test performance
7. **Edge Values**: `None`, empty strings, special characters

## Complexity Analysis

### Time Complexity

- **Hash Operations**: O(1) average, O(n) worst case
- **Frequency Counting**: O(n) where n is input size
- **Grouping**: O(n) for grouping, O(k) per group access
- **Two Sum**: O(n) with hash map vs O(n²) brute force

### Space Complexity

- **Hash Set**: O(n) for n unique elements
- **Hash Map**: O(n) for n key-value pairs
- **Frequency Map**: O(k) where k is number of unique elements

## Summary and Key Takeaways

### The Power of Hash Tables

Hash tables are fundamental because they provide:

1. **O(1) Operations**: Constant time lookup, insertion, deletion
2. **Flexibility**: Handle any hashable data type as keys
3. **Versatility**: Support counting, grouping, caching, indexing
4. **Optimization**: Transform O(n²) algorithms to O(n)

### Essential Patterns to Master

1. **Frequency Counting**: Use Counter or manual counting
2. **Fast Lookups**: Convert lists to sets for membership testing
3. **Complement Search**: Store seen values, check for complements
4. **Grouping**: Use computed keys to organize data
5. **Caching**: Store expensive computation results

### When to Choose Hash Tables

- ✅ Need fast lookups, insertions, or deletions
- ✅ Counting or frequency analysis required
- ✅ Grouping or categorizing data
- ✅ Checking for existence or duplicates
- ✅ Implementing caches or memoization

- ❌ Need ordered data (use trees instead)
- ❌ Range queries required (use arrays/trees)
- ❌ Memory is extremely constrained
- ❌ Keys are not hashable

### Final Practice Tips

- **Start with brute force**, then optimize with hash tables
- **Choose the right structure**: set vs dict vs Counter
- **Handle edge cases**: empty input, duplicates, invalid keys
- **Consider space-time tradeoffs**: hash tables use extra space for speed
- **Practice explaining**: why hash tables solve the problem efficiently

Hash tables are among the most important data structures in programming. Master them, and you'll have a powerful tool for solving a vast range of problems efficiently! 🚀
