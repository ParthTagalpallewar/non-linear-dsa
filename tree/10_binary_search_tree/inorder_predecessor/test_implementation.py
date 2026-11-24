from tree.nodes import BinaryNode

from .implementation import inorder_predecessor


def test_inexact_exact_and_absent_candidate():
    root = BinaryNode(4, BinaryNode(2), BinaryNode(6))
    assert inorder_predecessor(root, 5) == 4
    assert inorder_predecessor(root, 4) == 2
    assert inorder_predecessor(root, 0) is None
    assert inorder_predecessor(None, 5) is None
