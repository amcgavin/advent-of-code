from collections import Counter

import aocd


def part_1(data):
    binary = "".join(Counter(row).most_common()[0][0] for row in zip(*data))
    gamma = int(binary, base=2)
    return gamma * (~gamma & ((1 << len(binary)) - 1))


def filter_common(remaining, reverse=False, position=0):
    if len(remaining) == 1:
        return remaining[0]
    most_common = sorted(
        Counter((r[position] for r in remaining)).most_common(),
        key=lambda x: tuple(reversed(x)),
        reverse=reverse,
    )[0][0]
    return filter_common(
        list(filter(lambda x: x[position] == most_common, remaining)),
        reverse=reverse,
        position=position + 1,
    )


def part_2(data):
    return int(filter_common(data), base=2) * int(filter_common(data, reverse=True), base=2)


def main():
    data = aocd.get_data(day=3, year=2021).splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
