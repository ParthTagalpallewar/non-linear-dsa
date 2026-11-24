# Prüfer Sequence Encoding

**P3**

## 1. What is the algorithm?

Encode an N-vertex labeled tree as N−2 integer labels.

## 2. Problem it solves

Encode an N-vertex labeled tree as N−2 integer labels.

## 3. Core intuition

Repeatedly remove the smallest leaf and record its sole remaining neighbor.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Compute degrees and heapify all leaf labels.
2. Remove the smallest leaf, append its active neighbor, and update degrees.
3. Stop when two vertices remain.

## 6. Visual example

```text
    0
   / \
  1   2
 / \
3   4
```

## 7. Dry run

Leaves start [2, 3, 4]. Remove 2 and write 0. Now remove 0 and write 1. Remove 3 and write 1. The sequence is [0, 1, 1].

## 8. Python implementation

Start with `prufer_encode` in [implementation.py](implementation.py). Stop when two vertices remain.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N vertices, time O(N log N) and auxiliary space O(N). Across all removals, scanning the original adjacency rows touches O(N) entries.

## 10. Why the algorithm works

Only the neighbor's degree changes, so the heap contains exactly all current leaves. The deterministic smallest-leaf rule makes the encoding invertible.

## 11. When to use it

Encode an N-vertex labeled tree as N−2 integer labels.

## 12. When not to use it

The classic sequence format is defined here for N≥2. The empty sequence represents the two-vertex tree.

## 13. Common mistakes

Do not output the final edge, and ignore neighbors already removed.

## 14. Alternative approaches

A monotone leaf pointer can avoid a heap when labels are exactly 0 through N−1.

## 15. Practice problems

**Original exercise · P3.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Repeatedly remove the smallest leaf and record its sole remaining neighbor. Do not output the final edge, and ignore neighbors already removed.
