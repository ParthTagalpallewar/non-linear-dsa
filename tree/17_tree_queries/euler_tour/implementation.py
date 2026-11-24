"""Euler Tour."""

from tree.queries import euler_walk


def euler_tour(graph: list[list[int]], root: int = 0) -> tuple[list[int], list[int]]:
    """Return the full Euler walk and first position of each vertex."""
    return euler_walk(graph, root)
