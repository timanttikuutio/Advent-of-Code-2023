import re

total = 0

regex_match = "[1-9]"

with open("Trebuchet-input.txt", "r") as fp:
    data = fp.readlines()

for line in data:
    match = re.findall(regex_match, line)
    first, last = match[0], match[-1]
    print(f"first: {first}, last: {last}")
    total += int(first + last)

print(f"Total value: {total}")
