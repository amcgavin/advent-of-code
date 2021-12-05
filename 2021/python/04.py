import itertools
from collections import defaultdict

import aocd


def chunk_iterable(iterable, size):
    fill_value = object()
    chunks = [iter(iterable)] * size
    for chunk in itertools.zip_longest(*chunks, fillvalue=fill_value):
        yield (i for i in chunk if i is not fill_value)


def parse_boards(data):
    for i, chunk in enumerate(chunk_iterable(data, 6)):
        tiles = list(chunk)
        tiles.pop(0)
        rows = [row.split() for row in tiles]
        yield from [(i, row, "ROW") for row in rows]
        yield from [(i, col, "COL") for col in zip(*rows)]


def part_1(numbers, boards):
    board_backrefs = defaultdict(list)
    board_refs = defaultdict(list)
    board_markings = {}
    numbers_seen = set()
    for i, (board_no, tiles, orientation) in enumerate(boards):
        if orientation == "ROW":
            board_refs[board_no].extend(tiles)
        board_markings[i] = [None for _ in tiles]
        for tile in tiles:
            board_backrefs[tile].append((i, board_no))

    for number in numbers:
        numbers_seen.add(number)
        for board_id, board_no in board_backrefs.get(number, []):
            board_markings[board_id].pop()
            if len(board_markings[board_id]) == 0:
                return int(number) * sum(
                    [int(tile) for tile in board_refs[board_no] if tile not in numbers_seen]
                )


def part_2(numbers, boards):
    board_backrefs = defaultdict(list)
    board_refs = defaultdict(list)
    board_markings = {}
    numbers_seen = set()
    for i, (board_no, tiles, orientation) in enumerate(boards):
        if orientation == "ROW":
            board_refs[board_no].extend(tiles)
        board_markings[i] = [None for _ in tiles]
        for tile in tiles:
            board_backrefs[tile].append((i, board_no))

    for number in numbers:
        numbers_seen.add(number)
        for board_id, board_no in board_backrefs.get(number, []):
            if board_no not in board_refs:
                continue
            board_markings[board_id].pop()
            if len(board_markings[board_id]) == 0:
                board = board_refs.pop(board_no)
                if not board_refs:
                    return int(number) * sum(
                        [int(tile) for tile in board if tile not in numbers_seen]
                    )


def main():
    data = aocd.get_data(day=4, year=2021).splitlines()
    numbers = data.pop(0).split(",")
    boards = list(parse_boards(data))

    print(part_1(numbers, boards))
    print(part_2(numbers, boards))


if __name__ == "__main__":
    main()
