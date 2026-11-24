# Tree traversal cheat sheet

For root A, left child B, right child C, and B's left child D:

| Traversal | Local order | Output | Typical use |
| --- | --- | --- | --- |
| [Preorder](02_binary_tree_traversal/preorder_recursive/README.md) | Node, left, right | A B D C | Copy or encode structure |
| [Inorder](02_binary_tree_traversal/inorder_recursive/README.md) | Left, node, right | D B A C | Emit a BST in increasing order |
| [Postorder](02_binary_tree_traversal/postorder_recursive/README.md) | Left, right, node | D B C A | Compute subtree DP |
| [Level order](02_binary_tree_traversal/level_order/README.md) | Closest depth first | A / B C / D | Depth, views, or nearest leaf |
| [Reverse level order](02_binary_tree_traversal/reverse_level_order/README.md) | Deepest depth first | D / B C / A | Bottom-up reporting by depth |
| [Zigzag](02_binary_tree_traversal/zigzag/README.md) | Alternate each level | A / C B / D | Layer traversal with alternating output |
| [Boundary](02_binary_tree_traversal/boundary/README.md) | Root, left edge, leaves, reversed right edge | A B D C | Outline excluding repeated leaves |

All these traversals inspect O(N) nodes. Recursive and stack-based DFS use
O(H + 1) auxiliary space for tree height H, while BFS uses O(W) space for
largest level size W. [Morris inorder](02_binary_tree_traversal/morris_inorder/README.md)
and [Morris preorder](02_binary_tree_traversal/morris_preorder/README.md)
use O(1) working space by installing temporary threads, then restoring
the original pointers.
