
# Day 11

## Part 1

See previous section for details.

## Part 2

### Problem

Count all distinct paths from `svr` to `out` in a directed device graph,
but only those paths that visit both `dac` and `fft` (in any order).
    - Recursively explore all paths from `svr` to `out`.
    - Track the set of visited nodes to prevent cycles.
    - Track two booleans: whether `dac` and `fft` have been visited in the
       current path.
    - Only count a path if it reaches `out` and both `dac` and `fft` have
       been visited.
    - The search is pruned by not revisiting nodes in the current path
       (no cycles).
    - The solution is efficient for the expected input size, as the graph is
       not expected to be extremely large or cyclic.

### Approach

1. **Graph Construction:**
    - Parse the input into a directed graph where each device points to its
       possible next devices.

2. **Depth-First Search (DFS):**
    - Recursively explore all paths from `svr` to `out`.
    - Track the set of visited nodes to prevent cycles.
    - Track two booleans: whether `dac` and `fft` have been visited in the
       current path.
    - Only count a path if it reaches `out` and both `dac` and `fft` have been
       visited.

3. **Efficiency:**
      - The search is pruned by not revisiting nodes in the current path
         (no cycles).
      - The solution is efficient for the expected input size, as the graph is
         not
       expected to be extremely large or cyclic.

### Example

Given the sample in the puzzle, only 2 paths from `svr` to `out` visit both
`dac` and `fft`.

### Testing

Test cases are included for the example in the puzzle description.

### Challenges

- Ensuring that both required nodes are visited in any order before reaching
   `out`.
- Avoiding cycles in the graph.

### File Locations

- Solution: `day11/part2.py`
- Test: `day11/test_part2.py`
