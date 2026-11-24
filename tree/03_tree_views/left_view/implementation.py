"""Left View."""

from tree.nodes import BinaryNode


def left_view(root: BinaryNode | None) -> list[int]:
    """Take the first node at each depth when exploring left first."""
    result: list[int] = []
    pending = [(root, 0)]
    while pending:
        node, depth = pending.pop()
        if node is None:
            continue
        if depth == len(result):
            result.append(node.value)
        pending.append((node.right, depth + 1))
        pending.append((node.left, depth + 1))
    return result
