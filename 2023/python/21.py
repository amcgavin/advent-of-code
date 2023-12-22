import heapq
import itertools

import aocd


def immediate_neighbours(x, y):
    return {
        (x + 1, y),
        (x - 1, y),
        (x, y - 1),
        (x, y + 1),
    }


def dijkstra_algorithm(grid, start_node, max_distance=0, start_cost=0, repeat=0, distances=None):
    max_x = max(x for x, y in grid.keys()) + 1
    max_y = max(y for x, y in grid.keys()) + 1
    if distances is None:
        distances = {}
    seen = {}

    counter = itertools.count()
    heap = []

    seen[start_node] = 0
    heapq.heappush(heap, (start_cost, next(counter), start_node))
    while heap:
        distance, _, next_node = heapq.heappop(heap)
        if next_node in distances:
            continue
        distances[next_node] = distance
        for option in immediate_neighbours(*next_node):
            if repeat:
                x, y = option
                if not (-repeat < (x / max_x) < repeat + 1 and -repeat < (y / max_y) < repeat + 1):
                    continue
                if grid.get((x % max_x, y % max_y), "#") == "#":
                    continue
            elif grid.get(option, "#") == "#":
                continue

            next_distance = distances[next_node] + 1
            if max_distance and next_distance > max_distance:
                continue
            if option not in distances and option not in seen or next_distance < seen[option]:
                seen[option] = next_distance
                heapq.heappush(heap, (next_distance, next(counter), option))

    return distances


def part_1(data):
    grid = {}
    start = None
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = c
            if c == "S":
                start = (x, y)

    d = dijkstra_algorithm(grid, start, max_distance=64)
    return sum(1 for x in d.values() if x == 64 or x % 2 == 0)


def part_2(data):
    n = 26501365

    grid = {}
    start = None
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            grid[(x, y)] = c
            if c == "S":
                start = (x, y)
    d = dijkstra_algorithm(grid, start, repeat=0, max_distance=n)
    walls = set(grid.keys()) - set(d.keys())
    for x, y in walls:
        grid[(x, y)] = "#"
    max_x = max(x for x, y in grid.keys())
    evens = sum(1 for v in d.values() if v % 2 == sum(start) % 2)
    odds = sum(1 for v in d.values() if v % 2 != sum(start) % 2)

    total = 0
    x = n - start[0]
    x //= max_x + 1
    total += x**2 * odds
    total += (x - 1) ** 2 * evens

    middle = dijkstra_algorithm(grid, start, repeat=0, max_distance=65, start_cost=0)
    tl = dijkstra_algorithm(grid, (0, 0), repeat=0, max_distance=65, start_cost=0)
    bl = dijkstra_algorithm(grid, (0, max_x), repeat=0, max_distance=65, start_cost=0)
    tr = dijkstra_algorithm(grid, (max_x, 0), repeat=0, max_distance=65, start_cost=0)
    br = dijkstra_algorithm(grid, (max_x, max_x), repeat=0, max_distance=65, start_cost=0)

    me = sum(1 for x in middle.values() if x <= 65 and x % 2 == sum(start) % 2)
    tle = sum(1 for v in tl.values() if v <= 65 and v % 2 == sum(start) % 2)
    tlo = sum(1 for v in tl.values() if v <= 65 and v % 2 != sum(start) % 2)
    ble = sum(1 for v in bl.values() if v <= 65 and v % 2 == sum(start) % 2)
    blo = sum(1 for v in bl.values() if v <= 65 and v % 2 != sum(start) % 2)
    tre = sum(1 for v in tr.values() if v <= 65 and v % 2 == sum(start) % 2)
    tro = sum(1 for v in tr.values() if v <= 65 and v % 2 != sum(start) % 2)
    bre = sum(1 for v in br.values() if v <= 65 and v % 2 == sum(start) % 2)
    bro = sum(1 for v in br.values() if v <= 65 and v % 2 != sum(start) % 2)

    # end pieces
    tm = me + ble + bre
    lm = me + tre + bre
    rm = me + tle + ble
    bm = me + tle + tre
    total += tm + lm + rm + bm

    # edge
    tlb = me + tre + bre + ble
    blb = me + tle + tre + bre
    trb = me + tle + ble + bre
    brb = me + tle + tre + ble
    total += x * (tlb + blb + trb + brb)

    # inverse edge
    total += x * (tlo + blo + tro + bro)
    return total


sample = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""


def main():
    data = [x for x in aocd.get_data(day=21, year=2023).splitlines()]
    # data = sample.splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
