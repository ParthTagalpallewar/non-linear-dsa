"""B+ Tree Insertion."""

from tree.b_plus_tree import BPlusTree


def b_plus_tree_insert(tree: BPlusTree, key: int) -> bool:
    """Apply the B+ Tree insert operation to key."""
    return tree.insert(key)
