# Day 9: Movie Theater

## Part 1: Finding the Largest Rectangle

### Problem Summary

Given a grid of tiles where some are red (marked by coordinates), find the
largest rectangle that can be formed using any two red tiles as opposite
corners.

### Approach

The solution uses a brute-force approach:

1. **Parse Input**: Read all red tile coordinates from the input file.

2. **Calculate Rectangle Areas**: For each pair of tiles, calculate the area
   of the rectangle formed when those two tiles are opposite corners.

3. **Find Maximum**: Track and return the maximum area found.

### Key Insight: Inclusive Counting

The critical insight from the puzzle examples is that tiles are discrete grid
positions, and rectangles count tiles **inclusively**. This means:

- A rectangle from position (2,5) to (11,1) includes all positions from x=2
  to x=11 (10 tiles) and y=1 to y=5 (5 tiles)
- The formula is: `area = (|x2 - x1| + 1) x (|y2 - y1| + 1)`

Examples from the puzzle:

- Between (2,5) and (9,7): (9-2+1) x (7-5+1) = 8 x 3 = **24**
- Between (7,1) and (11,7): (11-7+1) x (7-1+1) = 5 x 7 = **35**
- Between (7,3) and (2,3): (7-2+1) x (3-3+1) = 6 x 1 = **6**
- Between (2,5) and (11,1): (11-2+1) x (5-1+1) = 10 x 5 = **50** (largest)

### Algorithm Complexity

- **Time Complexity**: O(n²) where n is the number of red tiles, since we
  check all pairs.
- **Space Complexity**: O(n) to store the coordinates.

For the input size (496 coordinates), this results in about 122,760
comparisons, which is easily manageable.

### Implementation Details

The solution is organized into three main functions:

1. `parse_coordinates(filename)`: Reads and parses coordinate pairs from the
   input file.
2. `calculate_rectangle_area(p1, p2)`: Calculates the inclusive area between
   two points.
3. `find_largest_rectangle(coordinates)`: Iterates through all pairs to find
   the maximum area.

### Running the Solution

```bash
uv run day09/part1.py day09/input.txt
```

### Testing

Tests cover:

- Rectangle area calculation with various coordinate configurations
- The example from the puzzle description
- Edge cases (same points, collinear points, negative coordinates)
- Parsing with empty lines

Run tests with:

```bash
uv run pytest day09/test_part1.py -v
```

## Part 2: Rectangles with Red and Green Tiles

### Part 2 Problem Summary

Part 2 adds the constraint that rectangles can only include red or green tiles.
The red tiles form a polygon (connected in order from the input), with green
tiles forming:

- **Edges**: Straight lines connecting consecutive red tiles
- **Interior**: All tiles inside the polygon

Rectangles must still have red tiles at opposite corners, but all other tiles
must be red or green.

### Part 2 Approach

The solution extends Part 1 by identifying valid tiles and filtering
rectangles:

1. **Identify Green Tiles**:
   - Build edge tiles by connecting consecutive red tiles
   - Use ray casting to identify interior tiles of the polygon

2. **Validate Rectangles**: For each pair of red tiles, check if all tiles in
   the rectangle are red or green

3. **Find Maximum**: Return the largest valid rectangle area

### Part 2 Key Insights

**Polygon Formation**: The red tiles form a rectilinear polygon (all edges are
horizontal or vertical) when connected in input order, wrapping from the last
to the first.

**Ray Casting Algorithm**: To determine if a point is inside the polygon, we
cast a ray from the point to infinity and count edge crossings. Odd crossings
= inside, even = outside.

**Edge Construction**: Since adjacent red tiles are on the same row or column,
edges are simple line segments with only horizontal or vertical tiles.

### Part 2 Algorithm Complexity

- **Preprocessing**: O(n × A) where n is the number of red tiles and A is the
  polygon's bounding box area (to identify all green tiles)
- **Rectangle Checking**: O(n² × R) where R is the average rectangle size
- **Space Complexity**: O(A) to store green tiles

For the input (496 red tiles, bounding box ~97K x 97K tiles), this is more
intensive than Part 1, but the actual polygon area is much smaller than the
bounding box.

### Part 2 Implementation Details

The solution is organized into several functions:

1. `build_edge_tiles(red_tiles)`: Creates green tiles on polygon edges
2. `is_point_inside_polygon(point, polygon)`: Ray casting algorithm
3. `build_green_tiles(red_tiles)`: Combines edges and interior tiles
4. `is_rectangle_valid(p1, p2, red, green)`: Checks if rectangle contains only
   valid tiles
5. `find_largest_valid_rectangle(red_tiles)`: Main algorithm

### Running Part 2

```bash
uv run day09/part2.py day09/input.txt
```

### Part 2 Testing

Tests cover:

- Edge tile construction for polygon boundaries
- Point-in-polygon algorithm with various test cases
- Green tile identification (edges + interior)
- Rectangle validation logic
- The example from the puzzle (expected area = 24)
- Simple polygon test cases

Run tests with:

```bash
uv run pytest day09/test_part2.py -v
```
