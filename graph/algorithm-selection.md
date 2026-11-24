# Graph algorithm selection guide

Start by identifying what the vertices represent and how to enumerate
their neighbors. A grid can be implicit. An edge list is useful when the
operation scans or sorts all edges. Keep direction, multiplicity, and weights
explicit.

| If the problem asks for… | Start with | Check first |
| --- | --- | --- |
| Reachability or region size | [BFS or DFS](bfs-vs-dfs.md) | Does each state need to be visited once? |
| Fewest moves | [BFS](07_shortest_path/unweighted_bfs/README.md) | Every move must have equal cost |
| Nearest facility | [Multi-source BFS](02_traversal/multi_source_bfs/README.md) or [heap Dijkstra](07_shortest_path/multi_source_shortest_path/README.md) | Reverse directed edges if measuring distance toward a facility |
| Weighted route | [Shortest-path selection](shortest-path-comparison.md) | Weight signs, cycles, and number of starts |
| Groups as links are added | [DSU](08_disjoint_set/dynamic_connectivity/README.md) | Insertions fit ordinary DSU. Deletions need a different model |
| Mutual reachability | [Strongly connected components](10_strongly_connected_components/README.md) | Follow original edge directions |
| Single points of failure | [Bridges and articulation points](11_bridges_and_articulation_points/README.md) | Track physical edge IDs in multigraphs |
| Ordering under prerequisites | [Topological sort](06_topological_sort/README.md) | A directed cycle makes the ordering impossible |
| Two-way conflict partition | [Bipartite check](05_graph_coloring/README.md) | An odd cycle is a contradiction |
| Cheapest set of connections | [Minimum spanning forest](09_minimum_spanning_tree/README.md) | Edge weights measure build cost across the selected set |
| Visit every edge once | [Euler walk](12_special_paths/hierholzer/README.md) | Ignore isolated vertices when checking edge connectivity |
| Visit every vertex once | [Hamiltonian search](12_special_paths/hamiltonian_path/README.md) | General instances can be exponential |
| Transfer subject to capacities | [Max flow and min cut](14_network_flow/README.md) | Model reverse residual capacity separately |
| Pair compatible items | [Bipartite matching](15_graph_matching/README.md) | Use weighted assignment if total pair cost matters |

Represent undirected edges symmetrically for neighbor traversals. Keep one
record per physical edge for Kruskal and DSU cycle detection. Include isolated
vertices explicitly when they matter to counts.
