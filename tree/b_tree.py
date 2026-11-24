"""A B-tree set with top-down insertion and deletion."""

from __future__ import annotations

from bisect import bisect_left
from dataclasses import dataclass, field


@dataclass
class BNode:
    """Sorted keys and, for internal nodes, one more child than keys."""

    keys: list[int] = field(default_factory=list)
    children: list[BNode] = field(default_factory=list)


class BTree:
    """Store distinct keys with between t−1 and 2t−1 keys per nonroot node."""

    def __init__(self, degree: int = 2) -> None:
        if degree < 2:
            raise ValueError("minimum degree must be at least two")
        self.degree = degree
        self.root = BNode()

    def __contains__(self, key: int) -> bool:
        node = self.root
        while True:
            slot = bisect_left(node.keys, key)
            if slot < len(node.keys) and node.keys[slot] == key:
                return True
            if not node.children:
                return False
            node = node.children[slot]

    def _split(self, node: BNode, index: int) -> None:
        child = node.children[index]
        middle = self.degree - 1
        promoted = child.keys[middle]
        sibling = BNode(child.keys[middle + 1 :], child.children[middle + 1 :])
        del child.keys[middle:]
        del child.children[middle + 1 :]
        node.keys.insert(index, promoted)
        node.children.insert(index + 1, sibling)

    def insert(self, key: int) -> bool:
        """Insert a distinct key and report whether the tree changed."""
        if key in self:
            return False
        if len(self.root.keys) == 2 * self.degree - 1:
            self.root = BNode(children=[self.root])
            self._split(self.root, 0)
        node = self.root
        while node.children:
            slot = bisect_left(node.keys, key)
            if len(node.children[slot].keys) == 2 * self.degree - 1:
                self._split(node, slot)
                if key > node.keys[slot]:
                    slot += 1
            node = node.children[slot]
        node.keys.insert(bisect_left(node.keys, key), key)
        return True

    def _merge(self, node: BNode, slot: int) -> BNode:
        left = node.children[slot]
        right = node.children.pop(slot + 1)
        left.keys.append(node.keys.pop(slot))
        left.keys.extend(right.keys)
        left.children.extend(right.children)
        return left

    def _prepare_child(self, node: BNode, slot: int) -> BNode:
        """Borrow or merge before descending into a minimum-size child."""
        child = node.children[slot]
        if len(child.keys) >= self.degree:
            return child
        if slot > 0 and len(node.children[slot - 1].keys) >= self.degree:
            left = node.children[slot - 1]
            child.keys.insert(0, node.keys[slot - 1])
            node.keys[slot - 1] = left.keys.pop()
            if left.children:
                child.children.insert(0, left.children.pop())
        elif slot + 1 < len(node.children) and (
            len(node.children[slot + 1].keys) >= self.degree
        ):
            right = node.children[slot + 1]
            child.keys.append(node.keys[slot])
            node.keys[slot] = right.keys.pop(0)
            if right.children:
                child.children.append(right.children.pop(0))
        else:
            return self._merge(node, slot if slot < len(node.keys) else slot - 1)
        return child

    def _delete(self, node: BNode, key: int) -> None:
        while True:
            slot = bisect_left(node.keys, key)
            if not node.children:
                node.keys.pop(slot)
                return
            if slot >= len(node.keys) or node.keys[slot] != key:
                node = self._prepare_child(node, slot)
                continue
            left, right = node.children[slot : slot + 2]
            if len(left.keys) >= self.degree:
                predecessor = left
                while predecessor.children:
                    predecessor = predecessor.children[-1]
                key = node.keys[slot] = predecessor.keys[-1]
                node = left
            elif len(right.keys) >= self.degree:
                successor = right
                while successor.children:
                    successor = successor.children[0]
                key = node.keys[slot] = successor.keys[0]
                node = right
            else:
                node = self._merge(node, slot)

    def delete(self, key: int) -> bool:
        """Delete key if present, borrowing or merging to prevent underflow."""
        if key not in self:
            return False
        self._delete(self.root, key)
        if not self.root.keys and self.root.children:
            self.root = self.root.children[0]
        return True
