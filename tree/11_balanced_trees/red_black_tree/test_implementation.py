from random import Random

from .implementation import red_black_tree


def test_red_and_black_invariants_after_mixed_updates():
    rng = Random(513)
    tree = red_black_tree()
    expected = set()

    def inspect(node):
        if node is None:
            return 1, []
        assert node.right is None or not node.right.red
        if node.red:
            assert node.left is None or not node.left.red
        left_black, left_keys = inspect(node.left)
        right_black, right_keys = inspect(node.right)
        assert left_black == right_black
        return left_black + (not node.red), left_keys + [node.key] + right_keys

    def verify():
        assert tree.root is None or not tree.root.red
        assert inspect(tree.root)[1] == sorted(expected)

    for key in range(80, -1, -1):
        tree.insert(key)
        expected.add(key)
        verify()
    for _ in range(800):
        key = rng.randrange(120)
        if rng.randrange(2):
            tree.insert(key)
            expected.add(key)
        else:
            tree.delete(key)
            expected.discard(key)
        verify()
        assert (key in tree) == (key in expected)
    for key in sorted(expected):
        tree.delete(key)
    assert tree.root is None
