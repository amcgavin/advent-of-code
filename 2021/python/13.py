import re

import aocd

fold_re = re.compile(r"fold along (x|y)=(\d+)")


def parse(data):
    is_coords = True
    grid = set()
    folds = []
    for line in data:
        if line == "":
            is_coords = False
            continue
        if is_coords:
            x, y = line.split(",")
            x = int(x)
            y = int(y)
            grid.add((x, y))
        else:
            axis, val = fold_re.match(line).groups()
            folds.append((0 if axis == "x" else 1, int(val)))
    return grid, folds


def part_1(data):
    grid, folds = parse(data)
    axis, val = folds[0]
    if axis == 0:
        grid = {(val - abs(x - val), y) for (x, y) in grid}
    else:
        grid = {(x, val - abs(y - val)) for (x, y) in grid}
    return len(grid)


def part_2(data):
    grid, folds = parse(data)
    for axis, val in folds:
        if axis == 0:
            grid = {(val - abs(x - val), y) for (x, y) in grid}
        else:
            grid = {(x, val - abs(y - val)) for (x, y) in grid}

    max_x = max(p[0] for p in grid)
    max_y = max(p[1] for p in grid)
    table = [[" "] * (max_x + 1) for _ in range(max_y + 1)]
    for (x, y) in grid:
        table[y][x] = "█"
    for line in table:
        print("".join(line))
    print("")


def main():
    data = aocd.get_data(day=13, year=2021).splitlines()
    print(part_1(data))
    part_2(data)


if __name__ == "__main__":
    main()
