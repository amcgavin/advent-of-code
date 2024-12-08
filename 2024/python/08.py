from collections import defaultdict

import aocd
import utils

import itertools


def part_1(data: utils.Input):
    nodes = defaultdict(list)
    antinodes = set()
    grid = dict()
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = c
            if c != ".":
                nodes[c].append((x, y))

    for freqs in nodes.values():
        for (x1, y1), (x2, y2) in itertools.combinations(freqs, 2):
            dy = y2 - y1
            dx = x2 - x1
            p1 = x1 - dx, y1 - dy
            p2 = x2 + dx, y2 + dy
            if p1 in grid:
                antinodes.add(p1)
            if p2 in grid:
                antinodes.add(p2)
    return len(antinodes)


def part_2(data: utils.Input):
    nodes = defaultdict(list)
    antinodes = set()
    grid = dict()
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = c
            if c != ".":
                nodes[c].append((x, y))

    for freqs in nodes.values():
        for (x1, y1), (x2, y2) in itertools.combinations(freqs, 2):
            dy = y2 - y1
            dx = x2 - x1
            antinodes.add((x1, y1))
            antinodes.add((x2, y2))
            p1 = x1 - dx, y1 - dy

            while p1 in grid:
                antinodes.add(p1)
                p1 = p1[0] - dx, p1[1] - dy

            p2 = x2 + dx, y2 + dy
            while p2 in grid:
                antinodes.add(p2)
                p2 = p2[0] + dx, p2[1] + dy
    return len(antinodes)


def main():
    data = [x for x in aocd.get_data(day=8, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
