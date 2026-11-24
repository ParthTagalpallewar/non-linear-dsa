from tree.nodes import BinaryNode

from .implementation import path_sum_ii


def test_branching_tree_and_empty_root():
    root = BinaryNode(1, BinaryNode(2, BinaryNode(4)), BinaryNode(3))
    assert path_sum_ii(root, 7) == [[1, 2, 4]]
    assert path_sum_ii(None, 7) == []
