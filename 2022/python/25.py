import math

import aocd


def part_1(data):
    answer = 0

    for line in data:
        for i, c in enumerate(line):
            match c:
                case "=":
                    answer -= 2 * math.pow(5, len(line) - i - 1)
                case "-":
                    answer -= math.pow(5, len(line) - i - 1)
                case "1":
                    answer += math.pow(5, len(line) - i - 1)
                case "2":
                    answer += 2 * math.pow(5, len(line) - i - 1)

    digits = []
    carry = 0
    while answer:
        digit = answer % 5 + carry
        if digit > 2:
            carry = 1
            digit -= 5
        else:
            carry = 0
        digits.append(int(digit))
        answer //= 5
    if carry:
        digits.append(carry)
    digits = ["-" if x == -1 else "=" if x == -2 else str(x) for x in digits]
    return "".join(reversed(digits))


def part_2(data):
    return "winner!"


def main():
    data = aocd.get_data(day=25, year=2022).splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
