from .implementation import binary_lifting


def test_power_of_two_entries_and_nonzero_root():
    graph = [[1], [0, 2], [1, 3], [2, 4], [3]]
    table = binary_lifting(graph, 4)
    assert table.up[0][0] == 1
    assert table.up[1][0] == 2
    assert table.up[2][0] == 4
    assert table.up[1][3] == -1
