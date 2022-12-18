import heapq
import itertools

import aocd
from parse import parse


def get_visible(cubes, limit):
    accessible = set()

    counter = itertools.count()
    heap = []
    start = (0, 0, 0)
    seen = {start}

    def neighbours(n):
        x, y, z = n
        for (dx, dy, dz) in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            if n in cubes:
                continue
            new = (x + dx, y + dy, z + dz)
            if not any(n < -1 or n > limit + 1 for n in new):
                yield new

    heapq.heappush(heap, (next(counter), start))
    while heap:
        _, next_node = heapq.heappop(heap)
        if next_node in accessible:
            continue
        accessible.add(next_node)
        for option in neighbours(next_node):
            if option not in accessible and option not in seen:
                seen.add(option)
                heapq.heappush(heap, (next(counter), option))

    return accessible


def part_1(data):
    answer = 0
    cubes = set()
    for (x, y, z) in (parse("{:d},{:d},{:d}", line) for line in data):
        cubes.add((x, y, z))

    for (x, y, z) in cubes:
        for (dx, dy, dz) in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            if (x + dx, y + dy, z + dz) not in cubes:
                answer += 1

    return answer


def part_2(data):
    cubes = set()
    for (x, y, z) in (parse("{:d},{:d},{:d}", line) for line in data):
        cubes.add((x, y, z))

    visible = get_visible(cubes, max(itertools.chain.from_iterable(cubes)))

    answer = 0
    for (x, y, z) in cubes:
        for (dx, dy, dz) in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            new = (x + dx, y + dy, z + dz)
            if new not in cubes and new in visible:
                answer += 1

    return answer


def main():
    data = aocd.get_data(day=18, year=2022).splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
