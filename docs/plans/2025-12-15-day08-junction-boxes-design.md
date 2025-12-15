# Day 8: Junction Box Circuits Design

## Problem Summary

Connect 1000 pairs of junction boxes (closest pairs first) and find the
product of the three largest circuit sizes.

## Approach

Use Union-Find (Disjoint Set Union) to efficiently track connected components
as we make connections.

## Data Structures

### Union-Find Class

- **Purpose**: Track which junction boxes are in the same circuit
- **Operations**:
  - `find(x)`: Find root of box x with path compression
  - `union(x, y)`: Connect two boxes, merging their circuits
- **Optimizations**:
  - Path compression: flatten tree during find operations
  - Union by rank: keep trees balanced

### Input Data

- List of (x, y, z) tuples representing junction box coordinates
- Box ID is the index in the list

## Algorithm Flow

1. **Parse input**: Read coordinates from file, parse as integer tuples
2. **Calculate all pairwise distances**:
   - For all pairs (i, j) where i < j
   - Distance = sqrt((x2-x1)² + (y2-y1)² + (z2-z1)²)
   - Store as (distance, box1_id, box2_id)
3. **Sort distances**: Ascending order
4. **Make 1000 connections**:
   - Initialize Union-Find with all boxes
   - Take first 1000 pairs from sorted list
   - Call union() for each pair
5. **Count circuit sizes**:
   - For each box, find its root
   - Group boxes by root to get circuit sizes
6. **Calculate answer**:
   - Sort circuit sizes descending
   - Multiply the three largest

## Complexity

- **Time**: O(n² log n) for distance calculation and sorting
- **Space**: O(n²) for storing all distances
- **With n=1000**: ~500K distance calculations, very manageable

## Implementation Notes

- Union-Find makes connecting and checking connectivity near-constant time
- We don't need to check if union() succeeds (puzzle mentions some pairs are
  already connected)
- 3D Euclidean distance formula for calculating distances
