"""AVL Tree."""

from tree.avl import AVLTree


def avl_tree() -> AVLTree:
    """Create an empty AVL search set."""
    return AVLTree()


if __name__ == "__main__":
    tree = avl_tree()
    for key in (3, 2, 1):
        tree.insert(key)
    print(tree.root)
