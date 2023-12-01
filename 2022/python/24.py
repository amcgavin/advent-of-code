import dataclasses
import heapq
import itertools
import math

import aocd


@dataclasses.dataclass
class Blizzard:
    x: int
    y: int
    dx: int
    dy: int

    def move(self, x_max, y_max):
        x = (self.x + self.dx) % x_max
        y = (self.y + self.dy) % y_max
        return Blizzard(x, y, self.dx, self.dy)


def build_states(data):
    blizzards = []
    y_max = len(data) - 2
    x_max = len(data[0]) - 2
    mod = math.lcm(y_max, x_max)

    for y, line in enumerate(data[1:-1]):
        for x, char in enumerate(line[1:-1]):
            match char:
                case ">":
                    blizzards.append(Blizzard(x, y, 1, 0))
                case "<":
                    blizzards.append(Blizzard(x, y, -1, 0))
                case "^":
                    blizzards.append(Blizzard(x, y, 0, -1))
                case "v":
                    blizzards.append(Blizzard(x, y, 0, 1))
    states = []
    for _ in range(mod):
        states.append(frozenset((b.x, b.y) for b in blizzards))
        blizzards = [b.move(x_max, y_max) for b in blizzards]
    return states


def dijkstra_algorithm(occupied, start, target):
    x_max = max(x for x, y in itertools.chain.from_iterable(occupied))
    y_max = max(y for x, y in itertools.chain.from_iterable(occupied))

    def neighbours(t, x, y):
        nt = (t + 1) % len(occupied)
        for a, b in [
            (x + 1, y),
            (x - 1, y),
            (x, y - 1),
            (x, y + 1),
        ]:
            if a < 0 or b < 0:
                continue
            if a > x_max or b > y_max:
                continue
            if (a, b) in occupied[nt]:
                continue
            yield nt, a, b
        if (x, y) not in occupied[nt]:
            yield nt, x, y
        if x == 0 and y == 0:
            yield nt, 0, y - 1
        if x == x_max and y == y_max:
            yield nt, x, y_max + 1

    distances = {}
    seen = {}

    counter = itertools.count()
    heap = []

    seen[start] = 0
    heapq.heappush(heap, (0, next(counter), start))
    while heap:
        distance, _, next_node = heapq.heappop(heap)
        if next_node in distances:
            continue

        distances[next_node] = distance
        if next_node[1:] == target:
            return distances[next_node]

        for option in neighbours(*next_node):
            next_distance = distances[next_node] + 1
            if option not in distances and option not in seen or next_distance < seen[option]:
                seen[option] = next_distance
                heapq.heappush(heap, (next_distance, next(counter), option))


def part_1(data):
    states = build_states(data)
    S = (0, 0, -1)
    E = (len(data[0]) - 3, len(data) - 2)
    return dijkstra_algorithm(states, S, E)


def part_2(data):
    states = build_states(data)
    S = (0, -1)
    E = (len(data[0]) - 3, len(data) - 2)
    t = 0
    for start, target in [(S, E), (E, S), (S, E)]:
        t += dijkstra_algorithm(states, (t, *start), target)
    return t


def main():
    data = aocd.get_data(day=24, year=2022).splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
