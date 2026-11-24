from random import Random

from .implementation import avl_updates


def test_balance_height_and_keys_after_mixed_updates():
    rng = Random(87)
    tree = avl_updates()
    expected = set()

    def inspect(node):
        if node is None:
            return 0, []
        left_height, left_keys = inspect(node.left)
        right_height, right_keys = inspect(node.right)
        assert abs(left_height - right_height) <= 1
        assert node.height == 1 + max(left_height, right_height)
        return node.height, left_keys + [node.key] + right_keys

    for key in range(80):
        tree.insert(key)
        expected.add(key)
        assert inspect(tree.root)[1] == sorted(expected)
    for _ in range(450):
        key = rng.randrange(100)
        if rng.randrange(2):
            tree.insert(key)
            expected.add(key)
        else:
            tree.delete(key)
            expected.discard(key)
        assert inspect(tree.root)[1] == sorted(expected)
        assert (key in tree) == (key in expected)
    for key in sorted(expected):
        tree.delete(key)
    assert tree.root is None
