"""Longest Root-to-Leaf Path."""

from tree.nodes import BinaryNode


def longest_root_to_leaf_path(root: BinaryNode | None) -> list[int]:
    """Return the first deepest root-to-leaf path in left-to-right order."""
    deepest = -1
    last: BinaryNode | None = None
    parent: dict[BinaryNode, BinaryNode | None] = {}
    if root is None:
        return []
    stack = [(root, 0)]
    parent[root] = None
    while stack:
        node, depth = stack.pop()
        if node.left is None and node.right is None and depth > deepest:
            deepest, last = depth, node
        for child in (node.right, node.left):
            if child is not None:
                parent[child] = node
                stack.append((child, depth + 1))
    result = []
    while last is not None:
        result.append(last.value)
        last = parent[last]
    return result[::-1]
