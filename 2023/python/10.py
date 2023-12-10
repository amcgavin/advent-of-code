import heapq
import itertools

import aocd


def get_visible(walls, limit, start=(0, 0)):
    accessible = set()

    counter = itertools.count()
    heap = []
    seen = {start}

    def immediate_neighbours(n):
        x, y = n
        for dx, dy in [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]:
            if n in walls:
                continue
            new = (x + dx, y + dy)
            if not any(n < -1 or n > limit + 1 for n in new):
                yield new

    heapq.heappush(heap, (next(counter), start))
    while heap:
        _, next_node = heapq.heappop(heap)
        if next_node in accessible:
            continue
        accessible.add(next_node)
        for option in immediate_neighbours(next_node):
            if option not in accessible and option not in seen:
                seen.add(option)
                heapq.heappush(heap, (next(counter), option))

    return accessible


def neighbours(x, y, letter, multiplier=1):
    if letter == "|":
        yield from (
            (x * multiplier, y * multiplier - 1),
            (x * multiplier, y * multiplier + 1),
        )
    elif letter == "-":
        yield from (
            (x * multiplier - 1, y * multiplier),
            (x * multiplier + 1, y * multiplier),
        )
    elif letter == "L":
        yield from (
            (x * multiplier, y * multiplier - 1),
            (x * multiplier + 1, y * multiplier),
        )
    elif letter == "J":
        yield from (
            (x * multiplier, y * multiplier - 1),
            (x * multiplier - 1, y * multiplier),
        )
    elif letter == "7":
        yield from (
            (x * multiplier, y * multiplier + 1),
            (x * multiplier - 1, y * multiplier),
        )
    elif letter == "F":
        yield from (
            (x * multiplier, y * multiplier + 1),
            (x * multiplier + 1, y * multiplier),
        )


def part_1(data):
    grid = {}
    start = None
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == ".":
                continue
            if c == "S":
                start = (x, y)
                c = "|"
            grid[(x, y)] = c
    path = set()
    position = start
    while position is not None:
        path.add(position)
        position = next(
            (x for x in neighbours(*position, grid[position]) if x in grid and x not in path), None
        )
    return len(path) // 2


def part_2(data):
    grid = {}
    start = None
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c == ".":
                continue
            if c == "S":
                start = (x, y)
                c = "|"
            grid[(x, y)] = c
    path = set()
    position = start
    while position is not None:
        path.add(position)
        position = next(
            (x for x in neighbours(*position, grid[position]) if x in grid and x not in path), None
        )

    walls = set()
    for (x, y), letter in grid.items():
        if (x, y) not in path:
            continue
        walls.add((x * 3, y * 3))
        walls.update(neighbours(x, y, letter, multiplier=3))

    visible = get_visible(walls, len(data) * 9)
    invis = set()
    for y in range(len(data) * 3):
        for x in range(len(data[0]) * 3):
            if (x, y) not in walls and (x // 3, y // 3) not in path and (x, y) not in visible:
                invis.add((x, y))

    return len(invis) // 9


def main():
    data = [x for x in aocd.get_data(day=10, year=2023).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
