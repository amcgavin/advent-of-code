import re
import aocd


def part_1(data):
    total = 0
    sequence = "".join(data)
    for match in re.findall(r"mul\((\d+),(\d+)\)", sequence):
        a, b = map(int, match)
        total += a * b
    return total


def part_2(data):
    total = 0
    sequence = "".join(data)
    sequence = re.sub(r"don't\(\).*?do\(\)", "", sequence)
    sequence = re.sub(r"don't\(\).*$", "", sequence)
    for match in re.findall(r"mul\((\d+),(\d+)\)", sequence):
        a, b = map(int, match)
        total += a * b
    return total


def main():
    data = [x for x in aocd.get_data(day=3, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
