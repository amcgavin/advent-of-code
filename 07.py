import re
from collections import defaultdict


def get_input():
    with open("./07.txt", mode="r") as fp:
        for line in fp.readlines():
            line = line.strip()
            if line:
                yield line


bag_re = re.compile(r"(?P<qty>\d+)?(?P<name>[a-z ]+) bags?")


def parse_rules(line):
    m = bag_re.match(line).groupdict(default="0")
    return int(m["qty"]), m["name"].strip()


def parse_bag(line):
    container, _, contents = line.partition(" contain ")
    bags = []
    _, container = parse_rules(container)
    for bag in contents.split(", "):
        qty, bag = parse_rules(bag)
        if bag == "no other":
            continue
        bags.append((qty, bag))
    return container, bags


def part1():
    parent_map = defaultdict(list)
    answer = set()

    for line in get_input():
        container, bags = parse_bag(line)
        for qty, bag in bags:
            parent_map[bag].append(container)

    def recursive_update(items):
        for item in items:
            yield item
            answer.update(recursive_update(parent_map[item]))

    answer.update(recursive_update(parent_map["shiny gold"]))
    return len(answer)


def part2():
    child_map = defaultdict(list)
    for line in get_input():
        container, bags = parse_bag(line)
        for qty, bag in bags:
            child_map[container].append((qty, bag))

    def recursive_find(parent_qty, items):
        num = 1
        for qty, bag in items:
            num += recursive_find(qty, child_map[bag])
        return num * parent_qty

    total = recursive_find(1, child_map["shiny gold"])
    return total - 1  # dont include the gold bag


if __name__ == "__main__":
    print(part1())
    print(part2())
