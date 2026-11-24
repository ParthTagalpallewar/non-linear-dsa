"""AVL Tree Insertion."""

from tree.avl import AVLTree


def avl_insert(tree: AVLTree, key: int) -> None:
    """Insert key if absent."""
    tree.insert(key)
