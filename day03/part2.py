"""Part 2 solution for Day 3: Find the largest 12-digit number from a string of digits."""


def largest_12_digit_number(s: str) -> int:
    """Given a string of digits, select 12 digits in order to form the largest possible number.

    This is a variant of the 'create largest number by removing k digits' problem.
    """
    n: int = len(s)
    k: int = n - 12
    stack: list[str] = []
    for digit in s:
        while k and stack and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    return int("".join(stack[:12]))


def main() -> None:
    """Read input and print the total maximum 12-digit number for all banks."""
    total: int = 0
    with open("day03/input.txt") as f:
        for line in f:
            line_stripped: str = line.strip()
            if not line_stripped:
                continue
            total += largest_12_digit_number(line_stripped)
    print(total)


if __name__ == "__main__":
    main()
