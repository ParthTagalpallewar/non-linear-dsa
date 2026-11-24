"""Bottom View."""

from collections import deque

from tree.nodes import BinaryNode


def bottom_view(root: BinaryNode | None) -> list[int]:
    """Return columns ordered by horizontal distance."""
    if root is None:
        return []
    pending = deque([(root, 0)])
    columns: dict[int, int] = {}
    while pending:
        node, offset = pending.popleft()
        columns[offset] = node.value
        if node.left is not None:
            pending.append((node.left, offset - 1))
        if node.right is not None:
            pending.append((node.right, offset + 1))
    return [columns[key] for key in sorted(columns)]
