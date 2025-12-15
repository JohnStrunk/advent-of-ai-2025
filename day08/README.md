# Day 8: Playground

## Problem Summary

Connect junction boxes suspended in 3D space by making 1000 connections between
the closest pairs. Junction boxes connected by wires form circuits. Find the
product of the three largest circuit sizes.

## Approach

This is a classic graph connectivity problem solved using the Union-Find
(Disjoint Set Union) data structure:

1. **Parse coordinates**: Read junction box positions from input as (x, y, z)
   tuples
2. **Calculate distances**: Compute 3D Euclidean distance for all pairs of
   boxes
3. **Sort by distance**: Order pairs from closest to farthest
4. **Connect boxes**: Use Union-Find to connect the 1000 closest pairs,
   tracking which boxes are in the same circuit
5. **Find circuit sizes**: Group boxes by their root component to count circuit
   sizes
6. **Calculate answer**: Multiply the three largest circuit sizes

## Implementation Notes

- **Union-Find optimization**: Used path compression in `find()` and union by
  rank to keep operations nearly constant time
- **Distance formula**: Standard 3D Euclidean distance: sqrt((x2-x1)² +
  (y2-y1)² + (z2-z1)²)
- **Flexible connections**: The `solve()` function accepts `num_connections`
  parameter, allowing testing with the example (10 connections) and actual
  puzzle (1000 connections)
- **Time complexity**: O(n² log n) for distance calculation and sorting, which
  is efficient enough for 1000 boxes

## Answer

Part 1: **164475**
