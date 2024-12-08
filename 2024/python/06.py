import aocd
import utils
from collections import defaultdict
from parse import parse
import re
import itertools


def part_1(data: utils.Input):
    grid = {(x, y): c for x, y, c in utils.as_grid(data)}

    start = next(i for i, v in grid.items() if v == "^")
    seen = set()
    directions = itertools.cycle(["U", "R", "D", "L"])
    direction = next(directions)
    current = start
    while True:
        if len(seen) > 0 and start == current and direction == "U":
            break
        seen.add(current)
        next_node = utils.straight_line(current[0], current[1], direction, 1)[0]
        if next_node not in grid:
            break
        if grid.get(next_node, "#") == "#":
            direction = next(directions)
            continue
        current = next_node

    # for y in range(10):
    #     print("".join(f"{'X' if (x, y) in seen else grid.get((x, y))}" for x in range(10)))
    #     print("")
    return len(seen)


def part_2(data: utils.Input):
    result = 0
    grid = {(x, y): c for x, y, c in utils.as_grid(data)}
    start = next(i for i, v in grid.items() if v == "^")

    for pos in grid.keys():
        if pos == start:
            continue
        seen = defaultdict(set)
        blocked = defaultdict(set)
        directions = itertools.cycle(["U", "R", "D", "L"])
        direction = next(directions)
        current = start
        while True:
            if len(seen) > 0 and direction in seen[current]:
                result += 1
                break
            seen[current].add(direction)
            next_node = utils.straight_line(current[0], current[1], direction, 1)[0]
            if next_node not in grid:
                break
            if next_node == pos or grid.get(next_node) == "#":
                if direction in blocked[next_node]:
                    result += 1
                    break
                blocked[next_node].add(direction)
                direction = next(directions)
                continue
            current = next_node
    return result


def main():
    data = [x for x in aocd.get_data(day=6, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
