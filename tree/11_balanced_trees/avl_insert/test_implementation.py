from tree.avl import AVLTree

from .implementation import avl_insert


def test_sorted_insertions_duplicate_and_order():
    tree = AVLTree()
    for key in range(40):
        avl_insert(tree, key)
    avl_insert(tree, 19)
    assert all(key in tree for key in range(40))
    assert 40 not in tree
    assert tree.root is not None and tree.root.key not in (0, 39)
