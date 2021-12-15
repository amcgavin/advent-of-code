import heapq
import itertools

import aocd


class Node:
    def __init__(self, position, value):
        self.position = position
        self.value = value
        self.links = set()

    def __hash__(self):
        return hash((self.position, self.value))

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.position == other.position and self.value == other.value

    def __repr__(self):
        return str(self.position)


def dijkstra_algorithm(nodes, start_node, finish_node):
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
        if next_node == finish_node:
            break

        for option in nodes[next_node.position].links:
            next_distance = distances[next_node] + option.value
            if option not in distances and option not in seen or next_distance < seen[option]:
                seen[option] = next_distance
                heapq.heappush(heap, (next_distance, next(counter), option))

    return distances


def part_1(data):
    nodes = {}
    for y, line in enumerate(data):
        for x, col in enumerate(line):
            nodes[(x, y)] = Node((x, y), int(col))

    for (x, y) in nodes.keys():
        for point in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            other = nodes.get(point)
            if other is None:
                continue
            nodes[point].links.add(nodes[(x, y)])
            nodes[(x, y)].links.add(other)

    finish_node = nodes[max(position for position in nodes.keys())]
    costs = dijkstra_algorithm(nodes, nodes[(0, 0)], finish_node)
    return costs[finish_node]


def limit(v):
    if v == 9:
        return v
    return v % 9


def part_2(data):
    max_y = len(data)
    max_x = len(data[0])
    nodes = {}
    for y, line in enumerate(data):
        for x, col in enumerate(line):
            for x_increment in range(5):
                for y_increment in range(5):
                    nodes[(max_x * x_increment + x, max_y * y_increment + y)] = Node(
                        (max_x * x_increment + x, max_y * y_increment + y),
                        limit(int(col) + y_increment + x_increment),
                    )

    for (x, y) in nodes.keys():
        for point in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            other = nodes.get(point)
            if other is None:
                continue
            nodes[point].links.add(nodes[(x, y)])
            nodes[(x, y)].links.add(other)

    finish_node = nodes[(max_x * 5 - 1, max_y * 5 - 1)]
    costs = dijkstra_algorithm(nodes, nodes[(0, 0)], finish_node)
    return costs[finish_node]


def main():
    data = aocd.get_data(day=15, year=2021).splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
