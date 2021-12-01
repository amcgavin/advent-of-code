import typing as t

import aocd


def num_increases(data: t.List[int]):
    previous = None
    total = 0
    for i, current in enumerate(data):
        if i > 0 and current > previous:
            total += 1
        previous = current
    return total


def part_1(data):
    return num_increases(data)


def part_2(data):
    windows = [sum(data[i : i + 3]) for i in range(len(data)) if i <= len(data) - 3]
    return num_increases(windows)


def main():
    data = [int(x) for x in aocd.get_data(day=1, year=2021).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
