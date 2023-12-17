import aocd


def next_square(x, y, direction):
    if direction == "N":
        return x, y - 1
    if direction == "S":
        return x, y + 1
    if direction == "E":
        return x + 1, y
    if direction == "W":
        return x - 1, y


def solve(start, grid):
    energised = set()
    beams = {start}
    seen = set()
    while beams:
        x, y, direction = beams.pop()
        x1, y1 = next_square(x, y, direction)
        if (x1, y1) not in grid:
            continue
        energised.add((x1, y1))
        if (x1, y1, direction) in seen:
            continue
        seen.add((x1, y1, direction))
        c = grid[(x1, y1)]
        if c == ".":
            beams.add((x1, y1, direction))
        elif c == "/":
            direction = {"E": "N", "N": "E", "W": "S", "S": "W"}[direction]
            beams.add((x1, y1, direction))
        elif c == "\\":
            direction = {"E": "S", "S": "E", "W": "N", "N": "W"}[direction]
            beams.add((x1, y1, direction))
        elif c == "|":
            if direction in ("N", "S"):
                beams.add((x1, y1, direction))
            else:
                beams.add((x1, y1, "N"))
                beams.add((x1, y1, "S"))
        elif c == "-":
            if direction in ("E", "W"):
                beams.add((x1, y1, direction))
            else:
                beams.add((x1, y1, "E"))
                beams.add((x1, y1, "W"))
    return len(energised)


def part_1(data):
    grid = {}
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = c

    return solve((-1, 0, "E"), grid)


def part_2(data):
    grid = {}

    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = c

    starters = []
    for i in range(len(data)):
        starters.append((-1, i, "E"))
        starters.append((len(data), i, "W"))
        starters.append((i, len(data), "N"))
        starters.append((i, -1, "S"))
    return max(solve(start, grid) for start in starters)


def main():
    data = [x for x in aocd.get_data(day=16, year=2023).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
