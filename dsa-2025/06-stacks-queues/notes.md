# Stacks and Queues - Study Notes

## Core Concepts

### Stack (LIFO - Last In, First Out)

- **Principle**: Last element added is first to be removed
- **Operations**: push (add), pop (remove), peek/top (view top), isEmpty
- **Real-world analogy**: Stack of plates, undo operations

```python
# Using Python list as stack
stack = []
stack.append(item)    # push - O(1)
item = stack.pop()    # pop - O(1)
top = stack[-1]       # peek - O(1)
is_empty = len(stack) == 0
```

### Queue (FIFO - First In, First Out)

- **Principle**: First element added is first to be removed
- **Operations**: enqueue (add), dequeue (remove), front (view first), isEmpty
- **Real-world analogy**: Line at store, printer queue

```python
from collections import deque

# Using deque for efficient queue operations
queue = deque()
queue.append(item)       # enqueue - O(1)
item = queue.popleft()   # dequeue - O(1)
front = queue[0]         # front - O(1)
is_empty = len(queue) == 0
```

## Types and Variations

### 1. Monotonic Stack

- **Purpose**: Maintain elements in monotonic order
- **Use cases**: Next greater element, histogram problems

```python
def monotonic_stack_increasing(arr):
    stack = []  # stores indices
    result = []

    for i, val in enumerate(arr):
        # Remove elements that violate monotonic property
        while stack and arr[stack[-1]] > val:
            stack.pop()

        # Process current element
        if stack:
            result.append(arr[stack[-1]])  # Previous smaller element
        else:
            result.append(-1)  # No smaller element

        stack.append(i)

    return result
```

### 2. Priority Queue (Heap)

- **Purpose**: Elements with higher priority are served first
- **Implementation**: Usually with heaps

```python
import heapq

# Min heap (default in Python)
pq = []
heapq.heappush(pq, item)     # O(log n)
item = heapq.heappop(pq)     # O(log n)

# Max heap (negate values)
heapq.heappush(pq, -item)
item = -heapq.heappop(pq)
```

### 3. Deque (Double-ended Queue)

- **Purpose**: Add/remove from both ends efficiently
- **Use cases**: Sliding window maximum, palindrome checking

```python
from collections import deque

dq = deque()
dq.append(item)      # add to right - O(1)
dq.appendleft(item)  # add to left - O(1)
dq.pop()             # remove from right - O(1)
dq.popleft()         # remove from left - O(1)
```

## Common Patterns

### Pattern 1: Parentheses/Bracket Matching

```python
def is_valid_parentheses(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:  # closing bracket
            if not stack or stack.pop() != mapping[char]:
                return False
        else:  # opening bracket
            stack.append(char)

    return len(stack) == 0
```

### Pattern 2: Next Greater/Smaller Element

```python
def next_greater_element(nums):
    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)

    return result
```

### Pattern 3: Evaluate Expression

```python
def evaluate_postfix(tokens):
    stack = []

    for token in tokens:
        if token in ['+', '-', '*', '/']:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            else:  # division
                stack.append(int(a / b))  # truncate towards zero
        else:
            stack.append(int(token))

    return stack[0]
```

### Pattern 4: Level Order Traversal (BFS)

```python
def level_order_traversal(root):
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result
```

### Pattern 5: Sliding Window Maximum

```python
def sliding_window_maximum(nums, k):
    dq = deque()  # stores indices
    result = []

    for i in range(len(nums)):
        # Remove indices outside window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove indices of smaller elements
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        dq.append(i)

        # Add to result when window is full
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
```

## When to Use Stacks vs Queues

### Use Stack When:

- **Undo operations**: Browser back, text editor undo
- **Expression evaluation**: Postfix, infix conversion
- **Parentheses matching**: Balanced brackets
- **Function calls**: Call stack
- **DFS traversal**: Depth-first search
- **Backtracking**: Try all possibilities

### Use Queue When:

- **BFS traversal**: Level-order, shortest path
- **Job scheduling**: Process tasks in order
- **Buffer**: Streaming data
- **Cache**: LRU cache implementation
- **Resource sharing**: Printer queue, CPU scheduling

### Use Deque When:

- **Sliding window**: Maximum/minimum in window
- **Palindrome**: Check from both ends
- **Undo/Redo**: Both operations needed
- **Circular operations**: Round-robin scheduling

## Stack Applications

### 1. Function Call Stack

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)  # Each call pushed to stack
```

### 2. Expression Parsing

```python
def infix_to_postfix(expression):
    stack = []
    result = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    for char in expression:
        if char.isalnum():
            result.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # Remove '('
        else:  # operator
            while (stack and stack[-1] != '(' and
                   precedence.get(stack[-1], 0) >= precedence[char]):
                result.append(stack.pop())
            stack.append(char)

    while stack:
        result.append(stack.pop())

    return ''.join(result)
```

### 3. Backtracking

```python
def generate_parentheses(n):
    result = []
    stack = []

    def backtrack(open_count, close_count):
        if open_count == close_count == n:
            result.append(''.join(stack))
            return

        if open_count < n:
            stack.append('(')
            backtrack(open_count + 1, close_count)
            stack.pop()

        if close_count < open_count:
            stack.append(')')
            backtrack(open_count, close_count + 1)
            stack.pop()

    backtrack(0, 0)
    return result
```

## Queue Applications

### 1. BFS Implementation

```python
def bfs_shortest_path(graph, start, end):
    queue = deque([(start, 0)])  # (node, distance)
    visited = {start}

    while queue:
        node, dist = queue.popleft()

        if node == end:
            return dist

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return -1  # No path found
```

### 2. Level Processing

```python
def print_levels(root):
    if not root:
        return

    queue = deque([root])
    level = 0

    while queue:
        print(f"Level {level}:")
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            print(node.val, end=' ')

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        print()  # New line after each level
        level += 1
```

## Time and Space Complexity

### Stack Operations:

| Operation | Time | Space |
| --------- | ---- | ----- |
| Push      | O(1) | O(1)  |
| Pop       | O(1) | O(1)  |
| Peek      | O(1) | O(1)  |
| Search    | O(n) | O(1)  |

### Queue Operations:

| Operation | Time | Space |
| --------- | ---- | ----- |
| Enqueue   | O(1) | O(1)  |
| Dequeue   | O(1) | O(1)  |
| Front     | O(1) | O(1)  |
| Search    | O(n) | O(1)  |

## Common Mistakes to Avoid

1. **Using list for queue**: `list.pop(0)` is O(n), use `deque`
2. **Not checking if empty**: Always check before pop/dequeue
3. **Forgetting to handle edge cases**: Empty structures
4. **Stack overflow**: Too much recursion without base case
5. **Memory leaks**: Not properly cleaning up references

## Implementation Templates

### Stack Template:

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

### Queue Template:

```python
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.popleft()

    def front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```
