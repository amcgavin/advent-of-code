import itertools

import aocd


def part_1(data):
    grid = {}
    dupe_rows = []
    dupe_columns = []
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = c
    for y in range(len(data)):
        if all(grid[(x, y)] == "." for x in range(len(data))):
            dupe_rows.append(y)
    for x in range(len(data)):
        if all(grid[(x, y)] == "." for y in range(len(data))):
            dupe_columns.append(x)

    galaxies = []
    for y, line in enumerate(data):
        offy = sum(1 for i in dupe_rows if i < y)
        for x, c in enumerate(line):
            offx = sum(1 for i in dupe_columns if i < x)
            if c == "#":
                galaxies.append((x + offx, y + offy))

    total = 0
    for (x1, y1), (x2, y2) in itertools.combinations(galaxies, 2):
        total += abs(x1 - x2) + abs(y1 - y2)

    return total


def part_2(data):
    grid = {}
    dupe_rows = []
    dupe_columns = []
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = c
    for y in range(len(data)):
        if all(grid[(x, y)] == "." for x in range(len(data))):
            dupe_rows.append(y)
    for x in range(len(data)):
        if all(grid[(x, y)] == "." for y in range(len(data))):
            dupe_columns.append(x)

    galaxies = []
    for y, line in enumerate(data):
        offy = sum(1000000 - 1 for i in dupe_rows if i < y)
        for x, c in enumerate(line):
            offx = sum(1000000 - 1 for i in dupe_columns if i < x)
            if c == "#":
                galaxies.append((x + offx, y + offy))

    total = 0
    for (x1, y1), (x2, y2) in itertools.combinations(galaxies, 2):
        total += abs(x1 - x2) + abs(y1 - y2)

    return total


def main():
    data = [x for x in aocd.get_data(day=11, year=2023).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
