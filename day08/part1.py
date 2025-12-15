#!/usr/bin/env python3
"""Solution for Day 8, Part 1."""

import sys


class UnionFind:
    """Union-Find data structure for tracking connected components."""

    def __init__(self, n: int) -> None:
        """Initialize with n separate components."""
        self.parent = {i: i for i in range(n)}
        self.rank = {i: 0 for i in range(n)}

    def find(self, x: int) -> int:
        """Find root of x with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """Union two components. Returns True if they were separate."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


def distance(box1: tuple[int, int, int], box2: tuple[int, int, int]) -> float:
    """Calculate 3D Euclidean distance between two boxes."""
    x1, y1, z1 = box1
    x2, y2, z2 = box2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5


def solve(input_file: str, num_connections: int = 1000) -> int:
    """Solve part 1 of the puzzle."""
    with open(input_file, encoding="utf-8") as f:
        lines = f.read().strip().split("\n")

    # Parse junction box coordinates
    boxes: list[tuple[int, int, int]] = []
    for line in lines:
        x, y, z = map(int, line.split(","))
        boxes.append((x, y, z))

    # Calculate all pairwise distances
    distances: list[tuple[float, int, int]] = []
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            dist = distance(boxes[i], boxes[j])
            distances.append((dist, i, j))

    # Sort by distance
    distances.sort()

    # Make connections using Union-Find
    uf = UnionFind(len(boxes))
    for dist, i, j in distances[:num_connections]:
        uf.union(i, j)

    # Count circuit sizes
    circuits: dict[int, int] = {}
    for i in range(len(boxes)):
        root = uf.find(i)
        circuits[root] = circuits.get(root, 0) + 1

    # Get three largest circuit sizes and multiply
    sizes = sorted(circuits.values(), reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


def main() -> None:
    """Run the solution."""
    if len(sys.argv) != 2:  # noqa: PLR2004
        print("Usage: python part1.py <input_file>", file=sys.stderr)
        sys.exit(1)

    result = solve(sys.argv[1])
    print(result)


if __name__ == "__main__":
    main()
