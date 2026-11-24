"""Boundary Traversal."""

from tree.nodes import BinaryNode


def boundary(root: BinaryNode | None) -> list[int]:
    """Return the anticlockwise boundary without emitting leaves twice."""
    if root is None:
        return []
    result = [root.value]

    def is_leaf(node: BinaryNode) -> bool:
        return node.left is None and node.right is None

    node = root.left
    while node is not None and not is_leaf(node):
        result.append(node.value)
        node = node.left if node.left is not None else node.right

    def leaves(node: BinaryNode | None) -> None:
        if node is None:
            return
        if is_leaf(node):
            result.append(node.value)
        else:
            leaves(node.left)
            leaves(node.right)

    leaves(root.left)
    leaves(root.right)
    right_boundary = []
    node = root.right
    while node is not None and not is_leaf(node):
        right_boundary.append(node.value)
        node = node.right if node.right is not None else node.left
    return result + right_boundary[::-1]
