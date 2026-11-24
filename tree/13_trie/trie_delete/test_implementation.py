from tree.tries import Trie

from .implementation import trie_delete


def test_word_and_prefix_markers():
    trie = Trie()
    trie.insert("cat")
    trie.insert("ca")
    assert trie_delete(trie, "cat")
    assert trie.walk("cat") is None
    assert trie.walk("ca").terminal
    assert not trie_delete(trie, "cat")
