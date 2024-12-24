import dataclasses
import itertools
import operator

from collections import defaultdict

import aocd
import utils
from parse import parse


def part_1(data: utils.Input):
    registers = {}
    initial, instructions = utils.partition_sections(data)

    for i in initial:
        registers[i[:3]] = int(i[5:])
    while instructions:
        n = instructions.pop()
        lhs, op, rhs, res = parse("{} {} {} -> {}", n)
        if rhs not in registers:
            instructions.insert(0, n)
            continue
        if lhs not in registers:
            instructions.insert(0, n)
            continue
        if op == "AND":
            registers[res] = registers[lhs] & registers[rhs]
        elif op == "OR":
            registers[res] = registers[lhs] | registers[rhs]
        elif op == "XOR":
            registers[res] = registers[lhs] ^ registers[rhs]
    return int(
        "".join(str(v) for k, v in sorted(registers.items(), reverse=True) if k[0] == "z"), 2
    )


@dataclasses.dataclass(eq=True, frozen=True)
class Literal:
    label: str

    def compute(self, values):
        return values[self.label]

    def __and__(self, other):
        return Op.create(self, other, "&", operator.and_)

    def __or__(self, other):
        return Op.create(self, other, "|", operator.or_)

    def __xor__(self, other):
        return Op.create(self, other, "^", operator.xor)

    def __lt__(self, other):
        if isinstance(other, Literal):
            return self.label < other.label
        return True

    def __str__(self):
        return self.label

    def __repr__(self):
        return str(self)


@dataclasses.dataclass(eq=True, frozen=True)
class Op:
    expressions: tuple

    @classmethod
    def create(cls, lhs, rhs, opd, op):
        if lhs < rhs:
            return cls(((lhs, rhs, opd, op)))
        return cls(((rhs, lhs, opd, op)))

    def __and__(self, other):
        return Op.create(self, other, "&", operator.and_)

    def __or__(self, other):
        return Op.create(self, other, "|", operator.or_)

    def __xor__(self, other):
        return Op.create(self, other, "^", operator.xor)

    def __lt__(self, other):
        if isinstance(other, Literal):
            return False
        return self.expressions < other.expressions

    def __str__(self):
        lhs, rhs, op, _ = self.expressions
        return f"({lhs} {op} {rhs})"

    def __repr__(self):
        return str(self)

    def compute(self, values):
        lhs, rhs, _, op = self.expressions
        lhs = lhs.compute(values)
        rhs = rhs.compute(values)
        return op(lhs, rhs)


def run_simulation(gates, swaps):
    instructions = [*gates]

    for k, v in swaps.items():
        o = list(instructions[k])
        p = list(instructions[v])
        xx = o[-3:]
        o[-3:] = p[-3:]
        p[-3:] = xx
        instructions[k] = "".join(o)
        instructions[v] = "".join(p)

    cycle_detection = {}
    registers = {}
    dependencies = defaultdict(set)

    for i in range(45):
        registers[f"x{i:02d}"] = Literal(f"x{i:02d}")
        registers[f"y{i:02d}"] = Literal(f"y{i:02d}")

    while instructions:
        n = instructions.pop()
        if cycle_detection.get(n) == len(instructions):
            return registers, dependencies
        cycle_detection[n] = len(instructions)
        lhs, op, rhs, res = parse("{} {} {} -> {}", n)
        if rhs not in registers:
            instructions.insert(0, n)
            continue
        if lhs not in registers:
            instructions.insert(0, n)
            continue
        if op == "AND":
            registers[res] = registers[lhs] & registers[rhs]
        elif op == "OR":
            registers[res] = registers[lhs] | registers[rhs]
        elif op == "XOR":
            registers[res] = registers[lhs] ^ registers[rhs]
        dependencies[res].update({lhs, rhs, res}.union(dependencies[lhs]).union(dependencies[rhs]))

    return registers, dependencies


def carry_from(n):
    if n == 0:
        return Literal("x00") & Literal("y00")
    return (Literal(f"x{n:02d}") & Literal(f"y{n:02d}")) | (
        (Literal(f"x{n:02d}") ^ Literal(f"y{n:02d}")) & carry_from(n - 1)
    )


def adder(n):
    if n == 0:
        return Literal("x00") ^ Literal("y00")
    return (Literal(f"x{n:02d}") ^ Literal(f"y{n:02d}")) ^ carry_from(n - 1)


def part_2(data: utils.Input):
    initial, instructions = utils.partition_sections(data)
    outs = {instruction[-3:]: i for i, instruction in enumerate(instructions)}
    r_outs = {v: k for k, v in outs.items()}
    locked = set()

    permanent_swaps = {}

    while len(permanent_swaps) < 4:
        registers, deps = run_simulation(instructions, permanent_swaps)
        for i in range(45):
            g = f"z{i:02d}"
            reg = registers[g]
            if reg != adder(i):
                break
            locked.update(deps[g])

        for s1, s2 in itertools.product(
            [outs[d] for d in deps[g] if d in outs], range(len(instructions))
        ):
            if r_outs[s1] in locked:
                continue
            if r_outs[s2] in locked:
                continue
            if s2 == s1:
                continue

            r, d2 = run_simulation(instructions, {**permanent_swaps, s1: s2})
            if r.get(g) == adder(i):
                permanent_swaps[s1] = s2
                break

    return ",".join(
        sorted(
            itertools.chain.from_iterable(
                [r_outs[k], r_outs[v]] for k, v in permanent_swaps.items()
            )
        )
    )


def main():
    data = [x for x in aocd.get_data(day=24, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
