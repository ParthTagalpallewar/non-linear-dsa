"""B-Tree Deletion."""

from tree.b_tree import BTree


def b_tree_delete(tree: BTree, key: int) -> bool:
    """Apply the B-Tree delete operation to key."""
    return tree.delete(key)
