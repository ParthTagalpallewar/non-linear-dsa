"""Articulation Point Algorithm."""

from graph.undirected_low_link import cuts


def articulation_points(vertex_count: int, edges: list[tuple[int, int]]) -> list[int]:
    """Return articulation vertex IDs."""
    return sorted(cuts(vertex_count, edges)[1])
