import collections

import math


import aocd
import z3

import utils
import string


def button_output(buttons, l):
    c = collections.defaultdict(int)
    for button in buttons:
        for b in button:
            c[b] += 1
    return tuple(c[i] % 2 for i in range(l))


def part_1(data):
    total = 0
    for machine in data:
        config, *buttons, _jolts = machine.split(" ")
        config = tuple(1 if i == "#" else 0 for i in config[1:-1])
        buttons = [tuple(utils.ints(x)) for x in buttons]
        mn = math.inf
        for i in range(2 ** len(buttons)):
            presses = [button for idx, button in enumerate(buttons) if i & (1 << idx)]
            op = button_output(presses, len(config))
            if config == op:
                mn = min(mn, len(presses))
        total += mn
    return total


def part_2(data):
    total = 0
    for machine in data:
        _config, *buttons, jolts = machine.split(" ")
        jolts = tuple(utils.ints(jolts))
        buttons = tuple(tuple(utils.ints(x)) for x in buttons)
        opt = z3.Optimize()
        variables = [z3.Int(x) for x in string.ascii_lowercase[: len(buttons)]]
        opt.add(v >= 0 for v in variables)
        opt.add(
            jolt == sum(v for v, btns in zip(variables, buttons) if i in btns)
            for i, jolt in enumerate(jolts)
        )

        ans = z3.Int("ans")
        opt.add(ans == sum(variables))

        opt.minimize(ans)
        opt.check()
        total += opt.model()[ans].as_long()
    return total


def main():
    data = [x for x in aocd.get_data(day=10, year=2025).splitlines()]

    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()

    # do something with mods counting up
