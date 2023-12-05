import aocd
import re
import itertools
import multiprocessing


def chunk_iterable(iterable, size):
    fill_value = object()
    chunks = [iter(iterable)] * size
    for chunk in itertools.zip_longest(*chunks, fillvalue=fill_value):
        yield (i for i in chunk if i is not fill_value)


def part_1(data):
    seeds = [int(x) for x in re.findall(r"\d+", data[0])]
    maps = "\n".join(data[2:]).split("\n\n")
    transforms = []
    for m in maps:
        d = m.splitlines()
        transform = []
        for row in d[1:]:
            dest, source, r = [int(x) for x in re.findall(r"\d+", row)]
            transform.append((source, source + r, source - dest))
        transforms.append(sorted(transform))

    values = []
    for seed in seeds:
        for transform in transforms:
            diff = next((diff for start, end, diff in transform if start <= seed <= end), 0)
            seed -= diff
        values.append(seed)
    return min(values)


def part_2(data, increment=12, start=0):
    seeds = [int(x) for x in re.findall(r"\d+", data[0])]
    valid_range = []
    for chunk in chunk_iterable(seeds, 2):
        s, r = list(chunk)
        valid_range.append((s, s + r))
    valid_range = sorted(valid_range)

    maps = "\n".join(data[2:]).split("\n\n")
    transforms = []
    for m in maps:
        d = m.splitlines()
        transform = []
        for row in d[1:]:
            dest, source, r = [int(x) for x in re.findall(r"\d+", row)]
            transform.append((source, source + r, source - dest))
        transforms.append(sorted(transform))

    transforms = list(reversed(transforms))

    location = start
    new_seed = -1
    while not any(s <= new_seed < e for s, e in valid_range):
        location += increment
        new_seed = location
        for transform in transforms:
            diff = next(
                (diff for start, end, diff in transform if start <= new_seed + diff < end), 0
            )
            new_seed += diff

    return location


def main():
    data = [x for x in aocd.get_data(day=5, year=2023).splitlines()]
    print(part_1(data))
    increment = 12
    with multiprocessing.Pool(increment) as p:
        print(min((p.starmap(part_2, [(data, increment, i) for i in range(12)]))))


if __name__ == "__main__":
    main()
