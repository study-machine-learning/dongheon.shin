import random


def calculate_bmi(height, weight):

    bmi = weight / (height / 100) ** 2

    if bmi < 18.5:
        return "thin"
    if bmi < 25:
        return "normal"

    return "fat"


with open("bmi.csv", "w", encoding="utf-8") as fp:

    fp.write("height,weight,label\n")

    count = {"thin": 0, "normal": 0, "fat": 0}

    for index in range(20000):

        height = random.randint(120, 200)
        weight = random.randint(35, 80)

        label = calculate_bmi(height, weight)

        count[label] += 1

        fp.write("{0},{1},{2}\n".format(height, weight, label))

    print("result = ", count)
