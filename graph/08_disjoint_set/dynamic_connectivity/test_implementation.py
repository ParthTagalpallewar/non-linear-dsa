import pytest

from .implementation import dynamic_connectivity


def test_queries_see_only_prior_additions():
    operations = [
        ("connected", 0, 2),
        ("add", 0, 1),
        ("add", 1, 2),
        ("connected", 0, 2),
        ("connected", 0, 3),
    ]
    assert dynamic_connectivity(4, operations) == [False, True, False]


def test_unknown_operation():
    with pytest.raises(ValueError):
        dynamic_connectivity(2, [("remove", 0, 1)])
