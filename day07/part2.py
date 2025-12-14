"""Day 7 Part 2: Count the number of timelines in a quantum tachyon manifold."""


def count_timelines(grid):
    """Count the number of unique timelines after quantum particle traversal.

    In a quantum manifold, the particle takes both left and right paths at
    each splitter. We use memoization to efficiently count all unique paths.
    """
    height = len(grid)
    width = len(grid[0])

    # Find the S position
    for y, row in enumerate(grid):
        if "S" in row:
            sx = row.index("S")
            sy = y
            break
    else:
        raise ValueError("No S found in grid")

    # Memoization cache: (x, y) -> number of timelines from this position
    memo = {}

    def count_from(x, y):
        """Recursively count timelines from position (x, y) moving downward."""
        # Check bounds - if we exit, this is 1 complete timeline
        if y >= height or x < 0 or x >= width:
            return 1

        # Check memo
        if (x, y) in memo:
            return memo[(x, y)]

        cell = grid[y][x]
        result = 0

        if cell == ".":
            # Continue downward
            result = count_from(x, y + 1)
        elif cell == "^":
            # Quantum split: add timelines from both left and right paths
            # From these new positions, beams continue downward
            result = count_from(x - 1, y) + count_from(x + 1, y)

        memo[(x, y)] = result
        return result

    # Start from position just below S
    return count_from(sx, sy + 1)


def main():
    """Read input.txt and print the number of timelines."""
    with open("input.txt") as f:
        grid = [line.rstrip("\n") for line in f if line.strip()]
    print(count_timelines(grid))


if __name__ == "__main__":
    main()
