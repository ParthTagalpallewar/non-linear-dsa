from tree.nodes import BinaryNode

from .implementation import inorder_iterative


def test_traversal_order_with_missing_child():
    root = BinaryNode(1, BinaryNode(2, BinaryNode(4)), BinaryNode(3))
    assert inorder_iterative(root) == [4, 2, 1, 3]
    assert inorder_iterative(None) == []


def test_duplicate_values_are_preserved():
    assert inorder_iterative(BinaryNode(1, None, BinaryNode(1))) == [1, 1]
