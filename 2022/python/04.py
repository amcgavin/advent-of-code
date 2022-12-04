import re

import aocd

expr = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")


def part_1(data):
    count = 0
    for row in data:
        l1, l2, r1, r2 = (int(x) for x in expr.match(row).groups())
        if (l1 <= r1 and l2 >= r2) or (r1 <= l1 and r2 >= l2):
            count += 1
    return count


def part_2(data):
    count = 0
    for row in data:
        l1, l2, r1, r2 = (int(x) for x in expr.match(row).groups())
        if r1 <= l2 and l1 <= r2:
            count += 1
    return count


def main():
    data = [x for x in aocd.get_data(day=4, year=2022).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
