import aocd
import utils

import heapq
from parse import parse


def get_value(combo_operand, registers):
    if combo_operand <= 3:
        return combo_operand
    if combo_operand == 4:
        return registers["A"]
    if combo_operand == 5:
        return registers["B"]
    if combo_operand == 6:
        return registers["C"]
    raise ValueError("Invalid operand")


def part_1(data: utils.Input):
    r, p = list(utils.partition_sections(data))
    registers = {}
    for register in r:
        l, n = parse("Register {}: {:d}", register)
        registers[l] = int(n)
    program = utils.ints(p[0])
    ptr = 0

    output = []

    while ptr < len(program):
        opcode = program[ptr]
        instruction = program[ptr + 1]

        if opcode == 0:
            r = registers["A"] // (2 ** get_value(instruction, registers))
            registers["A"] = r
        if opcode == 1:
            registers["B"] ^= instruction
        if opcode == 2:
            registers["B"] = get_value(instruction, registers) % 8
        if opcode == 3:
            if registers["A"] != 0:
                ptr = instruction
                continue
        if opcode == 4:
            registers["B"] ^= registers["C"]
        if opcode == 5:
            output.append(get_value(instruction, registers) % 8)
        if opcode == 6:
            registers["B"] = registers["A"] // (2 ** get_value(instruction, registers))
        if opcode == 7:
            registers["C"] = registers["A"] // (2 ** get_value(instruction, registers))

        ptr += 2
    return ",".join(map(str, output))


def part_2(data: utils.Input, increment=12, start=0):
    r, p = list(utils.partition_sections(data))

    program = utils.ints(p[0])

    h = [
        (0, 0, "0000000000000000"),
        (0, 0, "1000000000000000"),
        (0, 0, "2000000000000000"),
        (0, 0, "3000000000000000"),
        (0, 0, "4000000000000000"),
        (0, 0, "5000000000000000"),
        (0, 0, "6000000000000000"),
        (0, 0, "7000000000000000"),
    ]

    while h:
        _, b, s = heapq.heappop(h)
        registers = {"A": int(s, 8), "B": 0, "C": 0}
        ptr = 0
        output = []
        while ptr < len(program):
            opcode = program[ptr]
            instruction = program[ptr + 1]

            if opcode == 0:
                r = registers["A"] // (2 ** get_value(instruction, registers))
                registers["A"] = r
            if opcode == 1:
                registers["B"] ^= instruction
            if opcode == 2:
                registers["B"] = get_value(instruction, registers) % 8
            if opcode == 3:
                if registers["A"] != 0:
                    ptr = instruction
                    continue
            if opcode == 4:
                registers["B"] ^= registers["C"]
            if opcode == 5:
                output.append(get_value(instruction, registers) % 8)
            if opcode == 6:
                registers["B"] = registers["A"] // (2 ** get_value(instruction, registers))
            if opcode == 7:
                registers["C"] = registers["A"] // (2 ** get_value(instruction, registers))

            ptr += 2
        if output == program:
            return int(s, 8)
        if len(output) > b and output[-(b + 1)] == program[-(b + 1)]:
            for i in range(8):
                new = s[: b + 1] + str(i) + s[b + 2 :]
                heapq.heappush(h, (-(b + 1), b + 1, new))


def main():
    data = [x for x in aocd.get_data(day=17, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
