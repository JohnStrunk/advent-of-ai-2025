"""Pytest for Advent of Code 2025 Day 1 Part 1.

Validates the solution against the provided test input and expected output.
"""

import io

from day01 import part1


def test_count_zero_positions():
    """Test that count_zero_positions returns correct count for sample input."""
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
    expected_output = 3
    f = io.StringIO(test_input)
    assert part1.count_zero_positions(f) == expected_output
