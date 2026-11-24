from .implementation import edge_list


def test_preserves_order_weights_and_parallel_edges():
    edges = [(0, 1, -5), (0, 1, 0), (1, 0, 2)]
    assert edge_list(3, iter(edges)) == edges


def test_rejects_negative_endpoint():
    try:
        edge_list(2, [(-1, 0, 1)])
    except ValueError:
        return
    raise AssertionError("negative endpoint should be rejected")
