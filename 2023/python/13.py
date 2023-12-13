import aocd


def find_mirror_y(grid, data, expected=0):
    for y in range(len(data) - 1):
        total = 0
        for i in range(0, y + 1):
            total += sum(
                1
                if grid.get((x, y - i), grid.get((x, y + i + 1)))
                != grid.get((x, y + i + 1), grid.get((x, y - i)))
                else 0
                for x in range(len(data[0]))
            )
        if total == expected:
            return y + 1
    return 0


def find_mirror_x(grid, data, expected=0):
    for x in range(len(data[0]) - 1):
        total = 0
        for i in range(0, (x + 1)):
            total += sum(
                1
                if grid.get((x - i, y), grid.get((x + i + 1, y)))
                != grid.get((x + i + 1, y), grid.get((x - i, y)))
                else 0
                for y in range(len(data))
            )

        if total == expected:
            return x + 1
    return 0


def part_1(inp):
    d = "\n".join(inp)
    datum = d.split("\n\n")
    total = 0
    for puzzle in datum:
        data = puzzle.splitlines()
        grid = {}
        for y, line in enumerate(data):
            for x, c in enumerate(line):
                grid[(x, y)] = c

        total += 100 * find_mirror_y(grid, data, expected=0)
        total += find_mirror_x(grid, data, expected=0)

    return total


def part_2(inp):
    d = "\n".join(inp)
    datum = d.split("\n\n")
    total = 0
    for puzzle in datum:
        data = puzzle.splitlines()
        grid = {}
        for y, line in enumerate(data):
            for x, c in enumerate(line):
                grid[(x, y)] = c

        total += 100 * find_mirror_y(grid, data, expected=1)
        total += find_mirror_x(grid, data, expected=1)

    return total


def main():
    data = [x for x in aocd.get_data(day=13, year=2023).splitlines()]

    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
