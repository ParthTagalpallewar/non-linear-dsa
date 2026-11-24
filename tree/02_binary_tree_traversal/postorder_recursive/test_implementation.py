from tree.nodes import BinaryNode

from .implementation import postorder_recursive


def test_traversal_order_with_missing_child():
    root = BinaryNode(1, BinaryNode(2, BinaryNode(4)), BinaryNode(3))
    assert postorder_recursive(root) == [4, 2, 3, 1]
    assert postorder_recursive(None) == []


def test_duplicate_values_are_preserved():
    assert postorder_recursive(BinaryNode(1, None, BinaryNode(1))) == [1, 1]
