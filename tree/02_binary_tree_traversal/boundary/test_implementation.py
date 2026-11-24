from tree.nodes import BinaryNode

from .implementation import boundary


def test_right_spine_turn_and_leaves():
    root = BinaryNode(
        1, BinaryNode(2, None, BinaryNode(4)), BinaryNode(3, BinaryNode(5))
    )
    assert boundary(root) == [1, 2, 4, 5, 3]


def test_empty_singleton_and_right_only():
    assert boundary(None) == []
    assert boundary(BinaryNode(1)) == [1]
    assert boundary(BinaryNode(1, None, BinaryNode(2, None, BinaryNode(3)))) == [
        1,
        3,
        2,
    ]
