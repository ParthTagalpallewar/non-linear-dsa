import pytest

from .implementation import dependency_resolution


def test_implicit_requirement_and_shared_dependency():
    order = dependency_resolution({"app": ["lib"], "tests": ["lib", "app"]})
    assert order == ["lib", "app", "tests"]
    assert dependency_resolution({}) == []


def test_cycle_raises():
    with pytest.raises(ValueError):
        dependency_resolution({"a": ["b"], "b": ["a"]})
