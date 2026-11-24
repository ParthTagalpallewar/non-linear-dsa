from tree.range_structures import SegmentTree

from .implementation import point_update


def test_replacement_after_pending_range_addition():
    tree = SegmentTree([4, 3, 2], "min")
    tree.range_add(0, 3, 3)
    point_update(tree, 1, -1)
    assert tree.query(0, 3) == -1
    assert tree.query(0, 1) == 7
