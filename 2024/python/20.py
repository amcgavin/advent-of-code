import aocd
import utils
import itertools

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
            if grid.get(option, "#") == "#":
                continue

            next_distance = distances[next_node] + 1

            if option not in distances and option not in seen or next_distance < seen[option]:
                seen[option] = next_distance
                heapq.heappush(heap, (next_distance, next(counter), option))

    return distances


def part_1(data: utils.Input):
    grid = {}
    for p, c in utils.as_grid(data):
        if c == "S":
            start = p
        if c == "E":
            end = p
        grid[p] = c

    a = dijkstra_algorithm(grid, start)
    total = 0
    for p, c in grid.items():
        if c != "#":
            continue

        grid2 = grid.copy()
        grid2[p] = "."

        b = dijkstra_algorithm(grid2, start)
        if b[end] and a[end] - b[end] >= 100:
            total += 1
    return total


def box_around(p, grid, max_d=2):
    seen = {p}
    aaa = max_d
    while aaa:
        aaa -= 1
        n = set()
        for p2 in seen:
            for p3 in utils.cardinal_neighbours(*p2):
                if p3 not in grid:
                    continue
                if p3 in seen:
                    continue
                n.add(p3)
                yield (p3, max_d - aaa)

        seen.update(n)


def part_2(data: utils.Input):
    grid = {}
    for p, c in utils.as_grid(data):
        if c == "S":
            start = p
        if c == "E":
            end = p
        grid[p] = c

    scores = {p: dijkstra_algorithm(grid, p) for p, c in grid.items() if c != "#"}
    base_score = scores[start][end]
    total = set()
    for p, c in grid.items():
        if c == "#":
            continue
        for p2, addition in box_around(p, grid, 20):
            if p2 not in grid:
                continue
            if not (p2 in scores and end in scores[p2]):
                continue
            if base_score - (scores[start][p] + scores[p2][end] + addition) >= 100:
                total.add((p, p2))
    return len(total)


def main():
    data = [x for x in aocd.get_data(day=20, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
