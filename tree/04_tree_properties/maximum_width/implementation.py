"""Maximum Width."""

from collections import deque

from tree.nodes import BinaryNode


def maximum_width(root: BinaryNode | None) -> int:
    """Return the largest complete-tree span, including gaps."""
    if root is None:
        return 0
    queue = deque([(root, 0)])
    widest = 0
    while queue:
        base = queue[0][1]
        widest = max(widest, queue[-1][1] - base + 1)
        for _ in range(len(queue)):
            node, position = queue.popleft()
            position -= base
            if node.left is not None:
                queue.append((node.left, 2 * position))
            if node.right is not None:
                queue.append((node.right, 2 * position + 1))
    return widest
