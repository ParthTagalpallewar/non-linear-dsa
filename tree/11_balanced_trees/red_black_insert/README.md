# Red-Black Tree Insertion

**P3**

## 1. What is the algorithm?

Add a key without sacrificing logarithmic height.

## 2. Problem it solves

Add a key without sacrificing logarithmic height.

## 3. Core intuition

Insert a red leaf, then use rotations and color flips to restore left-leaning red links.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Find the key's search position.
2. Insert a red leaf, then use rotations and color flips to restore left-leaning red links.
3. Keep the repaired root for future operations.

## 6. Visual example

```text
   2
  / \
 1   3
```

## 7. Dry run

Inserting 3, 2, 1 lifts 2 to the root, with 1 left and 3 right.

## 8. Python implementation

Start with `red_black_insert` in [implementation.py](implementation.py). Keep the repaired root for future operations.

Read the [shared implementation](../../red_black.py) and run the [lesson tests](test_implementation.py).

## 9. Time and space complexity

For N keys, O(log(N + 1)) time and stack space. Rotations and color or height updates take constant local work.

## 10. Why the algorithm works

Reaching the update location preserves sorted key order. AVL repair bounds the height gap. Red-black repair preserves the black counts and red-link rules.

## 11. When to use it

Add a key without sacrificing logarithmic height.

## 12. When not to use it

Choose a plain BST if the shape is controlled and balancing metadata is unnecessary.

## 13. Common mistakes

Avoid creating duplicate keys and restore the root after rotations.

## 14. Alternative approaches

AVL balances with cached heights. A red-black tree balances through link colors and black counts.

## 15. Practice problems

**Original exercise · P3.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Insert a red leaf, then use rotations and color flips to restore left-leaning red links. Avoid creating duplicate keys and restore the root after rotations.
