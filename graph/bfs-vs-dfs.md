# BFS vs DFS

| Feature | BFS | DFS |
| --- | --- | --- |
| Pending work | FIFO queue | LIFO stack or recursive call frames |
| Discovery pattern | Increasing edge distance | Follow one branch, then backtrack |
| Typical use | Unweighted distance, nearest goal, level traversal | Ordering, components, active-path detection, low links |
| Seen state | Mark at enqueue | Mark on entry or explicit discovery |
| Space | O(V); frontier may be wide | O(V); call depth may be large |
| Time | O(V + E) with adjacency lists | O(V + E) with adjacency lists |

On edges 0→1, 0→2, and 1→3, BFS visits 0, 1, 2, 3. Recursive DFS
following neighbor order visits 0, 1, 3, 2. In a disconnected graph, loop
over all possible starting vertices if the question covers every component.
Directed cycle detection needs active versus finished state even after
a node is marked seen.

Read [BFS](02_traversal/bfs/README.md),
[recursive DFS](02_traversal/dfs/README.md), and
[iterative DFS](02_traversal/dfs_iterative/README.md).
