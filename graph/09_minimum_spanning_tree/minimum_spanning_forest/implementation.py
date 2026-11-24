"""Minimum Spanning Forest."""

from graph.disjoint_set import DisjointSet
from graph.shortest_paths import Edge


def minimum_spanning_forest(vertex_count: int, edges: list[Edge]) -> list[Edge]:
    """Select minimum-weight spanning edges separately in each component."""
    sets = DisjointSet(vertex_count)
    forest: list[Edge] = []
    for edge in sorted(edges, key=lambda item: item[2]):
        left, right, _ = edge
        if sets.union(left, right):
            forest.append(edge)
    return forest
