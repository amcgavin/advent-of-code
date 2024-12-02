import heapq
import itertools
from collections import defaultdict
import sys
import aocd
from parse import parse


def immediate_neighbours(x, y, pos):
    if pos == ">":
        return [(x + 1, y)]
    elif pos == "<":
        return [(x - 1, y)]
    elif pos == "^":
        return [(x, y - 1)]
    elif pos == "v":
        return [(x, y + 1)]
    return {
        (x + 1, y),
        (x - 1, y),
        (x, y - 1),
        (x, y + 1),
    }


def track(grid, start, nodes, prev=None):
    nodes[start] = []
    n = start
    for i in itertools.count():
        options = []
        for option in immediate_neighbours(*n, grid[n]):
            if grid.get(option, "#") == "#":
                continue
            if grid[option] == ">" and option[0] < n[0]:
                continue
            if grid[option] == "<" and option[0] > n[0]:
                continue
            if grid[option] == "^" and option[1] > n[1]:
                continue
            if grid[option] == "v" and option[1] < n[1]:
                continue
            if option == prev:
                continue
            options.append(option)

        if len(options) == 0:
            nodes[start].append((i, n))
            break
        if len(options) == 1:
            prev = n
            n = options[0]
            continue
        if len(options) == 3:
            pass

        for option in options:
            nodes[start].append((i, option))
            if option not in nodes:
                track(grid, option, nodes, prev=n)
        break


def part_1(data):
    grid = {}
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = c
    max_x = max(x for x, y in grid.keys())
    max_y = max(y for x, y in grid.keys())

    nodes = {}
    track(grid, (1, 0), nodes)
    end = (max_x - 1, max_y)
    modifications = True
    while modifications:
        new = {}
        modifications = False
        for key, vertices in nodes.items():
            if len(vertices) == 1 and vertices[0][1] != end:
                continue
            new[key] = []
            for d, pos in vertices:
                if pos == end or len(nodes[pos]) > 1:
                    new[key].append((d, pos))
                else:
                    new[key].append((d + nodes[pos][0][0], nodes[pos][0][1]))
                    modifications = True

            if len(new[key]) > 1 and all(v[1] == new[key][0][1] for v in new[key]):
                new[key] = [max(*new[key])]
        nodes = new

    return len(nodes)


def part_2(data):
    return 0


sample = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#"""


def main():
    data = [x for x in aocd.get_data(day=23, year=2023).splitlines()]
    data = sample.splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
