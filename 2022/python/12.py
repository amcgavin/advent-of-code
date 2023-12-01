import dataclasses
import heapq
import itertools

import aocd


@dataclasses.dataclass
class Node:
    position: tuple[int, int]
    weight: int
    links: set["Node"] = dataclasses.field(default_factory=set)

    def __hash__(self):
        return hash((self.position, self.weight))


def dijkstra_algorithm(
    nodes: dict[tuple[int, int], "Node"],
    start_node: Node,
    finish_node: Node,
):
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
            next_distance = distances[next_node] + 1
            if option not in distances and option not in seen or next_distance < seen[option]:
                seen[option] = next_distance
                heapq.heappush(heap, (next_distance, next(counter), option))

    return distances


def part_1(data):
    nodes = {}
    start = None
    end = None
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            weight = ord(char) - 96
            if char == "S":
                start = (x, y)
                weight = 0
            if char == "E":
                end = (x, y)
                weight = 26
            nodes[(x, y)] = Node(position=(x, y), weight=weight)
    for (x, y), node in nodes.items():
        for pos in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
            if other := nodes.get(pos):
                if other.weight <= node.weight + 1:
                    node.links.add(other)
    r = dijkstra_algorithm(nodes, nodes[start], nodes[end])
    return r[nodes[end]]


def part_2(data):
    nodes = {}
    starts = []
    end = None
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            weight = ord(char) - 96
            if char == "S":
                starts.append((x, y))
                weight = 0
            if char == "E":
                end = (x, y)
                weight = 26
            if char == "a":
                starts.append((x, y))
            nodes[(x, y)] = Node(position=(x, y), weight=weight)
    for (x, y), node in nodes.items():
        for pos in [(x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)]:
            if other := nodes.get(pos):
                if other.weight <= node.weight + 1:
                    node.links.add(other)

    costs = [
        dijkstra_algorithm(nodes, nodes[start], nodes[end]).get(nodes[end]) for start in starts
    ]
    return min(c for c in costs if c)


def main():
    data = [x for x in aocd.get_data(day=12, year=2022).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
