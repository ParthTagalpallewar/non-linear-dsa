# Tree Fundamentals

A rooted tree has one distinguished root. Every other node has exactly one
parent. Nodes sharing a parent are siblings. A node with no children is a
leaf, and a node with children is internal. The node's degree here means its
number of children. An ancestor lies on the path from a node toward the root.
A descendant lies below an ancestor. A subtree contains one node and every
descendant below it.

Depth counts edges from the root, so the root has depth and level zero.
Height counts edges down to the farthest leaf, so a leaf has height zero.
Some interview APIs count nodes instead. Those conventions are stated in
the relevant lessons.

A binary tree has up to two ordered children per node. A full binary tree
has zero or two children at every node. A complete tree fills all levels
except possibly the last, which fills from left to right. A perfect tree is
full and has every leaf at the same depth. A height-balanced tree has left
and right subtree heights differing by at most one at every node. A skewed
tree forms a chain by having at most one child per internal node.

The common [node definitions](../nodes.py) use identity semantics. Two nodes
can share the same value while remaining distinct objects.

## Lessons

- [ ] [Binary Tree Node](binary_node/README.md) · P1
- [ ] [N-ary Tree Node](nary_node/README.md) · P1
