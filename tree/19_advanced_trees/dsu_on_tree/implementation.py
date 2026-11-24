"""DSU on Tree Using Small-to-Large Merging."""

from tree.rooted import root_tree


def dsu_on_tree(graph: list[list[int]], colors: list[int], root: int = 0) -> list[int]:
    """Return the number of distinct colors in every rooted subtree."""
    if len(graph) != len(colors):
        raise ValueError("provide one color per vertex")
    tree = root_tree(graph, root)
    bags = [{color} for color in colors]
    result = [0] * len(graph)
    for vertex in reversed(tree.order):
        result[vertex] = len(bags[vertex])
        parent = tree.parent[vertex]
        if parent != -1:
            if len(bags[parent]) < len(bags[vertex]):
                bags[parent], bags[vertex] = bags[vertex], bags[parent]
            bags[parent].update(bags[vertex])
            bags[vertex].clear()
    return result
