"""Centroid Decomposition."""

from tree.rooted import root_tree


def centroid_decomposition(graph: list[list[int]]) -> list[int]:
    """Return the parent of each vertex in the centroid decomposition tree."""
    rooted = root_tree(graph)
    if not rooted.order:
        return []
    removed = [False] * len(graph)
    result = [-1] * len(graph)
    pending = [(0, -1)]
    while pending:
        seed, centroid_parent = pending.pop()
        parent = {seed: -1}
        order = [seed]
        for vertex in order:
            for neighbor in graph[vertex]:
                if not removed[neighbor] and neighbor != parent[vertex]:
                    parent[neighbor] = vertex
                    order.append(neighbor)
        size = dict.fromkeys(order, 1)
        for vertex in reversed(order[1:]):
            size[parent[vertex]] += size[vertex]
        centroid = seed
        for vertex in order:
            largest = max(
                (
                    size[v]
                    for v in graph[vertex]
                    if not removed[v] and parent[v] == vertex
                ),
                default=0,
            )
            if 2 * max(largest, len(order) - size[vertex]) <= len(order):
                centroid = vertex
                break
        result[centroid] = centroid_parent
        removed[centroid] = True
        pending.extend((v, centroid) for v in graph[centroid] if not removed[v])
    return result
