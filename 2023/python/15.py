from collections import defaultdict

import aocd


def part_1(data):
    total = 0
    numbers = data[0].split(",")
    for n in numbers:
        c = 0
        for m in n:
            b = ord(m)
            c += b
            c *= 17
            c = c % 256
        total += c
    return total


def part_2(data):
    total = 0
    hm = defaultdict(dict)
    numbers = data[0].split(",")
    for n in numbers:
        c = 0
        if n.endswith("-"):
            label = n[:-1]
            eq = 0
            action = "-"
        else:
            label, action, eq = n.partition("=")
        for m in label:
            b = ord(m)
            c += b
            c *= 17
            c = c % 256
        if action == "-":
            hm[c] = {k: v for k, v in hm[c].items() if k != label}
        else:
            hm[c][label] = int(eq)

    for b in range(1, 257):
        v = hm[b - 1]
        for i, (label, focus) in enumerate(v.items(), 1):
            total += i * focus * b
    return total


def main():
    data = [x for x in aocd.get_data(day=15, year=2023).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
