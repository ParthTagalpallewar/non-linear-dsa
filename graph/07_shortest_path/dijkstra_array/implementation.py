"""Dijkstra Using an Array."""

from math import inf

from graph.shortest_paths import WeightedGraph


def dijkstra_array(graph: WeightedGraph, source: int) -> list[float]:
    """Return shortest distances using an array scan for each selection."""
    if not 0 <= source < len(graph):
        raise IndexError("source outside the graph")
    if any(weight < 0 for adjacent in graph for _, weight in adjacent):
        raise ValueError("Dijkstra requires nonnegative weights")
    distance = [inf] * len(graph)
    distance[source] = 0
    settled = [False] * len(graph)
    for _ in graph:
        vertex = min(
            (i for i in range(len(graph)) if not settled[i]),
            key=distance.__getitem__,
        )
        if distance[vertex] == inf:
            break
        settled[vertex] = True
        for target, weight in graph[vertex]:
            distance[target] = min(distance[target], distance[vertex] + weight)
    return distance
