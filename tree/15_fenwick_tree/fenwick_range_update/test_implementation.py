from random import Random

from tree.range_structures import RangeFenwick

from .implementation import fenwick_range_update


def test_overlapping_intervals_against_plain_list():
    rng = Random(900)
    values = [rng.randrange(-5, 6) for _ in range(18)]
    tree = RangeFenwick(values)
    for _ in range(90):
        left, right = sorted(rng.sample(range(19), 2))
        delta = rng.randrange(-5, 6)
        fenwick_range_update(tree, left, right, delta)
        for index in range(left, right):
            values[index] += delta
        start, stop = sorted(rng.sample(range(19), 2))
        assert tree.range_sum(start, stop) == sum(values[start:stop])
    assert tree.range_sum(0, 18) == sum(values)
    assert RangeFenwick([]).prefix_sum(0) == 0
