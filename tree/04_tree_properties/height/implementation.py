"""Height of a Binary Tree."""

from tree.nodes import BinaryNode


def height(root: BinaryNode | None) -> int:
    """Calculate height of a binary tree for a binary tree."""
    if root is None:
        return -1
    return 1 + max(height(root.left), height(root.right))
