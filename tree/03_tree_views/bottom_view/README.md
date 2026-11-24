# Bottom View

**P1**

## 1. What is the algorithm?

Project a tree into vertical columns relative to the root.

## 2. Problem it solves

Project a tree into vertical columns relative to the root.

## 3. Core intuition

BFS reaches the deepest node last in each horizontal column.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Start the root at horizontal offset zero.
2. Move left by one for a left edge and right by one for a right edge.
3. Apply the view's selection policy and read columns in sorted offset order.

## 6. Visual example

```text
    1
   / \
  2   3
 / \
4   5
```

## 7. Dry run

Root 1 and node 5 share offset zero. BFS sees 1 first and 5 later. This view returns [4, 2, 5, 3].

## 8. Python implementation

Start with `bottom_view` in [implementation.py](implementation.py). Apply the view's selection policy and read columns in sorted offset order.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes, W maximum level size, and C columns, time is O(N + C log(C + 1)), and working space is O(W + C) plus stored values.

## 10. Why the algorithm works

Assigning offsets by signed edge count places exactly the nodes of a chosen vertical line in one bucket. BFS gives nondecreasing depth within every bucket.

## 11. When to use it

Project a tree into vertical columns relative to the root.

## 12. When not to use it

Some vertical traversal problems specify ascending node value for ties at the same position. This version uses BFS order.

## 13. Common mistakes

Use signed offsets rather than depth, and preserve the selected tie convention.

## 14. Alternative approaches

DFS can track depths explicitly, then sort records if the required tie rules differ.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

BFS reaches the deepest node last in each horizontal column. Use signed offsets rather than depth, and preserve the selected tie convention.
