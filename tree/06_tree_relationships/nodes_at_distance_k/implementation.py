"""Nodes at Distance K."""

from collections import deque

from tree.nodes import BinaryNode
from tree.relationships import parent_index


def nodes_at_distance_k(
    root: BinaryNode | None, target: BinaryNode, k: int
) -> list[BinaryNode]:
    """Return node identities exactly k edges from the target."""
    if k < 0:
        raise ValueError("k must be nonnegative")
    parents = parent_index(root)
    if target not in parents:
        return []
    queue = deque([(target, None, 0)])
    result = []
    while queue:
        node, previous, distance = queue.popleft()
        if distance == k:
            result.append(node)
            continue
        for neighbor in (node.left, node.right, parents[node]):
            if neighbor is not None and neighbor is not previous:
                queue.append((neighbor, node, distance + 1))
    return result
