import itertools

import aocd


def chunk_iterable(iterable, size):
    fill_value = object()
    chunks = [iter(iterable)] * size
    for chunk in itertools.zip_longest(*chunks, fillvalue=fill_value):
        yield (i for i in chunk if i is not fill_value)


def part_1(data):
    return sum(
        (ord(next(iter(set(row[: len(row) // 2]).intersection(row[len(row) // 2 :])))) - 96) % 58
        for row in data
    )


def part_2(data):
    total = 0
    for chunk in chunk_iterable(data, 3):
        chunk = list(chunk)
        i = next(iter(set(chunk[0]).intersection(chunk[1]).intersection(chunk[2])))
        total += (ord(i) - 96) % 58
    return total


def main():
    data = [x for x in aocd.get_data(day=3, year=2022).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
