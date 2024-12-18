import itertools

import aocd
import utils

import heapq


def dijkstra_algorithm(grid, start_node):
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
        for option in utils.cardinal_neighbours(*next_node):
            if grid.get(option, True):
                continue

            next_distance = distances[next_node] + 1

            if option not in distances and option not in seen or next_distance < seen[option]:
                seen[option] = next_distance
                heapq.heappush(heap, (next_distance, next(counter), option))

    return distances


def part_1(data: utils.Input):
    walls = {(x, y): False for x in range(71) for y in range(71)}
    for line in data[:1024]:
        x, y = utils.ints(line)
        walls[(x, y)] = True
    a = dijkstra_algorithm(walls, (0, 0))
    return a[(70, 70)]


def part_2(data: utils.Input):
    for i in range(len(data)):
        walls = {(x, y): False for x in range(71) for y in range(71)}
        for line in data[:i]:
            x, y = utils.ints(line)
            walls[(x, y)] = True
        a = dijkstra_algorithm(walls, (0, 0))
        if (70, 70) not in a:
            return data[i - 1]


def main():
    data = [x for x in aocd.get_data(day=18, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
