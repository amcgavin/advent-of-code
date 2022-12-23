import itertools
from collections import defaultdict

import aocd


def immediate_neighbours(x, y):
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


def north_neighbours(x, y):
    return {(x, y - 1), (x + 1, y - 1), (x - 1, y - 1)}, (x, y - 1)


def south_neighbours(x, y):
    return {(x, y + 1), (x + 1, y + 1), (x - 1, y + 1)}, (x, y + 1)


def west_neighbours(x, y):
    return {(x - 1, y), (x - 1, y - 1), (x - 1, y + 1)}, (x - 1, y)


def east_neighbours(x, y):
    return {(x + 1, y), (x + 1, y - 1), (x + 1, y + 1)}, (x + 1, y)


options = [north_neighbours, south_neighbours, west_neighbours, east_neighbours]


def part_1(data):
    grid = set()
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "#":
                grid.add((x, y))
    for i in range(10):
        proposed = defaultdict(list)
        for (x, y) in grid:
            if not grid.intersection(immediate_neighbours(x, y)):
                continue

            for offset in range(4):
                neighbours = options[(i + offset) % 4]
                check, move_to = neighbours(x, y)
                if grid.intersection(check):
                    continue
                proposed[move_to].append((x, y))
                break

        for (x, y), candidates in proposed.items():
            if len(candidates) > 1:
                continue
            grid.remove(candidates[0])
            grid.add((x, y))

    x_bounds = max(x for x, y in grid) - min(x for x, y in grid) + 1
    y_bounds = max(y for x, y in grid) - min(y for x, y in grid) + 1
    return x_bounds * y_bounds - len(grid)


def part_2(data):
    grid = set()
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "#":
                grid.add((x, y))

    for i in itertools.count():
        proposed = defaultdict(list)
        for (x, y) in grid:
            if not grid.intersection(immediate_neighbours(x, y)):
                continue

            for offset in range(4):
                neighbours = options[(i + offset) % 4]
                check, move_to = neighbours(x, y)
                if grid.intersection(check):
                    continue
                proposed[move_to].append((x, y))
                break

        moved = False
        for (x, y), candidates in proposed.items():
            if len(candidates) > 1:
                continue
            grid.remove(candidates[0])
            grid.add((x, y))
            moved = True
        if not moved:
            return i + 1


def main():
    data = aocd.get_data(day=23, year=2022).splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
