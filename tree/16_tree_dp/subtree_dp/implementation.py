"""Subtree Dynamic Programming."""

from tree.rooted import root_tree


def subtree_dp(graph: list[list[int]], values: list[int], root: int = 0) -> list[int]:
    """Return the sum of values in every subtree of the rooted tree."""
    if len(graph) != len(values):
        raise ValueError("provide one value per vertex")
    tree = root_tree(graph, root)
    totals = values.copy()
    for vertex in reversed(tree.order):
        parent = tree.parent[vertex]
        if parent != -1:
            totals[parent] += totals[vertex]
    return totals
