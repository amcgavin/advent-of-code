import dataclasses
import itertools
import math
from collections import defaultdict
import functools
import operator
import aocd
import utils

import heapq


def next_pos(x, y, c):
    if c == "v":
        return (x, y + 1), "D"
    elif c == "<":
        return (x - 1, y), "L"
    elif c == ">":
        return (x + 1, y), "R"
    elif c == "^":
        return (x, y - 1), "U"


def find_til_end(x, y, direction, grid):
    for b in utils.straight_line(x, y, direction, len(grid)):
        if b not in grid:
            return None
        if grid[b] == "#":
            return None
        if grid[b] == ".":
            return b
    return None


def part_1(data: utils.Input):
    grid = {}
    g = utils.partition_sections(data)
    m = next(g)
    instructions = next(g)

    start = (0, 0)
    for p, c in utils.as_grid(m):
        grid[p] = c
        if c == "@":
            start = p

    for i in "".join(instructions):
        ne, d = next_pos(*start, i)
        n = grid.get(ne, "#")
        if n == "#":
            continue
        if n == "O":
            p = find_til_end(*start, d, grid)
            if p is None:
                continue
            else:
                grid[p] = "O"
                grid[ne] = "@"
                grid[start] = "."
                start = ne
        else:
            grid[start] = "."
            start = ne
            grid[start] = "@"

    return sum(100 * y + x for (x, y), c in grid.items() if c == "O")


c = itertools.count()


@dataclasses.dataclass
class Box:
    x: int
    y: int
    id: int = dataclasses.field(default_factory=lambda: next(c))

    @property
    def pl(self):
        return (self.x, self.y)

    @property
    def pr(self):
        return (self.x + 1, self.y)

    def __hash__(self):
        return hash(self.id)


def part_2(data: utils.Input):
    walls = {}
    g = utils.partition_sections(data)
    m = next(g)
    instructions = next(g)

    start = (0, 0)
    boxes = dict()

    for i, ((x, y), c) in enumerate(utils.as_grid(m)):
        if c == "#":
            walls[(x * 2, y)], walls[(x * 2 + 1, y)] = "##"
        elif c == "@":
            start = (x * 2, y)
        elif c == "O":
            b = Box(x * 2, y)
            boxes[(x * 2, y)] = b
            boxes[(x * 2 + 1, y)] = b

    for i in "".join(instructions):
        ne, d = next_pos(*start, i)
        if ne in walls:
            continue
        if not ne in boxes:
            start = ne
            continue
        if d in ["L", "R"]:
            line_searches = [ne]
        else:
            line_searches = [boxes[ne].pl, boxes[ne].pr]
        is_ok = True
        to_commit = []
        to_delete = set()
        while line_searches:
            search_pos = line_searches.pop()
            box = boxes.get(search_pos)

            if search_pos in walls:
                is_ok = False
                break
            if box is None:
                is_ok = True
                continue
            to_delete.add(box)
            if d == "L":
                new_pos, _ = next_pos(*box.pl, i)
                b = Box(*new_pos)
                to_commit.append(b)
                line_searches.append(new_pos)
            elif d == "R":
                new_pos, _ = next_pos(*box.pl, i)
                s_pos, _ = next_pos(*box.pr, i)
                b = Box(*new_pos)
                to_commit.append(b)
                line_searches.append(s_pos)

            else:
                new_pos, _ = next_pos(*box.pl, i)
                other_pos, _ = next_pos(*box.pr, i)
                b = Box(*new_pos)
                to_commit.append(b)

                line_searches.append(new_pos)
                line_searches.append(other_pos)
        if is_ok:
            new_box_map = {}
            for box in boxes.values():
                if box not in to_delete:
                    new_box_map[box.pl] = box
                    new_box_map[box.pr] = box
            for box in to_commit:
                new_box_map[box.pl] = box
                new_box_map[box.pr] = box
            boxes = new_box_map
            start = ne

    return sum(100 * box.y + box.x for box in set(boxes.values()))


def main():
    data = [x for x in aocd.get_data(day=15, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
