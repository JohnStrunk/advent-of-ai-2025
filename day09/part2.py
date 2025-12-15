#!/usr/bin/env python3
"""Day 9 Part 2: Movie Theater - Find largest rectangle using only red/green tiles."""

import sys


def parse_coordinates(filename: str) -> list[tuple[int, int]]:
    """Parse coordinate pairs from input file."""
    coordinates: list[tuple[int, int]] = []
    with open(filename) as f:
        for raw_line in f:
            line = raw_line.strip()
            if line:
                parts = line.split(",")
                x, y = int(parts[0]), int(parts[1])
                coordinates.append((x, y))
    return coordinates


def build_edge_tiles(red_tiles: list[tuple[int, int]]) -> set[tuple[int, int]]:
    """Build set of green tiles on edges connecting consecutive red tiles."""
    green_edges = set()
    n = len(red_tiles)

    for i in range(n):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[(i + 1) % n]  # Wrap around to first tile

        # Add all tiles on the line segment (excluding endpoints which are red)
        if x1 == x2:  # Vertical line
            for y in range(min(y1, y2) + 1, max(y1, y2)):
                green_edges.add((x1, y))
        else:  # Horizontal line
            for x in range(min(x1, x2) + 1, max(x1, x2)):
                green_edges.add((x, y1))

    return green_edges


def is_point_inside_polygon(
    point: tuple[int, int], polygon: list[tuple[int, int]]
) -> bool:
    """Check if point is inside polygon using ray casting algorithm."""
    x, y = point
    n = len(polygon)
    inside = False

    # Ray casting: count crossings of a ray from the point to the right
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]

        # Check if the edge crosses the horizontal ray from (x,y) to the right
        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
            inside = not inside

    return inside


def build_green_tiles(red_tiles: list[tuple[int, int]]) -> set[tuple[int, int]]:
    """Build set of all green tiles (edges + interior)."""
    green_tiles = build_edge_tiles(red_tiles)

    # Find bounding box
    min_x = min(x for x, y in red_tiles)
    max_x = max(x for x, y in red_tiles)
    min_y = min(y for x, y in red_tiles)
    max_y = max(y for x, y in red_tiles)

    # Check all points in bounding box
    red_set = set(red_tiles)
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            point = (x, y)
            if point not in red_set and is_point_inside_polygon(point, red_tiles):
                green_tiles.add(point)

    return green_tiles


def calculate_rectangle_area(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    """Calculate area of rectangle with opposite corners at p1 and p2."""
    x1, y1 = p1
    x2, y2 = p2
    width = abs(x2 - x1) + 1
    height = abs(y2 - y1) + 1
    return width * height


def is_rectangle_valid(
    p1: tuple[int, int],
    p2: tuple[int, int],
    red_tiles: set[tuple[int, int]],
    green_tiles: set[tuple[int, int]],
) -> bool:
    """Check if rectangle contains only red or green tiles."""
    x1, y1 = p1
    x2, y2 = p2

    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            point = (x, y)
            if point not in red_tiles and point not in green_tiles:
                return False

    return True


def find_largest_valid_rectangle(red_tiles: list[tuple[int, int]]) -> int:
    """Find largest rectangle with red corners containing only red/green tiles."""
    green_tiles = build_green_tiles(red_tiles)
    red_set = set(red_tiles)

    max_area = 0
    n = len(red_tiles)

    for i in range(n):
        for j in range(i + 1, n):
            if is_rectangle_valid(red_tiles[i], red_tiles[j], red_set, green_tiles):
                area = calculate_rectangle_area(red_tiles[i], red_tiles[j])
                max_area = max(max_area, area)

    return max_area


def main() -> None:
    """Read input and find the largest valid rectangle area."""
    if len(sys.argv) != 2:  # noqa: PLR2004
        print("Usage: python part2.py <input_file>", file=sys.stderr)
        sys.exit(1)

    red_tiles = parse_coordinates(sys.argv[1])
    result = find_largest_valid_rectangle(red_tiles)
    print(result)


if __name__ == "__main__":
    main()
