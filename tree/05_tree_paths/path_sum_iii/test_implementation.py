from tree.nodes import BinaryNode

from .implementation import path_sum_iii


def test_repeated_prefixes_and_sibling_isolation():
    root = BinaryNode(0, BinaryNode(0), BinaryNode(0))
    assert path_sum_iii(root, 0) == 5
    assert path_sum_iii(None, 0) == 0


def test_paths_can_start_below_root():
    assert path_sum_iii(BinaryNode(8, BinaryNode(-2, BinaryNode(5))), 3) == 1
