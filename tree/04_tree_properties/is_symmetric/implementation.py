"""Symmetric Tree Check."""

from tree.nodes import BinaryNode


def is_symmetric(root: BinaryNode | None) -> bool:
    """Compare values and shape under reflection."""
    if root is None:
        return True
    left, right = root.left, root.right
    stack = [(left, right)]
    while stack:
        left, right = stack.pop()
        if left is None or right is None:
            if left is not right:
                return False
            continue
        if left.value != right.value:
            return False
        stack.append((left.left, right.right))
        stack.append((left.right, right.left))
    return True
