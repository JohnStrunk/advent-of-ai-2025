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
    green_edges: set[tuple[int, int]] = set()
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


def is_tile_valid(
    point: tuple[int, int],
    red_tiles_set: set[tuple[int, int]],
    green_edges: set[tuple[int, int]],
    polygon: list[tuple[int, int]],
    bbox: tuple[int, int, int, int] | None = None,
) -> bool:
    """Check if a tile is red or green (edge or interior)."""
    # O(1) checks first
    if point in red_tiles_set or point in green_edges:
        return True

    # Quick bounding box check before expensive ray-casting
    if bbox is not None:
        min_x, max_x, min_y, max_y = bbox
        x, y = point
        if x < min_x or x > max_x or y < min_y or y > max_y:
            return False

    # O(n) ray-casting only when necessary
    return is_point_inside_polygon(point, polygon)


def build_green_tiles(red_tiles: list[tuple[int, int]]) -> set[tuple[int, int]]:
    """Build set of all green tiles (edges + interior).

    Note: This is only used for testing. For large inputs, use is_tile_valid
    instead to avoid pre-computing all interior tiles.
    """
    green_tiles = build_edge_tiles(red_tiles)

    # Find bounding box
    min_x = min(x for x, _ in red_tiles)
    max_x = max(x for x, _ in red_tiles)
    min_y = min(y for _, y in red_tiles)
    max_y = max(y for _, y in red_tiles)

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
    red_tiles_set: set[tuple[int, int]],
    green_edges: set[tuple[int, int]],
    polygon: list[tuple[int, int]],
) -> bool:
    """Check if rectangle contains only red or green tiles.

    NOTE: This function checks all tiles in the rectangle. It's kept for
    backward compatibility with existing tests. For production use,
    prefer is_rectangle_valid_boundary_only() which is much faster.
    """
    x1, y1 = p1
    x2, y2 = p2

    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    # Check all tiles
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            point = (x, y)
            if not is_tile_valid(point, red_tiles_set, green_edges, polygon):
                return False

    return True


def is_rectangle_valid_boundary_only(  # noqa: PLR0913
    p1: tuple[int, int],
    p2: tuple[int, int],
    red_tiles_set: set[tuple[int, int]],
    green_edges: set[tuple[int, int]],
    polygon: list[tuple[int, int]],
    bbox: tuple[int, int, int, int] | None = None,
) -> bool:
    """Check if rectangle perimeter contains only red or green tiles.

    For simply-connected regions (no holes), if the perimeter is valid,
    the interior must also be valid. This is much faster than checking
    all tiles: O(perimeter) vs O(area).
    """
    x1, y1 = p1
    x2, y2 = p2

    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    # Check top edge: y=min_y, x from min_x to max_x
    for x in range(min_x, max_x + 1):
        if not is_tile_valid((x, min_y), red_tiles_set, green_edges, polygon, bbox):
            return False

    # Check bottom edge: y=max_y, x from min_x to max_x
    for x in range(min_x, max_x + 1):
        if not is_tile_valid((x, max_y), red_tiles_set, green_edges, polygon, bbox):
            return False

    # Check left edge: x=min_x, y from min_y+1 to max_y-1 (skip corners)
    for y in range(min_y + 1, max_y):
        if not is_tile_valid((min_x, y), red_tiles_set, green_edges, polygon, bbox):
            return False

    # Check right edge: x=max_x, y from min_y+1 to max_y-1 (skip corners)
    for y in range(min_y + 1, max_y):
        if not is_tile_valid((max_x, y), red_tiles_set, green_edges, polygon, bbox):
            return False

    return True


def is_point_in_rectangle(
    point: tuple[int, int], corner1: tuple[int, int], corner2: tuple[int, int]
) -> bool:
    """Check if point is strictly inside rectangle (not on boundary)."""
    x, y = point
    x1, y1 = corner1
    x2, y2 = corner2

    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    # Strictly inside means not touching the boundary
    return min_x < x < max_x and min_y < y < max_y


def find_largest_valid_rectangle(red_tiles: list[tuple[int, int]]) -> int:
    """Find largest rectangle with red corners containing only red/green tiles.

    Uses two-phase validation: fast rejection for red tiles inside,
    then boundary checking for perimeter tiles.
    """
    green_edges = build_edge_tiles(red_tiles)
    red_set = set(red_tiles)

    # Pre-compute bounding box for polygon
    min_x = min(x for x, _ in red_tiles)
    max_x = max(x for x, _ in red_tiles)
    min_y = min(y for _, y in red_tiles)
    max_y = max(y for _, y in red_tiles)
    bbox = (min_x, max_x, min_y, max_y)

    max_area = 0
    n = len(red_tiles)

    for i in range(n):
        for j in range(i + 1, n):
            area = calculate_rectangle_area(red_tiles[i], red_tiles[j])

            # Skip if area is too small to improve our result
            if area <= max_area:
                continue

            # Phase 1: Fast rejection - check if any red tile is inside
            has_red_inside = False
            for k in range(n):
                if k not in (i, j):
                    if is_point_in_rectangle(red_tiles[k], red_tiles[i], red_tiles[j]):
                        has_red_inside = True
                        break

            if has_red_inside:
                continue

            # Phase 2: Check perimeter (with early termination)
            if is_rectangle_valid_boundary_only(
                red_tiles[i], red_tiles[j], red_set, green_edges, red_tiles, bbox
            ):
                max_area = area

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
