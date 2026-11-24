"""Eulerian Circuit."""

from graph.euler import Edge, edge_walk


def eulerian_circuit(vertex_count: int, edges: list[Edge]) -> list[int] | None:
    """Return an Euler circuit in an undirected multigraph, or None."""
    return edge_walk(vertex_count, edges, closed=True)
