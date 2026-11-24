# Prüfer Sequence Decoding

**P3**

## 1. What is the algorithm?

Rebuild a labeled tree from its compact Prüfer code.

## 2. Problem it solves

Rebuild a labeled tree from its compact Prüfer code.

## 3. Core intuition

Every vertex appears in the remaining code exactly its remaining degree minus one, so labels absent from that suffix are current leaves.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Initialize all degrees to one and add occurrence counts.
2. Connect the smallest leaf to the next code label and decrement that neighbor's degree.
3. Join the two remaining leaves.

## 6. Visual example

```text
    0
   / \
  1   2
 / \
3   4
```

## 7. Dry run

For [0, 1, 1], degrees are [2, 3, 1, 1, 1]. Connect 2—0, then 0—1, then 3—1. Finally join 1—4.

## 8. Python implementation

Start with `prufer_decode` in [implementation.py](implementation.py). Join the two remaining leaves.

Run the example from the repository root with `uv run python -m tree.19_advanced_trees.prufer_decode.implementation`.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N decoded vertices, time O(N log N), with O(N) auxiliary and output storage.

## 10. Why the algorithm works

The degree rule identifies the exact leaf that encoding would have removed. Each reconstructed link reattaches one leaf without creating a cycle.

## 11. When to use it

Rebuild a labeled tree from its compact Prüfer code.

## 12. When not to use it

The sequence labels must be within 0 through N−1. This format does not carry edge weights.

## 13. Common mistakes

Use N=len(code)+2, and insert a neighbor into the heap only when its degree reaches one.

## 14. Alternative approaches

A monotone leaf pointer gives a linear-time decoder for dense integer labels.

## 15. Practice problems

**Original exercise · P3.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Every vertex appears in the remaining code exactly its remaining degree minus one, so labels absent from that suffix are current leaves. Use N=len(code)+2, and insert a neighbor into the heap only when its degree reaches one.
