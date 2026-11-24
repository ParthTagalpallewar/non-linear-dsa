"""Undirected Cycle Detection Using DSU."""

from collections.abc import Iterable

from graph.disjoint_set import DisjointSet


def undirected_cycle_dsu(vertex_count: int, edges: Iterable[tuple[int, int]]) -> bool:
    """Detect a cycle in a stream containing each undirected edge once."""
    groups = DisjointSet(vertex_count)
    return any(not groups.union(left, right) for left, right in edges)
