from collections import Counter

import aocd

mapping = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}


def part_1(data):
    total = 0
    for line in data:
        source, _, output = line.partition(" | ")
        output = output.split(" ")
        total += sum(1 for digit in output if len(digit) in (2, 3, 4, 7))

    return total


def part_2(data):
    total = 0
    for line in data:
        source, _, output = line.partition(" | ")
        source = source.split(" ")
        output = output.split(" ")

        # length of the segments reveals unique number sets
        digits = sorted(source, key=lambda s: (len(s)))

        # frequency analysis reveals unique segments
        counts = [c[0] for c in Counter("".join(source)).most_common()]
        key = {}

        # bottom right
        key["f"] = counts[0]

        # top left
        key["b"] = counts[5]

        # bottom left
        key["e"] = counts[6]

        # `a` (top) is in `7` but not in `1`
        key["a"] = next(c for c in digits[1] if c not in digits[0])

        # `c` (top right) is the 2nd most common (and not `a`)
        key["c"] = next(c for c in counts[1:3] if c not in key.values())

        # `4` contains `d` (middle) but not `g`
        key["d"] = next(c for c in digits[2] if c not in key.values())

        # `g` (bottom) is whatever is left
        key["g"] = next(c for c in digits[-1] if c not in key.values())
        key = {value: key for key, value in key.items()}

        total += int(
            "".join(
                mapping["".join(sorted(digit.translate("abcdefg".maketrans(key))))]
                for digit in output
            )
        )

    return total


def main():
    data = aocd.get_data(day=8, year=2021).splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
