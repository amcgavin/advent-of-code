import itertools
from collections import defaultdict
import functools
import operator
import aocd
import utils

import heapq

WIDTH = 101
HEIGHT = 103


def part_1(data: utils.Input):
    quadrants = defaultdict(int)
    for line in data:
        x, y, vx, vy = utils.ints(line)
        x += vx * 100
        y += vy * 100
        x %= WIDTH
        y %= HEIGHT
        if x == WIDTH // 2:
            continue
        if y == HEIGHT // 2:
            continue
        quadrants[(x < (WIDTH // 2), y < (HEIGHT // 2))] += 1
    return functools.reduce(operator.mul, quadrants.values())


def key_fn(grid):
    return len(grid[1]), grid[0]


def part_2(data: utils.Input):
    grids = []
    for i in range(1, WIDTH * HEIGHT):
        grid = {}
        for line in data:
            x, y, vx, vy = utils.ints(line)
            x += vx * i
            y += vy * i
            x %= WIDTH
            y %= HEIGHT
            grid[(x, y)] = "#"
        heapq.heappush(grids, (-len(grid), -i, i, grid))
    _, __, i, grid = heapq.heappop(grids)

    for y in range(HEIGHT):
        print("".join(grid.get((x, y), ".") for x in range(WIDTH)))
    return i


def main():
    data = [x for x in aocd.get_data(day=14, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
