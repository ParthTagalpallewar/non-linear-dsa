# Fleury’s Algorithm

**P3**

## 1. What is the algorithm?

Trace an Euler walk by choosing the next edge locally.

## 2. Problem it solves

Trace an Euler walk by choosing the next edge locally.

## 3. Core intuition

An unused bridge can strand edges on the current side, so postpone it when possible.

## 4. Prerequisites

Graph representations and the traversal or recurrence used below.

## 5. How it works

1. Choose a degree-compatible start.
2. Temporarily remove a candidate and test whether its endpoint remains reachable.
3. Prefer a nonbridge and consume the chosen edge permanently.

## 6. Visual example

```text
0 ─ 1
| \ |
3    2
```

## 7. Dry run

At 0, the route to 3 is a bridge. Take the triangle edges first and finish with 0—3.

## 8. Python implementation

Start with `fleury` in [implementation.py](implementation.py). Prefer a nonbridge and consume the chosen edge permanently.

## 9. Time and space complexity

For V vertices and E edges, each bridge test uses O(V + E) time. The implementation uses at most O(E²) candidate tests, giving a conservative O(E²(V + E) + V) bound and O(V + E) auxiliary space.

## 10. Why the algorithm works

Choosing a nonbridge keeps the remaining nonisolated portion connected. When all remaining incident choices reduce to one physical exit, crossing it is necessary.

## 11. When to use it

Trace an Euler walk by choosing the next edge locally.

## 12. When not to use it

Use Hierholzer for large inputs.

## 13. Common mistakes

Run the reachability test on unused edges only, preserving parallel edges by ID.

## 14. Alternative approaches

Hierholzer builds the same type of walk in linear time.

## 15. Practice problems

**Original exercise · P3.** Modify the worked example to introduce an isolated vertex, and predict the result before running the code.

## 16. Interview revision notes

An unused bridge can strand edges on the current side, so postpone it when possible. Run the reachability test on unused edges only, preserving parallel edges by ID.
