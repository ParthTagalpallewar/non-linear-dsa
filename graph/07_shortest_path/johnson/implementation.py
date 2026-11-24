"""Johnson’s All-Pairs Shortest Paths."""

from importlib import import_module

from graph.shortest_paths import Edge, WeightedGraph, heap_distances

bellman_ford = import_module(
    "graph.07_shortest_path.bellman_ford.implementation"
).bellman_ford


def johnson(vertex_count: int, edges: list[Edge]) -> list[list[float]]:
    """Find all-pairs distances or reject a negative cycle anywhere."""
    if vertex_count < 0:
        raise ValueError("vertex count must be nonnegative")
    extra = [(vertex_count, vertex, 0) for vertex in range(vertex_count)]
    potential = bellman_ford(vertex_count + 1, edges + extra, vertex_count)
    graph: WeightedGraph = [[] for _ in range(vertex_count)]
    for start, end, weight in edges:
        graph[start].append((end, int(weight + potential[start] - potential[end])))

    rows = []
    for start in range(vertex_count):
        distance, _ = heap_distances(graph, [start])
        rows.append(
            [
                value - potential[start] + potential[end]
                for end, value in enumerate(distance)
            ]
        )
    return rows
