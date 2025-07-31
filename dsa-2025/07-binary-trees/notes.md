# Binary Trees - Study Notes

## Core Concept

A Binary Tree is a hierarchical data structure where each node has at most two children, referred to as left and right child. It's fundamental for many algorithms and data structures.

## Basic Structure

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

## Types of Binary Trees

### 1. Full Binary Tree

- **Definition**: Every node has either 0 or 2 children
- **Properties**: No node has exactly one child

### 2. Complete Binary Tree

- **Definition**: All levels filled except possibly the last, which is filled left to right
- **Properties**: Optimal for heap implementation

### 3. Perfect Binary Tree

- **Definition**: All internal nodes have 2 children, all leaves at same level
- **Properties**: Has 2^h - 1 nodes where h is height

### 4. Balanced Binary Tree

- **Definition**: Height difference between left and right subtrees ≤ 1 for all nodes
- **Properties**: Ensures O(log n) operations

## Tree Traversals

### 1. Depth-First Search (DFS)

#### Inorder Traversal (Left → Root → Right)

```python
def inorder_traversal(root):
    result = []

    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

    inorder(root)
    return result

# Iterative version
def inorder_iterative(root):
    result, stack = [], []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.val)
        current = current.right

    return result
```

#### Preorder Traversal (Root → Left → Right)

```python
def preorder_traversal(root):
    result = []

    def preorder(node):
        if node:
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)

    preorder(root)
    return result

# Iterative version
def preorder_iterative(root):
    if not root:
        return []

    result, stack = [], [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result
```

#### Postorder Traversal (Left → Right → Root)

```python
def postorder_traversal(root):
    result = []

    def postorder(node):
        if node:
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)

    postorder(root)
    return result

# Iterative version (more complex)
def postorder_iterative(root):
    if not root:
        return []

    result, stack = [], []
    last_visited = None
    current = root

    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            peek_node = stack[-1]
            if peek_node.right and last_visited != peek_node.right:
                current = peek_node.right
            else:
                result.append(peek_node.val)
                last_visited = stack.pop()

    return result
```

### 2. Breadth-First Search (BFS)

#### Level Order Traversal

```python
from collections import deque

def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = deque([root])

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

## Common Patterns and Algorithms

### Pattern 1: Tree Properties

```python
# Calculate height/depth
def max_depth(root):
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# Check if balanced
def is_balanced(root):
    def height(node):
        if not node:
            return 0

        left_height = height(node.left)
        if left_height == -1:
            return -1

        right_height = height(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return 1 + max(left_height, right_height)

    return height(root) != -1
```

### Pattern 2: Path Problems

```python
# Binary tree paths
def binary_tree_paths(root):
    if not root:
        return []

    paths = []

    def dfs(node, path):
        if not node.left and not node.right:  # leaf node
            paths.append(path)
            return

        if node.left:
            dfs(node.left, path + "->" + str(node.left.val))
        if node.right:
            dfs(node.right, path + "->" + str(node.right.val))

    dfs(root, str(root.val))
    return paths

# Path sum
def has_path_sum(root, target_sum):
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == target_sum

    return (has_path_sum(root.left, target_sum - root.val) or
            has_path_sum(root.right, target_sum - root.val))
```

### Pattern 3: Tree Construction

```python
# Build tree from inorder and preorder
def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])

    root.left = build_tree(preorder[1:mid+1], inorder[:mid])
    root.right = build_tree(preorder[mid+1:], inorder[mid+1:])

    return root
```

### Pattern 4: Tree Modification

```python
# Invert binary tree
def invert_tree(root):
    if not root:
        return None

    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)

    return root

# Flatten to linked list
def flatten(root):
    def flatten_helper(node):
        if not node:
            return None

        if not node.left and not node.right:
            return node

        left_tail = flatten_helper(node.left)
        right_tail = flatten_helper(node.right)

        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None

        return right_tail if right_tail else left_tail

    flatten_helper(root)
```

## Advanced Concepts

### 1. Lowest Common Ancestor (LCA)

```python
def lowest_common_ancestor(root, p, q):
    if not root or root == p or root == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root

    return left if left else right
```

### 2. Diameter of Tree

```python
def diameter_of_binary_tree(root):
    self.diameter = 0

    def depth(node):
        if not node:
            return 0

        left_depth = depth(node.left)
        right_depth = depth(node.right)

        self.diameter = max(self.diameter, left_depth + right_depth)

        return 1 + max(left_depth, right_depth)

    depth(root)
    return self.diameter
```

### 3. Serialize and Deserialize

```python
def serialize(root):
    def preorder(node):
        if node:
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        else:
            vals.append("#")

    vals = []
    preorder(root)
    return ",".join(vals)

def deserialize(data):
    def build():
        val = next(vals)
        if val == "#":
            return None

        node = TreeNode(int(val))
        node.left = build()
        node.right = build()
        return node

    vals = iter(data.split(","))
    return build()
```

## When to Use Different Approaches

### Recursion vs Iteration:

- **Recursion**: Cleaner code, natural for tree problems
- **Iteration**: Better space complexity (no call stack), avoids stack overflow

### DFS vs BFS:

- **DFS**: Path problems, tree properties, modification
- **BFS**: Level-based problems, shortest path, complete traversal

### Traversal Choice:

- **Inorder**: BST operations, sorted output
- **Preorder**: Tree copying, prefix expressions
- **Postorder**: Tree deletion, postfix expressions
- **Level Order**: Level-based processing, printing by levels

## Time and Space Complexity

### Traversals:

- **Time**: O(n) for all traversals
- **Space**:
  - Recursive: O(h) where h is height
  - Iterative: O(h) for stack/queue
  - Level order: O(w) where w is maximum width

### Common Operations:

| Operation | Time | Space |
| --------- | ---- | ----- |
| Search    | O(n) | O(h)  |
| Insert    | O(n) | O(h)  |
| Delete    | O(n) | O(h)  |
| Traversal | O(n) | O(h)  |

## Problem-Solving Strategies

### 1. Identify the Pattern:

- **Single node processing**: Properties, validation
- **Path-based**: Root to leaf, path sum
- **Subtree-based**: Diameter, LCA
- **Level-based**: Level order, zigzag

### 2. Choose Traversal Method:

- **Top-down**: Process node first, then children
- **Bottom-up**: Process children first, then node
- **Level-by-level**: BFS for level-based problems

### 3. Handle Edge Cases:

- Empty tree (root is None)
- Single node tree
- Unbalanced trees
- Duplicate values

### 4. Optimize:

- Use iteration to save space
- Early termination when possible
- Memoization for repeated subproblems

## Common Mistakes to Avoid

1. **Null pointer exceptions**: Always check if node exists
2. **Incorrect base cases**: Handle empty tree properly
3. **Wrong traversal choice**: Match traversal to problem requirement
4. **Stack overflow**: Use iteration for very deep trees
5. **Modifying during traversal**: Be careful with tree modifications
