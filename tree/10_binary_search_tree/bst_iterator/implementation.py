"""BST Iterator."""

from collections.abc import Iterator

from tree.nodes import BinaryNode


def bst_iterator(root: BinaryNode | None) -> Iterator[int]:
    """Yield increasing keys without materializing an inorder list."""
    stack: list[BinaryNode] = []
    while root is not None or stack:
        while root is not None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        yield root.value
        root = root.right
