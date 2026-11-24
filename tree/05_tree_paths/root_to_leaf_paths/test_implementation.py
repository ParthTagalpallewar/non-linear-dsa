from tree.nodes import BinaryNode

from .implementation import root_to_leaf_paths


def test_branching_tree_and_empty_root():
    root = BinaryNode(1, BinaryNode(2, BinaryNode(4)), BinaryNode(3))
    assert root_to_leaf_paths(root) == [[1, 2, 4], [1, 3]]
    assert root_to_leaf_paths(None) == []
