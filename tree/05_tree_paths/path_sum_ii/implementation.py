"""Path Sum II."""

from tree.nodes import BinaryNode


def path_sum_ii(root: BinaryNode | None, target: int) -> list[list[int]]:
    """Return path sum ii using a backtracked root-to-node path."""
    result: list[list[int]] = []
    path: list[int] = []

    def visit(node: BinaryNode | None, remaining: int) -> None:
        if node is None:
            return
        path.append(node.value)
        if node.left is None and node.right is None:
            if remaining == node.value:
                result.append(path.copy())
        else:
            visit(node.left, remaining - node.value)
            visit(node.right, remaining - node.value)
        path.pop()

    visit(root, target)
    return result
