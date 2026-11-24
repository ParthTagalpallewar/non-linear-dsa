from .implementation import flood_fill


def test_fill_mutates_only_the_connected_region():
    image = [[1, 1, 0], [1, 0, 1]]
    assert flood_fill(image, (0, 0), 7) is image
    assert image == [[7, 7, 0], [7, 0, 1]]


def test_unchanged_color():
    assert flood_fill([[1]], (0, 0), 1) == [[1]]
