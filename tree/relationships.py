"""Parent indexing helpers for identity-based binary-tree queries."""

from tree.nodes import BinaryNode


def parent_index(root: BinaryNode | None) -> dict[BinaryNode, BinaryNode | None]:
    """Map every node in a proper binary tree to its parent."""
    if root is None:
        return {}
    parents: dict[BinaryNode, BinaryNode | None] = {root: None}
    pending = [root]
    while pending:
        node = pending.pop()
        for child in (node.left, node.right):
            if child is not None:
                parents[child] = node
                pending.append(child)
    return parents
