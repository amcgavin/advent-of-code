import re

import aocd

cd_cmd = re.compile(r"\$ cd (.+)")
ls_cmd = re.compile(r"\$ ls")
filesize = re.compile(r"(\d+) .*")


def get_sizes(data):
    current_dir = ""
    directories = {"": 0}
    for line in data:
        if ls_cmd.match(line):
            if current_dir not in directories:
                directories[current_dir] = 0
        if m := filesize.match(line):
            paths = current_dir.split("/")
            for i in range(len(paths)):
                directories["/".join(paths[: i + 1])] += int(m.groups()[0])
        if m := cd_cmd.match(line):
            directory = m.groups()[0]
            if directory == "..":
                current_dir = current_dir.rsplit("/", 1)[0]
            elif directory == "/":
                current_dir = ""
            else:
                current_dir = f"{current_dir}/{directory}"

    return directories


def part_1(data):
    sizes = get_sizes(data)
    return sum(v for v in sizes.values() if v <= 100000)


def part_2(data):
    sizes = get_sizes(data)
    return min(v for v in sizes.values() if v > sizes[""] - 40000000)


def main():
    data = [x for x in aocd.get_data(day=7, year=2022).splitlines()]
    print(part_1(data))
    print(part_2(data))


if __name__ == "__main__":
    main()
