from tree.nodes import BinaryNode

from .implementation import distance_between_nodes


def test_edges_across_root_and_missing_node():
    first, second = BinaryNode(4), BinaryNode(3)
    root = BinaryNode(1, BinaryNode(2, first), second)
    assert distance_between_nodes(root, first, second) == 3
    assert distance_between_nodes(root, first, first) == 0
    assert distance_between_nodes(root, first, BinaryNode(4)) is None
