from tree.range_structures import SegmentTree

from .implementation import range_min_query


def test_query_spans_the_root_split():
    tree = SegmentTree([4, -2, 7, 3], "min")
    assert range_min_query(tree, 1, 3) == -2
    assert range_min_query(tree, 0, 1) == 4
