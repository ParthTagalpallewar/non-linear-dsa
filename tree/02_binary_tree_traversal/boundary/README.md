# Boundary Traversal

**P1**

## 1. What is the algorithm?

Trace the outside nodes of a binary tree anticlockwise.

## 2. Problem it solves

Trace the outside nodes of a binary tree anticlockwise.

## 3. Core intuition

The boundary breaks into disjoint sections: root, left exterior, leaves, then right exterior reversed.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Emit the root once.
2. Follow the left-side path, preferring a left child, and emit nonleaves.
3. Emit leaves left to right, then append the reversed right-side nonleaves.

## 6. Visual example

```text
    1
   / \
  2   3
 /
4
```

## 7. Dry run

From the example, append root 1, left internal node 2, and leaves 4 and 3.

## 8. Python implementation

Start with `boundary` in [implementation.py](implementation.py). Emit leaves left to right, then append the reversed right-side nonleaves.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes and height H, time is O(N) and auxiliary space O(H + 1) excluding the result.

## 10. Why the algorithm works

The two side walks start in different subtrees, and both exclude leaves. The leaf pass covers every remaining outline node exactly once.

## 11. When to use it

Trace the outside nodes of a binary tree anticlockwise.

## 12. When not to use it

A level-wise extreme view is a different projection.

## 13. Common mistakes

Skip the root during the leaf pass and reverse only the right boundary.

## 14. Alternative approaches

An iterative leaf walk replaces recursion when skewed trees are expected.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

The boundary breaks into disjoint sections: root, left exterior, leaves, then right exterior reversed. Skip the root during the leaf pass and reverse only the right boundary.
