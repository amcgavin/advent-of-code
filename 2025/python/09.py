import itertools
import math

import aocd
import utils


def part_1(data):
    return max(
        (abs(p1[0] - p2[0]) + 1) * (1 + abs(p1[1] - p2[1]))
        for p1, p2 in itertools.combinations([tuple(utils.ints(line)) for line in data], 2)
    )


def extract_lines(pairs):
    horiz = []
    vert = []

    for (x1, y1), (x2, y2) in pairs:
        if (x1, y1) == (x2, y2):
            continue
        if x1 == x2:
            vert.append((x1, *sorted((y1, y2))))
        else:
            horiz.append((y1, *sorted((x1, x2))))

    return set(horiz), set(vert)


def count_intersections(line, cross):
    y, xmin, xmax = line
    return sum(xmin < x < xmax and ymin < y < ymax for (x, ymin, ymax) in cross)


def part_2(data):
    # keywords: point in loop, polygon, geometry
    # future me will thank me
    tiles = [tuple(utils.ints(line)) for line in data]
    horiz, vert = extract_lines(itertools.pairwise(tiles + tiles[:1]))
    m = 0
    for p1, p2 in itertools.combinations(tiles, 2):
        x1, y1 = p1
        x2, y2 = p2

        h1, v1 = extract_lines(
            [
                [(x1, y1), (x2, y1)],  # top
                [(x1, y2), (x2, y2)],  # bottom
                [(x1, y1), (x1, y2)],  # left
                [(x2, y1), (x2, y2)],  # right
            ]
        )
        if not (h1 and v1):
            continue
        b = 0
        for line in h1:
            b += count_intersections(line, vert)
        for line in v1:
            b += count_intersections(line, horiz)
        if b > 0:
            continue

        sx1, sx2 = sorted((x1, x2))
        sy1, sy2 = sorted((y1, y2))
        lu = count_intersections((sx1 + 1, 0, sy1 + 1), horiz)
        ld = count_intersections((sx1 + 1, sy2 - 1, math.inf), horiz)
        ru = count_intersections((sx2 - 1, 0, sy1 + 1), horiz)
        rd = count_intersections((sx2 - 1, sy2 - 1, math.inf), horiz)

        ul = count_intersections((sy1 + 1, 0, sx1 + 1), vert)
        dl = count_intersections((sy1 + 1, sx2 - 1, math.inf), vert)
        ur = count_intersections((sy2 - 1, 0, sx1 + 1), vert)
        dr = count_intersections((sy2 - 1, sx2 - 1, math.inf), vert)

        if all(t % 2 == 1 for t in [lu, ld, ru, rd, ul, dl, ur, dr]):
            area = (abs(x1 - x2) + 1) * (1 + abs(y1 - y2))
            if area > m:
                m = area

    return m


def main():
    data = [x for x in aocd.get_data(day=9, year=2025).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
