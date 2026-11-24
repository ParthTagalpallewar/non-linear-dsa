"""Maximum Path Sum."""

from tree.nodes import BinaryNode


def maximum_path_sum(root: BinaryNode | None) -> int | None:
    """Return the largest nonempty simple-path sum or None for an empty tree."""
    best: int | None = None

    def extend(node: BinaryNode | None) -> int:
        nonlocal best
        if node is None:
            return 0
        left = max(0, extend(node.left))
        right = max(0, extend(node.right))
        turning_sum = node.value + left + right
        best = turning_sum if best is None else max(best, turning_sum)
        return node.value + max(left, right)

    extend(root)
    return best
