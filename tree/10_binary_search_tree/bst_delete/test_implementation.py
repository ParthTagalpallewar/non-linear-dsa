from tree.nodes import BinaryNode

from .implementation import bst_delete


def test_deletes_root_with_two_children():
    root = BinaryNode(4, BinaryNode(2), BinaryNode(7, BinaryNode(5)))
    updated = bst_delete(root, 4)
    assert updated is root and root.value == 5
    assert root.right is not None and root.right.left is None
    assert bst_delete(root, 2).left is None


def test_root_with_one_child_and_missing_key():
    child = BinaryNode(1)
    root = BinaryNode(2, child)
    assert bst_delete(root, 8) is root
    assert bst_delete(root, 2) is child
    assert bst_delete(None, 0) is None
