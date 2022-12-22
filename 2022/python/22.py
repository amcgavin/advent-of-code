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

    y_bounds = {
        y: (min(a for a, b in grid.keys() if b == y), max(a for a, b in grid.keys() if b == y))
        for y in range(0, max(b for a, b in grid.keys()) + 1)
    }

    faces = {(1, 0): 2, (2, 0): 1, (1, 1): 3, (0, 2): 5, (1, 2): 4, (0, 3): 6}

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
                    elif target is False:
                        break
                    elif target is None:
                        face = faces[x // 50, y // 50]
                        if face == 1:
                            if angle == 0:
                                # 1 >> 4 <<
                                wrapx = 99
                                wrapy = 149 - y % 50
                                wrapangle = 180
                            elif angle == 90:
                                # 1 vv 3 <<
                                wrapx = 99
                                wrapy = x % 50 + 50
                                wrapangle = 180
                            elif angle == 270:
                                # 1 ^^ 6 ^^
                                wrapx = x - 100
                                wrapy = 199
                                wrapangle = 270
                        elif face == 2:
                            if angle == 180:
                                # 2 << 5 >>
                                wrapx = 0
                                wrapy = 149 - y % 50
                                wrapangle = 0
                            elif angle == 270:
                                # 2 ^^ 6 >>
                                wrapx = 0
                                wrapy = x % 50 + 150
                                wrapangle = 0
                        elif face == 3:
                            if angle == 0:
                                # 3 >> 1 ^^
                                wrapx = y % 50 + 100
                                wrapy = 49
                                wrapangle = 270
                            elif angle == 180:
                                # 3 << 5 vv
                                wrapx = y % 50
                                wrapy = 100
                                wrapangle = 90
                        elif face == 4:
                            if angle == 0:
                                # 4 >> 1 <<
                                wrapx = 149
                                wrapy = 49 - y % 50
                                wrapangle = 180
                            elif angle == 90:
                                # 4 vv 6 <<
                                wrapx = 49
                                wrapy = x % 50 + 150
                                wrapangle = 180
                        elif face == 5:
                            if angle == 180:
                                # 5 << 2 >>
                                wrapx = 50
                                wrapy = 49 - y % 50
                                wrapangle = 0
                            if angle == 270:
                                # 5 ^^ 3 >>
                                wrapx = 50
                                wrapy = x % 50 + 50
                                wrapangle = 0
                        elif face == 6:
                            if angle == 0:
                                # 6 >> 4 ^^
                                wrapy = 149
                                wrapx = y % 50 + 50
                                wrapangle = 270
                            elif angle == 90:
                                # 6 vv 1 vv
                                wrapx = x + 100
                                wrapy = 0
                                wrapangle = 90
                            elif angle == 180:
                                # 6 << 2 vv
                                wrapx = y % 50 + 50
                                wrapy = 0
                                wrapangle = 90
                        wrap = (wrapx, wrapy)
                        if wrap == (99, 150):
                            assert True
                        if grid[wrap]:
                            x, y = wrap
                            angle = wrapangle
                            dx = int(math.cos(math.radians(angle)))
                            dy = int(math.sin(math.radians(angle)))
                        else:
                            break

            case "R":
                angle += 90
                angle %= 360
            case "L":
                angle -= 90
                angle %= 360
    return 1000 * (y + 1) + 4 * (x + 1) + (angle % 360) // 90


sample = """        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5"""


def main():
    data = aocd.get_data(day=22, year=2022).splitlines()
    # data = sample.splitlines()
    # print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
