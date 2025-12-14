"""Test for Day 4, Part 2 solution."""

import os
import subprocess


def test_part2_example():
    """Test part2.py using the example from the puzzle description."""
    input_data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
    expected = "43"  # From the example in the description
    with open("day04/test-input-part2.txt", "w") as f:
        f.write(input_data)
    result = subprocess.run(
        ["uv", "run", "day04/part2.py", "day04/test-input-part2.txt"],
        check=False,
        capture_output=True,
        text=True,
    )
    os.remove("day04/test-input-part2.txt")
    assert result.stdout.strip() == expected
