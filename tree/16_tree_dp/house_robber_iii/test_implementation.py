from tree.nodes import BinaryNode

from .implementation import house_robber_iii


def test_prefers_grandchild_and_skips_negative_root():
    root = BinaryNode(4, BinaryNode(2, BinaryNode(5)), BinaryNode(3))
    assert house_robber_iii(root) == 9
    assert house_robber_iii(BinaryNode(-1)) == 0
    assert house_robber_iii(None) == 0
