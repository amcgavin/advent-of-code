import itertools


import aocd
import utils


def part_1(data: utils.Input):
    return sum(
        all(a + b <= 7 for a, b in zip(lock, key))
        for lock, key in itertools.product(
            *[
                list(group[1])
                for group in itertools.groupby(
                    sorted(
                        (
                            schema[0][0] == "#",
                            *(sum(1 for c in col if c == "#") for col in zip(*schema[::-1])),
                        )
                        for schema in utils.partition_sections(data)
                    ),
                    key=lambda x: x[0],
                )
            ]
        )
    )


def main():
    data = [x for x in aocd.get_data(day=25, year=2024).splitlines()]
    print(part_1(data))


if __name__ == "__main__":
    main()
