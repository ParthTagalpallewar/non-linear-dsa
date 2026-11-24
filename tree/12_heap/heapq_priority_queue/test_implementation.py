from .implementation import heapq_priority_queue


def test_ties_keep_arrival_order():
    tasks = [(3, "z"), (1, "first"), (1, "second"), (0, "urgent")]
    assert heapq_priority_queue(tasks) == ["urgent", "first", "second", "z"]
    assert heapq_priority_queue([]) == []
