"""Right–Left Rotation."""

from tree.avl import AVLNode
from tree.avl import rotate_right_left as _rotate


def rotate_right_left(node: AVLNode) -> AVLNode:
    """Return the new root after applying the AVL rotation."""
    return _rotate(node)
