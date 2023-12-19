import aocd


def trapezoid_formula(points):
    return abs(sum(((y + y1) * (x - x1)) for (x, y), (x1, y1) in zip(points, points[1:]))) // 2


def part_1(data):
    x, y = 0, 0
    points = [(x, y)]
    t = 0
    for line in data:
        d, n, c = line.split(" ")
        n = int(n)
        if d == "R":
            x += n
        elif d == "L":
            x -= n
        elif d == "U":
            y -= n
        elif d == "D":
            y += n
        t += n
        points.append((x, y))

    return trapezoid_formula(points) + t // 2 + 1


def part_2(data):
    x, y = 0, 0
    points = [(x, y)]
    t = 0
    for line in data:
        _d, _n, c = line.split(" ")
        n = int(c[2:7], 16)
        d = c[7]
        n = int(n)
        if d == "0":  # R
            x += n
        elif d == "2":  # L
            x -= n
        elif d == "3":  # U
            y -= n
        elif d == "1":  # D
            y += n
        t += n
        points.append((x, y))

    return trapezoid_formula(points) + t // 2 + 1


def main():
    data = [x for x in aocd.get_data(day=18, year=2023).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
