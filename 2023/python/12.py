import functools
import itertools
import multiprocessing
import math
import re

import aocd


def meets_criteria(partial, counts, remaining=True):
    g1 = tuple(len(list(g)) for k, g in itertools.groupby(partial.split("?")[0]) if k == "#")
    if not remaining:
        return g1 == counts
    if len(g1) == len(counts) and partial[-1] != "#":
        return g1 == counts
    if len(g1) > len(counts):
        return False

    if len(g1) > 0 and g1[:-1] != counts[: len(g1) - 1]:
        return False
    if len(g1) > 0 and g1[-1] > counts[len(g1) - 1]:
        return False
    return True


def part_1(data):
    m = 0
    for line in data:
        springs, counts = line.split(" ")
        counts = tuple(int(x) for x in counts.split(","))
        candidates = {""}
        for i, c in enumerate(springs):
            n = set()
            if c == "?":
                for cand in candidates:
                    if meets_criteria(cand + ".", counts):
                        n.add(cand + ".")
                    if meets_criteria(cand + "#", counts):
                        n.add(cand + "#")
            else:
                for cand in candidates:
                    if meets_criteria(cand + c, counts):
                        n.add(cand + c)
            candidates = n
        candidates = {c for c in candidates if meets_criteria(c, counts, remaining=False)}
        m += len(candidates)

    return m


@functools.cache
def fits_in(block, counts):
    if counts == (0,):
        return 0 if "#" in block else 1

    if all(x == "?" for x in block):
        groups = len(counts)
        empty = len(block) - (groups - 1) - sum(counts)
        if empty < 0:
            return 0
        return math.comb(groups + empty, groups)
    # now we have # in there
    groups = [(k, len(list(g))) for k, g in itertools.groupby(block)]
    first = block.index("#")


def part_2(data):
    m = 0
    for line in data:
        springs, counts = line.split(" ")
        counts = tuple(int(x) for x in counts.split(",")) * 5
        springs = ("." + "?".join([springs] * 5) + ".").replace(".", "..")

        print(f"{springs} {counts}")
        progression = iter(enumerate(counts))

        blocks = re.findall(r"\.([^.]+)\.", springs)


sample = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def main():
    data = [x for x in aocd.get_data(day=12, year=2023).splitlines()]
    data = sample.splitlines()
    print(part_1(data))
    print(part_2(data))
    # aocd.submit(str(part_2(data)), part='b', day=12, year=2023)


if __name__ == "__main__":
    main()
