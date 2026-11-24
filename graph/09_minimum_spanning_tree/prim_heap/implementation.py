"""Prim’s Algorithm Using a Priority Queue."""

from heapq import heappop, heappush

from graph.shortest_paths import Edge


def prim_heap(vertex_count: int, edges: list[Edge]) -> list[Edge]:
    """Grow a minimum spanning forest through heap-selected cut edges."""
    graph: list[list[tuple[int, int]]] = [[] for _ in range(vertex_count)]
    for left, right, weight in edges:
        graph[left].append((right, weight))
        graph[right].append((left, weight))
    visited = [False] * vertex_count
    forest = []
    for start in range(vertex_count):
        if visited[start]:
            continue
        candidates = [(0, start, start)]
        while candidates:
            weight, parent, vertex = heappop(candidates)
            if visited[vertex]:
                continue
            visited[vertex] = True
            if parent != vertex:
                forest.append((parent, vertex, weight))
            for target, next_weight in graph[vertex]:
                if not visited[target]:
                    heappush(candidates, (next_weight, vertex, target))
    return forest
