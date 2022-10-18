

import os
import sys
valid_lines = []
corrupt_lines = []


def validate_data(line):

    # TYPE YOUR SOLUTION CODE HERE
    items = line.split(",")
    datum = items[3].split("-")
    rij = []
    if len(items[0]) != 7:
        rij.append(items[0])
    elif items[0][:2] != "08" and items[0][:2] != "09":
        rij.append(items[0])
    if not items[1].isalpha():
        rij.append(items[1])
    if not items[2].isalpha():
        rij.append(items[2])
    if "-" in items[3]:
        if int(datum[0]) < 1960 or int(datum[0]) > 2004:
            rij.append(items[3])
        if int(datum[1]) < 1 or int(datum[1]) > 12:
            rij.append(items[3])
        if int(datum[2]) < 1 or int(datum[2]) > 31:
            rij.append(items[3])
    else:
        rij.append(items[3])
    if items[4] != "INF" and items[4] != "TINF" and items[4] != "CMD" and items[4] != "AI":
        rij.append(items[4])
    if rij != []:
        output = "".join(line) + f" => INVALID DATA: {rij}"
        corrupt_lines.append(output)
    if rij == []:
        valid_lines.append(line)


def main(csv_file):
    with open(os.path.join(sys.path[0], csv_file), newline='') as csv_file:
        next(csv_file)
        for line in csv_file:
            validate_data(line.strip())
    print('### VALID LINES ###')
    print("\n".join(valid_lines))
    print('### CORRUPT LINES ###')
    print("\n".join(corrupt_lines))


if __name__ == "__main__":
    main('students.csv')


if __name__ == "__main__":main('students.csv')

