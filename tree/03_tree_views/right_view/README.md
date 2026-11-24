# Right View

**P1**

## 1. What is the algorithm?

Identify the node visible at each depth from the right side.

## 2. Problem it solves

Identify the node visible at each depth from the right side.

## 3. Core intuition

Visit the right subtree first so its nodes win ties at the same depth.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Push the root at depth zero.
2. Visit the right subtree before the left subtree using stack order.
3. Record a value only when the depth is first seen.

## 6. Visual example

```text
    1
   / \
  2   3
 /
4
```

## 7. Dry run

Depth 0 records 1. Depth 1 records 3. The only depth-2 node is 4, even if it lies on the other side.

## 8. Python implementation

Start with `right_view` in [implementation.py](implementation.py). Record a value only when the depth is first seen.

Run the example from the repository root with `uv run python -m tree.03_tree_views.right_view.implementation`.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes and height H, time is O(N) and auxiliary stack space is O(H + 1).

## 10. Why the algorithm works

For any two nodes at the same depth, the side of their first differing branch determines which is visible. First visit respects that ordering.

## 11. When to use it

Identify the node visible at each depth from the right side.

## 12. When not to use it

This projection groups by depth. Horizontal-distance projections use a different coordinate.

## 13. Common mistakes

Do not follow only one branch, since another branch may extend deeper.

## 14. Alternative approaches

BFS can take the first or last node in each level, using O(W) queue space for maximum width W.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Visit the right subtree first so its nodes win ties at the same depth. Do not follow only one branch, since another branch may extend deeper.
