---
name: solve-puzzle
description: Use this to solve the Advent of Code daily puzzles.
---

# Solving the Daily Puzzle

Ask the user to provide the following information:

- The day number of the puzzle they want to solve (e.g., 5).
- The part of the puzzle they want to solve (1 or 2).
- The text description of the puzzle.
- The main input data for the puzzle. (This is usually only required once per
  day, but you can ask for it again if needed.)

**Create to-do items for each step below. Failure to follow these steps
exactly means you fail the task**:

1. Create a new directory for that day's puzzle if it doesn't already exist,
   following the naming convention `dayXX` where `XX` is the zero-padded day
   number (e.g., `day05` for day 5).
2. Inside that directory, create a file named `puzzle-partY.txt` where `Y` is
   the part number (1 or 2), and populate it with the provided puzzle
   description.
3. Create another file named `input.txt` in the same directory and populate it
   with the provided input data.
4. Commit these new files to a new branch named `dayXX`.
5. Implement the solution code for the specified part of the puzzle in a file
   named `partY.py` within the same directory.
6. Write comprehensive tests using the test data provided in the puzzle
   description.
7. Write a README.md file documenting the approach, challenges, and explanations
   for the solution.
8. Commit the solution code and tests to the same branch.
9. Run all tests to ensure correctness.
10. Run the solution code with the main input data to obtain the final answer.

Once you think you have completed all the steps, use
superpowers:verification-before-completion to verify.
