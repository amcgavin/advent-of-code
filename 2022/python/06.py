import aocd


def part_1(data):
    return next(i for i in range(len(data)) if len(set(data[i - 4 : i])) == 4)


def part_2(data):
    return next(i for i in range(len(data)) if len(set(data[i - 14 : i])) == 14)


def main():
    data = aocd.get_data(day=6, year=2022)
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
