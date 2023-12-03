import math
import re
import aocd


def immediate_neighbours(x, y):
    return {
        (x + 1, y),
        (x - 1, y),
        (x + 1, y - 1),
        (x + 1, y + 1),
        (x - 1, y + 1),
        (x - 1, y - 1),
        (x, y - 1),
        (x, y + 1),
    }


class Symbol:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


def part_1(data):
    total = 0
    exp = re.compile(r"[^0-9.]")
    mapping = {}

    numbers = {}
    for y, line in enumerate(data):
        num = ""
        parts = []

        def write_contents():
            if num:
                s = Symbol(num)
                for part in parts:
                    numbers[part] = s

        for x, c in enumerate(line):
            mapping[(x, y)] = c
            if c.isdigit():
                num += c
                parts.append((x, y))
            else:
                write_contents()
                num = ""
                parts = []

        write_contents()

    adjacent = set()
    for (x, y), c in mapping.items():
        for x2, y2 in immediate_neighbours(x, y):
            if exp.match(mapping.get((x2, y2), ".")):
                if c.isdigit():
                    adjacent.add((x, y))

    seen = set()
    for x, y in adjacent:
        n = numbers.get((x, y))
        if n and n not in seen:
            seen.add(n)
            total += int(n.value)

    return total


def part_2(data):
    total = 0
    mapping = {}
    numbers = {}
    for y, line in enumerate(data):
        num = ""
        parts = []

        def write_contents():
            if num:
                s = Symbol(num)
                for part in parts:
                    numbers[part] = s

        for x, c in enumerate(line):
            mapping[(x, y)] = c
            if c.isdigit():
                num += c
                parts.append((x, y))
            else:
                write_contents()
                num = ""
                parts = []

        write_contents()

    for (x, y), c in mapping.items():
        if c == "*":
            adjacent = set()
            for x2, y2 in immediate_neighbours(x, y):
                s = numbers.get((x2, y2))
                if s:
                    adjacent.add(s)
            if len(adjacent) == 2:
                total += math.prod(int(x.value) for x in adjacent)
    return total


def main():
    data = [x for x in aocd.get_data(day=3, year=2023).splitlines()]

    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
