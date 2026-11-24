import pytest

from .implementation import smallest_equivalent_string


def test_transitive_replacements_and_unrelated_character():
    assert smallest_equivalent_string("bc", "ca", "cbaz") == "aaaz"


def test_empty_and_invalid_pairs():
    assert smallest_equivalent_string("", "", "") == ""
    with pytest.raises(ValueError):
        smallest_equivalent_string("a", "", "x")
