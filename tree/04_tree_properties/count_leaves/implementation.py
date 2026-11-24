"""Count Leaf Nodes."""

from tree.nodes import BinaryNode


def count_leaves(root: BinaryNode | None) -> int:
    """Calculate count leaf nodes for a binary tree."""
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaves(root.left) + count_leaves(root.right)
