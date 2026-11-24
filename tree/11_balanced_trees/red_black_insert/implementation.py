"""Red-Black Tree Insertion."""

from tree.red_black import RedBlackTree


def red_black_insert(tree: RedBlackTree, key: int) -> None:
    """Insert key if absent."""
    tree.insert(key)
