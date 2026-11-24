"""Binary Tree Node."""

from tree.nodes import BinaryNode


def binary_node(
    value: int, left: BinaryNode | None = None, right: BinaryNode | None = None
) -> BinaryNode:
    """Create a binary tree node from a value and optional children."""
    return BinaryNode(value, left, right)


if __name__ == "__main__":
    print(binary_node(1, binary_node(2)))
