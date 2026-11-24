from tree.nodes import BinaryNode

from .implementation import bottom_view


def test_shared_column_and_missing_children():
    root = BinaryNode(1, BinaryNode(2, BinaryNode(4), BinaryNode(5)), BinaryNode(3))
    assert bottom_view(root) == [4, 2, 5, 3]
    assert bottom_view(None) == []
