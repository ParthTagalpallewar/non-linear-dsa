# Postorder Traversal (Recursive)

**P1**

## 1. What is the algorithm?

Visiting the parent last lets it combine completed child results.

## 2. Problem it solves

Visiting the parent last lets it combine completed child results.

## 3. Core intuition

For each subtree, perform the three local actions in left → right → node order.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Begin with the root and skip absent children.
2. Schedule subtree visits on the call stack.
3. Emit each node at its designated last point.

## 6. Visual example

```text
    1
   / \
  2   3
 /
4
```

## 7. Dry run

The tree with root 1, children 2 and 3, and left grandchild 4 emits [4, 2, 3, 1].

## 8. Python implementation

Start with `postorder_recursive` in [implementation.py](implementation.py). Emit each node at its designated last point.

## 9. Time and space complexity

For N nodes and height H, time is O(N), auxiliary space O(H + 1), and output space O(N).

## 10. Why the algorithm works

Every nonempty subtree contributes exactly one parent value plus its two recursively ordered child sequences. Induction gives the selected traversal order.

## 11. When to use it

Visiting the parent last lets it combine completed child results.

## 12. When not to use it

Use an explicit stack for a skewed tree near Python's recursion limit.

## 13. Common mistakes

Keep emission separate from exploration, and include duplicate values as separate nodes.

## 14. Alternative approaches

For inorder or preorder, Morris traversal can avoid the stack by temporarily changing pointers.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

For each subtree, perform the three local actions in left → right → node order. Keep emission separate from exploration, and include duplicate values as separate nodes.
