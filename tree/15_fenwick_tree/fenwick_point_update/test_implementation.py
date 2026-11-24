from tree.range_structures import FenwickTree

from .implementation import fenwick_point_update


def test_point_update():
    tree = FenwickTree([4, -2, 5, 1])
    fenwick_point_update(tree, 2, -4)
    assert tree.prefix_sum(3) == 3
