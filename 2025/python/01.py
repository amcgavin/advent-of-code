import aocd
import utils


def part_1(data):
    c = 0
    p = 50

    for line in data:
        n = utils.ints(line.replace("L", "-").replace("R", ""))[0]
        p += n
        p %= 100
        if p == 0:
            c += 1
    return c


def part_2(data):
    c = 0
    p = 50
    for line in data:
        n = utils.ints(line.replace("L", "-").replace("R", ""))[0]
        if (p + n) * p < 0:
            c += 1
        p += n
        if p == 0:
            c += 1
        c += abs(p) // 100
        p %= 100
    return c


def main():
    data = [x for x in aocd.get_data(day=1, year=2025).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
