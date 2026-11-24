from .implementation import multi_source_bfs


def test_multiple_sources_and_duplicate_source():
    assert multi_source_bfs({0: [1], 1: [2], 3: [2]}, [0, 3, 0]) == {
        0: 0,
        3: 0,
        1: 1,
        2: 1,
    }


def test_no_sources():
    assert multi_source_bfs({2: [1]}, []) == {}
