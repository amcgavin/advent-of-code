import utils
import collections
import aocd


def part_1(data):
    *presents, trees = utils.partition_sections(data)
    psizes = [collections.Counter("".join(present)).get("#") for present in presents]
    total = 0
    for tree in trees:
        w, h, *p = utils.ints(tree)
        if w * h >= sum(s * c for s, c in zip(psizes, p)):
            total += 1
    return total


def main():
    data = [x for x in aocd.get_data(day=12, year=2025).splitlines()]
    print(part_1(data))


if __name__ == "__main__":
    main()
