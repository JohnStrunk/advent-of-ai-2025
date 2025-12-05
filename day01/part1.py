"""Solution for Advent of Code 2025 Day 1, Part 1: Safe Dial Rotations.

This script reads a sequence of dial rotations from an input file and counts how many times the dial points at 0 after any rotation.

Usage:
    uv run day01/part1.py input.txt

The input file should contain one rotation per line, e.g.:
    L68
    R10
    ...
"""

import sys
from typing import TextIO

DIAL_SIZE = 100
START_POSITION = 50


def count_zero_positions(input_file: TextIO) -> int:
    """Count the number of times the dial points at 0 after a rotation.

    :param input_file: File-like object containing rotations, one per line.
    :return: Number of times the dial points at 0 after a rotation.
    """
    position = START_POSITION
    zero_count = 0
    for rotation_line in input_file:
        line = rotation_line.strip()
        if not line:
            continue
        direction = line[0]
        try:
            distance = int(line[1:])
        except ValueError:
            raise ValueError(f"Invalid rotation value: {line}")
        if direction == "L":
            position = (position - distance) % DIAL_SIZE
        elif direction == "R":
            position = (position + distance) % DIAL_SIZE
        else:
            raise ValueError(f"Invalid rotation direction: {direction}")
        if position == 0:
            zero_count += 1
    return zero_count


def main() -> None:
    """Run the safe dial rotation solution."""
    expected_arg_count = 2
    if len(sys.argv) != expected_arg_count:
        print("Usage: uv run day01/part1.py <input_file>", file=sys.stderr)
        sys.exit(1)
    input_path = sys.argv[1]
    with open(input_path, "r", encoding="utf-8") as f:
        result = count_zero_positions(f)
    print(result)


if __name__ == "__main__":
    main()
