"""Level Order Traversal."""

from collections import deque

from tree.nodes import BinaryNode


def level_order(root: BinaryNode | None) -> list[list[int]]:
    """Return values grouped in level order traversal."""
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
        levels.append(level)
    return levels
