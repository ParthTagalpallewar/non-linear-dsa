# Tree algorithm selection guide

Identify whether the input is rooted, ordered, weighted, or mutable. Decide
whether value equality is enough or whether a query identifies actual nodes.
For repeated queries, include preprocessing in the cost comparison.

| Problem signal | Start with | Critical distinction |
| --- | --- | --- |
| Process children before parents | [Postorder](02_binary_tree_traversal/postorder_recursive/README.md) | Returning one subtree summary differs from updating a global optimum |
| Inspect one layer or project a view | [BFS and views](03_tree_views/README.md) | Track depth or horizontal offset according to the question |
| Find a complete branch | [Root-to-leaf paths](05_tree_paths/root_to_leaf_paths/README.md) | A node with one child is internal |
| Count downward paths with a target sum | [Prefix sums](05_tree_paths/path_sum_iii/README.md) | Prefix state is scoped to the active branch |
| Find parent relationships with duplicates | [Identity-based queries](06_tree_relationships/README.md) | Node identity is independent from its value |
| Answer many static LCA queries | [Binary lifting or Euler-RMQ](17_tree_queries/README.md) | Euler-RMQ answers in O(1) after building a sparse table |
| Query or update subtrees | [Euler interval](17_tree_queries/subtree_queries/README.md) + [range structure](segment-vs-fenwick.md) | Use one preorder position per node |
| Static path sum | [Root prefixes with LCA](17_tree_queries/path_queries/README.md) | Count LCA once for vertex values |
| Change values while querying paths | [Heavy-light decomposition](19_advanced_trees/heavy_light_decomposition/README.md) | The topology is static |
| Keep ordered keys under insertion/deletion | [AVL or red-black](bst-vs-avl-vs-red-black.md) | Balanced height protects worst-case lookup time |
| Keep only the next extreme | [Heap](12_heap/README.md) | Heap order does not give arbitrary rank |
| Match text prefixes or high bits | [Trie](13_trie/README.md) | A stored prefix may lack a terminal marker |
| Optimize a condition across every possible root | [Rerooting DP](16_tree_dp/rerooting_dp/README.md) | Express how the answer changes across one edge |
| Scan ordered records in a high-fanout index | [B+ tree](18_multiway_trees/b_plus_tree/README.md) | Linked leaves hold the actual records |

Small trees and one-off queries often need only traversal. Use an explicit
stack when the input can be much deeper than Python's recursion limit.
