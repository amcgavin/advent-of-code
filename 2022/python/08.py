import aocd


def part_1(data):
    count = 0
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if (
                col == 0
                or row == 0
                or col == len(line) - 1
                or row == len(data) - 1
                or max(int(d[col]) for d in data[:row]) < int(char)
                or max(int(d) for d in line[:col]) < int(char)
                or max(int(d[col]) for d in data[row + 1 :]) < int(char)
                or max(int(d) for d in line[col + 1 :]) < int(char)
            ):
                count += 1
    return count


def part_2(data):
    best = 0
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if col == 0 or row == 0 or col == len(line) - 1 or row == len(data) - 1:
                continue
            lcol = col - 1
            while lcol > 0:
                if line[lcol] >= char:
                    break
                lcol -= 1
            rcol = col + 1
            while rcol < len(line) - 1:
                if line[rcol] >= char:
                    break
                rcol += 1
            lrow = row - 1
            while lrow > 0:
                if data[lrow][col] >= char:
                    break
                lrow -= 1
            rrow = row + 1
            while rrow < len(data) - 1:
                if data[rrow][col] >= char:
                    break
                rrow += 1
            best = max(best, (col - lcol) * (rcol - col) * (row - lrow) * (rrow - row))
    return best


def main():
    data = [x for x in aocd.get_data(day=8, year=2022).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
