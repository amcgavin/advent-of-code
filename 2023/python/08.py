import math
import aocd
from parse import parse


def part_1(data):
    path = data[0]
    m = {
        start: (left, right)
        for start, left, right in (parse("{} = ({}, {})", line) for line in data[2:])
    }
    i = 0
    s = "AAA"
    while s != "ZZZ":
        step = path[i % len(path)]
        s = m[s][0 if step == "L" else 1]
        i += 1
    return i


def part_2(data):
    path = data[0]
    m = {
        start: (left, right)
        for start, left, right in (parse("{} = ({}, {})", line) for line in data[2:])
    }
    mods = []
    for s in [x for x in m.keys() if x[2] == "A"]:
        i = 0
        while s[2] != "Z":
            step = path[i % len(path)]
            s = m[s][0 if step == "L" else 1]
            i += 1
        mods.append(i)
    return math.lcm(*mods)


def main():
    data = [x for x in aocd.get_data(day=8, year=2023).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
