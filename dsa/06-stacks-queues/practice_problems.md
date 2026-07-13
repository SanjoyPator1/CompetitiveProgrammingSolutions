# Stacks and Queues - Practice Problems

## Problem 1: Valid Parentheses

**Difficulty**: Easy

**Description**: Check if string of parentheses is valid (properly opened and closed).

**Example**:

```
Input: "()[]{}"
Output: True

Input: "([)]"
Output: False
```

**Hint**: Use stack to match opening brackets with closing ones.

---

## Problem 2: Implement Queue using Stacks

**Difficulty**: Easy

**Description**: Implement queue operations using only stack operations.

**Example**:

```
Input: ["MyQueue", "push", "push", "peek", "pop", "empty"]
       [[], [1], [2], [], [], []]
Output: [null, null, null, 1, 1, false]
```

**Hint**: Use two stacks - one for input, one for output.

---

## Problem 3: Implement Stack using Queues

**Difficulty**: Easy

**Description**: Implement stack operations using only queue operations.

**Example**:

```
Input: ["MyStack", "push", "push", "top", "pop", "empty"]
       [[], [1], [2], [], [], []]
Output: [null, null, null, 2, 2, false]
```

**Hint**: Use one or two queues, simulate LIFO behavior.

---

## Problem 4: Baseball Game

**Difficulty**: Easy

**Description**: Calculate final score based on operations: number (score), "C" (cancel), "D" (double), "+" (sum of last two).

**Example**:

```
Input: ["5","2","C","D","+"]
Output: 30 (5 + 2*2 + (2+4) = 15)
```

**Hint**: Use stack to track valid scores, apply operations.

---

## Problem 5: Next Greater Element I

**Difficulty**: Easy

**Description**: Find next greater element for each element in nums1 (subset of nums2).

**Example**:

```
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
```

**Hint**: Use monotonic stack on nums2, then lookup for nums1.

---

## Problem 6: Remove All Adjacent Duplicates

**Difficulty**: Easy

**Description**: Remove all adjacent duplicate characters.

**Example**:

```
Input: "abbaca"
Output: "ca"
```

**Hint**: Use stack, pop if top equals current character.

---

## Problem 7: Min Stack

**Difficulty**: Easy

**Description**: Design stack that supports push, pop, top, and getMin in O(1).

**Example**:

```
Input: ["MinStack","push","push","push","getMin","pop","top","getMin"]
       [[],[-2],[0],[-3],[],[],[],[]]
Output: [null,null,null,null,-3,null,0,-2]
```

**Hint**: Use auxiliary stack to track minimums or store pairs.

---

## Problem 8: Backspace String Compare

**Difficulty**: Easy

**Description**: Compare two strings where '#' represents backspace.

**Example**:

```
Input: s = "ab#c", t = "ad#c"
Output: True (both become "ac")
```

**Hint**: Use stack to process backspaces, or two pointers from right.

---

## Problem 9: Daily Temperatures

**Difficulty**: Medium

**Description**: Find how many days until warmer temperature for each day.

**Example**:

```
Input: [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

**Hint**: Use monotonic stack to find next greater element.

---

## Problem 10: Evaluate Reverse Polish Notation

**Difficulty**: Medium

**Description**: Evaluate arithmetic expression in postfix notation.

**Example**:

```
Input: ["2","1","+","3","*"]
Output: 9 ((2 + 1) * 3)
```

**Hint**: Use stack, push numbers, pop for operations.

---

## Problem 11: Generate Parentheses

**Difficulty**: Medium

**Description**: Generate all valid combinations of n pairs of parentheses.

**Example**:

```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

**Hint**: Use backtracking with stack to track current combination.

---

## Problem 12: Largest Rectangle in Histogram

**Difficulty**: Medium

**Description**: Find area of largest rectangle that can be formed in histogram.

**Example**:

```
Input: [2,1,5,6,2,3]
Output: 10 (rectangle with height 5 and width 2)
```

**Hint**: Use monotonic stack to find previous/next smaller elements.

---

## Problem 13: Sliding Window Maximum

**Difficulty**: Medium

**Description**: Find maximum element in each sliding window of size k.

**Example**:

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
```

**Hint**: Use deque to maintain potential maximums in window.

---

## Problem 14: Binary Tree Level Order Traversal

**Difficulty**: Medium

**Description**: Return level order traversal of binary tree.

**Example**:

```
Input: [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

**Hint**: Use queue for BFS, process one level at a time.

---

## Problem 15: Binary Tree Zigzag Level Order Traversal

**Difficulty**: Medium

**Description**: Return zigzag level order traversal (left-to-right, then right-to-left).

**Example**:

```
Input: [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
```

**Hint**: Use queue for BFS, reverse alternate levels.

---

## Problem 16: Decode String

**Difficulty**: Medium

**Description**: Decode string where pattern is k[encoded_string].

**Example**:

```
Input: "3[a2[c]]"
Output: "accaccacc"
```

**Hint**: Use stack to handle nested brackets, store count and string.

---

## Problem 17: Remove K Digits

**Difficulty**: Medium

**Description**: Remove k digits from number to make smallest possible number.

**Example**:

```
Input: num = "1432219", k = 3
Output: "1219"
```

**Hint**: Use monotonic stack, remove larger digits when possible.

---

## Problem 18: Asteroid Collision

**Difficulty**: Medium

**Description**: Simulate asteroid collisions (positive = right, negative = left).

**Example**:

```
Input: [5,10,-5]
Output: [5,10] (-5 destroyed by 10)
```

**Hint**: Use stack, handle collisions when positive meets negative.

---

## Solving Strategy for Stack and Queue Problems

### Stack Problem Patterns:

1. **Matching/Pairing**: Parentheses, duplicates
2. **Monotonic Stack**: Next greater/smaller element
3. **Expression Evaluation**: Postfix, infix conversion
4. **Backtracking**: Generate combinations
5. **Undo Operations**: Min stack, browser history

### Queue Problem Patterns:

1. **Level Processing**: BFS traversal, level order
2. **Sliding Window**: Maximum/minimum in window
3. **Scheduling**: Round-robin, job processing
4. **Buffer**: Stream processing, rate limiting

### Key Insights:

- **Stack for depth**: DFS, recursion simulation, undo
- **Queue for breadth**: BFS, level processing, FIFO
- **Deque for flexibility**: Both ends access, sliding window
- **Monotonic structures**: Optimization problems

### Problem-Solving Steps:

1. **Identify the access pattern**: LIFO vs FIFO vs both ends
2. **Choose appropriate data structure**: Stack, queue, or deque
3. **Handle edge cases**: Empty structures, single elements
4. **Consider time/space complexity**: Usually O(n) time, O(n) space
5. **Test with examples**: Trace through operations manually

### Common Techniques:

- **Auxiliary structures**: Extra stack/queue for optimization
- **State tracking**: What information to store with each element
- **Monotonic property**: Maintain order for optimization
- **Level processing**: Process elements in groups/le
