"""B+ Tree."""

from tree.b_plus_tree import BPlusTree


def b_plus_tree(degree: int = 2) -> BPlusTree:
    """Create an empty B+ Tree using the specified minimum degree."""
    return BPlusTree(degree)


if __name__ == "__main__":
    tree = b_plus_tree()
    for key in (4, 2, 1, 3):
        tree.insert(key)
    print(tree.range(2, 5))
