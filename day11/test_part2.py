"""Tests for Advent of Code 2025 Day 11 Part 2."""

from day11.part2 import solve


def test_example():
    """Test the example from the puzzle description."""
    example = (
        "svr: aaa bbb\n"
        "aaa: fft\n"
        "fft: ccc\n"
        "bbb: tty\n"
        "tty: ccc\n"
        "ccc: ddd eee\n"
        "ddd: hub\n"
        "hub: fff\n"
        "eee: dac\n"
        "dac: fff\n"
        "fff: ggg hhh\n"
        "ggg: out\n"
        "hhh: out\n"
    )
    assert solve(example) == 2
