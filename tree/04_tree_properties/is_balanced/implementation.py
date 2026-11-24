"""Balanced Binary Tree Check."""

from tree.nodes import BinaryNode


def is_balanced(root: BinaryNode | None) -> bool:
    """Test whether child heights differ by at most one at every node."""

    def height(node: BinaryNode | None) -> int:
        if node is None:
            return 0
        left = height(node.left)
        if left == -1:
            return -1
        right = height(node.right)
        if right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return height(root) != -1
