"""Tests for Advent of Code 2025 Day 5 Part 1."""

import io
import sys
import tempfile

from part1 import solve


def test_example():
    """Test the example from the puzzle description."""
    example = """3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32\n"""
    expected = "3\n"
    with tempfile.NamedTemporaryFile(mode="w+t", delete=False) as f:
        f.write(example)
        f.flush()
        # Capture stdout
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        solve(f.name)
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
    assert output == expected
