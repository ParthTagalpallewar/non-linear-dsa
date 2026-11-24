# Graph complexity cheat sheet

V is the number of vertices and E the number of edges. Bounds refer to
worst-case time unless noted. Space excludes the caller's input and includes
auxiliary structures created by the linked implementation.

| Algorithm | Time | Space | Reason |
| --- | --- | --- | --- |
| [BFS and DFS](02_traversal/README.md) | O(V + E) | O(V) | Discover each vertex once |
| [Connected components](03_connectivity/README.md) | O(V + E) for traversal | O(V) | Outer scan covers all components |
| [DSU](08_disjoint_set/README.md) | O(α(V)) amortized per operation | O(V) | Compression with rank or size |
| [Kahn](06_topological_sort/kahn/README.md) | O(V + E) | O(V) | Count and remove each incoming edge |
| [Dijkstra, lazy heap](07_shortest_path/dijkstra_heap/README.md) | O(V + E log(E + 1)) | O(V + E) | Up to E strict heap improvements |
| [Dijkstra, array](07_shortest_path/dijkstra_array/README.md) | O(V² + E) | O(V) | Scan unsettled vertices |
| [Bellman–Ford](07_shortest_path/bellman_ford/README.md) | O(VE + V) | O(V) | Up to V scans of all E edges |
| [Floyd–Warshall](07_shortest_path/floyd_warshall/README.md) | O(V³ + E) | O(V²) | One distance per ordered pair |
| [Johnson](07_shortest_path/johnson/README.md) | O(V² + VE log(E + 1)) | O(V² + E) | One Bellman–Ford and V heap searches, including output |
| [Kruskal and Prim](09_minimum_spanning_tree/README.md) | O(V + E log(E + 1)) for sorted edges or edge heap | O(V + E) | Order edge candidates |
| [SCCs](10_strongly_connected_components/README.md) | O(V + E) | O(V) Tarjan, O(V + E) Kosaraju | Tarjan keeps an active stack; Kosaraju stores the transpose |
| [Bridge and articulation DFS](11_bridges_and_articulation_points/README.md) | O(V + E), plus output sorting | O(V + E) | Track undirected edge identities and timestamps |
| [Hierholzer](12_special_paths/hierholzer/README.md) | O(V + E) | O(V + E) | Consume each physical edge once |
| [Edmonds–Karp](14_network_flow/edmonds_karp/README.md) | O(VE²), plus setup | O(V + E) | Augment on shortest residual paths |
| [Dinic](14_network_flow/dinic/README.md) | O(V²E), plus setup | O(V + E) | Block an entire level graph per phase |
| [Hopcroft–Karp](15_graph_matching/hopcroft_karp/README.md) | O(V + (V + E)√V) for this implementation | O(V) | Batch shortest alternating paths |
| [Hungarian](15_graph_matching/hungarian/README.md) | O(R²C), R ≤ C | O(R + C) | Grow assignments for R rows and C columns |

For sparse simple graphs E is typically near V, while a dense simple directed
graph can have E near V². Recursive implementations also inherit Python's
call-stack limit.
