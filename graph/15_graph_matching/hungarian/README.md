# Hungarian Assignment Algorithm

**P3**

## 1. What is the algorithm?

Assign every worker a distinct task while minimizing the sum of costs.

## 2. Problem it solves

Assign every worker a distinct task while minimizing the sum of costs.

## 3. Core intuition

Maintain row and column potentials so zero reduced-cost edges form a growing graph of equally tight choices.

## 4. Prerequisites

Graph representations and the traversal or recurrence used below.

## 5. How it works

1. Start an alternating search from each new row.
2. Track slack to unused columns and adjust potentials by the smallest slack when the search needs a new tight edge.
3. When a free column is reached, follow predecessor columns to rotate assignments.

## 6. Visual example

```text
       T0  T1
W0      4   1
W1      3   2
```

## 7. Dry run

W0 can take T1 at cost 1. For W1, taking the unused T0 at cost 3 gives assignment [1, 0] and total 4.

## 8. Python implementation

Start with `hungarian` in [implementation.py](implementation.py). When a free column is reached, follow predecessor columns to rotate assignments.

Run the example from the repository root with `uv run python -m graph.15_graph_matching.hungarian.implementation`.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For R rows and C columns with R≤C, time is O(R²C) and auxiliary space is O(R + C). Each new row expands at most R columns and scans C per expansion.

## 10. Why the algorithm works

Dual potentials give a lower bound on any assignment. The returned assignment uses tight edges, and unassigned columns have zero potential, so its cost equals that bound.

## 11. When to use it

Assign every worker a distinct task while minimizing the sum of costs.

## 12. When not to use it

This API expects a complete finite cost matrix and requires a column for every row.

## 13. Common mistakes

Keep the predecessor column separately from the owner row, and distinguish minimum assignment from maximum cardinality.

## 14. Alternative approaches

Minimum-cost flow allows sparse eligibility, side constraints, and capacities beyond one.

## 15. Practice problems

**Original exercise · P3.** Modify the worked example to introduce an isolated vertex, and predict the result before running the code.

## 16. Interview revision notes

Maintain row and column potentials so zero reduced-cost edges form a growing graph of equally tight choices. Keep the predecessor column separately from the owner row, and distinguish minimum assignment from maximum cardinality.
