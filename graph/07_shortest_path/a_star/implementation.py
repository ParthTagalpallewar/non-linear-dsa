"""A* Search."""

from collections.abc import Callable
from heapq import heappop, heappush
from math import inf

from graph.shortest_paths import WeightedGraph


def a_star(
    graph: WeightedGraph, start: int, goal: int, heuristic: Callable[[int], int]
) -> tuple[float, list[int]]:
    """Find a route with an admissible heuristic that is zero at the goal."""
    if not (0 <= start < len(graph) and 0 <= goal < len(graph)):
        raise IndexError("start or goal outside the graph")
    if any(weight < 0 for adjacent in graph for _, weight in adjacent):
        raise ValueError("A* requires nonnegative edge weights")
    if heuristic(goal) != 0:
        raise ValueError("the goal heuristic must be zero")
    distance = [inf] * len(graph)
    parent: list[int | None] = [None] * len(graph)
    distance[start] = 0
    pending: list[tuple[int, int, int]] = [(heuristic(start), 0, start)]
    while pending:
        _, current, vertex = heappop(pending)
        if current != distance[vertex]:
            continue
        if vertex == goal:
            path = [goal]
            while (previous := parent[path[-1]]) is not None:
                path.append(previous)
            return current, path[::-1]
        for target, weight in graph[vertex]:
            candidate = current + weight
            if candidate < distance[target]:
                distance[target] = candidate
                parent[target] = vertex
                heappush(pending, (candidate + heuristic(target), candidate, target))
    return inf, []
