"""Preorder Traversal (Recursive)."""

from tree.nodes import BinaryNode


def preorder_recursive(root: BinaryNode | None) -> list[int]:
    """Return values in node–left–right order."""
    result: list[int] = []

    def visit(node: BinaryNode | None) -> None:
        if node is None:
            return
        result.append(node.value)
        visit(node.left)
        visit(node.right)

    visit(root)
    return result
