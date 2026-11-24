# N-ary Tree Traversal

**P1**

## 1. What is the algorithm?

Visit every node of an ordered multiway tree.

## 2. Problem it solves

Visit every node of an ordered multiway tree.

## 3. Core intuition

Schedule children in reverse order on a LIFO stack so the first child is visited first.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Push the root when present.
2. Pop and yield one node.
3. Push its children in reverse order, repeating until the stack is empty.

## 6. Visual example

```text
    1
  / | \
 2  3  4
 |
 5
```

## 7. Dry run

After visiting 1, push [4, 3, 2]. Visiting 2 pushes 5 above 3 and 4.

## 8. Python implementation

Start with `nary_traversal` in [implementation.py](implementation.py). Push its children in reverse order, repeating until the stack is empty.

## 9. Time and space complexity

For N nodes, time O(N) and worst-case stack O(N), since a single parent can have N−1 children.

## 10. Why the algorithm works

The stack completes each child subtree before its siblings. Pushing in reverse preserves the tree's declared sibling order.

## 11. When to use it

Visit every node of an ordered multiway tree.

## 12. When not to use it

Use breadth-first traversal if levels must remain together.

## 13. Common mistakes

Reverse the order of pushes rather than modifying the node's actual child list.

## 14. Alternative approaches

A stack of child iterators can use O(H) space for tree height H.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Schedule children in reverse order on a LIFO stack so the first child is visited first. Reverse the order of pushes rather than modifying the node's actual child list.
