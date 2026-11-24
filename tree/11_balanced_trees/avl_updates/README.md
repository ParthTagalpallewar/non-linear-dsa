# AVL Tree Insertion and Deletion

**P2**

## 1. What is the algorithm?

Maintain a dynamic ordered set whose height stays logarithmic.

## 2. Problem it solves

Maintain a dynamic ordered set whose height stays logarithmic.

## 3. Core intuition

Cache subtree heights and repair any node whose child heights differ by more than one.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Follow the BST comparison path to the key or its successor.
2. Cache subtree heights and repair any node whose child heights differ by more than one.
3. Update cached heights after every local mutation and return the repaired root.

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

Start with `avl_updates` in [implementation.py](implementation.py). Update cached heights after every local mutation and return the repaired root.

The complete search, insertion, deletion, and local repair code is in [tree/avl.py](../../avl.py).

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N keys, search and update take O(log(N + 1)) time, with O(log(N + 1)) recursion space and O(N) storage.

## 10. Why the algorithm works

Rotations preserve inorder order. Rebalancing each visited subtree repairs its height before the parent's own balance calculation.

## 11. When to use it

Maintain a dynamic ordered set whose height stays logarithmic.

## 12. When not to use it

An ordinary unbalanced BST is simpler if the key set is small and predictable.

## 13. Common mistakes

A deletion can require repairs at multiple ancestors, so continue all the way to the root.

## 14. Alternative approaches

AVL tends to be more strictly balanced. Red-black trees enforce a looser height condition and are common in ordered maps.

## 15. Practice problems

**Original exercise · P2.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Cache subtree heights and repair any node whose child heights differ by more than one. A deletion can require repairs at multiple ancestors, so continue all the way to the root.
