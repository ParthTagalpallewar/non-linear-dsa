# Recover Binary Search Tree

**P1**

## 1. What is the algorithm?

Restore search order after exchanging two otherwise valid node values.

## 2. Problem it solves

Restore search order after exchanging two otherwise valid node values.

## 3. Core intuition

Find adjacent descents in inorder. Keep the first descent's predecessor and the last descent's current node.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Initialize the search or traversal at the root.
2. Find adjacent descents in inorder. Keep the first descent's predecessor and the last descent's current node.
3. Return the selected value or updated result.

## 6. Visual example

```text
    4
   / \
  2   6
 / \   \
1   3   8
```

## 7. Dry run

If inorder becomes [1, 6, 3, 4, 2, 8], descents 6>3 and 4>2 identify keys 6 and 2.

## 8. Python implementation

Start with `recover_bst` in [implementation.py](implementation.py). Return the selected value or updated result.

## 9. Time and space complexity

For N nodes and height H, time is O(N) and auxiliary space O(H + 1).

## 10. Why the algorithm works

A single swap creates one adjacent descent for adjacent values or two for nonadjacent values. The swapped keys are the outer endpoints of the descents.

## 11. When to use it

Restore search order after exchanging two otherwise valid node values.

## 12. When not to use it

The tree must already be valid or differ by precisely one swap of two distinct values.

## 13. Common mistakes

The second candidate must update on each descent, including the first.

## 14. Alternative approaches

Morris inorder can recover the same two values with O(1) auxiliary space.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Find adjacent descents in inorder. Keep the first descent's predecessor and the last descent's current node. The second candidate must update on each descent, including the first.
