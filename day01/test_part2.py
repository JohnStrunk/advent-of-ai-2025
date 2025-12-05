"""Pytest for Advent of Code 2025 Day 1 Part 2.

Validates the solution against the provided test input and expected output.
"""

import io

from day01 import part2


def test_count_all_zero_positions():
    """Test that count_all_zero_positions returns correct count for sample input."""
    test_input = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""
    expected_output = 6
    f = io.StringIO(test_input)
    assert part2.count_all_zero_positions(f) == expected_output
