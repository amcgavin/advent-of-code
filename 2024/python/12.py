import functools
import itertools

import aocd
import utils


def perimeter(points: list[utils.Coord]) -> int:
    total = 0
    for point in points:
        total += sum(1 for p in utils.cardinal_neighbours(*point) if p not in points)
    return total


def add_point(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1]


def n_edges(points: list[utils.Coord]) -> int:
    min_x = min(x for x, _ in points)
    max_x = max(x for x, _ in points)
    min_y = min(y for _, y in points)
    max_y = max(y for _, y in points)

    total = 0
    for direction, down, up in [
        ("R", (0, 1), (0, -1)),
        ("D", (1, 0), (-1, 0)),
    ]:
        x, y = (min_x, min_y)
        while x <= max_x and y <= max_y:
            in_segment_down = False
            in_segment_up = False
            for p in [(x, y)] + utils.straight_line(
                x, y, direction, max(max_x - min_x, max_y - min_y)
            ):
                if p not in points:
                    if in_segment_down:
                        in_segment_down = False
                        total += 1
                    if in_segment_up:
                        in_segment_up = False
                        total += 1
                    continue

                if add_point(p, down) in points and in_segment_down:
                    in_segment_down = False
                    total += 1
                if add_point(p, up) in points and in_segment_up:
                    in_segment_up = False
                    total += 1
                if add_point(p, down) not in points:
                    in_segment_down = True
                if add_point(p, up) not in points:
                    in_segment_up = True
            if in_segment_down:
                total += 1
            if in_segment_up:
                total += 1

            x, y = add_point((x, y), down)
    return total


def part_1(data: utils.Input):
    plots = []
    seen = set()
    grid = {p: c for p, c in utils.as_grid(data)}

    for p, c in grid.items():
        if p in seen:
            continue
        options = list(utils.cardinal_neighbours(*p))
        plot = [p]
        seen.add(p)
        while options:
            op = options.pop()
            if op in seen:
                continue
            if grid.get(op) == c:
                seen.add(op)
                plot.append(op)
                options.extend(utils.cardinal_neighbours(*op))
        plots.append((c, plot))

    return sum(perimeter(plot) * len(plot) for _, plot in plots)


def part_2(data: utils.Input):
    plots = []
    seen = set()
    grid = {p: c for p, c in utils.as_grid(data)}

    for p, c in grid.items():
        if p in seen:
            continue
        options = list(utils.cardinal_neighbours(*p))
        plot = [p]
        seen.add(p)
        while options:
            op = options.pop()
            if op in seen:
                continue
            if grid.get(op) == c:
                seen.add(op)
                plot.append(op)
                options.extend(utils.cardinal_neighbours(*op))
        plots.append((c, plot))

    return sum(n_edges(plot) * len(plot) for _, plot in plots)


def main():
    data = [x for x in aocd.get_data(day=12, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
