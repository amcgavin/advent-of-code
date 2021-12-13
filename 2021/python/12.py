import aocd


class Node:
    def __init__(self, identifier):
        self.identifier = identifier
        self.links = set()

    def __hash__(self):
        return hash(self.identifier)

    def __eq__(self, other):
        return self.identifier == other.identifier

    def __repr__(self):
        return self.identifier


def parse_nodes(data):
    nodes = {}
    for line in data:
        start, end = line.split("-")
        start = nodes.setdefault(start, Node(start))
        end = nodes.setdefault(end, Node(end))
        start.links.add(end)
        end.links.add(start)
    return nodes


def explore(node, path, can_double=False):
    new_path = f"{path}-{node}"
    if node.identifier == "end":
        yield new_path
    for option in node.links:
        if option.identifier.isupper():
            yield from explore(option, new_path, can_double=can_double)
        elif str(option) not in new_path:
            yield from explore(option, new_path, can_double=can_double)
        elif str(option) not in ("start", "end") and can_double:
            yield from explore(option, new_path, can_double=False)


def part_1(data):
    nodes = parse_nodes(data)
    return len(list(explore(nodes["start"], "", can_double=False)))


def part_2(data):
    nodes = parse_nodes(data)
    return len(list(explore(nodes["start"], "", can_double=True)))


def main():
    data = aocd.get_data(day=12, year=2021).splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
