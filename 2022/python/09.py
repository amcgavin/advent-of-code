import aocd


def part_1(data):
    visited = {(0, 0)}
    position = (0, 0)
    previous_tail = (0, 0)
    for line in data:
        direction, count = line.split(" ")
        for _step in range(int(count)):
            previous = position
            if direction == "R":
                position = (position[0] + 1, position[1])
            if direction == "L":
                position = (position[0] - 1, position[1])
            if direction == "U":
                position = (position[0], position[1] + 1)
            if direction == "D":
                position = (position[0], position[1] - 1)
            if any(abs(a[0] - a[1]) > 1 for a in zip(previous_tail, position)):
                previous_tail = previous
                visited.add(previous_tail)

    return len(visited)


def part_2(data):
    visited = {(0, 0)}
    q = [(0, 0) for _ in range(10)]

    for line in data:
        direction, count = line.split(" ")
        for _step in range(int(count)):
            position = q[0]
            if direction == "R":
                q[0] = (position[0] + 1, position[1])
            if direction == "L":
                q[0] = (position[0] - 1, position[1])
            if direction == "U":
                q[0] = (position[0], position[1] + 1)
            if direction == "D":
                q[0] = (position[0], position[1] - 1)
            for knot in range(1, len(q)):
                tail, head = q[knot], q[knot - 1]
                if any(abs(a[0] - a[1]) > 1 for a in zip(head, tail)):
                    x = (
                        (head[0] - tail[0]) // abs(head[0] - tail[0]) + tail[0]
                        if head[0] != tail[0]
                        else tail[0]
                    )
                    y = (
                        (head[1] - tail[1]) // abs(head[1] - tail[1]) + tail[1]
                        if head[1] != tail[1]
                        else tail[1]
                    )
                    q[knot] = (x, y)
            visited.add(q[-1])

    return len(visited)


sample = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""


def main():
    data = [x for x in aocd.get_data(day=9, year=2022).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
