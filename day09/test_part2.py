"""Tests for Day 9 Part 2: Movie Theater."""

from pathlib import Path

from day09.part2 import (
    build_edge_tiles,
    build_green_tiles,
    calculate_rectangle_area,
    find_largest_valid_rectangle,
    is_point_inside_polygon,
    is_rectangle_valid,
    parse_coordinates,
)


def test_parse_coordinates(tmp_path: Path) -> None:
    """Test parsing coordinates from a file."""
    test_file = tmp_path / "test.txt"
    test_file.write_text("1,2\n3,4\n5,6\n")

    coords = parse_coordinates(str(test_file))
    assert coords == [(1, 2), (3, 4), (5, 6)]


def test_build_edge_tiles() -> None:
    """Test building green tiles on edges."""
    # Simple square
    red_tiles = [(0, 0), (2, 0), (2, 2), (0, 2)]
    edges = build_edge_tiles(red_tiles)

    # Should have edges but not corners
    assert (1, 0) in edges  # Top edge
    assert (2, 1) in edges  # Right edge
    assert (1, 2) in edges  # Bottom edge
    assert (0, 1) in edges  # Left edge

    # Corners should not be in edges (they're red)
    assert (0, 0) not in edges
    assert (2, 0) not in edges
    assert (2, 2) not in edges
    assert (0, 2) not in edges


def test_is_point_inside_polygon() -> None:
    """Test point-in-polygon algorithm."""
    # Simple square from (0,0) to (4,4)
    square = [(0, 0), (4, 0), (4, 4), (0, 4)]

    # Points inside
    assert is_point_inside_polygon((2, 2), square)
    assert is_point_inside_polygon((1, 1), square)
    assert is_point_inside_polygon((3, 3), square)

    # Points outside
    assert not is_point_inside_polygon((5, 5), square)
    assert not is_point_inside_polygon((-1, 2), square)
    assert not is_point_inside_polygon((2, 5), square)

    # Points on boundary are tricky - ray casting may vary
    # but for our use case, we handle them separately


def test_build_green_tiles_example() -> None:
    """Test building green tiles with the puzzle example."""
    red_tiles = [
        (7, 1),
        (11, 1),
        (11, 7),
        (9, 7),
        (9, 5),
        (2, 5),
        (2, 3),
        (7, 3),
    ]

    green_tiles = build_green_tiles(red_tiles)

    # Check some edge tiles
    assert (8, 1) in green_tiles  # Edge from (7,1) to (11,1)
    assert (11, 3) in green_tiles  # Edge from (11,1) to (11,7)

    # Check some interior tiles
    assert (8, 4) in green_tiles  # Should be inside
    assert (10, 2) in green_tiles  # Should be inside

    # Red tiles should not be in green tiles
    assert (7, 1) not in green_tiles
    assert (11, 1) not in green_tiles


def test_calculate_rectangle_area() -> None:
    """Test rectangle area calculation."""
    assert calculate_rectangle_area((0, 0), (2, 2)) == 9
    assert calculate_rectangle_area((1, 1), (4, 5)) == 20
    assert calculate_rectangle_area((5, 5), (5, 5)) == 1


def test_is_rectangle_valid() -> None:
    """Test rectangle validation."""
    red_tiles = {(0, 0), (2, 0), (2, 2), (0, 2)}
    green_tiles = {(1, 0), (2, 1), (1, 2), (0, 1), (1, 1)}  # Edges + center

    # Rectangle with all red/green tiles
    assert is_rectangle_valid((0, 0), (2, 2), red_tiles, green_tiles)

    # Rectangle with only red corners
    assert is_rectangle_valid((0, 0), (2, 0), red_tiles, green_tiles)

    # Rectangle extending beyond red/green tiles
    assert not is_rectangle_valid((0, 0), (5, 5), red_tiles, green_tiles)


def test_find_largest_valid_rectangle_example() -> None:
    """Test with the example from the puzzle."""
    red_tiles = [
        (7, 1),
        (11, 1),
        (11, 7),
        (9, 7),
        (9, 5),
        (2, 5),
        (2, 3),
        (7, 3),
    ]

    # The largest valid rectangle has area 24
    assert find_largest_valid_rectangle(red_tiles) == 24


def test_find_largest_valid_rectangle_small() -> None:
    """Test with a small simple polygon."""
    # Simple square
    red_tiles = [(0, 0), (3, 0), (3, 3), (0, 3)]

    # The largest rectangle should be the full square: 4x4 = 16
    result = find_largest_valid_rectangle(red_tiles)
    assert result == 16


def test_with_test_input() -> None:
    """Test with the actual test input file."""
    test_file = Path(__file__).parent / "test-input.txt"
    expected_file = Path(__file__).parent / "test-output-part2.txt"

    red_tiles = parse_coordinates(str(test_file))
    result = find_largest_valid_rectangle(red_tiles)

    expected = int(expected_file.read_text().strip())
    assert result == expected
