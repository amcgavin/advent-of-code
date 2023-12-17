import heapq
import itertools

import aocd


def dijkstra_algorithm(nodes, start_node, finish_node, minimum=1, maximum=3):
    distances = {}
    seen = {}

    counter = itertools.count()
    heap = []

    seen[start_node] = 0
    heapq.heappush(heap, (0, next(counter), start_node))
    while heap:
        distance, _, next_node = heapq.heappop(heap)
        if next_node in distances:
            continue
        distances[next_node] = distance
        if next_node[:2] == finish_node:
            return distance

        options = []
        x, y, direction = next_node
        for i in range(minimum, maximum + 1):
            if direction != "H":
                options.append(
                    ((x + i, y, "H"), sum(nodes.get((x + j, y), 0) for j in range(1, i + 1)))
                )
                options.append(
                    ((x - i, y, "H"), sum(nodes.get((x - j, y), 0) for j in range(1, i + 1)))
                )
            if direction != "V":
                options.append(
                    ((x, y + i, "V"), sum(nodes.get((x, y + j), 0) for j in range(1, i + 1)))
                )
                options.append(
                    ((x, y - i, "V"), sum(nodes.get((x, y - j), 0) for j in range(1, i + 1)))
                )
        for option, cost in options:
            if option[:2] not in nodes:
                continue

            next_distance = distances[next_node] + cost
            if option not in distances and option not in seen or next_distance < seen[option]:
                seen[option] = next_distance
                heapq.heappush(heap, (next_distance, next(counter), option))


def part_1(data):
    grid = {}
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = int(c)
    d = dijkstra_algorithm(grid, (0, 0, ""), (x, y), minimum=1, maximum=3)
    return d


def part_2(data):
    grid = {}
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = int(c)
    d = dijkstra_algorithm(grid, (0, 0, ""), (x, y), minimum=4, maximum=10)
    return d


def main():
    data = [x for x in aocd.get_data(day=17, year=2023).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
