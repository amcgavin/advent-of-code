import heapq
import itertools
import math
from collections import defaultdict, deque, Counter
import aocd


def immediate_neighbours(x, y):
    return {
        (x + 1, y),
        (x - 1, y),
        (x, y - 1),
        (x, y + 1),
    }


def dijkstra_algorithm(grid, start_node, max_distance=0, start_cost=0, repeat=0, distances=None):
    max_x = max(x for x, y in grid.keys()) + 1
    max_y = max(y for x, y in grid.keys()) + 1
    if distances is None:
        distances = {}
    seen = {}

    counter = itertools.count()
    heap = []

    seen[start_node] = 0
    heapq.heappush(heap, (start_cost, next(counter), start_node))
    while heap:
        distance, _, next_node = heapq.heappop(heap)
        if next_node in distances:
            continue
        distances[next_node] = distance
        for option in immediate_neighbours(*next_node):
            if repeat:
                x, y = option
                if not (-repeat < (x / max_x) < repeat + 1 and -repeat < (y / max_y) < repeat + 1):
                    continue
                if grid.get((x % max_x, y % max_y), "#") == "#":
                    continue
            elif grid.get(option, "#") == "#":
                continue

            next_distance = distances[next_node] + 1
            if max_distance and next_distance > max_distance:
                continue
            if option not in distances and option not in seen or next_distance < seen[option]:
                seen[option] = next_distance
                heapq.heappush(heap, (next_distance, next(counter), option))

    return distances


def part_1(data):
    grid = {}
    start = None
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = c
            if c == "S":
                start = (x, y)

    d = dijkstra_algorithm(grid, start, max_distance=64)
    return sum(1 for x in d.values() if x == 64 or x % 2 == 0)


def part_2(data):
    n = 26501365
    # factors
    # 5, 11, 55, 481843 2409215
    grid = {}
    start = None
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = c
            if c == "S":
                start = (x, y)
    d = dijkstra_algorithm(grid, start, repeat=0, max_distance=n)
    walls = set(grid.keys()) - set(d.keys())
    for x, y in walls:
        grid[(x, y)] = "#"
    d = dijkstra_algorithm(grid, start, repeat=0, max_distance=n)
    max_x = max(x for x, y in grid.keys())
    max_y = max(y for x, y in grid.keys())
    t = n // (max_x + 1)  # 202300
    c = Counter(d.values())
    # cap at 7645, 67237, 187201, 367277, 607465, 907765, 1268177, 1688701, 2169337
    # 42, 39
    # 241, 229
    # ((7645, 7577)
    # (68136, 68068)

    evens = sum(1 for x in d.values() if x == n or x % 2 == 0)
    odds = sum(1 for x in d.values() if x == n or x % 2 == 1)

    total = 0
    for i in range(n // (max_x + 1) + 1):
        # gets us full squares.
        m = evens if i % 2 == 0 else odds
        total += max(i * 4, 1) * m

    # now, find the distances we can travel from edges in n % max steps.

    for start in [(0, max_x / 2), (max_x / 2, 0), (max_x, max_x / 2), (max_x / 2, max_x)]:
        d = dijkstra_algorithm(grid, start, repeat=0, max_distance=n % (max_x + 1), start_cost=0)
        total += sum(1 for x in d.values() if x <= n % (max_x + 1) and x % 2 == 0)

    # 622926932272509  x
    # 622926932272207  ?
    assert 622926904355205 < total < 622933090711756, total
    return total


sample = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""


def main():
    data = [x for x in aocd.get_data(day=21, year=2023).splitlines()]
    # data = sample.splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
