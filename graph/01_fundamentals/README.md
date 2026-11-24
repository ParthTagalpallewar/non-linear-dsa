# Graph fundamentals

A vertex is an object such as a city. An edge is a connection such as a road.
An undirected edge A—B allows travel in both directions. A directed edge A→B
allows travel from A to B. Its contribution is one to A's outdegree and one to
B's indegree. In an undirected graph the degree counts incident edge ends, so
an undirected loop contributes two. A weight can encode distance, cost, or time.
Unweighted graphs treat each edge as one step.

A path follows edges from vertex to vertex. A simple path visits distinct
vertices. In a cycle the route comes back to its starting vertex. A triangle is
cyclic, while an undirected chain is acyclic. The edges A→B, B→C and A→C form
a directed acyclic graph (DAG) because no directed path can return to its start.

An undirected graph is connected when every pair of vertices has a path.
Adding an isolated vertex to a triangle makes it disconnected. A complete
simple undirected graph connects every pair and has V(V−1)/2 edges. A chain
has V−1 edges and is sparse. A graph with a substantial fraction of the
possible edges is dense.

An adjacency list stores neighbors per vertex. A matrix stores a cell per
ordered vertex pair. An edge list stores all edges as records.

## Lessons

- [ ] [Adjacency List](adjacency_list/README.md) · P1
- [ ] [Adjacency Matrix](adjacency_matrix/README.md) · P1
- [ ] [Edge List](edge_list/README.md) · P1
