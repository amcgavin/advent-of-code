import itertools

import aocd

rock_patterns = [
    {(0, 0), (1, 0), (2, 0), (3, 0)},
    {(1, 2), (0, 1), (1, 1), (2, 1), (1, 0)},
    {(2, 2), (2, 1), (0, 0), (1, 0), (2, 0)},
    {(0, 3), (0, 2), (0, 1), (0, 0)},
    {(0, 1), (1, 1), (0, 0), (1, 0)},
]


def repeats(data):
    while True:
        for d in data:
            if d == ">":
                yield (1, 0)
            else:
                yield (-1, 0)


def collides(shape, position, tiles):
    c, d = position
    for a, b in shape:
        if (a + c, b + d) in tiles:
            return True
        if a + c < 0 or a + c >= 7:
            return True
        if b + d < 0:
            return True
    return False


def part_1(data):
    height = 0
    jets = repeats(data)
    tiles = set()

    for r in range(2022):
        rock = rock_patterns[r % len(rock_patterns)]
        x, y = 2, 3 + height
        for i in itertools.count():
            if i % 2 == 0:
                (dx, dy) = next(jets)
                if not collides(rock, (x + dx, y + dy), tiles):
                    x += dx
                    y += dy
            else:
                if not collides(rock, (x, y - 1), tiles):
                    y -= 1
                else:
                    break
        tiles.update(((a + x, b + y) for a, b in rock))
        height = max(height, max(y + b + 1 for a, b in rock))
    return height


def part_2(data):
    return 0


def main():
    data = aocd.get_data(day=17, year=2022)
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
