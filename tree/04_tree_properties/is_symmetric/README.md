# Symmetric Tree Check

**P1**

## 1. What is the algorithm?

Check whether the two sides of a tree are mirror images.

## 2. Problem it solves

Check whether the two sides of a tree are mirror images.

## 3. Core intuition

Compare node pairs and schedule corresponding child positions with left and right exchanged across the reflection.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle a missing root.
2. Compare node pairs and schedule corresponding child positions with left and right exchanged across the reflection.
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

Pair the first corresponding nodes. If both contain 2, continue to their children. Encountering one missing child and one present child rejects the comparison.

## 8. Python implementation

Start with `is_symmetric` in [implementation.py](implementation.py). Return the finalized measurement or predicate.

## 9. Time and space complexity

For N inspected node pairs and maximum compared height H, time is O(N + 1) and stack space O(H + 1). A root mismatch stops in O(1).

## 10. Why the algorithm works

Every stack entry is a pair that must agree under the required position mapping. Equal values and compatible children are necessary and sufficient.

## 11. When to use it

Check whether the two sides of a tree are mirror images.

## 12. When not to use it

Inputs must be proper trees without shared children or cycles.

## 13. Common mistakes

Comparing traversal value sequences alone can confuse different shapes.

## 14. Alternative approaches

An explicit stack can replace recursive traversal when depth is unbounded.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Compare node pairs and schedule corresponding child positions with left and right exchanged across the reflection. Comparing traversal value sequences alone can confuse different shapes.
