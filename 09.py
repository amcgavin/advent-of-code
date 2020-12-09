def get_input():
    with open("./09.txt", mode="r") as fp:
        for line in fp.readlines():
            line = line.strip()
            if line:
                yield line


def part1():
    numbers = [int(line) for line in get_input()]
    for i in range(25, len(numbers)):
        if not any(
            (numbers[i] - n) in set(numbers[i - 25 : i]) and numbers[i] / 2 != n
            for n in numbers
        ):
            return numbers[i]


def part2():
    target = part1()
    numbers = [int(line) for line in get_input()]
    start = end = 0
    while end < len(numbers):
        ans = sum(numbers[start:end])
        if ans == target:
            return min(numbers[start:end]) + max(numbers[start:end])
        if ans < target:
            end += 1
        if ans > target:
            start += 1


if __name__ == "__main__":
    print(part1())
    print(part2())
