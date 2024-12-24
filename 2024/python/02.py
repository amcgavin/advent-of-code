import math
import re
import aocd
from parse import parse


def check(numbers):
    return all(1 <= abs(n1 - n2) <= 3 for n1, n2 in zip(numbers, numbers[1:])) and (
        all(n1 > n2 for n1, n2 in zip(numbers, numbers[1:]))
        or all(n1 < n2 for n1, n2 in zip(numbers, numbers[1:]))
    )


def part_1(data):
    c = 0
    for line in data:
        numbers = [int(x) for x in re.findall(r"(\d+)", line)]
        if check(numbers):
            c += 1
    return c


def part_2(data):
    c = 0
    for line in data:
        numbers = [int(x) for x in re.findall(r"(\d+)", line)]
        if check(numbers):
            c += 1
        else:
            for i in range(len(numbers)):
                num2 = [*numbers]
                num2.pop(i)
                if check(num2):
                    c += 1
                    break
    return c


def main():
    data = [x for x in aocd.get_data(day=2, year=2024).splitlines()]

    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
