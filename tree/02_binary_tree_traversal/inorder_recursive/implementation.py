"""Inorder Traversal (Recursive)."""

from tree.nodes import BinaryNode


def inorder_recursive(root: BinaryNode | None) -> list[int]:
    """Return values in left–node–right order."""
    result: list[int] = []

    def visit(node: BinaryNode | None) -> None:
        if node is None:
            return
        visit(node.left)
        result.append(node.value)
        visit(node.right)

    visit(root)
    return result
