from .implementation import minimum_cut


def test_residual_cut_and_exhaustive_capacity():
    edges = [(0, 1, 3), (1, 2, 2), (0, 2, 1), (2, 0, 10)]
    value, side, crossing = minimum_cut(3, edges, 0, 2)
    assert side == {0, 1}
    assert crossing == [1, 2]
    assert value == sum(edges[index][2] for index in crossing) == 3


def test_cut_can_have_zero_capacity():
    assert minimum_cut(2, [(0, 1, 0)], 0, 1) == (0, {0}, [0])
