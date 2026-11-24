"""Lexicographically Smallest Equivalent String."""

from graph.disjoint_set import DisjointSet


def smallest_equivalent_string(first: str, second: str, text: str) -> str:
    """Replace each character by the minimum in its equivalence class."""
    if len(first) != len(second):
        raise ValueError("equivalence strings must have equal lengths")
    alphabet = sorted(set(first + second + text))
    indices = {char: index for index, char in enumerate(alphabet)}
    sets = DisjointSet(len(alphabet))
    for left, right in zip(first, second, strict=True):
        sets.union(indices[left], indices[right])
    minimum: dict[int, str] = {}
    for char in alphabet:
        minimum.setdefault(sets.find(indices[char]), char)
    return "".join(minimum[sets.find(indices[char])] for char in text)
