"""Vertical Order Traversal."""

from collections import deque

from tree.nodes import BinaryNode


def vertical_order(root: BinaryNode | None) -> list[list[int]]:
    """Return columns ordered by horizontal distance."""
    if root is None:
        return []
    pending = deque([(root, 0)])
    columns: dict[int, list[int]] = {}
    while pending:
        node, offset = pending.popleft()
        columns.setdefault(offset, []).append(node.value)
        if node.left is not None:
            pending.append((node.left, offset - 1))
        if node.right is not None:
            pending.append((node.right, offset + 1))
    return [columns[key] for key in sorted(columns)]
