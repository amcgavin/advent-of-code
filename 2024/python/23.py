import itertools
import math
from collections import defaultdict

import aocd
import utils


def part_1(data: utils.Input):
    bidi = defaultdict(set)
    for line in data:
        c1, c2 = utils.words(line)
        bidi[c1].add(c2)
        bidi[c2].add(c1)

    triplets = set()
    for c1, c2 in itertools.combinations(bidi.keys(), 2):
        if c2 not in bidi[c1]:
            continue
        for c3 in bidi[c1].intersection(bidi[c2]):
            triplets.add(tuple(sorted([c1, c2, c3])))

    return sum(1 for t in triplets if any(ti[0] == "t" for ti in t))


def part_2(data: utils.Input):
    bidi = defaultdict(set)
    for line in data:
        c1, c2 = utils.words(line)
        bidi[c1].update([c1, c2])
        bidi[c2].update([c1, c2])

    groups = defaultdict(int)
    for c1, c2 in itertools.combinations(bidi.keys(), 2):
        groups[frozenset(bidi[c1] & (bidi[c2]))] += 1

    return max(
        (len(items), ",".join(sorted(items)))
        for items, c in groups.items()
        if math.comb(len(items), 2) == c
    )[1]


def main():
    data = [x for x in aocd.get_data(day=23, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
