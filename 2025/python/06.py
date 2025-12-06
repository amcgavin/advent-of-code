import functools

import aocd
import utils
import operator


def part_1(data):
    ops = list(data[-1].replace(" ", ""))
    numbers = list(zip(*[utils.ints(line) for line in data[:-1]]))
    return sum(
        functools.reduce(operator.add if ops[i] == "+" else operator.mul, ns)
        for i, ns in enumerate(numbers)
    )


def part_2(data):
    ops = list(data[-1].replace(" ", ""))
    algos = list(zip(*data[:-1]))
    return sum(
        functools.reduce(operator.add if ops[i] == "+" else operator.mul, (int(x) for x in numbers))
        for i, numbers in enumerate(
            utils.partition_sections(["".join(x.strip() for x in a) for a in algos])
        )
    )


def main():
    data = [x for x in aocd.get_data(day=6, year=2025).splitlines()]

    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
