import heapq
import itertools

import aocd


def dijkstra_algorithm(nodes, start_node, finish_node, minimum=1, maximum=3):
    distances = {}
    seen = {}

    counter = itertools.count()
    heap = []

    seen[start_node] = 0
    heapq.heappush(heap, (0, next(counter), start_node, ""))
    while heap:
        distance, _, next_node, direction = heapq.heappop(heap)
        if (next_node, direction) in distances:
            continue
        distances[(next_node, direction)] = distance
        if next_node == finish_node:
            return distance

        options = []
        x, y = next_node
        for i in range(minimum, maximum + 1):
            if direction not in ("W", "E"):
                options.append(
                    ((x + i, y), "E", sum(nodes.get((x + j, y), 0) for j in range(1, i + 1)))
                )
                options.append(
                    ((x - i, y), "W", sum(nodes.get((x - j, y), 0) for j in range(1, i + 1)))
                )
            if direction not in ("S", "N"):
                options.append(
                    ((x, y + i), "S", sum(nodes.get((x, y + j), 0) for j in range(1, i + 1)))
                )
                options.append(
                    ((x, y - i), "N", sum(nodes.get((x, y - j), 0) for j in range(1, i + 1)))
                )
        for option, new_dir, cost in options:
            if option not in nodes:
                continue

            next_distance = distances[(next_node, direction)] + cost
            if (
                (option, new_dir) not in distances
                and (option, new_dir) not in seen
                or next_distance < seen[(option, new_dir)]
            ):
                seen[(option, new_dir)] = next_distance
                heapq.heappush(heap, (next_distance, next(counter), option, new_dir))


def part_1(data):
    grid = {}
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = int(c)
    d = dijkstra_algorithm(grid, (0, 0), (x, y), minimum=1, maximum=3)
    return d


def part_2(data):
    grid = {}
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = int(c)
    d = dijkstra_algorithm(grid, (0, 0), (x, y), minimum=4, maximum=10)
    return d


def main():
    data = [x for x in aocd.get_data(day=17, year=2023).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
