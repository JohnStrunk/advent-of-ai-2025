"""Day 4 Part 1: Count accessible rolls of paper in a grid."""

ADJACENT_THRESHOLD = 4  # Forklifts can access if fewer than 4 adjacent rolls


def count_accessible_rolls(grid):
    """Count the number of accessible rolls of paper in the grid.

    A roll is accessible if there are fewer than ADJACENT_THRESHOLD '@' in the 8 adjacent cells.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    accessible = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue
            adj = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "@":
                        adj += 1
            if adj < ADJACENT_THRESHOLD:
                accessible += 1
    return accessible


def main():
    """Read the input file and print the number of accessible rolls."""
    with open("input.txt") as f:
        lines = [line.rstrip("\n") for line in f if line.strip()]
    maxlen = max(len(line) for line in lines)
    grid = [line.ljust(maxlen, ".") for line in lines]
    print(count_accessible_rolls(grid))


if __name__ == "__main__":
    main()
