from .implementation import undirected_cycle_dsu


def test_first_redundant_edge():
    assert not undirected_cycle_dsu(4, [(0, 1), (2, 3)])
    assert undirected_cycle_dsu(4, [(0, 1), (1, 2), (2, 0)])


def test_loop_and_parallel_edges():
    assert undirected_cycle_dsu(1, [(0, 0)])
    assert undirected_cycle_dsu(2, [(0, 1), (1, 0)])
