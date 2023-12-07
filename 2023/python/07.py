import aocd
from collections import Counter


def part_1(data):
    ranks = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
    scores = []
    total = 0
    # fmt: off
    combos = {
        key: i
        for i, key in enumerate(
            [
                (1, 1, 1, 1, 1),
                (2, 1, 1, 1),
                (2, 2, 1,),
                (3, 1, 1),
                (3, 2),
                (4, 1),
                (5,),
            ],
            1,
        )
    }
    # fmt: on
    for line in data:
        cards, score = line.split()
        score = int(score)
        cards = list(cards)
        u = [int(ranks.get(x, x)) for x in cards]
        cards = Counter(u)
        common = tuple(sorted(cards.values(), reverse=True))
        rank = combos[common]
        scores.append((rank, u, score))
    for i, (a, p, s) in enumerate(sorted(scores), 1):
        total += i * s
    return total


def part_2(data):
    ranks = {"A": 14, "K": 13, "Q": 12, "J": 1, "T": 10}
    scores = []
    total = 0
    # fmt: off
    combos = {
        (0, 1, 1, 1, 1, 1): 1,
        (0, 2, 1, 1, 1): 2,
        (0, 2, 2, 1,): 3,
        (0, 3, 1, 1): 4,
        (0, 3, 2): 5,
        (0, 4, 1): 6,
        (0, 5,): 7,
        (1, 1, 1, 1, 1): 2,
        (1, 2, 1, 1): 4,
        (1, 2, 2, ): 5,
        (1, 3, 1,): 6,
        (1, 4): 7,
        (2, 1, 1, 1): 4,
        (2, 2, 1,): 6,
        (2, 3,): 7,
        (3, 1, 1,): 6,
        (3, 2,): 7,
        (4, 1,): 7,
        (5,): 7,
    }
    # fmt: on
    for line in data:
        cards, score = line.split()
        score = int(score)
        cards = list(cards)
        u = [ranks.get(x, int(x if x not in ranks else 0)) for x in cards]
        cards = Counter(u)
        jokers = cards.pop(1, 0)
        common = (jokers,) + tuple(sorted(cards.values(), reverse=True))
        rank = combos[common]
        scores.append((rank, u, score))
    for i, (a, p, s) in enumerate(sorted(scores), 1):
        total += i * s
    return total


def main():
    data = [x for x in aocd.get_data(day=7, year=2023).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
