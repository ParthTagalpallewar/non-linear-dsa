from tree.nodes import BinaryNode

from .implementation import inorder_successor


def test_inexact_exact_and_absent_candidate():
    root = BinaryNode(4, BinaryNode(2), BinaryNode(6))
    assert inorder_successor(root, 5) == 6
    assert inorder_successor(root, 4) == 6
    assert inorder_successor(root, 10) is None
    assert inorder_successor(None, 5) is None
