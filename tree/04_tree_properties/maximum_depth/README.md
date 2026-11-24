# Maximum Depth

**P1**

## 1. What is the algorithm?

Compute the longest root-to-leaf depth in nodes.

## 2. Problem it solves

Compute the longest root-to-leaf depth in nodes.

## 3. Core intuition

BFS visits nodes in increasing depth, so the last processed node determines the answer.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle a missing root.
2. BFS visits nodes in increasing depth, so the last processed node determines the answer.
3. Return the finalized measurement or predicate.

## 6. Visual example

```text
    1
   / \
  2   3
 /
4
```

## 7. Dry run

The reported depths of nodes 1, 2, 3, 4 are 1, 2, 2, 3. The last node is 4, so the answer is 3.

## 8. Python implementation

Start with `maximum_depth` in [implementation.py](implementation.py). Return the finalized measurement or predicate.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes and maximum number of nodes at a level W, worst-case time is O(N) and queue space O(W).

## 10. Why the algorithm works

A node enters the queue only through its parent, so its recorded depth is exact and queue order is nondecreasing.

## 11. When to use it

Compute the longest root-to-leaf depth in nodes.

## 12. When not to use it

Inputs must be proper trees without shared children or cycles.

## 13. Common mistakes

Depth here counts nodes and a leaf has no children. A missing child does not define a root-to-leaf route.

## 14. Alternative approaches

An explicit stack can replace recursive traversal when depth is unbounded.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

BFS visits nodes in increasing depth, so the last processed node determines the answer. Depth here counts nodes and a leaf has no children. A missing child does not define a root-to-leaf route.
