import pytest

from .implementation import dag_task_scheduling


def test_parallel_tasks_and_join():
    assert dag_task_scheduling([[2], [2], [3], [], []], [3, 7, 2, 0, 4]) == [
        3,
        7,
        9,
        9,
        4,
    ]


def test_invalid_durations_and_cycle():
    with pytest.raises(ValueError):
        dag_task_scheduling([[]], [-1])
    with pytest.raises(ValueError):
        dag_task_scheduling([[0]], [1])
