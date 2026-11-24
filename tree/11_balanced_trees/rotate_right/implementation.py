"""Right Rotation."""

from tree.avl import AVLNode
from tree.avl import rotate_right as _rotate


def rotate_right(node: AVLNode) -> AVLNode:
    """Return the new root after applying the AVL rotation."""
    return _rotate(node)
