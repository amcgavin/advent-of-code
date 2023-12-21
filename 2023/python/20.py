import itertools
import math
from collections import defaultdict, deque
import aocd


def receive_input(status, to_module, state, last_sent):
    new_signals = []
    next_state = state
    next_last_sent = last_sent
    for module, typ, connects, s in state:
        if module != to_module:
            continue
        if typ == "broadcaster":
            next_last_sent = tuple(
                (key, value if key != to_module else status) for key, value in last_sent
            )
            for output in connects:
                new_signals.append((output, status))
        if typ == "%":
            if status:
                continue
            next_last_sent = tuple(
                (key, value if key != to_module else not s) for key, value in last_sent
            )
            for output in connects:
                new_signals.append((output, not s))
            next_state = tuple(
                (item if item[0] != to_module else (module, typ, connects, not s)) for item in state
            )
        if typ == "&":
            senders = {m for m, _, cc, _ in state if module in cc}
            if all(value for key, value in last_sent if key in senders):
                next_last_sent = tuple(
                    (key, value if key != to_module else False) for key, value in last_sent
                )
                for output in connects:
                    new_signals.append((output, False))
            else:
                next_last_sent = tuple(
                    (key, value if key != to_module else True) for key, value in last_sent
                )
                for output in connects:
                    new_signals.append((output, True))
        break
    return new_signals, next_state, next_last_sent


def part_1(data):
    state = ()
    last_sent = ()
    for line in data:
        lhs, rhs = line.split(" -> ")
        if lhs == "broadcaster":
            state = (*state, (lhs, lhs, tuple(rhs.split(", ")), False))
            last_sent = (*last_sent, (lhs, False))
        else:
            state = (*state, (lhs[1:], lhs[0], tuple(rhs.split(", ")), False))
            last_sent = (*last_sent, (lhs[1:], False))

    result = {True: 0, False: 0}
    q = deque([])
    for _ in range(1000):
        result[False] += 1
        q.append(("broadcaster", False))
        while q:
            sender, status = q.popleft()
            pulses, state, last_sent = receive_input(status, sender, state, last_sent)
            for output, status in pulses:
                q.append((output, status))
                result[status] += 1

    return math.prod(result.values())


def part_2(data):
    state = ()
    last_sent = ()
    for line in data:
        lhs, rhs = line.split(" -> ")
        if lhs == "broadcaster":
            state = (*state, (lhs, lhs, tuple(rhs.split(", ")), False))
            last_sent = (*last_sent, (lhs, False))
        else:
            state = (*state, (lhs[1:], lhs[0], tuple(rhs.split(", ")), False))
            last_sent = (*last_sent, (lhs[1:], False))

    dependents = defaultdict(list)
    searching = ["rx"]
    while "broadcaster" not in searching:
        ns = []
        for module, typ, connects, s in state:
            for b in searching:
                if b in connects:
                    dependents[b].append(module)
                    ns.append(module)
        searching = ns

    cycle_times = {}
    q = deque([])
    for i in itertools.count(1):
        q.append(("broadcaster", False))
        while q:
            sender, status = q.popleft()
            pulses, state, last_sent = receive_input(status, sender, state, last_sent)
            for output, status in pulses:
                if (
                    status
                    and sender not in cycle_times
                    and sender in dependents[dependents["rx"][0]]
                ):
                    cycle_times[sender] = i
                q.append((output, status))

            if all(dp in cycle_times for dp in dependents[dependents["rx"][0]]):
                return math.lcm(*cycle_times.values())


def main():
    data = [x for x in aocd.get_data(day=20, year=2023).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
