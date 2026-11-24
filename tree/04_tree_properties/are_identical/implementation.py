"""Identical Trees Check."""

from tree.nodes import BinaryNode


def are_identical(left: BinaryNode | None, right: BinaryNode | None) -> bool:
    """Compare values and shape in corresponding positions."""
    stack = [(left, right)]
    while stack:
        left, right = stack.pop()
        if left is None or right is None:
            if left is not right:
                return False
            continue
        if left.value != right.value:
            return False
        stack.append((left.left, right.left))
        stack.append((left.right, right.right))
    return True
