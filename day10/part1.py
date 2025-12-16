"""
Solution for Day 10, Part 1.

This module contains the solution for Part 1 of Day 10.
"""

from itertools import product
from typing import NamedTuple


def _find_pivot(A_: list[list[int]], cidx: int, rank: int, n: int) -> int:
    """Find the pivot row for column cidx starting from rank."""
    for ridx in range(rank, n):
        if A_[ridx][cidx]:
            return ridx
    return -1


def parse_input(input_data: str) -> list[tuple[str, list[tuple[int, ...]]]]:
    """
    Parse the input data into a list of machines.

    Args:
        input_data (str): The raw input data.

    Returns:
        list: A list of tuples, each containing the target configuration and button wiring.
    """
    machines: list[tuple[str, list[tuple[int, ...]]]] = []
    for line in input_data.strip().split("\n"):
        parts = line.split()
        target = parts[0][1:-1]  # Extract the indicator light diagram
        buttons = [
            tuple(map(int, b[1:-1].split(","))) for b in parts[1:] if b.startswith("(")
        ]
        machines.append((target, buttons))
    return machines


def gf2_min_presses(target: str, buttons: list[tuple[int, ...]]) -> int:
    """Solve the lights out puzzle using Gaussian elimination over GF(2).

    Returns the minimum number of button presses, or -1 if unsolvable.
    """
    n = len(target)
    m = len(buttons)

    def build_matrix(buttons: list[tuple[int, ...]], n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(len(buttons))]
        for bidx, button in enumerate(buttons):
            for idx in button:
                matrix[bidx][idx] = 1
        return matrix

    def transpose(matrix: list[list[int]]) -> list[list[int]]:
        m = len(matrix)
        n = len(matrix[0]) if matrix else 0
        return [[matrix[j][i] for j in range(m)] for i in range(n)]

    def has_inconsistency(b_: list[int], rank: int, n: int) -> bool:
        return any(b_[ridx] for ridx in range(rank, n))

    class BackSubstituteParams(NamedTuple):
        A_: list[list[int]]
        b_: list[int]
        where: list[int]
        m: int
        free: list[int]

    def back_substitute(
        params: "BackSubstituteParams",
        values: tuple[int, ...],
    ) -> int:
        x = [0] * params.m
        for idx, val in zip(params.free, values):
            x[idx] = val
        for i in reversed(range(params.m)):
            if params.where[i] == -1:
                continue
            rowidx = params.where[i]
            s = params.b_[rowidx]
            for j in range(i + 1, params.m):
                s ^= params.A_[rowidx][j] & x[j]
            x[i] = s
        return sum(x)

    matrix = build_matrix(buttons, n)
    A = transpose(matrix)
    bvec = [1 if c == "#" else 0 for c in target]

    A_ = [row[:] for row in A]
    b_ = bvec[:]
    rank = 0
    where = [-1] * m
    for cidx in range(m):
        sel = _find_pivot(A_, cidx, rank, n)
        if sel == -1:
            continue
        A_[rank], A_[sel] = A_[sel], A_[rank]
        b_[rank], b_[sel] = b_[sel], b_[rank]
        where[cidx] = rank
        for ridx2 in range(n):
            if ridx2 == rank or not A_[ridx2][cidx]:
                continue
            for cc in range(cidx, m):
                A_[ridx2][cc] ^= A_[rank][cc]
            b_[ridx2] ^= b_[rank]
        rank += 1
    if has_inconsistency(b_, rank, n):
        return -1
    free = [i for i in range(m) if where[i] == -1]
    min_presses = None
    params = BackSubstituteParams(A_, b_, where, m, free)
    for values in product([0, 1], repeat=len(free)):
        presses = back_substitute(params, values)
        if min_presses is None or presses < min_presses:
            min_presses = presses
    return min_presses if min_presses is not None else -1


def solve(input_data: str) -> int:
    """Solve the Day 10, Part 1 puzzle for all machines in the input.

    Args:
        input_data (str): The raw input data for all machines.

    Returns:
        int: The total minimum number of button presses for all machines, or -1 if any is unsolvable.
    """
    machines = parse_input(input_data)
    total_presses: int = 0
    for t, btns in machines:
        presses = gf2_min_presses(t, btns)
        if presses == -1:
            return -1
        total_presses += presses
    return total_presses


if __name__ == "__main__":
    with open("input.txt") as f:
        input_data = f.read()
    print(solve(input_data))
