import re


# codes_list is just a multi-line string of the codes,
# I was too lazy to create a file and load that, lol.
with open("Trebuchet-input.txt", "r") as fp:
    codes_list = fp.readlines()


def string2int(input: str) -> str:
    if input.isnumeric():
        return str(input)

    letters = {
        "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9
    }

    return str(letters[input])


regex_match = "[1-9]|(?:one)|(?:two)|(?:three)|(?:four)|(?:five)|(?:six)|(?:seven)|(?:eight)|(?:nine)"

sum = 0
total = 0
matches = ["[0-9]", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for index, line in enumerate(codes_list):
    numbers = re.findall(f"(?=({'|'.join(matches)}))", line) # returns a list of all the matches
    first = numbers[0] if numbers[0].isdigit() else matches.index(numbers[0]) #
    second = numbers[len(numbers) - 1] if numbers[len(numbers) - 1].isdigit() else matches.index(
        numbers[len(numbers) - 1])

    tim_match = re.findall(regex_match, line)
    tim_first, tim_last = string2int(tim_match[0]), string2int(tim_match[-1])

    if str(first) != str(tim_first):
        print(f"no match at index {index}: tim first: {tim_first}, rob first: {first}")
    if str(second) != str(tim_last):
        print(f"no match at index {index}: tim first: {tim_last}, rob first: {second}")

    total += int(tim_first + tim_last)
    sum += int(f"{first}{second}")

print(f"Task 2: {sum}")



print(f"Total value: {total}")
