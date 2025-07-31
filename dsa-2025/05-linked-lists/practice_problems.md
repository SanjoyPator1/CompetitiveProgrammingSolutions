# Linked Lists - Practice Problems

## Problem 1: Reverse Linked List

**Difficulty**: Easy

**Description**: Reverse a singly linked list.

**Example**:

```
Input: 1->2->3->4->5
Output: 5->4->3->2->1
```

**Hint**: Use three pointers: prev, current, next. Iteratively reverse links.

---

## Problem 2: Middle of Linked List

**Difficulty**: Easy

**Description**: Find the middle node of linked list.

**Example**:

```
Input: 1->2->3->4->5
Output: Node with value 3
```

**Hint**: Use fast and slow pointers (tortoise and hare).

---

## Problem 3: Linked List Cycle

**Difficulty**: Easy

**Description**: Detect if linked list has a cycle.

**Example**:

```
Input: 3->2->0->-4 (with -4 pointing back to 2)
Output: True
```

**Hint**: Floyd's cycle detection algorithm with fast/slow pointers.

---

## Problem 4: Remove Duplicates from Sorted List

**Difficulty**: Easy

**Description**: Remove all duplicate nodes from sorted linked list.

**Example**:

```
Input: 1->1->2->3->3
Output: 1->2->3
```

**Hint**: Compare current node with next node, skip duplicates.

---

## Problem 5: Merge Two Sorted Lists

**Difficulty**: Easy

**Description**: Merge two sorted linked lists into one sorted list.

**Example**:

```
Input: l1 = 1->2->4, l2 = 1->3->4
Output: 1->1->2->3->4->4
```

**Hint**: Use dummy node and two pointers to compare values.

---

## Problem 6: Remove Linked List Elements

**Difficulty**: Easy

**Description**: Remove all nodes with given value.

**Example**:

```
Input: 1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
```

**Hint**: Use dummy node to handle edge cases like removing head.

---

## Problem 7: Palindrome Linked List

**Difficulty**: Easy

**Description**: Check if linked list is a palindrome.

**Example**:

```
Input: 1->2->2->1
Output: True
```

**Hint**: Find middle, reverse second half, compare with first half.

---

## Problem 8: Intersection of Two Linked Lists

**Difficulty**: Easy

**Description**: Find node where two linked lists intersect.

**Example**:

```
Input: listA = 4->1->8->4->5, listB = 5->6->1->8->4->5
Output: Node with value 8
```

**Hint**: Two pointers, when one reaches end, start from other list's head.

---

## Problem 9: Remove Nth Node From End

**Difficulty**: Medium

**Description**: Remove the nth node from end of list.

**Example**:

```
Input: 1->2->3->4->5, n = 2
Output: 1->2->3->5
```

**Hint**: Two pointers with n gap between them.

---

## Problem 10: Add Two Numbers

**Difficulty**: Medium

**Description**: Add two numbers represented as linked lists (digits in reverse order).

**Example**:

```
Input: l1 = 2->4->3, l2 = 5->6->4 (represents 342 + 465)
Output: 7->0->8 (represents 807)
```

**Hint**: Process digits one by one, handle carry.

---

## Problem 11: Swap Nodes in Pairs

**Difficulty**: Medium

**Description**: Swap every two adjacent nodes.

**Example**:

```
Input: 1->2->3->4
Output: 2->1->4->3
```

**Hint**: Use dummy node and carefully manage next pointers.

---

## Problem 12: Odd Even Linked List

**Difficulty**: Medium

**Description**: Group odd positioned nodes together, then even positioned nodes.

**Example**:

```
Input: 1->2->3->4->5
Output: 1->3->5->2->4
```

**Hint**: Maintain odd and even pointers, connect at the end.

---

## Problem 13: Rotate List

**Difficulty**: Medium

**Description**: Rotate list to the right by k places.

**Example**:

```
Input: 1->2->3->4->5, k = 2
Output: 4->5->1->2->3
```

**Hint**: Find length, make circular, then break at appropriate point.

---

## Problem 14: Sort List

**Difficulty**: Medium

**Description**: Sort linked list in O(n log n) time and O(1) space.

**Example**:

```
Input: 4->2->1->3
Output: 1->2->3->4
```

**Hint**: Use merge sort with find middle and merge operations.

---

## Problem 15: Reorder List

**Difficulty**: Medium

**Description**: Reorder list to L0→Ln→L1→Ln-1→L2→Ln-2→...

**Example**:

```
Input: 1->2->3->4->5
Output: 1->5->2->4->3
```

**Hint**: Find middle, reverse second half, merge alternately.

---

## Problem 16: Copy List with Random Pointer

**Difficulty**: Medium

**Description**: Deep copy linked list where each node has random pointer.

**Example**:

```
Input: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: Deep copy of the list
```

**Hint**: Three passes - create nodes, set random pointers, separate lists.

---

## Problem 17: Flatten Multilevel Doubly Linked List

**Difficulty**: Medium

**Description**: Flatten a multilevel doubly linked list.

**Example**:

```
Input: 1-2-3-4-5-6-NULL with branch at 3
Output: Flattened single level list
```

**Hint**: Use stack to handle branches, or recursion.

---

## Problem 18: Reverse Nodes in k-Group

**Difficulty**: Medium

**Description**: Reverse nodes in groups of k.

**Example**:

```
Input: 1->2->3->4->5, k = 3
Output: 3->2->1->4->5
```

**Hint**: Check if k nodes available, reverse group, recursively handle rest.

---

## Solving Strategy for Linked List Problems

### Step-by-Step Approach:

1. **Understand the structure**: Single/double, circular, with cycles?
2. **Identify pattern**: Two pointers, reversal, merging?
3. **Handle edge cases**: Empty list, single node
4. **Choose technique**: Iterative vs recursive
5. **Use dummy node**: Simplifies many problems

### Common Patterns:

- **Two pointers**: Fast/slow for cycles, middle finding
- **Dummy node**: Simplifies insertion/deletion at head
- **Reversal**: Three pointers for iterative reversal
- **Merging**: Compare values and link appropriately

### Key Insights:

- **Draw it out**: Visualize pointer movements
- **Edge cases first**: Handle null, single node cases
- **Dummy nodes**: Great for simplifying logic
- **Multiple passes**: Sometimes easier than single pass

### Testing Tips:

1. **Empty list**: `None` or `null`
2. **Single node**: Only one element
3. **Two nodes**: Minimum for swapping/reversing
4. **Cycles**: If problem allows
5. **Large lists**: Test performance
