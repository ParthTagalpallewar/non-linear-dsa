# Prim vs Kruskal

Both algorithms select safe edges using the cut property. A cheapest edge
crossing a cut that respects all selected edges can be included in an
optimal forest.

| Question | Prim | Kruskal |
| --- | --- | --- |
| Which edges are candidates? | Edges leaving the currently growing tree | All edges in ascending weight order |
| Natural input | Weighted adjacency list | Weighted edge list |
| State | Visited vertices and crossing candidates | Disjoint-set roots |
| Disconnected graph | Restart from each remaining unvisited vertex | Every independent component grows during the same scan |
| Time for V vertices and E edges | O(V + E log(E + 1)) edge heap or O(V² + E) array | O(V + E log(E + 1)) |
| Working storage in these lessons | O(V + E), including adjacency built from edges | O(V + E), including a sorted edge copy |

For a triangle with edge weights 4, 1, and 8, Prim starting at an endpoint
of the weight-4 edge may choose weight 4 first. Kruskal starts with weight
1. Both select weights 1 and 4 in the end. Parallel edges are valid choices
and negative weights cause no difficulty. Equal weights can yield multiple
optima. A spanning tree on a connected graph with V vertices uses V−1 edges.

Read [heap Prim](09_minimum_spanning_tree/prim_heap/README.md),
[array Prim](09_minimum_spanning_tree/prim_array/README.md), and
[Kruskal](09_minimum_spanning_tree/kruskal/README.md).
