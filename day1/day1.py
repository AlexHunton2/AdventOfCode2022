elf = []

with open('day1.txt') as f:
    line = f.readline()
    calories = 0
    while line:
        if (line == "\n"):
            elf.append(calories)
            calories = 0
        else:
            calories += int(line)
        line = f.readline()

first = max(elf)

print("Part 1: {}".format(first)) # part 1

elf.remove(first)
second = max(elf)
elf.remove(second)
third = max(elf)

print("Part 2: {}".format(first + second + third)) # part 1

