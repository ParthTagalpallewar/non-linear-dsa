# Non-Linear DSA

Learn to recognize, implement, and explain graph and tree algorithms in Python for software engineering interviews.

Start with representations and traversals, then move to connectivity, paths, and ordering. For trees, work through binary traversals and search trees before range queries and specialized structures.

- [ ] [Graph roadmap](graph/README.md)
- [ ] [Tree roadmap](tree/README.md)

Use P1 for interview essentials, P2 for advanced interview topics, and P3 for specialized or competitive-programming techniques.

## Installation and checks

Requires Python 3.10 or later and uv. Run these commands from the repository root.

```sh
uv sync
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

To format source files, run `uv run ruff format .`. Each lesson links to its implementation and tests.

See [project progress](PROGRESS.md) for the current coverage and next task.

## Run a lesson

```sh
uv run python -m graph.02_traversal.bfs.implementation
uv run pytest graph/02_traversal/bfs
```

## Implemented algorithm index

### Fundamentals

- [ ] [Adjacency List](graph/01_fundamentals/adjacency_list/README.md) · P1
- [ ] [Adjacency Matrix](graph/01_fundamentals/adjacency_matrix/README.md) · P1
- [ ] [Edge List](graph/01_fundamentals/edge_list/README.md) · P1

### Traversal

- [ ] [Breadth-First Search](graph/02_traversal/bfs/README.md) · P1
- [ ] [Recursive Depth-First Search](graph/02_traversal/dfs/README.md) · P1
- [ ] [Iterative Depth-First Search](graph/02_traversal/dfs_iterative/README.md) · P1
- [ ] [Multi-Source BFS](graph/02_traversal/multi_source_bfs/README.md) · P1
- [ ] [Bidirectional BFS](graph/02_traversal/bidirectional_bfs/README.md) · P2
- [ ] [Flood Fill](graph/02_traversal/flood_fill/README.md) · P1
- [ ] [Grid BFS](graph/02_traversal/grid_bfs/README.md) · P1
- [ ] [Grid DFS](graph/02_traversal/grid_dfs/README.md) · P1
- [ ] [Number of Islands](graph/02_traversal/number_of_islands/README.md) · P1

### Connectivity

- [ ] [Connected Components Using BFS](graph/03_connectivity/components_bfs/README.md) · P1
- [ ] [Connected Components Using DFS](graph/03_connectivity/components_dfs/README.md) · P1
- [ ] [Connected Components Using DSU](graph/03_connectivity/components_dsu/README.md) · P1

### Cycle Detection

- [ ] [Undirected Cycle Detection Using BFS](graph/04_cycle_detection/undirected_cycle_bfs/README.md) · P1
- [ ] [Undirected Cycle Detection Using DFS](graph/04_cycle_detection/undirected_cycle_dfs/README.md) · P1
- [ ] [Undirected Cycle Detection Using DSU](graph/04_cycle_detection/undirected_cycle_dsu/README.md) · P1
- [ ] [Directed Cycle Detection Using DFS](graph/04_cycle_detection/directed_cycle_dfs/README.md) · P1
- [ ] [Directed Cycle Detection Using Kahn’s Algorithm](graph/04_cycle_detection/directed_cycle_kahn/README.md) · P1
- [ ] [Eventual Safe Nodes](graph/04_cycle_detection/eventual_safe_nodes/README.md) · P1

### Graph Coloring

- [ ] [Bipartite Check Using BFS](graph/05_graph_coloring/bipartite_bfs/README.md) · P1
- [ ] [Bipartite Check Using DFS](graph/05_graph_coloring/bipartite_dfs/README.md) · P1
- [ ] [M-Coloring Using Backtracking](graph/05_graph_coloring/m_coloring/README.md) · P1

### Topological Sorting

- [ ] [Topological Sort Using DFS](graph/06_topological_sort/topological_sort_dfs/README.md) · P1
- [ ] [Kahn’s Algorithm](graph/06_topological_sort/kahn/README.md) · P1
- [ ] [Dependency Resolution](graph/06_topological_sort/dependency_resolution/README.md) · P1
- [ ] [DAG Task Scheduling](graph/06_topological_sort/dag_task_scheduling/README.md) · P1

### Shortest Paths

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

### Disjoint Sets

- [ ] [Basic Disjoint Set](graph/08_disjoint_set/basic_disjoint_set/README.md) · P1
- [ ] [Find Ultimate Parent](graph/08_disjoint_set/find_ultimate_parent/README.md) · P1
- [ ] [Path Compression](graph/08_disjoint_set/compress_path/README.md) · P1
- [ ] [Union by Rank](graph/08_disjoint_set/union_by_rank/README.md) · P1
- [ ] [Union by Size](graph/08_disjoint_set/union_by_size/README.md) · P1
- [ ] [Dynamic Connectivity with Insertions](graph/08_disjoint_set/dynamic_connectivity/README.md) · P1
- [ ] [Lexicographically Smallest Equivalent String](graph/08_disjoint_set/smallest_equivalent_string/README.md) · P1

### Minimum Spanning Trees

- [ ] [Prim’s Algorithm Using a Priority Queue](graph/09_minimum_spanning_tree/prim_heap/README.md) · P2
- [ ] [Prim’s Algorithm Using an Array](graph/09_minimum_spanning_tree/prim_array/README.md) · P2
- [ ] [Kruskal’s Algorithm](graph/09_minimum_spanning_tree/kruskal/README.md) · P1
- [ ] [Borůvka’s Algorithm](graph/09_minimum_spanning_tree/boruvka/README.md) · P3
- [ ] [Minimum Spanning Forest](graph/09_minimum_spanning_tree/minimum_spanning_forest/README.md) · P2

### Strongly Connected Components

- [ ] [Kosaraju’s Algorithm](graph/10_strongly_connected_components/kosaraju/README.md) · P2
- [ ] [Tarjan’s SCC Algorithm](graph/10_strongly_connected_components/tarjan_scc/README.md) · P2

### Bridges and Articulation Points

- [ ] [Tarjan’s Bridge Algorithm](graph/11_bridges_and_articulation_points/tarjan_bridges/README.md) · P2
- [ ] [Articulation Point Algorithm](graph/11_bridges_and_articulation_points/articulation_points/README.md) · P2

### Special Graph Paths

- [ ] [Eulerian Path](graph/12_special_paths/eulerian_path/README.md) · P2
- [ ] [Eulerian Circuit](graph/12_special_paths/eulerian_circuit/README.md) · P2
- [ ] [Hierholzer’s Algorithm](graph/12_special_paths/hierholzer/README.md) · P2
- [ ] [Fleury’s Algorithm](graph/12_special_paths/fleury/README.md) · P3
- [ ] [Hamiltonian Path Using Backtracking](graph/12_special_paths/hamiltonian_path/README.md) · P3
- [ ] [Hamiltonian Cycle Using Backtracking](graph/12_special_paths/hamiltonian_cycle/README.md) · P3

### Graph Dynamic Programming

- [ ] [Dynamic Programming on DAGs](graph/13_graph_dp/dag_dp/README.md) · P2
- [ ] [Longest Path in a DAG](graph/13_graph_dp/longest_path_dag/README.md) · P2
- [ ] [Counting Paths in a DAG](graph/13_graph_dp/count_paths_dag/README.md) · P2
- [ ] [Dependency-Based Dynamic Programming](graph/13_graph_dp/dependency_dp/README.md) · P2

### Network Flow

- [ ] [Ford–Fulkerson](graph/14_network_flow/ford_fulkerson/README.md) · P2
- [ ] [Edmonds–Karp](graph/14_network_flow/edmonds_karp/README.md) · P2
- [ ] [Maximum Flow](graph/14_network_flow/maximum_flow/README.md) · P2
- [ ] [Dinic’s Algorithm](graph/14_network_flow/dinic/README.md) · P3
- [ ] [Minimum Source–Sink Cut](graph/14_network_flow/minimum_cut/README.md) · P2

### Graph Matching

- [ ] [Bipartite Matching Using Augmenting Paths](graph/15_graph_matching/bipartite_matching/README.md) · P2
- [ ] [Hopcroft–Karp Algorithm](graph/15_graph_matching/hopcroft_karp/README.md) · P3
- [ ] [Hungarian Assignment Algorithm](graph/15_graph_matching/hungarian/README.md) · P3

### Tree Fundamentals

- [ ] [Binary Tree Node](tree/01_fundamentals/binary_node/README.md) · P1
- [ ] [N-ary Tree Node](tree/01_fundamentals/nary_node/README.md) · P1

### Binary Tree Traversal

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

### Tree Views

- [ ] [Left View](tree/03_tree_views/left_view/README.md) · P1
- [ ] [Right View](tree/03_tree_views/right_view/README.md) · P1
- [ ] [Top View](tree/03_tree_views/top_view/README.md) · P1
- [ ] [Bottom View](tree/03_tree_views/bottom_view/README.md) · P1
- [ ] [Vertical Order Traversal](tree/03_tree_views/vertical_order/README.md) · P1

### Tree Properties

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

## Interview preparation checklist

- [ ] Choose an adjacency list, adjacency matrix, or edge list for a given workload.
- [ ] Trace BFS and DFS on a graph with a cycle and an isolated vertex.
- [ ] Explain why BFS finds fewest-edge paths and why vertices are marked on discovery.
- [ ] Derive grid bounds and movement rules before implementing a traversal.
