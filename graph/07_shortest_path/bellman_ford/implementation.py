"""Bellman–Ford."""

from math import inf

from graph.shortest_paths import Edge


def bellman_ford(vertex_count: int, edges: list[Edge], source: int) -> list[float]:
    """Return shortest distances or reject a source-reachable negative cycle."""
    if not 0 <= source < vertex_count:
        raise IndexError("source outside the graph")
    distance = [inf] * vertex_count
    distance[source] = 0
    for _ in range(vertex_count - 1):
        changed = False
        for start, end, weight in edges:
            candidate = distance[start] + weight
            if candidate < distance[end]:
                distance[end] = candidate
                changed = True
        if not changed:
            return distance
    if any(distance[u] + w < distance[v] for u, v, w in edges):
        raise ValueError("reachable negative cycle")
    return distance
