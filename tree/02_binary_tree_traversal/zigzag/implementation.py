"""Zigzag Traversal."""

from collections import deque

from tree.nodes import BinaryNode


def zigzag(root: BinaryNode | None) -> list[list[int]]:
    """Return values grouped in zigzag traversal."""
    if root is None:
        return []
    pending = deque([root])
    levels = []
    while pending:
        level = []
        for _ in range(len(pending)):
            node = pending.popleft()
            level.append(node.value)
            if node.left is not None:
                pending.append(node.left)
            if node.right is not None:
                pending.append(node.right)
        if len(levels) % 2:
            level.reverse()
        levels.append(level)
    return levels
