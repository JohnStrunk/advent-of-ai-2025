"""Tests for day07 part2 solution."""

from day07.part2 import count_timelines


def test_sample():
    """Test the sample grid from the puzzle (should have 40 timelines)."""
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
    assert count_timelines(grid) == 40
