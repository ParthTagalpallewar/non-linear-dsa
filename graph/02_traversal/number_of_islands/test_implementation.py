from .implementation import number_of_islands


def test_adjacent_and_diagonal_land():
    grid = [[1, 1, 0], [0, 0, 1], [1, 0, 1]]
    assert number_of_islands(grid) == 3
    assert grid[0] == [1, 1, 0]


def test_empty_and_all_water():
    assert number_of_islands([]) == 0
    assert number_of_islands([[0, 0]]) == 0
