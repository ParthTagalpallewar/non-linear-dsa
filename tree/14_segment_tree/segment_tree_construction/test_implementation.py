from .implementation import segment_tree_construction


def test_builds_three_aggregates_and_empty_sum():
    values = [4, -2, 7, 3]
    for kind, expected in [("sum", 12), ("min", -2), ("max", 7)]:
        tree = segment_tree_construction(values, kind)
        assert tree.query(0, 4) == expected
    assert segment_tree_construction([]).query(0, 0) == 0
