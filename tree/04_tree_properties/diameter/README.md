# Diameter of a Binary Tree

**P1**

## 1. What is the algorithm?

Measure the longest simple path between any two nodes.

## 2. Problem it solves

Measure the longest simple path between any two nodes.

## 3. Core intuition

Try every node as the path's highest point and combine its two best downward arms.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle a missing root.
2. Try every node as the path's highest point and combine its two best downward arms.
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

Node 2 combines a one-edge arm to 4 and no right arm. Node 1 combines two edges down to 4 and one to 3 for length three.

## 8. Python implementation

Start with `diameter` in [implementation.py](implementation.py). Return the finalized measurement or predicate.

## 9. Time and space complexity

For N nodes and tree height H, time is O(N) and stack space O(H + 1).

## 10. Why the algorithm works

Every simple path has a unique lowest common ancestor of its endpoints. Its two arms can be optimized independently.

## 11. When to use it

Measure the longest simple path between any two nodes.

## 12. When not to use it

Inputs must be proper trees without shared children or cycles.

## 13. Common mistakes

Return a single downward arm to the parent, while tracking two-arm candidates separately.

## 14. Alternative approaches

An explicit stack can replace recursive traversal when depth is unbounded.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Try every node as the path's highest point and combine its two best downward arms. Return a single downward arm to the parent, while tracking two-arm candidates separately.
