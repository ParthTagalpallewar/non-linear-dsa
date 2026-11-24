"""Tree Diameter Using DP."""

from tree.rooted import root_tree


def tree_diameter_dp(graph: list[list[int]], root: int = 0) -> int:
    """Return the longest path in a numbered undirected tree, in edges."""
    tree = root_tree(graph, root)
    longest = [0] * len(graph)
    second = [0] * len(graph)
    answer = 0
    for vertex in reversed(tree.order):
        answer = max(answer, longest[vertex] + second[vertex])
        parent = tree.parent[vertex]
        if parent == -1:
            continue
        arm = longest[vertex] + 1
        if arm > longest[parent]:
            longest[parent], second[parent] = arm, longest[parent]
        elif arm > second[parent]:
            second[parent] = arm
    return answer
