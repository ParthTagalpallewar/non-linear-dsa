"""Prim’s Algorithm Using an Array."""

from math import inf

from graph.shortest_paths import Edge


def prim_array(vertex_count: int, edges: list[Edge]) -> list[Edge]:
    """Grow a minimum spanning forest using a linear scan per vertex."""
    graph: list[list[tuple[int, int]]] = [[] for _ in range(vertex_count)]
    for left, right, weight in edges:
        graph[left].append((right, weight))
        graph[right].append((left, weight))
    visited = [False] * vertex_count
    cheapest = [inf] * vertex_count
    parent = [-1] * vertex_count
    forest = []
    for _ in range(vertex_count):
        vertex = min(
            (v for v in range(vertex_count) if not visited[v]),
            key=cheapest.__getitem__,
        )
        visited[vertex] = True
        if parent[vertex] != -1:
            forest.append((parent[vertex], vertex, int(cheapest[vertex])))
        for target, weight in graph[vertex]:
            if not visited[target] and weight < cheapest[target]:
                cheapest[target] = weight
                parent[target] = vertex
    return forest
