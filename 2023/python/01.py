import re

import aocd


def part_1(data):
    regexp = re.compile(r"\d")
    return sum(map(lambda g: int(f"{g[0]}{g[-1]}"), map(lambda n: regexp.findall(n), data)))


def part_2(data):
    total = 0
    mapper = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }
    for n in data:
        r = len(n)
        l1 = None
        for i in range(r):
            if l1:
                break
            for j in range(r):
                word = n[i : i + j]
                if word in mapper:
                    l1 = mapper[word]
                    break
        l2 = None
        n2 = n[::-1]
        for i in range(r):
            if l2:
                break
            for j in range(r):
                word = "".join(reversed(n2[i : i + j]))
                if word in mapper:
                    l2 = mapper[word]
                    break
        y = int(f"{l1}{l2}")

        total += y
    return total


def main():
    data = [x for x in aocd.get_data(day=1, year=2023).splitlines()]

    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
