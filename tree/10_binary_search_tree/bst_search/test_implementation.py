from tree.nodes import BinaryNode

from .implementation import bst_search


def test_search_finds_identity_and_missing_key():
    target = BinaryNode(3)
    root = BinaryNode(4, BinaryNode(2, None, target))
    assert bst_search(root, 3) is target
    assert bst_search(root, 1) is None
    assert bst_search(None, 3) is None
