# AVL Tree Deletion

**P2**

## 1. What is the algorithm?

Remove a key while retaining logarithmic height.

## 2. Problem it solves

Remove a key while retaining logarithmic height.

## 3. Core intuition

Remove the key using BST deletion, then repair height differences on every ancestor.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Find the key's search position.
2. Remove the key using BST deletion, then repair height differences on every ancestor.
3. Keep the repaired root for future operations.

## 6. Visual example

```text
   2
  / \
 1   3
```

## 7. Dry run

Starting from 2 with children 1 and 3, deleting 2 replaces it with an ordered neighbor. The final set is {1, 3}.

## 8. Python implementation

Start with `avl_delete` in [implementation.py](implementation.py). Keep the repaired root for future operations.

Read the [shared implementation](../../avl.py) and run the [lesson tests](test_implementation.py).

## 9. Time and space complexity

For N keys, O(log(N + 1)) time and stack space. Rotations and color or height updates take constant local work.

## 10. Why the algorithm works

Reaching the update location preserves sorted key order. AVL repair bounds the height gap. Red-black repair preserves the black counts and red-link rules.

## 11. When to use it

Remove a key while retaining logarithmic height.

## 12. When not to use it

Choose a plain BST if the shape is controlled and balancing metadata is unnecessary.

## 13. Common mistakes

Avoid creating duplicate keys and restore the root after rotations.

## 14. Alternative approaches

AVL balances with cached heights. A red-black tree balances through link colors and black counts.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Remove the key using BST deletion, then repair height differences on every ancestor. Avoid creating duplicate keys and restore the root after rotations.
