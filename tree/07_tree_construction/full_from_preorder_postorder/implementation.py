"""Construct a Full Binary Tree from Preorder and Postorder."""

from tree.nodes import BinaryNode


def full_from_preorder_postorder(
    preorder: list[int], postorder: list[int]
) -> BinaryNode | None:
    """Rebuild a full binary tree with distinct keys from two traversals."""
    position = {key: index for index, key in enumerate(postorder)}
    if (
        len(preorder) != len(postorder)
        or len(position) != len(postorder)
        or set(preorder) != set(postorder)
    ):
        raise ValueError("inconsistent traversal keys")

    def build(pre_start: int, post_start: int, size: int) -> BinaryNode:
        value = preorder[pre_start]
        if value != postorder[post_start + size - 1]:
            raise ValueError("inconsistent traversal roots")
        node = BinaryNode(value)
        if size == 1:
            return node
        left_size = position[preorder[pre_start + 1]] - post_start + 1
        right_size = size - left_size - 1
        if min(left_size, right_size) <= 0:
            raise ValueError("the tree must be full")
        node.left = build(pre_start + 1, post_start, left_size)
        node.right = build(
            pre_start + left_size + 1, post_start + left_size, right_size
        )
        return node

    return build(0, 0, len(preorder)) if preorder else None
