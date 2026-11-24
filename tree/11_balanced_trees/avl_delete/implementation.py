"""AVL Tree Deletion."""

from tree.avl import AVLTree


def avl_delete(tree: AVLTree, key: int) -> None:
    """Delete key if present."""
    tree.delete(key)
