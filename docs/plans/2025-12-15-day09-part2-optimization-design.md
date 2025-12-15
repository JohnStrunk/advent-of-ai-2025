# Day 9 Part 2 Optimization Design

**Date:** 2025-12-15

**Problem:** Current implementation uses arbitrary area limit and is too slow
for large rectangles

**Solution:** Boundary-only validation algorithm

## Problem Analysis

### Current Implementation Issues

1. **Artificial limit:** `max_reasonable_area = 500000` is a code smell
   - Filters valid rectangles arbitrarily
   - Fragile - breaks if answer exceeds limit
   - No algorithmic justification

2. **Performance bottleneck:** Checking every tile in rectangle
   - For 500K tile rectangle: 500,000 point-in-polygon tests
   - Each test is O(n) ray-casting where n = polygon vertices
   - Unacceptably slow for large valid rectangles

3. **Complexity:** O(n² × area) where n = red tiles, area = rectangle size
   - 122,760 rectangle pairs × up to 500K tiles each
   - Even with early termination, checking large rectangles dominates runtime

## Proposed Solution: Boundary-Only Validation

### Core Insight

For a simply-connected region (no holes), if all tiles along a rectangle's
perimeter are valid, then all interior tiles must also be valid.

**Why this works:**

- Red tiles form a closed polygon
- Green tiles = polygon edges + interior
- Valid region (red ∪ green) is simply-connected by problem definition
- Geometric guarantee: valid perimeter → valid interior

### Performance Improvement

**Current approach:** Check all tiles = O(width × height)
**New approach:** Check perimeter only = O(2×width + 2×height)

**Example:** 707×707 rectangle (~500K tiles)

- Current: 500,000 tile checks
- New: ~2,828 tile checks
- **Speedup: ~177×**

### Algorithm

```python
def is_rectangle_valid_boundary_only(p1, p2, red_set, green_edges, polygon):
    """Check if rectangle perimeter contains only red/green tiles."""
    x1, y1 = p1
    x2, y2 = p2
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    # Check top edge: y=min_y, x from min_x to max_x
    for x in range(min_x, max_x + 1):
        if not is_tile_valid((x, min_y), red_set, green_edges, polygon):
            return False

    # Check bottom edge: y=max_y, x from min_x to max_x
    for x in range(min_x, max_x + 1):
        if not is_tile_valid((x, max_y), red_set, green_edges, polygon):
            return False

    # Check left edge: x=min_x, y from min_y+1 to max_y-1
    for y in range(min_y + 1, max_y):
        if not is_tile_valid((min_x, y), red_set, green_edges, polygon):
            return False

    # Check right edge: x=max_x, y from min_y+1 to max_y-1
    for y in range(min_y + 1, max_y):
        if not is_tile_valid((max_x, y), red_set, green_edges, polygon):
            return False

    return True
```

### Optimized Tile Validation

Most perimeter tiles are likely red or green edges (O(1) lookup), with only
occasional interior points requiring expensive ray-casting:

```python
def is_tile_valid(point, red_set, green_edges, polygon):
    # O(1) checks first - most perimeter tiles hit these
    if point in red_set or point in green_edges:
        return True

    # O(n) ray-casting only for interior points
    return is_point_inside_polygon(point, polygon)
```

## Implementation Plan

### Changes Required

1. **Add new function:** `is_rectangle_valid_boundary_only()`
   - Implements perimeter-checking logic
   - Reuses existing `is_tile_valid()` helper

2. **Update main algorithm:** `find_largest_valid_rectangle()`
   - Replace `is_rectangle_valid()` with boundary-only version
   - Remove `max_reasonable_area` limit entirely
   - Remove sample point checking (no longer needed)
   - Keep "skip if area <= max_area" optimization (still valid)

3. **Clean up dead code:**
   - Remove sample point checking logic from old function
   - Remove `max_reasonable_area` variable
   - Keep old `is_rectangle_valid()` for now (used by tests)

### Testing Strategy

**Unit Tests:**

- Small rectangles: boundary-only matches full checking
- Large rectangles: returns correct result
- Edge cases: single-tile, thin rectangles (1×N, N×1)

**Regression Tests:**

- All existing tests must pass
- Example (area=24) must work
- Test input file result must match

**Performance Verification:**

- Run on actual input (496 red tiles)
- Should complete without timeout (<30 seconds target)
- No artificial limits required

## Complexity Analysis

### Before Optimization

- Rectangle pairs: O(n²) where n = 496 red tiles = 122,760 pairs
- Per rectangle: O(area) where area can be up to 500K tiles
- Total: O(n² × max_area) = potentially billions of operations

### After Optimization

- Rectangle pairs: O(n²) = 122,760 pairs (unchanged)
- Per rectangle: O(perimeter) = O(width + height) ≈ O(√area)
- Total: O(n² × √max_area) = much more manageable

### Expected Runtime

With 122,760 pairs and average perimeter ~1,000 tiles:

- ~122 million tile checks (vs billions)
- Most are O(1) set lookups
- Should complete in seconds, not minutes

## Risks & Mitigations

**Risk:** Assumption that valid region has no holes could be wrong

**Mitigation:** Problem guarantees polygon interior is fully green; validate
with tests

**Risk:** Boundary checking has bugs in edge coordinate logic

**Mitigation:** Comprehensive unit tests, compare against full checking on
small examples

**Risk:** Performance still insufficient
**Mitigation:** Profile if needed, but 177× speedup should be more than adequate

## Success Criteria

1. ✅ No artificial area limits in code
2. ✅ All existing tests pass
3. ✅ Runs on actual input in <30 seconds
4. ✅ Returns correct answer (498648)
5. ✅ Code is cleaner and more maintainable
