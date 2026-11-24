from tree.tries import Trie

from .implementation import prefix_search


def test_word_and_prefix_markers():
    trie = Trie()
    trie.insert("cat")
    assert prefix_search(trie, "ca")
    assert prefix_search(trie, "")
    assert not prefix_search(trie, "cb")
