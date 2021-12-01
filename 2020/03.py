def get_input():
    with open("./03.txt", mode="r") as fp:
        for line in fp.readlines():
            yield line.strip()


def traverse_slope(right=3, down=1) -> int:
    count = 0
    pos = 0
    inputs = get_input()
    # always skip the first line
    line = next(inputs)
    while True:
        pos += right
        for _ in range(down):
            line = next(inputs, None)
        if line is None:
            return count
        if line[pos % len(line)] == "#":
            count += 1


def part1():
    return traverse_slope()


def part2():
    return (
        traverse_slope(right=1, down=1)
        * traverse_slope(right=3, down=1)
        * traverse_slope(right=5, down=1)
        * traverse_slope(right=7, down=1)
        * traverse_slope(right=1, down=2)
    )


if __name__ == "__main__":
    print(part1())
    print(part2())
