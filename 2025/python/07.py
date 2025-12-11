import functools
import aocd
import utils


def part_1(data):
    grid = dict(utils.as_grid(data))
    start = next((x, y) for (x, y), c in grid.items() if c == "S")
    total = 0
    seen = set()
    beams = [start]
    while beams:
        n = beams.pop(0)
        if n in seen:
            continue
        seen.add(n)
        nt = grid.get(n, None)
        if nt is None:
            continue
        nd = utils.directional_add(*n, "D")
        if nt == "^":
            total += 1
            beams.extend([utils.directional_add(*nd, "L"), utils.directional_add(*nd, "R")])
        else:
            beams.append(nd)

    return total


@functools.cache
def recurse(g, start):
    grid = dict(g)

    nt = grid.get(start, None)
    if nt is None:
        return 1
    ne = utils.directional_add(*start, "D")
    if nt == "^":
        return recurse(g, utils.directional_add(*ne, "L")) + recurse(
            g, utils.directional_add(*ne, "R")
        )

    return recurse(g, ne)


def part_2(data):
    grid = dict(utils.as_grid(data))
    start = next((x, y) for (x, y), c in grid.items() if c == "S")
    return recurse(tuple(grid.items()), start)


def main():
    data = [x for x in aocd.get_data(day=7, year=2025).splitlines()]

    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
