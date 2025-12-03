import aocd


def part_1(data):
    total = 0
    for line in data:
        line = [int(x) for x in line]
        s, e = 0, len(line) - 1
        for i in range(len(line) - 1):
            if line[i] > line[s]:
                s = i
        for i in range(s + 1, len(line)):
            if line[i] > line[e]:
                e = i
        total += int(f"{line[s]}{line[e]}")
    return total


def part_2(data):
    total = 0
    num_batteries = 12
    for line in data:
        line = [int(x) for x in line]
        batteries = [-1] + [x for x in range(len(line) - num_batteries, len(line))]

        for b in range(1, len(batteries)):
            for i in range(batteries[b - 1] + 1, len(line) - num_batteries + b):
                if line[i] > line[batteries[b]] or (
                    line[i] == line[batteries[b]] and i < batteries[b]
                ):
                    batteries[b] = i

        total += int("".join(str(line[b]) for b in batteries[1:]))
    return total


def main():
    data = [x for x in aocd.get_data(day=3, year=2025).splitlines()]
    # data=sample.splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
