from tree.nodes import BinaryNode

from .implementation import longest_root_to_leaf_path


def test_branching_tree_and_empty_root():
    root = BinaryNode(1, BinaryNode(2, BinaryNode(4)), BinaryNode(3))
    assert longest_root_to_leaf_path(root) == [1, 2, 4]
    assert longest_root_to_leaf_path(None) == []
