from tree.range_structures import FenwickTree

from .implementation import fenwick_range_sum


def test_range_sum():
    tree = FenwickTree([4, -2, 5, 1])
    assert fenwick_range_sum(tree, 1, 3) == 3
