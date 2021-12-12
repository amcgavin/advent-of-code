import aocd

tags = {"(": ")", "[": "]", "{": "}", "<": ">"}


class IncompleteLine(Exception):
    def __init__(self, open_tags):
        self.open_tags = open_tags


class InvalidTag(Exception):
    def __init__(self, char):
        self.char = char


def parse_line(line):
    current_tags = []
    for char in line:
        if char in tags:
            current_tags.append(char)
        elif tags.get(current_tags[-1], "?") == char:
            current_tags.pop()
        else:
            raise InvalidTag(char)
    raise IncompleteLine(current_tags)


def part_1(data):
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    total = 0
    for line in data:
        try:
            parse_line(line)
        except InvalidTag as e:
            total += scores[e.char]
        except IncompleteLine:
            pass
    return total


def part_2(data):
    scores = {"(": 1, "[": 2, "{": 3, "<": 4}
    all_scores = []
    for line in data:
        try:
            parse_line(line)
        except InvalidTag:
            pass
        except IncompleteLine as e:
            total = 0
            for char in reversed(e.open_tags):
                total *= 5
                total += scores[char]
            all_scores.append(total)
    return sorted(all_scores)[len(all_scores) // 2]


def main():
    data = aocd.get_data(day=10, year=2021).splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
