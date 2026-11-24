# Basic Disjoint Set

**P1**

## 1. What is the algorithm?

Represent a growing partition with one parent per element.

## 2. Problem it solves

Represent a growing partition with one parent per element.

## 3. Core intuition

A root names its group. Linking two roots merges both sets.

## 4. Prerequisites

Parent arrays, forests, and connected components.

## 5. How it works

1. Initialize every element as its own parent.
2. Follow parent pointers to find representatives.
3. Point one distinct representative at the other to merge.

## 6. Visual example

```text
0 ← 1 ← 2    3
```

## 7. Dry run

From [0, 1, 2, 3], union(0, 1) gives [0, 0, 2, 3]. Union(2, 1) gives [2, 0, 2, 3].

## 8. Python implementation

Start with `BasicDisjointSet` in [implementation.py](implementation.py). Point one distinct representative at the other to merge.

Run the example from the repository root with `uv run python -m graph.08_disjoint_set.basic_disjoint_set.implementation`.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For V elements, setup and storage are O(V). Find and union take O(V) worst case and O(1) best case.

## 10. Why the algorithm works

Joining distinct roots cannot create a cycle. Every element formerly under either root reaches the same root afterward.

## 11. When to use it

Represent a growing partition with one parent per element.

## 12. When not to use it

Standard DSU supports merges and queries. Deleting an edge can split a set and requires another approach.

## 13. Common mistakes

Link representatives instead of the two argument vertices.

## 14. Alternative approaches

Compare with the other DSU variants in this topic.

## 15. Practice problems

**Original exercise · P1.** Trace the parent array across two merges and a redundant union.

## 16. Interview revision notes

A root names its group. Linking two roots merges both sets. Link representatives instead of the two argument vertices.
