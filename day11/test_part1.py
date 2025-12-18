"""
Unit tests for Advent of Code 2025 Day 11 Part 1 solution.

Tests the solve function for correct path counting from 'you' to 'out'.
"""

import unittest

from .part1 import solve


class TestPart1(unittest.TestCase):
    """Test cases for the solve function for Day 11 Part 1."""

    def test_example(self):
        """
        Test the example from the puzzle description.

        Verifies that the solve function returns 5 for the provided example input.
        """
        input_data = (
            "aaa: you hhh\n"
            "you: bbb ccc\n"
            "bbb: ddd eee\n"
            "ccc: ddd eee fff\n"
            "ddd: ggg\n"
            "eee: out\n"
            "fff: out\n"
            "ggg: out\n"
            "hhh: ccc fff iii\n"
            "iii: out"
        )
        expected = 5
        self.assertEqual(solve(input_data), expected)


if __name__ == "__main__":
    unittest.main()
