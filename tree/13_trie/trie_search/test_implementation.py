from tree.tries import Trie

from .implementation import trie_search


def test_word_and_prefix_markers():
    trie = Trie()
    trie.insert("cat")
    assert trie_search(trie, "cat")
    assert not trie_search(trie, "ca")
    assert not trie_search(trie, "")
