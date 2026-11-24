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

## Interview preparation checklist

- [ ] Choose an adjacency list, adjacency matrix, or edge list for a given workload.
- [ ] Trace BFS and DFS on a graph with a cycle and an isolated vertex.
- [ ] Explain why BFS finds fewest-edge paths and why vertices are marked on discovery.
- [ ] Derive grid bounds and movement rules before implementing a traversal.
