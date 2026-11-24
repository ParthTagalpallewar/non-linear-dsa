"""BST Deletion."""

from tree.nodes import BinaryNode


def bst_delete(root: BinaryNode | None, key: int) -> BinaryNode | None:
    """Delete key in place and return the possibly changed root."""
    if root is None:
        return None
    if key < root.value:
        root.left = bst_delete(root.left, key)
    elif key > root.value:
        root.right = bst_delete(root.right, key)
    elif root.left is None:
        return root.right
    elif root.right is None:
        return root.left
    else:
        successor = root.right
        while successor.left is not None:
            successor = successor.left
        root.value = successor.value
        root.right = bst_delete(root.right, successor.value)
    return root
