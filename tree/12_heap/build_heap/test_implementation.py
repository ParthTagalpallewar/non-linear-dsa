from .implementation import build_heap


def test_result_is_heap_with_all_duplicate_values():
    values = [5, 2, 2, 1, 8]
    result = build_heap(values)
    assert sorted(result) == sorted(values)
    assert all(result[(i - 1) // 2] <= result[i] for i in range(1, len(result)))
    assert values == [5, 2, 2, 1, 8]
    assert build_heap([]) == []
