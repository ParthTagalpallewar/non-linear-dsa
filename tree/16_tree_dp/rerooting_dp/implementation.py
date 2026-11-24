"""Rerooting Dynamic Programming."""

from tree.rooted import root_tree, subtree_sizes


def rerooting_dp(graph: list[list[int]], root: int = 0) -> list[int]:
    """Return the sum of edge distances from each vertex to every other vertex."""
    tree = root_tree(graph, root)
    if not tree.order:
        return []
    size = len(graph)
    subtree = subtree_sizes(tree)
    total = [0] * size
    total[root] = sum(tree.depth)
    for vertex in tree.order[1:]:
        parent = tree.parent[vertex]
        total[vertex] = total[parent] + size - 2 * subtree[vertex]
    return total
