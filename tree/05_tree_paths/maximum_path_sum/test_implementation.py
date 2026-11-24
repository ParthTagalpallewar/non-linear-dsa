from tree.nodes import BinaryNode

from .implementation import maximum_path_sum


def test_paths_can_turn_below_root():
    root = BinaryNode(-10, BinaryNode(4, BinaryNode(8), BinaryNode(7)))
    assert maximum_path_sum(root) == 19


def test_all_negative_and_empty():
    assert maximum_path_sum(BinaryNode(-3, BinaryNode(-2))) == -2
    assert maximum_path_sum(None) is None
