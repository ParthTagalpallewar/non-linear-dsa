# Mirror Binary Tree

**P1**

## 1. What is the algorithm?

Reflect a binary tree horizontally.

## 2. Problem it solves

Reflect a binary tree horizontally.

## 3. Core intuition

Copy each node while crossing the two child positions.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle missing nodes or empty input.
2. Copy each node while crossing the two child positions.
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

Root 1 still has value 1. Child 2 moves right, child 3 moves left, and node 4 becomes the right child of 2.

## 8. Python implementation

Start with `mirror_tree` in [implementation.py](implementation.py). Produce the result from the completed traversal.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes and height H, worst-case time is O(N) and auxiliary space O(H + 1), excluding output.

## 10. Why the algorithm works

A reflected path exchanges left with right at every step. The transformation visits each node once and applies exactly that exchange.

## 11. When to use it

Reflect a binary tree horizontally.

## 12. When not to use it

Requires a proper tree. Shared descendants would be copied independently.

## 13. Common mistakes

Use a separate node if callers expect the original references to keep their old positions.

## 14. Alternative approaches

An in-place inversion avoids allocating new nodes.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Copy each node while crossing the two child positions. Use a separate node if callers expect the original references to keep their old positions.
