import dataclasses

import operator
from collections import defaultdict
from match import RegexMatch
import re
import aocd

import math


def lt(g, n):
    def f(d):
        return d[g] < n

    return f


def gt(g, n):
    def f(d):
        return d[g] > n

    return f


def part_1(data):
    rules = defaultdict(list)
    for i, line in enumerate(data):
        if line == "":
            break
        p = line.index("{")
        label = line[:p]
        rule = line[p + 1 : -1]
        for a in rule.split(","):
            match RegexMatch(a):
                case RegexMatch("A"):
                    rules[label].append((lambda d: True, True))
                case RegexMatch("R"):
                    rules[label].append((lambda d: True, False))
                case RegexMatch(r"(\w+)$", [g]):
                    rules[label].append((lambda d: True, g))
                case RegexMatch(r"(\w)<(\d+):A", [g, n]):
                    rules[label].append((lt(g, int(n)), True))
                case RegexMatch(r"(\w)>(\d+):A", [g, n]):
                    rules[label].append((gt(g, int(n)), True))
                case RegexMatch(r"(\w)<(\d+):R", [g, n]):
                    rules[label].append((lt(g, int(n)), False))
                case RegexMatch(r"(\w)>(\d+):R", [g, n]):
                    rules[label].append((gt(g, int(n)), False))
                case RegexMatch(r"(\w)<(\d+):(\w+)", [g, n, l]):
                    rules[label].append((lt(g, int(n)), l))
                case RegexMatch(r"(\w)>(\d+):(\w+)", [g, n, l]):
                    rules[label].append((gt(g, int(n)), l))
    total = 0
    for c in data[i + 1 :]:
        x, m, a, s = [int(x) for x in re.findall(r"\d+", c)]
        d = {"x": x, "m": m, "a": a, "s": s}
        unsolved = True
        start = "in"
        while unsolved:
            for t, h in rules[start]:
                if t(d):
                    if h is True:
                        total += x + m + a + s
                        unsolved = False
                    elif h is False:
                        unsolved = False
                    elif h:
                        start = h
                    break

    return total


def solve_for(target, rules):
    new_rules = []
    for label, ruleset in rules.items():
        for i, (key, op, n, accept) in enumerate(ruleset):
            if accept == target:
                rule = []
                rule.insert(0, (key, op, n, accept, False))
                for j in range(i - 1, -1, -1):
                    rule.insert(0, (*ruleset[j], True))
                new_rules.append((label, rule))
    return new_rules


@dataclasses.dataclass
class Range:
    start: int = 1
    end: int = 4000

    def __gt__(self, other):
        if other + 1 > self.end:
            assert False, "need to code it"
        return Range(max(other + 1, self.start), self.end)

    def __lt__(self, other):
        if other - 1 < self.start:
            assert False, "need to code it"
        return Range(self.start, min(other - 1, self.end))

    def __ge__(self, other):
        if other > self.end:
            assert False, "need to code it"
        return Range(max(other, self.start), self.end)

    def __le__(self, other):
        if other < self.start:
            assert False, "need to code it"
        return Range(self.start, min(other, self.end))

    def __len__(self):
        return self.end - self.start + 1


op_map = {
    ">": operator.gt,
    "<": operator.lt,
    "!<": operator.ge,
    "!>": operator.le,
}


def part_2(data):
    rules = defaultdict(list)
    for line in data:
        if line == "":
            break
        p = line.index("{")
        label = line[:p]
        rule = line[p + 1 : -1]
        for ex in rule.split(","):
            match RegexMatch(ex):
                case RegexMatch("A"):
                    rules[label].append((None, None, None, True))
                case RegexMatch("R"):
                    rules[label].append((None, None, None, False))
                case RegexMatch(r"(\w+)$", [key]):
                    rules[label].append((None, None, None, key))
                case RegexMatch(r"(\w)(<|>)(\d+):(\w+)", [key, op, n, expression]):
                    if expression == "A":
                        rules[label].append((key, op, n, True))
                    elif expression == "R":
                        rules[label].append((key, op, n, False))
                    else:
                        rules[label].append((key, op, n, expression))

    reverse_rules = solve_for(True, rules)

    finished_rules = []
    while reverse_rules:
        label, ruleset = reverse_rules.pop()
        if label == "in":
            finished_rules.append(ruleset)
            continue
        for new_label, new in solve_for(label, rules):
            reverse_rules.append((new_label, new + ruleset))

    answer = 0
    for expression in finished_rules:
        d = {"x": Range(), "m": Range(), "a": Range(), "s": Range()}
        for key, op, n, accept, inverse in expression:
            if key is None and accept is True and inverse:
                assert False, "need to code it"
            elif key is None and accept is False and not inverse:
                assert False, "need to code it"
            if key is None:
                continue
            oper = op_map[f"{'!' if inverse else ''}{op}"]
            d[key] = oper(d[key], int(n))
        answer += math.prod(len(x) for x in d.values())
    return answer


def main():
    data = [x for x in aocd.get_data(day=19, year=2023).splitlines()]

    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
