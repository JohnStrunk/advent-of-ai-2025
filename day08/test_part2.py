"""Tests for Day 8, Part 2."""

from day08.part2 import solve


def test_part2_example() -> None:
    """Test part 2 with the example input."""
    result = solve("day08/test-input.txt")
    assert result == 25272  # 216 * 117
