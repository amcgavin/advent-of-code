import itertools

import aocd


def build_grid(data):
    grid = {}
    coords = []
    for line in data:
        lists = []
        for coord in line.split(" -> "):
            lists.append([int(x) for x in coord.split(",")])
        coords.append(lists)

    for rock in coords:
        gen = iter(rock)
        (x1, y1) = next(gen)
        for (x2, y2) in gen:
            # figure out if it's vertical or horizontal
            if x1 != x2:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    grid[(x, y1)] = "#"
            if y2 != y1:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    grid[(x1, y)] = "#"

            x1, y1 = x2, y2
    return grid


def part_1(data):
    grid = build_grid(data)

    abyss = max(y for x, y in grid.keys())
    for i in itertools.count(1):
        x, y = (500, 0)
        while y <= abyss:
            # find the first occupied spot
            if (x, y + 1) not in grid:
                x, y = x, y + 1
                continue
            if (x - 1, y + 1) not in grid:
                x, y = x - 1, y + 1
                continue
            if (x + 1, y + 1) not in grid:
                x, y = x + 1, y + 1
                continue
            grid[(x, y)] = "o"
            break
        if y > abyss:
            return i - 1


def part_2(data):
    grid = build_grid(data)
    abyss = max(y for x, y in grid.keys()) + 2

    for i in itertools.count(1):
        x, y = (500, 0)
        while True:
            grid[(x, abyss)] = "#"
            grid[(x - 1, abyss)] = "#"
            grid[(x + 1, abyss)] = "#"
            # find the first occupied spot
            if (x, y + 1) not in grid:
                x, y = x, y + 1
                continue
            if (x - 1, y + 1) not in grid:
                x, y = x - 1, y + 1
                continue
            if (x + 1, y + 1) not in grid:
                x, y = x + 1, y + 1
                continue
            grid[(x, y)] = "o"
            if (x, y) == (500, 0):
                return i
            break


def main():
    data = [x for x in aocd.get_data(day=14, year=2022).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
