import heapq
import itertools
from collections import defaultdict
import sys
import aocd
from parse import parse


def part_1(data):
    lines = []
    for line in data:
        x1, y1, z1, vx, vy, vz = parse("{:d}, {:d}, {:d} @ {:d}, {:d}, {:d}", line)
        lines.append((x1, y1, vx, vy))
    for (cx1, cy1, mx1, my1), (cx2, cy2, mx2, my2) in itertools.combinations(lines, 2):
        if mx1 == mx2:
            continue
        x = (cx1 * mx2 - cx2 * mx1) / (-mx1 - -mx2)
        print(x)

    return 0


def part_2(data):
    return 0


sample = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3"""


def main():
    data = [x for x in aocd.get_data(day=24, year=2023).splitlines()]
    data = sample.splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
