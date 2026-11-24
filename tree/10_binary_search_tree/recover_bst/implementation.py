"""Recover Binary Search Tree."""

from tree.nodes import BinaryNode


def recover_bst(root: BinaryNode | None) -> None:
    """Restore a strict BST in place when exactly two values were swapped."""
    stack: list[BinaryNode] = []
    previous = first = second = None
    while root is not None or stack:
        while root is not None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        if previous is not None and previous.value > root.value:
            if first is None:
                first = previous
            second = root
        previous = root
        root = root.right
    if first is not None and second is not None:
        first.value, second.value = second.value, first.value
