"""Solution for Advent of Code 2025 Day 5 Part 1."""


def solve(input_file):
    """Count how many available ingredient IDs are fresh."""
    ranges = []
    ids = []
    with open(input_file) as f:
        content = f.read().split("\n")
    try:
        blank_idx = content.index("")
    except ValueError:
        blank_idx = len(content)
    for line in content[:blank_idx]:
        if "-" in line:
            start, end = map(int, line.split("-"))
            ranges.append((start, end))
    for line in content[blank_idx + 1 :]:
        if line.strip():
            ids.append(int(line.strip()))
    fresh_count = 0
    for id_ in ids:
        for start, end in ranges:
            if start <= id_ <= end:
                fresh_count += 1
                break
    print(fresh_count)


if __name__ == "__main__":
    import sys

    solve(sys.argv[1])
