import itertools

import aocd
import utils

import sympy


def naive_solve(ax, ay, bx, by, px, py):
    candidates = []
    for a in range(max(px // ax, py // ax)):
        for b in range(max(px // bx, py // by)):
            if ax * a + bx * b == px and ay * a + by * b == py:
                candidates.append(a * 3 + b)
    if len(candidates) == 1:
        return candidates[0]
    if len(candidates) == 0:
        return 0
    return min(*candidates)


def faster_solve(ax, ay, bx, by, px, py):
    a, b = sympy.symbols("a,b")
    eq1 = sympy.Eq(a * ax + b * bx, px)
    eq2 = sympy.Eq(a * ay + b * by, py)
    r = sympy.solve([eq1, eq2], (a, b))
    if r[a].is_integer and r[b].is_integer:
        return int(r[a] * 3 + r[b])

    return 0


def part_1(data: utils.Input):
    total = 0
    for a, b, p, _ in itertools.batched(data + [""], 4):
        ax, ay = utils.ints(a)
        bx, by = utils.ints(b)
        px, py = utils.ints(p)
        total += faster_solve(ax, ay, bx, by, px, py)

    return total


def part_2(data: utils.Input):
    total = 0
    for a, b, p, _ in itertools.batched(data + [""], 4):
        ax, ay = utils.ints(a)
        bx, by = utils.ints(b)
        px, py = utils.ints(p)
        total += faster_solve(ax, ay, bx, by, px + 10000000000000, py + 10000000000000)

    return total


def main():
    data = [x for x in aocd.get_data(day=13, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
