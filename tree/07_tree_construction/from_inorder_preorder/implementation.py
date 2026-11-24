"""Construct from Inorder and Preorder."""

from tree.nodes import BinaryNode


def from_inorder_preorder(inorder: list[int], preorder: list[int]) -> BinaryNode | None:
    """Reconstruct a binary tree from two traversals with distinct keys."""
    position = {key: index for index, key in enumerate(inorder)}
    if len(position) != len(inorder) or len(inorder) != len(preorder):
        raise ValueError("traversals must have equal lengths and distinct keys")
    cursor = 0

    def build(left: int, right: int) -> BinaryNode | None:
        nonlocal cursor
        if left >= right:
            return None
        key = preorder[cursor]
        cursor += 1
        middle = position.get(key, -1)
        if not left <= middle < right:
            raise ValueError("inconsistent traversals")
        root = BinaryNode(key)
        root.left = build(left, middle)
        root.right = build(middle + 1, right)
        return root

    return build(0, len(inorder))


if __name__ == "__main__":
    print(from_inorder_preorder([2, 1, 3], [1, 2, 3]))
