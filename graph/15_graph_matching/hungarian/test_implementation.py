from itertools import permutations
from random import Random

import pytest

from .implementation import hungarian


def test_rectangular_assignments_against_exhaustive_permutations():
    rng = Random(32)
    for rows in range(1, 5):
        for _ in range(12):
            columns = rows + 1
            cost = [[rng.randint(-6, 6) for _ in range(columns)] for _ in range(rows)]
            value, assignment = hungarian(cost)
            assert len(set(assignment)) == rows
            assert value == sum(
                cost[row][target] for row, target in enumerate(assignment)
            )
            assert value == min(
                sum(cost[row][target] for row, target in enumerate(candidate))
                for candidate in permutations(range(columns), rows)
            )


def test_empty_and_infeasible_matrix():
    assert hungarian([]) == (0, [])
    with pytest.raises(ValueError):
        hungarian([[0], [1]])
