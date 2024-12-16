import itertools
import math
from collections import defaultdict
import functools
import operator
import aocd
import utils
import heapq


def cardinal_neighbours(x: int, y: int):
    return {
        (x + 1, y, "R"),
        (x - 1, y, "L"),
        (x, y - 1, "U"),
        (x, y + 1, "D"),
    }


def dijkstra_algorithm(grid, start_node, start_direction, end=None, cap=None):
    distances = {}
    seen = {}
    counter = itertools.count()
    heap = []

    seen[(*start_node, start_direction)] = 0
    heapq.heappush(heap, (0, next(counter), start_node, start_direction))
    while heap:
        distance, _, next_node, next_direction = heapq.heappop(heap)
        if next_node in distances:
            continue
        distances[(*next_node, next_direction)] = distance
        if next_node == end:
            return distances
        for x, y, d in cardinal_neighbours(*next_node):
            if grid.get((x, y)) == "#":
                continue
            if next_direction == "D" and d == "U":
                continue
            if next_direction == "U" and d == "D":
                continue
            if next_direction == "L" and d == "R":
                continue
            if next_direction == "R" and d == "L":
                continue

            next_distance = distances[(*next_node, next_direction)] + 1
            if next_direction != d:
                next_distance += 1000

            if cap is not None and next_distance > cap:
                continue
            if (
                (x, y, d) not in distances
                and (x, y, d) not in seen
                or next_distance < seen[(x, y, d)]
            ):
                seen[(x, y, d)] = next_distance
                heapq.heappush(heap, (next_distance, next(counter), (x, y), d))

    return distances


def part_1(data: utils.Input):
    grid = {}
    for p, c in utils.as_grid(data):
        grid[p] = c
        if c == "S":
            start = p
        if c == "E":
            end = p
    a = dijkstra_algorithm(grid, start, "R", end)
    return min(a.get((*end, d), math.inf) for d in "LRUD")


def part_2(data: utils.Input):
    grid = {}
    for p, c in utils.as_grid(data):
        grid[p] = c
        if c == "S":
            start = p
        if c == "E":
            end = p

    squares = set()
    a = dijkstra_algorithm(grid, start, "R")
    best = min(a.get((*end, d), math.inf) for d in "LRUD")
    max_x = max(x for x, y in grid.keys())
    for i, (p, c) in enumerate(grid.items()):
        if c == "#":
            continue
        if c == "S":
            squares.add(p)
            continue
        if c == "E":
            squares.add(p)
            continue

        for d in "LRUD":
            from_start = a.get((*p, d), math.inf)
            to_end = dijkstra_algorithm(grid, p, d, end, cap=best - from_start + 1)
            nb = min((to_end.get((*end, dd), math.inf)) for dd in "LRUD")

            if from_start + nb == best:
                squares.add(p)
                break

    # there's a bug where 2 tiles are missing from the path.
    gaps = 0
    for s in squares:
        if s == start or s == end:
            continue
        if len([p for p in utils.cardinal_neighbours(*s) if p in squares]) < 2:
            gaps += 1

    for y in range(max(y for x, y in grid.keys()) + 1):
        pr = []
        for x in range(max(x for x, y in grid.keys()) + 1):
            if (x, y) in squares:
                pr.append("O")
            else:
                pr.append(grid.get((x, y), " "))
        print("".join(pr))

    return len(squares) + gaps // 2


def main():
    data = [x for x in aocd.get_data(day=16, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
