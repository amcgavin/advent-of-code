from collections import Counter

import aocd


def calculate(initial, days):
    new = Counter(initial)
    for _ in range(days):
        new = {key - 1: value for key, value in new.items()}
        c = new.pop(-1, 0)
        new[6] = new.get(6, 0) + c
        new[8] = new.get(8, 0) + c
    return sum(new.values())


def part_1(data):
    return calculate([int(x) for x in data[0].split(",")], 80)


def part_2(data):
    return calculate([int(x) for x in data[0].split(",")], 256)


def main():
    data = aocd.get_data(day=6, year=2021).splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
