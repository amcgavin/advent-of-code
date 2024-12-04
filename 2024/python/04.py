import aocd
import utils


def part_1(data):
    total = 0
    grid = utils.as_grid(data)
    for (x, y), start in grid.items():
        if start != "X":
            continue
        for direction in utils.all_directions():
            if (
                "".join(grid.get(coord, "") for coord in utils.straight_line(x, y, direction, 3))
                == "MAS"
            ):
                total += 1

    return total


def options(x, y):
    yield [
        (x - 1, y - 1, "M"),
        (x - 1, y + 1, "M"),
        (x + 1, y - 1, "S"),
        (x + 1, y + 1, "S"),
    ]
    yield [
        (x + 1, y - 1, "M"),
        (x + 1, y + 1, "M"),
        (x - 1, y - 1, "S"),
        (x - 1, y + 1, "S"),
    ]
    yield [
        (x - 1, y - 1, "S"),
        (x - 1, y + 1, "M"),
        (x + 1, y - 1, "S"),
        (x + 1, y + 1, "M"),
    ]
    yield [
        (x + 1, y - 1, "M"),
        (x + 1, y + 1, "S"),
        (x - 1, y - 1, "M"),
        (x - 1, y + 1, "S"),
    ]


def part_2(data):
    total = 0
    grid = utils.as_grid(data)
    for (x, y), start in grid.items():
        if start != "A":
            continue
        for option in options(x, y):
            if all(grid.get((x2, y2)) == l for x2, y2, l in option):
                total += 1

    return total


def main():
    data = [x for x in aocd.get_data(day=4, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
