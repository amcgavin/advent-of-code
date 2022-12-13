import sys

import aocd


def part_1(data):
    result = 0
    x = 1
    cycle = 0

    def add_cycle():
        nonlocal cycle
        nonlocal result
        cycle += 1
        if (cycle + 20) % 40 == 0:
            result += cycle * x

    for line in data:
        match line.split(" "):
            case ["noop"]:
                add_cycle()
            case ["addx", value]:
                add_cycle()
                add_cycle()
                x += int(value)

    return result


def part_2(data):
    x = 1
    cycle = 0

    def add_cycle():
        nonlocal cycle
        if cycle in {x - 1, x, x + 1}:
            sys.stdout.write("▓▓▓")
        else:
            sys.stdout.write("   ")
        cycle += 1
        if cycle == 40:
            cycle = 0
            sys.stdout.write("\n")

    for line in data:
        match line.split(" "):
            case ["noop"]:
                add_cycle()
            case ["addx", value]:
                add_cycle()
                add_cycle()
                x += int(value)


def main():
    data = [x for x in aocd.get_data(day=10, year=2022).splitlines()]
    print(part_1(data))
    part_2(data)


if __name__ == "__main__":
    main()
