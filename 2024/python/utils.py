import dataclasses
import heapq
import itertools
import re
from typing import Generator, Iterable, Sequence

type Line = str
type Input = list[Line]
type Coord = tuple[int, int]
type Grid = dict[Coord, str]


@dataclasses.dataclass
class Point:
    x: int
    y: int

    def __add__(self, other):
        if isinstance(other, tuple):
            other = Point(*other)
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if isinstance(other, tuple):
            other = Point(*other)
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)


def ints(line: Line) -> list[int]:
    return list(map(int, re.findall(r"-?\d+", line)))


def floats(line: Line) -> list[float]:
    return list(map(float, re.findall(r"-?\d+(?:\.\d+)?", line)))


def words(line: Line) -> list[str]:
    return re.findall(r"[a-zA-Z]+", line)


def partition_sections(data: Input) -> Generator[Input]:
    s = 0
    for i, line in enumerate(data):
        if line == "":
            yield data[s:i]
            s = i + 1
    yield data[s:]


def as_grid(data: Input) -> Generator[tuple[Coord, str]]:
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            yield (x, y), c


def as_table(data: Input) -> Grid:
    grid = {}
    for y, line in enumerate(data):
        for x, c in enumerate(line.split()):
            grid[(x, y)] = c
    return grid


def immediate_neighbours(x: int, y: int) -> set[Coord]:
    return {
        (x + 1, y),
        (x - 1, y),
        (x + 1, y - 1),
        (x + 1, y + 1),
        (x - 1, y + 1),
        (x - 1, y - 1),
        (x, y - 1),
        (x, y + 1),
    }


def cardinal_neighbours(x: int, y: int) -> set[Coord]:
    return {
        (x + 1, y),
        (x - 1, y),
        (x, y - 1),
        (x, y + 1),
    }


def all_directions():
    return ["U", "D", "L", "R", "UL", "UR", "DL", "DR"]


def cardinal_directions():
    return ["U", "L", "D", "R"]


def directional_add(x, y, d):
    if d == "L":
        return (x - 1, y)
    elif d == "R":
        return (x + 1, y)
    elif d == "U":
        return (x, y - 1)
    elif d == "D":
        return (x, y + 1)


def straight_line(x, y, direction, length) -> list[Coord]:
    if direction == "U":
        return [(x, y - i) for i in range(1, length + 1)]
    if direction == "D":
        return [(x, y + i) for i in range(1, length + 1)]
    if direction == "L":
        return [(x - i, y) for i in range(1, length + 1)]
    if direction == "R":
        return [(x + i, y) for i in range(1, length + 1)]
    if direction == "UR":
        return [(x + i, y - i) for i in range(1, length + 1)]
    if direction == "UL":
        return [(x - i, y - i) for i in range(1, length + 1)]
    if direction == "DR":
        return [(x + i, y + i) for i in range(1, length + 1)]
    if direction == "DL":
        return [(x - i, y + i) for i in range(1, length + 1)]


def find_in_grid(
    grid: Grid, patterns: Iterable[Sequence[Sequence[str]]]
) -> Generator[tuple[int, Coord]]:
    for x, y in grid.keys():
        for p, pattern in enumerate(patterns):
            if all(
                (not pattern[j][i]) or grid.get((x + i, y + j)) == pattern[j][i]
                for j in range(len(pattern))
                for i in range(len(pattern[j]))
            ):
                yield p, (x, y)


def dijkstra_algorithm(grid, start_node):
    distances = {}
    seen = {}
    counter = itertools.count()
    heap = []

    seen[start_node] = 0
    heapq.heappush(heap, (0, next(counter), start_node))
    while heap:
        distance, _, next_node = heapq.heappop(heap)
        if next_node in distances:
            continue
        distances[next_node] = distance
        for option in immediate_neighbours(*next_node):
            if option not in grid:
                continue

            next_distance = distances[next_node] + 1

            if option not in distances and option not in seen or next_distance < seen[option]:
                seen[option] = next_distance
                heapq.heappush(heap, (next_distance, next(counter), option))

    return distances
