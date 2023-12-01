import dataclasses
import functools
import operator
import typing

import aocd


@dataclasses.dataclass
class Human:
    operations: tuple[typing.Callable[[int], int], ...] = tuple()

    def __add__(self, other):
        return Human((lambda x: x - other, *self.operations))

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return Human((lambda x: x + other, *self.operations))

    def __rsub__(self, other):
        return Human((lambda x: other - x, *self.operations))

    def __mul__(self, other):
        return Human((lambda x: x / other, *self.operations))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return Human((lambda x: x * other, *self.operations))

    def __rtruediv__(self, other):
        return Human((lambda x: other / x, *self.operations))

    def __eq__(self, other):
        return functools.reduce(lambda x, f: f(x), self.operations, other)


operators = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
}


def part_1(data):
    known = {}
    while "root" not in known:
        for line in data:
            if line[:4] in known:
                continue
            match line.replace(":", "").split(" "):
                case [monkey, lhs, op, rhs]:
                    if lhs in known and rhs in known:
                        known[monkey] = operators[op](known[lhs], known[rhs])
                case [monkey, value]:
                    known[monkey] = int(value)
    return int(known["root"])


def part_2(data):
    known = {}
    while "root" not in known:
        for line in data:
            if line[:4] in known:
                continue
            match line.replace(":", "").split(" "):
                case ["humn", *_]:
                    known["humn"] = Human()
                case ["root", lhs, _, rhs]:
                    if lhs in known and rhs in known:
                        known["root"] = known[lhs] == known[rhs]
                case [monkey, lhs, op, rhs]:
                    if lhs in known and rhs in known:
                        known[monkey] = operators[op](known[lhs], known[rhs])
                case [monkey, value]:
                    known[monkey] = int(value)
    return int(known["root"])


def main():
    data = aocd.get_data(day=21, year=2022).splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
