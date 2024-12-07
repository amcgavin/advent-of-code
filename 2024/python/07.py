import aocd
import utils
import operator
import itertools
import functools


def part_1(data: utils.Input):
    t = 0
    for line in data:
        test, initial, *parts = utils.ints(line)
        if any(
            test == functools.reduce(lambda x, el: el[0](x, el[1]), zip(operations, parts), initial)
            for operations in itertools.product([operator.add, operator.mul], repeat=len(parts))
        ):
            t += test
    return t


def concat(a, b):
    return int(str(a) + str(b))


def part_2(data: utils.Input):
    t = 0
    for line in data:
        test, initial, *parts = utils.ints(line)
        if any(
            test == functools.reduce(lambda x, el: el[0](x, el[1]), zip(operations, parts), initial)
            for operations in itertools.product(
                [operator.add, operator.mul, concat], repeat=len(parts)
            )
        ):
            t += test
    return t


def main():
    data = [x for x in aocd.get_data(day=7, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
