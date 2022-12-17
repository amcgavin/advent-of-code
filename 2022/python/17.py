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
    height = 0
    deltas = []
    jets = repeats(data)
    tiles = set()

    for r in itertools.count():
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

        # 1695 - length of cycle
        # 2022 - no significance
        if len(deltas) > 5000 and deltas[-1695:] == deltas[2022 : 2022 + 1695]:
            main_deltas = deltas[-1695:]
            iterations = (1000000000000 - r) // 1695
            remainder = (1000000000000 - r) % 1695
            return height + sum(main_deltas) * iterations + sum(main_deltas[:remainder])

        delta = max(height, max(y + b + 1 for a, b in rock)) - height
        height += delta
        deltas.append(delta)


def main():
    data = aocd.get_data(day=17, year=2022)
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
