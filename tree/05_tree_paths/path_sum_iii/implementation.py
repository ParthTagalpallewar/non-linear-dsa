"""Path Sum III Using Prefix Sums."""

from collections import Counter

from tree.nodes import BinaryNode


def path_sum_iii(root: BinaryNode | None, target: int) -> int:
    """Count downward paths summing to target, starting and ending anywhere."""
    active = Counter({0: 1})

    def visit(node: BinaryNode | None, prefix: int) -> int:
        if node is None:
            return 0
        prefix += node.value
        matches = active[prefix - target]
        active[prefix] += 1
        total = matches + visit(node.left, prefix) + visit(node.right, prefix)
        active[prefix] -= 1
        if not active[prefix]:
            del active[prefix]
        return total

    return visit(root, 0)


if __name__ == "__main__":
    print(path_sum_iii(BinaryNode(1, BinaryNode(2)), 3))
