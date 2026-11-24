from itertools import combinations
from random import Random

from .implementation import maximum_xor


def test_against_pair_enumeration():
    rng = Random(8)
    for size in range(18):
        values = [rng.randrange(64) for _ in range(size)]
        assert maximum_xor(values) == max(
            (a ^ b for a, b in combinations(values, 2)), default=0
        )
    assert maximum_xor([0, 0, 0]) == 0
