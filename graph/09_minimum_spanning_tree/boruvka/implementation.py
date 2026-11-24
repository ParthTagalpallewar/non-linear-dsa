"""Borůvka’s Algorithm."""

from graph.disjoint_set import DisjointSet
from graph.shortest_paths import Edge


def boruvka(vertex_count: int, edges: list[Edge]) -> list[Edge]:
    """Merge through a cheapest outgoing edge per component each round."""
    sets = DisjointSet(vertex_count)
    forest = []
    while True:
        cheapest: dict[int, Edge] = {}
        for left, right, weight in edges:
            first, second = sets.find(left), sets.find(right)
            if first == second:
                continue
            for root in (first, second):
                if root not in cheapest or weight < cheapest[root][2]:
                    cheapest[root] = (left, right, weight)
        if not cheapest:
            return forest
        for left, right, weight in cheapest.values():
            if sets.union(left, right):
                forest.append((left, right, weight))
