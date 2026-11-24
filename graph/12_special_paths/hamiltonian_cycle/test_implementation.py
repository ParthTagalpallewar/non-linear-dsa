from .implementation import hamiltonian_cycle


def test_backtracks_from_dead_end():
    assert hamiltonian_cycle([[1, 2], [0], [1]]) == [0, 2, 1, 0]


def test_disconnected_graph_and_single_vertex():
    assert hamiltonian_cycle([[], []]) is None
    assert hamiltonian_cycle([[]]) is None
    assert hamiltonian_cycle([[0]]) == [0, 0]
