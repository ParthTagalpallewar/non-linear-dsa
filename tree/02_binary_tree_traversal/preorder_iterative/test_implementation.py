from tree.nodes import BinaryNode

from .implementation import preorder_iterative


def test_traversal_order_with_missing_child():
    root = BinaryNode(1, BinaryNode(2, BinaryNode(4)), BinaryNode(3))
    assert preorder_iterative(root) == [1, 2, 4, 3]
    assert preorder_iterative(None) == []


def test_duplicate_values_are_preserved():
    assert preorder_iterative(BinaryNode(1, None, BinaryNode(1))) == [1, 1]
