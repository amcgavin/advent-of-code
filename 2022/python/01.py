import aocd


def part_1(data):
    groups = []
    total = 0
    for n in data:
        if n == "":
            groups.append(total)
            total = 0
        else:
            total += int(n)
    return max(groups)


def part_2(data):
    groups = []
    total = 0
    for n in data:
        if n == "":
            groups.append(total)
            total = 0
        else:
            total += int(n)
    return sum(sorted(groups)[-3:])


def main():
    data = [x for x in aocd.get_data(day=1, year=2022).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
