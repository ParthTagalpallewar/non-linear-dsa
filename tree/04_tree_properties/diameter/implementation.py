"""Diameter of a Binary Tree."""

from tree.nodes import BinaryNode


def diameter(root: BinaryNode | None) -> int:
    """Return the longest simple path length in edges."""
    best = 0

    def height(node: BinaryNode | None) -> int:
        nonlocal best
        if node is None:
            return 0
        left, right = height(node.left), height(node.right)
        best = max(best, left + right)
        return 1 + max(left, right)

    height(root)
    return best


if __name__ == "__main__":
    print(diameter(BinaryNode(1, BinaryNode(2), BinaryNode(3))))
