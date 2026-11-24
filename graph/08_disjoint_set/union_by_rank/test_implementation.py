from .implementation import RankDisjointSet


def test_rank_increases_only_for_equal_roots():
    sets = RankDisjointSet(4)
    assert sets.union(0, 1)
    assert sets.union(2, 3)
    assert sets.union(0, 2)
    assert sets.rank[sets.find(3)] == 2
    assert not sets.union(1, 3)
    assert sets.rank[sets.find(0)] == 2
