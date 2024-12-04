import aocd
import utils


def part_1(data):
    total = 0
    grid = utils.as_grid(data)
    for (x, y), start in grid.items():
        if start != "X":
            continue
        for direction in utils.all_directions():
            if (
                "".join(grid.get(coord, "") for coord in utils.straight_line(x, y, direction, 3))
                == "MAS"
            ):
                total += 1

    return total


def part_2(data):
    grid = utils.as_grid(data)
    return len(
        list(
            utils.find_in_grid(
                grid,
                [
                    [
                        ("S", "", "S"),
                        ("", "A", ""),
                        ("M", "", "M"),
                    ],
                    [
                        ("M", "", "M"),
                        ("", "A", ""),
                        ("S", "", "S"),
                    ],
                    [
                        ("M", "", "S"),
                        ("", "A", ""),
                        ("M", "", "S"),
                    ],
                    [
                        ("S", "", "M"),
                        ("", "A", ""),
                        ("S", "", "M"),
                    ],
                ],
            )
        )
    )


def main():
    data = [x for x in aocd.get_data(day=4, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
