"""B+ Tree."""

from tree.b_plus_tree import BPlusTree


def b_plus_tree(degree: int = 2) -> BPlusTree:
    """Create an empty B+ Tree using the specified minimum degree."""
    return BPlusTree(degree)
