"""Day 6 - Part 1 Solution: Solve worksheet by reading numbers vertically in each problem group."""


def solve(input_lines: list[str]) -> int:
    """Solve the worksheet for part 1 rules."""
    rows: list[str] = [line.rstrip("\n") for line in input_lines]
    if not rows:
        return 0
    n_rows: int = len(rows)
    n_cols: int = max(len(row) for row in rows)
    # Pad all rows to the same length
    rows = [row.ljust(n_cols) for row in rows]
    problems: list[tuple[list[int], str]] = []
    col: int = 0
    while col < n_cols:
        # Find the start of a problem (not all spaces in the number rows)
        if all(rows[r][col] == " " for r in range(n_rows - 1)):
            col += 1
            continue
        # Collect columns for this problem until we hit a full space column
        problem_cols: list[int] = []
        while col < n_cols and not all(rows[r][col] == " " for r in range(n_rows - 1)):
            problem_cols.append(col)
            col += 1
        # Extract numbers and operator
        numbers: list[int] = []
        for r in range(n_rows - 1):
            num_str: str = "".join(rows[r][c] for c in problem_cols).strip()
            if num_str:
                numbers.append(int(num_str))
        op: str = "".join(rows[n_rows - 1][c] for c in problem_cols).strip()
        problems.append((numbers, op))
    # Now solve each problem
    total: int = 0
    for numbers, op in problems:
        if op == "+":
            total += sum(numbers)
        elif op == "*":
            prod: int = 1
            for n in numbers:
                prod *= n
            total += prod
        else:
            raise ValueError(f"Unknown operator: {op}")
    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        input_lines = f.read().splitlines()
    print(solve(input_lines))
