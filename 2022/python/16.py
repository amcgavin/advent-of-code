import dataclasses
import functools
import heapq
import itertools
import math
import multiprocessing

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


def dijkstra_algorithm(nodes: dict[str, Valve], start_node: Valve):
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
    return compute_best(weights, valves, 30, [v for v in valves.values() if v.flow])


def compute_best(weights, valves, time, group):
    best_order = [valves["AA"]]
    base_timer = time
    answer = 0
    while sorted_valves := sorted(
        (v for v in group if v.flow and v not in best_order), reverse=True
    ):
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


def chunk_iterable(iterable, size):
    fill_value = object()
    chunks = [iter(iterable)] * size
    for chunk in itertools.zip_longest(*chunks, fillvalue=fill_value):
        yield (i for i in chunk if i is not fill_value)


def part_2(data):
    valves = {}
    for line in data:
        name, flow, _, __, ___, links = parse("Valve {} has flow rate={:d}; {} {} to {} {}", line)
        valves[name] = Valve(name, flow, set(links.split(", ")))

    weights = {valve: dijkstra_algorithm(valves, valve) for valve in valves.values()}

    flow_valves = {v for v in valves.values() if v.flow}

    best_answer = 0

    seen = set()
    total = math.comb(len(flow_valves), len(flow_valves) // 2)
    for i, chunk in enumerate(
        chunk_iterable(itertools.combinations(flow_valves, len(flow_valves) // 2), 10)
    ):
        if i % 10 == 0:
            print(f"iteration: {i}/{int(total/10)}")
        p = multiprocessing.Pool(10)
        problems = []
        for group in chunk:
            other = flow_valves - set(group)
            tasks = {
                "".join(sorted(v.name for v in group)),
                "".join(sorted(v.name for v in other)),
            }
            if seen.intersection(tasks):
                continue
            seen.update(tasks)
            problems.extend([group, other])
        answers = iter(p.map(functools.partial(compute_best, weights, valves, 26), problems))
        for me, elephant in zip(answers, answers):
            best_answer = max(best_answer, me + elephant)
    return best_answer


def main():
    data = [x for x in aocd.get_data(day=16, year=2022).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
