import re

import aocd


def part_1(data):
    a = 0
    for line in data:
        numbers = [int(x) for x in re.findall(r"(-?\d+)", line)]
        s = [numbers]
        while any(n != 0 for n in numbers):
            numbers = [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]
            s.append(numbers)
        s = list(reversed(s))
        for i, n in enumerate(s[1:], 1):
            n.append(n[-1] + s[i - 1][-1])
        a += s[-1][-1]
    return a


def part_2(data):
    a = 0
    for line in data:
        numbers = [int(x) for x in re.findall(r"(-?\d+)", line)]
        s = [numbers]
        while any(n != 0 for n in numbers):
            numbers = [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]
            s.append(numbers)
        s = list(reversed(s))
        for i, n in enumerate(s[1:], 1):
            n.insert(0, n[0] - s[i - 1][0])
        a += s[-1][0]
    return a


def main():
    data = [x for x in aocd.get_data(day=9, year=2023).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
