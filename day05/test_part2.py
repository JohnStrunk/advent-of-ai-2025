"""Tests for day05 part2 solution."""

import io

from day05.part2 import count_fresh_ids, merge_ranges


def test_example():
    """Test the example from the puzzle description."""
    data = """3-5
10-14
16-20
12-18
"""
    f = io.StringIO(data)
    ranges: list[tuple[int, int]] = []
    for file_line in f:
        line = file_line.strip()
        if not line:
            continue
        if "-" in line:
            start, end = map(int, line.split("-"))
            ranges.append((start, end))
    assert count_fresh_ids(ranges) == 14


def test_merge_overlap():
    """Test merging of overlapping ranges."""
    ranges: list[tuple[int, int]] = [(1, 3), (2, 5), (10, 12)]
    merged: list[tuple[int, int]] = merge_ranges(ranges)
    assert merged == [(1, 5), (10, 12)]  # Corrected to tuple format
    assert count_fresh_ids(ranges) == 8
