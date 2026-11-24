from tree.nodes import BinaryNode

from .implementation import reverse_level_order


def test_orders_an_unbalanced_tree():
    root = BinaryNode(1, BinaryNode(2, BinaryNode(4)), BinaryNode(3))
    assert reverse_level_order(root) == [[4], [2, 3], [1]]


def test_empty_and_singleton():
    assert reverse_level_order(None) == []
    assert reverse_level_order(BinaryNode(8)) == [[8]]
