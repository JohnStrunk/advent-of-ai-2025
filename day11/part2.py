"""Advent of Code 2025 Day 11 Part 2: Efficient path counting with required intermediate nodes."""


def solve(input_data: str) -> int:
    """Given the puzzle input as a string, return the number of valid paths as required by part 2."""
    graph: dict[str, list[str]] = {}
    for line in input_data.strip().splitlines():
        if not line.strip():
            continue
        name, rest = line.split(":")
        graph[name.strip()] = [x.strip() for x in rest.strip().split()]

    required = ["dac", "fft"]
    total_paths = 0
    for first in required:
        second = (set(required) - {first}).pop()
        memo1: dict[tuple[str, str, tuple[str, ...]], int] = {}
        count1 = count_paths(graph, "svr", first, forbidden={second}, memo=memo1)
        memo2: dict[tuple[str, str, tuple[str, ...]], int] = {}
        count2 = count_paths(graph, first, second, forbidden=set(), memo=memo2)
        memo3: dict[tuple[str, str, tuple[str, ...]], int] = {}
        count3 = count_paths(graph, second, "out", forbidden=set(), memo=memo3)
        total_paths += count1 * count2 * count3
    return total_paths


# Advent of Code 2025 Day 11 Part 2: Efficient path counting with required intermediate nodes


def count_paths(
    graph: dict[str, list[str]],
    start: str,
    end: str,
    forbidden: set[str] | None = None,
    memo: dict[tuple[str, str, tuple[str, ...]], int] | None = None,
) -> int:
    """Count the number of paths from start to end in a DAG, optionally avoiding nodes in 'forbidden'."""
    if forbidden is None:
        forbidden = set()
    if memo is None:
        memo = {}
    key = (start, end, tuple(sorted(forbidden)))
    if key in memo:
        return memo[key]
    if start == end:
        return 1
    total = 0
    for neighbor in graph.get(start, []):
        if neighbor in forbidden:
            continue
        total += count_paths(graph, neighbor, end, forbidden, memo)
    memo[key] = total
    return total


def main() -> None:
    """Read the graph from 'input.txt', compute the number of paths from 'svr' to 'out' that pass through both 'dac' and 'fft', and print the result."""
    graph: dict[str, list[str]] = {}
    with open("input.txt") as f:
        for line in f:
            if not line.strip():
                continue
            name, rest = line.split(":")
            graph[name.strip()] = [x.strip() for x in rest.strip().split()]

    required = ["dac", "fft"]
    total_paths = 0
    for first in required:
        second = (set(required) - {first}).pop()
        # 1. Paths from svr to first (without passing through second)
        memo1: dict[tuple[str, str, tuple[str, ...]], int] = {}
        count1 = count_paths(graph, "svr", first, forbidden={second}, memo=memo1)
        # 2. Paths from first to second (no forbidden)
        memo2: dict[tuple[str, str, tuple[str, ...]], int] = {}
        count2 = count_paths(graph, first, second, forbidden=set(), memo=memo2)
        # 3. Paths from second to out (no forbidden)
        memo3: dict[tuple[str, str, tuple[str, ...]], int] = {}
        count3 = count_paths(graph, second, "out", forbidden=set(), memo=memo3)
        total_paths += count1 * count2 * count3
    print(total_paths)


if __name__ == "__main__":
    main()
