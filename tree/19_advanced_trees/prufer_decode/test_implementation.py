from importlib import import_module
from random import Random

import pytest

from .implementation import prufer_decode

encode = import_module(
    "tree.19_advanced_trees.prufer_encode.implementation"
).prufer_encode


def test_every_random_sequence_encodes_back_to_itself():
    rng = Random(11)
    for size in range(2, 45):
        code = [rng.randrange(size) for _ in range(size - 2)]
        assert encode(prufer_decode(code)) == code
    assert prufer_decode([]) == [[1], [0]]


def test_invalid_label():
    with pytest.raises(ValueError):
        prufer_decode([3])
