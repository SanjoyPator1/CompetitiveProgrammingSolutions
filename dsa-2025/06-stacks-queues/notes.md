# Stacks and Queues - Comprehensive Study Notes with Detailed Explanations

## Table of Contents

1. [Core Concept & Philosophy](#core-concept--philosophy)
2. [Stacks - Deep Dive](#stacks---deep-dive)
3. [Queues - Deep Dive](#queues---deep-dive)
4. [Advanced Variations](#advanced-variations)
5. [Pattern Deep Dive](#pattern-deep-dive)
6. [Problem Recognition Guide](#problem-recognition-guide)
7. [Implementation Templates](#implementation-templates)
8. [Complexity Analysis](#complexity-analysis)
9. [Common Pitfalls & Practice Framework](#common-pitfalls--practice-framework)

## Core Concept & Philosophy

### What are Stacks and Queues?

**Stacks** and **Queues** are **abstract data types (ADTs)** that define specific ways of organizing and accessing data. Unlike arrays or linked lists which allow access at any position, stacks and queues restrict access to specific ends, creating predictable and useful behavior patterns.

### The Big Idea

**Think of it like this**:

- **Stack** = A stack of plates in a cafeteria. You can only add or remove plates from the top. The last plate you put on is the first one you take off (LIFO - Last In, First Out).
- **Queue** = A line at a coffee shop. People join at the back and are served from the front. The first person in line is the first to be served (FIFO - First In, First Out).

### Core Principles

1. **Restricted Access**: Access is limited to specific ends only
2. **Predictable Order**: Elements are processed in a specific sequence
3. **Abstract Interface**: Focus on what operations are allowed, not how they're implemented
4. **Foundation for Algorithms**: Essential building blocks for many algorithms
5. **State Management**: Perfect for tracking nested operations or sequences

### When Stacks and Queues Shine

**Stacks Excel At**:

- **Nested Operations**: Function calls, parentheses matching
- **Undo Functionality**: Reversible operations
- **Expression Evaluation**: Mathematical expressions, parsing
- **Depth-First Traversals**: DFS in trees and graphs
- **Backtracking**: Exploring all possibilities

**Queues Excel At**:

- **Sequential Processing**: First-come, first-served scenarios
- **Breadth-First Traversals**: BFS in trees and graphs
- **Scheduling**: Process scheduling, task management
- **Buffering**: Stream processing, producer-consumer patterns
- **Level-Order Operations**: Processing data level by level

## Stacks - Deep Dive

### Stack Philosophy: LIFO (Last In, First Out)

**Mental Model**: Think of a stack as a "reversing machine." Whatever you put in last comes out first, naturally reversing the order of operations.

### Core Stack Operations

```python
class Stack:
    """
    Stack implementation using Python list.

    Core Operations:
    - push(item): Add item to top - O(1)
    - pop(): Remove and return top item - O(1)
    - peek()/top(): View top item without removing - O(1)
    - is_empty(): Check if stack is empty - O(1)
    - size(): Get number of items - O(1)
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        """Add item to top of stack"""
        self.items.append(item)
        print(f"Pushed: {item}, Stack: {self.items}")

    def pop(self):
        """Remove and return top item"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        item = self.items.pop()
        print(f"Popped: {item}, Stack: {self.items}")
        return item

    def peek(self):
        """View top item without removing"""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0

    def size(self):
        """Get number of items"""
        return len(self.items)

    def __str__(self):
        return f"Stack: {self.items} (top: {self.items[-1] if self.items else 'empty'})"
```

### Stack Implementation Variations

#### Array-Based Stack (Most Common)

**Advantages**:

- Simple implementation
- Good cache performance
- O(1) operations

**Disadvantages**:

- Fixed maximum size (in some languages)
- Potential memory waste

```python
class ArrayStack:
    """Fixed-size stack using array"""

    def __init__(self, capacity=100):
        self.capacity = capacity
        self.items = [None] * capacity
        self.top_index = -1

    def push(self, item):
        if self.top_index >= self.capacity - 1:
            raise OverflowError("Stack overflow")

        self.top_index += 1
        self.items[self.top_index] = item

    def pop(self):
        if self.top_index < 0:
            raise IndexError("Stack underflow")

        item = self.items[self.top_index]
        self.items[self.top_index] = None  # Help garbage collection
        self.top_index -= 1
        return item
```

#### Linked List-Based Stack

**Advantages**:

- Dynamic size
- No wasted memory
- True O(1) operations

**Disadvantages**:

- Extra memory for pointers
- Potential cache misses

```python
class LinkedStack:
    """Stack using linked list (nodes)"""

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None  # Top of stack
        self.size_count = 0

    def push(self, item):
        new_node = self.Node(item)
        new_node.next = self.head
        self.head = new_node
        self.size_count += 1

    def pop(self):
        if not self.head:
            raise IndexError("Pop from empty stack")

        item = self.head.data
        self.head = self.head.next
        self.size_count -= 1
        return item
```

## Queues - Deep Dive

### Queue Philosophy: FIFO (First In, First Out)

**Mental Model**: Think of a queue as a "fairness machine." Everyone gets served in the order they arrived, ensuring fairness and predictable processing.

### Core Queue Operations

```python
from collections import deque

class Queue:
    """
    Queue implementation using deque for efficiency.

    Core Operations:
    - enqueue(item): Add item to rear - O(1)
    - dequeue(): Remove and return front item - O(1)
    - front(): View front item without removing - O(1)
    - is_empty(): Check if queue is empty - O(1)
    - size(): Get number of items - O(1)
    """

    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        """Add item to rear of queue"""
        self.items.append(item)
        print(f"Enqueued: {item}, Queue: {list(self.items)}")

    def dequeue(self):
        """Remove and return front item"""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        item = self.items.popleft()
        print(f"Dequeued: {item}, Queue: {list(self.items)}")
        return item

    def front(self):
        """View front item without removing"""
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.items[0]

    def rear(self):
        """View rear item without removing"""
        if self.is_empty():
            raise IndexError("Rear from empty queue")
        return self.items[-1]

    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0

    def size(self):
        """Get number of items"""
        return len(self.items)
```

### Queue Implementation Variations

#### Circular Array Queue

**Key Insight**: Use circular array to avoid shifting elements, making both enqueue and dequeue O(1).

```python
class CircularQueue:
    """
    Efficient queue using circular array.

    Key concepts:
    - front: index of first element
    - rear: index of last element
    - Circular wraparound: (index + 1) % capacity
    """

    def __init__(self, capacity):
        self.capacity = capacity + 1  # Extra space to distinguish full vs empty
        self.items = [None] * self.capacity
        self.front_idx = 0
        self.rear_idx = 0

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue is full")

        self.items[self.rear_idx] = item
        self.rear_idx = (self.rear_idx + 1) % self.capacity

        print(f"Enqueued: {item}, front={self.front_idx}, rear={self.rear_idx}")

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        item = self.items[self.front_idx]
        self.items[self.front_idx] = None
        self.front_idx = (self.front_idx + 1) % self.capacity

        print(f"Dequeued: {item}, front={self.front_idx}, rear={self.rear_idx}")
        return item

    def is_empty(self):
        return self.front_idx == self.rear_idx

    def is_full(self):
        return (self.rear_idx + 1) % self.capacity == self.front_idx

    def size(self):
        return (self.rear_idx - self.front_idx + self.capacity) % self.capacity
```

## Advanced Variations

### 1. Monotonic Stack

**Concept**: A stack that maintains elements in monotonic (increasing or decreasing) order.

**Key Insight**: When adding a new element, pop elements that violate the monotonic property. This is useful for finding next greater/smaller elements.

```python
def monotonic_stack_template(arr, increasing=True):
    """
    Template for monotonic stack problems.

    Example: Find next greater element for each element
    arr = [2, 1, 2, 4, 3, 1]

    For increasing stack (to find next greater):
    i=0, val=2: stack=[], push 2, stack=[2]
    i=1, val=1: 1<2, push 1, stack=[2,1]
    i=2, val=2: 2>1, pop 1 (next greater of 1 is 2), push 2, stack=[2,2]
    i=3, val=4: 4>2, pop both 2s, push 4, stack=[4]
    Continue...
    """
    stack = []
    result = []

    for i, val in enumerate(arr):
        # Pop elements that violate monotonic property
        while stack and ((increasing and arr[stack[-1]] < val) or
                        (not increasing and arr[stack[-1]] > val)):
            index = stack.pop()
            # Process the popped element
            result.append((index, i))  # next greater/smaller found

        stack.append(i)

    return result

def next_greater_elements(arr):
    """Find next greater element for each element"""
    stack = []
    result = [-1] * len(arr)

    for i, val in enumerate(arr):
        # Pop smaller elements and set their next greater
        while stack and arr[stack[-1]] < val:
            index = stack.pop()
            result[index] = val

        stack.append(i)

    return result
```

### 2. Deque (Double-Ended Queue)

**Concept**: A queue that allows insertion and deletion at both ends.

**Use Cases**: Sliding window maximum, palindrome checking, undo-redo systems.

```python
from collections import deque

class Deque:
    """
    Double-ended queue allowing operations at both ends.

    Operations:
    - append_left(item): Add to front - O(1)
    - append_right(item): Add to rear - O(1)
    - pop_left(): Remove from front - O(1)
    - pop_right(): Remove from rear - O(1)
    """

    def __init__(self):
        self.items = deque()

    def append_left(self, item):
        """Add item to front"""
        self.items.appendleft(item)

    def append_right(self, item):
        """Add item to rear"""
        self.items.append(item)

    def pop_left(self):
        """Remove and return front item"""
        if not self.items:
            raise IndexError("Pop from empty deque")
        return self.items.popleft()

    def pop_right(self):
        """Remove and return rear item"""
        if not self.items:
            raise IndexError("Pop from empty deque")
        return self.items.pop()

def sliding_window_maximum(nums, k):
    """
    Find maximum in each sliding window using deque.

    Key insight: Maintain deque of indices in decreasing order of values.
    """
    dq = deque()
    result = []

    for i, num in enumerate(nums):
        # Remove indices outside current window
        while dq and dq[0] <= i - k:
            dq.popleft()

        # Remove indices with smaller values (they can't be maximum)
        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        # Add maximum of current window to result
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
```

### 3. Priority Queue (Min/Max Heap)

**Concept**: A queue where elements are served based on priority rather than arrival time.

```python
import heapq

class PriorityQueue:
    """
    Priority queue using Python's heapq (min-heap by default).

    For max-heap behavior, negate the values.
    """

    def __init__(self, max_heap=False):
        self.heap = []
        self.max_heap = max_heap

    def push(self, item, priority):
        """Add item with given priority"""
        # For max-heap, negate priority
        priority = -priority if self.max_heap else priority
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        """Remove and return highest priority item"""
        if not self.heap:
            raise IndexError("Pop from empty priority queue")

        priority, item = heapq.heappop(self.heap)
        # Convert back for max-heap
        priority = -priority if self.max_heap else priority
        return item, priority

    def peek(self):
        """View highest priority item without removing"""
        if not self.heap:
            raise IndexError("Peek from empty priority queue")

        priority, item = self.heap[0]
        priority = -priority if self.max_heap else priority
        return item, priority
```

## Pattern Deep Dive

### Pattern 1: Parentheses and Bracket Matching

This is the **most fundamental** stack pattern - using stack to track nested structures.

#### Basic Parentheses Matching

**Problem Setup**: Check if parentheses in a string are properly matched and nested.

**Key Insight**: Use stack to track opening brackets. When we see a closing bracket, it should match the most recent unmatched opening bracket (top of stack).

```python
def is_valid_parentheses(s):
    """
    Check if parentheses are properly matched.

    Example: s = "({[]})"

    Step 1: '(' → push to stack, stack = ['(']
    Step 2: '{' → push to stack, stack = ['(', '{']
    Step 3: '[' → push to stack, stack = ['(', '{', '[']
    Step 4: ']' → matches '[', pop, stack = ['(', '{']
    Step 5: '}' → matches '{', pop, stack = ['(']
    Step 6: ')' → matches '(', pop, stack = []

    Result: True (stack is empty)
    Time: O(n), Space: O(n)
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        print(f"Processing: '{char}', Stack: {stack}")

        if char in mapping:  # Closing bracket
            if not stack or stack[-1] != mapping[char]:
                print(f"Mismatch: expected '{mapping[char]}' but found '{stack[-1] if stack else 'empty'}'")
                return False
            stack.pop()
            print(f"Matched! Stack after pop: {stack}")
        else:  # Opening bracket
            stack.append(char)
            print(f"Pushed '{char}', Stack: {stack}")

    result = len(stack) == 0
    print(f"Final result: {result} (stack empty: {len(stack) == 0})")
    return result
```

**Why stack is perfect**: We need to match the most recent unmatched opening bracket, which is exactly what stack's LIFO property gives us.

#### Extended Bracket Matching with Context

```python
def validate_nested_structures(s):
    """
    Validate nested structures with additional context tracking.

    Example: Check if HTML-like tags are properly nested
    """
    stack = []

    i = 0
    while i < len(s):
        if s[i] == '<':
            # Find end of tag
            j = i
            while j < len(s) and s[j] != '>':
                j += 1

            if j == len(s):  # No closing >
                return False

            tag = s[i+1:j]

            if tag.startswith('/'):  # Closing tag
                if not stack or stack[-1] != tag[1:]:
                    return False
                stack.pop()
            else:  # Opening tag
                stack.append(tag)

            i = j + 1
        else:
            i += 1

    return len(stack) == 0
```

### Pattern 2: Expression Evaluation and Parsing

#### Infix to Postfix Conversion

**Problem Setup**: Convert mathematical expressions from infix (a + b) to postfix (a b +) notation.

**Key Strategy**: Use stack to manage operator precedence and associativity.

```python
def infix_to_postfix(expression):
    """
    Convert infix expression to postfix using stack.

    Example: "a + b * c" → "a b c * +"

    Algorithm:
    1. If operand → add to output
    2. If operator → pop higher/equal precedence operators, then push
    3. If '(' → push to stack
    4. If ')' → pop until '('

    Precedence: *, / > +, - > (
    """
    def precedence(op):
        prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        return prec.get(op, 0)

    def is_operator(char):
        return char in '+-*/^'

    stack = []
    postfix = []

    for char in expression:
        if char == ' ':
            continue

        print(f"Processing: '{char}', Stack: {stack}, Output: {postfix}")

        if char.isalnum():  # Operand
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            # Pop until opening parenthesis
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            if stack:
                stack.pop()  # Remove '('
        elif is_operator(char):
            # Pop operators with higher or equal precedence
            while (stack and stack[-1] != '(' and
                   precedence(stack[-1]) >= precedence(char)):
                postfix.append(stack.pop())
            stack.append(char)

        print(f"After processing: Stack: {stack}, Output: {postfix}")

    # Pop remaining operators
    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)

def evaluate_postfix(expression):
    """
    Evaluate postfix expression using stack.

    Example: "2 3 +" → 5

    Algorithm: For each token:
    - If number → push to stack
    - If operator → pop two operands, compute, push result
    """
    stack = []

    for token in expression.split():
        if token in '+-*/':
            # Pop two operands (note the order!)
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b

            stack.append(result)
            print(f"Computed: {a} {token} {b} = {result}, Stack: {stack}")
        else:
            # Operand
            stack.append(float(token))
            print(f"Pushed operand: {token}, Stack: {stack}")

    return stack[0] if stack else 0
```

### Pattern 3: BFS with Queues

#### Level-Order Tree Traversal

**Problem Setup**: Visit all nodes in a binary tree level by level.

**Key Insight**: Use queue to process nodes in the order we discover them, ensuring we visit all nodes at depth k before any nodes at depth k+1.

```python
def level_order_traversal(root):
    """
    Level-order traversal using queue.

    Example tree:      1
                     /   \
                    2     3
                   / \   / \
                  4   5 6   7

    Process: 1 → [2,3] → [4,5,6,7]
    Output: [[1], [2,3], [4,5,6,7]]
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        print(f"Processing level with {level_size} nodes")

        # Process all nodes at current level
        for i in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            print(f"  Visiting node: {node.val}")

            # Add children for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)
        print(f"Level complete: {current_level}, Queue size: {len(queue)}")

    return result
```

#### Graph BFS

```python
def bfs_graph(graph, start):
    """
    Breadth-first search in graph using queue.

    Key difference from DFS: Use queue instead of stack/recursion
    """
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)

            # Add neighbors to queue
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return result
```

### Pattern 4: Monotonic Stack Applications

#### Next Greater Element

**Problem Setup**: For each element in array, find the next greater element to its right.

**Key Strategy**: Use monotonic decreasing stack. When we find an element larger than stack top, the stack top has found its next greater element.

```python
def next_greater_element_detailed(nums):
    """
    Find next greater element for each element.

    Example: [2, 1, 2, 4, 3, 1]

    i=0, val=2: stack=[], push 0, stack=[0]
    i=1, val=1: 1<2, push 1, stack=[0,1]
    i=2, val=2: 2>1, nums[1]=1 → next greater is 2
                pop 1, stack=[0]
                2==2, push 2, stack=[0,2]
    i=3, val=4: 4>2, nums[2]=2 → next greater is 4
                pop 2, stack=[0]
                4>2, nums[0]=2 → next greater is 4
                pop 0, stack=[]
                push 3, stack=[3]
    Continue...

    Result: [4, 2, 4, -1, -1, -1]
    """
    stack = []  # Store indices
    result = [-1] * len(nums)

    for i, val in enumerate(nums):
        print(f"Processing index {i}, value {val}")
        print(f"Stack before: {[nums[idx] for idx in stack]} (indices: {stack})")

        # Pop elements smaller than current
        while stack and nums[stack[-1]] < val:
            index = stack.pop()
            result[index] = val
            print(f"  Found next greater for nums[{index}]={nums[index]}: {val}")

        stack.append(i)
        print(f"Stack after: {[nums[idx] for idx in stack]} (indices: {stack})")
        print(f"Result so far: {result}")
        print()

    return result
```

#### Daily Temperatures

**Problem Setup**: Given daily temperatures, find how many days until a warmer temperature.

```python
def daily_temperatures(temperatures):
    """
    Find days until warmer temperature using monotonic stack.

    Similar to next greater element, but return distance instead of value.
    """
    stack = []
    result = [0] * len(temperatures)

    for i, temp in enumerate(temperatures):
        # Pop cooler days and calculate waiting time
        while stack and temperatures[stack[-1]] < temp:
            prev_day = stack.pop()
            result[prev_day] = i - prev_day

        stack.append(i)

    return result
```

## Problem Recognition Guide

Learning to identify when to use stacks vs queues is crucial for efficient problem-solving.

### Stack Problem Indicators

🚨 **"Nested" or "Matching"** → Stack for tracking pairs

- "Valid parentheses", "Balanced brackets"
- "Nested function calls", "HTML tag validation"

🚨 **"Most Recent" or "Last"** → Stack's LIFO nature

- "Most recent unmatched", "Last opened"
- "Undo operations", "Browser back button"

🚨 **"Reverse" or "Backward"** → Stack naturally reverses

- "Reverse string", "Reverse linked list"
- "Postfix evaluation", "Expression parsing"

🚨 **"Next Greater/Smaller"** → Monotonic stack

- "Next greater element", "Daily temperatures"
- "Largest rectangle", "Stock span"

🚨 **"DFS" or "Backtracking"** → Stack for state management

- "Depth-first search", "Maze solving"
- "Generate all combinations", "N-Queens"

### Queue Problem Indicators

🚨 **"Level-by-level" or "Layer"** → Queue for BFS

- "Level-order traversal", "Print by levels"
- "Shortest path", "Minimum steps"

🚨 **"First-come, first-served"** → Queue's FIFO nature

- "Process scheduling", "Task management"
- "First in line", "Serve customers"

🚨 **"BFS" or "Shortest"** → Queue for exploration

- "Breadth-first search", "Shortest path in unweighted graph"
- "Minimum depth", "Steps to reach target"

🚨 **"Streaming" or "Buffer"** → Queue for data flow

- "Moving average", "Sliding window"
- "Producer-consumer", "Data stream"

### Decision-Making Framework

```
What is the access pattern?
├─ Need most recent item → Stack
├─ Need oldest item → Queue
├─ Need both ends → Deque
└─ Need by priority → Priority Queue

What is the traversal pattern?
├─ Depth-first (go deep) → Stack
├─ Breadth-first (go wide) → Queue
├─ Expression evaluation → Stack
└─ Level processing → Queue
```

## Implementation Templates

### Template 1: Basic Stack Operations

```python
def stack_template():
    """Use for: parentheses, expression evaluation, DFS"""
    stack = []

    for item in data:
        if condition_to_push(item):
            stack.append(item)
        elif condition_to_pop(item):
            if stack:  # Always check before popping
                popped = stack.pop()
                process(popped, item)

        # Process current state
        process_current_state(stack)

    # Handle remaining items
    while stack:
        process_remaining(stack.pop())
```

### Template 2: Monotonic Stack

```python
def monotonic_stack_template(arr):
    """Use for: next greater/smaller element problems"""
    stack = []  # Store indices
    result = [-1] * len(arr)

    for i, val in enumerate(arr):
        # Pop elements that violate monotonic property
        while stack and compare(arr[stack[-1]], val):
            index = stack.pop()
            result[index] = val  # Found next greater/smaller

        stack.append(i)

    return result
```

### Template 3: Basic Queue Operations (BFS)

```python
def queue_bfs_template(start):
    """Use for: level-order traversal, shortest path"""
    from collections import deque

    queue = deque([start])
    visited = set([start])

    while queue:
        # Process current level
        level_size = len(queue)

        for _ in range(level_size):
            current = queue.popleft()
            process(current)

            # Add neighbors/children
            for neighbor in get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    return result
```

### Template 4: Expression Evaluation

```python
def expression_evaluation_template(expression):
    """Use for: calculator, expression parsing"""
    operand_stack = []
    operator_stack = []

    for token in expression:
        if is_operand(token):
            operand_stack.append(token)
        elif is_operator(token):
            while (operator_stack and
                   precedence(operator_stack[-1]) >= precedence(token)):
                evaluate_top(operand_stack, operator_stack)
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack[-1] != '(':
                evaluate_top(operand_stack, operator_stack)
            operator_stack.pop()  # Remove '('

    while operator_stack:
        evaluate_top(operand_stack, operator_stack)

    return operand_stack[0]
```

## Complexity Analysis

### Time Complexity

**Stack Operations**:

- **Push**: O(1) - add to end of array/list
- **Pop**: O(1) - remove from end
- **Peek**: O(1) - access last element

**Queue Operations**:

- **Enqueue**: O(1) - with proper implementation (deque, circular array)
- **Dequeue**: O(1) - with proper implementation
- **Front**: O(1) - access first element

**Common Algorithms**:

- **Parentheses matching**: O(n) - single pass
- **Expression evaluation**: O(n) - linear processing
- **BFS traversal**: O(V + E) - visit all vertices and edges
- **Monotonic stack problems**: O(n) - each element pushed/popped once

### Space Complexity

- **Basic operations**: O(1) - constant extra space
- **Stack/Queue storage**: O(n) - proportional to stored elements
- **BFS**: O(w) where w is maximum width of tree/graph
- **DFS with stack**: O(h) where h is maximum depth

## Common Pitfalls & How to Avoid Them

### 1. Empty Stack/Queue Operations

**❌ Wrong**:

```python
# Not checking if empty before popping
item = stack.pop()  # Runtime error if empty!
```

**✅ Correct**:

```python
# Always check before operations
if stack:
    item = stack.pop()
else:
    handle_empty_case()
```

### 2. Queue Implementation Inefficiency

**❌ Wrong**:

```python
# Using list for queue (O(n) dequeue)
queue = []
queue.append(item)      # O(1) enqueue
item = queue.pop(0)     # O(n) dequeue - BAD!
```

**✅ Correct**:

```python
# Using deque for efficient operations
from collections import deque
queue = deque()
queue.append(item)      # O(1) enqueue
item = queue.popleft()  # O(1) dequeue - GOOD!
```

### 3. Monotonic Stack Index Confusion

**❌ Wrong**:

```python
# Storing values instead of indices
while stack and stack[-1] < val:
    stack.pop()  # Lost position information!
```

**✅ Correct**:

```python
# Store indices to track positions
while stack and arr[stack[-1]] < val:
    index = stack.pop()
    result[index] = val  # Can update result array
```

## Practice Framework

### Phase 1: Basic Operations (Week 1)

**Goal**: Master fundamental stack and queue operations.

**Problems to Master**:

1. **Valid Parentheses** - Stack foundation
2. **Implement Queue using Stacks** - Understanding both structures
3. **Min Stack** - Stack with additional functionality
4. **Binary Tree Level Order Traversal** - Queue for BFS

### Phase 2: Advanced Applications (Week 2)

**Goal**: Apply stacks and queues to complex algorithms.

**Problems to Master**:

1. **Daily Temperatures** - Monotonic stack
2. **Evaluate Reverse Polish Notation** - Stack evaluation
3. **Rotting Oranges** - Multi-source BFS with queue
4. **Largest Rectangle in Histogram** - Advanced monotonic stack

### Phase 3: System Design Applications (Week 3)

**Goal**: Understand real-world usage and optimizations.

**Topics to Cover**:

1. **Browser History** - Stack for back/forward
2. **Task Scheduler** - Priority queue applications
3. **Undo/Redo Systems** - Stack-based state management
4. **Stream Processing** - Queue-based buffering

### Testing Strategy

**Essential Test Cases**:

1. **Empty structures**: Operations on empty stack/queue
2. **Single element**: Push/pop, enqueue/dequeue one item
3. **Capacity limits**: Full stack/queue behavior
4. **Alternating operations**: Mixed push/pop sequences
5. **Edge cases**: Unmatched parentheses, empty expressions

## Summary and Key Takeaways

### The Power of Stacks and Queues

**Stacks excel at**:

- **Reversing order**: LIFO naturally reverses
- **Nested structures**: Tracking opening/closing pairs
- **State management**: Undo operations, function calls
- **Expression evaluation**: Operator precedence handling

**Queues excel at**:

- **Fair processing**: First-come, first-served
- **Level-by-level**: BFS traversals
- **Buffering**: Stream processing, producer-consumer
- **Shortest paths**: Unweighted graphs

### Essential Patterns to Master

1. **Parentheses Matching**: Stack for nested structures
2. **Expression Evaluation**: Stack for operator precedence
3. **Monotonic Stack**: Next greater/smaller elements
4. **BFS Traversal**: Queue for level-order processing
5. **State Management**: Stack for undo/redo operations

### When to Choose Each

**Use Stack when**:

- ✅ Need most recently added item
- ✅ Dealing with nested/paired structures
- ✅ Implementing undo functionality
- ✅ Parsing expressions or syntax
- ✅ DFS or backtracking algorithms

**Use Queue when**:

- ✅ Need first-added item (fairness)
- ✅ Processing items level-by-level
- ✅ BFS traversals
- ✅ Streaming or buffering data
- ✅ Shortest path in unweighted graphs

### Problem-Solving Strategy

1. **Identify access pattern**: LIFO vs FIFO
2. **Consider the data flow**: How items enter and leave
3. **Look for keywords**: Nested, matching, level-order, recent
4. **Choose implementation**: Array, linked list, or deque
5. **Handle edge cases**: Empty structures, capacity limits

### Final Practice Tips

- **Visualize the operations**: Draw stack/queue states
- **Practice implementation**: Code basic operations from scratch
- **Master the templates**: Recognize common patterns quickly
- **Test thoroughly**: Empty cases, single elements, edge conditions
- **Understand time/space**: Choose efficient implementations

Stacks and queues are fundamental building blocks that appear in countless algorithms and system designs. Master these patterns, and you'll have powerful tools for solving a wide variety of problems efficiently! 🚀
