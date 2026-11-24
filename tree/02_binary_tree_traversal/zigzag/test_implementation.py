from tree.nodes import BinaryNode

from .implementation import zigzag


def test_orders_an_unbalanced_tree():
    root = BinaryNode(1, BinaryNode(2, BinaryNode(4)), BinaryNode(3))
    assert zigzag(root) == [[1], [3, 2], [4]]


def test_empty_and_singleton():
    assert zigzag(None) == []
    assert zigzag(BinaryNode(8)) == [[8]]
