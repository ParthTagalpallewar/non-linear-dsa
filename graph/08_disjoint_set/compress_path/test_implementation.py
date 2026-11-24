from .implementation import compress_path


def test_chain_and_separate_root():
    parent = [0, 0, 1, 3]
    assert compress_path(parent, 2) == 0
    assert parent == [0, 0, 0, 3]
    assert compress_path(parent, 3) == 3
