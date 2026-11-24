from tree.nodes import BinaryNode

from .implementation import bst_ceil


def test_inexact_exact_and_absent_candidate():
    root = BinaryNode(4, BinaryNode(2), BinaryNode(6))
    assert bst_ceil(root, 5) == 6
    assert bst_ceil(root, 4) == 4
    assert bst_ceil(root, 10) is None
    assert bst_ceil(None, 5) is None
