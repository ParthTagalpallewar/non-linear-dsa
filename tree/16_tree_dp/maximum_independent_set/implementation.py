"""Maximum Independent Set on a Tree."""

from tree.rooted import root_tree


def maximum_independent_set(graph: list[list[int]], root: int = 0) -> int:
    """Return the largest number of vertices with no adjacent pair."""
    tree = root_tree(graph, root)
    if not tree.order:
        return 0
    choose = [1] * len(graph)
    skip = [0] * len(graph)
    for vertex in reversed(tree.order[1:]):
        parent = tree.parent[vertex]
        choose[parent] += skip[vertex]
        skip[parent] += max(choose[vertex], skip[vertex])
    return max(choose[root], skip[root])
