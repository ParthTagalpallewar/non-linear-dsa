# Iterative Depth-First Search

**P1**

## 1. What is the algorithm?

Iterative DFS stores suspended neighbor scans in a Python list.

## 2. Problem it solves

Traverse long chains and cyclic graphs without consuming Python recursion frames.

## 3. Core intuition

Each stack entry is the iterator for one active recursive call.

## 4. Prerequisites

Iterators, LIFO stacks, and adjacency lists.

## 5. How it works

1. Mark the start and push its neighbor iterator.
2. Advance the top iterator once.
3. Pop exhausted iterators and push new iterators for unseen neighbors.

## 6. Visual example

```text
0 → 1 → 3
 \→ 2 ↗
```

## 7. Dry run

The active iterators belong to vertices [0], [0, 1], then [0, 1, 3]. After unwinding, 2 is discovered.

## 8. Python implementation

Start with `dfs_iterative` in [implementation.py](implementation.py). Pop exhausted iterators and push new iterators for unseen neighbors.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For V reachable vertices and E outgoing edges inspected, time is O(V + E) and auxiliary space is O(V).

## 10. Why the algorithm works

Pushing an iterator starts a child scan and popping an exhausted iterator returns to the parent's unfinished scan.

## 11. When to use it

Traverse long chains and cyclic graphs without consuming Python recursion frames.

## 12. When not to use it

Use BFS for fewest-edge distances.

## 13. Common mistakes

Mark at discovery and retain each active iterator's current position.

## 14. Alternative approaches

A stack of pending vertices is simpler when exact recursive discovery order is irrelevant.

## 15. Practice problems

**Original exercise · P1.** Test a directed chain of 5,000 vertices and count the discoveries.

## 16. Interview revision notes

Each stack entry is the iterator for one active recursive call. Mark at discovery and retain each active iterator's current position.
