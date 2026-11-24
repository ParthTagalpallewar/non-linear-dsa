# Shortest path algorithm comparison

| Input and objective | Algorithm | Time |
| --- | --- | --- |
| Unit weights, one source | [BFS](07_shortest_path/unweighted_bfs/README.md) | O(V + E) |
| Zero and one weights | [0–1 BFS](07_shortest_path/zero_one_bfs/README.md) | O(V + E) |
| DAG, arbitrary integer weights | [Topological relaxation](07_shortest_path/dag_shortest_path/README.md) | O(V + E) |
| Nonnegative weights, sparse graph | [Heap Dijkstra](07_shortest_path/dijkstra_heap/README.md) | O(V + E log(E + 1)) |
| Nonnegative weights, dense graph | [Array Dijkstra](07_shortest_path/dijkstra_array/README.md) | O(V² + E) |
| Nonnegative weights, nearest of multiple starts | [Multi-source Dijkstra](07_shortest_path/multi_source_shortest_path/README.md) | One heap run with multiple starting entries |
| Nonnegative weights, one goal and a lower bound | [A*](07_shortest_path/a_star/README.md) | Depends on heuristic and re-expansions |
| Negative edges, one source | [Bellman–Ford](07_shortest_path/bellman_ford/README.md) | O(VE + V) |
| All pairs, dense or small | [Floyd–Warshall](07_shortest_path/floyd_warshall/README.md) | O(V³ + E) |
| All pairs, sparse, negative edges possible | [Johnson](07_shortest_path/johnson/README.md) | O(V² + VE log(E + 1)) |

V counts vertices and E counts edges. A negative edge can improve a vertex
after Dijkstra has finalized it. A reachable negative cycle makes any
distance that can traverse and exit the cycle unbounded below. Bellman–Ford
rejects source-reachable cycles, while both all-pairs lessons reject a
negative cycle anywhere.

If the output needs the actual route, track a [predecessor on each strict
improvement](07_shortest_path/shortest_path_reconstruction/README.md).
Distance-only code cannot recover the specific chosen route without extra
work.
