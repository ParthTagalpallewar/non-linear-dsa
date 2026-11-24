# Reverse Level Order Traversal

**P1**

## 1. What is the algorithm?

Return deepest levels first while preserving order within each level.

## 2. Problem it solves

Return deepest levels first while preserving order within each level.

## 3. Core intuition

Build top-down layers with BFS and reverse the layers.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Queue the root.
2. Freeze the current queue length and dequeue exactly that many nodes while appending children.
3. Emit levels in the requested order.

## 6. Visual example

```text
    1
   / \
  2   3
 /
4
```

## 7. Dry run

Queue snapshots at the start of each layer are [1], [2, 3], and [4]. The emitted result is [[4], [2, 3], [1]].

## 8. Python implementation

Start with `reverse_level_order` in [implementation.py](implementation.py). Emit levels in the requested order.

## 9. Time and space complexity

For N nodes and maximum level size W, time is O(N), queue space O(W), and output space O(N).

## 10. Why the algorithm works

At the start of a layer, every queued node has the same depth. Their children are appended after the fixed prefix for the current layer.

## 11. When to use it

Return deepest levels first while preserving order within each level.

## 12. When not to use it

Use DFS when the order must follow one subtree through completion before another.

## 13. Common mistakes

Freeze the layer size before appending children. Keep child enqueue order consistent.

## 14. Alternative approaches

A depth-indexed DFS can gather the same layers using O(H) call-stack space for tree height H.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Build top-down layers with BFS and reverse the layers. Freeze the layer size before appending children. Keep child enqueue order consistent.
