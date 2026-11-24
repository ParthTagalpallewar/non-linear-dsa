"""B-Tree."""

from tree.b_tree import BTree


def b_tree(degree: int = 2) -> BTree:
    """Create an empty B-Tree using the specified minimum degree."""
    return BTree(degree)
