"""Test for day04 part1 solution."""

import part1


def test_accessible_rolls_sample():
    """Test the sample grid from the puzzle description."""
    sample = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]
    assert part1.count_accessible_rolls(sample) == 13
