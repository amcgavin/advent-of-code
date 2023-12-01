import dataclasses
import functools
import operator

import aocd
from parse import parse


@dataclasses.dataclass
class Range:
    minimum: int = 0
    maximum: int = 0

    def __add__(self, other):
        if other.minimum > self.maximum + 1:
            raise ValueError(other.minimum - 1)
        return Range(
            minimum=min(self.minimum, other.minimum),
            maximum=max(self.maximum, other.maximum),
        )

    def __gt__(self, other):
        return self.minimum > other.minimum

    def __lt__(self, other):
        return self.minimum < other.minimum

    def __len__(self):
        return self.maximum - self.minimum


def part_1(data):
    y = 2000000
    ranges = []
    for line in data:
        sx, sy, bx, by = parse(
            "Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}", line
        )
        d = abs(by - sy) + abs(bx - sx)
        if sy - d <= y <= sy + d:
            ranges.append(Range(sx - (d - abs(sy - y)), sx + d - abs(sy - y)))

    return len(functools.reduce(operator.add, sorted(ranges)))


def part_2(data):
    sensors = []
    for line in data:
        sx, sy, bx, by = parse(
            "Sensor at x={:d}, y={:d}: closest beacon is at x={:d}, y={:d}", line
        )
        sensors.append((sx, sy, abs(by - sy) + abs(bx - sx)))

    for y in range(4000000):
        lists = []
        for sx, sy, d in sensors:
            if sy - d <= y <= sy + d:
                lists.append(Range(sx - (d - abs(sy - y)), sx + d - abs(sy - y)))

        if not lists:
            continue
        try:
            functools.reduce(operator.add, sorted(lists))
        except ValueError as e:
            return e.args[0] * 4000000 + y


def main():
    data = [x for x in aocd.get_data(day=15, year=2022).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
