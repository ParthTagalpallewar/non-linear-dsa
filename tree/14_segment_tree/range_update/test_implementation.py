from random import Random

from tree.range_structures import SegmentTree

from .implementation import range_update


def test_overlapping_updates_against_a_list():
    rng = Random(9)
    for kind, aggregate in (("sum", sum), ("min", min), ("max", max)):
        values = [rng.randrange(11) for _ in range(17)]
        tree = SegmentTree(values, kind)
        for _ in range(110):
            left = rng.randrange(len(values))
            right = rng.randrange(left + 1, len(values) + 1)
            delta = rng.randrange(-10, 11)
            range_update(tree, left, right, delta)
            for index in range(left, right):
                values[index] += delta
            start = rng.randrange(len(values))
            stop = rng.randrange(start + 1, len(values) + 1)
            assert tree.query(start, stop) == aggregate(values[start:stop])
