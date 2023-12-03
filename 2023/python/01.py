import re
import itertools
import aocd


def part_1(data):
    regexp = re.compile(r"\d")
    return sum(map(lambda g: int(f"{g[0]}{g[-1]}"), map(lambda n: regexp.findall(n), data)))


def part_2(data):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    regexp = "|".join(itertools.chain(numbers, (str(x) for x in range(1, 10))))
    reverse_regexp = "".join(reversed(regexp))
    mapping = {key: str(value) for value, key in enumerate(numbers, start=1)}
    mapping.update({"".join(reversed(k)): v for k, v in mapping.items()})

    total = 0
    for line in data:
        l1 = next(re.finditer(regexp, line)).group()
        l2 = next(re.finditer(reverse_regexp, line[::-1])).group()
        total += int(f"{mapping.get(l1, l1)}{mapping.get(l2, l2)}")

    return total


def main():
    data = [x for x in aocd.get_data(day=1, year=2023).splitlines()]

    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
