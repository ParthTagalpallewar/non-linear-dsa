# Non-Linear DSA

A Python 3.10+ curriculum for learning, revising, and implementing graph
and tree algorithms for software engineering interviews. Each lesson pairs
a worked explanation with an implementation and automated tests.

## Repository structure

```text
non-linear-dsa/
├── graph/                    Graph roadmap, references, and 15 topics
├── tree/                     Tree roadmap, references, and 19 topics
├── .github/workflows/ci.yml  Lint, formatting, and tests
├── PROGRESS.md               Phase completion and verification
├── pyproject.toml            Python, pytest, and Ruff settings
└── uv.lock                   Locked development dependencies
```

Each algorithm directory contains `README.md`, `implementation.py`, and
`test_implementation.py`. Shared node and data-structure modules live in
their respective top-level directories. Implementations use the Python
standard library.

## Installation and checks

Install Python 3.10 or later and uv. From the cloned repository root, run:

```sh
uv sync
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

Apply formatting with `uv run ruff format .`. Run a lesson's example or
only its tests from the root:

```sh
uv run python -m graph.02_traversal.bfs.implementation
uv run python -m tree.02_binary_tree_traversal.level_order.implementation
uv run pytest graph/02_traversal/bfs
```

See [project progress](PROGRESS.md) for verification details.

## Learning roadmaps

- [ ] [Graph roadmap](graph/README.md) · Start with representations and traversal. Continue with connectivity, cycles, coloring, topological order, shortest paths, DSU, and MST. Then study low links, directed components, DAG DP, flow, and matching.
- [ ] [Tree roadmap](tree/README.md) · Start with nodes and traversal. Practice properties, paths, relationships, and reconstruction. Then learn BSTs, heaps, tries, balancing, range queries, tree DP, and specialized decompositions.

Study **P1** first for interview essentials. Use **P2** for advanced interview
patterns after finishing the related P1 material. Use **P3** for specialized
roles and competitive programming. For each lesson, predict the dry run,
implement the idea from the description, and use the tests to check it.

## Complexity cheat sheet

V counts graph vertices, E graph edges, N tree nodes or array values, and H tree height.

| Pattern | Typical time | Auxiliary space |
| --- | --- | --- |
| Graph BFS / DFS | O(V + E) | O(V) |
| Heap Dijkstra | O(V + E log(E + 1)) | O(V + E) |
| Topological sort | O(V + E) | O(V) |
| Kruskal | O(V + E log(E + 1)) | O(V + E) |
| Tree DFS | O(N) | O(H + 1) |
| Plain BST operation | O(H + 1) | O(1) for iterative lookup |
| Balanced BST update | O(log(N + 1)) | O(log(N + 1)) for recursive repair |
| Segment or Fenwick query | O(log(N + 1)) | O(N) index storage |

Use the [graph complexity sheet](graph/complexity.md) and
[tree complexity sheet](tree/complexity.md) for advanced bounds. For unfamiliar
problems, start with the [graph selection guide](graph/algorithm-selection.md)
or [tree selection guide](tree/algorithm-selection.md).

## Interview preparation checklist

- [ ] Describe the state space, edge directions, weights, and whether paths or connections are being optimized.
- [ ] Trace BFS and DFS with a cycle, a disconnected component, and an isolated vertex.
- [ ] Select a shortest-path routine from the weight constraints and explain its invariant.
- [ ] Explain when a dependency order exists and trace an indegree update.
- [ ] Derive the MST cut property and identify when DSU avoids repeated traversal.
- [ ] Trace preorder, inorder, postorder, and layer traversal on the same asymmetric tree.
- [ ] Distinguish root-to-leaf paths, downward paths, and arbitrary endpoint paths.
- [ ] Show how BST ordering constrains search and two-child deletion.
- [ ] State whether a query distinguishes equal-valued nodes by identity.
- [ ] State preprocessing, query, update, and auxiliary-space bounds separately.
- [ ] Test empty inputs, repeated keys where supported, missing targets, and skewed input.

## Complete algorithm index

### Graph algorithms

#### Fundamentals

- [ ] [Adjacency List](graph/01_fundamentals/adjacency_list/README.md) · P1
- [ ] [Adjacency Matrix](graph/01_fundamentals/adjacency_matrix/README.md) · P1
- [ ] [Edge List](graph/01_fundamentals/edge_list/README.md) · P1

#### Traversal

- [ ] [Breadth-First Search](graph/02_traversal/bfs/README.md) · P1
- [ ] [Recursive Depth-First Search](graph/02_traversal/dfs/README.md) · P1
- [ ] [Iterative Depth-First Search](graph/02_traversal/dfs_iterative/README.md) · P1
- [ ] [Multi-Source BFS](graph/02_traversal/multi_source_bfs/README.md) · P1
- [ ] [Bidirectional BFS](graph/02_traversal/bidirectional_bfs/README.md) · P2
- [ ] [Flood Fill](graph/02_traversal/flood_fill/README.md) · P1
- [ ] [Grid BFS](graph/02_traversal/grid_bfs/README.md) · P1
- [ ] [Grid DFS](graph/02_traversal/grid_dfs/README.md) · P1
- [ ] [Number of Islands](graph/02_traversal/number_of_islands/README.md) · P1

#### Connectivity

- [ ] [Connected Components Using BFS](graph/03_connectivity/components_bfs/README.md) · P1
- [ ] [Connected Components Using DFS](graph/03_connectivity/components_dfs/README.md) · P1
- [ ] [Connected Components Using DSU](graph/03_connectivity/components_dsu/README.md) · P1

#### Cycle Detection

- [ ] [Undirected Cycle Detection Using BFS](graph/04_cycle_detection/undirected_cycle_bfs/README.md) · P1
- [ ] [Undirected Cycle Detection Using DFS](graph/04_cycle_detection/undirected_cycle_dfs/README.md) · P1
- [ ] [Undirected Cycle Detection Using DSU](graph/04_cycle_detection/undirected_cycle_dsu/README.md) · P1
- [ ] [Directed Cycle Detection Using DFS](graph/04_cycle_detection/directed_cycle_dfs/README.md) · P1
- [ ] [Directed Cycle Detection Using Kahn’s Algorithm](graph/04_cycle_detection/directed_cycle_kahn/README.md) · P1
- [ ] [Eventual Safe Nodes](graph/04_cycle_detection/eventual_safe_nodes/README.md) · P1

#### Graph Coloring

- [ ] [Bipartite Check Using BFS](graph/05_graph_coloring/bipartite_bfs/README.md) · P1
- [ ] [Bipartite Check Using DFS](graph/05_graph_coloring/bipartite_dfs/README.md) · P1
- [ ] [M-Coloring Using Backtracking](graph/05_graph_coloring/m_coloring/README.md) · P1

#### Topological Sorting

- [ ] [Topological Sort Using DFS](graph/06_topological_sort/topological_sort_dfs/README.md) · P1
- [ ] [Kahn’s Algorithm](graph/06_topological_sort/kahn/README.md) · P1
- [ ] [Dependency Resolution](graph/06_topological_sort/dependency_resolution/README.md) · P1
- [ ] [DAG Task Scheduling](graph/06_topological_sort/dag_task_scheduling/README.md) · P1

#### Shortest Paths

- [ ] [Unweighted Shortest Paths Using BFS](graph/07_shortest_path/unweighted_bfs/README.md) · P1
- [ ] [Shortest Paths in a DAG](graph/07_shortest_path/dag_shortest_path/README.md) · P1
- [ ] [Dijkstra Using a Priority Queue](graph/07_shortest_path/dijkstra_heap/README.md) · P1
- [ ] [Dijkstra Using an Array](graph/07_shortest_path/dijkstra_array/README.md) · P1
- [ ] [Bellman–Ford](graph/07_shortest_path/bellman_ford/README.md) · P2
- [ ] [Floyd–Warshall](graph/07_shortest_path/floyd_warshall/README.md) · P2
- [ ] [0–1 BFS](graph/07_shortest_path/zero_one_bfs/README.md) · P2
- [ ] [A* Search](graph/07_shortest_path/a_star/README.md) · P2
- [ ] [Multi-Source Weighted Shortest Paths](graph/07_shortest_path/multi_source_shortest_path/README.md) · P2
- [ ] [Shortest Path Reconstruction](graph/07_shortest_path/shortest_path_reconstruction/README.md) · P1
- [ ] [Johnson’s All-Pairs Shortest Paths](graph/07_shortest_path/johnson/README.md) · P3

#### Disjoint Sets

- [ ] [Basic Disjoint Set](graph/08_disjoint_set/basic_disjoint_set/README.md) · P1
- [ ] [Find Ultimate Parent](graph/08_disjoint_set/find_ultimate_parent/README.md) · P1
- [ ] [Path Compression](graph/08_disjoint_set/compress_path/README.md) · P1
- [ ] [Union by Rank](graph/08_disjoint_set/union_by_rank/README.md) · P1
- [ ] [Union by Size](graph/08_disjoint_set/union_by_size/README.md) · P1
- [ ] [Dynamic Connectivity with Insertions](graph/08_disjoint_set/dynamic_connectivity/README.md) · P1
- [ ] [Lexicographically Smallest Equivalent String](graph/08_disjoint_set/smallest_equivalent_string/README.md) · P1

#### Minimum Spanning Trees

- [ ] [Prim’s Algorithm Using a Priority Queue](graph/09_minimum_spanning_tree/prim_heap/README.md) · P2
- [ ] [Prim’s Algorithm Using an Array](graph/09_minimum_spanning_tree/prim_array/README.md) · P2
- [ ] [Kruskal’s Algorithm](graph/09_minimum_spanning_tree/kruskal/README.md) · P1
- [ ] [Borůvka’s Algorithm](graph/09_minimum_spanning_tree/boruvka/README.md) · P3
- [ ] [Minimum Spanning Forest](graph/09_minimum_spanning_tree/minimum_spanning_forest/README.md) · P2

#### Strongly Connected Components

- [ ] [Kosaraju’s Algorithm](graph/10_strongly_connected_components/kosaraju/README.md) · P2
- [ ] [Tarjan’s SCC Algorithm](graph/10_strongly_connected_components/tarjan_scc/README.md) · P2

#### Bridges and Articulation Points

- [ ] [Tarjan’s Bridge Algorithm](graph/11_bridges_and_articulation_points/tarjan_bridges/README.md) · P2
- [ ] [Articulation Point Algorithm](graph/11_bridges_and_articulation_points/articulation_points/README.md) · P2

#### Special Graph Paths

- [ ] [Eulerian Path](graph/12_special_paths/eulerian_path/README.md) · P2
- [ ] [Eulerian Circuit](graph/12_special_paths/eulerian_circuit/README.md) · P2
- [ ] [Hierholzer’s Algorithm](graph/12_special_paths/hierholzer/README.md) · P2
- [ ] [Fleury’s Algorithm](graph/12_special_paths/fleury/README.md) · P3
- [ ] [Hamiltonian Path Using Backtracking](graph/12_special_paths/hamiltonian_path/README.md) · P3
- [ ] [Hamiltonian Cycle Using Backtracking](graph/12_special_paths/hamiltonian_cycle/README.md) · P3

#### Graph Dynamic Programming

- [ ] [Dynamic Programming on DAGs](graph/13_graph_dp/dag_dp/README.md) · P2
- [ ] [Longest Path in a DAG](graph/13_graph_dp/longest_path_dag/README.md) · P2
- [ ] [Counting Paths in a DAG](graph/13_graph_dp/count_paths_dag/README.md) · P2
- [ ] [Dependency-Based Dynamic Programming](graph/13_graph_dp/dependency_dp/README.md) · P2

#### Network Flow

- [ ] [Ford–Fulkerson](graph/14_network_flow/ford_fulkerson/README.md) · P2
- [ ] [Edmonds–Karp](graph/14_network_flow/edmonds_karp/README.md) · P2
- [ ] [Maximum Flow](graph/14_network_flow/maximum_flow/README.md) · P2
- [ ] [Dinic’s Algorithm](graph/14_network_flow/dinic/README.md) · P3
- [ ] [Minimum Source–Sink Cut](graph/14_network_flow/minimum_cut/README.md) · P2

#### Graph Matching

- [ ] [Bipartite Matching Using Augmenting Paths](graph/15_graph_matching/bipartite_matching/README.md) · P2
- [ ] [Hopcroft–Karp Algorithm](graph/15_graph_matching/hopcroft_karp/README.md) · P3
- [ ] [Hungarian Assignment Algorithm](graph/15_graph_matching/hungarian/README.md) · P3

### Tree algorithms

#### Tree Fundamentals

- [ ] [Binary Tree Node](tree/01_fundamentals/binary_node/README.md) · P1
- [ ] [N-ary Tree Node](tree/01_fundamentals/nary_node/README.md) · P1

#### Binary Tree Traversal

- [ ] [Inorder Traversal (Recursive)](tree/02_binary_tree_traversal/inorder_recursive/README.md) · P1
- [ ] [Inorder Traversal (Iterative)](tree/02_binary_tree_traversal/inorder_iterative/README.md) · P1
- [ ] [Preorder Traversal (Recursive)](tree/02_binary_tree_traversal/preorder_recursive/README.md) · P1
- [ ] [Preorder Traversal (Iterative)](tree/02_binary_tree_traversal/preorder_iterative/README.md) · P1
- [ ] [Postorder Traversal (Recursive)](tree/02_binary_tree_traversal/postorder_recursive/README.md) · P1
- [ ] [Postorder Traversal (Iterative)](tree/02_binary_tree_traversal/postorder_iterative/README.md) · P1
- [ ] [Level Order Traversal](tree/02_binary_tree_traversal/level_order/README.md) · P1
- [ ] [Reverse Level Order Traversal](tree/02_binary_tree_traversal/reverse_level_order/README.md) · P1
- [ ] [Zigzag Traversal](tree/02_binary_tree_traversal/zigzag/README.md) · P1
- [ ] [Boundary Traversal](tree/02_binary_tree_traversal/boundary/README.md) · P1
- [ ] [Morris Inorder Traversal](tree/02_binary_tree_traversal/morris_inorder/README.md) · P2
- [ ] [Morris Preorder Traversal](tree/02_binary_tree_traversal/morris_preorder/README.md) · P2

#### Tree Views

- [ ] [Left View](tree/03_tree_views/left_view/README.md) · P1
- [ ] [Right View](tree/03_tree_views/right_view/README.md) · P1
- [ ] [Top View](tree/03_tree_views/top_view/README.md) · P1
- [ ] [Bottom View](tree/03_tree_views/bottom_view/README.md) · P1
- [ ] [Vertical Order Traversal](tree/03_tree_views/vertical_order/README.md) · P1

#### Tree Properties

- [ ] [Height of a Binary Tree](tree/04_tree_properties/height/README.md) · P1
- [ ] [Count Nodes](tree/04_tree_properties/count_nodes/README.md) · P1
- [ ] [Count Leaf Nodes](tree/04_tree_properties/count_leaves/README.md) · P1
- [ ] [Maximum Depth](tree/04_tree_properties/maximum_depth/README.md) · P1
- [ ] [Minimum Depth](tree/04_tree_properties/minimum_depth/README.md) · P1
- [ ] [Diameter of a Binary Tree](tree/04_tree_properties/diameter/README.md) · P1
- [ ] [Maximum Width](tree/04_tree_properties/maximum_width/README.md) · P1
- [ ] [Balanced Binary Tree Check](tree/04_tree_properties/is_balanced/README.md) · P1
- [ ] [Symmetric Tree Check](tree/04_tree_properties/is_symmetric/README.md) · P1
- [ ] [Identical Trees Check](tree/04_tree_properties/are_identical/README.md) · P1

#### Tree Paths

- [ ] [Root-to-Leaf Paths](tree/05_tree_paths/root_to_leaf_paths/README.md) · P1
- [ ] [Path Sum II](tree/05_tree_paths/path_sum_ii/README.md) · P1
- [ ] [Longest Root-to-Leaf Path](tree/05_tree_paths/longest_root_to_leaf_path/README.md) · P1
- [ ] [Root-to-Leaf Path Sum](tree/05_tree_paths/root_to_leaf_path_sum/README.md) · P1
- [ ] [Path Sum III Using Prefix Sums](tree/05_tree_paths/path_sum_iii/README.md) · P1
- [ ] [Maximum Path Sum](tree/05_tree_paths/maximum_path_sum/README.md) · P1

#### Tree Relationships

- [ ] [Lowest Common Ancestor in a Binary Tree](tree/06_tree_relationships/lca_binary_tree/README.md) · P1
- [ ] [Lowest Common Ancestor in a BST](tree/06_tree_relationships/lca_bst/README.md) · P1
- [ ] [Distance Between Two Nodes](tree/06_tree_relationships/distance_between_nodes/README.md) · P1
- [ ] [Kth Ancestor of a Node](tree/06_tree_relationships/kth_ancestor/README.md) · P1
- [ ] [Nodes at Distance K](tree/06_tree_relationships/nodes_at_distance_k/README.md) · P1
- [ ] [Ancestor and Descendant Queries](tree/06_tree_relationships/ancestor_queries/README.md) · P1

#### Tree Construction

- [ ] [Construct from Inorder and Preorder](tree/07_tree_construction/from_inorder_preorder/README.md) · P1
- [ ] [Construct from Inorder and Postorder](tree/07_tree_construction/from_inorder_postorder/README.md) · P1
- [ ] [Construct a Full Binary Tree from Preorder and Postorder](tree/07_tree_construction/full_from_preorder_postorder/README.md) · P2
- [ ] [Construct a BST from Preorder](tree/07_tree_construction/bst_from_preorder/README.md) · P1
- [ ] [Convert Sorted Array to Balanced BST](tree/07_tree_construction/sorted_array_to_bst/README.md) · P1

#### Tree Transformation

- [ ] [Invert Binary Tree](tree/08_tree_transformation/invert_tree/README.md) · P1
- [ ] [Mirror Binary Tree](tree/08_tree_transformation/mirror_tree/README.md) · P1
- [ ] [Flatten Binary Tree into a Linked List](tree/08_tree_transformation/flatten_preorder/README.md) · P1
- [ ] [Convert Binary Tree to Doubly Linked List](tree/08_tree_transformation/tree_to_doubly_linked_list/README.md) · P1

#### Serialization

- [ ] [Serialization and Deserialization Using BFS](tree/09_serialization/serialize_bfs/README.md) · P1
- [ ] [Serialization and Deserialization Using DFS](tree/09_serialization/serialize_dfs/README.md) · P1

#### Binary Search Trees

- [ ] [BST Search](tree/10_binary_search_tree/bst_search/README.md) · P1
- [ ] [BST Insertion](tree/10_binary_search_tree/bst_insert/README.md) · P1
- [ ] [BST Deletion](tree/10_binary_search_tree/bst_delete/README.md) · P1
- [ ] [BST Validation](tree/10_binary_search_tree/bst_validate/README.md) · P1
- [ ] [BST Floor](tree/10_binary_search_tree/bst_floor/README.md) · P1
- [ ] [BST Ceil](tree/10_binary_search_tree/bst_ceil/README.md) · P1
- [ ] [Inorder Successor](tree/10_binary_search_tree/inorder_successor/README.md) · P1
- [ ] [Inorder Predecessor](tree/10_binary_search_tree/inorder_predecessor/README.md) · P1
- [ ] [Kth Smallest Element](tree/10_binary_search_tree/kth_smallest/README.md) · P1
- [ ] [Kth Largest Element](tree/10_binary_search_tree/kth_largest/README.md) · P1
- [ ] [BST Iterator](tree/10_binary_search_tree/bst_iterator/README.md) · P1
- [ ] [Recover Binary Search Tree](tree/10_binary_search_tree/recover_bst/README.md) · P1
- [ ] [Two Sum in a BST](tree/10_binary_search_tree/bst_two_sum/README.md) · P1

#### Balanced Trees

- [ ] [Left Rotation](tree/11_balanced_trees/rotate_left/README.md) · P2
- [ ] [Right Rotation](tree/11_balanced_trees/rotate_right/README.md) · P2
- [ ] [Left–Right Rotation](tree/11_balanced_trees/rotate_left_right/README.md) · P2
- [ ] [Right–Left Rotation](tree/11_balanced_trees/rotate_right_left/README.md) · P2
- [ ] [AVL Tree](tree/11_balanced_trees/avl_tree/README.md) · P2
- [ ] [AVL Tree Insertion and Deletion](tree/11_balanced_trees/avl_updates/README.md) · P2
- [ ] [Red-Black Tree](tree/11_balanced_trees/red_black_tree/README.md) · P3
- [ ] [Red-Black Tree Insertion and Deletion](tree/11_balanced_trees/red_black_updates/README.md) · P3

- [ ] [AVL Tree Insertion](tree/11_balanced_trees/avl_insert/README.md) · P2
- [ ] [AVL Tree Deletion](tree/11_balanced_trees/avl_delete/README.md) · P2
- [ ] [Red-Black Tree Insertion](tree/11_balanced_trees/red_black_insert/README.md) · P3
- [ ] [Red-Black Tree Deletion](tree/11_balanced_trees/red_black_delete/README.md) · P3

#### Heaps

- [ ] [Min Heap](tree/12_heap/min_heap/README.md) · P1
- [ ] [Max Heap](tree/12_heap/max_heap/README.md) · P1
- [ ] [Heapify](tree/12_heap/heapify/README.md) · P1
- [ ] [Build Heap](tree/12_heap/build_heap/README.md) · P1
- [ ] [Heap Insertion](tree/12_heap/heap_insert/README.md) · P1
- [ ] [Heap Deletion](tree/12_heap/heap_delete/README.md) · P1
- [ ] [Heap Sort](tree/12_heap/heap_sort/README.md) · P1
- [ ] [Priority Queue Using heapq](tree/12_heap/heapq_priority_queue/README.md) · P1

#### Tries

- [ ] [Trie Insertion](tree/13_trie/trie_insert/README.md) · P1
- [ ] [Trie Search](tree/13_trie/trie_search/README.md) · P1
- [ ] [Trie Deletion](tree/13_trie/trie_delete/README.md) · P1
- [ ] [Prefix Search](tree/13_trie/prefix_search/README.md) · P1
- [ ] [Autocomplete Using a Trie](tree/13_trie/autocomplete/README.md) · P2
- [ ] [Bitwise Trie](tree/13_trie/bitwise_trie/README.md) · P2
- [ ] [Maximum XOR Using a Bitwise Trie](tree/13_trie/maximum_xor/README.md) · P2

#### Segment Trees

- [ ] [Segment Tree Construction](tree/14_segment_tree/segment_tree_construction/README.md) · P2
- [ ] [Range Sum Query](tree/14_segment_tree/range_sum_query/README.md) · P2
- [ ] [Range Min Query](tree/14_segment_tree/range_min_query/README.md) · P2
- [ ] [Range Max Query](tree/14_segment_tree/range_max_query/README.md) · P2
- [ ] [Segment Tree Point Update](tree/14_segment_tree/point_update/README.md) · P2
- [ ] [Range Update](tree/14_segment_tree/range_update/README.md) · P2
- [ ] [Lazy Propagation](tree/14_segment_tree/lazy_propagation/README.md) · P2

#### Fenwick Trees

- [ ] [Binary Indexed Tree Construction](tree/15_fenwick_tree/fenwick_construction/README.md) · P2
- [ ] [Fenwick Prefix Sum Query](tree/15_fenwick_tree/fenwick_prefix_sum/README.md) · P2
- [ ] [Fenwick Range Sum Query](tree/15_fenwick_tree/fenwick_range_sum/README.md) · P2
- [ ] [Fenwick Point Update](tree/15_fenwick_tree/fenwick_point_update/README.md) · P2
- [ ] [Fenwick Range Update](tree/15_fenwick_tree/fenwick_range_update/README.md) · P2

#### Tree Dynamic Programming

- [ ] [Subtree Dynamic Programming](tree/16_tree_dp/subtree_dp/README.md) · P2
- [ ] [Maximum Independent Set on a Tree](tree/16_tree_dp/maximum_independent_set/README.md) · P2
- [ ] [House Robber III](tree/16_tree_dp/house_robber_iii/README.md) · P2
- [ ] [Tree Diameter Using DP](tree/16_tree_dp/tree_diameter_dp/README.md) · P2
- [ ] [Rerooting Dynamic Programming](tree/16_tree_dp/rerooting_dp/README.md) · P2
- [ ] [Sum of Distances in a Tree](tree/16_tree_dp/sum_of_distances/README.md) · P2

#### Tree Queries

- [ ] [Binary Lifting](tree/17_tree_queries/binary_lifting/README.md) · P2
- [ ] [Kth Ancestor Using Binary Lifting](tree/17_tree_queries/kth_ancestor_binary_lifting/README.md) · P2
- [ ] [LCA Using Binary Lifting](tree/17_tree_queries/lca_binary_lifting/README.md) · P2
- [ ] [Euler Tour](tree/17_tree_queries/euler_tour/README.md) · P2
- [ ] [Subtree Queries Using an Euler Tour](tree/17_tree_queries/subtree_queries/README.md) · P2
- [ ] [LCA Using Euler Tour and Sparse Table](tree/17_tree_queries/lca_euler_sparse_table/README.md) · P3
- [ ] [Static Path Sum Queries](tree/17_tree_queries/path_queries/README.md) · P2

#### Multiway Trees

- [ ] [N-ary Tree Traversal](tree/18_multiway_trees/nary_traversal/README.md) · P1
- [ ] [B-Tree](tree/18_multiway_trees/b_tree/README.md) · P3
- [ ] [B-Tree Search](tree/18_multiway_trees/b_tree_search/README.md) · P3
- [ ] [B-Tree Insertion](tree/18_multiway_trees/b_tree_insert/README.md) · P3
- [ ] [B-Tree Deletion](tree/18_multiway_trees/b_tree_delete/README.md) · P3
- [ ] [B+ Tree](tree/18_multiway_trees/b_plus_tree/README.md) · P3
- [ ] [B+ Tree Search](tree/18_multiway_trees/b_plus_tree_search/README.md) · P3
- [ ] [B+ Tree Insertion](tree/18_multiway_trees/b_plus_tree_insert/README.md) · P3
- [ ] [B+ Tree Deletion](tree/18_multiway_trees/b_plus_tree_delete/README.md) · P3

#### Advanced Tree Algorithms

- [ ] [Heavy-Light Decomposition](tree/19_advanced_trees/heavy_light_decomposition/README.md) · P3
- [ ] [Centroid Decomposition](tree/19_advanced_trees/centroid_decomposition/README.md) · P3
- [ ] [DSU on Tree Using Small-to-Large Merging](tree/19_advanced_trees/dsu_on_tree/README.md) · P3
- [ ] [Unrooted Tree Isomorphism](tree/19_advanced_trees/tree_isomorphism/README.md) · P3
- [ ] [Prüfer Sequence Encoding](tree/19_advanced_trees/prufer_encode/README.md) · P3
- [ ] [Prüfer Sequence Decoding](tree/19_advanced_trees/prufer_decode/README.md) · P3
