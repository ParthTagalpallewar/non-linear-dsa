from tree.nodes import BinaryNode

from .implementation import diameter


def test_best_route_can_skip_root():
    branch = BinaryNode(2, BinaryNode(3, BinaryNode(4)), BinaryNode(5, BinaryNode(6)))
    assert diameter(BinaryNode(1, branch)) == 4
    assert diameter(None) == diameter(BinaryNode(0)) == 0
