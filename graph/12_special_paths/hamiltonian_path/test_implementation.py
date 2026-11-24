from .implementation import hamiltonian_path


def test_backtracks_from_dead_end():
    assert hamiltonian_path([[1, 2], [], [1]]) == [0, 2, 1]


def test_disconnected_graph_and_single_vertex():
    assert hamiltonian_path([[], []]) is None
    assert hamiltonian_path([[]]) == [0]
    assert hamiltonian_path([[0]]) == [0]
