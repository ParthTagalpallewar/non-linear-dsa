"""Construct from Inorder and Postorder."""

from tree.nodes import BinaryNode


def from_inorder_postorder(
    inorder: list[int], postorder: list[int]
) -> BinaryNode | None:
    """Reconstruct a binary tree from two traversals with distinct keys."""
    position = {key: index for index, key in enumerate(inorder)}
    if len(position) != len(inorder) or len(inorder) != len(postorder):
        raise ValueError("traversals must have equal lengths and distinct keys")
    cursor = len(postorder) - 1

    def build(left: int, right: int) -> BinaryNode | None:
        nonlocal cursor
        if left >= right:
            return None
        key = postorder[cursor]
        cursor -= 1
        middle = position.get(key, -1)
        if not left <= middle < right:
            raise ValueError("inconsistent traversals")
        root = BinaryNode(key)
        root.right = build(middle + 1, right)
        root.left = build(left, middle)
        return root

    return build(0, len(inorder))
