"""Kth Smallest Element."""

from tree.nodes import BinaryNode


def kth_smallest(root: BinaryNode | None, k: int) -> int:
    """Return the one-indexed kth smallest element in a strict BST."""
    if k <= 0:
        raise ValueError("k must be positive")
    stack: list[BinaryNode] = []
    while root is not None or stack:
        while root is not None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.value
        root = root.right
    raise ValueError("k is larger than the tree")
