# Advent of Code 2025 - Day 1 Part 1

This solution implements the safe dial rotation puzzle. The dial starts at 50,
and each rotation (L or R followed by a number) moves the dial left or right on
a circular dial from 0 to 99. The password is the number of times the dial
points at 0 after any rotation.

## Approach

- Parse each rotation from the input file.
- Update the dial position according to the direction and distance, wrapping
 around using modulo arithmetic.
- Count each time the dial lands on 0 after a rotation.

## Usage

Run the solution with:

```bash
uv run day01/part1.py input.txt
```

## Example

Given the following input:

```text
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
```

The output will be:

```text
3
```

## Notes

- The code is fully type-annotated and documented.
- All logic is contained in `part1.py` and does not depend on any external
 libraries beyond the Python standard library.
- See `test-input-1.txt` and `text-output-1.txt` for sample input and expected
 output.
