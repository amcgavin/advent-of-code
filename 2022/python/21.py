import aocd


class Special:
    def __init__(self):
        self.ops = []

    def __add__(self, other):
        self.ops.append(("+", other))
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        self.ops.append(("-", other))
        return self

    def __rsub__(self, other):
        self.ops.append(("--", other))
        return self

    def __mul__(self, other):
        self.ops.append(("*", other))
        return self

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        self.ops.append(("/", other))
        return self

    def __rtruediv__(self, other):
        self.ops.append(("//", other))
        return self

    def __eq__(self, other):
        ans = other
        for op, val in reversed(self.ops):
            match op:
                case "+":
                    ans = ans - val
                case "-":
                    ans += val
                case "--":
                    ans = val - ans
                case "*":
                    ans = ans / val
                case "/":
                    ans = val * ans
                case "//":
                    ans = val * 1 / ans

        return ans


def part_1(data):
    known = {}
    while "root" not in known:
        for line in data:
            if line[:4] in known:
                continue
            match line.replace(":", "").split(" "):
                case [monkey, lhs, "+", rhs]:
                    if lhs in known and rhs in known:
                        known[monkey] = known[lhs] + known[rhs]
                case [monkey, lhs, "-", rhs]:
                    if lhs in known and rhs in known:
                        known[monkey] = known[lhs] - known[rhs]
                case [monkey, lhs, "/", rhs]:
                    if lhs in known and rhs in known:
                        known[monkey] = known[lhs] / known[rhs]
                case [monkey, lhs, "*", rhs]:
                    if lhs in known and rhs in known:
                        known[monkey] = known[lhs] * known[rhs]
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
                    known["humn"] = Special()
                case ["root", lhs, _, rhs]:
                    if lhs in known and rhs in known:
                        known["root"] = known[lhs] == known[rhs]
                case [monkey, lhs, "+", rhs]:
                    if lhs in known and rhs in known:
                        known[monkey] = known[lhs] + known[rhs]
                case [monkey, lhs, "-", rhs]:
                    if lhs in known and rhs in known:
                        known[monkey] = known[lhs] - known[rhs]
                case [monkey, lhs, "/", rhs]:
                    if lhs in known and rhs in known:
                        known[monkey] = known[lhs] / known[rhs]
                case [monkey, lhs, "*", rhs]:
                    if lhs in known and rhs in known:
                        known[monkey] = known[lhs] * known[rhs]

                case [monkey, value]:
                    known[monkey] = int(value)
    return int(known["root"])


def main():
    data = aocd.get_data(day=21, year=2022).splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
