# Instructions for AI coding assistants

The following instructions **MUST** be followed by any AI coding assistant
when making changes to this repository.

## Project architecture

The major features and architectural decisions for this project are documented
in the [`design/`](design/) directory. Each feature and decision is captured
in a separate markdown file. These documents serve as a reference for
understanding the rationale behind various design choices and provide context
for future development.
**All changes must be consistent with these documents.**

Before making changes to the repository or adding new code:

- Review all existing decision records and feature descriptions in the `design/`
  directory. Changes and additions must align with these documents.
- If requirements or instructions from the user are ambiguous or incomplete,
  ask clarifying questions before proceeding.

## Repository structure

Each day of Advent of Code is organized into its own directory named `dayXX/`,
where `XX` is the two-digit day number (e.g., `day01`, `day02`, ..., `day25`).
Each day's directory contains the following files:

- `puzzle-part1.txt`: The text of that day's part1 challenge as provided by
  the Advent of Code website.
- `puzzle-part2.txt`: The text of that day's part2 challenge as provided by
  the Advent of Code website.
- `part1.py`: The solution code for part 1 of that day's challenge.
- `part2.py`: The solution code for part 2 of that day's challenge.
- `input.txt`: The input data for that day's challenge. There may be multiple
  input files if the challenge requires different inputs for different parts.
- `test-input.txt`: Sample input data for testing purposes.
- `test-output.txt`: Expected output for the sample input data.
- `README.md`: A markdown file documenting the solution approach, any
  challenges faced, and explanations of the code.
- `__init__.py`: This file allows Python to treat the directory as a package,
  ensuring proper module resolution during testing and execution. It can be
  empty or contain a simple docstring, such as:

  ```python
  """Day XX package init."""
  ```

Only code that is specific to a particular day's challenge should reside in
that day's directory. As much as possible, re-usable code should be placed in
a top-level `utils/` directory. The `utils/` code **must not** contain any
logic that is specific to a particular day's challenge, and **must not**
depend on any day-specific code.

Each day's solution code (`part1.py` and `part2.py`) should only depend on
standard libraries and the `utils/` code. There should be no dependencies
between different days' directories. If necessary, refactor common logic
into the `utils/` directory to avoid cross-day dependencies.

Each day's solution code should take a single input file (e.g., `input.txt` or
`test-input.txt`) and produce output directly to standard output. The code
should not read from or write to any other files.

You have a skill for solving these puzzles! Make sure you use it!

## Testing

Each day's directory must include test cases. The solution code should be
structured to facilitate easy testing and verification of correctness. Tests
should cover edge cases and typical scenarios as described in the puzzle text.
The tests for all days should be run when `pytest` is executed at the
repository root.

The `utils/` directory should also include unit tests for any utility
functions or classes. These tests should execute when `pytest` is run at the
repository root.

## Running Python code

All Python code in this repository must be run using uv. To run a Python file,
use the following command:

```bash
uv run path/to/file.py
```

ALL python code MUST be run using uv: `uv run ...`. This includes utilities
like formatters, linters, and test runners.

## Additional Requirements for Day Directories

To ensure consistent behavior and avoid import issues, each day's directory
**must** include an `__init__.py` file. This file allows Python to treat the
directory as a package, ensuring proper module resolution during testing and
execution. The `__init__.py` file can be empty or contain a simple docstring,
such as:

```python
"""Day XX package init."""
```

This practice prevents import conflicts and ensures that all test files can
locate the correct modules for each day.
