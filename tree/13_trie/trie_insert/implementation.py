"""Trie Insertion."""

from tree.tries import Trie


def trie_insert(trie: Trie, word: str) -> None:
    """Add a whole word while sharing existing prefix nodes."""
    trie.insert(word)
