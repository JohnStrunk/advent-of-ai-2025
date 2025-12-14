"""Day 4, Part 2: Iterative removal of accessible paper rolls."""

import sys

ADJACENT_THRESHOLD = 4  # Rolls with fewer than this many adjacent are accessible
EXPECTED_ARG_COUNT = 2  # Script name + input file


def main(filename):
    """Remove accessible rolls in rounds and print the total removed."""
    with open(filename) as f:
        grid = parse_grid(f.readlines())
    total_removed = 0
    while True:
        removed = remove_accessible(grid)
        if removed == 0:
            break
        total_removed += removed
    print(total_removed)


def parse_grid(lines):
    """Parse the input lines into a grid of characters."""
    return [list(line.strip()) for line in lines if line.strip()]


def count_adjacent(grid, r, c):
    """Count the number of adjacent '@' rolls around position (r, c)."""
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                if grid[nr][nc] == "@":
                    count += 1
    return count


def remove_accessible(grid):
    """Remove all accessible '@' rolls from the grid in one round. Return the count removed."""
    to_remove = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@" and count_adjacent(grid, r, c) < ADJACENT_THRESHOLD:
                to_remove.append((r, c))
    for r, c in to_remove:
        grid[r][c] = "."
    return len(to_remove)


if __name__ == "__main__":
    if len(sys.argv) != EXPECTED_ARG_COUNT:
        print(f"Usage: uv run {sys.argv[0]} <input_file>")
        sys.exit(1)
    main(sys.argv[1])
