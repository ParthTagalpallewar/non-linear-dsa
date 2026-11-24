"""Lowest Common Ancestor in a Binary Tree."""

from tree.nodes import BinaryNode
from tree.relationships import parent_index


def lca_binary_tree(
    root: BinaryNode | None, first: BinaryNode, second: BinaryNode
) -> BinaryNode | None:
    """Return the deepest common ancestor, or None if a node is absent."""
    parents = parent_index(root)
    if first not in parents or second not in parents:
        return None
    ancestors = set()
    current: BinaryNode | None = first
    while current is not None:
        ancestors.add(current)
        current = parents[current]
    current = second
    while current not in ancestors:
        current = parents[current]
    return current
