"""Maximum XOR Using a Bitwise Trie."""

from tree.tries import BitwiseTrie


def maximum_xor(values: list[int]) -> int:
    """Return maximum XOR over distinct indices, or zero for fewer than two."""
    if any(value < 0 for value in values):
        raise ValueError("values must be nonnegative")
    if len(values) < 2:
        return 0
    trie = BitwiseTrie(max(1, max(values).bit_length()))
    trie.insert(values[0])
    answer = 0
    for value in values[1:]:
        answer = max(answer, trie.best_xor(value))
        trie.insert(value)
    return answer
