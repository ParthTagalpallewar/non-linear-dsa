"""Inorder Predecessor."""

from tree.nodes import BinaryNode


def inorder_predecessor(root: BinaryNode | None, key: int) -> int | None:
    """Return the greatest key strictly below the target, or None."""
    best = None
    while root is not None:
        if root.value < key:
            best = root.value
            root = root.right
        else:
            root = root.left
    return best
