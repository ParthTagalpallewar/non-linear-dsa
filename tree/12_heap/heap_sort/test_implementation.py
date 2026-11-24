from random import Random

from .implementation import heap_sort


def test_random_arrays_against_python_sort():
    rng = Random(2)
    for size in range(20):
        values = [rng.randint(-8, 8) for _ in range(size)]
        expected = sorted(values)
        heap_sort(values)
        assert values == expected
