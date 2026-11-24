# Right Rotation

**P2**

## 1. What is the algorithm?

Repair a local search-tree imbalance without reordering keys.

## 2. Problem it solves

Repair a local search-tree imbalance without reordering keys.

## 3. Core intuition

Lift the left child. Move its right subtree to the old root's left.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Identify the pivot and required child links.
2. Lift the left child. Move its right subtree to the old root's left.
3. Refresh heights from the lower pivot upward and return the new root.

## 6. Visual example

```text
Before: root 3, branch bends toward key 2
After:       2
            / \
           1   3
```

## 7. Dry run

Starting with root 3, the rotation places 2 above children 1 and 3.

## 8. Python implementation

Start with `rotate_right` in [implementation.py](implementation.py). Refresh heights from the lower pivot upward and return the new root.

## 9. Time and space complexity

One or two rotations touch a constant number of nodes, so time and auxiliary space are O(1).

## 10. Why the algorithm works

All transferred keys lie between the two pivots. The middle subtree can therefore move to the opposite side of its original parent while retaining BST order.

## 11. When to use it

Repair a local search-tree imbalance without reordering keys.

## 12. When not to use it

Use the appropriate rotation for the child shape. A missing pivot child is an error.

## 13. Common mistakes

Assign the return value back into the parent's child slot or tree root.

## 14. Alternative approaches

For an inner-heavy branch, a double rotation first changes it into the outer-heavy case.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Lift the left child. Move its right subtree to the old root's left. Assign the return value back into the parent's child slot or tree root.
