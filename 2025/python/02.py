import aocd


def part_1(data):
    lines = data[0].split(",")
    total = 0
    for line in lines:
        start, end = [int(x) for x in line.split("-")]
        for i in range(start, end + 1):
            s = f"{i}"
            if len(s) % 2 != 0:
                continue
            l = len(s) // 2
            if all(s[n] == s[n + l] for n in range(0, l)):
                total += i

    return total


def part_2(data):
    lines = data[0].split(",")
    total = 0
    for line in lines:
        start, end = [int(x) for x in line.split("-")]
        for i in range(start, end + 1):
            s = f"{i}"
            for chunks in range(len(s), 1, -1):
                if len(s) % chunks != 0:
                    continue
                l = len(s) // chunks
                if len({s[n * l : l * (n + 1)] for n in range(chunks)}) == 1:
                    total += i
                    break
    return total


def main():
    data = [x for x in aocd.get_data(day=2, year=2025).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
