import itertools
import math


import aocd
import utils


def part_1(data: utils.Input):
    locks = []
    keys = []
    for schema in utils.partition_sections(data):
        l = tuple(sum(1 for c in col if c == "#") for col in zip(*schema[::-1]))
        if schema[0][0] == "#":
            locks.append(l)
        else:
            keys.append(l)

    return sum(
        all(a + b <= 7 for a, b in zip(lock, key)) for lock, key in itertools.product(locks, keys)
    )


def main():
    data = [x for x in aocd.get_data(day=25, year=2024).splitlines()]
    print(part_1(data))


if __name__ == "__main__":
    main()
