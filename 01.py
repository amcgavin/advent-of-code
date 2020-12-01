def part_1():
    # we'll attempt to fit in all into memory
    inputs = set()
    with open("./01.txt", mode="r") as fp:
        for line in fp.readlines():
            i = int(line.strip())
            # since we're working with 2 numbers it's easy to figure out what number we're looking for
            # if we've seen it, that's the answer!
            if 2020 - i in inputs:
                return f"{i}, {2020 - i} = {i * (2020 - i)}"
            inputs.add(i)


def part_2():
    # not as nice, but can do in O(n^2)
    inputs = set()

    # for the problem 2020 - i - j = k:
    # maintain a set of (2020 - i - j)
    targets = {}
    with open("./01.txt", mode="r") as fp:
        for line in fp.readlines():
            i = int(line.strip())
            if i in targets:
                j, k = targets[i]
                return f"{i}, {j}, {k} = {i * j * k}"

            for j in inputs:
                targets[2020 - i - j] = (i, j)
            inputs.add(i)


if __name__ == "__main__":
    print(part_1())
    print(part_2())
