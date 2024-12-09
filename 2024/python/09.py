import heapq
import aocd
import utils

import itertools


def part_1(data: utils.Input):
    cur_id = itertools.count()
    ptr = 0
    filesystem = []
    blanks = []
    for i, n in enumerate(data[0]):
        n = int(n)
        if i % 2 == 0:
            filesystem.extend(itertools.repeat(next(cur_id), n))
        else:
            blanks.extend(range(ptr, ptr + int(n)))
        ptr += n

    for b in blanks:
        filesystem.insert(b, filesystem.pop())

    return sum(i * n for i, n in enumerate(filesystem))


def part_2(data: utils.Input):
    cur_id = itertools.count()
    ptr = 0
    filesystem = []
    blanks = []

    for i, n in enumerate(data[0]):
        n = int(n)
        if i % 2 == 0:
            filesystem.append((next(cur_id), n, ptr))
        else:
            blanks.append((ptr, n))
        ptr += n

    r = list(reversed(filesystem))
    answer = 0
    while blanks and r:
        ptr, size = blanks.pop(0)
        idx = next((i for i, (_, n, fptr) in enumerate(r) if fptr > ptr and n <= size), None)
        if idx is None:
            fid, n, fptr = r.pop()
            answer += sum(i * fid for i in range(fptr, fptr + n))
            continue
        fid, n, _ = r.pop(idx)
        answer += sum(i * fid for i in range(ptr, ptr + n))
        if n < size:
            blanks.insert(0, (ptr + n, size - n))

    return answer


def main():
    data = [x for x in aocd.get_data(day=9, year=2024).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
