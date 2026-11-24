"""Prüfer Sequence Decoding."""

from heapq import heapify, heappop, heappush


def prufer_decode(code: list[int]) -> list[list[int]]:
    """Decode a Prüfer sequence into a symmetric adjacency list."""
    size = len(code) + 2
    degree = [1] * size
    for vertex in code:
        if not 0 <= vertex < size:
            raise ValueError("label outside decoded tree")
        degree[vertex] += 1
    leaves = [v for v, count in enumerate(degree) if count == 1]
    heapify(leaves)
    graph: list[list[int]] = [[] for _ in range(size)]
    for neighbor in code:
        leaf = heappop(leaves)
        graph[leaf].append(neighbor)
        graph[neighbor].append(leaf)
        degree[neighbor] -= 1
        if degree[neighbor] == 1:
            heappush(leaves, neighbor)
    first, second = leaves
    graph[first].append(second)
    graph[second].append(first)
    return graph


if __name__ == "__main__":
    print(prufer_decode([0, 1, 1]))
