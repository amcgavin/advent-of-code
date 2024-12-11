import functools

import aocd
import utils


@functools.cache
def transform_rock(rock: str, iterations: int):
    if iterations == 0:
        return 1
    if rock == "0":
        return transform_rock("1", iterations - 1)
    if len(rock) > 1 and len(rock) % 2 == 0:
        return transform_rock(str(int(rock[: len(rock) // 2])), iterations - 1) + transform_rock(
            str(int(rock[len(rock) // 2 :])), iterations - 1
        )
    return transform_rock(str(int(rock) * 2024), iterations - 1)


def part_1(data: utils.Input):
    rocks = data[0].split()
    return sum(transform_rock(rock, 25) for rock in rocks)


def part_2(data: utils.Input):
    rocks = data[0].split()
    return sum(transform_rock(rock, 75) for rock in rocks)


def main():
    data = [x for x in aocd.get_data(day=11, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
