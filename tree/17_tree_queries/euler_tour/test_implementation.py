from .implementation import euler_tour


def test_return_steps_and_first_occurrences():
    walk, first = euler_tour([[1, 2], [0, 3, 4], [0], [1], [1]])
    assert walk == [0, 1, 3, 1, 4, 1, 0, 2, 0]
    assert first == [0, 1, 7, 2, 4]
    assert euler_tour([]) == ([], [])
