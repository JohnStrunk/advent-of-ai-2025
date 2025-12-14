"""Tests for day07 part1 solution."""

from day07.part1 import count_splits


def test_sample():
    """Test the sample grid from the puzzle description (should split 21 times)."""
    grid = [
        ".......S.......",
        "...............",
        ".......^.......",
        "...............",
        "......^.^......",
        "...............",
        ".....^.^.^.....",
        "...............",
        "....^.^...^....",
        "...............",
        "...^.^...^.^...",
        "...............",
        "..^...^.....^..",
        "...............",
        ".^.^.^.^.^...^.",
        "...............",
    ]
    assert count_splits(grid) == 21
