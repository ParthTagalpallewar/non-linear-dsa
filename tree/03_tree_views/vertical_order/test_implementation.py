from tree.nodes import BinaryNode

from .implementation import vertical_order


def test_shared_column_and_missing_children():
    root = BinaryNode(1, BinaryNode(2, BinaryNode(4), BinaryNode(5)), BinaryNode(3))
    assert vertical_order(root) == [[4], [2], [1, 5], [3]]
    assert vertical_order(None) == []
