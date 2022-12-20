import multiprocessing
from collections import Counter, deque

import aocd
from parse import parse


def types():
    # ore=0, clay=1, obsidian=2, geode=3
    yield from range(4)


def calculate_best(time, robots, inventory, bp):
    if time > 24:
        return
    n_robots = Counter(robots)
    new_inventory = tuple(inventory[robot] + n_robots.get(robot, 0) for robot in types())
    for robot in types():
        if not all(resource in n_robots for resource, cost in zip(types(), bp[robot]) if cost > 0):
            continue

        if not all(inventory[resource] >= cost for resource, cost in zip(types(), bp[robot])):
            # can't afford it now, but can in future
            max_time = 0
            for resource, cost in zip(types(), bp[robot]):
                if inventory[resource] < cost:
                    max_time = max(
                        max_time,
                        1
                        + (cost - inventory[resource] + n_robots[resource] - 1)
                        // n_robots[resource],
                    )
            if max_time + time > 24:
                continue
            yield (
                time + max_time,
                tuple([*robots, robot]),
                tuple(
                    inventory[resource] + max_time * n_robots.get(resource, 0) - bp[robot][resource]
                    for resource in types()
                ),
            )
            continue

        yield (
            time + 1,
            tuple([*robots, robot]),
            tuple(new_inventory[resource] - cost for resource, cost in zip(types(), bp[robot])),
        )
    # yield (
    #    time + 1, robots, new_inventory
    # )


def future_geodes(time, robots, inventory):
    return inventory[3] + (23 - time) * sum(1 for r in robots if r == 3)


def maximum_geodes(time, robots, inventory):
    return future_geodes(time, robots, inventory) + (23 - time) * (22 - time) // 2


def calculate(args):
    bpid, bp = args
    # t=0, robots=[ore], inventory=0
    start_state = (0, (0,), (0, 0, 0, 0))
    queue = deque([start_state])
    max_geodes = 0
    seen = {start_state}

    while queue:
        for next_state in calculate_best(*queue.popleft(), bp):
            if next_state in seen:
                continue
            if maximum_geodes(*next_state) < max_geodes:
                continue
            queue.append(next_state)
            seen.add(next_state)
            max_geodes = max(max_geodes, future_geodes(*next_state), next_state[2][3])
    print(f"{bpid=} {max_geodes=}")
    return bpid * max_geodes


def part_1(data):
    bp1 = [(4, 0, 0, 0), (2, 0, 0, 0), (3, 14, 0, 0), (2, 0, 7, 0)]
    bp2 = [(2, 0, 0, 0), (3, 0, 0, 0), (3, 8, 0, 0), (3, 0, 12, 0)]
    bps = []

    for line in data:
        bp, ore, clay, ob1, ob2, geo1, geo2 = parse(
            "Blueprint {:d}: Each ore robot costs {:d} ore. Each clay robot costs {:d} ore. Each obsidian robot costs {:d} ore and {:d} clay. Each geode robot costs {:d} ore and {:d} obsidian.",
            line,
        )
        bps.append(
            (
                bp,
                [
                    (ore, 0, 0, 0),
                    (clay, 0, 0, 0),
                    (ob1, ob2, 0, 0),
                    (geo1, 0, geo2, 0),
                ],
            )
        )

    p = multiprocessing.Pool(10)
    return sum(p.map(calculate, bps))


def part_2(data):
    return 0


def main():
    data = aocd.get_data(day=19, year=2022).splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
