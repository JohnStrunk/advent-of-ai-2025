"""
Tests for Day 10, Part 1.

This module contains test cases for the solution to Part 1 of Day 10.
"""

from day10.part1 import solve


def test_solve():
    """Test the solve function with example input."""
    example_input = (
        "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}\n"
        "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}\n"
        "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"
    )
    expected_output = 7
    assert solve(example_input) == expected_output
