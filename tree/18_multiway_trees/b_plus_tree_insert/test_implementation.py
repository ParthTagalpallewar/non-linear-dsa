from random import Random

from tree.b_plus_tree import BPlusTree

from .implementation import b_plus_tree_insert


def test_occupancy_order_and_equal_leaf_depth_after_updates():
    rng = Random(811)
    for degree in (2, 3, 5):
        tree = BPlusTree(degree)
        expected = set()

        def verify():
            leaf_depths = set()
            leaves = []

            def visit(node, depth, is_root=False):
                assert node.keys == sorted(set(node.keys))
                assert len(node.keys) <= 2 * degree - 1
                if not is_root:
                    assert len(node.keys) >= degree - 1
                if not node.children:
                    leaf_depths.add(depth)
                    leaves.append(node)
                    assert node.minimum == (node.keys[0] if node.keys else None)
                    return node.keys.copy()
                assert len(node.children) == len(node.keys) + 1
                assert node.keys
                parts = [visit(child, depth + 1) for child in node.children]
                assert node.keys == [part[0] for part in parts[1:]]
                assert node.minimum == parts[0][0]
                return [key for part in parts for key in part]

            assert visit(tree.root, 0, True) == sorted(expected)
            assert len(leaf_depths) == 1
            for first, following in zip(leaves, leaves[1:], strict=False):
                assert first.next_leaf is following
            assert leaves[-1].next_leaf is None
            assert tree.range(10, 30) == sorted(v for v in expected if 10 <= v < 30)

        for key in range(55):
            assert b_plus_tree_insert(tree, key)
            expected.add(key)
            verify()
        for _ in range(370):
            key = rng.randrange(-5, 70)
            if rng.randrange(2):
                assert b_plus_tree_insert(tree, key) == (key not in expected)
                expected.add(key)
            else:
                assert tree.delete(key) == (key in expected)
                expected.discard(key)
            assert (key in tree) == (key in expected)
            verify()
        for key in sorted(expected):
            assert tree.delete(key)
        assert not tree.root.keys and not tree.root.children
