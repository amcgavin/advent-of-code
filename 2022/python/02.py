import aocd


def part_1(data):
    score = 0
    for game in data:
        p1, _, p2 = game.translate(
            "ABCXYZ".maketrans(dict(X="1", Y="2", Z="3", A="1", B="2", C="3"))
        ).partition(" ")
        p1 = int(p1)
        p2 = int(p2)
        score += p2
        result = (p2 - p1) % 3
        if result == 0:
            score += 3
        elif result == 2:
            score += 0
        elif result == 1:
            score += 6
    return score


def part_2(data):
    score = 0
    for game in data:
        p1, _, p2 = game.translate(
            "ABCXYZ".maketrans(dict(X="0", Y="1", Z="2", A="0", B="1", C="2"))
        ).partition(" ")
        p1 = int(p1)
        p2 = int(p2)
        if p2 == 0:
            score += (p1 - 1) % 3 + 1
        if p2 == 1:
            score += p1 + 4
        if p2 == 2:
            score += (p1 + 1) % 3 + 7
    return score


def main():
    data = [x for x in aocd.get_data(day=2, year=2022).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
