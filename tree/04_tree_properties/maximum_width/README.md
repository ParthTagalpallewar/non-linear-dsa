# Maximum Width

**P1**

## 1. What is the algorithm?

Measure the maximum horizontal span of a level, including missing positions.

## 2. Problem it solves

Measure the maximum horizontal span of a level, including missing positions.

## 3. Core intuition

Use complete-tree positions to capture gaps, subtracting the first position of each level before producing child indices.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle a missing root.
2. Use complete-tree positions to capture gaps, subtracting the first position of each level before producing child indices.
3. Return the finalized measurement or predicate.

## 6. Visual example

```text
    1
   / \
  2   3
 /
4
```

## 7. Dry run

If both outer grandchildren exist, their relative positions are 0 and 3. The depth-two span is 4.

## 8. Python implementation

Start with `maximum_width` in [implementation.py](implementation.py). Return the finalized measurement or predicate.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes and maximum number of nodes at a level W, worst-case time is O(N) and queue space O(W). The operation count treats integer index arithmetic as constant time.

## 10. Why the algorithm works

Doubling a parent's position and optionally adding one preserves the complete-tree gap structure. Shifting all positions by the same amount preserves differences.

## 11. When to use it

Measure the maximum horizontal span of a level, including missing positions.

## 12. When not to use it

Inputs must be proper trees without shared children or cycles.

## 13. Common mistakes

Do not use queue length when gaps count toward the width.

## 14. Alternative approaches

An explicit stack can replace recursive traversal when depth is unbounded.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

Use complete-tree positions to capture gaps, subtracting the first position of each level before producing child indices. Do not use queue length when gaps count toward the width.
