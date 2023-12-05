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
    paths = []
    for i, m in enumerate(maps, 1):
        d = m.splitlines()
        path = []
        for row in d[1:]:
            dest, source, r = [int(x) for x in re.findall(r"\d+", row)]
            diff = source - dest
            path.append((source, source + r, diff))
        paths.append(sorted(path))

    values = []
    for seed in seeds:
        for path in paths:
            for start, end, diff in path:
                if start <= seed <= end:
                    seed -= diff
                    break
        values.append(seed)
    return min(values)


def part_2(data, start=0):
    seeds = [int(x) for x in re.findall(r"\d+", data[0])]
    valid_range = []
    for chunk in chunk_iterable(seeds, 2):
        s, r = list(chunk)
        valid_range.append((s, s + r))
    valid_range = sorted(valid_range)

    maps = "\n".join(data[2:]).split("\n\n")
    paths = []
    for i, m in enumerate(maps, 1):
        d = m.splitlines()
        path = []
        for row in d[1:]:
            dest, source, r = [int(x) for x in re.findall(r"\d+", row)]
            diff = source - dest
            path.append((source, source + r, diff))
        paths.append(sorted(path))

    paths = list(reversed(paths))

    location = start
    new_seed = -1
    while not any(s <= new_seed < e for s, e in valid_range):
        location += 12
        new_seed = location
        for i, path in enumerate(paths):
            for start, end, diff in path:
                if start <= new_seed + diff < end:
                    new_seed += diff
                    break
    return location


def main():
    data = [x for x in aocd.get_data(day=5, year=2023).splitlines()]
    print(part_1(data))
    with multiprocessing.Pool(12) as p:
        print(min((p.starmap(part_2, [(data, i) for i in range(12)]))))


if __name__ == "__main__":
    main()
