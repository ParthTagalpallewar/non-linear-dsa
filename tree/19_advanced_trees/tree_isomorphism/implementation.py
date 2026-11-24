"""Unrooted Tree Isomorphism."""

from tree.rooted import root_tree


def tree_isomorphism(first: list[list[int]], second: list[list[int]]) -> bool:
    """Check whether two undirected trees are equal up to vertex relabeling."""
    if len(first) != len(second):
        return False
    if not first:
        return True
    identifiers: dict[tuple[int, ...], int] = {}

    def signatures(graph: list[list[int]]) -> set[int]:
        root_tree(graph)
        degree = list(map(len, graph))
        leaves = [v for v, count in enumerate(degree) if count <= 1]
        remaining = len(graph)
        while remaining > 2:
            remaining -= len(leaves)
            next_leaves = []
            for leaf in leaves:
                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        next_leaves.append(neighbor)
            leaves = next_leaves
        result = set()
        for center in leaves:
            tree = root_tree(graph, center)
            shape = [0] * len(graph)
            for vertex in reversed(tree.order):
                key = tuple(
                    sorted(shape[v] for v in graph[vertex] if tree.parent[v] == vertex)
                )
                shape[vertex] = identifiers.setdefault(key, len(identifiers))
            result.add(shape[center])
        return result

    return bool(signatures(first) & signatures(second))
