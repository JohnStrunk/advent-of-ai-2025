"""Part 1 solution for Day 3: Find the largest two-digit number from a string of digits."""


def max_joltage_from_bank(bank: str) -> int:
    """Given a string of digits, return the largest two-digit number that can be formed.

    Select any two digits in order (not necessarily adjacent).
    """
    max_joltage = 0
    n = len(bank)
    for i in range(n - 1):
        for j in range(i + 1, n):
            joltage = int(bank[i] + bank[j])
            max_joltage = max(max_joltage, joltage)
    return max_joltage


def main():
    """Read input and print the total maximum joltage for all banks."""
    total = 0
    with open("day03/input.txt") as f:
        for line in f:
            line_stripped = line.strip()
            if line_stripped:
                total += max_joltage_from_bank(line_stripped)
    print(total)


if __name__ == "__main__":
    main()
