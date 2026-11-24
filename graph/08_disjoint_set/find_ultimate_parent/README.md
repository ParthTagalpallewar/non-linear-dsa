# Find Ultimate Parent

**P1**

## 1. What is the algorithm?

Find the representative of a set in a parent forest.

## 2. Problem it solves

Find the representative of a set in a parent forest.

## 3. Core intuition

Only the root of a tree points to itself.

## 4. Prerequisites

Parent arrays, forests, and connected components.

## 5. How it works

1. Start at the requested vertex.
2. Follow parents until reaching a self-parent.
3. Return that root without changing the forest.

## 6. Visual example

```text
0 ← 1 ← 2    3
```

## 7. Dry run

For [0, 0, 1, 3], find(2) walks 2→1→0. The array stays unchanged.

## 8. Python implementation

Start with `find_ultimate_parent` in [implementation.py](implementation.py). Return that root without changing the forest.

## 9. Time and space complexity

For a traversed path of H links, time is O(H + 1) and auxiliary space is O(1). H can be V−1 for V elements.

## 10. Why the algorithm works

All vertices on the path already belong to the same representative, so changes to shortcut links preserve the partition.

## 11. When to use it

Find the representative of a set in a parent forest.

## 12. When not to use it

A general directed graph can have cycles or multiple outgoing choices.

## 13. Common mistakes

The parent array must already be an acyclic forest with self-parent roots.

## 14. Alternative approaches

Compare with the other DSU variants in this topic.

## 15. Practice problems

**Original exercise · P1.** Trace the parent array across two merges and a redundant union.

## 16. Interview revision notes

Only the root of a tree points to itself. The parent array must already be an acyclic forest with self-parent roots.
