"""B-Tree Insertion."""

from tree.b_tree import BTree


def b_tree_insert(tree: BTree, key: int) -> bool:
    """Apply the B-Tree insert operation to key."""
    return tree.insert(key)
