# Linked Lists - Study Notes

## Core Concept

Linked Lists are linear data structures where elements (nodes) are stored in sequence, but not necessarily in contiguous memory locations. Each node contains data and a reference (pointer) to the next node.

## Types of Linked Lists

### 1. Singly Linked List

- **Structure**: Each node points to the next node
- **Traversal**: Only forward direction
- **Memory**: Less memory per node

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### 2. Doubly Linked List

- **Structure**: Each node has pointers to both next and previous nodes
- **Traversal**: Both forward and backward
- **Memory**: More memory per node

```python
class DoublyListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
```

### 3. Circular Linked List

- **Structure**: Last node points back to first node
- **Traversal**: Can loop infinitely
- **Detection**: Need special handling to avoid infinite loops

## Common Operations

### Basic Operations:

```python
# Traversal
def traverse(head):
    current = head
    while current:
        print(current.val)
        current = current.next

# Search
def search(head, target):
    current = head
    while current:
        if current.val == target:
            return current
        current = current.next
    return None

# Insert at beginning
def insert_at_beginning(head, val):
    new_node = ListNode(val)
    new_node.next = head
    return new_node

# Insert at end
def insert_at_end(head, val):
    new_node = ListNode(val)
    if not head:
        return new_node

    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

# Delete node
def delete_node(head, val):
    if not head:
        return None

    if head.val == val:
        return head.next

    current = head
    while current.next and current.next.val != val:
        current = current.next

    if current.next:
        current.next = current.next.next

    return head
```

## Common Patterns

### Pattern 1: Two Pointers (Fast & Slow)

```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

### Pattern 2: Dummy Node

```python
def remove_elements(head, val):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next

    return dummy.next
```

### Pattern 3: Reverse Linked List

```python
def reverse_list(head):
    prev = None
    current = head

    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp

    return prev
```

### Pattern 4: Merge Two Lists

```python
def merge_two_lists(l1, l2):
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 or l2
    return dummy.next
```

## When to Use Linked Lists

### Advantages:

- **Dynamic size**: Can grow/shrink during runtime
- **Efficient insertion/deletion**: O(1) at known positions
- **Memory efficient**: Only allocate what's needed

### Disadvantages:

- **No random access**: Must traverse to reach elements
- **Extra memory**: Storage overhead for pointers
- **Cache locality**: Poor cache performance

### Use Cases:

- **Undo functionality**: Easy to add/remove operations
- **Music playlists**: Easy insertion/deletion of songs
- **Browser history**: Navigate back/forward
- **Implementation of stacks/queues**

## Time Complexity

| Operation | Array | Linked List |
| --------- | ----- | ----------- |
| Access    | O(1)  | O(n)        |
| Search    | O(n)  | O(n)        |
| Insert    | O(n)  | O(1)\*      |
| Delete    | O(n)  | O(1)\*      |

\*O(1) if position is known, O(n) if need to find position

## Common Techniques

### 1. Sentinel/Dummy Nodes

- Simplify edge cases (empty list, single node)
- Make code cleaner and less error-prone

### 2. Two Pointers

- **Fast/Slow**: Find middle, detect cycles
- **Distance**: Maintain k distance between pointers

### 3. Recursion

- Natural fit for linked list problems
- Base case: null or single node
- Recursive case: process current + recurse on rest

### 4. Stack for Reversal

- Store nodes while traversing forward
- Pop to get reverse order

## Edge Cases to Consider

1. **Empty list**: `head = None`
2. **Single node**: `head.next = None`
3. **Cycles**: Use Floyd's algorithm
4. **Memory management**: Avoid memory leaks
5. **Invalid positions**: Handle gracefully

## Templates

### Basic Traversal Template:

```python
def process_list(head):
    current = head
    while current:
        # Process current node
        process(current.val)
        current = current.next
```

### Two Pointers Template:

```python
def two_pointers_solution(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # Check condition
    return slow
```

### Recursive Template:

```python
def recursive_solution(head):
    # Base case
    if not head:
        return None

    # Process current
    result = process(head.val)

    # Recurse
    head.next = recursive_solution(head.next)

    return head
```
