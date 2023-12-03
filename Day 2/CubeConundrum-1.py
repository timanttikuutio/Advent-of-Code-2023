with open("Cube-Conundrum-input.txt", "r") as fp:
    data = fp.readlines()

total = 0

for line in data:
    game_id = int(line.split("Game")[1].split(":")[0])
    values = []

    # print(line.split(":")[1].split(";"))

    for index, cubeset in enumerate(line.split(": ")[1].split("; ")):
        values.append({"red": 0, "green": 0, "blue": 0})

        for value in cubeset.split(", "):
            cubevalue, color = value.split(" ")

            if not values[index].get(color.strip("\n")):
                values[index][color.strip("\n")] = 0

            values[index][color.strip("\n")] += int(cubevalue)

    if all(True if i["red"] <= 12 and i["green"] <= 13 and i["blue"] <= 14 else False for i in values):
        total += game_id

print(total)