# BST Iterator

**P1**

## 1. What is the algorithm?

Stream sorted keys one at a time without constructing an array.

## 2. Problem it solves

Stream sorted keys one at a time without constructing an array.

## 3. Core intuition

Save the suspended inorder stack across generator yields.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Initialize the search or traversal at the root.
2. Save the suspended inorder stack across generator yields.
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

The first call pushes 4 and 2 and yields 2. Resuming pops and yields 4, then visits 6.

## 8. Python implementation

Start with `bst_iterator` in [implementation.py](implementation.py). Return the selected value or updated result.

Run the example from the repository root with `uv run python -m tree.10_binary_search_tree.bst_iterator.implementation`.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes and height H, full iteration takes O(N) time and O(H + 1) space. Each node is pushed and popped once, so yields cost amortized O(1) over the full scan.

## 10. Why the algorithm works

The next stack pop occurs only after completing that node's left subtree, preserving sorted order.

## 11. When to use it

Stream sorted keys one at a time without constructing an array.

## 12. When not to use it

The algorithm assumes a strict BST with distinct integer keys.

## 13. Common mistakes

Do not mutate the tree while an iterator is active.

## 14. Alternative approaches

AVL or red-black trees keep the search height logarithmic.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Save the suspended inorder stack across generator yields. Do not mutate the tree while an iterator is active.
