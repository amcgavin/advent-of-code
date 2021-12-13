import aocd


class Node:
    def __init__(self, identifier):
        self.identifier = identifier
        self.links = set()

    def __hash__(self):
        return hash(self.identifier)

    def __eq__(self, other):
        return self.identifier == other.identifier

    @property
    def look_back(self):
        return self.identifier.upper() == self.identifier

    def __repr__(self):
        return self.identifier


def visit_1(node, path):
    new_path = f"{path}-{node}"
    if node.identifier == "end":
        yield new_path
    for option in node.links:
        if option.look_back or str(option) not in new_path:
            yield from visit_1(option, new_path)


def visit_2(node, path, can_double=True):
    new_path = f"{path}-{node}"
    if node.identifier == "end":
        yield new_path
    for option in node.links:
        if option.look_back:
            yield from visit_2(option, new_path, can_double=can_double)
        elif str(option) not in new_path:
            yield from visit_2(option, new_path, can_double=can_double)
        elif str(option) not in ("start", "end") and can_double:
            yield from visit_2(option, new_path, can_double=False)


def part_1(data):
    nodes = {}
    for line in data:
        start, end = line.split("-")
        start = nodes.setdefault(start, Node(start))
        end = nodes.setdefault(end, Node(end))
        start.links.add(end)
        end.links.add(start)

    return len(list(visit_1(nodes["start"], "")))


def part_2(data):
    nodes = {}
    for line in data:
        start, end = line.split("-")
        start = nodes.setdefault(start, Node(start))
        end = nodes.setdefault(end, Node(end))
        start.links.add(end)
        end.links.add(start)

    return len(list(visit_2(nodes["start"], "", can_double=True)))


def main():
    data = aocd.get_data(day=12, year=2021).splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
