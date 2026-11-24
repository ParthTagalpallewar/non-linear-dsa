from tree.tries import Trie

from .implementation import trie_insert


def test_word_and_prefix_markers():
    trie = Trie()
    trie.insert("cat")
    trie_insert(trie, "car")
    trie_insert(trie, "")
    assert trie.walk("car").terminal and trie.root.terminal
