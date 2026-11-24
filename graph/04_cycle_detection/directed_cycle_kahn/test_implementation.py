from .implementation import directed_cycle_kahn


def test_cycle_with_incoming_and_outgoing_tails():
    assert directed_cycle_kahn([[1], [2], [1, 3], []])
    assert not directed_cycle_kahn([[1, 1], [], []])


def test_empty_and_loop():
    assert not directed_cycle_kahn([])
    assert directed_cycle_kahn([[0]])
