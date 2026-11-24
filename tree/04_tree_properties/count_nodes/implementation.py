"""Count Nodes."""

from tree.nodes import BinaryNode


def count_nodes(root: BinaryNode | None) -> int:
    """Calculate count nodes for a binary tree."""
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)
