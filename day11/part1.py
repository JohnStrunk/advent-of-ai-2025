"""Advent of Code 2025 Day 11 Part 1: Count all paths from 'you' to 'out' in the device graph."""


def solve(input_data: str) -> int:
    """Count all distinct paths from 'you' to 'out' in the device graph described by input_data."""
    # Parse the input into a graph
    graph: dict[str, list[str]] = {}
    for line in input_data.strip().splitlines():
        if not line.strip():
            continue
        name, rest = line.split(":")
        graph[name.strip()] = [x.strip() for x in rest.strip().split()]

    # DFS to count all paths from 'you' to 'out'

    def dfs(node: str) -> int:
        """Recursively count all paths from node to 'out'."""
        if node == "out":
            return 1
        total = 0
        for neighbor in graph.get(node, []):
            total += dfs(neighbor)
        return total

    return dfs("you")


if __name__ == "__main__":
    with open("input.txt") as f:
        input_data = f.read()
    print(solve(input_data))
