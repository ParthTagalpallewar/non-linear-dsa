from tree.nodes import BinaryNode

from .implementation import postorder_iterative


def test_traversal_order_with_missing_child():
    root = BinaryNode(1, BinaryNode(2, BinaryNode(4)), BinaryNode(3))
    assert postorder_iterative(root) == [4, 2, 3, 1]
    assert postorder_iterative(None) == []


def test_duplicate_values_are_preserved():
    assert postorder_iterative(BinaryNode(1, None, BinaryNode(1))) == [1, 1]
