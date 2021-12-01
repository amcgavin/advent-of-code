def get_input():
    with open("./06.txt", mode="r") as fp:
        for line in fp.readlines():
            yield line.strip()
        yield ""


def part1():
    count = 0
    current = set()
    for line in get_input():
        current.update(line)
        if line == "":
            count += len(current)
            current = set()
    return count


def part2():
    count = 0
    current = None
    for line in get_input():
        if line == "":
            count += len(current)
            current = None
            continue
        if current is None:
            current = set(line)
        current = current.intersection(set(line))

    return count


if __name__ == "__main__":
    print(part1())
    print(part2())
