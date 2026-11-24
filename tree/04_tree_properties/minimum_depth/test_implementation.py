from tree.nodes import BinaryNode

from .implementation import minimum_depth


def test_short_and_long_leaf_depths():
    root = BinaryNode(1, BinaryNode(2, BinaryNode(4)), BinaryNode(3))
    assert minimum_depth(root) == 2
    assert minimum_depth(None) == 0


def test_single_child_is_not_a_leaf():
    assert minimum_depth(BinaryNode(1, BinaryNode(2))) == 2
