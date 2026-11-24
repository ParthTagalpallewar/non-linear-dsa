"""BST Search."""

from tree.nodes import BinaryNode


def bst_search(root: BinaryNode | None, key: int) -> BinaryNode | None:
    """Return the node with key or None."""
    while root is not None and root.value != key:
        root = root.left if key < root.value else root.right
    return root
