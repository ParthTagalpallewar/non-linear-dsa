"""Postorder Traversal (Recursive)."""

from tree.nodes import BinaryNode


def postorder_recursive(root: BinaryNode | None) -> list[int]:
    """Return values in left–right–node order."""
    result: list[int] = []

    def visit(node: BinaryNode | None) -> None:
        if node is None:
            return
        visit(node.left)
        visit(node.right)
        result.append(node.value)

    visit(root)
    return result
