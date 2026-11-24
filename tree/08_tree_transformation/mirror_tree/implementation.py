"""Mirror Binary Tree."""

from tree.nodes import BinaryNode


def mirror_tree(root: BinaryNode | None) -> BinaryNode | None:
    """Return a mirror copy without modifying the original tree."""
    if root is None:
        return None
    return BinaryNode(root.value, mirror_tree(root.right), mirror_tree(root.left))
