"""Bitwise Trie."""

from collections.abc import Iterable

from tree.tries import BitwiseTrie


def bitwise_trie(width: int, values: Iterable[int] = ()) -> BitwiseTrie:
    """Build a fixed-width binary trie indexing the supplied integers."""
    trie = BitwiseTrie(width)
    for value in values:
        trie.insert(value)
    return trie
