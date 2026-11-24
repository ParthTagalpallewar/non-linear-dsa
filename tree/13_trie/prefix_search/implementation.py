"""Prefix Search."""

from tree.tries import Trie


def prefix_search(trie: Trie, word: str) -> bool:
    """Check whether the trie has a path for the given prefix."""
    return trie.walk(word) is not None
