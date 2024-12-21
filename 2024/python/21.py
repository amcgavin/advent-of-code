import functools
import math

import aocd
import utils


keypad = {
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "0": (1, 3),
    "A": (2, 3),
}

arrows = {
    "U": (1, 0),
    "A": (2, 0),
    "L": (0, 1),
    "D": (1, 1),
    "R": (2, 1),
}


@functools.cache
def cost_to_press(btn, start, depth=2, is_keypad=False):
    if depth == 0:
        return 1

    if start == btn:
        return 1

    stack = [(start, (start,), "A", 0)]
    candidates = [math.inf]
    while stack:
        c, path, last_arrow, current_cost = stack.pop()
        for d in "LRUD":
            p1 = utils.directional_add(*c, d)
            if p1 in path:
                continue
            if is_keypad and p1 not in keypad.values():
                continue

            if not is_keypad and p1 not in arrows.values():
                continue

            new_cost = cost_to_press(arrows[d], arrows[last_arrow], depth - 1)

            if p1 == btn:
                candidates.append(
                    current_cost + new_cost + cost_to_press(arrows["A"], arrows[d], depth - 1)
                )
            else:
                stack.append((p1, (*path, p1), d, current_cost + new_cost))

    return min(candidates)


def part_1(data: utils.Input):
    total = 0

    for line in data:
        t = 0
        for c, p in zip(line, "A" + line[:3]):
            t += cost_to_press(keypad[c], keypad[p], depth=3, is_keypad=True)
        total += utils.ints(line)[0] * t
    return total


def part_2(data: utils.Input):
    total = 0

    for line in data:
        t = 0
        for c, p in zip(line, "A" + line[:3]):
            t += cost_to_press(keypad[c], keypad[p], depth=26, is_keypad=True)
        total += utils.ints(line)[0] * t
    return total


def main():
    data = [x for x in aocd.get_data(day=21, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
