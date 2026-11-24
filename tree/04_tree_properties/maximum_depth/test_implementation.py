from tree.nodes import BinaryNode

from .implementation import maximum_depth


def test_short_and_long_leaf_depths():
    root = BinaryNode(1, BinaryNode(2, BinaryNode(4)), BinaryNode(3))
    assert maximum_depth(root) == 3
    assert maximum_depth(None) == 0


def test_single_child_is_not_a_leaf():
    assert maximum_depth(BinaryNode(1, BinaryNode(2))) == 2
