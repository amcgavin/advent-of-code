import functools
import itertools
import json

import aocd


def coerce(v):
    if isinstance(v, list):
        return v
    return [v]


def recurse(p1, p2):
    for left, right in itertools.zip_longest(p1, p2, fillvalue=None):
        if left is None:
            raise StopIteration(True)
        if right is None:
            raise StopIteration(False)
        if isinstance(left, list) or isinstance(right, list):
            recurse(coerce(left), coerce(right))
            continue
        if left < right:
            raise StopIteration(True)
        if left > right:
            raise StopIteration(False)


def cmp(d1, d2):
    try:
        recurse(d1, d2)
        return -1
    except StopIteration as e:
        return -1 if e.value else 1


def part_1(data):
    return sum(
        i
        for i, pair in enumerate(zip(*([(json.loads(line) for line in data if line)] * 2)), 1)
        if cmp(*pair) < 0
    )


def part_2(data):
    items = [[], [2], [6]]
    items.extend(json.loads(line) for line in data if line)
    items = sorted(items, key=functools.cmp_to_key(cmp))
    return items.index([2]) * items.index([6])


def main():
    data = [x for x in aocd.get_data(day=13, year=2022).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
