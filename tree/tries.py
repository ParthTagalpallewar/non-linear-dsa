"""Reusable text and fixed-width binary tries."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TrieNode:
    """A character prefix with optional complete-word marker."""

    children: dict[str, TrieNode] = field(default_factory=dict)
    terminal: bool = False


class Trie:
    """Store distinct Python strings, including the empty string."""

    def __init__(self) -> None:
        self.root = TrieNode()

    def walk(self, prefix: str) -> TrieNode | None:
        """Return the node representing prefix, if present."""
        node = self.root
        for char in prefix:
            child = node.children.get(char)
            if child is None:
                return None
            node = child
        return node

    def insert(self, word: str) -> None:
        """Add missing edges and set the terminal marker."""
        node = self.root
        for char in word:
            child = node.children.get(char)
            if child is None:
                child = TrieNode()
                node.children[char] = child
            node = child
        node.terminal = True

    def delete(self, word: str) -> bool:
        """Remove the word and prune nodes with no other purpose."""
        node = self.root
        links = []
        for char in word:
            child = node.children.get(char)
            if child is None:
                return False
            links.append((node, char))
            node = child
        if not node.terminal:
            return False
        node.terminal = False
        for parent, char in reversed(links):
            child = parent.children[char]
            if child.terminal or child.children:
                break
            del parent.children[char]
        return True


@dataclass
class BitNode:
    """A prefix of fixed-width bits."""

    children: dict[int, BitNode] = field(default_factory=dict)


class BitwiseTrie:
    """Index nonnegative integers of a chosen fixed bit width."""

    def __init__(self, width: int) -> None:
        if width <= 0:
            raise ValueError("bit width must be positive")
        self.width = width
        self.root = BitNode()

    def _validate(self, value: int) -> None:
        if value < 0 or value.bit_length() > self.width:
            raise ValueError("value outside bit width")

    def insert(self, value: int) -> None:
        """Index a value from most to least significant bit."""
        self._validate(value)
        node = self.root
        for shift in range(self.width - 1, -1, -1):
            bit = (value >> shift) & 1
            child = node.children.get(bit)
            if child is None:
                child = BitNode()
                node.children[bit] = child
            node = child

    def best_xor(self, value: int) -> int:
        """Return the largest XOR score against an indexed value."""
        self._validate(value)
        if not self.root.children:
            raise ValueError("trie is empty")
        node = self.root
        score = 0
        for shift in range(self.width - 1, -1, -1):
            bit = (value >> shift) & 1
            other = bit ^ 1
            if other in node.children:
                score |= 1 << shift
                node = node.children[other]
            else:
                node = node.children[bit]
        return score
