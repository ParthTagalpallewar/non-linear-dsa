"""Morris Inorder Traversal."""

from tree.nodes import BinaryNode


def morris_inorder(root: BinaryNode | None) -> list[int]:
    """Traverse without stack storage and restore every temporary thread."""
    result = []
    current = root
    while current is not None:
        if current.left is None:
            result.append(current.value)
            current = current.right
            continue
        predecessor = current.left
        while predecessor.right is not None and predecessor.right is not current:
            predecessor = predecessor.right
        if predecessor.right is None:
            predecessor.right = current
            current = current.left
        else:
            predecessor.right = None
            result.append(current.value)
            current = current.right
    return result
