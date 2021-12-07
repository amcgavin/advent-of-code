import statistics

import aocd


def part_1(data):
    median = statistics.median(data)
    return sum([abs(median - x) for x in data])


def series(n):
    return n * (n + 1) / 2


def part_2(data):
    avg = int(statistics.mean(data))
    return sum(series(abs(x - avg)) for x in data)


def main():
    data = [int(x) for x in aocd.get_data(day=7, year=2021).split(",")]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
