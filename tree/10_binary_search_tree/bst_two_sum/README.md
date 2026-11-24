# Two Sum in a BST

**P1**

## 1. What is the algorithm?

Check whether any two distinct tree nodes sum to a target.

## 2. Problem it solves

Check whether any two distinct tree nodes sum to a target.

## 3. Core intuition

For each node, look for its complement among already visited keys.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Initialize the search or traversal at the root.
2. For each node, look for its complement among already visited keys.
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

For target 10, visiting 8 after 2 or 2 after 8 finds the complement.

## 8. Python implementation

Start with `bst_two_sum` in [implementation.py](implementation.py). Return the selected value or updated result.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes, expected time O(N) and auxiliary space O(N) for the set and stack.

## 10. Why the algorithm works

In every valid pair, the second encountered member sees the first in the set.

## 11. When to use it

Check whether any two distinct tree nodes sum to a target.

## 12. When not to use it

The set approach also works on arbitrary binary trees, but its memory can be large.

## 13. Common mistakes

Check the complement before inserting the current value so a node is never reused.

## 14. Alternative approaches

Two opposite-direction BST iterators give O(N) time and O(H) auxiliary space.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

For each node, look for its complement among already visited keys. Check the complement before inserting the current value so a node is never reused.
