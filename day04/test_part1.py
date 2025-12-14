"""Test for day04 part1 solution."""

from day04.part1 import count_accessible_rolls


def test_accessible_rolls_sample() -> None:
    """Test the sample grid from the puzzle description."""
    sample: list[list[str]] = [
        list("..@@.@@@@."),
        list("@@@.@.@.@@"),
        list("@@@@@.@.@@"),
        list("@.@@@@..@."),
        list("@@.@@@@.@@"),
        list(".@@@@@@@.@"),
        list(".@.@.@.@@@"),
        list("@.@@@.@@@@"),
        list(".@@@@@@@@."),
        list("@.@.@@@.@."),
    ]
    assert count_accessible_rolls(sample) == 13
