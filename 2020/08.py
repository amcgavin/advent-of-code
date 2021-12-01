import re
import dataclasses


def get_input():
    with open("./08.txt", mode="r") as fp:
        for line in fp.readlines():
            line = line.strip()
            if line:
                yield line


command_re = re.compile(r"(?P<cmd>nop|acc|jmp) (?P<value>(?:\+|-)\d+)")


def parse(line):
    match = command_re.match(line).groupdict()
    return match["cmd"], int(match["value"])


def execute(program, exit_on_loop=False):
    seen = set()
    acc = 0
    pointer = 0
    while True:
        if pointer >= len(program):
            return acc
        if pointer in seen:
            if not exit_on_loop:
                raise ValueError("loop detected")
            return acc
        seen.add(pointer)
        cmd, value = program[pointer]
        if cmd == "nop":
            pointer += 1
        if cmd == "acc":
            acc += value
            pointer += 1
        if cmd == "jmp":
            pointer += value


def part1():
    program = [parse(line) for line in get_input()]
    return execute(program, exit_on_loop=True)


@dataclasses.dataclass
class Node:
    def __init__(self, idx):
        self.idx = idx
        self.direct = []
        self.indirect = []


def switch(cmd, value):
    if cmd == "acc":
        return "acc", value
    if cmd == "nop":
        return "jmp", value
    return "nop", value


class AnswerFound(Exception):
    def __init__(self, answer):
        self.answer = answer


def part2():
    program = [parse(line) for line in get_input()]

    # allow for an ending node (if this is executed we're good!)
    graph = [Node(i) for i in range(len(program) + 1)]
    end = graph[-1]

    def limit(a):
        # anything that would execute after the `end`, we'll cap at the `end`.
        return min(a, len(graph))

    # build a reverse graph of nodes which can be accessed
    # - directly: no switching required
    # - indirectly: the jmp/nop must be switched
    for i, (cmd, value) in enumerate(program):
        if cmd == "acc":
            graph[limit(i + 1)].direct.append(graph[i])

        if cmd == "nop":
            graph[limit(i + 1)].direct.append(graph[i])
            graph[limit(i + value)].indirect.append(graph[i])

        if cmd == "jmp":
            graph[limit(i + 1)].indirect.append(graph[i])
            graph[limit(i + value)].direct.append(graph[i])

    def search(node, can_switch, switched_node):
        # now try and find a way back to the start.
        if node.idx == 0:
            raise AnswerFound(switched_node.idx)
        for n in node.direct:
            search(n, can_switch, switched_node)
        if can_switch:
            # if we've already switched we can't do it again
            for n in node.indirect:
                search(n, False, n)

    try:
        search(end, True, None)
        raise ValueError("No answer found")
    except AnswerFound as e:
        program[e.answer] = switch(*program[e.answer])

    return execute(program)


def part2_naive():
    # won't work as you increase the allowed number of switches
    program = [parse(line) for line in get_input()]
    for i in range(len(program) * 2):
        try:
            return execute(program, exit_on_loop=False)
        except ValueError:
            program[i // 2] = switch(*program[i // 2])


if __name__ == "__main__":
    print(part1())
    print(part2())
