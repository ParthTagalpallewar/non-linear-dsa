"""BST Floor."""

from tree.nodes import BinaryNode


def bst_floor(root: BinaryNode | None, key: int) -> int | None:
    """Return the greatest key at most the target, or None."""
    best = None
    while root is not None:
        if root.value <= key:
            best = root.value
            root = root.right
        else:
            root = root.left
    return best
