import itertools
from collections import defaultdict
import sys
import aocd
from parse import parse


def part_1(data):
    bricks = {}
    rev_bricks = {}
    max_x = max_y = max_z = 0
    for i, line in enumerate(data):
        x1, y1, z1, x2, y2, z2 = parse("{:d},{:d},{:d}~{:d},{:d},{:d}", line)
        max_x = max(max_x, x2)
        max_y = max(max_y, y2)
        max_z = max(max_z, z2)
        assert x1 <= x2
        assert y1 <= y2
        assert z1 <= z2
        b = []
        for j in range(x1, x2 + 1):
            for k in range(y1, y2 + 1):
                for l in range(z1, z2 + 1):
                    b.append((j, k, l))
        rev_bricks[i] = b
        for j in b:
            bricks[j] = i

    supports = defaultdict(set)
    is_supporting = defaultdict(set)
    free = set()
    for i, values in rev_bricks.items():
        is_free = True
        cmz = max_z + 1
        for coord in values:
            for z in range(coord[2] + 1, cmz):
                if (supporting := bricks.get((coord[0], coord[1], z), i)) != i:
                    is_free = False
                    supports[supporting].add(i)
                    is_supporting[i].add(supporting)
                    cmz = z
                    break
        if is_free:
            free.add(i)
    for i, supporting in supports.items():
        winners = set()
        winner = 0
        for s in supporting:
            mz = max(z for x, y, z in rev_bricks[s])
            if mz > winner:
                winner = mz
                winners = {s}
            elif mz == winner:
                winners.add(s)
        losers = supporting - winners
        supporting.clear()
        supporting.update(winners)
        for loser in losers:
            is_supporting[loser].remove(i)
            if not is_supporting[loser]:
                free.add(loser)

    for i, values in is_supporting.items():
        if all(len(supports[j]) > 1 for j in values):
            free.add(i)

    zy = {(y, z): c for (x, y, z), c in bricks.items()}
    zx = {(x, z): c for (x, y, z), c in bricks.items()}
    for z in range(max_z, -1, -1):
        for y in range(max_y + 1):
            c = zy.get((y, z))
            if c is None:
                sys.stdout.write("    ")
            else:
                sys.stdout.write(f"{c:04x}X" if c in free else f"{c:04x}#")

        sys.stdout.write(" | ")
        for x in range(max_x + 1):
            c = zx.get((x, z))
            if c is None:
                sys.stdout.write("    ")
            else:
                sys.stdout.write(f"{c:04x}X" if c in free else f"{c:04x}#")
        sys.stdout.write("\n")
    return len(free)


def part_2(data):
    return 0


sample = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""


def main():
    data = [x for x in aocd.get_data(day=22, year=2023).splitlines()]
    data = sample.splitlines()
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
