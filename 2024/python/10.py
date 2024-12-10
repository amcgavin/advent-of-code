from collections import defaultdict

import aocd
import utils


def search(grid, start_node):
    seen = defaultdict(lambda: 0)
    heap = [start_node]

    seen[start_node] = 0
    while heap:
        next_node = heap.pop()
        for option in utils.cardinal_neighbours(*next_node):
            if grid.get(option) != grid[next_node] + 1:
                continue
            seen[option] += 1
            heap.append(option)

    return seen


def part_1(data: utils.Input):
    grid = {}
    zeroes = set()
    nines = set()
    for p, c in utils.as_grid(data):
        c = int(c)
        grid[p] = c
        if c == 0:
            zeroes.add(p)
        if c == 9:
            nines.add(p)

    t = 0
    for p in zeroes:
        d = search(grid, p)
        t += sum(1 for n in nines if n in d)
    return t


def part_2(data: utils.Input):
    grid = {}
    zeroes = set()
    nines = set()
    for p, c in utils.as_grid(data):
        c = int(c)
        grid[p] = c
        if c == 0:
            zeroes.add(p)
        if c == 9:
            nines.add(p)

    t = 0
    for p in zeroes:
        d = search(grid, p)
        t += sum(d.get(n, 0) for n in nines)
    return t


def main():
    data = [x for x in aocd.get_data(day=10, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
