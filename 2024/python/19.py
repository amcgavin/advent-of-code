import functools
import aocd
import utils


@functools.cache
def can_match(patterns, design):
    if not design:
        return 1

    return sum(
        can_match(patterns, design[i:]) for i in range(1, len(design) + 1) if design[:i] in patterns
    )


def part_1(data: utils.Input):
    patterns, designs = utils.partition_sections(data)
    patterns = frozenset(utils.words(patterns[0]))
    return sum(1 for design in designs if can_match(patterns, design))


def part_2(data: utils.Input):
    patterns, designs = utils.partition_sections(data)
    patterns = frozenset(utils.words(patterns[0]))
    return sum(can_match(patterns, design) for design in designs)


def main():
    data = [x for x in aocd.get_data(day=19, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
