# Bridges and Articulation Points

Removing a bridge edge or an articulation vertex increases the number of connected components. DFS discovery time assigns a timestamp when entering each vertex. Its low-link value is the smallest discovery time reachable from its subtree by descending through tree edges and then taking at most one back edge. For tree edge u—v, a low[v] greater than discovery[u] identifies a bridge. A nonroot u is an articulation point if some child v has low[v] at least discovery[u]. Equality rescues the edge but still relies on u. A root is special and needs at least two DFS children.

## Lessons

- [ ] [Tarjan’s Bridge Algorithm](tarjan_bridges/README.md) · P2
- [ ] [Articulation Point Algorithm](articulation_points/README.md) · P2
