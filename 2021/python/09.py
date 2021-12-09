import functools
import operator

import aocd


def build_grid(data):
    grid = {}
    for x, row in enumerate(data):
        for y, col in enumerate(row):
            grid[(x, y)] = int(col)
    return grid


def find_low_points(grid):
    for (x, y), point in grid.items():
        if all(
            grid.get(pos, 10) > point for pos in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        ):
            yield x, y


def part_1(data):
    grid = build_grid(data)
    total = 0
    for pos in find_low_points(grid):
        total += 1 + grid[pos]
    return total


def search_higher(grid, position, seen=None):
    if seen is None:
        seen = set()
    if position in seen:
        return 0

    count = 1
    seen.add(position)
    x, y = position
    for point in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if 9 > grid.get(point, 10) > grid[position]:
            count += search_higher(grid, point, seen=seen)
    return count


def part_2(data):
    grid = build_grid(data)
    basins = []
    for pos in find_low_points(grid):
        basins.append(search_higher(grid, pos))

    return functools.reduce(operator.mul, sorted(basins)[-3:])


def main():
    data = aocd.get_data(day=9, year=2021).splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
