import aocd


def part_1(data):
    total = 0
    for line in data:
        game, game_data = line.split(": ")
        rounds = game_data.split("; ")
        mins = {"green": 0, "red": 0, "blue": 0}
        for r in rounds:
            for session in r.split(", "):
                num, colour = session.split(" ")
                num = int(num)
                mins[colour] = max(mins[colour], num)
        if mins["blue"] <= 14 and mins["green"] <= 13 and mins["red"] <= 12:
            total += int(game[5:])

    return total


def part_2(data):
    total = 0
    for line in data:
        game, game_data = line.split(": ")
        games = game_data.split("; ")
        mins = {"green": 0, "red": 0, "blue": 0}
        for g in games:
            for session in g.split(", "):
                num, colour = session.split(" ")
                num = int(num)
                mins[colour] = max(mins[colour], num)
        total += mins["green"] * mins["red"] * mins["blue"]

    return total


def main():
    data = [x for x in aocd.get_data(day=2, year=2023).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
