from collections import defaultdict

import aocd
import re
import math


def part_1(data):
    total = 0
    for line in data:
        _, card = line.split(":")
        winners, numbers = card.split(" | ")
        winning = set(re.findall(r"\d+", winners))
        c = len([number for number in re.findall(r"\d+", numbers) if number in winning])
        if c:
            total += math.pow(2, c - 1)
    return total


def part_2(data):
    multiplier = defaultdict(lambda: 0)
    for i, line in enumerate(data, 1):
        multiplier[i] += 1
        winning = set()
        have = set()
        _, card = line.split(":")
        winners, numbers = card.split(" | ")
        for number in re.findall(r"\d+", winners):
            winning.add(number.strip())
        for number in re.findall(r"\d+", numbers):
            have.add(number.strip())

        count = len(have.intersection(winning))
        for c in range(i + 1, i + count + 1):
            multiplier[c] += multiplier[i]
    return sum(multiplier.values())


def main():
    data = [x for x in aocd.get_data(day=4, year=2023).splitlines()]

    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
