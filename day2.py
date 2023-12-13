from enum import Enum


def print_solution_day_2_part_1():
    # Print the solution for day 2 part 1 of the Advent of Code
    file2 = open("2.txt", "r")
    count = 0
    total = 0
    for x in file2.readlines():
        possible = True
        count += 1
        x = x.split(":", 1)[1]
        line = x.split(";")
        for y in line:
            z = y.split(",")
            for a in z:
                for col in Colors:
                    if a.find(col.name) > 0:
                        a = a.replace(col.name, "")
                        if col.value == "r" and int(a) > 12:
                            possible = False
                        if col.value == "g" and int(a) > 13:
                            possible = False
                        if col.value == "b" and int(a) > 14:
                            possible = False
        if possible:
            total += count
    print("Answer for day 2 part 1:")
    print(total)


def print_solution_day_2_part_2():
    # Print the solution for day 2 part 2 of the Advent of Code
    file2 = open("2.txt", "r")
    total = 0
    for x in file2.readlines():
        r = 0
        g = 0
        b = 0
        x = x.split(":", 1)[1]
        line = x.split(";")
        for y in line:
            z = y.split(",")
            for a in z:
                for col in Colors:
                    if a.find(col.name) > 0:
                        a = a.replace(col.name, "")
                        if col.value == "r" and int(a) > r:
                            r = int(a)
                        if col.value == "g" and int(a) > g:
                            g = int(a)
                        if col.value == "b" and int(a) > b:
                            b = int(a)
        power = r * g * b
        total += power
    print("Answer for day 2 part 2:")
    print(total)


class Colors(Enum):
    red = "r"
    green = "g"
    blue = "b"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_solution_day_2_part_1()
    print_solution_day_2_part_2()
