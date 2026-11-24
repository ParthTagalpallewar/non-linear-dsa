from random import Random

from .implementation import b_tree


def test_occupancy_order_and_equal_leaf_depth_after_updates():
    rng = Random(811)
    for degree in (2, 3, 5):
        tree = b_tree(degree)
        expected = set()

        def verify():
            leaf_depths = set()

            def visit(node, depth, is_root=False):
                assert node.keys == sorted(set(node.keys))
                assert len(node.keys) <= 2 * degree - 1
                if not is_root:
                    assert len(node.keys) >= degree - 1
                if not node.children:
                    leaf_depths.add(depth)
                    return node.keys.copy()
                assert len(node.children) == len(node.keys) + 1
                assert node.keys
                parts = [visit(child, depth + 1) for child in node.children]
                result = parts[0]
                for key, part in zip(node.keys, parts[1:], strict=True):
                    result.extend([key, *part])
                return result

            assert visit(tree.root, 0, True) == sorted(expected)
            assert len(leaf_depths) == 1

        for key in range(55):
            assert tree.insert(key)
            expected.add(key)
            verify()
        for _ in range(370):
            key = rng.randrange(-5, 70)
            if rng.randrange(2):
                assert tree.insert(key) == (key not in expected)
                expected.add(key)
            else:
                assert tree.delete(key) == (key in expected)
                expected.discard(key)
            assert (key in tree) == (key in expected)
            verify()
        for key in sorted(expected):
            assert tree.delete(key)
        assert not tree.root.keys and not tree.root.children
