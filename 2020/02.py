import re


def get_input():
    with open("./02.txt", mode="r") as fp:
        yield from fp.readlines()


def part1():
    expr = re.compile(r"(?P<min>\d+)-(?P<max>\d+) (?P<letter>\w): (?P<password>\w+)")
    valid = 0
    for line in get_input():
        params = expr.match(line).groupdict()
        count = params["password"].count(params["letter"])
        if int(params["min"]) <= count <= int(params["max"]):
            valid += 1
    return valid


def part2():
    expr = re.compile(r"(?P<p1>\d+)-(?P<p2>\d+) (?P<letter>\w): (?P<password>\w+)")
    valid = 0
    for line in get_input():
        params = expr.match(line).groupdict()
        m1 = params["password"][int(params["p1"]) - 1] == params["letter"]
        m2 = params["password"][int(params["p2"]) - 1] == params["letter"]
        if m1 ^ m2:
            valid += 1
    return valid


if __name__ == "__main__":
    print(part1())
    print(part2())
