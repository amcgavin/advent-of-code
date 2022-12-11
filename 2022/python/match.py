import re
from collections.abc import Sequence


class RegexMatch:
    class Check:
        def __init__(self, matcher, expression):
            self.matcher = matcher
            self.expression = expression

        def __eq__(self, other):
            if match := re.compile(other).match(self.expression):
                self.matcher.groups = match.groups()
                return True
            return False

    class Groups(Sequence):
        def __init__(self):
            self.groups = []

        def __getitem__(self, item):
            return self.groups[item]

        def __len__(self):
            return len(self.groups)

        def __iter__(self):
            return iter(self.groups)

    __match_args__ = ("pattern", "groups")

    def __init__(self, expression):
        self._pattern = self.Check(self, expression)
        self._groups = self.Groups()

    @property
    def pattern(self):
        return self._pattern

    @property
    def groups(self):
        return self._groups

    @groups.setter
    def groups(self, val):
        self._groups.groups = val


def main():
    match RegexMatch("hel3o world"):
        case RegexMatch(r"hel(\w)o w(\w)rld", [a, b, c]):
            # doesn't match because there's no 3rd group
            print(f"1st case, {a=}, {b=}, {c=}")
        case RegexMatch(r"hel(\w)o w(\w)rl(\w)", [a, b, c]):
            print(f"2nd case, {a=}, {b=}, {c=}")
        case _:
            print("no match")


if __name__ == "__main__":
    main()
