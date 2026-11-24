"""Floyd–Warshall."""

from math import inf

from graph.shortest_paths import Edge


def floyd_warshall(vertex_count: int, edges: list[Edge]) -> list[list[float]]:
    """Return all-pairs distances or reject any negative cycle."""
    if vertex_count < 0:
        raise ValueError("vertex count must be nonnegative")
    distance = [[inf] * vertex_count for _ in range(vertex_count)]
    for vertex in range(vertex_count):
        distance[vertex][vertex] = 0
    for start, end, weight in edges:
        distance[start][end] = min(distance[start][end], weight)
    for middle in range(vertex_count):
        for start in range(vertex_count):
            for end in range(vertex_count):
                candidate = distance[start][middle] + distance[middle][end]
                if candidate < distance[start][end]:
                    distance[start][end] = candidate
    if any(distance[v][v] < 0 for v in range(vertex_count)):
        raise ValueError("graph has a negative cycle")
    return distance
