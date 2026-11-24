from .implementation import fenwick_construction


def test_linear_build_stores_lowbit_blocks():
    tree = fenwick_construction([3, 1, 4, 2, 8])
    assert tree.data == [0, 3, 4, 4, 10, 8]
    assert fenwick_construction([]).prefix_sum(0) == 0
