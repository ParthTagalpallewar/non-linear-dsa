from tree.nodes import NaryNode

from .implementation import nary_traversal


def test_sibling_order_and_depth():
    root = NaryNode(1, [NaryNode(2, [NaryNode(5)]), NaryNode(3), NaryNode(4)])
    assert list(nary_traversal(root)) == [1, 2, 5, 3, 4]
    assert list(nary_traversal(None)) == []
