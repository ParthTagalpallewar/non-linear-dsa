"""Invert Binary Tree."""

from tree.nodes import BinaryNode


def invert_tree(root: BinaryNode | None) -> BinaryNode | None:
    """Swap every node's children in place and return the same root."""
    if root is None:
        return None
    stack = [root]
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    return root


if __name__ == "__main__":
    print(invert_tree(BinaryNode(1, BinaryNode(2))))
