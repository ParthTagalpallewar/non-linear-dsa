# Union by Size

**P1**

## 1. What is the algorithm?

Keep parent trees shallow while retaining exact component sizes.

## 2. Problem it solves

Keep parent trees shallow while retaining exact component sizes.

## 3. Core intuition

Whenever a node moves down a level, its group size at least doubles.

## 4. Prerequisites

Parent arrays, forests, and connected components.

## 5. How it works

1. Find the two roots.
2. Attach the smaller group beneath the larger.
3. Add the losing group's size to the surviving root.

## 6. Visual example

```text
0 ← 1 ← 2    3
```

## 7. Dry run

After joining 1 and 2, their group has size two. Joining 0 to 2 attaches the singleton to that group and makes size three.

## 8. Python implementation

Start with `union_by_size` in [implementation.py](implementation.py). Add the losing group's size to the surviving root.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For V elements, storage and setup are O(V). With path halving, the amortized operation cost is O(α(V)).

## 10. Why the algorithm works

Only the surviving root needs current size. Its old group and the losing group were disjoint, so summing gives the exact size.

## 11. When to use it

Keep parent trees shallow while retaining exact component sizes.

## 12. When not to use it

Standard DSU supports merges and queries. Deleting an edge can split a set and requires another approach.

## 13. Common mistakes

Read size through the representative. Former roots may have stale sizes.

## 14. Alternative approaches

Compare with the other DSU variants in this topic.

## 15. Practice problems

**Original exercise · P1.** Trace the parent array across two merges and a redundant union.

## 16. Interview revision notes

Whenever a node moves down a level, its group size at least doubles. Read size through the representative. Former roots may have stale sizes.
