"""Trie Search."""

from tree.tries import Trie


def trie_search(trie: Trie, word: str) -> bool:
    """Check whether a whole word is stored."""
    node = trie.walk(word)
    return node is not None and node.terminal
