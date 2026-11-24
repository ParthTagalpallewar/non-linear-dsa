from .implementation import BasicDisjointSet


def test_merges_and_redundant_union():
    sets = BasicDisjointSet(4)
    assert sets.union(0, 1)
    assert sets.union(2, 1)
    assert sets.find(0) == sets.find(1) == sets.find(2) == 2
    assert not sets.union(1, 2)
    assert sets.find(3) == 3
