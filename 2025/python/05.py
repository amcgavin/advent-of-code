import aocd
import utils


def part_1(data):
    r, ingredients = utils.partition_sections(data)
    ranges = []
    for rr in r:
        x, y = rr.split("-")
        ranges.append((int(x), int(y)))

    total = 0
    for i in ingredients:
        i = int(i)
        for mm, mx in ranges:
            if mm <= i <= mx:
                total += 1
                break

    return total


def part_2(data):
    r, ingredients = utils.partition_sections(data)
    ranges = []
    for rr in r:
        x, y = rr.split("-")
        ranges.append([int(x), int(y)])

    ranges = sorted(ranges)
    nr = [ranges[0]]
    for mm, mx in ranges:
        if mm <= nr[-1][1] and mx <= nr[-1][1]:
            continue
        elif mm <= nr[-1][1]:
            nr[-1][1] = max(mx, nr[-1][1])
        else:
            nr.append([mm, mx])

    return sum(mx - mn + 1 for mn, mx in nr)


def main():
    data = [x for x in aocd.get_data(day=5, year=2025).splitlines()]

    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
