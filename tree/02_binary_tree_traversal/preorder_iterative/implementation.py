"""Preorder Traversal (Iterative)."""

from tree.nodes import BinaryNode


def preorder_iterative(root: BinaryNode | None) -> list[int]:
    """Return values in node–left–right order without recursion."""
    pending = [(root, False)]
    result = []
    while pending:
        node, emit = pending.pop()
        if node is None:
            continue
        if emit:
            result.append(node.value)
        else:
            pending.append((node.right, False))
            pending.append((node.left, False))
            pending.append((node, True))
    return result
