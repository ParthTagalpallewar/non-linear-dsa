from tree.nodes import BinaryNode

from .implementation import nodes_at_distance_k


def test_crosses_parent_and_preserves_duplicates():
    leaf, sibling = BinaryNode(4), BinaryNode(4)
    target = BinaryNode(2, leaf)
    root = BinaryNode(1, target, BinaryNode(3, sibling))
    assert nodes_at_distance_k(root, target, 0) == [target]
    assert nodes_at_distance_k(root, target, 1) == [leaf, root]
    assert nodes_at_distance_k(root, target, 3) == [sibling]
    assert nodes_at_distance_k(root, BinaryNode(2), 1) == []
