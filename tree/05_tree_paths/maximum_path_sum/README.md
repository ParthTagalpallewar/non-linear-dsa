# Maximum Path Sum

**P1**

## 1. What is the algorithm?

Maximize the sum of a nonempty simple path between any two nodes.

## 2. Problem it solves

Maximize the sum of a nonempty simple path between any two nodes.

## 3. Core intuition

At each node consider joining both profitable child arms, while returning just one arm for possible extension by the parent.

## 4. Prerequisites

Tree terminology, recursive subproblems, and the data structure used below.

## 5. How it works

1. Handle missing nodes or empty input.
2. At each node consider joining both profitable child arms, while returning just one arm for possible extension by the parent.
3. Produce the result from the completed traversal.

## 6. Visual example

```text
    1
   / \
  2   3
 /
4
```

## 7. Dry run

At node 2, arm 4 adds four to the value 2. At node 1, joining the arm worth 6 and node 3 gives ten.

## 8. Python implementation

Start with `maximum_path_sum` in [implementation.py](implementation.py). Produce the result from the completed traversal.

Run the [lesson tests](test_implementation.py) for executable examples.

## 9. Time and space complexity

For N nodes and height H, worst-case time is O(N) and auxiliary space O(H + 1), excluding output.

## 10. Why the algorithm works

Every simple path has one highest node. At that node arms can be optimized independently and negative arms can be omitted.

## 11. When to use it

Maximize the sum of a nonempty simple path between any two nodes.

## 12. When not to use it

Recursive implementations can reach Python's recursion limit on skewed trees.

## 13. Common mistakes

Do not initialize the overall answer to zero, since all available paths may be negative.

## 14. Alternative approaches

An explicit stack avoids using Python call frames.

## 15. Practice problems

**Original exercise · P1.** Modify the worked example by adding a leaf and predict what changes.

## 16. Interview revision notes

At each node consider joining both profitable child arms, while returning just one arm for possible extension by the parent. Do not initialize the overall answer to zero, since all available paths may be negative.
