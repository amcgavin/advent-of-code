import itertools
import re
from collections import Counter

import aocd

grammar_re = re.compile(r"(\w\w) -> (\w)")


def parse_data(data):
    start = data[0]
    rules = [grammar_re.match(line).groups() for line in data[2:]]

    return start, dict(rules)


def pairwise(iterable):
    # https://docs.python.org/3/library/itertools.html#itertools.pairwise
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG

    a, b = itertools.tee(iterable)
    next(b, None)
    return ("".join(x) for x in zip(a, b))


def part_1(data):
    start, rules = parse_data(data)
    current_polymer = start
    for _ in range(10):
        insertions = (rules[pair] for pair in pairwise(current_polymer))
        current_polymer = "".join(
            f"{a}{b}" for a, b in itertools.zip_longest(current_polymer, insertions, fillvalue="")
        )
    common = Counter(current_polymer).most_common()
    return common[0][1] - common[-1][1]


def part_2(data):
    start, rules = parse_data(data)
    pairs = Counter(list(pairwise(start)))

    for _ in range(40):
        next_pairs = Counter()
        for pair, count in pairs.items():
            rule = rules[pair]
            next_pairs.update({f"{pair[0]}{rule}": count, f"{rule}{pair[1]}": count})
        pairs = next_pairs

    totals = Counter()
    for (char, _), count in pairs.items():
        # only take the first item, we'll be off by 1 at the end.
        totals.update({char: count})

    # add in last char again
    totals.update([start[-1]])

    common = totals.most_common()
    return common[0][1] - common[-1][1]


def main():
    data = aocd.get_data(day=14, year=2021).splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
