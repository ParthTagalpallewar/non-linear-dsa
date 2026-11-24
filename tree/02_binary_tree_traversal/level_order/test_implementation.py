from tree.nodes import BinaryNode

from .implementation import level_order


def test_orders_an_unbalanced_tree():
    root = BinaryNode(1, BinaryNode(2, BinaryNode(4)), BinaryNode(3))
    assert level_order(root) == [[1], [2, 3], [4]]


def test_empty_and_singleton():
    assert level_order(None) == []
    assert level_order(BinaryNode(8)) == [[8]]
