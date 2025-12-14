"""Unit tests for day03 part2 solution."""

from day03.part2 import largest_12_digit_number


def test_largest_12_digit_number_examples():
    """Test largest_12_digit_number with puzzle description examples."""
    assert largest_12_digit_number("987654321111111") == 987654321111
    assert largest_12_digit_number("811111111111119") == 811111111119
    assert largest_12_digit_number("234234234234278") == 434234234278
    assert largest_12_digit_number("818181911112111") == 888911112111


def test_largest_12_digit_number_edge_cases():
    """Test largest_12_digit_number with edge case inputs."""
    # All digits the same
    assert largest_12_digit_number("111111111111111") == 111111111111
    # Already 12 digits
    assert largest_12_digit_number("123456789012") == 123456789012
    # Descending order
    assert largest_12_digit_number("98765432109876543210") == 989876543210
    # Ascending order
    assert largest_12_digit_number("12345678901234567890") == 901234567890
