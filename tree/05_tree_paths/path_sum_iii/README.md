# Path Sum III Using Prefix Sums

**P1**

## 1. What is the algorithm?

Count matching downward sums without restarting DFS at every node.

## 2. Problem it solves

Count matching downward sums without restarting DFS at every node.

## 3. Core intuition

A path ending at the current node has sum target exactly when an earlier branch prefix equals current prefix minus target.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle missing nodes or empty input.
2. A path ending at the current node has sum target exactly when an earlier branch prefix equals current prefix minus target.
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

On branch 1→2→4 with target 6, current prefix is 7 and prior prefix 1 yields path [2, 4].

## 8. Python implementation

Start with `path_sum_iii` in [implementation.py](implementation.py). Produce the result from the completed traversal.

## 9. Time and space complexity

For N nodes and height H, expected time is O(N) and space O(H + 1) for active prefixes and stack frames.

## 10. Why the algorithm works

Only ancestors can be the excluded prefix of a downward path. Restoring the count after the subtree removes prefixes that do not belong to sibling branches.

## 11. When to use it

Count matching downward sums without restarting DFS at every node.

## 12. When not to use it

Recursive implementations can reach Python's recursion limit on skewed trees.

## 13. Common mistakes

Look up older prefixes before inserting the current prefix so empty paths are excluded.

## 14. Alternative approaches

An explicit stack avoids using Python call frames.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

A path ending at the current node has sum target exactly when an earlier branch prefix equals current prefix minus target. Look up older prefixes before inserting the current prefix so empty paths are excluded.
