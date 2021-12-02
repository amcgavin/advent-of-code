import re

import aocd

commands_re = re.compile(r"(forward|down|up) (\d+)")


def part_1(data):
    horizontal = depth = 0
    for command, value in data:
        if command == "forward":
            horizontal += int(value)
        elif command == "up":
            depth -= int(value)
        elif command == "down":
            depth += int(value)
    return horizontal * depth


def part_2(data):
    horizontal = depth = aim = 0
    for command, value in data:
        if command == "forward":
            horizontal += int(value)
            depth += aim * int(value)
        elif command == "up":
            aim -= int(value)
        elif command == "down":
            aim += int(value)
    return horizontal * depth


def main():
    data = [
        commands_re.match(line).groups() for line in aocd.get_data(day=2, year=2021).splitlines()
    ]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
