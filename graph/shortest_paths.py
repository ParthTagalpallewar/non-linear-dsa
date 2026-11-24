"""Shared types and heap relaxation for shortest-path lessons."""

from heapq import heappop, heappush
from math import inf

WeightedGraph = list[list[tuple[int, int]]]
Edge = tuple[int, int, int]


def heap_distances(
    graph: WeightedGraph, sources: list[int]
) -> tuple[list[float], list[int | None]]:
    """Return distances and predecessors for nonnegative weighted edges."""
    if any(weight < 0 for adjacent in graph for _, weight in adjacent):
        raise ValueError("Dijkstra requires nonnegative weights")
    distance = [inf] * len(graph)
    parent: list[int | None] = [None] * len(graph)
    pending: list[tuple[float, int]] = []
    for source in sources:
        if not 0 <= source < len(graph):
            raise IndexError("source outside the graph")
        if distance[source] != 0:
            distance[source] = 0
            heappush(pending, (0, source))
    while pending:
        current, vertex = heappop(pending)
        if current != distance[vertex]:
            continue
        for neighbor, weight in graph[vertex]:
            candidate = current + weight
            if candidate < distance[neighbor]:
                distance[neighbor] = candidate
                parent[neighbor] = vertex
                heappush(pending, (candidate, neighbor))
    return distance, parent
