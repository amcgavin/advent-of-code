import functools
import math
import operator
from collections import defaultdict

import aocd
from match import RegexMatch


def parse_monkeys(data):
    monkey = {}
    monkeys = {}
    for line in data:
        match RegexMatch(line):
            case RegexMatch(r"Monkey (\d+):", [name]):
                monkey = {}
                monkeys[name] = monkey
            case RegexMatch(r"  Starting items: (.*)", [items]):
                monkey["items"] = [int(x) for x in items.split(", ")]
            case RegexMatch(r"  Operation: new = old \+ (\d+)", [num]):
                monkey["operator"] = functools.partial(operator.add, int(num))
            case RegexMatch(r"  Operation: new = old \* (\d+)", [num]):
                monkey["operator"] = functools.partial(operator.mul, int(num))
            case RegexMatch(r"  Operation: new = old \* old"):
                monkey["operator"] = lambda x: x * x
            case RegexMatch(r"  Test: divisible by (\w+)", [num]):
                monkey["test"] = int(num)
            case RegexMatch(r"    If true: throw to monkey (\d)", [name]):
                monkey[True] = name
            case RegexMatch(r"    If false: throw to monkey (\d)", [name]):
                monkey[False] = name
    return monkeys


def part_1(data):
    monkeys = parse_monkeys(data)
    counts = defaultdict(lambda: 0)
    for _ in range(20):
        for name, monkey in monkeys.items():
            counts[name] += len(monkey["items"])
            for old in monkey["items"]:
                new = monkey["operator"](old) // 3
                monkeys[monkey[new % monkey["test"] == 0]]["items"].append(new)

            monkey["items"] = []

    return operator.mul(*sorted(counts.values())[-2:])


def part_2(data):
    monkeys = parse_monkeys(data)
    mod = math.lcm(*[monkey["test"] for monkey in monkeys.values()])
    counts = defaultdict(lambda: 0)
    for _ in range(10000):
        for name, monkey in monkeys.items():
            counts[name] += len(monkey["items"])
            for old in monkey["items"]:
                new = monkey["operator"](old) % mod
                monkeys[monkey[new % monkey["test"] == 0]]["items"].append(new)

            monkey["items"] = []

    return operator.mul(*sorted(counts.values())[-2:])


def main():
    data = [x for x in aocd.get_data(day=11, year=2022).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
