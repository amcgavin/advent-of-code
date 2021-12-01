import re


def get_input():
    with open("./04.txt", mode="r") as fp:
        for line in fp.readlines():
            yield line.strip()
        yield ""


hcl_re = re.compile(r"#[0-9a-f]{6}")
ecl_re = re.compile(r"(amb|blu|brn|gry|grn|hzl|oth)")
hgt_re = re.compile(r"(?P<height>\d+)(?P<unit>cm|in)")


def height_validator(x):
    match = hgt_re.match(x)
    if not match:
        return False
    d = match.groupdict()
    if d["unit"] == "cm":
        return 150 <= int(d["height"]) <= 193
    else:
        return 59 <= int(d["height"]) <= 76


def is_int(x):
    try:
        int(x)
        return True
    except (TypeError, ValueError):
        return False


validators = {
    "byr": lambda x: is_int(x) and 1920 <= int(x) <= 2002,
    "iyr": lambda x: is_int(x) and 2010 <= int(x) <= 2020,
    "eyr": lambda x: is_int(x) and 2020 <= int(x) <= 2030,
    "hgt": height_validator,
    "hcl": lambda x: hcl_re.match(x) is not None,
    "ecl": lambda x: ecl_re.match(x) is not None,
    "pid": lambda x: is_int(x) and len(x) == 9,
}


def part1():
    valid = 0
    current = {}
    for line in get_input():
        for section in line.split(" "):
            key, _, value = section.partition(":")
            current[key] = value
        if line == "":
            if all(c in current.keys() for c in validators.keys()):
                valid += 1
            current = {}
    return valid


def part2():
    valid = 0
    current = {}
    for line in get_input():
        for section in line.split(" "):
            key, _, value = section.partition(":")
            current[key] = value
        if line == "":
            is_valid = True
            for key, validator in validators.items():
                if key not in current:
                    is_valid = False
                    break
                if not validator(current[key]):
                    is_valid = False
                    break
            if is_valid:
                valid += 1
            current = {}
    return valid


if __name__ == "__main__":
    print(part1())
    print(part2())
