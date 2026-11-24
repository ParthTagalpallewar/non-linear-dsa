"""Tarjan’s Bridge Algorithm."""

from graph.undirected_low_link import cuts


def tarjan_bridges(vertex_count: int, edges: list[tuple[int, int]]) -> list[int]:
    """Return input edge indices of bridges."""
    return sorted(cuts(vertex_count, edges)[0])
