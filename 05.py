def get_input():
    with open("./05.txt", mode="r") as fp:
        for line in fp.readlines():
            line = line.strip()
            if line:
                yield line


def get_seat_ids():
    seat_ids = set()
    for line in get_input():
        binary = line.translate("FBLR".maketrans(dict(F="0", B="1", L="0", R="1")))
        row = int(binary[:7], base=2)
        col = int(binary[7:], base=2)
        seat_ids.add(row * 8 + col)
    return seat_ids


def part1():
    return max(get_seat_ids())


def part2():
    ids = get_seat_ids()
    for i in ids:
        if not ids.issuperset({i - 1, i + 1}):
            if i == min(ids) or i == max(ids):
                continue
            return i + 1


if __name__ == "__main__":
    print(part1())
    print(part2())
