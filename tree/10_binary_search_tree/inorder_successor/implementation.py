"""Inorder Successor."""

from tree.nodes import BinaryNode


def inorder_successor(root: BinaryNode | None, key: int) -> int | None:
    """Return the smallest key strictly above the target, or None."""
    best = None
    while root is not None:
        if root.value > key:
            best = root.value
            root = root.left
        else:
            root = root.right
    return best
