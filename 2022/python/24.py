import dataclasses
import heapq
import itertools

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


def dijkstra_algorithm(occupied, start, bounds, target):
    def neighbours(t, x, y):
        nt = (t + 1) % len(occupied)
        for (a, b) in [
            (x + 1, y),
            (x - 1, y),
            (x, y - 1),
            (x, y + 1),
        ]:
            if a < 0 or b < 0:
                continue
            if a > bounds[0] or b > bounds[1]:
                continue
            if (a, b) in occupied[nt]:
                continue
            yield nt, a, b
        if (x, y) not in occupied[nt]:
            yield nt, x, y

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
            break

        for option in neighbours(*next_node):
            next_distance = distances[next_node] + 1
            if option not in distances and option not in seen or next_distance < seen[option]:
                seen[option] = next_distance
                heapq.heappush(heap, (next_distance, next(counter), option))

    return distances


def part_1(data):
    blizzards = []

    y_max = len(data) - 2
    x_max = len(data[0]) - 2
    mod = y_max * x_max

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
    for _ in range(0, mod):
        states.append(frozenset((b.x, b.y) for b in blizzards))
        blizzards = [b.move(x_max, y_max) for b in blizzards]

    paths = dijkstra_algorithm(states, (0, 0, -1), (x_max - 1, y_max - 1), (x_max - 1, y_max - 1))
    return min(v for (t, x, y), v in paths.items() if x == x_max - 1 and y == y_max - 1) + 1


def part_2(data):
    blizzards = []
    y_max = len(data) - 2
    x_max = len(data[0]) - 2
    mod = y_max * x_max
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
    for _ in range(0, mod):
        states.append(frozenset((b.x, b.y) for b in blizzards))
        blizzards = [b.move(x_max, y_max) for b in blizzards]

    paths = dijkstra_algorithm(states, (0, 0, -1), (x_max - 1, y_max - 1), (x_max - 1, y_max - 1))
    v, t, x, y = min(
        (v, t, x, y) for (t, x, y), v in paths.items() if x == x_max - 1 and y == y_max - 1
    )
    answer = v + 1
    back_paths = dijkstra_algorithm(states, (t + 1, x, y + 1), (x_max - 1, y_max - 1), (0, 0))
    v, t, x, y = min((v, t, x, y) for (t, x, y), v in back_paths.items() if x == 0 and y == 0)
    answer += v + 1
    paths = dijkstra_algorithm(
        states, (t + 1, 0, -1), (x_max - 1, y_max - 1), (x_max - 1, y_max - 1)
    )
    return (
        answer + min(v for (t, x, y), v in paths.items() if x == x_max - 1 and y == y_max - 1) + 1
    )


def main():
    data = aocd.get_data(day=24, year=2022).splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
