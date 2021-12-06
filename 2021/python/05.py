import itertools
import re
from collections import Counter

import aocd

line_re = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")


def line_points(x1, y1, x2, y2):
    if x1 < x2:
        xmult = 1
    elif x1 > x2:
        xmult = -1
    else:
        xmult = 0
    if y1 < y2:
        ymult = 1
    elif y1 > y2:
        ymult = -1
    else:
        ymult = 0
    x = x1
    y = y1
    while x != x2 or y != y2:
        yield (x, y)
        x += xmult
        y += ymult
    yield (x, y)


def part_1(data):
    total = 0
    for collision in Counter(
        itertools.chain.from_iterable(
            (line_points(x1, y1, x2, y2) for x1, y1, x2, y2 in data if x1 == x2 or y1 == y2)
        )
    ).values():
        if collision > 1:
            total += 1
    return total


def part_2(data):
    total = 0
    for collision in Counter(
        itertools.chain.from_iterable((line_points(x1, y1, x2, y2) for x1, y1, x2, y2 in data))
    ).values():
        if collision > 1:
            total += 1
    return total


def main():
    data = [
        [int(g) for g in line_re.match(line).groups()]
        for line in aocd.get_data(day=5, year=2021).splitlines()
    ]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
