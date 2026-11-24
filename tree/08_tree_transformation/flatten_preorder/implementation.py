"""Flatten Binary Tree into a Linked List."""

from tree.nodes import BinaryNode


def flatten_preorder(root: BinaryNode | None) -> BinaryNode | None:
    """Rewrite the tree as a right-only chain in preorder."""
    if root is None:
        return None
    stack = [root]
    previous = None
    while stack:
        node = stack.pop()
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
        if previous is not None:
            previous.right = node
        node.left = None
        previous = node
    return root
