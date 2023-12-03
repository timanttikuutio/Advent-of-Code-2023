with open("Cube-Conundrum-input.txt", "r") as fp:
    data = fp.readlines()

total = 0

for line in data:
    values = {
        "red": [],
        "green": [],
        "blue": []
    }

    for index, cubeset in enumerate(line.split(": ")[1].split("; ")):
        for value in cubeset.split(", "):
            cubevalue, colour = value.split(" ")

            values[colour.strip("\n")].append(int(cubevalue))

    for i in values:
        values[i].sort(reverse=True)

    total += (values["red"][0] * values["green"][0] * values["blue"][0])

print(total)
