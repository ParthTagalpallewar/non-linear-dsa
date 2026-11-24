"""Kth Largest Element."""

from tree.nodes import BinaryNode


def kth_largest(root: BinaryNode | None, k: int) -> int:
    """Return the one-indexed kth largest element in a strict BST."""
    if k <= 0:
        raise ValueError("k must be positive")
    stack: list[BinaryNode] = []
    while root is not None or stack:
        while root is not None:
            stack.append(root)
            root = root.right
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.value
        root = root.left
    raise ValueError("k is larger than the tree")
