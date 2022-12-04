import re

import aocd

expr = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")


def part_1(data):
    return sum(
        (l1 <= r1 and l2 >= r2) or (r1 <= l1 and r2 >= l2)
        for l1, l2, r1, r2 in ([int(x) for x in expr.match(row).groups()] for row in data)
    )


def part_2(data):
    return sum(
        r1 <= l2 and l1 <= r2
        for l1, l2, r1, r2 in ([int(x) for x in expr.match(row).groups()] for row in data)
    )


def main():
    data = [x for x in aocd.get_data(day=4, year=2022).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
