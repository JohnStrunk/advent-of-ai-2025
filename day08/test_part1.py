"""Tests for Day 8, Part 1."""

from day08.part1 import solve


def test_part1_example() -> None:
    """Test part 1 with the example input (10 connections, not 1000)."""
    # Example has 20 boxes and makes 10 connections, expecting answer 40
    result = solve("day08/test-input.txt", num_connections=10)
    assert result == 40
