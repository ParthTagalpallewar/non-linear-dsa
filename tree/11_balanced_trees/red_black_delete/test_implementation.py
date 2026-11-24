from tree.red_black import RedBlackTree

from .implementation import red_black_delete


def test_deletes_root_and_ignores_absent_key():
    tree = RedBlackTree()
    for key in (4, 2, 6, 1, 3, 5, 7):
        tree.insert(key)
    assert tree.root is not None
    former_root = tree.root.key
    red_black_delete(tree, former_root)
    assert former_root not in tree
    assert all(key in tree for key in range(1, 8) if key != former_root)
    red_black_delete(tree, 99)
    for key in range(1, 8):
        red_black_delete(tree, key)
    assert tree.root is None
