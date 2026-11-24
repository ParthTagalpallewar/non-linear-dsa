"""Bipartite Check Using BFS."""

from collections import deque


def bipartite_bfs(graph: list[list[int]]) -> bool:
    """Check whether a symmetric adjacency list has a two-coloring."""
    colors = [-1] * len(graph)
    for seed in range(len(graph)):
        if colors[seed] != -1:
            continue
        colors[seed] = 0
        pending = deque([seed])
        while pending:
            vertex = pending.popleft()
            for neighbor in graph[vertex]:
                if colors[neighbor] == colors[vertex]:
                    return False
                if colors[neighbor] == -1:
                    colors[neighbor] = 1 - colors[vertex]
                    pending.append(neighbor)
    return True


if __name__ == "__main__":
    print(bipartite_bfs([[1], [0, 2], [1]]))
