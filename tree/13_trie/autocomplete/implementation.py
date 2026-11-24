"""Autocomplete Using a Trie."""

from tree.tries import Trie, TrieNode


def autocomplete(trie: Trie, prefix: str, limit: int | None = None) -> list[str]:
    """Return at most limit matching words in Unicode lexicographic order."""
    if limit is not None and limit < 0:
        raise ValueError("limit must be nonnegative")
    root = trie.walk(prefix)
    if root is None or limit == 0:
        return []
    result: list[str] = []
    current = list(prefix)

    def visit(node: TrieNode) -> None:
        if node.terminal:
            result.append("".join(current))
        for char in sorted(node.children):
            if limit is not None and len(result) >= limit:
                return
            current.append(char)
            visit(node.children[char])
            current.pop()

    visit(root)
    return result
