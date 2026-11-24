# B+ Tree Deletion

**P3**

## 1. What is the algorithm?

Maintain a dynamic ordered collection with high fanout and all leaves at one depth.

## 2. Problem it solves

Maintain a dynamic ordered collection with high fanout and all leaves at one depth.

## 3. Core intuition

Delete at the leaf, borrow from a sibling or merge if underfull, then refresh separator copies.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Start at the root using the current sorted boundaries.
2. Delete at the leaf, borrow from a sibling or merge if underfull, then refresh separator copies.
3. Update the root if a split or merge changes the tree height.

## 6. Visual example

```text
           [separator]
           /          \
      [lower keys]  [upper keys]
```

## 7. Dry run

With degree two and leaves [1] and [3, 4], deleting 1 borrows 3. The new leaf minima are 3 and 4, so the separator becomes 4.

## 8. Python implementation

Start with `b_plus_tree_delete` in [implementation.py](implementation.py). Update the root if a split or merge changes the tree height.

See the complete [search, split, borrow, and merge code](../../b_plus_tree.py).

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N records, minimum degree t, and height H=O(logₜ(N + 1)), search takes O(H log t) comparisons. Updates take O(t(H + 1)) time with Python list shifts. The index stores O(N) keys and child links.

## 10. Why the algorithm works

Each child covers its own ordered key interval. Splits and merges preserve that order and move leaf depth only when the entire root grows or shrinks.

## 11. When to use it

Maintain a dynamic ordered collection with high fanout and all leaves at one depth.

## 12. When not to use it

A pointer-rich Python tree has overhead. High fanout is especially valuable when one node corresponds to a disk or paging unit.

## 13. Common mistakes

Apply occupancy rules to nonroot nodes and shrink an internal root with only one child after deletion.

## 14. Alternative approaches

B-trees may finish searches at internal keys. B+ trees keep all records in linked leaves for efficient ordered scans.

## 15. Practice problems

**Original exercise · P3.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Delete at the leaf, borrow from a sibling or merge if underfull, then refresh separator copies. Apply occupancy rules to nonroot nodes and shrink an internal root with only one child after deletion.
