"""B+ Tree Search."""

from tree.b_plus_tree import BPlusTree


def b_plus_tree_search(tree: BPlusTree, key: int) -> bool:
    """Apply the B+ Tree search operation to key."""
    return key in tree
