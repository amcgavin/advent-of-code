from collections import Counter
import aocd
from parse import parse


def part_1(data):
    a1 = []
    a2 = []
    for line in data:
        l1, _, l2 = parse("{:d}{:s}{:d}", line)
        a1.append(int(l1))
        a2.append(int(l2))
    a1 = sorted(a1)
    a2 = sorted(a2)
    return sum(abs(l1 - l2) for l1, l2 in zip(a1, a2))


def part_2(data):
    a1 = []
    a2 = []
    for line in data:
        l1, _, l2 = parse("{:d}{:s}{:d}", line)
        a1.append(int(l1))
        a2.append(int(l2))
    a1 = sorted(a1)
    a2 = Counter(a2)
    return sum(l1 * a2.get(l1, 0) for l1 in a1)


def main():
    data = [x for x in aocd.get_data(day=1, year=2024).splitlines()]

    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
