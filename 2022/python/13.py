import functools
import itertools

import aocd


def coerce(v):
    if isinstance(v, list):
        return v
    return [v]


class InOrder(Exception):
    pass


class NotInOrder(Exception):
    pass


def recurse(p1, p2, step=1):
    for left, right in itertools.zip_longest(p1, p2, fillvalue=None):
        if left is None:
            raise InOrder()
        if right is None:
            raise NotInOrder()
        if isinstance(left, list) or isinstance(right, list):
            recurse(coerce(left), coerce(right), step)
            continue
        if left < right:
            raise InOrder()
        if left > right:
            raise NotInOrder()


def cmp(d1, d2):
    try:
        recurse(d1, d2)
        return -1
    except InOrder:
        return -1
    except NotInOrder:
        return 1


def part_1(data):
    pairs = []
    current = []
    for line in data:
        if line == "":
            pairs.append(current)
            current = []
        else:
            current.append(eval(line))
    pairs.append(current)

    total = 0
    totals = []
    for i, (d1, d2) in enumerate(pairs, 1):
        try:
            recurse(d1, d2, step=i)
            totals.append(i)
            total += i
        except InOrder:
            totals.append(i)
            total += i
        except NotInOrder:
            pass

    return total


def part_2(data):
    pairs = [[2], [6]]
    for line in data:
        if line == "":
            continue
        pairs.append(eval(line))

    pairs = sorted(pairs, key=functools.cmp_to_key(cmp))
    return (pairs.index([2]) + 1) * (pairs.index([6]) + 1)


def main():
    data = [x for x in aocd.get_data(day=13, year=2022).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
