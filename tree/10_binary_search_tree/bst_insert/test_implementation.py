from tree.nodes import BinaryNode

from .implementation import bst_insert


def test_leaf_insertion_and_duplicates():
    root = bst_insert(None, 4)
    assert isinstance(root, BinaryNode)
    assert bst_insert(root, 2) is root
    assert root.left is not None and root.left.value == 2
    child = root.left
    assert bst_insert(root, 2).left is child
    assert child.left is child.right is None
