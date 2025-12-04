import aocd
import utils


def part_1(data):
    grid = dict(utils.as_grid(data))
    total = 0
    for (x, y), c in grid.items():
        if c == ".":
            continue
        if sum(grid.get((p1, p2), ".") == "@" for p1, p2 in utils.immediate_neighbours(x, y)) < 4:
            total += 1

    return total


def part_2(data):
    grid = dict(utils.as_grid(data))
    q = [(x, y) for (x, y), c in grid.items() if c == "@"]
    total = 0
    working = True
    while working:
        working = False
        nq = []
        for x, y in q:
            if (
                sum(grid.get((p1, p2), ".") == "@" for p1, p2 in utils.immediate_neighbours(x, y))
                < 4
            ):
                total += 1
                grid[(x, y)] = "."
                working = True
            else:
                nq.append((x, y))
        q = nq
    return total


def main():
    data = [x for x in aocd.get_data(day=4, year=2025).splitlines()]
    # data=sample.splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
