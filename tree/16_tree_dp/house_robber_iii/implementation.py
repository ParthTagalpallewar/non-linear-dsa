"""House Robber III."""

from tree.nodes import BinaryNode


def house_robber_iii(root: BinaryNode | None) -> int:
    """Maximize chosen node values with no chosen parent-child pair."""

    def visit(node: BinaryNode | None) -> tuple[int, int]:
        if node is None:
            return 0, 0
        left_take, left_skip = visit(node.left)
        right_take, right_skip = visit(node.right)
        take = node.value + left_skip + right_skip
        skip = max(left_take, left_skip) + max(right_take, right_skip)
        return take, skip

    return max(visit(root))
