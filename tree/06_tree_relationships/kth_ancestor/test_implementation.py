from tree.nodes import BinaryNode

from .implementation import kth_ancestor


def test_zero_exact_and_too_many_steps():
    leaf = BinaryNode(4)
    root = BinaryNode(1, BinaryNode(2, leaf))
    assert kth_ancestor(root, leaf, 0) is leaf
    assert kth_ancestor(root, leaf, 2) is root
    assert kth_ancestor(root, leaf, 3) is None
    assert kth_ancestor(root, BinaryNode(4), 0) is None
