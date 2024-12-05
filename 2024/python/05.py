import aocd
import utils
from collections import defaultdict


def check(r, priorities):
    for t, j in enumerate(r):
        if any(True for x in priorities[j] if x not in r[:t] and x in r):
            return False
    return True


def part_1(data: utils.Input):
    result = 0
    priorities = defaultdict(list)
    orders, pages = utils.partition_sections(data)

    for line in orders:
        s1, s2 = utils.ints(line)
        priorities[s2].append(s1)
    for line in pages:
        ints = utils.ints(line)
        if check(ints, priorities):
            result += ints[len(ints) // 2]

    return result


def remove_dupe(li):
    s = set()
    a = []
    for x in li:
        if x in s:
            continue
        s.add(x)
        a.append(x)
    return a


def sort(line, priorities):
    r = []
    for x in line:
        for dep in priorities[x]:
            if dep not in line:
                continue
            o = len(r)
            if x in r:
                o = r.index(x)
            r.insert(o, dep)
        r.append(x)
    return remove_dupe(r)


def part_2(data: utils.Input):
    result = 0
    priorities = defaultdict(list)
    orders, pages = utils.partition_sections(data)

    for line in orders:
        s1, s2 = utils.ints(line)
        priorities[s2].append(s1)

    for line in pages:
        ints = utils.ints(line)
        if not check(ints, priorities):
            r = sort(ints, priorities)
            while not check(r, priorities):
                r = sort(r, priorities)
            result += r[len(r) // 2]
    return result


def main():
    data = [x for x in aocd.get_data(day=5, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
