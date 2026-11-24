"""A B+ tree with leaf records and a linked leaf chain."""

from __future__ import annotations

from bisect import bisect_left, bisect_right
from dataclasses import dataclass, field


@dataclass
class BPlusNode:
    """Internal nodes store separators, leaves store actual keys."""

    keys: list[int] = field(default_factory=list)
    children: list[BPlusNode] = field(default_factory=list)
    next_leaf: BPlusNode | None = None
    minimum: int | None = None

    def refresh(self) -> None:
        """Set the minimum and derive separators from child minima."""
        if self.children:
            self.minimum = self.children[0].minimum
            self.keys = []
            for child in self.children[1:]:
                assert child.minimum is not None
                self.keys.append(child.minimum)
        else:
            self.minimum = self.keys[0] if self.keys else None


class BPlusTree:
    """Store distinct keys in linked, equal-depth leaves."""

    def __init__(self, degree: int = 2) -> None:
        if degree < 2:
            raise ValueError("minimum degree must be at least two")
        self.degree = degree
        self.root = BPlusNode()

    def _locate(self, key: int) -> tuple[BPlusNode, list[tuple[BPlusNode, int]]]:
        node = self.root
        path = []
        while node.children:
            slot = bisect_right(node.keys, key)
            path.append((node, slot))
            node = node.children[slot]
        return node, path

    def __contains__(self, key: int) -> bool:
        leaf, _ = self._locate(key)
        slot = bisect_left(leaf.keys, key)
        return slot < len(leaf.keys) and leaf.keys[slot] == key

    def range(self, start: int, stop: int) -> list[int]:
        """Return keys in [start, stop) by searching once, then scanning leaves."""
        if start >= stop:
            return []
        leaf, _ = self._locate(start)
        slot = bisect_left(leaf.keys, start)
        result = []
        current: BPlusNode | None = leaf
        while current is not None:
            for index in range(slot, len(current.keys)):
                key = current.keys[index]
                if key >= stop:
                    return result
                result.append(key)
            current = current.next_leaf
            slot = 0
        return result

    def _split(self, node: BPlusNode) -> BPlusNode | None:
        middle = self.degree
        if node.children:
            if len(node.children) <= 2 * middle:
                return None
            right = BPlusNode(children=node.children[middle:])
            del node.children[middle:]
        else:
            if len(node.keys) < 2 * middle:
                return None
            right = BPlusNode(node.keys[middle:], next_leaf=node.next_leaf)
            del node.keys[middle:]
            node.next_leaf = right
        node.refresh()
        right.refresh()
        return right

    def insert(self, key: int) -> bool:
        """Insert a record and propagate any splits upward."""
        leaf, path = self._locate(key)
        slot = bisect_left(leaf.keys, key)
        if slot < len(leaf.keys) and leaf.keys[slot] == key:
            return False
        leaf.keys.insert(slot, key)
        leaf.refresh()
        sibling = self._split(leaf)
        for parent, slot in reversed(path):
            if sibling is not None:
                parent.children.insert(slot + 1, sibling)
            parent.refresh()
            sibling = self._split(parent)
        if sibling is not None:
            self.root = BPlusNode(children=[self.root, sibling])
            self.root.refresh()
        return True

    def _minimum_size(self, node: BPlusNode) -> int:
        return self.degree if node.children else self.degree - 1

    @staticmethod
    def _items(node: BPlusNode) -> list[BPlusNode] | list[int]:
        return node.children if node.children else node.keys

    def _repair_child(self, parent: BPlusNode, slot: int) -> None:
        child = parent.children[slot]
        items = self._items(child)
        if len(items) >= self._minimum_size(child):
            return
        if slot > 0:
            left = parent.children[slot - 1]
            left_items = self._items(left)
            if len(left_items) > self._minimum_size(left):
                items.insert(0, left_items.pop())
                left.refresh()
                child.refresh()
                return
        if slot + 1 < len(parent.children):
            right = parent.children[slot + 1]
            right_items = self._items(right)
            if len(right_items) > self._minimum_size(right):
                items.append(right_items.pop(0))
                right.refresh()
                child.refresh()
                return
        left_slot = max(0, slot - 1)
        left = parent.children[left_slot]
        right = parent.children.pop(left_slot + 1)
        if left.children:
            left.children.extend(right.children)
        else:
            left.keys.extend(right.keys)
            left.next_leaf = right.next_leaf
        left.refresh()

    def delete(self, key: int) -> bool:
        """Delete a leaf record and repair occupancy as changes move upward."""
        leaf, path = self._locate(key)
        slot = bisect_left(leaf.keys, key)
        if slot == len(leaf.keys) or leaf.keys[slot] != key:
            return False
        leaf.keys.pop(slot)
        leaf.refresh()
        for parent, slot in reversed(path):
            self._repair_child(parent, slot)
            parent.refresh()
        if len(self.root.children) == 1:
            self.root = self.root.children[0]
        return True
