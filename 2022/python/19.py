import functools
import math
import multiprocessing
import operator
from collections import Counter

import aocd
from parse import parse


def types():
    # ore=0, clay=1, obsidian=2, geode=3
    yield from range(4)


@functools.lru_cache(maxsize=None)
def calculate_best(time, robots, inventory, bp, maximum_timer):
    if time > maximum_timer:
        return
    n_robots = Counter(robots)

    for robot in types():
        if time == 4 and robot == 0:
            assert True
        if not all(resource in n_robots for resource, cost in zip(types(), bp[robot]) if cost > 0):
            continue
        if robot != 3 and max(bp[resource][robot] for resource in types()) <= n_robots[robot]:
            continue

        if not all(inventory[resource] >= cost for resource, cost in zip(types(), bp[robot])):
            # can't afford it now, but can in future
            max_time = 0
            for resource, cost in zip(types(), bp[robot]):
                if inventory[resource] < cost:
                    max_time = max(
                        max_time,
                        1 + math.ceil((cost - inventory[resource]) / n_robots[resource]),
                    )
            if max_time + time > maximum_timer:
                continue
            yield (
                time + max_time,
                (*robots, robot),
                tuple(
                    inventory[resource] + max_time * n_robots.get(resource, 0) - bp[robot][resource]
                    for resource in types()
                ),
            )
            continue

        if time < maximum_timer:
            yield (
                time + 1,
                (*robots, robot),
                tuple(
                    inventory[resource] - cost + n_robots.get(resource, 0)
                    for resource, cost in zip(types(), bp[robot])
                ),
            )


def future_geodes(time, robots, inventory, maximum_timer):
    if 3 not in robots:
        return 0
    return inventory[3] + (maximum_timer + 1 - time) * sum(1 for r in robots if r == 3)


def theoretical_max(time, robots, inventory, maximum_timer):
    # can build a robot every minute
    # assume that we can build a geode every minute from now
    return future_geodes(time, robots, inventory, maximum_timer) + sum(range(maximum_timer - time))


def calculate(maximum_timer, args):
    bpid, bp = args
    # t=0, robots=[ore], inventory=0
    start_state = (1, (0,), (0, 0, 0, 0))
    queue = [start_state]
    max_geodes = 0

    while queue:
        current_state = queue.pop(0)
        for next_state in calculate_best(*current_state, bp, maximum_timer):

            if theoretical_max(*next_state, maximum_timer) < max_geodes:
                continue
            queue.append(next_state)
            max_geodes = max(
                max_geodes, future_geodes(*next_state, maximum_timer), next_state[2][3]
            )
    return max_geodes


def part_1(data):
    bps = []

    for line in data:
        bp, ore, clay, ob1, ob2, geo1, geo2 = parse(
            "Blueprint {:d}: Each ore robot costs {:d} ore. Each clay robot costs {:d} ore. "
            "Each obsidian robot costs {:d} ore and {:d} clay. Each geode robot costs {:d} ore and {:d} obsidian.",
            line,
        )
        bps.append(
            (
                bp,
                (
                    (ore, 0, 0, 0),
                    (clay, 0, 0, 0),
                    (ob1, ob2, 0, 0),
                    (geo1, 0, geo2, 0),
                ),
            )
        )
    p = multiprocessing.Pool(10)
    return sum(bp[0] * ans for bp, ans in zip(bps, p.map(functools.partial(calculate, 24), bps)))


def part_2(data):
    bps = []
    for line in data:
        bp, ore, clay, ob1, ob2, geo1, geo2 = parse(
            "Blueprint {:d}: Each ore robot costs {:d} ore. Each clay robot costs {:d} ore. "
            "Each obsidian robot costs {:d} ore and {:d} clay. Each geode robot costs {:d} ore and {:d} obsidian.",
            line,
        )
        bps.append(
            (
                bp,
                (
                    (ore, 0, 0, 0),
                    (clay, 0, 0, 0),
                    (ob1, ob2, 0, 0),
                    (geo1, 0, geo2, 0),
                ),
            )
        )
    bps = bps[:3]
    p = multiprocessing.Pool(10)
    return functools.reduce(operator.mul, p.map(functools.partial(calculate, 32), bps))


def main():
    data = aocd.get_data(day=19, year=2022).splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
