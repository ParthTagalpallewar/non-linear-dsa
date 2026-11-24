"""B-Tree Search."""

from tree.b_tree import BTree


def b_tree_search(tree: BTree, key: int) -> bool:
    """Apply the B-Tree search operation to key."""
    return key in tree
