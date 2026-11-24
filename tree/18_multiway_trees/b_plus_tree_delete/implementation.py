"""B+ Tree Deletion."""

from tree.b_plus_tree import BPlusTree


def b_plus_tree_delete(tree: BPlusTree, key: int) -> bool:
    """Apply the B+ Tree delete operation to key."""
    return tree.delete(key)
