"""Eulerian Path."""

from graph.euler import Edge, edge_walk


def eulerian_path(vertex_count: int, edges: list[Edge]) -> list[int] | None:
    """Return an Euler walk in an undirected multigraph, or None."""
    return edge_walk(vertex_count, edges)
