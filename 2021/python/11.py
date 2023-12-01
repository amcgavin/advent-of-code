import aocd


class Octopus:
    def __init__(self, power):
        self.power = power

    def increment(self) -> bool:
        if self.power < 10:
            self.power += 1
            if self.power == 10:
                return True
        return False

    def reset(self):
        if self.power == 10:
            self.power = 0
            return True
        return False

    def __repr__(self):
        return f"{self.power}"


def increment(x, y, grid):
    flashes = 0
    if (x, y) not in grid:
        return flashes
    if grid[(x, y)].increment():
        flashes += 1
        for x1, y1 in [
            (x - 1, y - 1),
            (x, y - 1),
            (x + 1, y - 1),
            (x - 1, y),
            (x + 1, y),
            (x - 1, y + 1),
            (x, y + 1),
            (x + 1, y + 1),
        ]:
            flashes += increment(x1, y1, grid)
    return flashes


def part_1(data):
    grid = {}
    for x, line in enumerate(data):
        for y, char in enumerate(line):
            grid[(x, y)] = Octopus(int(char))

    flashes = 0
    for _ in range(100):
        for octopus in grid.values():
            octopus.reset()
        for x, y in grid.keys():
            flashes += increment(x, y, grid)
    return flashes


def part_2(data):
    grid = {}
    for x, line in enumerate(data):
        for y, char in enumerate(line):
            grid[(x, y)] = Octopus(int(char))

    count = 0
    while True:
        all_flash = True
        for octopus in grid.values():
            all_flash = octopus.reset() and all_flash
        if all_flash:
            return count
        for x, y in grid.keys():
            increment(x, y, grid)
        count += 1


def main():
    data = aocd.get_data(day=11, year=2021).splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
