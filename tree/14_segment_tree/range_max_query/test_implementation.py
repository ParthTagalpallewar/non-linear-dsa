from tree.range_structures import SegmentTree

from .implementation import range_max_query


def test_query_spans_the_root_split():
    tree = SegmentTree([4, -2, 7, 3], "max")
    assert range_max_query(tree, 1, 3) == 7
    assert range_max_query(tree, 0, 1) == 4
