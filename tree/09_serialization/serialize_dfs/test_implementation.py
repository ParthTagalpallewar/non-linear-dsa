import pytest

from tree.nodes import BinaryNode

from .implementation import deserialize_dfs, serialize_dfs


def test_round_trip_preserves_shape_and_values():
    root = BinaryNode(1, BinaryNode(2, BinaryNode(4)), BinaryNode(3))
    assert serialize_dfs(root) == "1,2,4,#,#,#,3,#,#"
    restored = deserialize_dfs(serialize_dfs(root))
    assert restored is not root
    assert serialize_dfs(restored) == "1,2,4,#,#,#,3,#,#"
    assert deserialize_dfs(serialize_dfs(None)) is None
    assert serialize_dfs(deserialize_dfs("-4,#,#")) == "-4,#,#"


def test_rejects_truncated_and_trailing_data():
    for data in ("1,#", "#,#", ""):
        with pytest.raises(ValueError):
            deserialize_dfs(data)
