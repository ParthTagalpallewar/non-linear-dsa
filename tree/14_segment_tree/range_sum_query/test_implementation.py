from tree.range_structures import SegmentTree

from .implementation import range_sum_query


def test_query_spans_the_root_split():
    tree = SegmentTree([4, -2, 7, 3], "sum")
    assert range_sum_query(tree, 1, 3) == 5
    assert range_sum_query(tree, 0, 1) == 4
