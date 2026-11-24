"""Trie Deletion."""

from tree.tries import Trie


def trie_delete(trie: Trie, word: str) -> bool:
    """Remove a stored word while retaining all shared prefixes."""
    return trie.delete(word)
