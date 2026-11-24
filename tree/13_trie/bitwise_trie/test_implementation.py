import pytest

from .implementation import bitwise_trie


def test_leading_zero_and_width_validation():
    trie = bitwise_trie(3, [0, 4, 7])
    assert trie.best_xor(2) == 6
    with pytest.raises(ValueError):
        trie.insert(8)
    with pytest.raises(ValueError):
        bitwise_trie(0)
