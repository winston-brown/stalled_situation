import pytest

from stalls import choose_stall


@pytest.mark.parametrize(
    "stall_status, expected_index",
    [
        ("_", 0),                 # Single empty stall
        ("X", None),              # Single occupied stall
        ("__", 0),                # All empty -> leftmost
        ("X_X", 1),               # Only one empty in middle
        ("X__", 2),               # Farther from occupied (index 0) is index 2
        ("__X", 0),               # Farther from occupied (index 2) is index 0
        ("X_XX__X__", 8),         # Example-like string
        ("X__X", 1),              # Distances: index1->1, index2->1 -> tie -> leftmost (1)
        ("_X__", 3),              # Distances: 0->1, 2->1, 3->2 -> choose 3
        ("XX__XX", 2),            # Middle empty stalls, both equally close -> leftmost (2)
    ],
)
def test_choose_stall(stall_status, expected_index):
    assert choose_stall(stall_status) == expected_index
