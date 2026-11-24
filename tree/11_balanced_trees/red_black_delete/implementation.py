"""Red-Black Tree Deletion."""

from tree.red_black import RedBlackTree


def red_black_delete(tree: RedBlackTree, key: int) -> None:
    """Delete key if present."""
    tree.delete(key)
