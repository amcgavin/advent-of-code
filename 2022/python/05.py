import itertools
import re
from collections import defaultdict

import aocd

init_re = re.compile(r"( *\[\w] *)+")
stack_re = re.compile(r"\[(\w)]")
instruction_re = re.compile(r"move (\d+) from (\d+) to (\d+)")


def chunk_iterable(iterable, size):
    fill_value = object()
    chunks = [iter(iterable)] * size
    for chunk in itertools.zip_longest(*chunks, fillvalue=fill_value):
        yield (i for i in chunk if i is not fill_value)


def part_1(data):
    stacks = defaultdict(list)

    for row in data:
        if init_re.match(row):
            for i, spot in enumerate(chunk_iterable(row, 4), 1):
                m = stack_re.match("".join(spot))
                if m is None:
                    continue
                stacks[i].insert(0, m.groups()[0])
            continue

        m = instruction_re.match(row)
        if m:
            c, src, dst = (int(x) for x in m.groups())
            for _ in range(c):
                if stacks[src]:
                    stacks[dst].append(stacks[src].pop())
    return "".join([stacks[i][-1] for i in sorted(stacks.keys())])


def part_2(data):
    stacks = defaultdict(list)

    for row in data:
        if init_re.match(row):
            for i, spot in enumerate(chunk_iterable(row, 4), 1):
                m = stack_re.match("".join(spot))
                if m is None:
                    continue
                stacks[i].insert(0, m.groups()[0])
            continue

        m = instruction_re.match(row)
        if m:
            c, src, dst = (int(x) for x in m.groups())
            if stacks[src]:
                stacks[dst].extend(stacks[src][-c:])
                stacks[src] = stacks[src][:-c]
    return "".join([stacks[i][-1] for i in sorted(stacks.keys())])


def main():
    data = [x for x in aocd.get_data(day=5, year=2022).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
