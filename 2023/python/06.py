import math

import aocd
import re


def part_1(data):
    times = [int(x) for x in re.findall(r"\d+", data[0])]
    distances = [int(x) for x in re.findall(r"\d+", data[1])]
    totals = []
    for t, d in zip(times, distances):
        total = sum(1 for i in range(t) if i * (t - i) > d)
        totals.append(total)
    return math.prod(totals)


def part_2(data):
    t = int("".join(re.findall(r"\d+", data[0])))
    d = int("".join(re.findall(r"\d+", data[1])))
    return sum(1 for i in range(t) if i * (t - i) > d)


def main():
    data = [x for x in aocd.get_data(day=6, year=2023).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
