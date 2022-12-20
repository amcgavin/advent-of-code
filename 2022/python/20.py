import dataclasses

import aocd


def part_1(data):
    f = [int(x) for x in data]

    minimum = 0
    while minimum < len(f):
        d = f.pop(minimum)
        if isinstance(d, str):
            f.insert(minimum, d)
            minimum += 1
            continue
        if minimum + d == 0:
            f.append(f"{d}")
        elif minimum + d < 0:
            f.insert((minimum + d) % (len(f)), f"{d}")
        else:
            f.insert((minimum + d) % (len(f)), f"{d}")

    zero = f.index("0")
    return (
        int(f[(zero + 1000) % len(f)])
        + int(f[(zero + 2000) % len(f)])
        + int(f[(zero + 3000) % len(f)])
    )


@dataclasses.dataclass
class UniqueInt:
    value: int
    idx: int

    def __hash__(self):
        return hash(self.idx)

    def __radd__(self, other):
        return other + self.value

    def __eq__(self, other):
        if other == 0:
            return other == self.value
        return self.idx == other


def part_2(data):
    f = [UniqueInt(811589153 * int(x), i) for i, x in enumerate(data, 1)]
    zero = None
    for _ in range(10):
        for i in range(1, len(f) + 1):
            idx = f.index(i)
            d = f.pop(idx)
            if d.value == 0:
                zero = d
            new = (idx + d) % len(f)
            if d == 0 and new == 0:
                f.insert(0, d)
            elif new == 0:
                f.append(d)
            else:
                f.insert(new, d)

    zero = f.index(zero.idx)
    return (
        f[(zero + 1000) % len(f)].value
        + f[(zero + 2000) % len(f)].value
        + f[(zero + 3000) % len(f)].value
    )


def main():
    data = aocd.get_data(day=20, year=2022).splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
