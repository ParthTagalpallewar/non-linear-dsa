from tree.tries import Trie

from .implementation import autocomplete


def test_prefix_word_sorting_and_limits():
    trie = Trie()
    for word in ("cat", "car", "ca", "cab", "dog"):
        trie.insert(word)
    assert autocomplete(trie, "ca", 3) == ["ca", "cab", "car"]
    assert autocomplete(trie, "cat") == ["cat"]
    assert autocomplete(trie, "z") == []
    assert autocomplete(trie, "", 0) == []
