"""Inorder Traversal (Iterative)."""

from tree.nodes import BinaryNode


def inorder_iterative(root: BinaryNode | None) -> list[int]:
    """Return values in left–node–right order without recursion."""
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
            pending.append((node, True))
            pending.append((node.left, False))
    return result
