from tree.red_black import RedBlackTree

from .implementation import red_black_insert


def test_sorted_insertions_duplicate_and_order():
    tree = RedBlackTree()
    for key in range(40):
        red_black_insert(tree, key)
    red_black_insert(tree, 19)
    assert all(key in tree for key in range(40))
    assert 40 not in tree
    assert tree.root is not None and tree.root.key not in (0, 39)
