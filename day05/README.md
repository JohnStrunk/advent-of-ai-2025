
# Day 5 Part 1 Solution

## Problem Summary

Given a list of inclusive ingredient ID ranges and a list of available
ingredient IDs, count how many available IDs are 'fresh' (i.e., fall within
any of the ranges).

## Approach

1. **Parse Input:**
   - Read the input file and split it into two sections: ranges and IDs.
   - Ranges are parsed as tuples of (start, end).
   - IDs are parsed as integers.
2. **Check Freshness:**
   - For each available ID, check if it falls within any of the given ranges.
   - Count the number of IDs that are fresh.
3. **Output:**
   - Print the count of fresh IDs.

## Example

Input:

```text
3-5
10-14
16-20
12-18

1
5
8
11
17
32
```

Output:

```text
3
```

## Testing

- The solution is tested with the example from the puzzle description.
- To run the test: `uv run -m pytest day05/test_part1.py`

## Notes

- The solution handles overlapping and single-value ranges.
- The code is structured for easy testing and verification.
