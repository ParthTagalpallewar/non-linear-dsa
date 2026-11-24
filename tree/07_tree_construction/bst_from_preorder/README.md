# Construct a BST from Preorder

**P1**

## 1. What is the algorithm?

Rebuild a strict BST from one traversal in linear time.

## 2. Problem it solves

Rebuild a strict BST from one traversal in linear time.

## 3. Core intuition

Ancestor comparisons bound the keys allowed in every recursive subtree. Leave a key unread when it belongs outside that interval.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle missing nodes or empty input.
2. Ancestor comparisons bound the keys allowed in every recursive subtree. Leave a key unread when it belongs outside that interval.
3. Produce the result from the completed traversal.

## 6. Visual example

```text
    8
   / \
  5   10
 / \
1   7
```

## 7. Dry run

For [8, 5, 1, 7, 10], the key 7 is outside the bounds for children of 1 but fits between 5 and 8 as 5's right child.

## 8. Python implementation

Start with `bst_from_preorder` in [implementation.py](implementation.py). Produce the result from the completed traversal.

## 9. Time and space complexity

For N nodes and height H, worst-case time is O(N) and auxiliary space O(H + 1), excluding output.

## 10. Why the algorithm works

Preorder provides each subtree root first. Its bound checks identify the entire contiguous prefix that can belong to that subtree.

## 11. When to use it

Rebuild a strict BST from one traversal in linear time.

## 12. When not to use it

Recursive implementations can reach Python's recursion limit on skewed trees.

## 13. Common mistakes

Check that all input was consumed to catch inconsistent order and duplicates.

## 14. Alternative approaches

Repeated insertions are straightforward but can cost O(N²) on sorted input.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Ancestor comparisons bound the keys allowed in every recursive subtree. Leave a key unread when it belongs outside that interval. Check that all input was consumed to catch inconsistent order and duplicates.
