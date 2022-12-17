import dataclasses
import heapq
import itertools
import typing

import aocd
from parse import parse


@dataclasses.dataclass
class Valve:
    name: str
    flow: int
    links: set

    def __hash__(self):
        return hash(self.name)

    def __lt__(self, other):
        return self.flow < other.flow

    def __gt__(self, other):
        return self.flow > other.flow


def dijkstra_algorithm(nodes: typing.Dict[str, Valve], start_node: Valve):
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
        for name in nodes[next_node.name].links:
            option = nodes[name]
            next_distance = distances[next_node] + 1
            if option not in distances and option not in seen or next_distance < seen[option]:
                seen[option] = next_distance
                heapq.heappush(heap, (next_distance, next(counter), option))

    return distances


def part_1(data):
    valves = {}
    for line in data:
        name, flow, _, __, ___, links = parse("Valve {} has flow rate={:d}; {} {} to {} {}", line)
        valves[name] = Valve(name, flow, set(links.split(", ")))

    weights = {valve: dijkstra_algorithm(valves, valve) for valve in valves.values()}

    best_order = [valves["AA"]]
    base_timer = 30
    answer = 0

    while True:
        sorted_valves = sorted(
            (v for v in valves.values() if v.flow and v not in best_order), reverse=True
        )
        if not sorted_valves:
            break
        overall_best = None
        while sorted_valves:
            best = None
            for order in itertools.permutations(sorted_valves[:8]):
                timer = base_timer
                start = best_order[-1]
                flow = 0
                for target in order:
                    timer -= weights[start][target]
                    timer -= 1
                    flow += max(0, timer) * target.flow
                    start = target
                if best is None or (flow, order) > best:
                    best = (flow, order)

            if overall_best is None or best > overall_best:
                overall_best = best

            sorted_valves.remove(best[1][-1])

        top = overall_best[1][0]
        base_timer -= weights[best_order[-1]][top]
        base_timer -= 1
        answer += max(0, base_timer) * top.flow
        best_order.append(top)

    return answer


def part_2(data):
    return 0


sample = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""


def main():
    data = [x for x in aocd.get_data(day=16, year=2022).splitlines()]
    print(part_1(data))
    # print(part_2(data))
    # print(part_1(sample.splitlines()))


if __name__ == "__main__":
    main()
