"""
Day 2 Part 1: Find and sum all invalid product IDs in the given ranges.

An invalid ID is a number made by repeating a sequence of digits twice.
"""


def is_invalid_id(n: int) -> bool:
    """Return True if n is a number made by repeating a sequence of digits twice."""
    s = str(n)
    length = len(s)
    if length % 2 != 0:
        return False
    half = length // 2
    return s[:half] == s[half:]


def main():
    """Read input ranges, find and sum all invalid product IDs, and print the result."""
    with open("input.txt") as f:
        ranges = f.read().strip().split(",")
    total = 0
    RANGE_SPLIT_COUNT = 2
    for r in ranges:
        if not r:
            continue
        start_end = r.split("-")
        if len(start_end) != RANGE_SPLIT_COUNT:
            continue
        start, end = map(int, start_end)
        for n in range(start, end + 1):
            if is_invalid_id(n):
                total += n
    print(total)


if __name__ == "__main__":
    main()
