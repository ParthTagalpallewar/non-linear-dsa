"""Lowest Common Ancestor in a BST."""

from tree.nodes import BinaryNode


def lca_bst(root: BinaryNode | None, first: int, second: int) -> BinaryNode | None:
    """Find LCA by key in a strict BST, requiring both keys to exist."""

    def contains(node: BinaryNode | None, key: int) -> bool:
        while node is not None:
            if node.value == key:
                return True
            node = node.left if key < node.value else node.right
        return False

    low, high = sorted((first, second))
    while root is not None:
        if high < root.value:
            root = root.left
        elif low > root.value:
            root = root.right
        else:
            return root if contains(root, low) and contains(root, high) else None
    return None
