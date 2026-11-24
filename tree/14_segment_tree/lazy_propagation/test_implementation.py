from .implementation import lazy_propagation


def test_overlapping_updates():
    assert lazy_propagation([1, 2, 3, 4], [(0, 4, 2), (1, 3, -1)]) == [18, 16]
