# Tree complexity cheat sheet

N is the number of nodes, H their height, W maximum level size, K a query
rank, L a key length, and B a bit width. Time is worst-case except where
noted. Auxiliary space excludes the result unless listed as index storage.

| Algorithm or structure | Build or full traversal | Query/update | Extra or index space |
| --- | --- | --- | --- |
| [DFS traversal](02_binary_tree_traversal/README.md) | O(N) | — | O(H + 1), or O(1) for Morris |
| [BFS traversal](02_binary_tree_traversal/level_order/README.md) | O(N) | — | O(W) |
| [Path Sum III](05_tree_paths/path_sum_iii/README.md) | O(N) expected | — | O(H + 1) |
| [Reconstruction from inorder](07_tree_construction/README.md) | O(N) expected | — | O(N + H) |
| [Plain BST](10_binary_search_tree/README.md) | O(N²) worst-case repeated insertion | O(H + 1) | O(N) nodes |
| [AVL / red-black](11_balanced_trees/README.md) | O(N log(N + 1)) via inserts | O(log(N + 1)) | O(N) nodes |
| [Heap](12_heap/README.md) | O(N) bottom-up | O(1) peek, O(log(N + 1)) push/pop | O(N) entries |
| [Trie](13_trie/README.md) | O(total input characters) expected | O(L + 1) expected for basic operations | O(total distinct prefixes) |
| [Maximum XOR](13_trie/maximum_xor/README.md) | O(NB) bit/trie operations | O(B) per lookup | O(NB) upper bound |
| [Segment tree](14_segment_tree/README.md) | O(N) | O(log(N + 1)) | O(N) index |
| [Fenwick](15_fenwick_tree/README.md) | O(N) | O(log(N + 1)) | O(N) index |
| [Tree DP and rerooting](16_tree_dp/README.md) | O(N) | — | O(N), or O(H + 1) recursion for node-based summaries |
| [Binary lifting](17_tree_queries/binary_lifting/README.md) | O(N log(N + 1)) | O(log(N + 1)) | O(N log(N + 1)) index |
| [Euler sparse-table LCA](17_tree_queries/lca_euler_sparse_table/README.md) | O(N log(N + 1)) | O(1) | O(N log(N + 1)) index |
| [B/B+ trees](18_multiway_trees/README.md) | O(N log(N + 1)) for fixed degree via inserts | O(log(N + 1)) for fixed degree | O(N) index |
| [Heavy-light decomposition](19_advanced_trees/heavy_light_decomposition/README.md) | O(N) | O(log²(N + 1)) path, O(log(N + 1)) update | O(N) index |
| [Centroid decomposition](19_advanced_trees/centroid_decomposition/README.md) | O(N log(N + 1)) | — | O(N) |
| [Prüfer encoding/decoding](19_advanced_trees/README.md) | O(N log N) | — | O(N) |

An inorder rank query on a plain BST takes O(H + K) time. Maintaining
subtree sizes can reduce selection to O(H + 1).
