import heapq
import itertools
import math
import aocd
import utils


def part_1(data):
    unconnected = []
    circuits = {}
    junction_map = {}
    for i, line in enumerate(data):
        x, y, z = utils.ints(line)
        q = (x, y, z)
        unconnected.append(q)
        circuits[i] = {q}
        junction_map[q] = i

    queue = []
    heapq.heapify(queue)
    for a, b in itertools.combinations(unconnected, 2):
        heapq.heappush(queue, (math.dist(a, b), a, b))

    for _ in range(1000):
        _, q, p = heapq.heappop(queue)
        oc = junction_map[p]
        nc = junction_map[q]
        if oc == nc:
            continue
        for j in circuits[oc]:
            junction_map[j] = nc
        circuits[nc].update(circuits[oc])
        circuits.pop(oc)

    top = sorted(circuits.values(), key=lambda x: len(x), reverse=True)
    return len(top[0]) * len(top[1]) * len(top[2])


def part_2(data):
    unconnected = []
    circuits = {}
    junction_map = {}
    for i, line in enumerate(data):
        x, y, z = utils.ints(line)
        q = (x, y, z)
        unconnected.append(q)
        circuits[i] = {q}
        junction_map[q] = i

    queue = []
    heapq.heapify(queue)
    for a, b in itertools.combinations(unconnected, 2):
        heapq.heappush(queue, (math.dist(a, b), a, b))

    while queue:
        _, q, p = heapq.heappop(queue)
        oc = junction_map[p]
        nc = junction_map[q]
        if oc == nc:
            continue
        for j in circuits[oc]:
            junction_map[j] = nc
        circuits[nc].update(circuits[oc])
        circuits.pop(oc)
        if len(circuits) == 1:
            return q[0] * p[0]


def main():
    data = [x for x in aocd.get_data(day=8, year=2025).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
