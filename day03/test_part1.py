"""Unit tests for day03 part1 solution."""

from part1 import max_joltage_from_bank


def test_max_joltage_from_bank():
    """Test the max_joltage_from_bank function with provided and edge case examples."""
    # Provided examples
    assert max_joltage_from_bank("987654321111111") == 98
    assert max_joltage_from_bank("811111111111119") == 89
    assert max_joltage_from_bank("234234234234278") == 78
    assert max_joltage_from_bank("818181911112111") == 92
    # Edge cases
    assert max_joltage_from_bank("12") == 12
    assert max_joltage_from_bank("21") == 21
    assert max_joltage_from_bank("99") == 99
    assert max_joltage_from_bank("11") == 11
    assert max_joltage_from_bank("123456789") == 89
