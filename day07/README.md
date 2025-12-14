
# Day 7: Laboratories

## Part 1: Classical Tachyon Manifold

### Part 1 Problem Summary

Given a grid representing a tachyon manifold, a beam enters at 'S' and moves
downward. It passes through '.' and splits at '^' into left and right beams
that continue downward from their new positions. Count the total number of
splits until all beams exit the grid.

### Part 1 Approach

- Parse the grid and locate 'S'.
- Simulate the downward beam, splitting at '^' into left/right beams.
- Track visited positions to avoid infinite loops.
- Count each split event.

### Part 1 Challenges

- Ensuring beams do not split infinitely or revisit the same cell.
- Handling edge cases at grid boundaries.

## Part 2: Quantum Tachyon Manifold

### Part 2 Problem Summary

In a quantum manifold, a single particle takes ALL possible paths
simultaneously. Each time it encounters a splitter (^), it creates separate
timelines by going both left and right. Count the total number of unique
timelines (complete paths through the manifold).

### Part 2 Approach

- Use recursive memoization to count paths efficiently.
- For each position (x, y):
  - If at '.': continue downward, return count from next position
  - If at '^': sum counts from both left and right positions
  - If exiting grid: return 1 (one complete timeline)
- Memoize results for each (x, y) to avoid recomputation.

### Part 2 Challenges

- Initial approach of tracking full path sequences caused exponential memory
  growth and timeouts.
- Solution: use memoization with position-based counting instead of path
  tracking.
- Key insight: from any position, the number of possible timelines is fixed
  regardless of how we got there, so we can memoize by position alone.

## Testing

- Part 1: Verified with sample (21 splits)
- Part 2: Verified with sample (40 timelines)
- All tests pass via pytest

## Usage

Run the solutions:

```sh
uv run day07/part1.py
uv run day07/part2.py
```

Run tests:

```sh
uv run -m pytest day07/
```
