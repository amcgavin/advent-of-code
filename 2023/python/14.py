from collections import defaultdict

import aocd


def part_1(data):
    grid = {}
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = c

    score = 0
    columns = defaultdict(lambda: 0)
    for y in range(len(data)):
        for x in range(len(data[0])):
            if grid[(x, y)] == "#":
                columns[x] = y + 1
            elif grid[(x, y)] == "O":
                score += len(data) - columns[x]
                columns[x] += 1

    return score


def north(grid, s):
    new_grid = {}
    columns = defaultdict(lambda: 0)
    for y in range(s):
        for x in range(s):
            if grid.get((x, y)) == "#":
                new_grid[(x, y)] = "#"
                columns[x] = y + 1
            elif grid.get((x, y)) == "O":
                new_grid[(x, columns[x])] = "O"
                columns[x] += 1
    return new_grid


def south(grid, s):
    new_grid = {}
    columns = defaultdict(lambda: s - 1)
    for y1 in range(s):
        y = s - y1 - 1
        for x in range(s):
            if grid.get((x, y)) == "#":
                new_grid[(x, y)] = "#"
                columns[x] = y - 1
            elif grid.get((x, y)) == "O":
                new_grid[(x, columns[x])] = "O"
                columns[x] -= 1
    return new_grid


def west(grid, s):
    new_grid = {}
    columns = defaultdict(lambda: 0)
    for x in range(s):
        for y in range(s):
            if grid.get((x, y)) == "#":
                new_grid[(x, y)] = "#"
                columns[y] = x + 1
            elif grid.get((x, y)) == "O":
                new_grid[(columns[y], y)] = "O"
                columns[y] += 1
    return new_grid


def east(grid, s):
    new_grid = {}
    columns = defaultdict(lambda: s - 1)
    for x in range(s, -1, -1):
        for y in range(s):
            if grid.get((x, y)) == "#":
                new_grid[(x, y)] = "#"
                columns[y] = x - 1
            elif grid.get((x, y)) == "O":
                new_grid[(columns[y], y)] = "O"
                columns[y] -= 1
    return new_grid


def calc_score(grid, s):
    score = 0
    for y in range(s):
        for x in range(s):
            if grid.get((x, y)) == "O":
                score += s - y
    return score


def part_2(data):
    grid = {}
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = c

    s = len(data)
    deltas = [north, west, south, east]
    scores = []
    for i in range(1000):
        if i % 4 == 0 and i > 0:
            score = calc_score(grid, s)
            scores.append(score)

        xform = deltas[i % 4]
        grid = xform(grid, s)

    p = scores[194 - 14 : 194]
    return p[(4_000_000_000 - 997) % 14]


def main():
    data = [x for x in aocd.get_data(day=14, year=2023).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
