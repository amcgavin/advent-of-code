from collections import defaultdict

import aocd
import utils


def search(grid, start_node):
    seen = defaultdict(lambda: 0)
    heap = [start_node]

    while heap:
        next_node = heap.pop()
        for option in utils.cardinal_neighbours(*next_node):
            if grid.get(option) != grid[next_node] + 1:
                continue

            if grid[option] == 9:
                seen[option] += 1
            else:
                heap.append(option)

    return seen


def part_1(data: utils.Input):
    grid = {p: int(c) for p, c in utils.as_grid(data)}
    return sum(len(search(grid, p).keys()) for p, c in grid.items() if c == 0)


def part_2(data: utils.Input):
    grid = {p: int(c) for p, c in utils.as_grid(data)}
    return sum(sum(search(grid, p).values()) for p, c in grid.items() if c == 0)


def main():
    data = [x for x in aocd.get_data(day=10, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
