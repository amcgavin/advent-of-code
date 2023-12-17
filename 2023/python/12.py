import functools
import itertools


import aocd


@functools.cache
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


def solve(line, counts):
    dp = [[] for _ in range(len(counts))]
    for i, num in enumerate(counts):
        for j, c in enumerate(line):
            dp[i].append(0)
            start = j - num + 1
            if c == "." or start < 0:
                continue

            if "." in line[start : j + 1]:
                continue
            if j + 1 < len(line) and line[j + 1] == "#":
                continue

            if i == 0:
                dp[i][j] = 1 if "#" not in line[:start] else 0
                continue

            total = 0
            for end in range(start - 1):
                if "#" not in line[end + 1 : start]:
                    total += dp[i - 1][end]
            dp[i][j] = total

    total = 0
    for pos in range(len(line) - 1, -1, -1):
        if line[pos] == "#":
            total += dp[len(counts) - 1][pos]
            break
        elif line[pos] == "?":
            total += dp[len(counts) - 1][pos]

    return total


def part_2(data):
    total = 0
    for line in data:
        springs, counts = line.split(" ")
        counts = tuple(int(x) for x in counts.split(",")) * 5
        springs = "?".join([springs] * 5)
        total += solve(springs, counts)
    return total


def main():
    data = [x for x in aocd.get_data(day=12, year=2023).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
