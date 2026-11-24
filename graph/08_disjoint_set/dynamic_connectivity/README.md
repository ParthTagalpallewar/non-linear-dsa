# Dynamic Connectivity with Insertions

**P1**

## 1. What is the algorithm?

Answer repeated connectivity queries as edges are added.

## 2. Problem it solves

Answer repeated connectivity queries as edges are added.

## 3. Core intuition

Process events online and maintain exactly the connected components seen so far.

## 4. Prerequisites

Parent arrays, forests, and connected components.

## 5. How it works

1. Start with one set per vertex.
2. Union the endpoints of each added edge.
3. Compare roots on a connectivity query.

## 6. Visual example

```text
0 ← 1 ← 2    3
```

## 7. Dry run

Querying 0 and 2 before additions returns false. After adding 0—1 and 1—2 it returns true.

## 8. Python implementation

Start with `dynamic_connectivity` in [implementation.py](implementation.py). Compare roots on a connectivity query.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For V vertices and Q operations, time is O(V + Q α(V)) amortized. Working space is O(V), plus the query answers.

## 10. Why the algorithm works

Every addition either stays inside a component or joins exactly two components. Union implements both cases.

## 11. When to use it

Answer repeated connectivity queries as edges are added.

## 12. When not to use it

Standard DSU supports merges and queries. Deleting an edge can split a set and requires another approach.

## 13. Common mistakes

Process operations in their original order.

## 14. Alternative approaches

Compare with the other DSU variants in this topic.

## 15. Practice problems

**Original exercise · P1.** Trace the parent array across two merges and a redundant union.

## 16. Interview revision notes

Process events online and maintain exactly the connected components seen so far. Process operations in their original order.
