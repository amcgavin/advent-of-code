import re


def ints(line):
    return list(map(int, re.findall(r"-?\d+", line)))


def floats(line):
    return list(map(float, re.findall(r"-?\d+(?:\.\d+)?", line)))


def words(line):
    return re.findall(r"[a-zA-Z]+", line)


def as_grid(data):
    grid = {}
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = c
    return grid


def as_table(data):
    grid = {}
    for y, line in enumerate(data):
        for x, c in enumerate(line.split()):
            grid[(x, y)] = c
    return grid


def immediate_neighbours(x, y):
    return {
        (x + 1, y),
        (x - 1, y),
        (x + 1, y - 1),
        (x + 1, y + 1),
        (x - 1, y + 1),
        (x - 1, y - 1),
        (x, y - 1),
        (x, y + 1),
    }


def all_directions():
    return ["U", "D", "L", "R", "UL", "UR", "DL", "DR"]


def cardinal_directions():
    return ["U", "L", "D", "R"]


def straight_line(x, y, direction, length):
    if direction == "U":
        return [(x, y - i) for i in range(1, length + 1)]
    if direction == "D":
        return [(x, y + i) for i in range(1, length + 1)]
    if direction == "L":
        return [(x - i, y) for i in range(1, length + 1)]
    if direction == "R":
        return [(x + i, y) for i in range(1, length + 1)]
    if direction == "UR":
        return [(x + i, y - i) for i in range(1, length + 1)]
    if direction == "UL":
        return [(x - i, y - i) for i in range(1, length + 1)]
    if direction == "DR":
        return [(x + i, y + i) for i in range(1, length + 1)]
    if direction == "DL":
        return [(x - i, y + i) for i in range(1, length + 1)]
