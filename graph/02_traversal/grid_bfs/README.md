# Grid BFS

**P1**

## 1. What is the algorithm?

Grid BFS traverses an implicit graph of passable cells.

## 2. Problem it solves

Explore the region reachable by horizontal and vertical moves around blocked cells.

## 3. Core intuition

Generate up to four neighbors on demand and use a queue to maintain distance layers.

## 4. Prerequisites

Row and column indices, bounds checks, and FIFO queues.

## 5. How it works

1. Return an empty order if the start is blocked or outside the grid.
2. Record the start and add it to the pending cells.
3. Visit each pending cell and add unseen passable neighbors.

## 6. Visual example

```text
S 0
0 #
```

## 7. Dry run

After popping S, pending contains [(1, 0), (0, 1)]. The queue next pops (1, 0).

## 8. Python implementation

Start with `grid_bfs` in [implementation.py](implementation.py). Visit each pending cell and add unseen passable neighbors.

## 9. Time and space complexity

For R rows and C columns, the worst case is O(RC) time and O(RC) auxiliary space. Each reached cell has at most four neighbors.

## 10. Why the algorithm works

Every discovered cell is connected to the start through passable cells. Checking all neighbors of each visited cell eventually discovers every reachable cell.

## 11. When to use it

Explore the region reachable by horizontal and vertical moves around blocked cells.

## 12. When not to use it

Movement with different costs needs a weighted traversal. The implementation assumes a rectangular grid.

## 13. Common mistakes

Check bounds before indexing Python lists, where negative indices otherwise wrap.

## 14. Alternative approaches

Use DFS for reachability without distance layers.

## 15. Practice problems

**Original exercise · P1.** Extend this traversal to find whether a cell on the opposite edge is reachable.

## 16. Interview revision notes

Generate up to four neighbors on demand and use a queue to maintain distance layers. Check bounds before indexing Python lists, where negative indices otherwise wrap.
