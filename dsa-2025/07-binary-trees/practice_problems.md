# Binary Trees - Practice Problems

## Problem 1: Binary Tree Inorder Traversal

**Difficulty**: Easy

**Description**: Return inorder traversal of binary tree (left → root → right).

**Example**:

```
Input: [1,null,2,3]
Output: [1,3,2]
```

**Hint**: Use recursion or stack-based iteration.

---

## Problem 2: Binary Tree Preorder Traversal

**Difficulty**: Easy

**Description**: Return preorder traversal of binary tree (root → left → right).

**Example**:

```
Input: [1,null,2,3]
Output: [1,2,3]
```

**Hint**: Use recursion or stack, process root first.

---

## Problem 3: Binary Tree Postorder Traversal

**Difficulty**: Easy

**Description**: Return postorder traversal of binary tree (left → right → root).

**Example**:

```
Input: [1,null,2,3]
Output: [3,2,1]
```

**Hint**: Use recursion or modified stack approach.

---

## Problem 4: Maximum Depth of Binary Tree

**Difficulty**: Easy

**Description**: Find maximum depth (height) of binary tree.

**Example**:

```
Input: [3,9,20,null,null,15,7]
Output: 3
```

**Hint**: Use recursion - 1 + max(left_depth, right_depth).

---

## Problem 5: Same Tree

**Difficulty**: Easy

**Description**: Check if two binary trees are identical.

**Example**:

```
Input: p = [1,2,3], q = [1,2,3]
Output: True
```

**Hint**: Recursively compare values and structure.

---

## Problem 6: Invert Binary Tree

**Difficulty**: Easy

**Description**: Invert/flip binary tree (swap left and right children).

**Example**:

```
Input: [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
```

**Hint**: Recursively swap left and right children.

---

## Problem 7: Symmetric Tree

**Difficulty**: Easy

**Description**: Check if binary tree is symmetric around its center.

**Example**:

```
Input: [1,2,2,3,4,4,3]
Output: True
```

**Hint**: Compare left subtree with mirrored right subtree.

---

## Problem 8: Binary Tree Level Order Traversal

**Difficulty**: Medium

**Description**: Return level order traversal as list of lists.

**Example**:

```
Input: [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
```

**Hint**: Use BFS with queue, process one level at a time.

---

## Problem 9: Minimum Depth of Binary Tree

**Difficulty**: Easy

**Description**: Find minimum depth (shortest path to leaf).

**Example**:

```
Input: [3,9,20,null,null,15,7]
Output: 2
```

**Hint**: Use BFS for optimal solution, or DFS with careful handling.

---

## Problem 10: Balanced Binary Tree

**Difficulty**: Easy

**Description**: Check if binary tree is height-balanced.

**Example**:

```
Input: [3,9,20,null,null,15,7]
Output: True
```

**Hint**: Check if height difference between subtrees ≤ 1 for all nodes.

---

## Problem 11: Binary Tree Paths

**Difficulty**: Easy

**Description**: Return all root-to-leaf paths.

**Example**:

```
Input: [1,2,3,null,5]
Output: ["1->2->5","1->3"]
```

**Hint**: Use DFS with path tracking, backtrack after processing.

---

## Problem 12: Path Sum

**Difficulty**: Easy

**Description**: Check if there's root-to-leaf path with given sum.

**Example**:

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: True
```

**Hint**: DFS with running sum, check at leaf nodes.

---

## Problem 13: Sum of Left Leaves

**Difficulty**: Easy

**Description**: Find sum of all left leaves in binary tree.

**Example**:

```
Input: [3,9,20,null,null,15,7]
Output: 24 (9 + 15)
```

**Hint**: Track if current node is left child and leaf.

---

## Problem 14: Diameter of Binary Tree

**Difficulty**: Easy

**Description**: Find diameter (longest path between any two nodes).

**Example**:

```
Input: [1,2,3,4,5]
Output: 3 (path 4->2->1->3 or 5->2->1->3)
```

**Hint**: For each node, diameter = left_height + right_height.

---

## Problem 15: Binary Tree Zigzag Level Order Traversal

**Difficulty**: Medium

**Description**: Return zigzag level order (left-to-right, then right-to-left alternating).

**Example**:

```
Input: [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
```

**Hint**: Use BFS, reverse alternate levels.

---

## Problem 16: Construct Binary Tree from Preorder and Inorder

**Difficulty**: Medium

**Description**: Build binary tree from preorder and inorder traversal arrays.

**Example**:

```
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
```

**Hint**: First element in preorder is root, find it in inorder to split.

---

## Problem 17: Validate Binary Search Tree

**Difficulty**: Medium

**Description**: Check if binary tree is valid BST.

**Example**:

```
Input: [2,1,3]
Output: True
```

**Hint**: Use inorder traversal (should be sorted) or range validation.

---

## Problem 18: Lowest Common Ancestor of Binary Tree

**Difficulty**: Medium

**Description**: Find lowest common ancestor of two nodes.

**Example**:

```
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
```

**Hint**: If both nodes found in different subtrees, current node is LCA.

---

## Solving Strategy for Binary Tree Problems

### Step-by-Step Approach:

1. **Understand the problem**: What needs to be computed/found?
2. **Choose traversal method**: DFS (recursion/iteration) or BFS
3. **Identify the pattern**: Single node, path-based, subtree-based, level-based
4. **Handle base cases**: Empty tree, single node, leaf nodes
5. **Implement and test**: Start with simple cases

### Common Patterns:

- **Tree Properties**: Height, balance, symmetry
- **Traversals**: Different orders for different purposes
- **Path Problems**: Root-to-leaf paths, path sums
- **Construction**: Build tree from traversals
- **Modification**: Invert, flatten, prune

### Key Insights:

- **Recursion is natural**: Trees have recursive structure
- **Base case first**: Handle null nodes and leaves
- **Process vs collect**: Some problems process nodes, others collect results
- **Level processing**: BFS when levels matter

### Testing Tips:

1. **Empty tree**: `root = None`
2. **Single node**: Just root
3. **Linear tree**: All nodes in one direction
4. **Complete tree**: Full balanced tree
5. **Edge cases**: Duplicate values, negative numbers
