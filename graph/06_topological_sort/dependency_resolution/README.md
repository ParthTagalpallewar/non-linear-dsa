# Dependency Resolution

**P1**

## 1. What is the algorithm?

Dependency Resolution answers a structural question about a graph.

## 2. Problem it solves

Determine a valid build or installation order.

## 3. Core intuition

Index task names and direct each edge from a prerequisite to the task that needs it.

## 4. Prerequisites

Adjacency lists, vertex indexing, and the traversal used by the implementation.

## 5. How it works

1. Initialize per-vertex state.
2. Index task names and direct each edge from a prerequisite to the task that needs it.
3. Use the final state to produce the result.

## 6. Visual example

```text
lib → app → tests
```

## 7. Dry run

For tests requiring app and app requiring lib, lib is ready first. Removing lib unlocks app, which unlocks tests.

## 8. Python implementation

Start with `dependency_resolution` in [implementation.py](implementation.py). Use the final state to produce the result.

## 9. Time and space complexity

For V distinct names and E requirement entries, expected time and auxiliary space are O(V + E), counting dictionary operations as constant time.

## 10. Why the algorithm works

Each dependency contributes an incoming edge to its consumer, so indegree elimination schedules every prerequisite first.

## 11. When to use it

Determine a valid build or installation order.

## 12. When not to use it

Version constraints and optional dependencies require additional resolution logic.

## 13. Common mistakes

Include names that occur exclusively as prerequisites.

## 14. Alternative approaches

Compare the search state with the other implementations in this topic.

## 15. Practice problems

**Original exercise · P1.** Modify the example to include an isolated vertex and predict how the result changes.

## 16. Interview revision notes

Index task names and direct each edge from a prerequisite to the task that needs it. Include names that occur exclusively as prerequisites.
