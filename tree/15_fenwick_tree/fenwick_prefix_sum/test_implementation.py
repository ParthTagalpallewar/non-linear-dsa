from tree.range_structures import FenwickTree

from .implementation import fenwick_prefix_sum


def test_prefix_sum():
    tree = FenwickTree([4, -2, 5, 1])
    assert fenwick_prefix_sum(tree, 3) == 7
