import re


def string2int(input: str) -> str:
    if input.isnumeric():
        return str(input)

    letters = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }

    return str(letters[input])


total = 0

regex_match = "(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))"

with open("Trebuchet-input.txt", "r") as fp:
    data = fp.readlines()

for line in data:
    match = re.findall(regex_match, line)
    first, last = string2int(match[0]), string2int(match[len(match) - 1])
    print(f"first: {first}, last: {last}")
    total += int(first + last)

print(f"Total value: {total}")
