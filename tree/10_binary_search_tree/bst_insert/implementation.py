"""BST Insertion."""

from tree.nodes import BinaryNode


def bst_insert(root: BinaryNode | None, key: int) -> BinaryNode:
    """Insert a distinct key in place and return the root."""
    if root is None:
        return BinaryNode(key)
    current = root
    while current.value != key:
        if key < current.value:
            if current.left is None:
                current.left = BinaryNode(key)
                break
            current = current.left
        else:
            if current.right is None:
                current.right = BinaryNode(key)
                break
            current = current.right
    return root
