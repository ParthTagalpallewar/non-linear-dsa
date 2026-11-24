"""Construct a BST from Preorder."""

from tree.nodes import BinaryNode


def bst_from_preorder(preorder: list[int]) -> BinaryNode | None:
    """Build a strict BST in preorder or reject inconsistent keys."""
    index = 0

    def build(low: int | None, high: int | None) -> BinaryNode | None:
        nonlocal index
        if index == len(preorder):
            return None
        value = preorder[index]
        if (low is not None and value <= low) or (high is not None and value >= high):
            return None
        index += 1
        return BinaryNode(value, build(low, value), build(value, high))

    root = build(None, None)
    if index != len(preorder):
        raise ValueError("invalid strict BST preorder")
    return root
