from tree.nodes import BinaryNode

from .implementation import bst_floor


def test_inexact_exact_and_absent_candidate():
    root = BinaryNode(4, BinaryNode(2), BinaryNode(6))
    assert bst_floor(root, 5) == 4
    assert bst_floor(root, 4) == 4
    assert bst_floor(root, 0) is None
    assert bst_floor(None, 5) is None
