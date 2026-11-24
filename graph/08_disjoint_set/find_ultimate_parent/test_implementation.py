from .implementation import find_ultimate_parent


def test_chain_and_separate_root():
    parent = [0, 0, 1, 3]
    assert find_ultimate_parent(parent, 2) == 0
    assert parent == [0, 0, 1, 3]
    assert find_ultimate_parent(parent, 3) == 3
