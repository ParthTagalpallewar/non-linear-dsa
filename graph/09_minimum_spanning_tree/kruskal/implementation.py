"""Kruskal’s Algorithm."""

from graph.disjoint_set import DisjointSet
from graph.shortest_paths import Edge


def kruskal(vertex_count: int, edges: list[Edge]) -> list[Edge]:
    """Select edges by weight, rejecting those that would create cycles."""
    sets = DisjointSet(vertex_count)
    forest = []
    for left, right, weight in sorted(edges, key=lambda edge: edge[2]):
        if sets.union(left, right):
            forest.append((left, right, weight))
    return forest
