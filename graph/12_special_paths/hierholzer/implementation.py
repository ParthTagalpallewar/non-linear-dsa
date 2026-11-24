"""Hierholzer’s Algorithm."""

from graph.euler import Edge, edge_walk


def hierholzer(vertex_count: int, edges: list[Edge]) -> list[int] | None:
    """Return an Euler walk in an undirected multigraph, or None."""
    return edge_walk(vertex_count, edges)


if __name__ == "__main__":
    print(hierholzer(3, [(0, 1), (1, 2), (2, 0)]))
