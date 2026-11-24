"""Prüfer Sequence Encoding."""

from heapq import heapify, heappop, heappush

from tree.rooted import root_tree


def prufer_encode(graph: list[list[int]]) -> list[int]:
    """Encode a labeled undirected tree with at least two vertices."""
    if len(graph) < 2:
        raise ValueError("Prüfer encoding requires at least two vertices")
    root_tree(graph)
    degree = list(map(len, graph))
    leaves = [v for v, count in enumerate(degree) if count == 1]
    heapify(leaves)
    code = []
    for _ in range(len(graph) - 2):
        leaf = heappop(leaves)
        degree[leaf] = 0
        neighbor = next(v for v in graph[leaf] if degree[v])
        code.append(neighbor)
        degree[neighbor] -= 1
        if degree[neighbor] == 1:
            heappush(leaves, neighbor)
    return code
