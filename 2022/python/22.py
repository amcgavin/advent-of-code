import itertools
import math
import re

import aocd


def draw_path(grid, x, y, angle):
    for b in range(16):
        me = ">"
        match angle % 360:
            case 90:
                me = "v"
            case 180:
                me = "<"
            case 270:
                me = "^"
        print(
            "".join(
                me
                if (a, b) == (x, y)
                else "."
                if grid.get((a, b))
                else "#"
                if grid.get((a, b)) is False
                else " "
                for a in range(16)
            )
        )


def part_1(data):
    grid = dict()
    for y, line in enumerate(data):
        if line == "":
            break
        for x, char in enumerate(line):

            if char == "#":
                grid[(x, y)] = False
            elif char == ".":
                grid[(x, y)] = True

    path = data[y + 1 :][0]
    steps = [int(x) for x in re.split(r"L|R", path)]
    rotations = [x for x in re.split(r"\d+", path) if x]

    y_bounds = {
        y: (min(a for a, b in grid.keys() if b == y), max(a for a, b in grid.keys() if b == y))
        for y in range(0, max(b for a, b in grid.keys()) + 1)
    }
    x_bounds = {
        x: (min(b for a, b in grid.keys() if a == x), max(b for a, b in grid.keys() if a == x))
        for x in range(0, max(a for a, b in grid.keys()) + 1)
    }
    x, y = (y_bounds[0][0], 0)
    angle = 0
    for instruction in itertools.chain.from_iterable(itertools.zip_longest(steps, rotations)):
        match instruction:
            case int(steps):
                dx = int(math.cos(math.radians(angle)))
                dy = int(math.sin(math.radians(angle)))
                for _ in range(steps):
                    target = grid.get((x + dx, y + dy))
                    if target is True:
                        x += dx
                        y += dy
                    if target is False:
                        break
                    if target is None:
                        if dy > 0:
                            wrapy = x_bounds[x][0]
                        elif dy < 0:
                            wrapy = x_bounds[x][1]
                        else:
                            wrapy = y
                        if dx > 0:
                            wrapx = y_bounds[y][0]
                        elif dx < 0:
                            wrapx = y_bounds[y][1]
                        else:
                            wrapx = x
                        wrap_target = wrapx, wrapy
                        if grid[wrap_target]:
                            x, y = wrap_target
                        else:
                            break
            case "R":
                angle += 90
            case "L":
                angle -= 90

    return 1000 * (y + 1) + 4 * (x + 1) + (angle % 360) // 90


def part_2(data):
    grid = dict()
    for y, line in enumerate(data):
        if line == "":
            break
        for x, char in enumerate(line):

            if char == "#":
                grid[(x, y)] = False
            elif char == ".":
                grid[(x, y)] = True

    path = data[y + 1 :][0]
    steps = [int(x) for x in re.split(r"L|R", path)]
    rotations = [x for x in re.split(r"\d+", path) if x]

    faces = {(1, 0): 2, (2, 0): 1, (1, 1): 3, (0, 2): 5, (1, 2): 4, (0, 3): 6}
    transforms = {
        (1, 0): lambda a, b: (99, 149 - b % 50, 180),  # 1 > 4 <
        (1, 90): lambda a, b: (99, 50 + a % 50, 180),  # 1 v 3 <
        (1, 270): lambda a, b: (a - 100, 199, 270),  # 1 ^ 6 ^
        (2, 180): lambda a, b: (0, 149 - b % 50, 0),  # 2 < 5 >
        (2, 270): lambda a, b: (0, 150 + a % 50, 0),  # 2 ^ 6 >
        (3, 0): lambda a, b: (100 + b % 50, 49, 270),  # 3 > 1 ^
        (3, 180): lambda a, b: (b % 50, 100, 90),  # 3 < 5 v
        (4, 0): lambda a, b: (149, 49 - b % 50, 180),  # 4 > 1 <
        (4, 90): lambda a, b: (49, 150 + a % 50, 180),  # 4 v 6 <
        (5, 180): lambda a, b: (50, 49 - b % 50, 0),  # 5 < 2 >
        (5, 270): lambda a, b: (50, 50 + a % 50, 0),  # 5 ^ 3 >
        (6, 0): lambda a, b: (50 + b % 50, 149, 270),  # 6 > 4 ^
        (6, 90): lambda a, b: (100 + a, 0, 90),  # 6 v 1 v
        (6, 180): lambda a, b: (50 + b % 50, 0, 90),  # 6 < 2 v
    }

    x, y = (min(a for a, b in grid.keys() if b == 0), 0)
    angle = 0
    for instruction in itertools.chain.from_iterable(itertools.zip_longest(steps, rotations)):
        match instruction:
            case int(steps):
                for _ in range(steps):
                    dx = int(math.cos(math.radians(angle)))
                    dy = int(math.sin(math.radians(angle)))
                    target = grid.get((x + dx, y + dy))
                    if target is True:
                        x += dx
                        y += dy
                    elif target is False:
                        break
                    elif target is None:
                        face = faces[x // 50, y // 50]
                        wrap_x, wrap_y, new_angle = transforms[(face, angle)](x, y)
                        if grid[(wrap_x, wrap_y)]:
                            x, y = wrap_x, wrap_y
                            angle = new_angle
                        else:
                            break

            case "R":
                angle += 90
                angle %= 360
            case "L":
                angle -= 90
                angle %= 360
    return 1000 * (y + 1) + 4 * (x + 1) + (angle % 360) // 90


def main():
    data = aocd.get_data(day=22, year=2022).splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
