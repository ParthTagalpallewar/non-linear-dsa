# Red-Black Tree

**P3**

## 1. What is the algorithm?

Maintain a dynamic ordered set whose height stays logarithmic.

## 2. Problem it solves

Maintain a dynamic ordered set whose height stays logarithmic.

## 3. Core intuition

Store the color of each incoming edge and represent three-nodes with left red links.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Follow the BST comparison path to the key or its successor.
2. Store the color of each incoming edge and represent three-nodes with left red links.
3. Repair ancestors on the return path and restore a black root.

## 6. Visual example

```text
3            2
/     →      / \
2            1   3
/
1
```

## 7. Dry run

Insert 3, then 2, then 1. Repair lifts 2 to the root and orders 1 left and 3 right. Deleting 3 then retains keys 1 and 2.

## 8. Python implementation

Start with `red_black_tree` in [implementation.py](implementation.py). Repair ancestors on the return path and restore a black root.

The complete search, insertion, deletion, and local repair code is in [tree/red_black.py](../../red_black.py).

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N keys, search and update take O(log(N + 1)) time, with O(log(N + 1)) recursion space and O(N) storage.

## 10. Why the algorithm works

Equal black counts and no consecutive red links bound total height. Red moves and flips preserve black counts while opening a branch for an update.

## 11. When to use it

Maintain a dynamic ordered set whose height stays logarithmic.

## 12. When not to use it

An ordinary unbalanced BST is simpler if the key set is small and predictable.

## 13. Common mistakes

Use both a clean membership policy for absent deletions and root recoloring after updates.

## 14. Alternative approaches

AVL tends to be more strictly balanced. Red-black trees enforce a looser height condition and are common in ordered maps.

## 15. Practice problems

**Original exercise · P3.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Store the color of each incoming edge and represent three-nodes with left red links. Use both a clean membership policy for absent deletions and root recoloring after updates.
