# Kth Ancestor of a Node

**P1**

## 1. What is the algorithm?

Return the ancestor a fixed number of edges above a node.

## 2. Problem it solves

Return the ancestor a fixed number of edges above a node.

## 3. Core intuition

Follow the unique parent pointer once per step.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle missing nodes or empty input.
2. Follow the unique parent pointer once per step.
3. Produce the result from the completed traversal.

## 6. Visual example

```text
    1
   / \
  2   3
 /
4
```

## 7. Dry run

From node 4, one step reaches node 2 and two steps reach node 1. A third step has no ancestor.

## 8. Python implementation

Start with `kth_ancestor` in [implementation.py](implementation.py). Produce the result from the completed traversal.

## 9. Time and space complexity

For N nodes, worst-case time and auxiliary space are O(N) due to parent indexing.

## 10. Why the algorithm works

After i iterations the cursor is precisely i parent links from the start, if that node exists.

## 11. When to use it

Return the ancestor a fixed number of edges above a node.

## 12. When not to use it

Recursive implementations can reach Python's recursion limit on skewed trees.

## 13. Common mistakes

Treat k=0 as the queried node itself and handle k larger than its depth.

## 14. Alternative approaches

Binary lifting replaces linear climbing with logarithmic jumps.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Follow the unique parent pointer once per step. Treat k=0 as the queried node itself and handle k larger than its depth.
