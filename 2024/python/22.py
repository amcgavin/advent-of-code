import functools
import itertools
import math

import aocd
import utils


def mix(n1, n2):
    return n1 ^ n2


def prune(n):
    return n % 16777216


def next_secret(s):
    s = prune(mix(s * 64, s))
    s = prune(mix(s, (s // 32)))
    return prune(mix(s, s * 2048))


def part_1(data: utils.Input):
    total = 0
    for line in data:
        s = int(line)
        for _ in range(2000):
            s = next_secret(s)
        total += s
    return total


def part_2(data: utils.Input):
    monkeys = []
    for line in data:
        s = int(line)
        price = s % 10
        seq = []
        lookup = {}
        monkeys.append(lookup)
        for _ in range(2000):
            s = next_secret(s)
            np = s % 10
            seq.append(np - price)

            idx = tuple(seq[-4:])
            if idx not in lookup:
                lookup[idx] = np
            price = np

    uniq = set(itertools.chain.from_iterable(monkey.keys() for monkey in monkeys))
    return max(sum(monkey.get(key, 0) for monkey in monkeys) for key in uniq)


def main():
    data = [x for x in aocd.get_data(day=22, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
