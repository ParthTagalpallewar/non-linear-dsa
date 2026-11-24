# Flood Fill

**P1**

## 1. What is the algorithm?

Flood fill recolors every pixel connected to a seed through pixels of its original color.

## 2. Problem it solves

Implement a paint-bucket tool or label one connected region.

## 3. Core intuition

Recolor on discovery so the image doubles as the visited structure.

## 4. Prerequisites

A rectangular grid, four-way adjacency, and stack-based traversal.

## 5. How it works

1. Read the seed's original color.
2. Recolor the seed and push its coordinates.
3. Recolor and push each matching neighbor before continuing.

## 6. Visual example

```text
1 1 0
1 0 1
```

## 7. Dry run

From (0, 0), the stack receives (1, 0) and (0, 1). The lower-right 1 has no connecting path and stays unchanged.

## 8. Python implementation

Start with `flood_fill` in [implementation.py](implementation.py). Recolor and push each matching neighbor before continuing.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For R rows and C columns, the worst case is O(RC) time and O(RC) auxiliary space. Each reached cell has at most four neighbors. If the color stays the same, the function returns in O(1).

## 10. Why the algorithm works

Each pushed pixel matches the original color and extends a path from the seed. Traversal checks every border of the reached region.

## 11. When to use it

Implement a paint-bucket tool or label one connected region.

## 12. When not to use it

Copy the image first when the caller needs to preserve its original contents.

## 13. Common mistakes

Return immediately when the replacement is equal to the original color.

## 14. Alternative approaches

BFS with a queue fills the same region. An explicit visited set allows traversal without recoloring during discovery.

## 15. Practice problems

- LeetCode #733, Easy. Traversal of one equal-color region. [Flood Fill](https://leetcode.com/problems/flood-fill/)

**Original exercise · P1.** Add an option for diagonal connectivity and compare results on a checkerboard.

## 16. Interview revision notes

Recolor on discovery so the image doubles as the visited structure. Return immediately when the replacement is equal to the original color.
