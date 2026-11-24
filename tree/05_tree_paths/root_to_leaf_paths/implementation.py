"""Root-to-Leaf Paths."""

from tree.nodes import BinaryNode


def root_to_leaf_paths(root: BinaryNode | None) -> list[list[int]]:
    """Return root-to-leaf paths using a backtracked root-to-node path."""
    result: list[list[int]] = []
    path: list[int] = []

    def visit(node: BinaryNode | None) -> None:
        if node is None:
            return
        path.append(node.value)
        if node.left is None and node.right is None:
            result.append(path.copy())
        else:
            visit(node.left)
            visit(node.right)
        path.pop()

    visit(root)
    return result
