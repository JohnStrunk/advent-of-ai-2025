"""Day 7 Part 1: Count the number of beam splits in the tachyon manifold grid."""


def count_splits(grid):
    """Count the number of splits as the beam traverses the grid."""
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

    # Each beam is (x, y, direction)
    # For part 1, all beams move downward (direction = 'down')
    beams = [(sx, sy + 1)]  # Start just below S
    split_count = 0
    visited = set()

    while beams:
        x, y = beams.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if y >= height:
            continue
        cell = grid[y][x]
        if cell == ".":
            beams.append((x, y + 1))
        elif cell == "^":
            split_count += 1
            # Split: left and right, if within bounds
            if x > 0:
                beams.append((x - 1, y))
            if x < width - 1:
                beams.append((x + 1, y))
        # else: ignore (shouldn't happen)
    return split_count


def main():
    """Read input.txt and print the number of splits."""
    with open("input.txt") as f:
        grid = [line.rstrip("\n") for line in f if line.strip()]
    print(count_splits(grid))


if __name__ == "__main__":
    main()
