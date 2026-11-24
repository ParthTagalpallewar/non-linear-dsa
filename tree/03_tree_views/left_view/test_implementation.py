from tree.nodes import BinaryNode

from .implementation import left_view


def test_deepest_node_can_come_from_either_side():
    root = BinaryNode(1, BinaryNode(2, BinaryNode(4)), BinaryNode(3))
    assert left_view(root) == [1, 2, 4]
    assert left_view(None) == []
