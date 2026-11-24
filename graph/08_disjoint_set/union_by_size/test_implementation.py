from graph.disjoint_set import DisjointSet

from .implementation import union_by_size


def test_smaller_root_attaches_to_larger_root():
    sets = DisjointSet(4)
    assert union_by_size(sets, 1, 2)
    assert union_by_size(sets, 0, 2)
    root = sets.find(0)
    assert root == 1
    assert sets.size[root] == 3
    assert not union_by_size(sets, 1, 0)
    assert sets.size[root] == 3
