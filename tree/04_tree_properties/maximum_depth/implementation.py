"""Maximum Depth."""

from collections import deque

from tree.nodes import BinaryNode


def maximum_depth(root: BinaryNode | None) -> int:
    """Measure the longest root-to-leaf path in nodes."""
    if root is None:
        return 0
    queue = deque([(root, 1)])
    while queue:
        node, depth = queue.popleft()
        if node.left is not None:
            queue.append((node.left, depth + 1))
        if node.right is not None:
            queue.append((node.right, depth + 1))
    return depth
